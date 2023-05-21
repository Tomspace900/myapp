from api.configs.db_config import db


# ! exemples de requêtes SQL
class FormRepository:
    def save_form(self, data):
        # cursor = db.cursor()
        query = "INSERT INTO forms (name, email) VALUES (%s, %s)"
        values = (data["name"], data["email"])
        # cursor.execute(query, values)
        # db.commit()

    def get_forms(self):
        # cursor = db.cursor()
        query = "SELECT * FROM forms"
        # cursor.execute(query)
        # result = cursor.fetchall()
        # return result
        return []
