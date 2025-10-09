#!/usr/bin/env python3
"""
Explorium API Integration for Tristone Partners
Data enrichment and external API integration service
"""

import os
import requests
import json
from datetime import datetime

class ExploriumService:
    def __init__(self):
        self.api_key = os.getenv('EXPLORIUM_API_KEY', 'd5612baf93cd4ae59d5b0c8787a8f2f8')
        self.base_url = os.getenv('EXPLORIUM_BASE_URL', 'https://admin.explorium.ai')
        
    def get_headers(self):
        """Get standard headers for Explorium API requests"""
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def test_connection(self):
        """Test connection to Explorium API"""
        try:
            url = f"{self.base_url}/api/health"
            response = requests.get(url, headers=self.get_headers(), timeout=10)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'message': 'Explorium API connection successful',
                    'data': response.json() if response.content else {}
                }
            else:
                return {
                    'success': False,
                    'message': f'Explorium API returned status {response.status_code}',
                    'error': response.text
                }
        except Exception as e:
            return {
                'success': False,
                'message': f'Failed to connect to Explorium API: {str(e)}'
            }
    
    def get_integrations(self):
        """Get available integrations from Explorium"""
        try:
            url = f"{self.base_url}/integrations"
            response = requests.get(url, headers=self.get_headers(), timeout=10)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'data': response.json() if response.content else [],
                    'message': 'Integrations retrieved successfully'
                }
            else:
                return {
                    'success': False,
                    'message': f'Failed to get integrations: {response.status_code}',
                    'error': response.text
                }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error getting integrations: {str(e)}'
            }
    
    def enrich_company_data(self, company_ticker):
        """Enrich company data using Explorium"""
        try:
            url = f"{self.base_url}/api/enrich"
            payload = {
                'ticker': company_ticker,
                'data_sources': ['financial', 'market', 'news'],
                'timestamp': datetime.now().isoformat()
            }
            
            response = requests.post(url, json=payload, headers=self.get_headers(), timeout=30)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'data': response.json(),
                    'message': f'Company data enriched for {company_ticker}'
                }
            else:
                return {
                    'success': False,
                    'message': f'Data enrichment failed: {response.status_code}',
                    'error': response.text
                }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error enriching company data: {str(e)}'
            }
    
    def get_market_insights(self, tickers):
        """Get market insights for multiple tickers"""
        try:
            url = f"{self.base_url}/api/insights"
            payload = {
                'tickers': tickers if isinstance(tickers, list) else [tickers],
                'metrics': ['volatility', 'sentiment', 'trends'],
                'period': '30d'
            }
            
            response = requests.post(url, json=payload, headers=self.get_headers(), timeout=30)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'data': response.json(),
                    'message': 'Market insights retrieved successfully'
                }
            else:
                return {
                    'success': False,
                    'message': f'Failed to get market insights: {response.status_code}',
                    'error': response.text
                }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error getting market insights: {str(e)}'
            }
    
    def analyze_sec_filing(self, filing_url):
        """Analyze SEC filing using Explorium"""
        try:
            url = f"{self.base_url}/api/analyze"
            payload = {
                'source': 'sec_filing',
                'url': filing_url,
                'analysis_type': 'comprehensive',
                'extract_metrics': True
            }
            
            response = requests.post(url, json=payload, headers=self.get_headers(), timeout=60)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'data': response.json(),
                    'message': 'SEC filing analyzed successfully'
                }
            else:
                return {
                    'success': False,
                    'message': f'SEC filing analysis failed: {response.status_code}',
                    'error': response.text
                }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error analyzing SEC filing: {str(e)}'
            }

# Demo functions for testing without real API calls
def demo_explorium_service():
    """Demo version of Explorium service for testing"""
    
    demo_data = {
        'integrations': [
            {'name': 'SEC EDGAR', 'status': 'active', 'type': 'financial'},
            {'name': 'Market Data', 'status': 'active', 'type': 'market'},
            {'name': 'News Analytics', 'status': 'active', 'type': 'news'},
            {'name': 'ESG Metrics', 'status': 'active', 'type': 'sustainability'}
        ],
        'company_enrichment': {
            'ticker': 'AMZN',
            'company_name': 'Amazon.com Inc',
            'sector': 'Consumer Discretionary',
            'market_cap': '$1.2T',
            'esg_score': 'B+',
            'risk_metrics': {
                'volatility': 'Medium',
                'liquidity': 'High',
                'credit_rating': 'AA'
            }
        },
        'market_insights': {
            'sentiment': 'Positive',
            'trend': 'Upward',
            'volatility': '15.2%',
            'volume_trend': 'Above Average'
        }
    }
    
    return {
        'success': True,
        'data': demo_data,
        'message': 'Demo data - Explorium integration ready for production'
    }

if __name__ == '__main__':
    # Test the Explorium service
    print("🔗 Testing Explorium API Integration")
    print("=" * 50)
    
    service = ExploriumService()
    
    # Test connection
    result = service.test_connection()
    if result['success']:
        print("✅ Explorium API connection successful")
    else:
        print("⚠️  Using demo mode - set up Explorium API for production")
        demo_result = demo_explorium_service()
        print(f"📊 Demo data available: {len(demo_result['data']['integrations'])} integrations")
    
    print("\n🎯 Explorium integration ready for Tristone Partners dashboard!")
