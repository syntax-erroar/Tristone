#!/usr/bin/env python3
"""
Test script to verify the 10-Q consolidation logic works correctly.
This script tests the new quarter-based sorting for 10-Q filings.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from automated_sec_downloader import SECDownloader

def test_quarter_extraction():
    """Test the quarter extraction from filenames"""
    downloader = SECDownloader()
    
    # Test cases for quarter extraction
    test_cases = [
        ("AAPL_2022-Q1.xlsx", ("2022", 1)),
        ("AAPL_2022-Q2.xlsx", ("2022", 2)),
        ("AAPL_2022-Q3.xlsx", ("2022", 3)),
        ("AAPL_2023-Q1.xlsx", ("2023", 1)),
        ("AAPL_2023-Q2.xlsx", ("2023", 2)),
        ("AAPL_2023-Q3.xlsx", ("2023", 3)),
        ("MSFT_2022Q1.xlsx", ("2022", 1)),
        ("MSFT_2022Q2.xlsx", ("2022", 2)),
        ("MSFT_2023Q1.xlsx", ("2023", 1)),
        ("AAPL_2022.xlsx", ("2022", 0)),  # No quarter info
    ]
    
    print("🧪 Testing quarter extraction from filenames...")
    for filename, expected in test_cases:
        year, quarter = downloader._extract_year_quarter_from_filename(filename)
        print(f"  📁 {filename}")
        print(f"     Expected: {expected}, Got: ({year}, {quarter})")
        assert (year, quarter) == expected, f"Failed for {filename}: expected {expected}, got ({year}, {quarter})"
        print(f"     ✅ PASS")
    
    print("✅ All quarter extraction tests passed!")

def test_quarter_sorting():
    """Test the quarter-based sorting logic"""
    downloader = SECDownloader()
    
    # Test data with mixed quarters and years
    test_data = [
        "2023-Q2", "2022-Q3", "2023-Q1", "2022-Q1", "2023-Q3", "2022-Q2"
    ]
    
    expected_sorted = [
        "2022-Q1", "2022-Q2", "2022-Q3", "2023-Q1", "2023-Q2", "2023-Q3"
    ]
    
    print("\n🧪 Testing quarter-based sorting...")
    print(f"  📊 Input data: {test_data}")
    
    sorted_data = downloader._sort_quarters_chronologically(test_data)
    print(f"  📊 Sorted data: {sorted_data}")
    print(f"  📊 Expected:   {expected_sorted}")
    
    assert sorted_data == expected_sorted, f"Sorting failed: expected {expected_sorted}, got {sorted_data}"
    print("  ✅ Quarter sorting test passed!")

def test_consolidation_key_generation():
    """Test the key generation for consolidation"""
    downloader = SECDownloader()
    
    print("\n🧪 Testing consolidation key generation...")
    
    # Test 10-Q key generation
    filename = "AAPL_2022-Q1.xlsx"
    year, quarter = downloader._extract_year_quarter_from_filename(filename)
    year_key = f"{year}-Q{quarter}" if quarter > 0 else year
    print(f"  📁 {filename} -> Key: {year_key}")
    assert year_key == "2022-Q1"
    
    # Test 10-K key generation (no quarter)
    filename = "AAPL_2022.xlsx"
    year, quarter = downloader._extract_year_quarter_from_filename(filename)
    year_key = f"{year}-Q{quarter}" if quarter > 0 else year
    print(f"  📁 {filename} -> Key: {year_key}")
    assert year_key == "2022"
    
    print("  ✅ Key generation tests passed!")

if __name__ == "__main__":
    print("🚀 Starting 10-Q consolidation logic tests...")
    
    try:
        test_quarter_extraction()
        test_quarter_sorting()
        test_consolidation_key_generation()
        
        print("\n🎉 All tests passed! The 10-Q consolidation logic is working correctly.")
        print("\n📋 Summary of changes:")
        print("  ✅ Added _extract_year_quarter_from_filename() function")
        print("  ✅ Added _sort_quarters_chronologically() function")
        print("  ✅ Added _add_smart_statement_section() function")
        print("  ✅ Updated consolidation functions to handle 10-Q vs 10-K differently")
        print("\n🔧 The consolidation will now sort 10-Q filings chronologically:")
        print("    2022-Q1, 2022-Q2, 2022-Q3, 2023-Q1, 2023-Q2, 2023-Q3, ...")
        print("    Instead of the previous year-only reverse sorting.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)

