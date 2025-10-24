# SEC Tools Suite - Technical Documentation

## 🏗️ Architecture

### Core Components
- **Frontend**: Streamlit web application (`app.py`)
- **Backend**: Python modules for data processing
- **Database**: SQLite for user authentication
- **Storage**: Temporary files on Streamlit Cloud

### Key Files Structure
```
├── app.py                          # Main Streamlit application
├── automated_sec_downloader.py     # Core SEC data processing
├── xbrl_json_to_excel.py          # XBRL conversion utilities
├── full_text_search.py            # SEC filing search functionality
├── filing_download_pdf.py         # PDF generation utilities
├── extractor_api.py               # Data extraction API
├── requirements.txt               # Python dependencies
├── tristone_auth.db              # User authentication database
└── config.env                    # Environment configuration
```

## 🔧 Core Modules

### 1. Automated SEC Downloader (`automated_sec_downloader.py`)

#### Main Class: `AdvancedSECDownloader`
```python
class AdvancedSECDownloader:
    def __init__(self, api_key: str)
    def automated_download_with_range(self, ticker, form_type, start_date, end_date)
    def context_aware_deduplicate(self, input_path, output_path_before, output_path_after)
    def _merge_rows_by_values(self, df)
```

#### Key Features:
- **Multi-method Downloads**: curl, wget, requests with fallbacks
- **Context-aware Deduplication**: Intelligent merging of similar financial metrics
- **Value-based Merging**: Combines rows with matching financial values
- **Excel Processing**: Extracts and consolidates financial statements

#### Data Processing Pipeline:
1. **Filing Discovery**: Find SEC filings for given ticker/date range
2. **Excel Download**: Download Excel attachments using multiple methods
3. **Data Extraction**: Extract Income Statement, Balance Sheet, Cash Flow
4. **Consolidation**: Combine data across multiple years
5. **Deduplication**: Merge similar metrics and remove duplicates
6. **Output Generation**: Create multiple output formats

### 2. Authentication System (`app.py`)

#### JWT-based Authentication
```python
def create_token(email: str) -> str
def verify_token(token: str) -> bool
def init_db() -> None
def get_user_by_email(email: str) -> Optional[Tuple]
```

#### Database Schema:
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 1,
    role TEXT NOT NULL DEFAULT 'user',
    created_at TEXT NOT NULL
);
```

### 3. Data Processing Features

#### Deduplication Logic
The system uses multiple strategies for data consolidation:

1. **Context-aware Deduplication**:
   - Identifies similar financial metrics by name patterns
   - Groups related metrics together
   - Handles variations in naming conventions

2. **Value-based Merging**:
   - Merges rows with identical financial values
   - Preserves data integrity across years
   - Handles missing or incomplete data

3. **Semantic Similarity** (Planned Enhancement):
   - Recognizes similar metric names even with different wording
   - Handles abbreviations and variations
   - Improves merging accuracy

#### File Output Types:
- **Individual Financials**: Single year/quarter data
- **Master Consolidated**: All years combined with full detail
- **Cleaned Versions**: Removed empty rows/columns
- **Deduplicated Versions**: Merged duplicates with highlighting

## 🔍 Data Quality Features

### Error Handling
- **Download Failures**: Multiple fallback methods (curl → wget → requests)
- **Data Validation**: Checks for valid Excel files and data integrity
- **Missing Data**: Graceful handling of incomplete filings
- **Format Variations**: Handles different Excel formats and structures

### Data Normalization
- **Value Normalization**: Removes formatting, converts to numeric
- **Name Standardization**: Normalizes metric names for comparison
- **Date Handling**: Standardizes date formats across years
- **Currency Processing**: Handles different currency formats

### Quality Indicators
- **Yellow Highlighting**: Shows merged/consolidated rows
- **File Size Validation**: Ensures downloaded files are valid
- **Data Completeness**: Reports on missing or incomplete data
- **Processing Logs**: Detailed logging for troubleshooting

## 🚀 Deployment

### Streamlit Community Cloud
- **Repository**: GitHub repository with public visibility
- **Main File**: `app.py`
- **Dependencies**: `requirements.txt`
- **Environment Variables**: Set in Streamlit Cloud dashboard

### Required Environment Variables
```bash
APP_SECRET_KEY=your-secret-key-here
ADMIN_EMAIL=nishit.wadhwani@tristone-partners.com
ADMIN_PASSWORD=your-admin-password
```

### Dependencies
```
streamlit>=1.28.0
pandas>=1.5.0
openpyxl>=3.0.0
requests>=2.31.0
bcrypt>=4.0.1
PyJWT>=2.8.0
python-dotenv>=1.0.0
Flask>=2.3.3
Flask-CORS>=4.0.0
```

## 🔧 Configuration

### SEC API Configuration
- **API Key**: Required for SEC EDGAR access
- **Rate Limiting**: Built-in delays between requests
- **User Agents**: Rotating user agents to avoid blocking
- **Timeout Handling**: Configurable timeouts for downloads

### File Processing Settings
- **Header Detection**: Automatic detection of year headers
- **Data Start Row**: Configurable starting row for data extraction
- **Merge Thresholds**: Configurable similarity thresholds for merging
- **Output Formats**: Multiple output format options

## 🐛 Known Issues and Solutions

### Common Problems

#### 1. Download Failures
- **Issue**: Some Excel files fail to download
- **Cause**: SEC server issues or file format changes
- **Solution**: Multiple fallback methods implemented

#### 2. Duplicate Data Not Merged
- **Issue**: Similar metrics not being consolidated
- **Cause**: Different naming conventions or formatting
- **Solution**: Enhanced semantic similarity detection (planned)

#### 3. Missing Data
- **Issue**: Incomplete financial statements
- **Cause**: SEC filings may not include Excel attachments
- **Solution**: Graceful handling with user notification

#### 4. Large File Downloads
- **Issue**: Browser timeouts on large files
- **Solution**: Individual file downloads and ZIP options

### Performance Optimizations
- **Parallel Processing**: Concurrent downloads where possible
- **Caching**: Temporary file caching for repeated operations
- **Memory Management**: Efficient handling of large datasets
- **Progress Indicators**: User feedback during long operations

## 🔮 Future Enhancements

### Planned Features
1. **Enhanced Semantic Matching**: Better recognition of similar metrics
2. **Machine Learning**: AI-powered data quality improvements
3. **Real-time Updates**: Live SEC filing monitoring
4. **Advanced Analytics**: Built-in financial analysis tools
5. **API Endpoints**: REST API for programmatic access

### Technical Improvements
1. **Database Optimization**: Better query performance
2. **Caching Layer**: Redis for improved response times
3. **Microservices**: Modular architecture for scalability
4. **Monitoring**: Application performance monitoring
5. **Testing**: Comprehensive test suite

## 📊 Performance Metrics

### Typical Processing Times
- **Single Company (5 years)**: 1-3 minutes
- **Large Company (10+ years)**: 3-5 minutes
- **Multiple Form Types**: 2-4 minutes per form type
- **File Downloads**: 10-30 seconds per file

### Resource Usage
- **Memory**: 100-500MB typical usage
- **Storage**: Temporary files cleaned after processing
- **CPU**: Moderate usage during data processing
- **Network**: Moderate bandwidth for SEC downloads

## 🛠️ Development Setup

### Local Development
```bash
# Clone repository
git clone https://github.com/syntax-erroar/Tristone.git
cd Tristone

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

### Environment Setup
```bash
# Create environment file
cp env.example config.env

# Edit configuration
nano config.env

# Set environment variables
export $(cat config.env | xargs)
```

### Testing
```bash
# Run tests
python -m pytest tests/

# Test specific modules
python test_automated_sec_downloader.py
python test_auth.py
```

---

**Technical Support**: For technical issues or development questions, contact the development team.

