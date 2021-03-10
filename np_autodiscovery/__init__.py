default_app_config = 'np_autodiscovery.apps.NPAutoDiscoveryConfig'

from extras.plugins import PluginConfig
from .version import __version__

class NpAutodiscoveryConfig(PluginConfig):
    name = 'np_autodiscovery'
    verbose_name = 'Autodiscovery'
    description = 'auto discovery of existing devices in a network'
    version = '1.0.0'
    author='John Anderson',
    author_email='lampwins@gmail.com',
    required_settings = []
    default_settings = {}
config = NpAutodiscoveryConfig
