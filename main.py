import sys
from tabulate import tabulate

from tracker.github_api import (
    get_user_profile,
    get_user_repos,
    get_pull_requests,
    get_issues
)

from tracker.profile_stats import extract_profile_stats
from tracker.repo_stats import analyze_repositories


def display_results(profile_stats, repo_stats, pull_requests, issues):
    table = [
        ["User", profile_stats["name"]],
        ["Followers", profile_stats["followers"]],
        ["Public Repositories", profile_stats["public_repos"]],
        ["Total Stars", repo_stats["stars"]],
        ["Total Forks", repo_stats["forks"]],
        ["Most Used Language", repo_stats["top_language"]],
        ["Pull Requests Created", pull_requests],
        ["Issues Created", issues]
    ]

    print("\nGitHub Contribution Analysis\n")
    print(tabulate(table, headers=["Metric", "Value"], tablefmt="github"))


def run_tracker(username):
    profile = get_user_profile(username)
    repos = get_user_repos(username)
    pull_requests = get_pull_requests(username)
    issues = get_issues(username)

    profile_stats = extract_profile_stats(profile)
    repo_stats = analyze_repositories(repos)

    table = [
        ["User", profile_stats["name"]],
        ["Followers", profile_stats["followers"]],
        ["Public Repositories", profile_stats["public_repos"]],
        ["Total Stars", repo_stats["stars"]],
        ["Total Forks", repo_stats["forks"]],
        ["Most Used Language", repo_stats["top_language"]],
        ["Pull Requests Created", pull_requests],
        ["Issues Created", issues]
    ]

    print("\nGitHub Contribution Analysis\n")
    print(tabulate(table, headers=["Metric", "Value"], tablefmt="github"))

    print("\nLanguage Usage\n")

    lang_table = []

    for lang, count in repo_stats["languages"].items():
        lang_table.append([lang, count])

    print(tabulate(lang_table, headers=["Language", "Repositories"], tablefmt="github"))