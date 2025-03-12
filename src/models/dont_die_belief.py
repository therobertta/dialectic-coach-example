from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class Evidence(BaseModel):
    type: str = Field(...)
    description: str = Field(...)
    source: str = Field(...)
    date_added: datetime = Field(default_factory=datetime.now)

class ActionItem(BaseModel):
    description: str = Field(...)
    status: str = Field(...)
    target_date: datetime = Field(...)
    completion_date: Optional[datetime] = Field(None)

class CommunityAspect(BaseModel):
    type: str = Field(...)
    description: str = Field(...)
    engagement_level: int = Field(..., ge=1, le=5)

class DontDieBelief(BaseModel):
    id: str = Field(...)
    category: str = Field(...)
    statement: str = Field(...)
    confidence: float = Field(..., ge=0, le=1)
    evidence: List[Evidence] = Field(default_factory=list)
    action_items: List[ActionItem] = Field(default_factory=list)
    community_aspects: List[CommunityAspect] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class BeliefTrack(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    beliefs: List[DontDieBelief] = Field(default_factory=list)
    progress: float = Field(default=0.0, ge=0, le=1)
    priority: int = Field(..., ge=1, le=5)

class DontDieBeliefSystem(BaseModel):
    user_id: str = Field(...)
    tracks: List[BeliefTrack] = Field(...)
    overall_progress: float = Field(default=0.0, ge=0, le=1)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)