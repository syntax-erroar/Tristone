#!/usr/bin/env python3
"""
Test script to verify that year headers are not formatted as currency
"""

import re

def _is_year_header(content: str) -> bool:
    """Check if content is a year header (e.g., 2021, 2022, 2023)"""
    if not content:
        return False
    
    # Check if it's a 4-digit year
    if content.isdigit() and len(content) == 4:
        year = int(content)
        # Check if it's a reasonable year (1900-2100)
        if 1900 <= year <= 2100:
            return True
    
    return False

def _is_non_currency_number(content: str) -> bool:
    """Check if content is a number that shouldn't be formatted as currency"""
    if not content:
        return False
    
    # Check for common non-currency numbers
    non_currency_patterns = [
        r'^\d{4}$',  # 4-digit years
        r'^\d{1,2}$',  # Single or double digit numbers (likely row numbers, percentages, etc.)
        r'^\d+\.\d{1,2}$',  # Decimal numbers with 1-2 decimal places (likely percentages, ratios)
        r'^\d+%$',  # Numbers with percentage sign
        r'^\d+\.\d+$',  # Decimal numbers (could be ratios, not currency)
    ]
    
    for pattern in non_currency_patterns:
        if re.match(pattern, content.strip()):
            return True
    
    return False

def test_year_header_detection():
    """Test year header detection"""
    
    test_cases = [
        # Should be detected as year headers (should NOT be formatted as currency)
        ("2021", True, "Year header"),
        ("2022", True, "Year header"),
        ("2023", True, "Year header"),
        ("2024", True, "Year header"),
        ("2025", True, "Year header"),
        ("1999", True, "Year header"),
        ("2100", True, "Year header"),
        
        # Should NOT be detected as year headers (should be formatted as currency)
        ("2021.5", False, "Decimal year - not a year header"),
        ("202", False, "3-digit number - not a year header"),
        ("20211", False, "5-digit number - not a year header"),
        ("71,074", False, "Financial number - should be currency"),
        ("168,088", False, "Financial number - should be currency"),
        ("61,271", False, "Financial number - should be currency"),
        ("8.12", False, "Decimal number - could be currency"),
        ("1", False, "Single digit - not a year header"),
        ("12", False, "Double digit - not a year header"),
        ("123", False, "Triple digit - not a year header"),
    ]
    
    print("🧪 Testing Year Header Detection")
    print("=" * 50)
    
    all_passed = True
    
    for i, (content, expected_is_year, description) in enumerate(test_cases, 1):
        is_year = _is_year_header(content)
        passed = is_year == expected_is_year
        
        status = "✅ PASS" if passed else "❌ FAIL"
        currency_action = "SKIP currency formatting" if is_year else "APPLY currency formatting"
        print(f"{i:2d}. {status} | '{content}' -> {currency_action} ({description})")
        
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All year header detection tests passed!")
    else:
        print("❌ Some year header detection tests failed.")
    
    return all_passed

def test_non_currency_detection():
    """Test non-currency number detection"""
    
    test_cases = [
        # Should be detected as non-currency (should NOT be formatted as currency)
        ("2021", True, "Year header"),
        ("2022", True, "Year header"),
        ("1", True, "Single digit"),
        ("12", True, "Double digit"),
        ("8.12", True, "Decimal with 2 places"),
        ("5.5", True, "Decimal with 1 place"),
        ("15%", True, "Percentage"),
        ("100%", True, "Percentage"),
        
        # Should NOT be detected as non-currency (should be formatted as currency)
        ("71,074", False, "Financial number - should be currency"),
        ("168,088", False, "Financial number - should be currency"),
        ("61,271", False, "Financial number - should be currency"),
        ("1,234.56", False, "Large decimal - could be currency"),
        ("123456", False, "Large number - could be currency"),
    ]
    
    print("\n🧪 Testing Non-Currency Number Detection")
    print("=" * 50)
    
    all_passed = True
    
    for i, (content, expected_is_non_currency, description) in enumerate(test_cases, 1):
        is_non_currency = _is_non_currency_number(content)
        passed = is_non_currency == expected_is_non_currency
        
        status = "✅ PASS" if passed else "❌ FAIL"
        currency_action = "SKIP currency formatting" if is_non_currency else "APPLY currency formatting"
        print(f"{i:2d}. {status} | '{content}' -> {currency_action} ({description})")
        
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All non-currency detection tests passed!")
    else:
        print("❌ Some non-currency detection tests failed.")
    
    return all_passed

if __name__ == "__main__":
    print("🔧 Testing Currency Formatting Logic")
    print("=" * 60)
    
    year_test_passed = test_year_header_detection()
    non_currency_test_passed = test_non_currency_detection()
    
    print(f"\n📊 Overall Results:")
    print(f"   Year Header Detection: {'✅ PASS' if year_test_passed else '❌ FAIL'}")
    print(f"   Non-Currency Detection: {'✅ PASS' if non_currency_test_passed else '❌ FAIL'}")
    
    if year_test_passed and non_currency_test_passed:
        print(f"\n🎉 SUCCESS: Year headers will no longer be formatted as currency!")
    else:
        print(f"\n❌ FAILED: Some issues remain with currency formatting logic.")
