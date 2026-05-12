import sqlite3
from config import path_db
from db import queries

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.tasks_table)
    conn.commit()
    conn.close()

def insert_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def select_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_tasks)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task, task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_task, (task, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_task, (task_id,))
    conn.commit()
    conn.close()