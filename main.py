from src.clients.ABCclient import BaseAPIclient
from src.clients import HeadHunterAPI
from src.connect_files import JSONconnector
from src.connect_files.ABCconnector import FileConnector
from pathlib import Path

Base_Path = Path(__file__).parent
Vacancies_Path_File = Base_Path.joinpath('vacancies.json')

APIclients: BaseAPIclient = HeadHunterAPI()
connector: FileConnector = JSONconnector(Vacancies_Path_File)

welcome = '''
Добро пожаловать, выберите действия: 
    1. загрузить доступные вакансии по ключевому слову.
    2. вывести топ 5 вакансий.
    3. выход.
    '''


def main():
    vacancies = []
    while True:
        print(welcome)
        user_input = input()
        if not user_input.isdigit():
            continue

        user_answer = int(user_input)

        if user_answer == 1:
            search_word = input('Введите ключевое слово для поиска: ')

            try:
                vacancies = APIclients.get_vacancies(search_word.lower())

            except KeyError as e:
                print(f'Ошибка: Ничего не найдено по ключу "{e}"')
            except Exception as e:
                print(f"Ошибка: {e}")

            for vac in vacancies:
                connector.add_vacancy(vac)

        elif user_answer == 2:
            vacancies = connector.get_vacancies()
            for vac in sorted(vacancies, key=lambda x: x.salary, reverse=True)[:5]:
                print(vac)

        if user_answer == 3:
            break


if __name__ == '__main__':
    main()
