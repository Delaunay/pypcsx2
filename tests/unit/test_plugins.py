import pypcsx2.plugins
from pypcsx2.core import discover_plugins


def test_plugins():
    plugins = discover_plugins(pypcsx2.plugins)

    assert len(plugins) == 1
