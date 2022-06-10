import logging
import inspect
import jsonpickle
import re
import simplejson
import threading
from contextlib import contextmanager
from functools import wraps
from pathlib import Path
from typing import Any, List, Tuple, Set


class Logger(logging.getLoggerClass()):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._suppressed: Set[Tuple[threading.Thread, int]] = set()
        self._json_pickle_dumps = lambda d: jsonpickle.dumps(d, max_depth=2, unpicklable=False, indent=2)
        self._children: 'List[Logger]' = []
        self.manager.loggerClass = Logger
        self.msg_char_limit = 0
        self._suppressed_lock = threading.Lock()

    def _copy_suppressed(self):
        with self._suppressed_lock:
            copy = self._suppressed.copy()
        return copy

    def _add_suppressed(self, value: Tuple[threading.Thread, int]):
        with self._suppressed_lock:
            self._suppressed.add(value)

    def _remove_suppressed(self, value: Tuple[threading.Thread, int]):
        with self._suppressed_lock:
            self._suppressed.remove(value)

    def _log(self, level, msg, args, exc_info=None, truncate=True, **kwargs) -> None:
        current_thread = threading.current_thread()
        for s_thread, s_level in self._copy_suppressed():
            if s_thread == current_thread and level < s_level:
                return
        if truncate and not exc_info and isinstance(self.msg_char_limit, int) and self.msg_char_limit > 0:
            msg = msg[:self.msg_char_limit]
        return super()._log(level, msg, args=args, exc_info=exc_info, **kwargs)

    def debug(self, *args, exc_info=None, stack_info=None, stacklevel=1,
              extra=None, truncate=True, **kwargs: Any) -> None:
        kwargs['truncate'] = truncate
        return super().debug(*args, exc_info=exc_info, stack_info=stack_info,
                             stacklevel=stacklevel + 2, extra=extra, **kwargs)

    def info(self, *args, exc_info=None, stack_info=None, stacklevel=1,
             extra=None, truncate=True, **kwargs: Any) -> None:
        kwargs['truncate'] = truncate
        return super().info(*args, exc_info=exc_info, stack_info=stack_info,
                            stacklevel=stacklevel + 2, extra=extra, **kwargs)

    def warning(self, *args, exc_info=None, stack_info=None, stacklevel=1,
                extra=None, truncate=True, **kwargs: Any) -> None:
        kwargs['truncate'] = truncate
        return super().warning(*args, exc_info=exc_info, stack_info=stack_info,
                               stacklevel=stacklevel + 2, extra=extra, **kwargs)

    def error(self, *args, exc_info=None, stack_info=None, stacklevel=1,
              extra=None, truncate=True, **kwargs: Any) -> None:
        kwargs['truncate'] = truncate
        return super().error(*args, exc_info=exc_info, stack_info=stack_info,
                             stacklevel=stacklevel + 2, extra=extra, **kwargs)

    def critical(self, *args, exc_info=None, stack_info=None, stacklevel=1,
                 extra=None, truncate=True, **kwargs: Any) -> None:
        kwargs['truncate'] = truncate
        return super().critical(*args, exc_info=exc_info, stack_info=stack_info,
                                stacklevel=stacklevel + 2, extra=extra, **kwargs)

    def exception(self, *args, exc_info=True, stack_info=None, stacklevel=1,
                  extra=None, truncate=True, **kwargs: Any) -> None:
        kwargs['truncate'] = truncate
        return super().exception(*args, exc_info=exc_info, stack_info=stack_info,
                                 stacklevel=stacklevel + 2, extra=extra, **kwargs)

    @contextmanager
    def suppressed(self, level: int, include_child_loggers: bool = True):
        thread = threading.current_thread()
        self._add_suppressed((thread, level))
        if include_child_loggers:
            for cl in self._children:
                cl._add_suppressed((thread, level))
        yield
        try:
            self._remove_suppressed((thread, level))
            if include_child_loggers:
                for cl in self._children:
                    cl._remove_suppressed((thread, level))
        except:
            # Don't let this exception stop the running program.
            pass

    def suppress_function(self, level: int, include_child_loggers: bool = True):
        def dec(f):
            @wraps(f)
            def wrap(*args, **kwargs):
                with self.suppressed(level=level, include_child_loggers=include_child_loggers):
                    return f(*args, **kwargs)

            return wrap

        return dec

    def wrap_class(self, level: int, include: str = '', exclude: str = '__.*',
                   *logging_args, **logging_kwargs):
        def wrap(cls):
            for attr, fn in inspect.getmembers(cls, inspect.isroutine):
                if callable(getattr(cls, attr)):
                    if include:
                        matches = re.findall(pattern=include, string=fn.__name__, flags=re.IGNORECASE)
                        if fn.__name__ not in matches:
                            continue
                    if exclude:
                        matches = re.findall(pattern=exclude, string=fn.__name__, flags=re.IGNORECASE)
                        if fn.__name__ in matches:
                            continue
                    setattr(cls, attr, self.wrap_func(
                        level=level, _class=cls, *logging_args, **logging_kwargs
                    )(getattr(cls, attr)))
            return cls

        return wrap

    def wrap_func(self, level: int, _class=None, *logging_args, **logging_kwargs):
        def dec(func):
            if func.__name__.startswith('__'):
                return func

            is_staticmethod = isinstance(inspect.getattr_static(_class, func.__name__, None), staticmethod)
            is_classmethod = isinstance(inspect.getattr_static(_class, func.__name__, None), classmethod)

            unwrapped_func = inspect.unwrap(func)
            extra = {
                '_funcName': unwrapped_func.__qualname__,
                '_lineno'  : unwrapped_func.__code__.co_firstlineno,
                '_filename': Path(unwrapped_func.__code__.co_filename).name,
                '_pathname': unwrapped_func.__code__.co_filename,
                '_module'  : inspect.getmodulename(unwrapped_func.__code__.co_filename)
            }

            @wraps(func)
            def wrap(*args, **kwargs):
                in_msg_dict = {
                    'CALLED': func.__qualname__
                }
                if _class and (is_classmethod or is_staticmethod):
                    args = [a for e, a in enumerate(args) if e > 0]
                if args:
                    in_msg_dict['ARGS'] = args
                if kwargs:
                    in_msg_dict['KWARGS'] = kwargs
                self.log(
                    level=level, msg=self._json_pickle_dumps(in_msg_dict), extra=extra,
                    *logging_args, **logging_kwargs
                )
                try:
                    result = func(*args, **kwargs)
                    out_msg_dict = {
                        'RETURNED': func.__qualname__
                    }
                    if result:
                        out_msg_dict['OUTPUT'] = result
                    self.log(
                        level=level, msg=self._json_pickle_dumps(out_msg_dict), extra=extra,
                        *logging_args, **logging_kwargs
                    )
                    return result
                except:
                    self.exception(f'An error occurred in {extra["_funcName"]}.', extra=extra)
                    raise

            return wrap

        return dec

    def getChild(self, suffix: str) -> 'Logger':
        self.manager.loggerClass = Logger
        child = super().getChild(suffix=suffix)
        self._children.append(child)
        return child


def get_logger(name: str = None) -> Logger:
    _original_global_logging_class = logging.getLoggerClass()
    if not isinstance(_original_global_logging_class, type) or not issubclass(
            _original_global_logging_class, logging.Logger):
        _original_global_logging_class = logging.Logger

    _original_root_manager_logging_class = logging.root.manager.loggerClass
    if not isinstance(_original_root_manager_logging_class, type) or not issubclass(
            _original_root_manager_logging_class, logging.Logger):
        _original_root_manager_logging_class = logging.Logger
    # noinspection PyUnresolvedReferences
    logging._acquireLock()
    try:
        logging.setLoggerClass(Logger)
        logging.root.manager.setLoggerClass(Logger)
        new_logger = logging.getLogger(name=name)
        logging.setLoggerClass(_original_global_logging_class)
        logging.root.manager.setLoggerClass(_original_root_manager_logging_class)
        return new_logger
    finally:
        # noinspection PyUnresolvedReferences
        logging._releaseLock()


logger = get_logger('pytpp')
api_logger = logger.getChild('api')
features_logger = logger.getChild('features')

json_pickler = jsonpickle
json_pickler.set_encoder_options(simplejson.__name__, sort_keys=True, indent=2)
