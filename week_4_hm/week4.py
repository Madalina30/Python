import requests
from bs4 import BeautifulSoup
import csv
from week_4_hm.handle.extract_data import get_data

'''
Să se scrie un web scraper care obține date pe care le afișează într-un fișier:
○ datele ce urmează a fi obținute sunt la alegere (pentru lipsă de idei 
puteți obține informații despre articolele
disponibile la adresa http://frsah.ro/)
○ formatul fișierului și modul de stocare al datelor este la alegere.
○ extra:
➠ adăugați funcționalitate de citire a informației din fișier 
și afișarea ei în consolă.
➠ adăugați funcționalitate de citire a informației anterioare 
și completarea acesteia cu informații noi
'''

# new_cars = [
#     ['dacia', 'logan', 2005],
#     ['renault', 'clin', 2005]
# ]

# profs.info.uaic.ro/~orar/participanti/orar_I2B2.html
# get zilele (un row), ore_inceput (alt row),
# ore_final (alt row), materie (alt row)
# html - body - p[0] - table - tbody - tr - td: get data

URL = "https://profs.info.uaic.ro/~orar/participanti/orar_I2B2.html"

if __name__ == '__main__':
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='html.parser')
    table = soup.find('table')
    table_rows = table.findAll('tr')
    orar = list(map(get_data, table_rows))
    # print("orar", orar)
    # names = table_rows.find_all('th')
    # print("\nnames:\n", names)

    with open('C:/Users/Mada/Desktop/python HM/week_4_hm/data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for ore in orar:
            csv_writer.writerow(ore)

    # functionalitatea de citire a inf din fis si afis ei in consola
    with open('C:/Users/Mada/Desktop/python HM/week_4_hm/data.csv', 'r') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            print(row)
