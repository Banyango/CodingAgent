from typing import List

from core.plans.models import PlanModel
from core.plans.use_cases.create_a_readme import plan as create_a_readme
from core.plans.use_cases.create_a_unit_test import plan as create_a_unit_test
from core.plans.use_cases.create_a_code_review import plan as create_a_code_review
from core.plans.use_cases.create_boilerplate_code import plan as create_boilerplate_code
from core.plans.use_cases.refactor_messy_module import plan as refactor_messy_module
from core.plans.use_cases.write_unit_tests import plan as write_unit_tests
from core.plans.use_cases.explain_code_and_bugs import plan as explain_code_and_bugs
from core.plans.use_cases.create_dockerfile import plan as create_dockerfile
from core.plans.use_cases.optimize_sql_query import plan as optimize_sql_query
from core.plans.use_cases.convert_code_language import plan as convert_code_language
from core.plans.use_cases.generate_documentation import plan as generate_documentation
from core.plans.use_cases.design_database_schema import plan as design_database_schema
from core.plans.use_cases.implement_feature_from_user_story import (
    plan as implement_feature_from_user_story,
)
from core.plans.use_cases.fix_bug_from_traceback import plan as fix_bug_from_traceback
from core.plans.use_cases.write_cicd_pipeline import plan as write_cicd_pipeline
from core.plans.use_cases.create_example_api_clients import (
    plan as create_example_api_clients,
)
from core.plans.use_cases.setup_logging_and_metrics import (
    plan as setup_logging_and_metrics,
)
from core.plans.use_cases.write_data_migration_script import (
    plan as write_data_migration_script,
)
from core.plans.use_cases.build_cli_tool import plan as build_cli_tool
from core.plans.use_cases.implement_auth_authorization import (
    plan as implement_auth_authorization,
)
from core.plans.use_cases.generate_mock_data_fixtures import (
    plan as generate_mock_data_fixtures,
)
from core.plans.use_cases.detect_and_fix_security_vulnerabilities import (
    plan as detect_and_fix_security_vulnerabilities,
)
from core.plans.use_cases.update_configuration_files import (
    plan as update_configuration_files,
)
from core.plans.use_cases.write_integration_tests_api import (
    plan as write_integration_tests_api,
)
from core.plans.use_cases.build_ui_components import plan as build_ui_components
from core.plans.use_cases.profile_codebase_and_suggest_improvements import (
    plan as profile_codebase_and_suggest_improvements,
)
from core.plans.use_cases.implement_caching_layer import plan as implement_caching_layer
from core.plans.use_cases.create_openapi_docs import plan as create_openapi_docs
from core.plans.use_cases.setup_local_dev_environment import (
    plan as setup_local_dev_environment,
)
from core.plans.use_cases.write_plugin_or_extension import (
    plan as write_plugin_or_extension,
)
from core.plans.use_cases.generate_data_visualizations import (
    plan as generate_data_visualizations,
)
from core.plans.use_cases.add_code_comments_and_explanations import (
    plan as add_code_comments_and_explanations,
)
from core.plans.use_cases.simulate_external_services import (
    plan as simulate_external_services,
)

ALL_PLANS: List[PlanModel] = [
    create_a_readme,
    create_a_unit_test,
    create_a_code_review,
    create_boilerplate_code,
    refactor_messy_module,
    write_unit_tests,
    explain_code_and_bugs,
    create_dockerfile,
    optimize_sql_query,
    convert_code_language,
    generate_documentation,
    design_database_schema,
    implement_feature_from_user_story,
    fix_bug_from_traceback,
    write_cicd_pipeline,
    create_example_api_clients,
    setup_logging_and_metrics,
    write_data_migration_script,
    build_cli_tool,
    implement_auth_authorization,
    generate_mock_data_fixtures,
    detect_and_fix_security_vulnerabilities,
    update_configuration_files,
    write_integration_tests_api,
    build_ui_components,
    profile_codebase_and_suggest_improvements,
    implement_caching_layer,
    create_openapi_docs,
    setup_local_dev_environment,
    write_plugin_or_extension,
    generate_data_visualizations,
    add_code_comments_and_explanations,
    simulate_external_services,
]
