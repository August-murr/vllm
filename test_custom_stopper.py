#!/usr/bin/env python3
"""
Simple test to verify the StoppingCriteria implementation works.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from vllm.engine.output_processor.stopping_criteria import StoppingCriteria
from vllm.sampling_params import SamplingParams


class TestStopper(StoppingCriteria):
    def stop(self, text: str) -> bool:
        return "STOP_HERE" in text


def test_stopping_criteria():
    # Test 1: Create a custom stopper
    custom_stopper = TestStopper()
    
    # Test 2: Create SamplingParams with the custom stopper
    sampling_params = SamplingParams(
        temperature=0.7,
        max_tokens=100,
        stopping_criteria=custom_stopper
    )
    
    # Test 3: Verify the stopper is properly stored
    assert sampling_params.stopping_criteria is not None
    assert isinstance(sampling_params.stopping_criteria, StoppingCriteria)
    assert isinstance(sampling_params.stopping_criteria, TestStopper)
    
    # Test 4: Test the stopper logic
    assert custom_stopper.stop("This should not stop") == False
    assert custom_stopper.stop("This text has STOP_HERE marker") == True
    
    print("✅ All tests passed!")
    print(f"✅ SamplingParams with custom stopper: {sampling_params}")


if __name__ == "__main__":
    test_stopping_criteria()
