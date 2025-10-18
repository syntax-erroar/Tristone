#!/usr/bin/env python3
import re

def test_regex():
    test_cases = ["71,074 $", "168,088 $", "61,271 $", "8.12 $"]
    
    for case in test_cases:
        print(f"Testing: '{case}'")
        
        # Test the current pattern
        result1 = re.sub(r'([\d,]+\.?\d*)\s+\$', r'\1$', case)
        print(f"  Pattern 1: '{result1}'")
        
        # Test a simpler pattern
        result2 = re.sub(r'(\d[\d,]*\.?\d*)\s+\$', r'\1$', case)
        print(f"  Pattern 2: '{result2}'")
        
        # Test with word boundary
        result3 = re.sub(r'(\d[\d,]*\.?\d*)\s+\$', r'\1$', case)
        print(f"  Pattern 3: '{result3}'")
        
        print()

if __name__ == "__main__":
    test_regex()
