from typing import TypedDict, List, Optional, Annotated
from operator import add

class DueDiligenceState(TypedDict): 
    # Input 
    startup_name: str 
    startup_description: str 
    funding_state: Optional[str]

    # Research Outputs
    research_outputs: Annotated[List[dict], add]

    # Analysis Outputs
    analysis_outputs: Annotated[List[dict], add]

    # Synthesis Outputs
    full_report: Optional[str]
    investment_decision: Optional[dict]

    # Metadata
    current_stage: str 
    errors: Annotated[List[str], add]
    retry_count: int

def create_initial_state(
        startup_name: str, 
        startup_description: str,
        funding_stage: Optional[str] = None
) -> DueDiligenceState:
    """ Create an initial state from user input"""
    return DueDiligenceState(
        startup_name = startup_name,
        startup_description=startup_description,
        funding_stage=funding_stage, 
        research_outputs=[], 
        analysis_outputs=[], 
        full_report=None, 
        investment_decision=None,
        current_stage="init", 
        errors=[],
        retry_count=0
    )