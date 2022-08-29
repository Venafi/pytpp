import re
from textwrap import dedent
from pathlib import Path
from runpy import run_path
from typing import List
import shutil
from pytpp.api.api_base import ObjectModel

PROJECT_ROOT = Path(__file__).parent.parent
FEATURES_PATH = Path(PROJECT_ROOT, 'pytpp', 'features')
FEATURES_DOC_PATH = Path(PROJECT_ROOT, 'docs', 'rst', 'features')
MODELS_PATH = Path(PROJECT_ROOT, 'pytpp', 'api', 'websdk', 'models')
MODELS_DOC_PATH = Path(PROJECT_ROOT, 'docs', 'rst', 'models')


def make_title(title: str, underline: str = '='):
    return title, (underline * len(title))


def model_rst_template(module: type, model_name: str):
    title, h1 = make_title(model_name, '-')
    return dedent(f"""
    {title}
    {h1}

    .. _{module.__name__}.{title.replace(" ", "_").lower()}_model:
    .. autopydantic_model:: {module.__name__}.{model_name}
    """).lstrip()


def toc_rst_template(title: str, toc_items: List[str], tag: str = 'feature_list'):
    made_title, h1 = make_title(title.replace('_', ' ').title())
    toc_items_rst = '\n\t\t'.join(toc_items)
    return dedent(f"""
    .. _{title.lower()}_{tag}:

    {made_title}
    {h1}

    .. toctree::
        :maxdepth: 1

        {toc_items_rst}
    """.replace('\t', '    ')).lstrip()


def feature_class_rst_template(module_path: str, class_: str):
    title: str = getattr(class_, '__feature__')
    if not title:
        raise AttributeError(f'{class_.__name__} does not have a __feature__ attribute.')
    made_title, h1 = make_title(title)

    return dedent(f"""
    .. _{title.replace(" ", "_").lower()}_feature:

    {made_title}
    {h1}

    .. autoclass:: {module_path}.{class_.__name__}
       :members:
       :undoc-members:
       :show-inheritance:
       :inherited-members:
    """).lstrip()


def get_feature_docs():
    # Recreate the features doc folder.
    shutil.rmtree(path=str(FEATURES_DOC_PATH), ignore_errors=True)
    FEATURES_DOC_PATH.mkdir(exist_ok=True, parents=True)

    features_rst_files = []  # rst/feature/<feature> files to be added to the main features TOC.
    for feature in FEATURES_PATH.glob('*.py'):
        if not feature.is_file() or feature.name.startswith('_'):
            continue

        # Collection feature classes
        classes = run_path(str(feature.absolute()))
        feature_classes = sorted([c for c in classes.values() if hasattr(c, '__feature__')],
                                 key=lambda x: x.__name__)

        # Get the module path for Sphinx's .. autoclass:: directive.
        rel_file_path = Path(classes['__file__']).relative_to(PROJECT_ROOT)
        module_path = Path(str(rel_file_path).replace('/', '.')).stem

        # Create the rst/features/<feature> folder.
        feature_file_path = Path(FEATURES_DOC_PATH, feature.stem)
        feature_file_path.mkdir(exist_ok=True, parents=True)

        def process_class_rst(f_cls):
            # Create the .. autoclass:: rst file.
            rst = feature_class_rst_template(module_path=module_path, class_=f_cls)
            rst_file_name = Path(re.sub("[^a-zA-Z\d]+", "_", f_cls.__feature__).lower() + '.rst')
            rst_file_path = Path(feature_file_path, rst_file_name)  # rst/features/<feature>/<feature_class>.rst
            with rst_file_path.open('w') as ff:
                ff.write(rst)
            return rst_file_path  # <feature_class>

        if len(feature_classes) > 1:
            # Stores all class rst files for each class in a feature file with @feature().
            feature_class_rst_files = []

            # Create the feature class rst files.
            for feature_class in feature_classes:
                feature_class_rst_files.append(process_class_rst(feature_class).stem)

            # Create the rst/features/<feature>/<feature>.rst file.
            feature_toc_rst = toc_rst_template(title=feature.stem, toc_items=feature_class_rst_files)
            feature_rst_file = Path(feature_file_path, f'{feature.stem}_toc.rst')
            with feature_rst_file.open('w') as f:
                f.write(feature_toc_rst)
            features_rst_files.append(feature_rst_file)
        else:
            features_rst_files.append(process_class_rst(feature_classes[0]))
    pytpp_features_rst = toc_rst_template(
        title='Features',
        toc_items=[f'{f.parent.name}/{f.stem}' for f in sorted(features_rst_files)]
    )
    pytpp_features_rst = f'.. _features:\n\n{pytpp_features_rst}'
    with Path(FEATURES_DOC_PATH, 'features_toc.rst').open('w') as f:
        f.write(pytpp_features_rst)


def get_property_docs():
    from pytpp.api.websdk import models
    import inspect

    # Recreate the dataclasses doc folder.
    shutil.rmtree(path=str(MODELS_DOC_PATH), ignore_errors=True)
    MODELS_DOC_PATH.mkdir(exist_ok=True, parents=True)

    toc_items = []
    for item in vars(models).values():
        if not inspect.ismodule(item):
            continue
        mod_file = Path(item.__file__)
        title, h1 = make_title(mod_file.stem.replace('_', ' ').title())
        rst_path = Path(MODELS_DOC_PATH, f'{mod_file.stem}.rst')
        objects = run_path(mod_file)
        rst_content = [f'{title}\n{h1}\n']
        for name, obj in sorted(objects.items(), key=lambda x: x[0]):
            if isinstance(obj, type) and issubclass(obj, ObjectModel) and obj is not ObjectModel:
                rst_content.append(model_rst_template(item, obj.__name__))
        with rst_path.open('w') as dm:
            dm.write('\n'.join(rst_content))
        toc_items.append(rst_path.stem)
    models_toc_rst_content = toc_rst_template('Models', toc_items, tag='models')
    with Path(MODELS_DOC_PATH, 'models_toc.rst').open('w') as pd:
        pd.write(models_toc_rst_content)


def main():
    print('\n\n\n############RECOMPILING FEATURES AND PROPERTIES!!!############\n\n\n')
    get_feature_docs()
    get_property_docs()


if __name__ == '__main__':
    main()

