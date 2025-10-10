import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bridge_gad.plugins import load_plugins

def test_plugins():
    print("Testing plugin loading...")
    plugins = load_plugins()
    print(f"Loaded {len(plugins)} plugins")
    for plugin in plugins:
        print(f"- {plugin.name}: {plugin.description}")
    print("Plugin test completed successfully!")

if __name__ == "__main__":
    test_plugins()