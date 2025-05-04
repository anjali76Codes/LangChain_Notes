from typing import TypedDict


class Person:
    name: str
    age: int


new_person: Person = {"name": "Yash", "age": 20}
print(new_person)
