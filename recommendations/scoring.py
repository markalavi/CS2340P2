# Returns a candidate's score (ranges from 0.0 to 1.0)
def candidate_score(required_skills : set, candidate_skills : set) -> float:
    if not required_skills:
        return 0.0
    return len(required_skills.intersection(candidate_skills)) / len(required_skills)