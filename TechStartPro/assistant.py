from database import *

def create_cat_table():
    """
    Create a table categories
    """
    try:
        create_table_cat()
        return 'i'
    except:
        return '0'
        pass

def create_product_table():
    try:
        create_table()
        return 'i'
    except:
        return '0'
        pass
def importCat(file):
    """
    IMPORTA A LISTA DE CATEGORIAS PARA UMA LISTA CHAMADA 'CATEGORY
    """
    import pandas as pd
    while True:
        category = []
        cat = pd.read_csv(file, header=None)
        for n in range(0, len(cat)):
            cater = cat.iloc[n][0]
            category.append(cater)
        try:
            add_category(category)
            return 'i'
        except:
            return '0'
            pass

def test_have_id(product, getId):
    """Test if have an Id on database products"""
    i = 0
    for n in range(0, len(product)):
        if product[n][0] == int(getId):
            id = n
            i += 1
    if i == 0:
        id = 'nf'
    return id

def add_product(list):
    try:
        add(list)
        return 'i'
    except:
        return '0'
        pass

create_product_table()