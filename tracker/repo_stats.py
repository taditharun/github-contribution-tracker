def analyze_repositories(repos):

    total_stars = 0
    total_forks = 0
    languages = {}

    for repo in repos:

        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)
        language = repo.get("language")

        total_stars += stars
        total_forks += forks

        if language:
            languages[language] = languages.get(language, 0) + 1

    if languages:
        top_language = max(languages, key=languages.get)
    else:
        top_language = "None"

    return {
        "stars": total_stars,
        "forks": total_forks,
        "top_language": top_language,
        "languages": languages
    }