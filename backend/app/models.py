from typing import List, Literal, Optional
from pydantic import BaseModel

OutputType = Literal[
    "linkedin_post",
    "twitter_thread",
    "executive_summary",
    "advisory",
    "presentation"
]

class TransformConfig(BaseModel):
    target_audience: str
    tone: str
    language: str
    detail_level: str  # brief / standard / detailed
    communication_objective: str
    content_style: str

class TransformRequest(BaseModel):
    text: str
    files: Optional[List[dict]] = None  # metadata if you handle files
    output_types: List[OutputType]
    config: TransformConfig

class TransformResult(BaseModel):
    output_type: str
    content: str  # or JSON string for presentation
    download_url: Optional[str] = None
