#!/usr/bin/env python3
"""
Test script to demonstrate the currency formatting fix
"""

import re

def _fix_currency_formatting(content: str) -> str:
    """Fix currency formatting issues where dollar signs are separated from numbers"""
    if not content:
        return content
    
    # Pattern to match dollar signs followed by whitespace and then numbers
    # This handles cases like "$ 71,074" or "$71,074" 
    content = re.sub(r'\$\s+(\d)', r'$\1', content)
    
    # Pattern to match numbers followed by whitespace and then dollar signs
    # This handles cases like "71,074 $" - need to be more specific about what constitutes a number
    content = re.sub(r'([\d,]+\.?\d*)\s+\$', r'\1$', content)
    
    # Pattern to match standalone dollar signs that should be attached to the next number
    # This handles cases where $ is in a separate cell from the number
    content = re.sub(r'\$\s*$', '', content)  # Remove trailing dollar signs
    
    # Clean up any remaining extra whitespace
    content = re.sub(r'\s+', ' ', content).strip()
    
    return content

def test_currency_fixes():
    """Test various currency formatting scenarios"""
    
    test_cases = [
        # Input -> Expected Output
        ("$ 71,074", "$71,074"),
        ("71,074 $", "71,074$"),
        ("$", ""),  # Standalone dollar sign should be removed
        ("$71,074", "$71,074"),  # Already correct
        ("71,074", "71,074"),  # No dollar sign
        ("$ 168,088", "$168,088"),
        ("168,088 $", "168,088$"),
        ("$ 61,271", "$61,271"),
        ("61,271 $", "61,271$"),
        ("$ 8.12", "$8.12"),
        ("8.12 $", "8.12$"),
    ]
    
    print("🧪 Testing Currency Formatting Fix")
    print("=" * 50)
    
    all_passed = True
    
    for i, (input_text, expected) in enumerate(test_cases, 1):
        result = _fix_currency_formatting(input_text)
        passed = result == expected
        
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{i:2d}. {status} | '{input_text}' -> '{result}' (expected: '{expected}')")
        
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Currency formatting fix is working correctly.")
    else:
        print("❌ Some tests failed. Currency formatting fix needs improvement.")
    
    return all_passed

if __name__ == "__main__":
    test_currency_fixes()
