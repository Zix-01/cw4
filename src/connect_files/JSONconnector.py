import json
from abc import ABC
from pathlib import Path

from src.connect_files.ABCconnector import FileConnector
from src.dto import Vacancy, Salary


class JSONconnector(FileConnector, ABC):

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.encoding = 'utf-8'

    def get_vacancies(self) -> list[Vacancy]:
        if not self.file_path.exists():
            return []

        vacancies = []
        with self.file_path.open(encoding=self.encoding) as file:
            for item in json.load(file):
                vacancy = self._parse_dict_to_vacancy(item)
                vacancies.append(vacancy)

        return vacancies

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
        self._save(*vacancies)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        if vacancy in vacancies:
            vacancies.remove(vacancy)
            self._save(*vacancies)

    def _save(self, *vacancies: Vacancy) -> None:
        data = [self._parse_vacancy_to_dict(vac) for vac in vacancies]
        with self.file_path.open('w', encoding=self.encoding) as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    @staticmethod
    def _parse_vacancy_to_dict(vacancy: Vacancy) -> dict:
        return {
            'name': vacancy.name,
            'url': vacancy.url,
            'employer': vacancy.employer,
            'salary': {
                'currency': vacancy.salary.currency,
                'salary_to': vacancy.salary.salary_to,
                'salary_from': vacancy.salary.salary_from
            }
        }

    @staticmethod
    def _parse_dict_to_vacancy(data: dict) -> Vacancy:
        return Vacancy(
            name=data['name'],
            url=data['url'],
            employer=data['employer'],
            salary=Salary(
                salary_from=data['salary']['salary_from'],
                salary_to=data['salary']['salary_to'],
                currency=data['salary']['currency'],
            )
        )
