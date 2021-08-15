from _typeshed import StrOrBytesPath
from typing import MutableSequence


age_text=input("age above 75= Y/N").lower()
age=False
immune=False
chronic=False
if age_text=="y":
    age=True

chronic_text=input("dou you have chronic sick = Y/N").lower()
if chronic_text=="y":
    chronic=True

immune_text=input("how your immune Weak/Strong").lower()
if immune_text=="weak":
    immune=True


if age==True and immune==True and chronic==True:
    print("You are in risky group")
else:
    print("You are not in risky group")

