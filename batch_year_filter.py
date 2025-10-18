#!/usr/bin/env python3
"""
Batch Year-Based Table Filter
Processes multiple Excel files to extract only year-based financial tables.
"""

import os
import glob
from year_based_table_filter import YearBasedTableFilter

def batch_filter_excel_files(input_pattern: str, output_dir: str = "filtered_output"):
    """Process multiple Excel files matching a pattern"""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all Excel files matching the pattern
    excel_files = glob.glob(input_pattern)
    
    if not excel_files:
        print(f"No Excel files found matching pattern: {input_pattern}")
        return
    
    print(f"Found {len(excel_files)} Excel files to process")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    filter_obj = YearBasedTableFilter()
    total_stats = {
        'files_processed': 0,
        'files_successful': 0,
        'total_tables_found': 0,
        'total_tables_kept': 0,
        'total_sheets_kept': 0
    }
    
    for excel_file in excel_files:
        print(f"\nProcessing: {excel_file}")
        
        # Generate output filename
        base_name = os.path.splitext(os.path.basename(excel_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}_YearBased_Filtered.xlsx")
        
        try:
            result = filter_obj.filter_excel_file(excel_file, output_file)
            
            if 'error' not in result:
                total_stats['files_processed'] += 1
                total_stats['files_successful'] += 1
                total_stats['total_tables_found'] += result.get('tables_found', 0)
                total_stats['total_tables_kept'] += result.get('tables_kept', 0)
                total_stats['total_sheets_kept'] += len(result.get('sheets_kept', []))
                
                print(f"  ✓ Success: {result.get('tables_kept', 0)} tables kept from {result.get('tables_found', 0)} found")
                print(f"  ✓ Output: {output_file}")
            else:
                print(f"  ✗ Error: {result['error']}")
                total_stats['files_processed'] += 1
                
        except Exception as e:
            print(f"  ✗ Exception: {e}")
            total_stats['files_processed'] += 1
    
    # Print summary
    print("\n" + "=" * 50)
    print("BATCH PROCESSING SUMMARY")
    print("=" * 50)
    print(f"Files processed: {total_stats['files_processed']}")
    print(f"Files successful: {total_stats['files_successful']}")
    print(f"Total tables found: {total_stats['total_tables_found']}")
    print(f"Total tables kept: {total_stats['total_tables_kept']}")
    print(f"Total sheets kept: {total_stats['total_sheets_kept']}")
    
    if total_stats['files_successful'] > 0:
        avg_tables_per_file = total_stats['total_tables_kept'] / total_stats['files_successful']
        print(f"Average tables per file: {avg_tables_per_file:.1f}")
    
    print(f"\nFiltered files saved in: {output_dir}")

def main():
    """Main function"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python batch_year_filter.py <pattern> [output_dir]")
        print("Examples:")
        print("  python batch_year_filter.py '*_Multi_Year_Cleaned.xlsx'")
        print("  python batch_year_filter.py 'MSFT_*.xlsx' filtered_msft")
        print("  python batch_year_filter.py '*.xlsx' filtered_output")
        return
    
    input_pattern = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "filtered_output"
    
    batch_filter_excel_files(input_pattern, output_dir)

if __name__ == "__main__":
    main()
