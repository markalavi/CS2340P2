# Returns a candidate's score (ranges from 0.0 to 1.0)
def candidate_score(required_skills : set, candidate_skills : set) -> float:
    return len(required_skills.intersection(candidate_skills)) / len(required_skills)