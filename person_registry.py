import pymysql.cursors
import pymysql

class PersonRegistry():
    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1',user='myuser', password='12345', db='my_users')
        self.cursor =  self.connection.cursor()
        # Creating schema
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR (20), birth DATE);")
            
    def get_sql_data(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def add_person(self, name,birth_day):
        registered_birt_day = self.get_birh_date(name)
        if registered_birt_day and registered_birt_day != birth_day:
            # update birth_day
            self.cursor.execute("UPDATE users SET birth = '"+str(birth_day)+"' WHERE name ='"+ name+"';")
            # self.data_base[name] = birth_day
        elif not registered_birt_day:
            # insert new birh_day
            self.cursor.execute("INSERT INTO users VALUES ('"+ name+"','"+str(birth_day)+"');")
            # self.data_base[name] = birth_day
        self.connection.commit()
    
    def get_birh_date(self,name):
        birth_date = self.get_sql_data("SELECT birth FROM users WHERE name = '"+ name +"';")
        return birth_date

    def remove_person(self,name):
        if self.get_birh_date(name):
            self.cursor.execute("DELETE FROM users  WHERE name ='"+ name+"';")
            self.connection.commit()