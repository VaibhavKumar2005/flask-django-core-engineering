# predictor.py
import numpy as np

def get_marks_prediction(hours):
    """
    This function contains your Linear Regression logic.
    """
    try:
        # Simple Linear Regression: y = mx + c
        # (Assuming your model found: 7 marks per hour + 20 base marks)
        hours_float = float(hours)
        prediction = (hours_float * 7) + 20
        
        # SRE Rule: Always validate your output (cap marks at 100)
        final_score = min(100, prediction)
        return round(final_score, 2)
    except Exception as e:
        return f"Error in calculation: {e}"