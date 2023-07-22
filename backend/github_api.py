import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_github_repository(owner, repo_name, token):
    """
    Retrieves information about a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        token (str): Your GitHub personal access token.

    Returns:
        dict: A dictionary containing information about the repository.
    """
    g = Github(token)

    try:
        repo = g.get_repo(f"{owner}/{repo_name}")
    except Exception as e:
        return {"error": str(e)}

    repository_info = {
        "name": repo.name,
        "description": repo.description,
        "url": repo.html_url,
    }

    return repository_info

def get_github_issues(owner, repo_name, token):
    """
    Retrieves all issues from a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        token (str): Your GitHub personal access token.

    Returns:
        list: A list of dictionaries containing information about each issue.
    """
    g = Github(token)

    try:
        repo = g.get_repo(f"{owner}/{repo_name}")
        issues = repo.get_issues(state="all")
    except Exception as e:
        return [{"error": str(e)}]

    issues_list = []
    for issue in issues:
        issue_info = {
            "number": issue.number,
            "title": issue.title,
            "state": issue.state,
            "body": preprocess_text(issue.body),  # Preprocess the issue body
        }
        issues_list.append(issue_info)

    return issues_list

def preprocess_text(text):
    # Implement your text preprocessing logic here
    # For example, you can remove stopwords, HTML tags, etc.
    # ...

    # Example: Removing HTML tags using BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    processed_text = soup.get_text()

    return processed_text
