#!/usr/bin/env python3
"""
Ideal Template Formulas and Validation
Provides comprehensive validation against ideal financial templates
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import warnings

@dataclass
class ValidationResult:
    """Result of template validation"""
    concept_name: str
    is_valid: bool
    confidence: float
    error_message: Optional[str] = None
    suggested_correction: Optional[float] = None

class IdealTemplateFormulas:
    """
    Ideal template formulas for financial data validation
    """
    
    def __init__(self):
        self.validation_rules = self._initialize_validation_rules()
        self.tolerance_thresholds = self._initialize_tolerance_thresholds()
    
    def _initialize_validation_rules(self) -> Dict[str, Dict]:
        """Initialize validation rules for financial concepts"""
        return {
            'revenue': {
                'min_value': 0,
                'max_ratio_to_assets': 5.0,  # Revenue shouldn't be more than 5x assets
                'required_components': ['cost_of_revenue'],
                'derived_from': ['gross_profit', 'cost_of_revenue']
            },
            'gross_profit': {
                'min_value': 0,
                'max_ratio_to_revenue': 0.95,  # Gross profit margin shouldn't exceed 95%
                'derived_from': ['revenue', 'cost_of_revenue'],
                'formula': 'revenue - cost_of_revenue'
            },
            'operating_income': {
                'min_ratio_to_revenue': -0.5,  # Operating loss shouldn't exceed 50% of revenue
                'max_ratio_to_revenue': 0.8,   # Operating margin shouldn't exceed 80%
                'derived_from': ['gross_profit', 'research_development', 'sales_marketing', 'general_administrative'],
                'formula': 'gross_profit - research_development - sales_marketing - general_administrative'
            },
            'net_income': {
                'min_ratio_to_revenue': -1.0,  # Net loss shouldn't exceed 100% of revenue
                'max_ratio_to_revenue': 0.6,   # Net margin shouldn't exceed 60%
                'derived_from': ['operating_income', 'interest_expense', 'income_tax_provision'],
                'formula': 'operating_income - interest_expense - income_tax_provision'
            },
            'total_assets': {
                'min_value': 0,
                'min_ratio_to_revenue': 0.1,   # Assets should be at least 10% of revenue
                'max_ratio_to_revenue': 20.0,  # Assets shouldn't be more than 20x revenue
                'components': ['cash_and_equivalents', 'total_debt', 'stockholders_equity']
            },
            'cash_and_equivalents': {
                'min_value': 0,
                'max_ratio_to_assets': 0.8,    # Cash shouldn't exceed 80% of total assets
                'min_ratio_to_revenue': 0.01,  # Cash should be at least 1% of revenue
                'max_ratio_to_revenue': 2.0    # Cash shouldn't exceed 200% of revenue
            },
            'total_debt': {
                'min_value': 0,
                'max_ratio_to_assets': 0.9,    # Debt shouldn't exceed 90% of assets
                'max_ratio_to_revenue': 10.0   # Debt shouldn't exceed 10x revenue
            },
            'stockholders_equity': {
                'min_ratio_to_assets': 0.05,   # Equity should be at least 5% of assets
                'max_ratio_to_assets': 1.0,    # Equity shouldn't exceed 100% of assets
                'derived_from': ['total_assets', 'total_debt'],
                'formula': 'total_assets - total_debt'
            }
        }
    
    def _initialize_tolerance_thresholds(self) -> Dict[str, float]:
        """Initialize tolerance thresholds for validation"""
        return {
            'quarterly_sum_tolerance': 0.05,    # 5% tolerance for quarterly sums
            'formula_tolerance': 0.02,          # 2% tolerance for formula validation
            'ratio_tolerance': 0.1,             # 10% tolerance for ratio validation
            'magnitude_tolerance': 0.2          # 20% tolerance for magnitude validation
        }
    
    def validate_concept(self, concept_name: str, value: float, 
                        financial_data: Dict[str, Any], year: int) -> ValidationResult:
        """Validate a single financial concept against ideal template rules"""
        
        if concept_name not in self.validation_rules:
            return ValidationResult(
                concept_name=concept_name,
                is_valid=True,
                confidence=0.5,
                error_message="No validation rules defined"
            )
        
        rules = self.validation_rules[concept_name]
        confidence = 1.0
        error_messages = []
        
        # Basic value validation
        if 'min_value' in rules and value < rules['min_value']:
            confidence -= 0.3
            error_messages.append(f"Value {value} below minimum {rules['min_value']}")
        
        # Ratio validations
        if 'max_ratio_to_revenue' in rules:
            revenue = self._get_concept_value(financial_data, 'revenue', year)
            if revenue and revenue > 0:
                ratio = value / revenue
                if ratio > rules['max_ratio_to_revenue']:
                    confidence -= 0.2
                    error_messages.append(f"Ratio to revenue {ratio:.3f} exceeds maximum {rules['max_ratio_to_revenue']}")
        
        if 'min_ratio_to_revenue' in rules:
            revenue = self._get_concept_value(financial_data, 'revenue', year)
            if revenue and revenue > 0:
                ratio = value / revenue
                if ratio < rules['min_ratio_to_revenue']:
                    confidence -= 0.2
                    error_messages.append(f"Ratio to revenue {ratio:.3f} below minimum {rules['min_ratio_to_revenue']}")
        
        # Formula validation
        if 'formula' in rules:
            formula_result = self._validate_formula(rules['formula'], financial_data, year)
            if formula_result is not None:
                tolerance = self.tolerance_thresholds['formula_tolerance']
                if abs(value - formula_result) / max(abs(value), abs(formula_result), 1) > tolerance:
                    confidence -= 0.3
                    error_messages.append(f"Formula validation failed: expected {formula_result}, got {value}")
        
        # Component validation
        if 'derived_from' in rules:
            components_valid = self._validate_components(rules['derived_from'], financial_data, year)
            if not components_valid:
                confidence -= 0.1
                error_messages.append("Required components missing or invalid")
        
        is_valid = confidence >= 0.7
        error_message = "; ".join(error_messages) if error_messages else None
        
        return ValidationResult(
            concept_name=concept_name,
            is_valid=is_valid,
            confidence=confidence,
            error_message=error_message
        )
    
    def _get_concept_value(self, financial_data: Dict[str, Any], concept: str, year: int) -> Optional[float]:
        """Get concept value for a specific year"""
        try:
            annual_data = financial_data.get('annual_data', {})
            if year in annual_data and concept in annual_data[year]:
                return annual_data[year][concept]
            return None
        except (KeyError, TypeError):
            return None
    
    def _validate_formula(self, formula: str, financial_data: Dict[str, Any], year: int) -> Optional[float]:
        """Validate a financial formula"""
        try:
            # Simple formula evaluation (can be extended)
            if formula == 'revenue - cost_of_revenue':
                revenue = self._get_concept_value(financial_data, 'revenue', year)
                cost = self._get_concept_value(financial_data, 'cost_of_revenue', year)
                if revenue is not None and cost is not None:
                    return revenue - cost
            
            elif formula == 'gross_profit - research_development - sales_marketing - general_administrative':
                gross_profit = self._get_concept_value(financial_data, 'gross_profit', year)
                rd = self._get_concept_value(financial_data, 'research_development', year) or 0
                sm = self._get_concept_value(financial_data, 'sales_marketing', year) or 0
                ga = self._get_concept_value(financial_data, 'general_administrative', year) or 0
                if gross_profit is not None:
                    return gross_profit - rd - sm - ga
            
            elif formula == 'total_assets - total_debt':
                assets = self._get_concept_value(financial_data, 'total_assets', year)
                debt = self._get_concept_value(financial_data, 'total_debt', year)
                if assets is not None and debt is not None:
                    return assets - debt
            
            return None
        except (TypeError, ValueError):
            return None
    
    def _validate_components(self, components: List[str], financial_data: Dict[str, Any], year: int) -> bool:
        """Validate that required components exist and are valid"""
        for component in components:
            value = self._get_concept_value(financial_data, component, year)
            if value is None or value < 0:
                return False
        return True

class IdealTemplateValidator:
    """
    Comprehensive validator for financial data against ideal templates
    """
    
    def __init__(self):
        self.formulas = IdealTemplateFormulas()
        self.validation_results = {}
    
    def comprehensive_validation(self, financial_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform comprehensive validation of financial data"""
        
        validation_summary = {
            'overall_score': 0.0,
            'concept_validations': {},
            'quarterly_validations': {},
            'formula_validations': {},
            'recommendations': [],
            'total_concepts': 0,
            'valid_concepts': 0,
            'invalid_concepts': 0
        }
        
        # Validate annual data
        annual_data = financial_data.get('annual_data', {})
        concept_scores = []
        
        for year, year_data in annual_data.items():
            if not isinstance(year_data, dict):
                continue
                
            year_validations = {}
            for concept, value in year_data.items():
                if isinstance(value, (int, float)) and not np.isnan(value):
                    result = self.formulas.validate_concept(concept, value, financial_data, year)
                    year_validations[concept] = {
                        'is_valid': result.is_valid,
                        'confidence': result.confidence,
                        'error_message': result.error_message
                    }
                    concept_scores.append(result.confidence)
            
            validation_summary['concept_validations'][year] = year_validations
        
        # Validate quarterly data
        quarterly_data = financial_data.get('quarterly_data', {})
        for year, quarters in quarterly_data.items():
            if not isinstance(quarters, dict):
                continue
                
            quarterly_validation = self._validate_quarterly_consistency(quarters, annual_data.get(year, {}))
            validation_summary['quarterly_validations'][year] = quarterly_validation
        
        # Calculate overall score
        if concept_scores:
            validation_summary['overall_score'] = np.mean(concept_scores)
            validation_summary['total_concepts'] = len(concept_scores)
            validation_summary['valid_concepts'] = sum(1 for score in concept_scores if score >= 0.7)
            validation_summary['invalid_concepts'] = validation_summary['total_concepts'] - validation_summary['valid_concepts']
        
        # Generate recommendations
        validation_summary['recommendations'] = self._generate_recommendations(validation_summary)
        
        return validation_summary
    
    def _validate_quarterly_consistency(self, quarters: Dict, annual_data: Dict) -> Dict[str, Any]:
        """Validate quarterly data consistency"""
        tolerance = self.formulas.tolerance_thresholds['quarterly_sum_tolerance']
        quarterly_validation = {
            'is_consistent': True,
            'inconsistencies': [],
            'concept_validations': {}
        }
        
        # Check if Q1 + Q2 + Q3 + Q4 ≈ Annual for each concept
        for concept in ['revenue', 'cost_of_revenue', 'operating_income', 'net_income']:
            if concept in annual_data:
                annual_value = annual_data[concept]
                quarterly_sum = 0
                quarterly_count = 0
                
                for quarter in ['Q1', 'Q2', 'Q3', 'Q4']:
                    if quarter in quarters and concept in quarters[quarter]:
                        quarterly_sum += quarters[quarter][concept]
                        quarterly_count += 1
                
                if quarterly_count == 4 and annual_value != 0:
                    ratio_diff = abs(quarterly_sum - annual_value) / abs(annual_value)
                    is_consistent = ratio_diff <= tolerance
                    
                    quarterly_validation['concept_validations'][concept] = {
                        'is_consistent': is_consistent,
                        'quarterly_sum': quarterly_sum,
                        'annual_value': annual_value,
                        'difference_ratio': ratio_diff
                    }
                    
                    if not is_consistent:
                        quarterly_validation['is_consistent'] = False
                        quarterly_validation['inconsistencies'].append(
                            f"{concept}: Q1+Q2+Q3+Q4 ({quarterly_sum:.2f}) ≠ Annual ({annual_value:.2f})"
                        )
        
        return quarterly_validation
    
    def _generate_recommendations(self, validation_summary: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on validation results"""
        recommendations = []
        
        overall_score = validation_summary.get('overall_score', 0)
        
        if overall_score < 0.7:
            recommendations.append("Overall validation score is low. Review data quality and XBRL mappings.")
        
        if validation_summary.get('invalid_concepts', 0) > 0:
            recommendations.append(f"Found {validation_summary['invalid_concepts']} invalid concepts. Review these mappings.")
        
        # Check quarterly consistency
        quarterly_issues = 0
        for year, q_validation in validation_summary.get('quarterly_validations', {}).items():
            if not q_validation.get('is_consistent', True):
                quarterly_issues += 1
        
        if quarterly_issues > 0:
            recommendations.append(f"Found quarterly consistency issues in {quarterly_issues} years. Review quarterly data extraction.")
        
        if not recommendations:
            recommendations.append("Data validation passed successfully. All concepts meet quality standards.")
        
        return recommendations

# Example usage and testing
if __name__ == "__main__":
    # Test the validation system
    validator = IdealTemplateValidator()
    
    # Sample financial data for testing
    test_data = {
        'annual_data': {
            2023: {
                'revenue': 1000000,
                'cost_of_revenue': 600000,
                'gross_profit': 400000,
                'research_development': 100000,
                'sales_marketing': 50000,
                'general_administrative': 30000,
                'operating_income': 220000,
                'net_income': 200000,
                'total_assets': 2000000,
                'total_debt': 500000,
                'stockholders_equity': 1500000
            }
        },
        'quarterly_data': {
            2023: {
                'Q1': {'revenue': 250000, 'net_income': 50000},
                'Q2': {'revenue': 250000, 'net_income': 50000},
                'Q3': {'revenue': 250000, 'net_income': 50000},
                'Q4': {'revenue': 250000, 'net_income': 50000}
            }
        }
    }
    
    # Run validation
    results = validator.comprehensive_validation(test_data)
    
    print("Validation Results:")
    print(f"Overall Score: {results['overall_score']:.3f}")
    print(f"Valid Concepts: {results['valid_concepts']}/{results['total_concepts']}")
    print("Recommendations:")
    for rec in results['recommendations']:
        print(f"  • {rec}")
