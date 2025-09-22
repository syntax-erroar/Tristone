# Tristone Financial Data Extraction Tools

This repository contains comprehensive tools for extracting and processing financial data from SEC filings and other sources.

## 🚀 Main Tools

### 1. SEC Table Extractor (`sec_table_extractor.py`)
- **Purpose**: Extract all financial tables from SEC 10-K, 10-Q, and 8-K filings
- **Features**: 
  - No filtering - extracts all tables from SEC filings
  - Multi-year data extraction (1-10 years)
  - Automatic Excel file generation
  - Currency formatting and data cleaning

**Usage:**
```bash
python sec_table_extractor.py
# Enter: MSFT (or any ticker)
# Enter: 10-K (or 10-Q, 8-K)
# Enter: 5 (number of years)
```

### 2. Year-Based Table Filter (`year_based_table_filter.py`)
- **Purpose**: Filter existing Excel files to keep only tables with year-based financial data
- **Features**:
  - Identifies tables with years in first column
  - Preserves formatting and structure
  - Configurable confidence thresholds

**Usage:**
```bash
python year_based_table_filter.py input_file.xlsx output_file.xlsx
```

### 3. Batch Processor (`batch_year_filter.py`)
- **Purpose**: Process multiple Excel files at once
- **Features**:
  - Pattern-based file selection
  - Organized output directory
  - Comprehensive statistics

**Usage:**
```bash
python batch_year_filter.py "*_Multi_Year_Cleaned.xlsx"
```

### 4. Universal HTML Table Extractor (`universal_html_table_extractor.py`)
- **Purpose**: Extract tables from any HTML source
- **Features**:
  - Multiple extraction methods
  - Data cleaning and validation
  - Flexible output formats

### 5. Financial Data Consolidator (`consolidate_financial_data.py`)
- **Purpose**: Consolidate and merge financial data from multiple sources
- **Features**:
  - Data deduplication
  - Format standardization
  - Quality validation

## 📊 Key Features

- **No Filtering**: The main extractor now extracts ALL tables without any filtering
- **Year-Based Filtering**: Optional filtering for tables with year headers
- **Batch Processing**: Handle multiple files efficiently
- **Data Quality**: Automatic cleaning and formatting
- **Multiple Formats**: Support for various input and output formats

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/tristone-financial-spread/Tristone.git
cd Tristone
```

2. Install required packages:
```bash
pip install openpyxl lxml requests
```

3. Get SEC API key from [sec-api.io](https://sec-api.io) and update the API key in `sec_table_extractor.py`

## 📁 File Structure

```
├── sec_table_extractor.py          # Main SEC extractor (no filtering)
├── year_based_table_filter.py      # Year-based table filter
├── batch_year_filter.py            # Batch processor
├── universal_html_table_extractor.py # Universal HTML extractor
├── consolidate_financial_data.py   # Data consolidator
├── YEAR_BASED_FILTERING_SOLUTION.md # Detailed documentation
└── README.md                       # This file
```

## 🎯 Use Cases

1. **Complete Data Extraction**: Extract all financial tables from SEC filings
2. **Selective Filtering**: Filter for specific year-based financial data
3. **Batch Processing**: Process multiple companies or time periods
4. **Data Consolidation**: Merge and clean financial data from multiple sources

## 📈 Example Output

The tools generate Excel files with:
- Separate sheets for each year/period
- All financial tables (no filtering)
- Proper currency formatting
- Clean, organized data structure

## 🔍 Recent Changes

- **Removed Aggressive Filtering**: The main extractor now extracts all tables without filtering
- **Simplified Logic**: Focus on comprehensive data extraction rather than selective filtering
- **Enhanced Documentation**: Complete usage guide and examples

## 📞 Support

For questions or issues, please refer to the detailed documentation in `YEAR_BASED_FILTERING_SOLUTION.md` or create an issue in the repository.

## 📄 License

This project is proprietary to Tristone Strategic Partners LLP.
