import psycopg2


class dataMod():
    def __init__(self):
        self.connection = psycopg2.connect(host='localhost', port='5432',
                                           user='Guest', password='1234', database='banking')  # credentials and the database to aim at in the postgreSQL server
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()



class DbCustomer(dataMod):
    def createTable(self):
        createTableCom = f"""
                CREATE TABLE banking (
                    id_num varchar(30) NOT NULL,
                    email varchar(50) NOT NULL,
                    time_zone varchar(30) NOT NULL,
                    first_name varchar(30) NOT NULL,
                    last_name varchar(30) NOT NULL
                );
            """
        createTableComA = f"""
                CREATE TABLE credit_cards (
                    client_id varchar(30) NOT NULL,
                    authorizer varchar(30) NOT NULL,
                    card_number varchar(30) NOT NULL,
                    expiration_date varchar(30) NOT NULL,
                    balance decimal(18,2) NOT NULL
                );
            """
        self.cursor.execute(createTableCom)
        self.cursor.execute(createTableComA)
        # self.cursor.close()
        # self.connection.close()

    def insert(self, file):
        statement = f"""
        INSERT INTO banking (
            id_num,
            email,
            time_zone,
            first_name,
            last_name
        )
        VALUES(
            '{file.id}',
            '{file.email}',
            '{file.timeZone}',
            '{file.firstName.replace("'","''")}',
            '{file.lastName.replace("'","''")}'
        );
    """
        self.cursor.execute(statement)
        # self.cursor.close()
        # self.connection.close()

    def insertCard(self, clientId, file):
        statement = f"""
        INSERT INTO credit_cards(
            client_id,
            authorizer,
            card_number,
            expiration_date,
            balance
        )
        VALUES(
            '{clientId}',
            '{file.authorizer}',
            '{file.cardNum}',
            '{file.expirationDate}',
            '{file.balance}'
        );
        """
        self.cursor.execute(statement)
        # self.cursor.close()
        # self.connection.close()
