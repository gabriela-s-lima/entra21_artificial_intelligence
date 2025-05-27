import os
import requests
from dotenv import load_dotenv

# Load the API KEY from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY_NEWS")

def fetch_news(topic, amount):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "pageSize": amount,
        "apiKey": API_KEY,
        "sortBy": "publishedAt",
        "language": "en"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    else:
        print(f"Error fetching news: {response.status_code}")
        return []

def interactive_menu():
    history = []
    total_news = 0
    
    while True:
        print("\n📰 NEWS MENU 📰")
        print("1 - Fetch news")
        print("2 - Exit")
        
        option = input("Choose an option: ")
        
        if option == "1":
            topic = input("Enter the topic you want to search for: ").strip()
            
            try:
                amount = int(input("How many news articles do you want? (1 to 10): "))
                if amount < 1 or amount > 10:
                    print("⚠️ Please choose a number between 1 and 10.")
                    continue
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue
            
            news = fetch_news(topic, amount)
            
            if news:
                print(f"\n🔍 News about '{topic}':\n")
                for idx, article in enumerate(news, start=1):
                    title = article.get('title', 'No title')
                    source = article.get('source', {}).get('name', 'Unknown source')
                    author = article.get('author', 'Unknown author')
                    
                    print(f"{idx}. 🗞️ {title}")
                    print(f"   Source: {source}")
                    print(f"   Author: {author}\n")
            else:
                print("No news found or an error occurred.")
            
            history.append({"topic": topic, "amount": amount})
            total_news += amount
        
        elif option == "2":
            print("\n📜 SEARCH HISTORY 📜")
            if history:
                for search in history:
                    print(f"- Topic: '{search['topic']}' | News fetched: {search['amount']}")
                print(f"\nTotal news fetched: {total_news}")
            else:
                print("No searches made.")
            print("\nThank you for using the news system! 👋")
            break
        
        else:
            print("⚠️ Invalid option, please try again.")

if __name__ == "__main__":
    interactive_menu()
