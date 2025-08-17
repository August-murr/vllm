# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

from abc import ABC, abstractmethod


class StoppingCriteria(ABC):
    """Abstract base class for custom stopping criteria.
    
    Users should inherit from this class to implement custom stopping logic
    that goes beyond the built-in stop strings and stop token IDs.
    
    Example:
        class MyCustomStopper(StoppingCriteria):
            def stop(self, text: str) -> bool:
                return "CUSTOM_END" in text and len(text) > 100
    """
    
    @abstractmethod
    def stop(self, text: str) -> bool:
        """Determine if generation should stop based on the current output text.
        
        Args:
            text: The current generated text string
            
        Returns:
            True if generation should stop, False otherwise.
        """
        raise NotImplementedError
