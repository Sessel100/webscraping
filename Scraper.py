from bs4 import BeautifulSoup
import requests



url = "https://chartmasters.org/most-streamed-artists-ever-on-spotify/"
r = requests.get(url)


soup = BeautifulSoup(r.text, 'html.parser')


artist_table = soup.find('table',class_ =  'responsive display nowrap data-t data-t wpDataTable wpDataTableID-1')



def get_artist(text):
    row_number = text
    table_row = soup.find("tr", {"id": f"table_1_row_{int(row_number) - 1}"})
    artist_name = table_row.find("a")

    try: 
        print (artist_name.text)
    
    except AttributeError:
        artist_name = table_row.find("b").text
        # print (table_row.find_all("td")[2].get_text())
        print(artist_name)

get_artist(67)

def get_streams(text):

      # Finidng the row number
    row_number = text

    table_row = soup.find("tr", {"id": f"table_1_row_{int(row_number) - 1}"}).find_all("td")[3]



    # Extract the artist name from the table row
    # streams = table_row.find("a").text

    print(table_row.get_text())

