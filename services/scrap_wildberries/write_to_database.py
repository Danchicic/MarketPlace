import random
import sqlite3

from parser import unparse_wb_json
from json_data import JSON


class Row:
    def __init__(self, name: str, price: int, image_url: str, description: str = ''):
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url


class CRUD:
    def __init__(self):
        self.conn = sqlite3.connect('../../db.sqlite3')
        self.cur = self.conn.cursor()

    def write_row(self, row: Row):
        shop_id = random.choice([1, 2, 3, 8, 9])
        req = f"""
        INSERT INTO market_product
        (name, price, product_description, preview, category_id, shop_id) 
        VALUES('{row.name}','{row.price}', '{row.description}', '{row.image_url}',
        3, {shop_id})
        """
        self.cur.execute(req)
        self.conn.commit()


def write_data(db: CRUD):
    for name, price, desc, image_url in unparse_wb_json(JSON):
        row = Row(name, price, image_url, desc)
        try:
            db.write_row(row)
        except Exception:
            continue


def main():
    db = CRUD()
    write_data(db)


if __name__ == '__main__':
    main()
