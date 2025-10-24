# SEC Tools Suite - User Guide

## 🚀 Overview

The SEC Tools Suite is a comprehensive web application for downloading, analyzing, and processing SEC EDGAR filings. It provides multiple tools to help financial analysts, researchers, and investors work with SEC data more efficiently.

## 🔐 Getting Started

### Accessing the App
1. **Web App**: Visit your deployed Streamlit app URL
2. **Login**: Use the provided credentials to access the application
3. **Navigation**: Use the tabs at the top to switch between different tools

### Default Credentials
- **Email**: `nishit.wadhwani@tristone-partners.com`
- **Password**: `Nishit@120304`

## 📊 Available Tools

### 1. Automated Downloader (Primary Tool)
**Purpose**: Download and consolidate SEC Excel filings for any company

#### How to Use:
1. **Enter Company Details**:
   - **Ticker**: Enter the stock symbol (e.g., AAPL, AMZN, TSLA, BRK-B)
   - **Form Type**: Choose 10-K (annual) or 10-Q (quarterly)
   - **Date Range**: Select start and end dates for filings

2. **Advanced Options**:
   - **Download Both**: Check to download both 10-K and 10-Q filings
   - **Date Range**: Specify the time period for filings

3. **Run Download**:
   - Click "Run Automated Download"
   - Wait for processing (usually 1-3 minutes)
   - Download individual files or all files as ZIP

#### What You Get:
- **Individual Financial Statements**: Separate Excel files for each year/quarter
- **Master Consolidated File**: All years combined in one workbook
- **Cleaned Versions**: Files with empty rows/columns removed
- **Deduplicated Versions**: Files with duplicate entries merged

#### Important Files to Look At:
1. **`{TICKER}_{FORM}_Master_Consolidated_Financials_Detailed.xlsx`**
   - Complete financial data across all years
   - Best for comprehensive analysis
   - Contains all three financial statements

2. **`{TICKER}_{FORM}_Master_Consolidated_Financials_RemovedEmptyRowsCols_deduplicated_after_merge.xlsx`**
   - Clean, deduplicated data
   - Best for analysis and modeling
   - Yellow highlighting shows merged rows

3. **Individual Year Files** (e.g., `2024-10K_Individual_Financials.xlsx`)
   - Single year data
   - Good for year-over-year comparisons

### 2. XBRL JSON → Excel
**Purpose**: Convert XBRL JSON data to Excel format

#### How to Use:
1. Upload XBRL JSON file
2. Click "Convert to Excel"
3. Download the converted file

### 3. Full-Text Search
**Purpose**: Search through SEC filings using advanced queries

#### How to Use:
1. **Build Query**: Use the query builder or enter custom queries
2. **Filters**: Apply form types, date ranges, and CIK filters
3. **Search**: Click "Run Search" to execute
4. **Results**: View and download results as CSV

#### Query Examples:
- `"revenue" AND "growth"`
- `"accounts receivable" AND "allowance"`
- `"cash flow" OR "operating activities"`

### 4. Download/PDF
**Purpose**: Download original SEC filings or convert to PDF

#### Modes:
- **Download Original**: Get the original filing files
- **Generate PDF**: Convert HTML filings to PDF format

### 5. Extractor
**Purpose**: Extract specific data from 10-K, 10-Q, or 8-K filings

#### How to Use:
1. Enter filing URL or accession number
2. Select extraction type
3. Run extraction
4. Download results

### 6. Stream
**Purpose**: Real-time SEC filing monitoring

#### Setup:
1. Install required packages: `pip install websocket-client`
2. Run: `python stream_listener.py --out-jsonl stream.jsonl`

## 📁 Understanding the Output Files

### File Naming Convention
```
SEC_Excel_Downloads_{TICKER}_{FORM}/
├── {YEAR}-{FORM}_Individual_Financials.xlsx
├── {TICKER}_{FORM}_Master_Consolidated_Financials_Detailed.xlsx
├── {TICKER}_{FORM}_Master_Consolidated_Financials_RemovedEmptyRowsCols.xlsx
├── {TICKER}_{FORM}_Master_Consolidated_Financials_RemovedEmptyRowsCols_deduplicated_before_merge.xlsx
└── {TICKER}_{FORM}_Master_Consolidated_Financials_RemovedEmptyRowsCols_deduplicated_after_merge.xlsx
```

### File Types Explained

#### 1. Individual Financials
- **Purpose**: Single year/quarter data
- **Use Case**: Year-over-year analysis
- **Contains**: Complete financial statements for one period

#### 2. Master Consolidated (Detailed)
- **Purpose**: All years combined with full detail
- **Use Case**: Comprehensive historical analysis
- **Contains**: All financial data across all periods

#### 3. Removed Empty Rows/Columns
- **Purpose**: Clean data without empty cells
- **Use Case**: Data analysis and modeling
- **Contains**: Only meaningful data

#### 4. Deduplicated Versions
- **Purpose**: Merged duplicate entries
- **Use Case**: Final analysis and reporting
- **Contains**: Clean, consolidated data
- **Note**: Yellow highlighting shows merged rows

## 🎯 Best Practices

### For Financial Analysis
1. **Start with Master Consolidated**: Get the big picture first
2. **Use Deduplicated Files**: For final analysis and modeling
3. **Check Individual Files**: For specific year investigations
4. **Look for Yellow Highlighting**: Indicates merged/consolidated data

### For Data Quality
1. **Verify Ticker Symbols**: Use correct stock symbols (e.g., BRK-B, not BRK.B)
2. **Check Date Ranges**: Ensure you're getting the right time period
3. **Review Merged Data**: Yellow highlighted rows show where duplicates were combined

### For Different Use Cases
- **Investment Research**: Use Master Consolidated files
- **Academic Research**: Use Individual files for specific periods
- **Financial Modeling**: Use Deduplicated files
- **Quick Analysis**: Use Removed Empty Rows/Columns files

## 🔧 Troubleshooting

### Common Issues

#### 1. "0 files found" Error
- **Cause**: Incorrect ticker symbol or no filings in date range
- **Solution**: Verify ticker symbol and expand date range

#### 2. Download Buttons Not Working
- **Cause**: Browser blocking downloads or file too large
- **Solution**: Try individual file downloads or use ZIP download

#### 3. Incomplete Data
- **Cause**: SEC filing may not have Excel attachments
- **Solution**: Try different form types or date ranges

#### 4. Duplicate Data Not Merged
- **Cause**: Data may have different formatting or naming
- **Solution**: Check the deduplicated files - they should have merged similar entries

### File Size Considerations
- **Large Files**: Use ZIP download for multiple files
- **Individual Downloads**: Better for specific files
- **Browser Limits**: Some browsers have download size limits

## 📈 Advanced Features

### Data Consolidation
The app automatically:
- **Merges Duplicates**: Combines similar financial metrics
- **Fills Gaps**: Handles missing data across years
- **Normalizes Formats**: Standardizes data presentation
- **Highlights Changes**: Shows where data was merged

### Quality Indicators
- **Yellow Highlighting**: Merged/consolidated rows
- **File Sizes**: Larger files typically have more complete data
- **Row Counts**: More rows indicate more detailed financial data

## 🆘 Support

### Getting Help
1. **Check File Names**: Ensure you're looking at the right file type
2. **Verify Data**: Compare with original SEC filings if needed
3. **Try Different Options**: Use different form types or date ranges
4. **Contact Support**: Reach out to the development team for issues

### Data Sources
- **SEC EDGAR Database**: All data comes from official SEC filings
- **Real-time Processing**: Data is processed when you run the tool
- **No Storage**: Files are generated on-demand

## 🎉 Success Tips

1. **Start Simple**: Begin with well-known companies (AAPL, MSFT, AMZN)
2. **Use Recent Data**: Recent filings typically have better Excel attachments
3. **Check Multiple Forms**: Try both 10-K and 10-Q for comprehensive data
4. **Download Everything**: Use the ZIP option to get all files at once
5. **Review the Data**: Always check the output files to ensure data quality

---

**Happy Analyzing!** 🚀

This tool is designed to make SEC data analysis faster and more efficient. If you have questions or need help, don't hesitate to reach out to the development team.

