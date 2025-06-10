import os
import sys 
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def save_object(file_path, obj):
    """
    Save an object to a file using numpy's save function.
    
    Parameters:
    - file_path (str): The path where the object will be saved.
    - obj: The object to be saved.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)  
        
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
    except Exception as e:
        print(f"Error saving object: {e}")
        raise e