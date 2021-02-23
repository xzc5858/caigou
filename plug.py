import requests
from bs4 import BeautifulSoup


def request_post(url, data):
    try:
        response = requests.post(url, data)
        if response.status_code == 200:
            return response
    except requests.RequestException:
        return None


def request_get(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
    except requests.RequestException:
        return None


def request_getsoup(url):
    r = request_get(url)
    soup = BeautifulSoup(r.text, "html5lib")

    return soup


def request_postsoup(url, data):
    r = request_post(url, data)
    soup = BeautifulSoup(r.text, "html5lib")

    return soup


def request_soup(url, isGet, data):
    if isGet:
        # print('get')
        return request_getsoup(url)
    else:
        # print('post')
        return request_postsoup(url, data)
