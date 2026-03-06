# GitHub Contribution Tracker

A Python CLI tool that analyzes a GitHub user's contributions and repository statistics using the GitHub REST API.

This project collects information about a user's repositories, pull requests, issues, and programming language usage, then displays the results in a structured table.

--------------------------------------------------

FEATURES

• Fetch GitHub user profile information  
• Analyze public repositories  
• Calculate total stars across repositories  
• Calculate total forks across repositories  
• Identify most used programming language  
• Count pull requests created by the user  
• Count issues created by the user  
• Display repository language usage statistics  

--------------------------------------------------

TECHNOLOGIES USED

Python 3  
GitHub REST API  
Requests  
Tabulate  

--------------------------------------------------

PROJECT STRUCTURE

github-contribution-tracker
│
├── tracker
│   ├── __init__.py
│   ├── github_api.py
│   ├── profile_stats.py
│   └── repo_stats.py
│
├── main.py
├── requirements.txt
└── README.md

--------------------------------------------------

FILE DESCRIPTION

main.py  
Main CLI entry point that runs the program and displays formatted results.

tracker/github_api.py  
Handles communication with the GitHub REST API and retrieves data.

tracker/profile_stats.py  
Processes GitHub user profile statistics.

tracker/repo_stats.py  
Analyzes repository statistics such as stars, forks, and language usage.

--------------------------------------------------

INSTALLATION

Clone the repository

git clone https://github.com/yourusername/github-contribution-tracker.git

Move into the project folder

cd github-contribution-tracker

Install dependencies

pip install -r requirements.txt

--------------------------------------------------

USAGE

Run the program using a GitHub username.

python main.py <github_username>

Example

python main.py torvalds

--------------------------------------------------

EXAMPLE OUTPUT

GitHub Contribution Analysis

Metric                     Value
----------------------------------------
User                       torvalds
Followers                  200000+
Public Repositories        6
Total Stars                180000+
Total Forks                60000+
Most Used Language         C
Pull Requests Created      85
Issues Created             7

Language Usage

Language       Repositories
---------------------------
C              9
C++            1
OpenSCAD       1

--------------------------------------------------

FUTURE IMPROVEMENTS

• Add commit analytics  
• Add contribution timeline graphs  
• Export results to CSV or JSON  
• Add GitHub API authentication support  
• Build a web dashboard version  

--------------------------------------------------

AUTHOR :

Tharun

GitHub: https://github.com/taditharun  

Email: taditharun8@gmail.com
