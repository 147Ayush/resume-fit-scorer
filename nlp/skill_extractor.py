def extract_skills(text: str, skill_list: list) -> set:
    text = text.lower()
    return {skill for skill in skill_list if skill.lower() in text}
