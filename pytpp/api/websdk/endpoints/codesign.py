from typing import List, Dict, Union
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.codesign import CodeSign


class _Codesign:
    def __init__(self, api_obj):
        self.AddAdministrator = self._AddAdministrator(api_obj=api_obj)
        self.AddApplicationAdministrator = self._AddApplicationAdministrator(api_obj=api_obj)
        self.AddProjectAdministrator = self._AddProjectAdministrator(api_obj=api_obj)
        self.AddProjectApprover = self._AddProjectApprover(api_obj=api_obj)
        self.CountReferences = self._CountReferences(api_obj=api_obj)
        self.CreateApplication = self._CreateApplication(api_obj=api_obj)
        self.CreateApplicationCollection = self._CreateApplicationCollection(api_obj=api_obj)
        self.CreateEnvironment = self._CreateEnvironment(api_obj=api_obj)
        self.CreateProject = self._CreateProject(api_obj=api_obj)
        self.CreateTemplate = self._CreateTemplate(api_obj=api_obj)
        self.DeleteApplication = self._DeleteApplication(api_obj=api_obj)
        self.DeleteApplicationCollection = self._DeleteApplicationCollection(api_obj=api_obj)
        self.DeleteEnvironment = self._DeleteEnvironment(api_obj=api_obj)
        self.DeleteProject = self._DeleteProject(api_obj=api_obj)
        self.DeleteTemplate = self._DeleteTemplate(api_obj=api_obj)
        self.EnumerateApplications = self._EnumerateApplications(api_obj=api_obj)
        self.EnumerateApplicationCollections = self._EnumerateApplicationCollections(api_obj=api_obj)
        self.EnumerateProjects = self._EnumerateProjects(api_obj=api_obj)
        self.EnumerateReferences = self._EnumerateReferences(api_obj=api_obj)
        self.EnumerateTemplates = self._EnumerateTemplates(api_obj=api_obj)
        self.GetApplication = self._GetApplication(api_obj=api_obj)
        self.GetApplicationCollection = self._GetApplicationCollection(api_obj=api_obj)
        self.GetApplicationCollectionMembers = self._GetApplicationCollectionMembers(api_obj=api_obj)
        self.GetApplicationCollectionMemberDNs = self._GetApplicationCollectionMemberDNs(api_obj=api_obj)
        self.GetEnvironment = self._GetEnvironment(api_obj=api_obj)
        self.GetGlobalConfiguration = self._GetGlobalConfiguration(api_obj=api_obj)
        self.GetObjectRights = self._GetObjectRights(api_obj=api_obj)
        self.GetRight = self._GetRight(api_obj=api_obj)
        self.GetTemplate = self._GetTemplate(api_obj=api_obj)
        self.GetTrusteeRights = self._GetTrusteeRights(api_obj=api_obj)
        self.RemoveAdministrator = self._RemoveAdministrator(api_obj=api_obj)
        self.RemoveApplicationAdministrator = self._RemoveApplicationAdministrator(api_obj=api_obj)
        self.RemoveProjectAdministrator = self._RemoveProjectAdministrator(api_obj=api_obj)
        self.RenameApplication = self._RenameApplication(api_obj=api_obj)
        self.RenameApplicationCollection = self._RenameApplicationCollection(api_obj=api_obj)
        self.RenameProject = self._RenameProject(api_obj=api_obj)
        self.RenameTemplate = self._RenameTemplate(api_obj=api_obj)
        self.SetGlobalConfiguration = self._SetGlobalConfiguration(api_obj=api_obj)
        self.UpdateApplication = self._UpdateApplication(api_obj=api_obj)
        self.UpdateApplicationCollection = self._UpdateApplicationCollection(api_obj=api_obj)
        self.UpdateEnvironment = self._UpdateEnvironment(api_obj=api_obj)
        self.UpdateProject = self._UpdateProject(api_obj=api_obj)
        self.UpdateProjectStatus = self._UpdateProjectStatus(api_obj=api_obj)
        self.UpdateTemplate = self._UpdateTemplate(api_obj=api_obj)

    class _AddAdministrator(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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

    class _AddApplicationAdministrator(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddApplicationAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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

    class _AddProjectAdministrator(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddProjectAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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

    class _AddProjectApprover(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddProjectApprover')
            
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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
        

    class _AddPreApproval(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddPreApproval')

        def post(self, dn: str, comment: str, user: str, hours: int = None, ip_address: str = None,
                 signing_executable: str = None, single_use: bool = None):
            body = {
                'Dn': dn,
                'Comment': comment,
                'Hours': hours,
                'IPAddress': ip_address,
                'SigningExecutable': signing_executable,
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

    class _CountReferences(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CountReferences')

        def post(self, application: dict = None, application_collection: dict = None):
            body = {
                'Application': application,
                'ApplicationCollection': application_collection
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

    class _CreateApplication(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateApplication')

        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def application(self):
                    return CodeSign.Application(self._from_json(key='Application'))

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

    class _CreateApplicationCollection(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateApplicationCollection')

        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def application(self):
                    return CodeSign.ApplicationCollection(self._from_json(key='ApplicationCollection'))

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

    class _CreateEnvironment(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateEnvironment')

        def post(self, dn: str, environment_name: str, project: Dict[str, Union[str, int]],
                 template: List[Dict[str, str]], template_dn: str = None):
            body = {
                'Dn': dn,
                'EnvironmentName': environment_name,
                'Project': project,
                'Template': template,
                'TemplateDn': template_dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def apple_environment(self) -> str:
                    return CodeSign.AppleEnvironment(self._from_json(key='AppleEnvironment'))

                @property
                @api_response_property()
                def csp_environment(self) -> str:
                    return CodeSign.CSPEnvironment(self._from_json(key='CSPEnvironment'))

                @property
                @api_response_property()
                def dot_net_environment(self) -> str:
                    return CodeSign.DotNetEnvironment(self._from_json(key='DotNetEnvironment'))

                @property
                @api_response_property()
                def gpg_environment(self) -> str:
                    return CodeSign.GPGEnvironment(self._from_json(key='GPGEnvironment'))

                @property
                @api_response_property()
                def key_pair_environment(self) -> str:
                    return CodeSign.KeyPairEnvironment(self._from_json(key='KeyPairEnvironment'))

                @property
                @api_response_property()
                def apple_template(self) -> str:
                    return CodeSign.AppleTemplate(self._from_json(key='AppleTemplate'))

                @property
                @api_response_property()
                def csp_template(self) -> str:
                    return CodeSign.CSPTemplate(self._from_json(key='EnviCSPTemplateronment'))

                @property
                @api_response_property()
                def dot_net_template(self) -> str:
                    return CodeSign.DotNetTemplate(self._from_json(key='DotNetTemplate'))

                @property
                @api_response_property()
                def gpg_template(self) -> str:
                    return CodeSign.GPGTemplate(self._from_json(key='GPGTemplate'))

                @property
                @api_response_property()
                def key_pair_environment(self) -> str:
                    return CodeSign.KeyPairTemplate(self._from_json(key='KeyPairTemplate'))

                @property
                @api_response_property()
                def result(self):
                    return CodeSign.ResultCode(self._from_json(key='Result'))

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _CreateProject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateProject')

        def post(self, dn: str):
            body = {
                'Dn': dn
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
                def project(self):
                    return CodeSign.Project(self._from_json(key='Project'))

                @property
                @api_response_property()
                def result(self):
                    return CodeSign.ResultCode(self._from_json(key='Result'))

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _CreateTemplate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateTemplate')

        def post(self, dn: str, template_type: str, per_user: bool):
            body = {
                'Dn': dn,
                'TemplateType': template_type,
                'PerUser': per_user
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def certificate_template(self):
                    return CodeSign.CertificateTemplate(self._from_json(key='CertificateTemplate'))

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

    class _DeleteApplication(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteApplication')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id
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

    class _DeleteApplicationCollection(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteApplicationCollection')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
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

    class _DeleteEnvironment(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteEnvironment')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id
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

    class _DeleteProject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteProject')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
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

    class _DeleteTemplate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteTemplate')

        def post(self, dn: str = None, force: bool = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Force': force,
                'Guid': guid,
                'Id': id
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

    class _EnumerateApplications(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateApplications')

        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def applications(self):
                    return [
                        CodeSign.Application(a) for a in self._from_json(key='Applications')
                    ]

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

    class _EnumerateApplicationCollections(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateApplicationCollections')

        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def application_collections(self):
                    return [
                        CodeSign.ApplicationCollection(ac)
                        for ac in self._from_json(key='ApplicationCollections')
                    ]

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

    class _EnumerateProjects(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateProjects')

        def post(self, filter: str = None, rights: int = None):
            body = {
                'Filter': filter,
                'Rights': rights
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
                def projects(self):
                    return [CodeSign.Project(p) for p in self._from_json(key='Projects')]

                @property
                @api_response_property()
                def result(self):
                    return CodeSign.ResultCode(self._from_json(key='Result'))

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _EnumerateReferences(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateReferences')

        def post(self, application: dict = None, application_collection: dict = None,
                 application_dn: str = None, application_guid: str = None,
                 collection_dn: str = None, collection_guid: str = None):
            body = {
                'Application': application,
                'ApplicationCollection': application_collection,
                'ApplicationDn': application_dn,
                'ApplicationGuid': application_guid,
                'CollectionDn': collection_dn,
                'CollectionGuid': collection_guid
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
                def reference_dns(self) -> List[str]:
                    return self._from_json(key='ReferenceDNs')

                @property
                @api_response_property()
                def result(self):
                    return CodeSign.ResultCode(self._from_json(key='Result'))

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')


            return _Response(response=self._post(data=body))

    class _EnumerateTemplates(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateTemplates')

        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def certificate_templates(self):
                    return [
                        CodeSign.CertificateTemplate(t)
                        for t in self._from_json(key='CertificateTemplates')
                    ]

                @property
                @api_response_property()
                def csp_templates(self):
                    return [
                        CodeSign.CSPTemplate(t)
                        for t in self._from_json(key='CSPTemplates')
                    ]

                @property
                @api_response_property()
                def dot_net_templates(self):
                    return [
                        CodeSign.DotNetTemplate(t)
                        for t in self._from_json(key='DotNetTemplates')
                    ]

                @property
                @api_response_property()
                def gpg_templates(self):
                    return [
                        CodeSign.GPGTemplate(t)
                        for t in self._from_json(key='GPGTemplates')
                    ]

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

    class _GetApplication(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplication')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def application(self):
                    return CodeSign.Application(self._from_json(key='Application'))

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

    class _GetApplicationCollection(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplicationCollection')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def application_collection(self):
                    return CodeSign.ApplicationCollection(self._from_json(key='ApplicationCollection'))

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

    class _GetApplicationCollectionMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplicationCollectionMembers')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def application_collection(self):
                    return CodeSign.ApplicationCollection(self._from_json(key='ApplicationCollection'))

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

    class _GetApplicationCollectionMemberDNs(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplicationCollectionMemberDNs')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def application_collection(self):
                    return CodeSign.ApplicationCollection(self._from_json(key='ApplicationCollection'))

                @property
                @api_response_property()
                def application_collection_dns(self) -> List[str]:
                    return self._from_json(key='ApplicationCollectionDNs')

                @property
                @api_response_property()
                def application_dns(self) -> List[str]:
                    return self._from_json(key='ApplicationDNs')

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

    class _GetEnvironment(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetEnvironment')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def certificate_environment(self):
                    return CodeSign.CertificateEnvironment(self._from_json(key='CertificateEnvironment'))

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

    class _GetGlobalConfiguration(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetGlobalConfiguration')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def error(self) -> str:
                    return self._from_json(key='Error')

                @property
                @api_response_property()
                def global_configuration(self):
                    return CodeSign.GlobalConfiguration(self._from_json(key='GlobalConfiguration'))

                @property
                @api_response_property()
                def result(self):
                    return CodeSign.ResultCode(self._from_json(key='Result'))

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._get())

    class _GetObjectRights(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetObjectRights')

        def post(self, dn: str):
            body = {
                'Dn': dn
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
                def rights_list(self):
                    return [CodeSign.RightsKeyValue(r) for r in self._from_json(key='RightsList')]

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _GetProject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetProject')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
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
                def project(self):
                    return CodeSign.Project(self._from_json(key='Project'))

                @property
                @api_response_property()
                def result(self):
                    return CodeSign.ResultCode(self._from_json(key='Result'))

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _GetRight(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetRight')

        def post(self, dn: str):
            body = {
                'Dn': dn
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
                def rights(self):
                    return CodeSign.Rights(self._from_json(key='Rights'))

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _GetTemplate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetTemplate')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def certificate_template(self):
                    return CodeSign.CertificateTemplate(self._from_json(key='CertificateTemplate'))

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

    class _GetTrusteeRights(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetTrusteeRights')

        def post(self, dn: str):
            body = {
                'Dn': dn
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
                def rights_list(self):
                    return [CodeSign.RightsKeyValue(r) for r in self._from_json(key='RightsList')]

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _RemoveAdministrator(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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

    class _RemoveApplicationAdministrator(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveApplicationAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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

    class _RemoveProjectAdministrator(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveProjectAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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

    class _RemoveProjectApprover(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveProjectApprover')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
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

    class _RenameApplication(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameApplication')

        def post(self, dn: str, new_dn: str):
            body = {
                'Dn': dn,
                'NewDn': new_dn
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

    class _RenameApplicationCollection(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameApplicationCollection')

        def post(self, dn: str, new_dn: str):
            body = {
                'Dn'   : dn,
                'NewDn': new_dn
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

    class _RenameProject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameProject')

        def post(self, new_dn: str, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id,
                'NewDn': new_dn
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

    class _RenameTemplate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameTemplate')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id
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

    class _SetGlobalConfiguration(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/SetGlobalConfiguration')

        def post(self, global_configuration: dict):
            body = {
                'GlobalConfiguration': global_configuration
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

    class _UpdateApplication(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateApplication')

        def post(self, application: dict):
            body = {
                'Application': application
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

    class _UpdateApplicationCollection(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateApplicationCollection')

        def post(self, application_collection: dict):
            body = {
                'ApplicationCollection': application_collection
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

    class _UpdateEnvironment(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateEnvironment')

        def post(self, certificate_environment: dict):
            body = {
                'CertificateEnvironment': certificate_environment
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def certificate_environment(self):
                    return CodeSign.CertificateEnvironment(self._from_json(key='CertificateEnvironment'))

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

    class _UpdateProject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateProject')

        def post(self, project: dict):
            body = {
                'Project': project
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

    class _UpdateProjectStatus(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateProjectStatus')

        def post(self, project_status: int, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn': dn,
                'Guid': guid,
                'Id': id,
                'ProjectStatus': project_status,
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

    class _UpdateTemplate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateTemplate')

        def post(self, dn: str, certificate_template: dict, object_naming_pattern: str = None):
            body = {
                'Dn': dn,
                'CertificateTemplate': certificate_template,
                'ObjectNamingPattern': object_naming_pattern
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
