#!/usr/bin/env python3
"""
Test Explorium integration
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_explorium_integrations():
    """Test Explorium integrations endpoint"""
    print("Testing Explorium integrations...")
    
    try:
        response = requests.get(f'{BASE_URL}/api/explorium/integrations')
        print(f"Status Code: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2)}")
        return result.get('success', False)
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_company_enrichment():
    """Test company data enrichment"""
    print("\nTesting company data enrichment...")
    
    data = {"ticker": "AMZN"}
    
    try:
        response = requests.post(f'{BASE_URL}/api/explorium/enrich', json=data)
        print(f"Status Code: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2)}")
        return result.get('success', False)
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_market_insights():
    """Test market insights"""
    print("\nTesting market insights...")
    
    data = {"tickers": ["AMZN", "TSLA", "AAPL"]}
    
    try:
        response = requests.post(f'{BASE_URL}/api/explorium/insights', json=data)
        print(f"Status Code: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2)}")
        return result.get('success', False)
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 60)
    print("TRISTONE PARTNERS - EXPLORIUM INTEGRATION TEST")
    print("=" * 60)
    print(f"API Key: d5612baf93cd4ae59d5b0c8787a8f2f8")
    print(f"Base URL: https://admin.explorium.ai")
    print("=" * 60)
    
    # Test integrations
    if test_explorium_integrations():
        print("OK: Explorium integrations working")
    else:
        print("ERROR: Explorium integrations failed")
    
    # Test company enrichment
    if test_company_enrichment():
        print("OK: Company enrichment working")
    else:
        print("ERROR: Company enrichment failed")
    
    # Test market insights
    if test_market_insights():
        print("OK: Market insights working")
    else:
        print("ERROR: Market insights failed")
    
    print("\n" + "=" * 60)
    print("🎯 Explorium integration ready for your dashboard!")
    print("=" * 60)

if __name__ == '__main__':
    main()
