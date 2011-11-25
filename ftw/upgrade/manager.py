from ftw.upgrade.interfaces import IUpgradeManager
from types import ModuleType
from zope.interface import implements
from ftw.upgrade.utils import get_modules

class UpgradeManager(object):
    implements(IUpgradeManager)

    def __init__(self):
        self._upgrade_packages = []

    def add_upgrade_package(self, module):
        if not isinstance(module, ModuleType):
            raise ValueError('Expected module, got "%s"' % str(module))

        self._upgrade_packages.append(module)

    def list_upgrades(self):
        modules = []
        for package in self._upgrade_packages:
            import pdb; pdb.set_trace( )
            modules.append(get_modules(package.__name__))
        
    def install_upgrades(self, upgrades):
        # XXX: implement install_upgrades
        raise NotImplementedError()

    def is_installed(self, dottedname):
        # XXX: implement is_installed
        raise NotImplementedError()

    def get_upgrade(self, dottedname):
        # XXX: implement get_upgrade
        raise NotImplementedError()
