"""
Example demonstrating the status checking functionality ("ALL GOODS NOW?")
"""

import sys
import os

# Add src to path for local imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ibim import IBIM


def main():
    """Demonstrate status checking features"""
    
    # Create an IBIM instance
    print("Creating IBIM instance with components...")
    ibim = IBIM(name="StatusCheckExample")
    
    # Add some components
    ibim.add_component("Component1", {"type": "test"})
    ibim.add_component("Component2", {"type": "test"})
    ibim.add_component("Component3", {"type": "test"})
    
    # Check status before processing
    print("\n--- Before Processing ---")
    print(f"All components good? {ibim.all_good()}")
    summary = ibim.get_status_summary()
    print(f"Status Summary:")
    print(f"  Total components: {summary['total']}")
    print(f"  Status counts: {summary['status_counts']}")
    print(f"  All good: {summary['all_good']}")
    
    # Process all components
    print("\n--- Processing Components ---")
    ibim.process()
    print("Processing complete!")
    
    # Check status after processing
    print("\n--- After Processing ---")
    print(f"All components good? {ibim.all_good()}")
    summary = ibim.get_status_summary()
    print(f"Status Summary:")
    print(f"  Total components: {summary['total']}")
    print(f"  Status counts: {summary['status_counts']}")
    print(f"  All good: {summary['all_good']}")
    
    # Show individual component statuses
    print("\n--- Individual Component Statuses ---")
    for comp_status in summary['components']:
        print(f"  {comp_status['name']}: {comp_status['status']}")
    
    # Answer the question: "ALL GOODS NOW?"
    print("\n" + "=" * 50)
    if ibim.all_good():
        print("✓ YES! ALL GOODS NOW!")
    else:
        print("✗ NO! Not all components are processed.")
    print("=" * 50)


if __name__ == "__main__":
    main()
