import requests

def fetch_data(endpoint, filters={}):
    url = f'https://rickandmortyapi.com/api/{endpoint}'
    response = requests.get(url, params=filters)
    
    return response.json() if response.status_code == 200 else None

characters = fetch_data('character', {'name': 'Rick'})

if characters:
    print(characters)
else:
    print('Erro ao consultar valores')