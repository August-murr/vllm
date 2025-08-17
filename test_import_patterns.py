#!/usr/bin/env python3
"""Test both import patterns for StoppingCriteria."""

def test_main_package_import():
    """Test importing from main vllm package."""
    try:
        from vllm import StoppingCriteria
        print("✅ Import from main package: from vllm import StoppingCriteria")
        return StoppingCriteria
    except ImportError as e:
        print(f"❌ Main package import failed: {e}")
        return None

def test_direct_module_import():
    """Test importing from specific module."""
    try:
        from vllm.engine.output_processor.stopping_criteria import StoppingCriteria
        print("✅ Import from module: from vllm.engine.output_processor.stopping_criteria import StoppingCriteria")
        return StoppingCriteria
    except ImportError as e:
        print(f"❌ Direct module import failed: {e}")
        return None

def test_both_imports_same():
    """Test that both import methods give the same class."""
    main_class = test_main_package_import()
    direct_class = test_direct_module_import()
    
    if main_class and direct_class:
        if main_class is direct_class:
            print("✅ Both imports reference the same class")
            return True
        else:
            print("❌ Imports reference different classes")
            return False
    return False

def test_usage_patterns():
    """Test different usage patterns."""
    # Pattern 1: Import from main package
    from vllm import StoppingCriteria
    
    class LengthStopper(StoppingCriteria):
        def __init__(self, max_length: int):
            self.max_length = max_length
        
        def stop(self, text: str) -> bool:
            return len(text) > self.max_length
    
    stopper = LengthStopper(15)
    result1 = stopper.stop("short text")
    result2 = stopper.stop("this is a much longer text that should trigger stopping")
    
    print(f"✅ Usage test - short text: {result1}, long text: {result2}")
    
    if not result1 and result2:
        print("✅ Stopping logic works correctly")
        return True
    else:
        print("❌ Stopping logic failed")
        return False

if __name__ == "__main__":
    print("Testing StoppingCriteria import patterns...\n")
    
    success = True
    success &= test_both_imports_same()
    success &= test_usage_patterns()
    
    print("\n" + "="*50)
    if success:
        print("🎉 All tests passed! StoppingCriteria is properly importable.")
        print("\nUsage examples:")
        print("  from vllm import StoppingCriteria  # Recommended")
        print("  from vllm.engine.output_processor.stopping_criteria import StoppingCriteria  # Also works")
    else:
        print("💥 Some tests failed!")
        exit(1)
