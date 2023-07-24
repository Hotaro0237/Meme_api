import requests

def fetch_random_meme():
    api_url = 'https://meme-api.com/gimme'
    try:
        res = requests.get(api_url)

        if res.status_code == 200:
            data = res.json()
            meme_url = data['url']  # Extract the URL of the meme image
            title = data['title']
            return meme_url, title
        else:
            print(f"Error: Unable to fetch data from the API. Status code: {res.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    
if __name__ == "__main__":
    meme_url, meme_title = fetch_random_meme()
    if meme_url and meme_title:
        print("Meme URL:", meme_url)
        print("Meme title:", meme_title)
    else:
        print('Failed to fetch meme.')