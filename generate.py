from semantic_kernel import Kernel
from semantic_kernel.connectors.ai import PromptExecutionSettings
from semantic_kernel.functions import KernelFunction, KernelArguments
from semantic_kernel.prompt_template import PromptTemplateConfig, InputVariable

prompt = """
Using the job description below:
{{$job}}

{{$user_input}}
"""


def add_generate_function(kernel: Kernel, req_settings: PromptExecutionSettings):
    generate_function = kernel.add_function(
        function_name="generate",
        plugin_name="generatePlugin",
        prompt_template_config=PromptTemplateConfig(
            template=prompt,
            name="generate",
            template_format="semantic-kernel",
            input_variables=[
                InputVariable(name="job", description="The job the user is applying to", is_required=True),
            ],
            execution_settings=req_settings,
        ),
    )

    return generate_function


def print_ai_response(answer, title=None):
    if title:
        print(f'---------{title} ---------')

    print(answer)


async def generate(kernel: Kernel,
                   generate_function: KernelFunction,
                   job: list[str],
                   input_text: str) -> None:
    return await kernel.invoke(generate_function, KernelArguments(job=job, user_input=input_text))

