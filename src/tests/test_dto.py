import pytest

from src.dto import Salary


class TestSalary:

    def test_equal_none_salary_same_currency(self):
        salary1 = Salary(salary_to=None, salary_from=None, currency='RUB')
        salary2 = Salary(salary_to=None, salary_from=None, currency='RUB')

        assert salary1 == salary2

    def test_equal_not_none_salary_same_currency(self):
        salary1 = Salary(salary_to=100, salary_from=1_000, currency='RUB')
        salary2 = Salary(salary_to=100, salary_from=1_000, currency='RUB')

        assert salary1 == salary2

    def test_comparison_min_salary(self):
        lower_salary = Salary(salary_to=500, salary_from=None, currency='RUB')
        higher_salary = Salary(salary_to=1_000, salary_from=None, currency='RUB')

        assert lower_salary < higher_salary

    @pytest.mark.parametrize('not_none_salary', [
        {'salary_from': 100, 'salary_to': None},
        {'salary_from': None, 'salary_to': 300},
        {'salary_from': 100, 'salary_to': 300}
    ])
    def test_highest_salary_to(self, not_none_salary):
        lower_salary = Salary(salary_to=None, salary_from=None, currency='RUB')
        higher_salary = Salary(currency='RUB', **not_none_salary)

        assert lower_salary < higher_salary

    