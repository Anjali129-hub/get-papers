# get_papers/filter.py

def is_non_academic(affiliation: str) -> bool:
    affiliation = affiliation.lower()
    academic_keywords = [
        "university", "college", "hospital", "school", "institute",
        "research centre", "research center", "faculty", "dept", "department", "lab"
    ]
    return not any(word in affiliation for word in academic_keywords)
