# GitHub Contribution Tracker

A Python command-line tool that analyzes GitHub users and summarizes their repository statistics and contribution activity using the GitHub REST API.

This project provides a quick overview of a developer's GitHub profile, including repository statistics, programming language usage, and contribution activity.

---

## Features

- Fetch GitHub user profile information
- Analyze repository statistics
- Calculate total stars and forks across repositories
- Detect the most frequently used programming language
- Count pull requests created by the user
- Count issues created by the user
- Clean CLI table output using tabulate
- Basic GitHub API error handling

## Technologies Used

- Python
- GitHub REST API
- Requests library
- JSON data processing

---

## Project Structure

```
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
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/taditharun/github-contribution-tracker.git
```

Navigate to the project directory:

```bash
cd github-contribution-tracker
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program with a GitHub username:

```bash
python main.py <github_username>
```

Example:

```bash
python main.py torvalds
```

---

## Example Output

```
GitHub Contribution Analysis
----------------------------

User: torvalds
Followers: 250000
Public Repositories: 8

Repository Statistics
---------------------

Total Stars Received: 120000
Total Forks: 35000
Most Used Language: C

Contribution Activity
---------------------

Pull Requests Created: 340
Issues Created: 120
```

---

## GitHub API Endpoints Used

This project uses the following GitHub API endpoints:

```
GET /users/{username}
GET /users/{username}/repos
GET /search/issues?q=author:{username}+type:pr
GET /search/issues?q=author:{username}+type:issue
```

Official API documentation:  
https://docs.github.com/en/rest

---

## Future Improvements

Possible enhancements for this project:

- Commit activity analysis
- Language usage charts
- Export analysis results to JSON or CSV
- Web-based dashboard version
- GitHub API rate limit handling

---

## Author

Tharun  

GitHub:  
https://github.com/taditharun