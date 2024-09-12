import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Переменные окружения
GITHUB_API_URL = "https://api.github.com"
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

# Заголовки с аутентификацией
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def create_repo():
    url = f"{GITHUB_API_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "private": False
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Репозиторий {REPO_NAME} успешно создан.")
    else:
        print(f"Ошибка при создании репозитория: {response.status_code} - {response.json()}")

def check_repo():
    url = f"{GITHUB_API_URL}/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url, headers=headers)
    repos = response.json()
    repo_names = [repo['name'] for repo in repos]
    if REPO_NAME in repo_names:
        print(f"Репозиторий {REPO_NAME} найден.")
    else:
        print(f"Репозиторий {REPO_NAME} не найден.")

def delete_repo():
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Репозиторий {REPO_NAME} успешно удалён.")
    else:
        print(f"Ошибка при удалении репозитория: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    create_repo()
    check_repo()
    delete_repo()
