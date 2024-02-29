from pathlib import Path

import aind_behavior_pay_to_sample.rig
import aind_behavior_pay_to_sample.session
import aind_behavior_pay_to_sample.task_logic
from aind_behavior_services.utils import convert_pydantic_to_bonsai

SCHEMA_ROOT = Path("./src/DataSchemas/")
EXTENSIONS_ROOT = Path("./src/Extensions/")
NAMESPACE_PREFIX = "AindPayToSampleDataSchema"


def main():
    models = {
        "aind_behavior_pay_to_sample_task": aind_behavior_pay_to_sample.task_logic.schema(),
        "aind_behavior_pay_to_sample_session": aind_behavior_pay_to_sample.session.schema(),
        "aind_behavior_pay_to_sample_rig": aind_behavior_pay_to_sample.rig.schema(),
    }
    convert_pydantic_to_bonsai(
        models, schema_path=SCHEMA_ROOT, output_path=EXTENSIONS_ROOT, namespace_prefix=NAMESPACE_PREFIX
    )


if __name__ == "__main__":
    main()
