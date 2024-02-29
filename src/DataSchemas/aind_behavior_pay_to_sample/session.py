from typing import Literal

from aind_behavior_services import __version__
from aind_behavior_services.session import AindBehaviorSessionModel
from pydantic import BaseModel, Field


class AindInformationForagingSession(AindBehaviorSessionModel):
    describedBy: Literal[""] = Field("")
    schema_version: Literal[__version__] = __version__


def schema() -> BaseModel:
    return AindInformationForagingSession
