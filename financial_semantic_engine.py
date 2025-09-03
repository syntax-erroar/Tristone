#!/usr/bin/env python3
"""
Financial Semantic Engine
Advanced semantic similarity using sentence transformers for financial data analysis
"""

import numpy as np
import json
import pickle
import os
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
import logging
from pathlib import Path
import hashlib
import time

# Lazy imports for performance
try:
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False
    print("Warning: sentence-transformers not available. Using fallback semantic scoring.")

@dataclass
class SemanticMatch:
    """Result of semantic matching"""
    concept_name: str
    similarity_score: float
    confidence_level: str  # 'high', 'medium', 'low'
    method: str  # 'transformer', 'fallback'
    context: str

class FinancialSemanticEngine:
    """
    Advanced semantic engine for financial data analysis using sentence transformers
    """
    
    def __init__(self, cache_dir: str = "semantic_cache", model_name: str = "all-MiniLM-L6-v2"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.model_name = model_name
        self.model = None
        self.embedding_cache = {}
        self.financial_concept_embeddings = {}
        self.initialization_time = None
        self.logger = self._setup_logger()
        
        # Financial domain-specific context mappings
        self.financial_contexts = {
            'income_statement': [
                'revenue', 'sales', 'income', 'profit', 'loss', 'earnings',
                'expense', 'cost', 'operating', 'gross', 'net', 'ebitda'
            ],
            'balance_sheet': [
                'asset', 'liability', 'equity', 'debt', 'cash', 'inventory',
                'receivable', 'payable', 'capital', 'retained', 'stock'
            ],
            'cash_flow': [
                'cash', 'flow', 'operating', 'investing', 'financing',
                'activities', 'depreciation', 'amortization', 'working'
            ]
        }
        
        # Financial terminology synonyms
        self.financial_synonyms = {
            'revenue': ['sales', 'income', 'turnover', 'receipts'],
            'profit': ['earnings', 'income', 'gain', 'surplus'],
            'expense': ['cost', 'expenditure', 'outlay', 'charge'],
            'asset': ['property', 'holding', 'investment', 'resource'],
            'liability': ['debt', 'obligation', 'payable', 'burden'],
            'equity': ['capital', 'ownership', 'shares', 'stock'],
            'cash': ['liquidity', 'funds', 'money', 'currency'],
            'operating': ['operational', 'business', 'core', 'primary']
        }
        
    def _setup_logger(self) -> logging.Logger:
        """Setup logging for the semantic engine"""
        logger = logging.getLogger('FinancialSemanticEngine')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            
        return logger
    
    def initialize_model(self, force_reload: bool = False) -> bool:
        """
        Initialize the sentence transformer model with lazy loading
        """
        if self.model is not None and not force_reload:
            return True
            
        if not SENTENCE_TRANSFORMERS_AVAILABLE:
            self.logger.warning("Sentence transformers not available, using fallback")
            return False
            
        try:
            start_time = time.time()
            self.logger.info(f"Loading sentence transformer model: {self.model_name}")
            
            # Load model with optimized settings
            self.model = SentenceTransformer(self.model_name)
            
            # Warm up the model with a simple encoding
            _ = self.model.encode(["financial data analysis"])
            
            self.initialization_time = time.time() - start_time
            self.logger.info(f"Model loaded successfully in {self.initialization_time:.2f}s")
            
            # Pre-compute embeddings for common financial concepts
            self._precompute_financial_embeddings()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load sentence transformer model: {e}")
            self.model = None
            return False
    
    def _precompute_financial_embeddings(self):
        """Pre-compute embeddings for common financial concepts"""
        if not self.model:
            return
            
        self.logger.info("Pre-computing financial concept embeddings...")
        
        # Common financial concepts with context
        financial_concepts = [
            "total revenue sales income",
            "operating income profit earnings",
            "net income profit after tax",
            "gross profit margin",
            "operating expenses costs",
            "cost of goods sold COGS",
            "total assets balance sheet",
            "current assets liquid",
            "total liabilities debt obligations",
            "stockholders equity capital",
            "cash and cash equivalents",
            "operating cash flow activities",
            "free cash flow FCF",
            "depreciation amortization",
            "research and development R&D",
            "selling general administrative SG&A",
            "interest expense debt service",
            "tax expense provision",
            "dividends paid shareholders",
            "share repurchase buyback"
        ]
        
        try:
            embeddings = self.model.encode(financial_concepts)
            for concept, embedding in zip(financial_concepts, embeddings):
                self.financial_concept_embeddings[concept] = embedding
                
            self.logger.info(f"Pre-computed {len(financial_concepts)} financial concept embeddings")
            
        except Exception as e:
            self.logger.error(f"Failed to pre-compute embeddings: {e}")
    
    def _get_cache_key(self, text: str) -> str:
        """Generate cache key for text"""
        return hashlib.md5(text.encode()).hexdigest()
    
    def _load_embedding_cache(self) -> bool:
        """Load embedding cache from disk"""
        cache_file = self.cache_dir / "embedding_cache.pkl"
        if cache_file.exists():
            try:
                with open(cache_file, 'rb') as f:
                    self.embedding_cache = pickle.load(f)
                self.logger.info(f"Loaded {len(self.embedding_cache)} cached embeddings")
                return True
            except Exception as e:
                self.logger.warning(f"Failed to load embedding cache: {e}")
        return False
    
    def _save_embedding_cache(self):
        """Save embedding cache to disk"""
        cache_file = self.cache_dir / "embedding_cache.pkl"
        try:
            with open(cache_file, 'wb') as f:
                pickle.dump(self.embedding_cache, f)
            self.logger.info(f"Saved {len(self.embedding_cache)} cached embeddings")
        except Exception as e:
            self.logger.warning(f"Failed to save embedding cache: {e}")
    
    def get_embedding(self, text: str, use_cache: bool = True) -> Optional[np.ndarray]:
        """
        Get embedding for text with caching
        """
        if not self.model:
            return None
            
        # Check cache first
        if use_cache:
            cache_key = self._get_cache_key(text)
            if cache_key in self.embedding_cache:
                return self.embedding_cache[cache_key]
        
        try:
            # Generate embedding
            embedding = self.model.encode([text])[0]
            
            # Cache the result
            if use_cache:
                self.embedding_cache[cache_key] = embedding
                
            return embedding
            
        except Exception as e:
            self.logger.error(f"Failed to generate embedding for '{text}': {e}")
            return None
    
    def create_financial_context(self, metric_name: str, statement_type: str = None) -> str:
        """
        Create context-rich text for better semantic understanding
        """
        # Clean and normalize the metric name
        clean_name = metric_name.lower().strip()
        
        # Add financial context based on statement type
        context_terms = []
        if statement_type and statement_type in self.financial_contexts:
            context_terms.extend(self.financial_contexts[statement_type])
        
        # Add synonyms for better matching
        for term, synonyms in self.financial_synonyms.items():
            if term in clean_name:
                context_terms.extend(synonyms)
        
        # Combine metric name with context
        context_text = clean_name
        if context_terms:
            context_text += " " + " ".join(context_terms[:5])  # Limit to 5 terms
        
        return context_text
    
    def calculate_semantic_similarity(self, metric_name: str, concept_name: str, 
                                    statement_type: str = None) -> SemanticMatch:
        """
        Calculate semantic similarity between metric and concept using sentence transformers
        """
        # Initialize model if needed
        if not self.model and not self.initialize_model():
            # Fallback to basic similarity
            return self._fallback_similarity(metric_name, concept_name)
        
        try:
            # Create context-rich representations
            metric_context = self.create_financial_context(metric_name, statement_type)
            concept_context = self.create_financial_context(concept_name, statement_type)
            
            # Get embeddings
            metric_embedding = self.get_embedding(metric_context)
            concept_embedding = self.get_embedding(concept_context)
            
            if metric_embedding is None or concept_embedding is None:
                return self._fallback_similarity(metric_name, concept_name)
            
            # Calculate cosine similarity
            similarity = cosine_similarity(
                metric_embedding.reshape(1, -1),
                concept_embedding.reshape(1, -1)
            )[0][0]
            
            # Determine confidence level
            if similarity >= 0.8:
                confidence = 'high'
            elif similarity >= 0.6:
                confidence = 'medium'
            else:
                confidence = 'low'
            
            return SemanticMatch(
                concept_name=concept_name,
                similarity_score=float(similarity),
                confidence_level=confidence,
                method='transformer',
                context=f"metric: {metric_context}, concept: {concept_context}"
            )
            
        except Exception as e:
            self.logger.error(f"Error in semantic similarity calculation: {e}")
            return self._fallback_similarity(metric_name, concept_name)
    
    def _fallback_similarity(self, metric_name: str, concept_name: str) -> SemanticMatch:
        """
        Fallback similarity calculation when sentence transformers are not available
        """
        # Simple word overlap similarity
        metric_words = set(metric_name.lower().split())
        concept_words = set(concept_name.lower().split())
        
        intersection = len(metric_words.intersection(concept_words))
        union = len(metric_words.union(concept_words))
        
        similarity = intersection / union if union > 0 else 0.0
        
        # Determine confidence level
        if similarity >= 0.7:
            confidence = 'high'
        elif similarity >= 0.4:
            confidence = 'medium'
        else:
            confidence = 'low'
        
        return SemanticMatch(
            concept_name=concept_name,
            similarity_score=similarity,
            confidence_level=confidence,
            method='fallback',
            context=f"fallback calculation"
        )
    
    def find_best_semantic_matches(self, metric_name: str, concept_candidates: List[str],
                                 statement_type: str = None, top_k: int = 3) -> List[SemanticMatch]:
        """
        Find the best semantic matches for a metric among concept candidates
        """
        matches = []
        
        for concept in concept_candidates:
            match = self.calculate_semantic_similarity(metric_name, concept, statement_type)
            matches.append(match)
        
        # Sort by similarity score and return top_k
        matches.sort(key=lambda x: x.similarity_score, reverse=True)
        return matches[:top_k]
    
    def batch_calculate_similarities(self, metric_concept_pairs: List[Tuple[str, str]], 
                                   statement_type: str = None) -> List[SemanticMatch]:
        """
        Calculate similarities for multiple metric-concept pairs efficiently
        """
        if not self.model:
            # Fallback for each pair
            return [self._fallback_similarity(metric, concept) 
                   for metric, concept in metric_concept_pairs]
        
        try:
            # Prepare all texts for batch processing
            metric_texts = []
            concept_texts = []
            
            for metric, concept in metric_concept_pairs:
                metric_context = self.create_financial_context(metric, statement_type)
                concept_context = self.create_financial_context(concept, statement_type)
                metric_texts.append(metric_context)
                concept_texts.append(concept_context)
            
            # Batch encode
            metric_embeddings = self.model.encode(metric_texts)
            concept_embeddings = self.model.encode(concept_texts)
            
            # Calculate similarities
            similarities = cosine_similarity(metric_embeddings, concept_embeddings)
            
            # Create results
            results = []
            for i, (metric, concept) in enumerate(metric_concept_pairs):
                similarity = similarities[i][i]  # Diagonal elements
                
                if similarity >= 0.8:
                    confidence = 'high'
                elif similarity >= 0.6:
                    confidence = 'medium'
                else:
                    confidence = 'low'
                
                results.append(SemanticMatch(
                    concept_name=concept,
                    similarity_score=float(similarity),
                    confidence_level=confidence,
                    method='transformer',
                    context=f"batch processing"
                ))
            
            return results
            
        except Exception as e:
            self.logger.error(f"Error in batch similarity calculation: {e}")
            # Fallback to individual calculations
            return [self._fallback_similarity(metric, concept) 
                   for metric, concept in metric_concept_pairs]
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Get performance statistics for the semantic engine"""
        return {
            'model_loaded': self.model is not None,
            'model_name': self.model_name,
            'initialization_time': self.initialization_time,
            'cached_embeddings': len(self.embedding_cache),
            'precomputed_concepts': len(self.financial_concept_embeddings),
            'sentence_transformers_available': SENTENCE_TRANSFORMERS_AVAILABLE
        }
    
    def cleanup(self):
        """Cleanup resources and save cache"""
        if self.embedding_cache:
            self._save_embedding_cache()
        self.logger.info("Semantic engine cleanup completed")
