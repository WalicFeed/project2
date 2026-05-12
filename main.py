import flet as ft
from db import main_db


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()

    def view_tasks(task_id,task_text):
        def enable_edit(e):
            if task_field.read_only:
                task_field.read_only = False
            else:
                task_field.read_only = True
        def save_task(e):
            main_db.update_task(task_field.value, task_id)
            task_field.read_only = True
        def delete_task(e):
            main_db.delete_task(task_id)
            task_list.controls.remove(task_row)
        
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)
        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_task)
        task_row = ft.Row([task_field, edit_button, save_button, delete_button])
        return task_row

    def add_task(e):
        if task_input.value:
            task = task_input.value
            task_id = main_db.insert_task(task)
            print(f"Task {task} added with ID: {task_id}")
            task_list.controls.append(view_tasks(task_id = task_id, task_text = task))
            task_input.value = ""

    task_input = ft.TextField(label="Your task: ", expand=True)
    task_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task)

    send_task = ft.Row([task_input, task_button])
    page.add(
        send_task,
        task_list
    )

if __name__ == "__main__":
    main_db.init_db()
    ft.run(main, view = ft.AppView.WEB_BROWSER)
