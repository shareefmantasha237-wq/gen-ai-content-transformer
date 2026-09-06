from typing import Any, Dict, List
from app.generators.linkedin import LinkedInGenerator
from app.generators.twitter import TwitterGenerator
from app.generators.executive_summary import ExecutiveSummaryGenerator
from app.generators.advisory import AdvisoryGenerator
from app.generators.presentation import PresentationGenerator

GENERATORS = {
    "linkedin_post": LinkedInGenerator(),
    "twitter_thread": TwitterGenerator(),
    "executive_summary": ExecutiveSummaryGenerator(),
    "advisory": AdvisoryGenerator(),
    "presentation": PresentationGenerator(),
}

async def run_transformation(source: str, output_types: List[str], config: dict) -> List[Dict[str, Any]]:
    results = []
    for ot in output_types:
        gen = GENERATORS[ot]
        if ot == "presentation":
            out = await gen.generate(source, config)
            results.append({
                "output_type": ot,
                "content": out["json"],
                "download_url": "/download/" + out["pptx_path"].split("/")[-1]
            })
        else:
            content = await gen.generate(source, config)
            results.append({
                "output_type": ot,
                "content": content,
                "download_url": None
            })
    return results
