from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("table_report") as html_file:
        soup = BeautifulSoup(html_file, "lxml")

    print(soup.title)
    print(soup.title.string)
    for cell in soup.find_all("td"):
        print(cell)
    print(soup.prettify())
    print(soup.get_text())