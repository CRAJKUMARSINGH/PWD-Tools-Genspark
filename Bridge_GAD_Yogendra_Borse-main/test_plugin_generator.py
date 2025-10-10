import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Test the plugin generator
from bridge_gad.plugin_generator import PLUGIN_DIR, TEMPLATE

def test_plugin_generator():
    print("Testing plugin generator...")
    print(f"Plugin directory: {PLUGIN_DIR}")
    
    # Test template generation
    class_name = "TBeamBridgePlugin"
    display_name = "T-Beam Bridge"
    description = "Auto-generated module for T-Beam Bridge design."
    
    plugin_content = TEMPLATE.format(
        class_name=class_name,
        display_name=display_name,
        description=description
    )
    
    print("Generated plugin content:")
    print(plugin_content)
    print("Plugin generator test completed successfully!")

if __name__ == "__main__":
    test_plugin_generator()