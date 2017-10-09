# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 21:28:36 2017

@author: Home
"""

from Owner import Owner
from Dog import Dog
from Cat import Cat
import pandas as pd

Owners = pd.read_csv('owners.csv')
Dogs= pd.read_csv('dogs.csv')
Cats= pd.read_csv('cats.csv')
Owners_dict = {}
Dogs_dict = {}
Cats_dict = {}
def deleteOwner(id):
    Owners_dict.pop(id)
def createOwner(Owner):
    Owners_dict.update({Owners_dict.keys()[-1] + 1 : Owner})

def updateOwner(id, Owner):
    Owners_dict[id]=Owner

def displayOwner(id):
    print('Owner Name: ' + str(Owners_dict.get(id).first_name) +" "+ str(Owners_dict.get(id).last_name) )

def listAllOwners():
    for key in Owners_dict:
        print('Owner Name: ' + str(Owners_dict.get(key).first_name) +" "+ str(Owners_dict.get(key).last_name) )


def deleteCat(id):
    Owner_id=Cats_dict.get(id).Owner_id    
    print(Owner_id)
    print(Owners_dict.get(Owner_id).Cats_list).remove(str(id))

def deleteDog(id):
    Owner_id=Dogs_dict.get(id).Owner_id    
    print(Owner_id)
    print(Owners_dict.get(Owner_id).Dogs_list).remove(str(id))
    
def display_cat(id):
    print('Cat Name: ' + str(Cats_dict.get(id).name) )
    
def display_dog(id):
    print('Dog Name: ' + str(Dogs_dict.get(id).name) )
    
def createOwnersFromCSV():
    for i in range(len(Owners)):
        Owners_dict[Owners.loc[i,'Id']] = Owner(Owners.loc[i,'First Name'], Owners.loc[i,'Last Name'],
                    Owners.loc[i,'Birthday'],convertToList(list(Owners['Dogs_ids'][i])),
                    convertToList(list(Owners['Cats_ids'][i]))) 

def createDogsFromCSV():
    for i in range(len(Dogs)):
        Dogs_dict[Dogs.loc[i,'Id']] = Dog(Dogs.loc[i,'Name'], Dogs.loc[i,'Birthday'], Dogs.loc[i, 'Owner_id'])


def createCatsFromCSV():
    for i in range(len(Cats)):
        Cats_dict[Cats.loc[i,'Id']] = Cat(Cats.loc[i,'Name'], Cats.loc[i,'Birthday'], Cats.loc[i, 'Owner_id'])


def convertToList(list):
    return [i for i in list if i != ' ']
    

createOwnersFromCSV()
createDogsFromCSV()
createCatsFromCSV()

#print(Owners_dict.get(1).Cats_list.remove(str(3)))