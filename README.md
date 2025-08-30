# 🏢 Enhanced SEC Financial Model Generator

A comprehensive Python tool for generating financial models from SEC EDGAR data using advanced XBRL processing, semantic matching, and validation.

## 🚨 Current Status: Version 1.0 - Accuracy Improvements Needed

**Working Features:**
- ✅ SEC EDGAR API integration
- ✅ AI-powered XBRL classification  
- ✅ Multi-sheet Excel export
- ✅ Market data integration
- ✅ Comprehensive reporting

**Known Issues (Priority Fixes):**
- ⚠️ Revenue classification accuracy needs improvement
- ⚠️ Data aggregation logic requires refinement
- ⚠️ Cost of revenue classification issues

## Features

- **SEC EDGAR API Integration**: Fetches company facts and XBRL data directly from SEC
- **Semantic Matching**: Uses AI-powered concept matching with sentence transformers
- **Pattern-Based Fallback**: Traditional keyword and pattern-based matching
- **Data Validation**: Context validation and cross-validation of financial relationships
- **Quality Scoring**: Calculates data quality scores based on completeness, consistency, accuracy, and timeliness
- **Derived Metrics**: Calculates Gross Profit, EBITDA, EBIT, Free Cash Flow, ROA, and more
- **Financial Projections**: Generates projections using historical trends and industry benchmarks
- **Market Data Integration**: Fetches current market data using Yahoo Finance API

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **First Run Setup** (uncomment in sec_financial_model.py):
   ```python
   # Uncomment the next line for first run
   install_packages()
   ```

## Usage

### Basic Usage

Run the main script:
```bash
python sec_financial_model.py
```

The script will prompt you for:
- Company name (default: Microsoft Corporation)
- Ticker symbol (default: MSFT)
- CIK number (default: 0000789019)
- Email address (required for SEC API compliance)
- Fiscal year end (default: 0630)

### Programmatic Usage

```python
from sec_financial_model import EnhancedSECFinancialModelGenerator

# Initialize the model generator
model = EnhancedSECFinancialModelGenerator(
    company_name="Microsoft Corporation",
    ticker="MSFT",
    cik="0000789019",
    user_agent_email="your.email@example.com",
    fiscal_year_end="0630"
)

# Fetch data
model.fetch_sec_data()
model.fetch_market_data()

# Classify metrics
model.find_and_classify_metrics()

# Calculate derived metrics
model.calculate_derived_metrics()

# Generate projections
model.generate_projections([2025, 2026, 2027])

# Access results
print(f"Categories matched: {len(model.standardized_categories)}")
print(f"Market cap: ${model.market_data['market_cap']:,.0f}M")
```

### Testing

Run the test script to verify functionality:
```bash
python test_sec_model.py
```

## Output

The tool provides:

1. **Classification Results**: Matched financial metrics with confidence scores
2. **Data Quality Analysis**: Quality scores for each category
3. **Financial Metrics**: Historical and projected financial data
4. **Market Data**: Current market information and valuation metrics

## Key Financial Concepts Supported

- **Revenue**: Total revenue from operations
- **Cost of Revenue**: Direct costs of goods sold
- **Operating Income**: Income from operations
- **Net Income**: Net earnings after tax
- **Cash Flow Operations**: Operating cash flow
- **Cash Equivalents**: Cash and short-term investments
- **Total Assets**: Balance sheet assets
- **Total Liabilities**: Balance sheet liabilities

## Derived Metrics

- **Gross Profit**: Revenue minus cost of revenue
- **EBITDA**: Earnings before interest, taxes, depreciation, and amortization
- **EBIT**: Earnings before interest and taxes
- **Free Cash Flow**: Operating cash flow minus capital expenditures
- **ROA**: Return on Assets

## Data Sources

- **SEC EDGAR API**: Financial statements and XBRL data
- **Yahoo Finance API**: Market data and stock information
- **Semantic Matching**: AI-powered concept matching using sentence transformers

## Requirements

- Python 3.7+
- Internet connection for API access
- Valid email address for SEC API compliance

## Dependencies

See `requirements.txt` for the complete list of dependencies, including:
- pandas, numpy, requests
- yfinance, openpyxl
- sentence-transformers, scikit-learn
- torch, transformers
- lxml, python-dateutil

## Limitations

- Requires valid SEC CIK number
- Internet connection required for data fetching
- Some advanced features require additional dependencies
- Projections are estimates based on historical trends

## License

This tool is provided for educational and research purposes. Please ensure compliance with SEC API usage guidelines and terms of service for all data sources.
