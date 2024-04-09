from aind_behavior_information_foraging.rig import AindInformationForagingRig
from aind_behavior_information_foraging.session import AindBehaviorSessionModel
from aind_behavior_information_foraging.task_logic import AindInformationForagingTaskLogic
from aind_behavior_services.launcher import LauncherCli

if __name__ == "__main__":
    launcher_cli = LauncherCli(
        rig_schema=AindInformationForagingRig,
        session_schema=AindBehaviorSessionModel,
        task_logic_schema=AindInformationForagingTaskLogic,
        data_dir=r"C:/Data",
        remote_data_dir=None,
        config_library_dir=r"\\allen\aind\scratch\AindBehavior.db\AindInformationForaging",
        workflow=r"./src/main.bonsai",
    )
    launcher_cli.run()
