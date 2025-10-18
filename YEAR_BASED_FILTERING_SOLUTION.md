# Year-Based Financial Table Filtering Solution

## Overview

This solution provides comprehensive filtering for Excel files containing SEC financial data to extract only tables with year-based financial information (e.g., tables with column headers like 2021, 2022, 2023, etc.).

## Problem Solved

When extracting financial data from SEC filings, you often get many tables, but you're only interested in those that contain:
- Year headers (2021, 2022, 2023, etc.)
- Financial data across multiple years
- Standard financial statement information (Income Statement, Balance Sheet, Cash Flow, etc.)

## Solution Components

### 1. Modified SEC Table Extractor (`sec_table_extractor.py`)

**Changes Made:**
- Added `_is_year_based_financial_table()` method
- Modified `extract_tables_from_html()` to filter tables during extraction
- Only extracts tables that contain year-based financial data

**Key Features:**
- Detects 4-digit years (1900-2099) in table headers
- Identifies financial content using keywords and currency patterns
- Requires at least 2 years and financial content for inclusion
- Works with various table formats (Microsoft, Apple, etc.)

### 2. Standalone Filter (`year_based_table_filter.py`)

**Purpose:** Filter existing Excel files to keep only year-based financial tables

**Usage:**
```bash
python year_based_table_filter.py input_file.xlsx output_file.xlsx
```

**Features:**
- Analyzes table structure and confidence scores
- Classifies table types (Income Statement, Balance Sheet, etc.)
- Preserves formatting and creates organized output
- Configurable confidence thresholds

### 3. Batch Processor (`batch_year_filter.py`)

**Purpose:** Process multiple Excel files at once

**Usage:**
```bash
python batch_year_filter.py "*_Multi_Year_Cleaned.xlsx"
python batch_year_filter.py "MSFT_*.xlsx" filtered_msft
```

**Features:**
- Processes multiple files matching a pattern
- Creates organized output directory
- Provides comprehensive statistics
- Error handling for individual files

## How It Works

### 1. Year Detection
- Looks for 4-digit years (1900-2099) in table cells
- Handles both standalone years and years embedded in text
- Uses regex pattern: `\b(19|20)\d{2}\b`

### 2. Financial Content Detection
- Identifies financial keywords: revenue, income, assets, liabilities, equity, cash, etc.
- Detects currency patterns: $123,456, (123,456), 123,456.78
- Analyzes content density across table rows

### 3. Confidence Scoring
- **Year Headers (50%):** Base score for having year headers
- **Year Count (40%):** More years = higher confidence (3+ years gets max score)
- **Financial Content (20%):** Ratio of financial content rows
- **Multiple Columns (10%):** Bonus for multiple year columns

### 4. Table Classification
- **Income Statement:** Contains "income statement", "operations"
- **Balance Sheet:** Contains "balance sheet", "assets", "liabilities"
- **Cash Flow:** Contains "cash flow"
- **Comprehensive Income:** Contains "comprehensive income"
- **Shareholders Equity:** Contains "equity", "shareholders"

## Usage Examples

### Example 1: Filter Single File
```bash
python year_based_table_filter.py MSFT_10-K_Multi_Year_Cleaned.xlsx MSFT_Filtered.xlsx
```

**Output:**
```
✓ Filtered file saved: MSFT_Filtered.xlsx

=== Filtering Results ===
Input file: MSFT_10-K_Multi_Year_Cleaned.xlsx
Output file: MSFT_Filtered.xlsx
Sheets processed: 5
Tables found: 243
Tables kept: 243
Sheets kept: 5
Sheets with year-based tables: 2025_06_30, 2024_06_30, 2023_06_30, 2022_06_30, 2021_06_30
```

### Example 2: Batch Process Multiple Files
```bash
python batch_year_filter.py "*_Multi_Year_Cleaned.xlsx"
```

**Output:**
```
Found 2 Excel files to process
Output directory: filtered_output
--------------------------------------------------

Processing: AAPL_10-K_Multi_Year_Cleaned.xlsx
  ✓ Success: 503 tables kept from 503 found
  ✓ Output: filtered_output/AAPL_10-K_Multi_Year_Cleaned_YearBased_Filtered.xlsx

Processing: MSFT_10-K_Multi_Year_Cleaned.xlsx
  ✓ Success: 243 tables kept from 243 found
  ✓ Output: filtered_output/MSFT_10-K_Multi_Year_Cleaned_YearBased_Filtered.xlsx

==================================================
BATCH PROCESSING SUMMARY
==================================================
Files processed: 2
Files successful: 2
Total tables found: 746
Total tables kept: 746
Total sheets kept: 10
Average tables per file: 373.0

Filtered files saved in: filtered_output
```

### Example 3: Use Modified Extractor for New Data
```bash
python sec_table_extractor.py
# Enter: MSFT
# Enter: 10-K
# Enter: 5
```

The modified extractor will now automatically filter for year-based tables during extraction.

## Configuration Options

### Confidence Threshold
Modify the confidence threshold in `year_based_table_filter.py`:
```python
# Line 183: Change from 0.6 to desired threshold
if analysis['confidence_score'] >= 0.6:
```

**Thresholds:**
- **0.3-0.5:** More permissive, includes more tables
- **0.6-0.7:** Balanced (recommended)
- **0.8-0.9:** Strict, only high-confidence tables

### Financial Keywords
Add or modify keywords in the `financial_keywords` list:
```python
financial_keywords = [
    'revenue', 'income', 'assets', 'liabilities', 'equity', 'cash',
    'operating', 'gross margin', 'net income', 'total revenue',
    # Add your custom keywords here
]
```

## File Structure

```
├── sec_table_extractor.py          # Modified extractor with filtering
├── year_based_table_filter.py      # Standalone filter
├── batch_year_filter.py            # Batch processor
├── analyze_excel_structure.py      # Analysis tool
└── YEAR_BASED_FILTERING_SOLUTION.md # This documentation
```

## Benefits

1. **Focused Data:** Only extracts relevant year-based financial tables
2. **Universal:** Works with all companies and SEC filing types
3. **Configurable:** Adjustable confidence thresholds and keywords
4. **Batch Processing:** Handle multiple files efficiently
5. **Quality Control:** Confidence scoring ensures data relevance
6. **Preserved Formatting:** Maintains Excel formatting and structure

## Troubleshooting

### No Tables Found
- Check confidence threshold (try lowering to 0.3)
- Verify input file has year headers
- Check if financial keywords match your data

### Too Many Tables
- Increase confidence threshold (try 0.7 or 0.8)
- Add more specific financial keywords
- Check table boundary detection

### Performance Issues
- Use batch processing for multiple files
- Consider processing smaller file sets
- Check available memory for large files

## Future Enhancements

1. **Machine Learning:** Train models to better identify financial tables
2. **Custom Patterns:** Support for company-specific table formats
3. **Data Validation:** Verify extracted data against known financial statements
4. **Export Options:** Support for CSV, JSON, and other formats
5. **GUI Interface:** User-friendly interface for non-technical users
