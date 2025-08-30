import pandas as pd
import numpy as np

def analyze_files():
    print("="*80)
    print("ANALYZING MODEL ACCURACY - COMPARING IDEAL vs OUR OUTPUT")
    print("="*80)
    
    # Read our generated model
    try:
        our_model = pd.read_excel('microsoft_corporation_enhanced_model_20250830_203706.xlsx', 
                                 sheet_name='Financial Model', header=None)
        print("\n✓ Successfully loaded our generated model")
        print(f"Dimensions: {our_model.shape}")
        
        # Find revenue data in our model
        print("\nOUR MODEL - Revenue Data:")
        for i in range(len(our_model)):
            if pd.notna(our_model.iloc[i, 0]) and 'Total Revenue' in str(our_model.iloc[i, 0]):
                print(f"Row {i}: {list(our_model.iloc[i, :10])}")
                break
                
    except Exception as e:
        print(f"Error loading our model: {e}")
    
    # Read ideal model
    try:
        ideal_model = pd.read_excel('Example of an ideal output for a tech company like microsoft.xlsx', 
                                   header=None)
        print(f"\n✓ Successfully loaded ideal model")
        print(f"Dimensions: {ideal_model.shape}")
        
        # Search for financial data in ideal model
        print("\nIDEAL MODEL - Searching for financial statements...")
        revenue_found = False
        for i in range(len(ideal_model)):
            text = str(ideal_model.iloc[i, 0])
            if pd.notna(ideal_model.iloc[i, 0]):
                text_lower = text.lower()
                if any(keyword in text_lower for keyword in ['total revenue', 'net revenue', 'sales revenue', 'revenue from']):
                    print(f"Found revenue at Row {i}: {text}")
                    print("Context around revenue:")
                    start_row = max(0, i-3)
                    end_row = min(len(ideal_model), i+10)
                    for j in range(start_row, end_row):
                        row_data = []
                        for k in range(min(10, ideal_model.shape[1])):
                            val = ideal_model.iloc[j, k]
                            if pd.notna(val):
                                if isinstance(val, (int, float)):
                                    row_data.append(f"{val:,.0f}" if abs(val) > 1 else f"{val}")
                                else:
                                    row_data.append(str(val)[:30])
                            else:
                                row_data.append("")
                        print(f"Row {j}: {row_data}")
                    revenue_found = True
                    break
        
        if not revenue_found:
            print("No explicit revenue line found. Showing sample rows with numbers:")
            for i in range(len(ideal_model)):
                if pd.notna(ideal_model.iloc[i, 1]) and isinstance(ideal_model.iloc[i, 1], (int, float)) and ideal_model.iloc[i, 1] > 100000:
                    print(f"Row {i}: {list(ideal_model.iloc[i, :8])}")
                    if i > 100:  # Limit search
                        break
                        
    except Exception as e:
        print(f"Error loading ideal model: {e}")
    
    print("\n" + "="*80)
    print("ISSUES IDENTIFIED IN OUR MODEL:")
    print("="*80)
    
    # Analyze our model's issues based on the output we saw
    print("1. REVENUE DATA INCONSISTENCIES:")
    print("   - 2018A: $26,819M vs expected ~$110,000M")
    print("   - 2019A: $30,571M vs expected ~$125,000M") 
    print("   - 2020A: $35,021M vs expected ~$143,000M")
    print("   - Jump from $35B to $143B in 2021 (308% growth) - clearly wrong")
    
    print("\n2. GROSS PROFIT CALCULATION ERRORS:")
    print("   - Negative gross profit in early years (-$7,442M, -$7,782M)")
    print("   - This suggests wrong Cost of Revenue classification")
    
    print("\n3. DATA AGGREGATION PROBLEMS:")
    print("   - Model is picking wrong/inconsistent data points")
    print("   - Quarterly data aggregation is failing")
    print("   - XBRL concept matching is misidentifying revenue streams")
    
    print("\n4. PROJECTION ISSUES:")
    print("   - 2025P: $309,069M (too high - based on wrong base)")
    print("   - Growth rates are unrealistic due to bad historical data")

if __name__ == "__main__":
    analyze_files()
