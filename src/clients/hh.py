import requests

from src.clients.ABCclient import BaseAPIclient
from src.dto import Vacancy, Salary


def parse_data(data: dict) -> Vacancy:
    return Vacancy(
        name=data['name'],
        url=data['alternate_url'],
        employer=data['employer']['name'],
        salary=Salary(
            salary_from=data['salary']['from'],
            salary_to=data['salary']['to'],
            currency=data['salary']['currency']
        )
    )


class HeadHunterAPI(BaseAPIclient):

    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        url = 'https://api.hh.ru/vacancies/'
        params = {
            'only_with_salary': True,
            'per_page': 100,
            'text': search_text
        }

        response = requests.get(url, params=params, timeout=15)
        if not response.ok:
            print(f'Ошибка получения данных, {response.content}')
            return []

        return [
            parse_data(item) for item in response.json()['items']
        ]
