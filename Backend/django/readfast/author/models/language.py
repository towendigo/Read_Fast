from .author_en import Author_en
from .author_tr import Author_tr
from .data import *

def LanguageSet():
    return {
        'en': Author_en,
        'tr': Author_tr
    }