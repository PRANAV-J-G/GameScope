import requests 
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("RAWG_API_KEY")
base_url = 'https://api.rawg.io/api'

def get_info(platforms):
    params = {'key':api_key,'page': page , 'page_size':40}
    url = f"{base_url}/platforms"
    print(url)
    response = requests.get(url,params=params)
    print(response.status_code)
    print(response.json())


games = "platforms"
print(get_info(games))


for page in range(1,6):
    pass
