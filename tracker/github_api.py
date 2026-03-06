import requests

BASE_URL = "https://api.github.com"


def fetch_json(url):
    """
    Send a GET request and safely return JSON.
    Handles common GitHub API errors.
    """
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    if response.status_code == 404:
        print("Error: GitHub user not found.")
        exit()

    if response.status_code == 403:
        print("Error: API rate limit exceeded. Try again later.")
        exit()

    print(f"Unexpected error: {response.status_code}")
    exit()


def get_user_profile(username):
    url = f"{BASE_URL}/users/{username}"
    return fetch_json(url)


def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"
    return fetch_json(url)


def get_pull_requests(username):
    url = f"{BASE_URL}/search/issues?q=author:{username}+type:pr"
    data = fetch_json(url)
    return data.get("total_count", 0)


def get_issues(username):
    url = f"{BASE_URL}/search/issues?q=author:{username}+type:issue"
    data = fetch_json(url)
    return data.get("total_count", 0)