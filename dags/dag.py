from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
import os
from pendulum import datetime

profile_config_dev = ProfileConfig(
    profile_name="projeto_airflow_dbt",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="docker_postgres_db",
        profile_args={"schema": "public"},
    ),
)

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path="/usr/local/airflow/dbt/projeto_airflow_dbt",
        project_name="projeto_airflow_dbt",
    ),
    profile_config=profile_config_dev,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
    ),
    operator_args={
        "install_deps": True,
        "target": profile_config_dev.target_name,
    },
    schedule="@daily",
    start_date=datetime(2025, 5, 30),
    catchup=False,
    dag_id=f"dag_projeto_airflow_dbt_dev",
    default_args={"retries": 2},
)