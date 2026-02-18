import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Typing Test"

    def get_words():
        try:
            r = requests.get("https://random-word-api.herokuapp.com/word?number=15")
            return r.json()
        except:
            return ["apple", "banana", "cherry", "dragon", "elephant", "forest", "guitar", "honey", "island", "joker", "koala", "lemon", "mountain", "nature", "ocean"]