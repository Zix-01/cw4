from src.clients.ABCclient import BaseAPIclient
from src.clients import HeadHunterAPI
from src.connect_files import JSONconnector
from src.connect_files.ABCconnector import FileConnector
from pathlib import Path

Base_Path = Path(__file__).parent
Vacancies_Path_File = Base_Path.joinpath('vacancies.json')

clients: BaseAPIclient = HeadHunterAPI()
connector: FileConnector = JSONconnector(Vacancies_Path_File)

welcome = '''
Добро пожаловать, выберите действия:
    1. загрузить доступные вакансии по ключевому слову.
    2. вывести топ 5 вакансий.
    3. выход.
    '''


def main():
    while True:
        print(welcome)
        user_input = input()
        if not user_input.isdigit():
            continue

        user_answer = int(user_input)
        if user_answer == 0:
            break


if __name__ == '__main__':
    main()
