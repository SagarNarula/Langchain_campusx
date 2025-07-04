from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int


new_person:Person={'name':'Sagar','age':31}
new_person:Person={'name':'Sagar','age':'31'}
print(new_person)