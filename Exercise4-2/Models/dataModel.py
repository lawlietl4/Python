import psycopg2


class dataMod():
    def __init__(self):
        self.connection = psycopg2.connect(host='localhost', port='5432',
                                           user='Guest', password='1234', database='banking')  # credentials and the database to aim at in the postgreSQL server
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()


class DbCustomer(dataMod):
    def createTable(self, table):
        createTableCom = f"""
                CREATE TABLE {table} (
                    id SERIAL NOT NULL PRIMARY KEY,
                    email varchar(50) NOT NULL,
                    password varchar(60) NOT NULL,
                    first_name varchar(20) NOT NULL,
                    last_name varchar(20) NOT NULL
                );
            """
        self.cursor.execute(createTableCom)
        self.cursor.close()
        self.connection.close()

    def delTable(self, table):
        deleteTableCom = f"""
        DROP TABLE {table}
        """
        self.cursor.execute(deleteTableCom)
        self.cursor.close()
        self.connection.close()

    def insert(self, email, password, firstName, lastName, table):
        statement = f"""
            INSERT INTO {table} (
                email,
                password,
                first_name,
                last_name
            )
            VALUES(
                '{email}',
                '{password}',
                '{firstName}',
                '{lastName}'
            );
        """
        self.cursor.execute(statement)
        self.cursor.close()
        self.connection.close()

    def login(self, username, password):
        self.password = ''
        self.username = ''
        self.connection = psycopg2.connect(host='localhost', port='5432',
                                           user=username, password=password)

    def select(self, table):
        statement = f"""
        SELECT id
            , email
            , password
            , first_name
            , last_name
        FROM {table}
        """
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()

        print(rows)
