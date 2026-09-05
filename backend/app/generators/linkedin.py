from app.generators.base import BaseGenerator
from app.llm import client, prompts

class LinkedInGenerator(BaseGenerator):
    async def generate(self, source: str, config: dict) -> str:
        system_prompt = prompts.BASE_SYSTEM
        user_prompt = prompts.build_user_prompt(
            source, config, prompts.FORMAT_INSTRUCTIONS["linkedin_post"]
        )
        return await client.call_llm(system_prompt, user_prompt)
