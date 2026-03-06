def extract_profile_stats(profile):

    return {
        "name": profile.get("login"),
        "followers": profile.get("followers"),
        "public_repos": profile.get("public_repos"),
    }