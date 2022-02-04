from typing import List 
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.config import Config


class _Config:
    def __init__(self, api_obj):
        self.AddDnValue = self._AddDnValue(api_obj=api_obj)
        self.AddPolicyValue = self._AddPolicyValue(api_obj=api_obj)
        self.AddValue = self._AddValue(api_obj=api_obj)
        self.ClearAttribute = self._ClearAttribute(api_obj=api_obj)
        self.ClearPolicyAttribute = self._ClearPolicyAttribute(api_obj=api_obj)
        self.ContainableClasses = self._ContainableClasses(api_obj=api_obj)
        self.Create = self._Create(api_obj=api_obj)
        self.DefaultDN = self._DefaultDN(api_obj=api_obj)
        self.Delete = self._Delete(api_obj=api_obj)
        self.DnToGuid = self._DnToGuid(api_obj=api_obj)
        self.Enumerate = self._Enumerate(api_obj=api_obj)
        self.EnumerateAll = self._EnumerateAll(api_obj=api_obj)
        self.EnumerateObjectsDerivedFrom = self._EnumerateObjectsDerivedFrom(api_obj=api_obj)
        self.EnumeratePolicies = self._EnumeratePolicies(api_obj=api_obj)
        self.Find = self._Find(api_obj=api_obj)
        self.FindObjectsOfClass = self._FindObjectsOfClass(api_obj=api_obj)
        self.FindPolicy = self._FindPolicy(api_obj=api_obj)
        self.GetHighestRevision = self._GetHighestRevision(api_obj=api_obj)
        self.GetRevision = self._GetRevision(api_obj=api_obj)
        self.GuidToDn = self._GuidToDn(api_obj=api_obj)
        self.IdInfo = self._IdInfo(api_obj=api_obj)
        self.IsValid = self._IsValid(api_obj=api_obj)
        self.MutateObject = self._MutateObject(api_obj=api_obj)
        self.Read = self._Read(api_obj=api_obj)
        self.ReadAll = self._ReadAll(api_obj=api_obj)
        self.ReadDn = self._ReadDn(api_obj=api_obj)
        self.ReadDnReferences = self._ReadDnReferences(api_obj=api_obj)
        self.ReadEffectivePolicy = self._ReadEffectivePolicy(api_obj=api_obj)
        self.ReadPolicy = self._ReadPolicy(api_obj=api_obj)
        self.RemoveDnValue = self._RemoveDnValue(api_obj=api_obj)
        self.RemovePolicyValue = self._RemovePolicyValue(api_obj=api_obj)
        self.RenameObject = self._RenameObject(api_obj=api_obj)
        self.Write = self._Write(api_obj=api_obj)
        self.WriteDn = self._WriteDn(api_obj=api_obj)
        self.WritePolicy = self._WritePolicy(api_obj=api_obj)

    class _AddDnValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
                    
            return _Response(response=self._post(data=body))

    class _AddPolicyValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddPolicyValue')

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str, locked: bool):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Class': class_name,
                'Value': value,
                'Locked': locked
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _AddValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value,
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _ClearAttribute(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ClearAttribute')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _ClearPolicyAttribute(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ClearPolicyAttribute')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                'ObjectDN': object_dn,
                'Class': class_name,
                'AttributeName': attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _ContainableClasses(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ContainableClasses')

        def post(self, object_dn: str):
            body = {
                'ObjectDN': object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def class_names(self) -> List[str]:
                    return self._from_json(key='ClassNames')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _CountObjects(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/CountObjects')

        def post(self, object_dn: str, type_name: str, recursive: bool = False, pattern: str = None):
            body = {
                'ObjectDN': object_dn,
                'Type': type_name,
                'Pattern': pattern,
                'Recursive': recursive
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def count(self) -> int:
                    return self._from_json(key='Count')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _Create(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Create')

        def post(self, object_dn: str, class_name: str, name_attribute_list: list):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "NameAttributeList": name_attribute_list
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def object(self):
                    return Config.Object(self._from_json(key='Object'))

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _DefaultDN(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/DefaultDN')

        def post(self, default_dn: str):
            body = {
                'DefaultDN': default_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def default_dn(self) -> str:
                    return self._from_json(key='DefaultDN')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _Delete(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Delete')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _DnToGuid(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/DnToGuid')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn,
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def class_name(self) -> str:
                    return self._from_json(key='ClassName')

                @property
                @api_response_property()
                def guid(self) -> str:
                    return self._from_json(key='GUID')

                @property
                @api_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @api_response_property()
                def hierarchical_guid(self) -> str:
                    return self._from_json(key='HierarchicalGUID')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _Enumerate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Enumerate')

        def post(self, object_dn: str = None, recursive: bool = False, pattern: str = None):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive,
                "Pattern": pattern
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def objects(self):
                    return [Config.Object(obj) for obj in self._from_json(key='Objects')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _EnumerateAll(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumerateAll')

        def post(self, pattern: str):
            body = {
                "Pattern": pattern
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def objects(self):
                    return [Config.Object(obj) for obj in self._from_json(key='Objects')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _EnumerateObjectsDerivedFrom(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumerateObjectsDerivedFrom')

        def post(self, derived_from: str, pattern: str = None, object_dn: str = None):
            body = {
                "ObjectDN": object_dn,
                "DerivedFrom": derived_from,
                "Pattern": pattern
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def objects(self):
                    return [Config.Object(obj) for obj in self._from_json(key='Objects')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _EnumeratePolicies(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumeratePolicies')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def policies(self):
                    return [Config.Policy(obj) for obj in self._from_json(key='Policies')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _Find(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Find')

        def post(self, pattern: str, attribute_names: str = None):
            body = {
                "Pattern": pattern,
                "AttributeNames": attribute_names
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def objects(self):
                    return [Config.Object(obj) for obj in self._from_json(key='Objects')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _FindContainers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindContainers')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def objects(self):
                    return [Config.Object(obj) for obj in self._from_json(key='Objects')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _FindObjectsOfClass(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindObjectsOfClass')

        def post(self, classes: str = None, class_name: str = None, object_dn: str = None, pattern: str = None, recursive: bool = False):
            if not (classes or class_name):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "Classes": classes,
                "Class": class_name,
                'ObjectDN': object_dn,
                'Pattern': pattern,
                'Recursive': recursive
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def objects(self):
                    return [Config.Object(obj) for obj in self._from_json(key='Objects')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _FindPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindPolicy')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json(key='Locked')

                @property
                @api_response_property()
                def policy_dn(self) -> str:
                    return self._from_json(key='PolicyDN')

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _GetHighestRevision(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GetHighestRevision')

        def post(self, object_dn: str, classes: str = None):
            body = {
                "ObjectDN": object_dn,
                'Classes': classes
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _GetRevision(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GetRevision')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _GuidToDn(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GuidToDn')

        def post(self, object_guid: str):
            body = {
                "ObjectGUID": object_guid
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def object_dn(self) -> str:
                    return self._from_json(key='ObjectDN')

                @property
                @api_response_property()
                def class_name(self) -> str:
                    return self._from_json(key='ClassName')

                @property
                @api_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @api_response_property()
                def hierarchical_guid(self) -> str:
                    return self._from_json(key='HierarchicalGUID')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _IdInfo(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/IdInfo')

        def post(self, object_id: str):
            body = {
                "ObjectID": object_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def guid(self) -> str:
                    return self._from_json(key='GUID')

                @property
                @api_response_property()
                def class_name(self) -> str:
                    return self._from_json(key='ClassName')

                @property
                @api_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @api_response_property()
                def hierarchical_guid(self) -> str:
                    return self._from_json(key='HierarchicalGUID')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _IsValid(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/IsValid')

        def post(self, object_dn: str = None, object_guid: str = None):
            if not (object_dn or object_guid):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "ObjectGUID": object_guid,
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def object(self):
                    return Config.Object(self._from_json(key='Object'))

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _MutateObject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/MutateObject')

        def post(self, object_dn: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _Read(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Read')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def object_dn(self) -> str:
                    return self._from_json(key='ObjectDN')

                @property
                @api_response_property()
                def attribute_name(self) -> str:
                    return self._from_json(key='AttributeName')

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _ReadAll(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadAll')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def name_values(self):
                    return [Config.NameValues(nv) for nv in self._from_json(key='NameValues')]

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _ReadDn(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadDn')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _ReadDnReferences(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadDnReferences')

        def post(self, object_dn: str, reference_attribute_name: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "ReferenceAttributeName": reference_attribute_name,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values', return_on_error=list)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _ReadEffectivePolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadEffectivePolicy')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json(key='Locked')

                @property
                @api_response_property()
                def overridden(self) -> bool:
                    return self._from_json(key='Overridden')

                @property
                @api_response_property()
                def policy_dn(self) -> str:
                    return self._from_json(key='PolicyDN')

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _ReadPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadPolicy')

        def post(self, object_dn: str, attribute_name: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Class": class_name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json(key='Locked')

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values', return_on_error=list)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _RemoveDnValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RemoveDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Value": value
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))                    
            
            return _Response(response=self._post(data=body))

    class _RemovePolicyValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RemovePolicyValue')

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Class": class_name,
                "Value": value
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _RenameObject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RenameObject')

        def post(self, object_dn: str, new_object_dn: str):
            body = {
                "ObjectDN": object_dn,
                "NewObjectDN": new_object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _Write(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Write')

        def post(self, object_dn: str, attribute_data: dict):
            body = {
                "ObjectDN": object_dn,
                "AttributeData": attribute_data
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _WriteDn(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/WriteDn')

        def post(self, object_dn: str, attribute_name: str, values: List[str]):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Values": values
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))

    class _WritePolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/WritePolicy')

        def post(self, object_dn: str, class_name: str, attribute_name: str, locked: bool = False, values: str = None):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name,
                "Locked": locked,
                "Values": values
            }
            
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(response=self._post(data=body))
