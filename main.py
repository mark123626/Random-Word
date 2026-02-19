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
    
    words = get_words()
    data = {"idx": 0, "correct": 0, "wrong": 0}

    target_word = ft.Text(value=words[0], size=40, weight="bold")
    input_box = ft.TextField(label="Type word and Enter", autofocus=True)
    status = ft.Text(size=20)
    progress = ft.Text(value=f"Word: 0 / {len(words)}")
    accuracy = ft.Text()

    def check_logic(e):
        current = words[data["idx"]]
        user_input = input_box.value.strip().lower()

        if user_input == current.lower():
            data["correct"] += 1
            status.value = "Correct!"
            status.color = "green"
        else:
            data["wrong"] += 1
            status.value = "Incorrect!"
            status.color = "red"

        data["idx"] += 1
        
        if data["idx"] < len(words):
            target_word.value = words[data["idx"]]
            input_box.value = ""
            progress.value = f"Word: {data['idx']} / {len(words)}"
        else:
            acc = (data["correct"] / len(words)) * 100
            target_word.value = "Game Over!"
            input_box.disabled = True
            accuracy.value = f"Accuracy: {acc:.1f}%"
            status.value = f"Correct: {data['correct']} | Wrong: {data['wrong']}"

        page.update()

    input_box.on_submit = check_logic
    page.add(target_word, input_box, status, progress, accuracy)

if __name__ == "__main__":
    ft.app(target=main)