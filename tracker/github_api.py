import requests

BASE_URL = "https://api.github.com"


def get_user_profile(username):

    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)

    return response.json()


def get_user_repos(username):

    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url)

    return response.json()


def get_pull_requests(username):

    url = f"{BASE_URL}/search/issues?q=author:{username}+type:pr"
    response = requests.get(url)

    data = response.json()

    return data.get("total_count", 0)


def get_issues(username):

    url = f"{BASE_URL}/search/issues?q=author:{username}+type:issue"
    response = requests.get(url)

    data = response.json()

    return data.get("total_count", 0)