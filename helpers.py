from dotenv import dotenv_values
from semantic_kernel import Kernel

config = dotenv_values(".env")


def load_request_settings(kernel: Kernel, service_id: str):
    # Define the request settings
    req_settings = kernel.get_prompt_execution_settings_from_service_id(service_id)
    req_settings.max_tokens = config.get("MAX_TOKENS", 2000)
    req_settings.temperature = config.get("TEMPERATURE", 0.7)
    req_settings.top_p = config.get("TOP_P", 0.8)

    return req_settings
