import re
import requests
from bs4 import BeautifulSoup

def setDesignPattern(text: str):
    text_without_breaks = re.sub(r'[\n\xa0]', '', text)
    return text_without_breaks

def get_pernambuco_events():
    url = 'https://recifeingressos.com/eventos'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        events = []

        events_html = soup.find_all('div', class_='evento')

        for event_html in events_html:
            event_name = event_html.find('h3').text
            ul_element = event_html.find('ul')
            li_elements = ul_element.find_all('li')
            location_event = li_elements[0].text
            date_event = re.sub('à', '-', li_elements[1].text)

            events.append({
                'name': setDesignPattern(event_name),
                'date': setDesignPattern(date_event),
                'location': setDesignPattern(location_event)
            })

        return events
    else:
        print('Could not retrieve events.')
        return []