import sqlite3 as sql

def create_table_cat():
    conn = sql.connect('category.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE categories (id integer PRIMARY KEY AUTOINCREMENT,
        category text)
    """)
    conn.commit()
    conn.close()

def add_category(infs):

    conn = sql.connect('category.db')
    c = conn.cursor()

    for n in range(0, len(infs)):
        cat = infs[n]
        c.execute("INSERT INTO categories (category) VALUES(?)", (cat,))

    conn.commit()
    conn.close()


def open_category():
    conn = sql.connect('category.db')
    c = conn.cursor()

    c.execute("SELECT * FROM categories")
    categories = c.fetchall()

    conn.commit()
    conn.close()

    return categories

def open_one_category(id):
    conn = sql.connect('category.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM categories WHERE id = {id}")
    categories = c.fetchall()

    conn.commit()
    conn.close()

    return categories


def delete_category():
    conn = sql.connect('category.db')
    c = conn.cursor()

    c.execute("DELETE from categories")

    conn.commit()
    conn.commit()


def create_table():
    conn = sql.connect('produtos.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE products (id integer PRIMARY KEY AUTOINCREMENT,
        name text,
        description text,
        cost real,
        categories text)
    """)
    conn.commit()
    conn.close()

def add(infs):
    conn = sql.connect('produtos.db')
    c = conn.cursor()

    c.executemany("INSERT INTO products (name, description, cost, categories) VALUES(?, ?, ?, ?)", (infs,))

    conn.commit()
    conn.close()

def open_products():
    conn = sql.connect('produtos.db')
    c = conn.cursor()

    c.execute("SELECT * FROM products")
    products = c.fetchall()

    conn.commit()
    conn.close()

    return products

def open_one_product(item, id):
    conn = sql.connect('produtos.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM products WHERE {item} =?", (id,))
    products = c.fetchall()

    conn.commit()
    conn.close()

    return products

def update_product(item, new, id):
    conn = sql.connect('produtos.db')
    c = conn.cursor()

    c.execute(f""" UPDATE products SET {item} = ?
        WHERE id = ?""", (new, id,))

    conn.commit()
    conn.close()

def delete_product(id):
    conn = sql.connect('produtos.db')
    c = conn.cursor()

    c.execute("DELETE from products WHERE id = ?",(id,))

    conn.commit()
    conn.close()
