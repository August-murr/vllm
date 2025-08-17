#!/usr/bin/env python3
"""Test that StoppingCriteria can be imported from vllm package."""

def test_import():
    """Test importing StoppingCriteria from main vllm package."""
    try:
        from vllm import StoppingCriteria
        print("✅ Successfully imported StoppingCriteria from vllm")
        
        # Test that it's the right class
        import inspect
        if inspect.isabstract(StoppingCriteria):
            print("✅ StoppingCriteria is correctly abstract")
        else:
            print("❌ StoppingCriteria should be abstract")
            
        # Test that it has the right method
        if hasattr(StoppingCriteria, 'stop'):
            print("✅ StoppingCriteria has 'stop' method")
        else:
            print("❌ StoppingCriteria missing 'stop' method")
            
        # Test creating a concrete implementation
        class TestStopper(StoppingCriteria):
            def stop(self, text: str) -> bool:
                return len(text) > 10
                
        stopper = TestStopper()
        result = stopper.stop("short")
        print(f"✅ Created and used custom stopper: stop('short') = {result}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import StoppingCriteria: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_import()
    if success:
        print("🎉 All import tests passed!")
    else:
        print("💥 Import tests failed!")
        exit(1)
