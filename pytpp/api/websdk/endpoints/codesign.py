from typing import List, Dict, Union
from pytpp.api.websdk.models import codesign
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Codesign(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Codesign')
        self.AddAdministrator = self._AddAdministrator(api_obj=api_obj, url=f'{self._url}/AddAdministrator')
        self.AddApplicationAdministrator = self._AddApplicationAdministrator(api_obj=api_obj, url=f'{self._url}/AddApplicationAdministrator')
        self.AddProjectAdministrator = self._AddProjectAdministrator(api_obj=api_obj, url=f'{self._url}/AddProjectAdministrator')
        self.AddProjectApprover = self._AddProjectApprover(api_obj=api_obj, url=f'{self._url}/AddProjectApprover')
        self.CountReferences = self._CountReferences(api_obj=api_obj, url=f'{self._url}/CountReferences')
        self.CreateApplication = self._CreateApplication(api_obj=api_obj, url=f'{self._url}/CreateApplication')
        self.CreateApplicationCollection = self._CreateApplicationCollection(api_obj=api_obj, url=f'{self._url}/CreateApplicationCollection')
        self.CreateEnvironment = self._CreateEnvironment(api_obj=api_obj, url=f'{self._url}/CreateEnvironment')
        self.CreateProject = self._CreateProject(api_obj=api_obj, url=f'{self._url}/CreateProject')
        self.CreateTemplate = self._CreateTemplate(api_obj=api_obj, url=f'{self._url}/CreateTemplate')
        self.DeleteApplication = self._DeleteApplication(api_obj=api_obj, url=f'{self._url}/DeleteApplication')
        self.DeleteApplicationCollection = self._DeleteApplicationCollection(api_obj=api_obj, url=f'{self._url}/DeleteApplicationCollection')
        self.DeleteEnvironment = self._DeleteEnvironment(api_obj=api_obj, url=f'{self._url}/DeleteEnvironment')
        self.DeleteProject = self._DeleteProject(api_obj=api_obj, url=f'{self._url}/DeleteProject')
        self.DeleteTemplate = self._DeleteTemplate(api_obj=api_obj, url=f'{self._url}/DeleteTemplate')
        self.EnumerateApplications = self._EnumerateApplications(api_obj=api_obj, url=f'{self._url}/EnumerateApplications')
        self.EnumerateApplicationCollections = self._EnumerateApplicationCollections(api_obj=api_obj, url=f'{self._url}/EnumerateApplicationCollections')
        self.EnumerateProjects = self._EnumerateProjects(api_obj=api_obj, url=f'{self._url}/EnumerateProjects')
        self.EnumerateReferences = self._EnumerateReferences(api_obj=api_obj, url=f'{self._url}/EnumerateReferences')
        self.EnumerateTemplates = self._EnumerateTemplates(api_obj=api_obj, url=f'{self._url}/EnumerateTemplates')
        self.GetApplication = self._GetApplication(api_obj=api_obj, url=f'{self._url}/GetApplication')
        self.GetApplicationCollection = self._GetApplicationCollection(api_obj=api_obj, url=f'{self._url}/GetApplicationCollection')
        self.GetApplicationCollectionMembers = self._GetApplicationCollectionMembers(api_obj=api_obj, url=f'{self._url}/GetApplicationCollectionMembers')
        self.GetApplicationCollectionMemberDNs = self._GetApplicationCollectionMemberDNs(api_obj=api_obj, url=f'{self._url}/GetApplicationCollectionMemberDNs')
        self.GetEnvironment = self._GetEnvironment(api_obj=api_obj, url=f'{self._url}/GetEnvironment')
        self.GetGlobalConfiguration = self._GetGlobalConfiguration(api_obj=api_obj, url=f'{self._url}/GetGlobalConfiguration')
        self.GetObjectRights = self._GetObjectRights(api_obj=api_obj, url=f'{self._url}/GetObjectRights')
        self.GetProject = self._GetProject(api_obj=api_obj, url=f'{self._url}/GetProject')
        self.GetRight = self._GetRight(api_obj=api_obj, url=f'{self._url}/GetRight')
        self.GetTemplate = self._GetTemplate(api_obj=api_obj, url=f'{self._url}/GetTemplate')
        self.GetTrusteeRights = self._GetTrusteeRights(api_obj=api_obj, url=f'{self._url}/GetTrusteeRights')
        self.RemoveAdministrator = self._RemoveAdministrator(api_obj=api_obj, url=f'{self._url}/RemoveAdministrator')
        self.RemoveApplicationAdministrator = self._RemoveApplicationAdministrator(api_obj=api_obj, url=f'{self._url}/RemoveApplicationAdministrator')
        self.RemoveProjectAdministrator = self._RemoveProjectAdministrator(api_obj=api_obj, url=f'{self._url}/RemoveProjectAdministrator')
        self.RenameApplication = self._RenameApplication(api_obj=api_obj, url=f'{self._url}/RenameApplication')
        self.RenameApplicationCollection = self._RenameApplicationCollection(api_obj=api_obj, url=f'{self._url}/RenameApplicationCollection')
        self.RenameProject = self._RenameProject(api_obj=api_obj, url=f'{self._url}/RenameProject')
        self.RenameTemplate = self._RenameTemplate(api_obj=api_obj, url=f'{self._url}/RenameTemplate')
        self.SetGlobalConfiguration = self._SetGlobalConfiguration(api_obj=api_obj, url=f'{self._url}/SetGlobalConfiguration')
        self.UpdateApplication = self._UpdateApplication(api_obj=api_obj, url=f'{self._url}/UpdateApplication')
        self.UpdateApplicationCollection = self._UpdateApplicationCollection(api_obj=api_obj, url=f'{self._url}/UpdateApplicationCollection')
        self.UpdateEnvironment = self._UpdateEnvironment(api_obj=api_obj, url=f'{self._url}/UpdateEnvironment')
        self.UpdateProject = self._UpdateProject(api_obj=api_obj, url=f'{self._url}/UpdateProject')
        self.UpdateProjectStatus = self._UpdateProjectStatus(api_obj=api_obj, url=f'{self._url}/UpdateProjectStatus')
        self.UpdateTemplate = self._UpdateTemplate(api_obj=api_obj, url=f'{self._url}/UpdateTemplate')

    class _AddAdministrator(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddApplicationAdministrator(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddProjectAdministrator(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddProjectApprover(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddPreApproval(WebSdkEndpoint):
        def post(self, dn: str, comment: str, user: str, hours: int = None, ip_address: str = None,
                 signing_executable: str = None, single_use: bool = None, not_before: str = None, ):
            body = {
                'Dn'               : dn,
                'Comment'          : comment,
                'Hours'            : hours,
                'IPAddress'        : ip_address,
                'SigningExecutable': signing_executable,
                'SingleUse'        : single_use,
                'User'             : user,
                'NotBefore'        : not_before
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CountReferences(WebSdkEndpoint):
        def post(self, application: Union[dict, codesign.Application] = None, 
                 application_collection: Union[dict, codesign.ApplicationCollection] = None):
            body = {
                'Application'          : application,
                'ApplicationCollection': application_collection
            }

            class Output(WebSdkOutputModel):
                count: int = ApiField(alias='Count')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateApplication(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                application: codesign.Application = ApiField(alias='Application')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateApplicationCollection(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                application: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateEnvironment(WebSdkEndpoint):
        def post(self, dn: str, environment_name: str, project: Dict[str, Union[str, int]],
                 template: List[Dict[str, str]], template_dn: str = None):
            body = {
                'Dn'             : dn,
                'EnvironmentName': environment_name,
                'Project'        : project,
                'Template'       : template,
                'TemplateDn'     : template_dn
            }

            class Output(WebSdkOutputModel):
                apple_environment: codesign.AppleEnvironment = ApiField(alias='AppleEnvironment')
                certificate_environment: codesign.CertificateEnvironment = ApiField(alias='CertificateEnvironment')
                csp_environment: codesign.CSPEnvironment = ApiField(alias='CSPEnvironment')
                dot_net_environment: codesign.DotNetEnvironment = ApiField(alias='DotNetEnvironment')
                gpg_environment: codesign.GPGEnvironment = ApiField(alias='GPGEnvironment')
                key_pair_environment: codesign.KeyPairEnvironment = ApiField(alias='KeyPairEnvironment')
                apple_template: codesign.AppleTemplate = ApiField(alias='AppleTemplate')
                certificate_template: codesign.CertificateTemplate = ApiField(alias='CertificateTemplate')
                csp_template: codesign.CSPTemplate = ApiField(alias='CSPTemplate')
                dot_net_template: codesign.DotNetTemplate = ApiField(alias='DotNetTemplate')
                gpg_template: codesign.GPGTemplate = ApiField(alias='GPGTemplate')
                key_pair_template: codesign.KeyPairTemplate = ApiField(alias='KeyPairTemplate')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateProject(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                project: codesign.Project = ApiField(alias='Project')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateTemplate(WebSdkEndpoint):
        def post(self, dn: str, template_type: codesign.TemplateType = None, per_user: bool = None):
            body = {
                'Dn'          : dn,
                'TemplateType': template_type,
                'PerUser'     : per_user
            }

            class Output(WebSdkOutputModel):
                certificate_template: codesign.CertificateTemplate = ApiField(alias='CertificateTemplate')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteApplication(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteApplicationCollection(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteEnvironment(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteProject(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteTemplate(WebSdkEndpoint):
        def post(self, dn: str = None, force: bool = None, guid: str = None, id: int = None):
            body = {
                'Dn'   : dn,
                'Force': force,
                'Guid' : guid,
                'Id'   : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateApplications(WebSdkEndpoint):
        # noinspection ALL
        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class Output(WebSdkOutputModel):
                applications: List[codesign.Application] = ApiField(alias='Applications', default_factory=list)
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateApplicationCollections(WebSdkEndpoint):
        # noinspection ALL
        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class Output(WebSdkOutputModel):
                application_collections: List[codesign.ApplicationCollection] = ApiField(alias='ApplicationCollections', default_factory=list)
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateProjects(WebSdkEndpoint):
        # noinspection ALL
        def post(self, filter: str = None, rights: int = None):
            body = {
                'Filter': filter,
                'Rights': rights
            }

            class Output(WebSdkOutputModel):
                projects: List[codesign.Project] = ApiField(alias='Projects', default_factory=list)
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateReferences(WebSdkEndpoint):
        def post(self, application: Union[dict, codesign.Application] = None, 
                 application_collection: Union[dict] = None,
                 application_dn: str = None, application_guid: str = None,
                 collection_dn: str = None, collection_guid: str = None):
            body = {
                'Application'          : application,
                'ApplicationCollection': application_collection,
                'ApplicationDn'        : application_dn,
                'ApplicationGuid'      : application_guid,
                'CollectionDn'         : collection_dn,
                'CollectionGuid'       : collection_guid
            }

            class Output(WebSdkOutputModel):
                reference_dns: List[str] = ApiField(alias='ReferenceDNs', default_factory=list)
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateTemplates(WebSdkEndpoint):
        # noinspection ALL
        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class Output(WebSdkOutputModel):
                apple_templates: List[codesign.AppleTemplate] = ApiField(alias='AppleTemplates', default_factory=list)
                certificate_templates: List[codesign.CertificateTemplate] = ApiField(alias='CertificateTemplates', default_factory=list)
                csp_templates: List[codesign.CSPTemplate] = ApiField(alias='CSPTemplates', default_factory=list)
                dot_net_templates: List[codesign.DotNetTemplate] = ApiField(alias='DotNetTemplates', default_factory=list)
                gpg_templates: List[codesign.GPGTemplate] = ApiField(alias='GPGTemplates', default_factory=list)
                key_pair_templates: List[codesign.KeyPairTemplate] = ApiField(alias='KeyPairTemplates', default_factory=list)
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplication(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                application: codesign.Application = ApiField(alias='Application')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplicationCollection(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                application_collection: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplicationCollectionMembers(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                application_collection: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplicationCollectionMemberDNs(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None, application: Union[dict, codesign.Application] = None):
            body = {
                'Application': application,
                'Dn'         : dn,
                'Guid'       : guid,
                'Id'         : id
            }

            class Output(WebSdkOutputModel):
                application_collection: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                application_collection_dns: List[str] = ApiField(alias='ApplicationCollectionDNs', default_factory=list)
                application_dns: List[str] = ApiField(alias='ApplicationDNs', default_factory=list)
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetEnvironment(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                apple_environment: codesign.AppleEnvironment = ApiField(alias='AppleEnvironment')
                certificate_environment: codesign.CertificateEnvironment = ApiField(alias='CertificateEnvironment')
                csp_environment: codesign.CSPEnvironment = ApiField(alias='CSPEnvironment')
                dot_net_environment: codesign.DotNetEnvironment = ApiField(alias='DotNetEnvironment')
                gpg_environment: codesign.GPGEnvironment = ApiField(alias='GPGEnvironment')
                key_pair_environment: codesign.KeyPairEnvironment = ApiField(alias='KeyPairEnvironment')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetGlobalConfiguration(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                global_configuration: codesign.GlobalConfiguration = ApiField(alias='GlobalConfiguration')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._get(), output_cls=Output)

    class _GetObjectRights(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                rights_list: List[codesign.RightsKeyValue] = ApiField(alias='RightsList', default_factory=list)
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetProject(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                project: codesign.Project = ApiField(alias='Project')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetRight(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                rights: codesign.Rights = ApiField(alias='Rights', converter=lambda x: codesign.Rights(value=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetTemplate(WebSdkEndpoint):
        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                apple_template: codesign.AppleTemplate = ApiField(alias='AppleTemplate')
                certificate_template: codesign.CertificateTemplate = ApiField(alias='CertificateTemplate')
                csp_template: codesign.CSPTemplate = ApiField(alias='CSPTemplate')
                dot_net_template: codesign.DotNetTemplate = ApiField(alias='DotNetTemplate')
                gpg_template: codesign.GPGTemplate = ApiField(alias='GPGTemplate')
                key_pair_template: codesign.KeyPairTemplate = ApiField(alias='KeyPairTemplate')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetTrusteeRights(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                rights_list: List[codesign.RightsKeyValue] = ApiField(alias='RightsList', default_factory=list)
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveAdministrator(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveApplicationAdministrator(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveProjectAdministrator(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveProjectApprover(WebSdkEndpoint):
        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameApplication(WebSdkEndpoint):
        def post(self, dn: str, new_dn: str):
            body = {
                'Dn'   : dn,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameApplicationCollection(WebSdkEndpoint):
        def post(self, dn: str, new_dn: str):
            body = {
                'Dn'   : dn,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameProject(WebSdkEndpoint):
        def post(self, new_dn: str, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'   : dn,
                'Guid' : guid,
                'Id'   : id,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameTemplate(WebSdkEndpoint):
        def post(self, new_dn: str, dn: str = None, guid: str = None):
            body = {
                'Dn'   : dn,
                'Guid' : guid,
                'Id'   : id,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _SetGlobalConfiguration(WebSdkEndpoint):
        def post(self, global_configuration: Union[dict, codesign.GlobalConfiguration]):
            body = {
                'GlobalConfiguration': global_configuration
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateApplication(WebSdkEndpoint):
        def post(self, application: Union[dict, codesign.Application]):
            body = {
                'Application': application
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateApplicationCollection(WebSdkEndpoint):
        def post(self, application_collection: Union[dict, codesign.ApplicationCollection]):
            body = {
                'ApplicationCollection': application_collection
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateEnvironment(WebSdkEndpoint):
        def post(self, certificate_environment: Union[dict, codesign.CertificateEnvironment] = None,
                 apple_environment: Union[dict, codesign.AppleEnvironment] = None,
                 csp_environment: Union[dict, codesign.CSPEnvironment] = None,
                 dot_net_environment: Union[dict, codesign.DotNetEnvironment] = None,
                 gpg_environment: Union[dict, codesign.GPGEnvironment] = None,
                 key_pair_environment: Union[dict, codesign.KeyPairEnvironment] = None):
            body = {
                'AppleEnvironment'      : apple_environment,
                'CertificateEnvironment': certificate_environment,
                'CSPEnvironment'        : csp_environment,
                'DotNetEnvironment'     : dot_net_environment,
                'GPGEnvironment'        : gpg_environment,
                'KeyPairEnvironment'    : key_pair_environment
            }

            class Output(WebSdkOutputModel):
                apple_environment: codesign.AppleEnvironment = ApiField(alias='AppleEnvironment')
                certificate_environment: codesign.CertificateEnvironment = ApiField(alias='CertificateEnvironment')
                csp_environment: codesign.CSPEnvironment = ApiField(alias='CSPEnvironment')
                dot_net_environment: codesign.DotNetEnvironment = ApiField(alias='DotNetEnvironment')
                gpg_environment: codesign.GPGEnvironment = ApiField(alias='GPGEnvironment')
                key_pair_environment: codesign.KeyPairEnvironment = ApiField(alias='KeyPairEnvironment')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateProject(WebSdkEndpoint):
        def post(self, project: Union[dict, codesign.Project]):
            body = {
                'Project': project
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateProjectStatus(WebSdkEndpoint):
        def post(self, project_status: int, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'           : dn,
                'Guid'         : guid,
                'Id'           : id,
                'ProjectStatus': project_status,
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateTemplate(WebSdkEndpoint):
        def post(self, dn: str, certificate_template: Union[dict, codesign.CertificateTemplate, codesign.CSPTemplate,
                 codesign.DotNetTemplate, codesign.AppleTemplate, codesign.GPGTemplate, codesign.KeyPairTemplate],
                 object_naming_pattern: str = None):
            body = {
                'Dn'                 : dn,
                'CertificateTemplate': certificate_template,
                'ObjectNamingPattern': object_naming_pattern
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)
