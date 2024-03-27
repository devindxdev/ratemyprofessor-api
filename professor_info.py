import ratemyprofessor

def summarize_course_ratings(ratings):
    """Summarizes ratings for a single course."""
    total_rating = sum(r.rating for r in ratings)
    total_difficulty = sum(r.difficulty for r in ratings)
    would_take_again_count = sum(1 for r in ratings if r.take_again)
    return {
        'average_rating': total_rating / len(ratings),
        'average_difficulty': total_difficulty / len(ratings),
        'would_take_again_percentage': (would_take_again_count / len(ratings)) * 100
    }

def get_professor_info(professor_name):
    """Fetches and prints professor information and ratings for a given name at Thompson Rivers University."""
    university = ratemyprofessor.get_school_by_name("Thompson Rivers University")
    professor = ratemyprofessor.get_professor_by_school_and_name(university, professor_name)

    if professor is not None:
        info = {
            "name": professor.name,
            "department": professor.department,
            "school": professor.school.name,
            "rating": professor.rating,
            "difficulty": professor.difficulty,
            "num_ratings": professor.num_ratings,
            "would_take_again": round(professor.would_take_again, 1) if professor.would_take_again is not None else 'N/A',
            "courses": []
        }

        for course in professor.courses:
            ratings = professor.get_ratings(course_name=course.name)
            course_info = {"name": course.name, "ratings": [], "summary": {}}
            if ratings:
                summary = summarize_course_ratings(ratings)
                course_info["summary"] = summary
                course_info["ratings"] = [{"userComment": rating.comment} for rating in ratings]
            else:
                course_info["summary"] = "No ratings found for this course."
            info["courses"].append(course_info)
        return info
    else:
        return {"error": "Professor not found"}
