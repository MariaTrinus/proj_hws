""" Лекція 11. Network. Requests """

print(f"\n=======================| Task 1 |=======================")

#   Create a program that allows you to search for images in gif format.
#   The program should allow you
#       to enter a search word.
#       Using this word, search for GIFs using the Giphy API.
#       As a result, print the links to the GIFs.

import requests  # I use pip install to install requests


def search_gifs(search_term, api_key):
    url = (f"https://api.giphy.com/v1/stickers/search?api_key={api_key}&q={search_term}&limit=1"
           f"&offset=0&rating=g&lang=en&bundle=messaging_non_clips")
    response = requests.get(url)
    data = response.json()
    gifs = data['data']
    for gif in gifs:
        gif_url = gif['images']['original']['url']
        print(gif_url)


def main():
    search_term = input(" Enter a search request: ")
    api_key = "IcBtB6lPQU3QMU39uMjcNfxeQD7RXfBS"
    print(f" Here is the link to the gif you were looking for: ")
    search_gifs(search_term, api_key)


main()

print(f"\n=======================| Task 2 |=======================")

#   Optional: Add the Telegram bot to the previous exercise.
#       Ask the user to enter a search word in the Telegram interface
#       and get a gif image as a result.

# One day I will do it, I promise )
print(f" This feature is under development) ")
