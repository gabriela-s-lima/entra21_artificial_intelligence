import requests
import os
from dotenv import load_dotenv


def fetch_cat_images(limit):
    
    # Fetches a specified number of cat images from TheCatAPI.
    
    load_dotenv()
    api_key = os.getenv("API_KEY_CAT")

    if not api_key:
        raise ValueError("API Key not found in environment variables.")

    url = "https://api.thecatapi.com/v1/images/search"
    headers = {'x-api-key': api_key}
    params = {"limit": limit}

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching images: {response.status_code}")


def ask_for_quantity():
   
    # Asks the user how many cat images they want to fetch (1 to 5).
    
    while True:
        try:
            qty = int(input("How many cats do you want to fetch? (max 5): "))
            if 1 <= qty <= 5:
                return qty
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def display_results(cat_list):
    
    #Displays the fetched cat image information (ID and URL).
    
    print("\n🐱 Cat images found:")
    for i, cat in enumerate(cat_list, start=1):
        print(f"{i}. ID: {cat.get('id', 'N/A')}")
        print(f"   URL: {cat.get('url', 'URL not found')}\n")


if __name__ == "__main__":
    quantity = ask_for_quantity()
    images = fetch_cat_images(quantity)
    display_results(images)
