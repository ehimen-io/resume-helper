from semantic_kernel import Kernel
from semantic_kernel.connectors.ai import PromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import KernelFunction, KernelArguments
from semantic_kernel.prompt_template import PromptTemplateConfig, InputVariable

chat_history = ChatHistory()

with open("resources/resume.txt", 'r') as resume_txt:
    resume = resume_txt.readlines()

prompt = """
Use the job description below:
{{$job}}

The user's resume for the job is below:
{{$resume}}

{{$history}}
User: {{$user_input}}
ChatBot: 
"""
chat_history.add_system_message("Your task is to answer questions about the job requirements and the user's resume")
chat_history.add_system_message("Assume that the user wants to apply for the job")

def add_chat_function(kernel: Kernel, req_settings: PromptExecutionSettings):
    resume_chat = kernel.add_function(
        function_name="chatFunction",
        plugin_name="resumeChat",
        prompt_template_config=PromptTemplateConfig(
            template=prompt,
            name="chat",
            template_format="semantic-kernel",
            input_variables=[
                InputVariable(name="job", description="The job the user is applying to", is_required=True),
                InputVariable(name="resume", description="The user's resume", is_required=True),
                InputVariable(name="history", description="The conversation history", is_required=True),
            ],
            execution_settings=req_settings,
        ),
    )

    return resume_chat


async def chat(kernel: Kernel, resume_chat: KernelFunction, job: list[str], input_text: str) -> None:
    # Save new message in the context variables
    chat_history.add_user_message(input_text)

    # Process the user message and get an answer
    answer = await kernel.invoke(resume_chat, KernelArguments(job=job, user_input=input_text, resume=resume, history=chat_history))

    # Show the response
    print(f"ChatBot: {answer}")

    chat_history.add_assistant_message(str(answer))
