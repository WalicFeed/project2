import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = "Hello, Flet!"
    page.add(
        ft.Text("Welcome to Flet!"),
        ft.ElevatedButton("Click me!", on_click=lambda e: print("Button clicked!"))
    )

if __name__ == "__main__":
    main_db.init_db()
    # ft.run(main, view = ft.AppView.WEB_BROWSER)
