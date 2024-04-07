from __future__ import annotations

from enum import Enum
from typing import Annotated, Dict, List, Literal, Optional, Union
from functools import partial

import aind_behavior_services.task_logic.distributions as distributions
from aind_behavior_information_foraging import __version__
from aind_behavior_services.task_logic import AindBehaviorTaskLogicModel
from pydantic import BaseModel, Field, RootModel


class Size(BaseModel):
    width: float = Field(default=0, description="Width of the texture")
    height: float = Field(default=0, description="Height of the texture")


class Vector2(BaseModel):
    x: float = Field(default=0, description="X coordinate of the point")
    y: float = Field(default=0, description="Y coordinate of the point")


class Vector3(BaseModel):
    x: float = Field(default=0, description="X coordinate of the point")
    y: float = Field(default=0, description="Y coordinate of the point")
    z: float = Field(default=0, description="Z coordinate of the point")


class OdorControl(BaseModel):
    valve_max_open_time: float = Field(
        default=10, ge=0, description="Maximum time (s) the valve can be open continuously"
    )
    target_total_flow: float = Field(
        default=1000, ge=100, le=1000, description="Target total flow (ml/s) of the odor mixture"
    )
    use_channel_3_as_carrier: bool = Field(default=True, description="Whether to use channel 3 as carrier")
    target_odor_flow: float = Field(
        default=100, ge=0, le=100, description="Target odor flow (ml/s) in the odor mixture"
    )


class PositionControl(BaseModel):
    gain: Vector3 = Field(default=Vector3(x=1, y=1, z=1), description="Gain of the position control.")
    initial_position: Vector3 = Field(default=Vector3(x=0, y=2.56, z=0), description="Gain of the position control.")
    frequency_filter_cutoff: float = Field(
        default=0.5,
        ge=0,
        le=100,
        description="Cutoff frequency (Hz) of the low-pass filter used to filter the velocity signal.",
    )
    velocity_threshold: float = Field(
        default=1, ge=0, description="Threshold (cm/s) of the velocity signal used to detect when the animal is moving."
    )


class AudioControl(BaseModel):
    duration: float = Field(default=0.2, ge=0, description="Duration", units="s")
    frequency: float = Field(default=1000, ge=100, description="Frequency", units="Hz")


class Texture(BaseModel):
    name: str = Field(default="default", description="Name of the texture")
    size: Size = Field(default=Size(width=40, height=40), description="Size of the texture")


class WallTextures(BaseModel):
    floor: Texture = Field(..., description="The texture of the floor")
    ceiling: Texture = Field(..., description="The texture of the ceiling")
    left: Texture = Field(..., description="The texture of the left")
    right: Texture = Field(..., description="The texture of the right")


class VisualCorridor(BaseModel):
    id: int = Field(default=0, ge=0, description="Id of the visual corridor object")
    size: Size = Field(default=Size(width=40, height=40), description="Size of the corridor (cm)")
    start_position: float = Field(default=0, ge=0, description="Start position of the corridor (cm)")
    length: float = Field(default=120, ge=0, description="Length of the corridor site (cm)")
    textures: WallTextures = Field(..., description="The textures of the corridor")


class RenderControl(BaseModel):
    corridor_seed: VisualCorridor = Field(
        default=VisualCorridor(), validate_default=True, description="Seed of the visual corridor"
    )


class OperationControl(BaseModel):
    odor_control: OdorControl = Field(default=OdorControl(), description="Control of the odor", validate_default=True)
    position_control: PositionControl = Field(
        default=PositionControl(), description="Control of the position", validate_default=True
    )
    audio_control: AudioControl = Field(
        default=AudioControl(), description="Control of the audio", validate_default=True
    )
    render_control: RenderControl = Field(
        default=RenderControl(), description="Control of the rendering", validate_default=True
    )


class InterpolationMethod(str, Enum):
    NEAREST = "Nearest"
    LINEAR = "Linear"
    ROUNDUP = "Roundup"
    ROUNDDOWN = "RoundDown"


class Reward(BaseModel):
    pass


class PatchInformation(BaseModel):
    pass


class PatchOdorSpecs(BaseModel):
    identity: None
    max_duration: float


class Patch(BaseModel):
    reward: Reward
    information: List[PatchInformation] = Field(default=[], description="Information of the patch")
    odor: PatchOdorSpecs = Field(default=PatchOdorSpecs(), description="Odor of the patch")


class AindInformationForagingTaskLogic(AindBehaviorTaskLogicModel):
    describedBy: Literal[
        "https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.InformationForaging/main/src/DataSchemas/aind_behavior_information_foraging_task.json"
    ] = Field(
        "https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.InformationForaging/main/src/DataSchemas/aind_behavior_information_foraging_task.json"
    )
    schema_version: Literal[__version__] = __version__
    operation_control: OperationControl = Field(
        OperationControl(), validate_default=True, description="Control of the task"
    )
    placeholder: distributions.Distribution


def schema() -> BaseModel:
    return AindInformationForagingTaskLogic
