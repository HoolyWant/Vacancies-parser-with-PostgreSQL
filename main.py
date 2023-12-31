# from pprint import pprint

from src.api_utils import HHEmployers
from src.DBManager import DBManager
from src.config import config
from src import bd_utils

"""
Файл демонстрирует работу программы
"""

employers_id_list = ['733', '5178281', '5843588', '4917', # Список id работадателей
                     '2650528', '4082', '675403',
                     '3672566', '2696688', '4569685']

hh_employers = HHEmployers(employers_id_list)
hh_employers.get_hh_employers()
hh_employers.get_vacancies()
employers = hh_employers.employers_info
vacancies = hh_employers.vacancies_info
# pprint(vacancies)
# pprint(employers)

params = config('database.ini', 'postgresql')
bd_utils.create_database('hh_employers', params)
bd_utils.fill_employer_table('hh_employers', params, employers)
bd_utils.fill_vacancy_table('hh_employers', params, vacancies)

dbmanager = DBManager('hh_employers', params)
dbmanager.get_companies_and_vacancies_count()
dbmanager.get_all_vacancies()
dbmanager.get_avg_salary()
dbmanager.get_vacancies_with_higher_salary()
dbmanager.get_vacancies_with_keyword()
