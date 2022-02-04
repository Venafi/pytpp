from dataclasses import dataclass

@dataclass
class Permissions:
    name: str
    approve: bool = None
    delete: bool = None
    discover: bool = None
    manage: bool = None
    read: bool = None
    revoke: bool = None

    def to_dict(self):
        return {
            'approve' : self.approve,
            'delete'  : self.delete,
            'discover': self.discover,
            'manage'  : self.manage,
            'read'    : self.read,
            'revoke'  : self.revoke,
        }

    def effective(self):
        # "read" is implied when specifying the access permission, so it must be omitted.
        return [k for k, v in self.to_dict().items() if v is not None and k != 'read']


@dataclass
class Scope:
    def __init__(self):
        self._certificate = Permissions(name='certificate')
        self._ssh = Permissions(name='ssh')
        self._codesign = Permissions(name='codesign')
        self._configuration = Permissions(name='configuration')
        self._restricted = Permissions(name='restricted')
        self._security = Permissions(name='security')
        self._statistics = Permissions(name='statistics')
        self._agent = Permissions(name='agent')

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.to_string()

    @property
    def scopes(self):
        return [
            {'name': p.name, 'permissions': p.to_dict()}
            for p in self.list()
        ]

    def list(self):
        return [
            self._certificate, self._ssh, self._codesign,
            self._configuration, self._restricted,
            self._security, self._statistics, self._agent
        ]

    def to_string(self):
        scopes = [
            f'{p.name}:{",".join(p.effective())}'
            for p in self.list() if p.effective()
        ]
        return ';'.join(scopes)

    def agent(self, delete: bool = False, read: bool = False):
        self._agent.delete = delete
        self._agent.read = read
        return self

    def certificate(self, approve: bool = False, delete: bool = False, discover: bool = False,
                    manage: bool = False, read: bool = False, revoke: bool = False):
        self._certificate.approve = approve
        self._certificate.delete = delete
        self._certificate.discover = discover
        self._certificate.manage = manage
        self._certificate.read = read
        self._certificate.revoke = revoke
        return self

    def configuration(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._configuration.delete = delete
        self._configuration.manage = manage
        self._configuration.read = read
        return self

    def codesign(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._codesign.delete = delete
        self._codesign.manage = manage
        self._codesign.read = read
        return self

    def restricted(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._restricted.delete = delete
        self._restricted.manage = manage
        self._restricted.read = read
        return self

    def security(self, delete: bool = False, manage: bool = False, read: bool = False):
        self._security.delete = delete
        self._security.manage = manage
        self._security.read = read
        return self

    def ssh(self, approve: bool = False, delete: bool = False, discover: bool = False,
            manage: bool = False, read: bool = False):
        self._ssh.approve = approve
        self._ssh.delete = delete
        self._ssh.discover = discover
        self._ssh.manage = manage
        self._ssh.read = read
        return self

    def statistics(self, read: bool = False):
        self._statistics.read = read
        return self
