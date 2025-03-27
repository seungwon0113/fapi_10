from  enum import Enum
'''
from enum import Enum

class Skill(Enum):
    HTML = 1
    CSS = 2
    JS = 3

>>> Skill.HTML
<Skill.HTML: 'HTML'>
>>> Skill.HTML.name
'HTML'
>>> Skill.HTML.value
'''

from pydantic import BaseModel

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Users(BaseModel):
    username: str
    age: int
    gender: Gender

