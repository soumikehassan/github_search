import requests

def search_github(query):

    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        items = data['items']

        for item in items:
            print(f"Repository name: {item['name']}")
            print(f"Link: {item['html_url']}\n")

    else:
        print("Error: Could not retrieve search results.")

# Example usage:
search_query = input("Enter your GitHub search query: ")
search_github(search_query)




