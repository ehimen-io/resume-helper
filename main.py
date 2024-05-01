import asyncio
import time

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.utils.settings import openai_settings_from_dot_env

from chat import add_chat_function, chat
from generate import add_generate_function, generate, print_ai_response
from helpers import load_request_settings
from prompts import bullet_points, tech_stack, years_of_experience

kernel = Kernel()

with open("resources/job.txt", 'r') as job_txt:
    job = job_txt.readlines()

# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = openai_settings_from_dot_env()
service_id = "chat-gpt"
kernel.add_service(
    OpenAIChatCompletion(
        service_id=service_id,
        ai_model_id="gpt-4",
        api_key=api_key,
        org_id=org_id
    )
)

req_settings = load_request_settings(kernel, service_id)

c = add_chat_function(kernel, req_settings)
g = add_generate_function(kernel, req_settings)


async def generate_response(prompt):
    return await generate(kernel, g, job, prompt)


async def generate_prompt_responses():
    titles = ["Years of Experience", "Bullet Points", "Tech Stack"]

    responses = await asyncio.gather(
        generate_response(years_of_experience),
        generate_response(bullet_points),
        generate_response(tech_stack)
    )

    return titles, responses


async def start_chat():
    while True:
        user_input = input("User: ").lower()
        if user_input == "qc":
            return False
        elif user_input == "q":
            return True

        await chat(kernel, c, job, user_input)


async def main():
    while True:
        user_input = input("> ").lower()
        if user_input == "q":
            break
        elif user_input == "g":
            print("Generating...")
            titles, responses = await generate_prompt_responses()

            for i, title in enumerate(titles):
                print_ai_response(responses[i], title)
                time.sleep(1)
        elif user_input == "c":
            quit_session = await start_chat()
            if quit_session:
                break


if __name__ == "__main__":
    asyncio.run(main())
