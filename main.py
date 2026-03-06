import sys

from tracker.github_api import (
    get_user_profile,
    get_user_repos,
    get_pull_requests,
    get_issues
)

from tracker.profile_stats import extract_profile_stats
from tracker.repo_stats import analyze_repositories


def run_tracker(username):

    profile = get_user_profile(username)
    repos = get_user_repos(username)
    pull_requests = get_pull_requests(username)
    issues = get_issues(username)

    profile_stats = extract_profile_stats(profile)
    repo_stats = analyze_repositories(repos)

    print("\nGitHub Contribution Analysis")
    print("-----------------------------")

    print(f"User: {profile_stats['name']}")
    print(f"Followers: {profile_stats['followers']}")
    print(f"Public Repositories: {profile_stats['public_repos']}")

    print("\nRepository Statistics")
    print("---------------------")

    print(f"Total Stars Received: {repo_stats['stars']}")
    print(f"Total Forks: {repo_stats['forks']}")
    print(f"Most Used Language: {repo_stats['top_language']}")

    print("\nContribution Activity")
    print("---------------------")

    print(f"Pull Requests Created: {pull_requests}")
    print(f"Issues Created: {issues}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python main.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]

    run_tracker(username)