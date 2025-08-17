#!/usr/bin/env python3
"""
Example usage of custom StoppingCriteria in vLLM.

This example demonstrates how to create and use custom stopping criteria
to control text generation beyond the built-in stop strings and tokens.
"""

from vllm import LLM, SamplingParams, StoppingCriteria
import re


class LengthBasedStopper(StoppingCriteria):
    """Stop generation when text reaches a certain length."""
    
    def __init__(self, max_length: int = 100):
        self.max_length = max_length
    
    def stop(self, text: str) -> bool:
        return len(text) > self.max_length


class PatternStopper(StoppingCriteria):
    """Stop generation when specific patterns are detected."""
    
    def __init__(self, patterns: list[str]):
        self.patterns = patterns
    
    def stop(self, text: str) -> bool:
        return any(pattern in text for pattern in self.patterns)


class ConditionalStopper(StoppingCriteria):
    """Stop generation based on complex conditions."""
    
    def stop(self, text: str) -> bool:
        # Stop if text contains "END" and has at least 50 characters
        return "END" in text and len(text) >= 50


# Example usage:
if __name__ == "__main__":
    # This would be used in your VLLM request like:
    # 
    # from vllm import SamplingParams
    # 
    # # Create custom stopper
    # custom_stopper = LengthBasedStopper(max_length=200)
    # 
    # # Use it in sampling params
    # sampling_params = SamplingParams(
    #     temperature=0.7,
    #     max_tokens=500,
    #     stopping_criteria=custom_stopper
    # )
    # 
    # # Generate with custom stopping
    # outputs = llm.generate(prompt, sampling_params)
    
    # Test the stoppers
    test_text = "This is a test string with END marker and more content"
    
    length_stopper = LengthBasedStopper(max_length=30)
    pattern_stopper = PatternStopper(["END", "STOP"])
    conditional_stopper = ConditionalStopper()
    
    print(f"Text: '{test_text}'")
    print(f"Length: {len(test_text)}")
    print(f"LengthBasedStopper(30): {length_stopper.stop(test_text)}")
    print(f"PatternStopper(['END', 'STOP']): {pattern_stopper.stop(test_text)}")
    print(f"ConditionalStopper: {conditional_stopper.stop(test_text)}")
