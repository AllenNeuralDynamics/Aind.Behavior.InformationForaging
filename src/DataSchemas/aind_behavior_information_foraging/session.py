from typing import Literal

from aind_behavior_services import __version__
from aind_behavior_services.session import AindBehaviorSessionModel
from pydantic import BaseModel, Field


class AindInformationForagingSession(AindBehaviorSessionModel):
    describedBy: Literal[
        "https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.InformationForaging/main/src/DataSchemas/aind_behavior_information_foraging_session.json"
    ] = Field(
        "https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.InformationForaging/main/src/DataSchemas/aind_behavior_information_foraging_session.json"
    )
    schema_version: Literal[__version__] = __version__


def schema() -> BaseModel:
    return AindInformationForagingSession
