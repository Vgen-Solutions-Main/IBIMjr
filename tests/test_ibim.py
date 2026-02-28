"""
Basic tests for IBIM core functionality
"""

import sys
import os

# Add src to path for local imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ibim import IBIM, Component


def test_component_creation():
    """Test Component creation and initialization"""
    component = Component("TestComponent", {"key": "value"})
    assert component.name == "TestComponent"
    assert component.config == {"key": "value"}
    assert component.status == "initialized"
    print("✓ Component creation test passed")


def test_component_process():
    """Test Component processing"""
    component = Component("TestComponent", {"type": "test"})
    result = component.process()
    assert result["name"] == "TestComponent"
    assert result["status"] == "processed"
    assert component.status == "processed"
    print("✓ Component process test passed")


def test_ibim_creation():
    """Test IBIM creation"""
    ibim = IBIM("TestIBIM")
    assert ibim.name == "TestIBIM"
    assert len(ibim.components) == 0
    assert len(ibim.results) == 0
    print("✓ IBIM creation test passed")


def test_ibim_add_component():
    """Test adding components to IBIM"""
    ibim = IBIM()
    component = ibim.add_component("Component1", {"value": 123})
    assert "Component1" in ibim.components
    assert component.name == "Component1"
    assert component.config["value"] == 123
    print("✓ IBIM add component test passed")


def test_ibim_remove_component():
    """Test removing components from IBIM"""
    ibim = IBIM()
    ibim.add_component("Component1")
    ibim.add_component("Component2")
    
    removed = ibim.remove_component("Component1")
    assert removed is True
    assert "Component1" not in ibim.components
    assert "Component2" in ibim.components
    
    removed = ibim.remove_component("NonExistent")
    assert removed is False
    print("✓ IBIM remove component test passed")


def test_ibim_get_component():
    """Test getting components from IBIM"""
    ibim = IBIM()
    ibim.add_component("Component1", {"data": "test"})
    
    component = ibim.get_component("Component1")
    assert component is not None
    assert component.name == "Component1"
    
    component = ibim.get_component("NonExistent")
    assert component is None
    print("✓ IBIM get component test passed")


def test_ibim_process():
    """Test processing all components"""
    ibim = IBIM()
    ibim.add_component("Component1", {"id": 1})
    ibim.add_component("Component2", {"id": 2})
    ibim.add_component("Component3", {"id": 3})
    
    results = ibim.process()
    assert len(results) == 3
    assert all(r["status"] == "processed" for r in results)
    
    retrieved_results = ibim.get_results()
    assert results == retrieved_results
    print("✓ IBIM process test passed")


def test_ibim_all_good():
    """Test all_good method for checking component statuses"""
    ibim = IBIM()
    
    # Empty IBIM should be all good
    assert ibim.all_good() is True
    
    # Add components but don't process
    ibim.add_component("Component1")
    ibim.add_component("Component2")
    assert ibim.all_good() is False  # Not processed yet
    
    # Process all components
    ibim.process()
    assert ibim.all_good() is True  # All processed now
    
    print("✓ IBIM all_good test passed")


def test_ibim_status_summary():
    """Test get_status_summary method"""
    ibim = IBIM()
    
    # Empty IBIM
    summary = ibim.get_status_summary()
    assert summary["total"] == 0
    assert summary["all_good"] is True
    assert len(summary["components"]) == 0
    
    # Add components
    ibim.add_component("Component1")
    ibim.add_component("Component2")
    ibim.add_component("Component3")
    
    summary = ibim.get_status_summary()
    assert summary["total"] == 3
    assert summary["status_counts"]["initialized"] == 3
    assert summary["all_good"] is False
    
    # Process components
    ibim.process()
    summary = ibim.get_status_summary()
    assert summary["total"] == 3
    assert summary["status_counts"]["processed"] == 3
    assert summary["all_good"] is True
    assert len(summary["components"]) == 3
    
    print("✓ IBIM status_summary test passed")


def run_all_tests():
    """Run all tests"""
    print("Running IBIM tests...\n")
    
    test_component_creation()
    test_component_process()
    test_ibim_creation()
    test_ibim_add_component()
    test_ibim_remove_component()
    test_ibim_get_component()
    test_ibim_process()
    test_ibim_all_good()
    test_ibim_status_summary()
    
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
