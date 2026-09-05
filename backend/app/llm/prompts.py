BASE_SYSTEM = """You are an expert content transformation engine.
You receive source content and configuration (audience, tone, language, detail, objective, style).
You must generate high-quality, platform-appropriate content strictly following the requested output format.
Do not add extra commentary. Return only the requested artefact."""

def build_user_prompt(source: str, config: dict, format_instruction: str) -> str:
    return f"""SOURCE CONTENT:
{source}

CONFIGURATION:
- Target audience: {config['target_audience']}
- Tone: {config['tone']}
- Language: {config['language']}
- Detail level: {config['detail_level']}
- Communication objective: {config['communication_objective']}
- Content style: {config['content_style']}

INSTRUCTION FOR THIS OUTPUT FORMAT:
{format_instruction}

Generate the requested output now."""

FORMAT_INSTRUCTIONS = {
    "linkedin_post": """Generate a professional LinkedIn post.
Structure:
- Hook (1–2 lines)
- Body (3–6 short paragraphs or bullets)
- Call to action
- 3–5 relevant hashtags
Keep it concise, engaging, and suitable for senior professionals.""",

    "twitter_thread": """Generate a Twitter/X thread (3–7 tweets).
Each tweet must be ≤ 280 characters.
Number them as "1/", "2/", etc.
Ensure logical flow: hook → key points → conclusion/CTA.""",

    "executive_summary": """Generate a concise executive summary (150–250 words).
Include:
- Context/background
- Key insights/findings
- Implications
- Recommended actions (if any)
Use clear, formal business language.""",

    "advisory": """Generate a structured advisory document.
Use sections:
1. Background
2. Current Situation / Threat / Issue
3. Risk / Impact
4. Recommendations
5. Action Items (with owners/timelines if possible)
Use clear headings and bullet points.""",

    "presentation": """Generate a presentation as JSON with this schema:
{
  "title": "Presentation title",
  "slides": [
    {
      "title": "Slide title",
      "bullets": ["point 1", "point 2"],
      "speaker_notes": "Short speaker notes for this slide"
    }
  ]
}
Create 5–8 slides covering: context, key points, implications, recommendations, next steps.
Return ONLY valid JSON, no extra text."""
}
