from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.flow import Flow
from pytpp.properties.response_objects.codesign import CodeSign
from typing import List


class _Flow:
    def __init__(self, api_obj):
        self.Actions = self._Actions(api_obj=api_obj)
        self.Tickets = self._Tickets(api_obj=api_obj)

    class _Actions:
        def __init__(self, api_obj):
            self.CodeSign = self._CodeSign(api_obj=api_obj)

        class _CodeSign:
            def __init__(self, api_obj):
                self.PreQualify = self._PreQualify(api_obj=api_obj)

            class _PreQualify:
                def __init__(self, api_obj):
                    self.Create = self._Create(api_obj=api_obj)

                class _Create(API):
                    def __init__(self, api_obj):
                        super().__init__(api_obj=api_obj, url='Flow/Actions/CodeSign/PreQualify/Create')

                    def post(self, comment: str, data: str, dn: str, user: str, hours: int = None,
                             single_use: bool = None):
                        body = {
                            'Comment': comment,
                            'Data': data,
                            'Dn': dn,
                            'Hours': hours,
                            'SingleUse': single_use,
                            'User': user
                        }

                        class _Response(APIResponse):
                            def __init__(self, response):
                                super().__init__(response=response)

                            @property
                            @api_response_property()
                            def error(self) -> str:
                                return self._from_json(key='Error')

                            @property
                            @api_response_property()
                            def result(self):
                                return CodeSign.ResultCode(self._from_json(key='Result'))

                            @property
                            @api_response_property()
                            def success(self) -> bool:
                                return self._from_json(key='Success')

                        return _Response(response=self._post(data=body))

    class _Tickets:
        def __init__(self, api_obj):
            self.Approve = self._Approve(api_obj=api_obj)
            self.Count = self._Count(api_obj=api_obj)
            self.CountApproved = self._CountApproved(api_obj=api_obj)
            self.Enumerate = self._Enumerate(api_obj=api_obj)
            self.EnumerateApproved = self._EnumerateApproved(api_obj=api_obj)
            self.Load = self._Load(api_obj=api_obj)
            self.Reject = self._Reject(api_obj=api_obj)
            self.Update = self._Update(api_obj=api_obj)

        class _Approve(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Approve')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None, expires: str = None,
                     comment: str = None, not_before: str = None, use_count: int = None):
                body = {
                    'Expires'  : expires,
                    'Comment'  : comment,
                    'notBefore': not_before,
                    'TicketId' : ticket_id,
                    'TicketIds': ticket_ids,
                    'useCount' : use_count
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                return _Response(response=self._post(data=body))

        class _Count(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Count')

            def post(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def count(self) -> int:
                        return self._from_json(key='Count')

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                return _Response(response=self._post(data={}))

        class _CountApproved(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/CountApproved')

            def post(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def count(self) -> int:
                        return self._from_json(key='Count')

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                return _Response(response=self._post(data={}))

        class _Enumerate(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Enumerate')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @api_response_property()
                    def tickets(self):
                        return [Flow.Ticket(ticket) for ticket in self._from_json(key='Tickets')]

                return _Response(response=self._post(data=body))

        class _EnumerateApproved(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/EnumerateApproved')

            def post(self, product_code: int = None, ticket_page_size: int = None, ticket_page_number: int = None):
                body = {
                    'ProductCode'     : product_code,
                    'TicketPageSize'  : ticket_page_size,
                    'TicketPageNumber': ticket_page_number
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @api_response_property()
                    def tickets(self):
                        return [Flow.Ticket(ticket) for ticket in self._from_json(key='Tickets')]

                return _Response(response=self._post(data=body))

        class _Load(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Load')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None):
                body = {
                    'TicketId' : ticket_id,
                    'TicketIds': ticket_ids
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @api_response_property()
                    def tickets(self):
                        return [Flow.Ticket(ticket) for ticket in self._from_json(key='Tickets')]

                return _Response(response=self._post(data=body))

        class _Reject(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Reject')

            def post(self, comment: str, rejection_level: int, ticket_id: int = None,
                     ticket_ids: List[int] = None):
                body = {
                    'Comment'       : comment,
                    'RejectionLevel': rejection_level,
                    'TicketId'      : ticket_id,
                    'TicketIds'     : ticket_ids
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def invalid_ticket_ids(self) -> List[int]:
                        return self._from_json(key='InvalidTicketIds')

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                return _Response(response=self._post(data=body))

        class _Update(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Flow/Tickets/Update')

            def post(self, ticket_id: int = None, ticket_ids: List[int] = None, expires: str = None,
                     comment: str = None, not_before: str = None, use_count: int = None):
                body = {
                    'Expires'  : expires,
                    'Comment'  : comment,
                    'notBefore': not_before,
                    'TicketId' : ticket_id,
                    'TicketIds': ticket_ids,
                    'useCount' : use_count
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Flow.Result(self._from_json(key='Result'))

                    @property
                    @api_response_property()
                    def message(self) -> str:
                        return self._from_json(key='Message')

                return _Response(response=self._post(data=body))
