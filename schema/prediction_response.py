from pydantic import Field,BaseModel # type: ignore
from typing import Dict



class PredictionResponse(BaseModel):
    predicted_category: str = Field(...,
        description ='The Predicted insurance premium category', example = "high"
        )
    
    confidence: float = Field(..., 
        description = "Model's confidence score for the predicted class (range 0 to 1)",
        example = 0.876)
    
    class_probabilities: Dict[str,float] = Field(...,
        description = 'Probability distribution across all possible classes',
        example = {"Low":0.01, "Medium": 0.15, "High":0.84})
    
    