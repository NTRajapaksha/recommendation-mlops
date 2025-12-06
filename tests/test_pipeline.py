# tests/test_pipeline.py
import os
import pytest
from src.train import train

def test_training_artifacts_created():
    """
    This test runs the training function and checks 
    if the model file is actually created.
    """
    # 1. Run the training (This might take a moment)
    train()
    
    # 2. Check if MLflow created the 'mlruns' directory
    assert os.path.exists("mlruns") == True, "MLflow runs folder was not created"
    
    # 3. Check if the 'data' folder was populated
    assert os.path.exists("data/ml-latest-small") == True, "Data was not downloaded"
    
    print("✅ System passed the Smoke Test!")