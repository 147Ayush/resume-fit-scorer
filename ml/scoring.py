def skill_match_score(resume_skills: set, jd_skills: set) -> float:
    if not jd_skills:
        return 0.0
    return round((len(resume_skills & jd_skills) / len(jd_skills)) * 100, 2)


def final_resume_score(skill_score: float, text_score: float) -> float:
    # Skills matter more than wording
    return round((0.6 * skill_score) + (0.4 * text_score), 2)
