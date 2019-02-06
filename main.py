from src.add_keys import add_dcirs_keys_to_table_schema
from src.convert import table_schema_to_markdown, table_schema_to_sql_within_docker, table_schema_to_relational_diagram_from_host
from src.reformat_snds_dico import dico_snds_to_table_schema
from src.utils import is_running_in_docker

dico_snds_to_table_schema()
add_dcirs_keys_to_table_schema()
table_schema_to_markdown()

if is_running_in_docker():
    table_schema_to_sql_within_docker()
else:
    table_schema_to_relational_diagram_from_host()
