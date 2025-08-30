#!/usr/bin/env python3
"""
Test script for the SEC Financial Model Generator
"""

# Import the main module
from sec_financial_model import EnhancedSECFinancialModelGenerator

def test_basic_functionality():
    """Test basic initialization and data fetching"""
    print("Testing SEC Financial Model Generator...")
    
    # Test with Microsoft data
    company_name = "Microsoft Corporation"
    ticker = "MSFT"
    cik = "0000789019"
    email = "test@example.com"
    fiscal_year_end = "0630"
    
    try:
        # Initialize the model generator
        print("Initializing model generator...")
        model = EnhancedSECFinancialModelGenerator(
            company_name, ticker, cik, email, fiscal_year_end
        )
        
        print("✓ Model generator initialized successfully")
        
        # Test SEC data fetching
        print("\nTesting SEC data fetching...")
        if model.fetch_sec_data():
            print("✓ SEC data fetched successfully")
            print(f"  Found {len(model.facts_data.get('facts', {}))} taxonomies")
        else:
            print("✗ Failed to fetch SEC data")
            return False
        
        # Test market data fetching
        print("\nTesting market data fetching...")
        model.fetch_market_data()
        print("✓ Market data fetched successfully")
        print(f"  Market cap: ${model.market_data.get('market_cap', 0):,.0f}M")
        
        # Test metric classification
        print("\nTesting metric classification...")
        model.find_and_classify_metrics()
        print(f"✓ Classification complete: {len(model.standardized_categories)} categories matched")
        
        # Show some results
        print("\nClassification Results:")
        for category, data in model.standardized_categories.items():
            display_name = data.get('display_name', category)
            method = data.get('method', 'unknown')
            confidence = data.get('confidence', 0)
            print(f"  {display_name}: {method} (confidence: {confidence:.2f})")
        
        print("\n✓ All tests passed successfully!")
        return True
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_basic_functionality()
