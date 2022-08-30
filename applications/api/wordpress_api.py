import requests


class WordPressAPI:
                       
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        

    def get_user(self, id: str):
        r = requests.get(f"{self.base_url}/users/{id}")
        r.raise_for_status()
        
        return r.json()

    def get_category(self, id: str):
        r = requests.get(
            f"{self.base_url}/categories/{id}",
        
            )

        r.raise_for_status()

        return r.json()
