from __future__ import annotations

from enum import Enum
from typing import Annotated, Dict, List, Literal, Optional, Union
from functools import partial

import aind_behavior_services.task_logic.distributions as distributions
from aind_behavior_information_foraging import __version__
from aind_behavior_services.task_logic import AindBehaviorTaskLogicModel
from aind_data_schema.base import BaseModel
from pydantic import BaseModel, Field, RootModel


class AindInformationForagingTaskLogic(AindBehaviorTaskLogicModel):
    describedBy: Literal[
        "https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.InformationForaging/main/src/DataSchemas/aind_behavior_information_foraging_task_logic.json"
    ] = Field(
        "https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.InformationForaging/main/src/DataSchemas/aind_behavior_information_foraging_task_logic.json"
    )
    schema_version: Literal[__version__] = __version__


def schema() -> BaseModel:
    return AindInformationForagingTaskLogic
