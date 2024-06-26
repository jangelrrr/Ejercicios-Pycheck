from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'
TASK_DONE_SYMBOL = '✔'
TASK_PENDING_SYMBOL = '⎕'


class Task:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo.'''

    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, done: bool = False, id: int = -1):
        '''Crea los atributos homónimos a los parámetros'''
        self.name = name
        self.done = done
        self.id = id

    def save(self):
        '''Guarda esta tarea en la base de datos.
        El identificador asignado en la base de datos se debe usar para actualizar el
        atributo id de la tarea.'''
        self.cur.execute('INSERT INTO Tarea VALUES ("self.name")')

    def update(self):
        '''Actualiza la tarea (nombre y estado) en la base de datos'''
        cur.execute('UPDATE Tarea SET name = self.name, id = self.id')

    def check(self):
        '''Marca la tarea como completada. Haz uso también de .update()'''
        Tarea.update(name = self_name, id = self_id, self.done = True)

    def uncheck(self):
        '''Marca la tarea como no completada. Haz uso también de .update()'''
        Tarea.update()

    def __repr__(self):
        '''Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)'''
        pass

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        '''Construye una nueva tarea a partir de una fila de consulta devuelta por execute()'''
        pass

    @classmethod
    def get(cls, task_id: int) -> Task:
        '''Devuelve un objeto Task desde la consulta a la base de datos'''
        pass


class ToDo:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo.'''

    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def create_db(self):
        '''Crea la base de datos con los campos "id", "name" y "done"'''
        self.cur.execute("""CREATE TABLE Tarea(
                    id INTEGER PRIMARY KEY
                    name TEXT
                    done BOOL
        )""")

    def get_tasks(self, *, done: int = -1):
        '''Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora.'''
        pass

    def add_task(self, name: str):
        '''Añade la tarea con nombre "name"'''
        self.cur execute('INSERT INTO Tarea VALUES ("name")'

    def complete_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como completada'''
        self.cur.execute('UPDATE Tarea SET done = True')

    def reopen_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como pendiente'''
        pass
