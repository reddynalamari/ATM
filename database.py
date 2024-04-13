import mysql.connector as connector


class DBHelper():
    def __init__(self):
        self.con = connector.connect(
            host='localhost', port='3306', user='root', password='Your_password', database='atm',
            auth_plugin='mysql_native_password')
        query = 'create table if not exists accounts(a_num int primary key, pin int NOT NULL,balance int, name varchar(50), mailid varchar(100)\
              NOT NULL,UNIQUE(mailid))'
        cur = self.con.cursor()
        cur.execute(query)
        

    # inserting
    def insert_data(self,a_num,pin,balance,name,mailid):

        query = "insert into accounts(a_num,pin,balance,name,mailid)" \
                "values({},{},{},'{}','{}')".format(a_num,pin,balance,name,mailid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        cur.close()

    # Fetch values
    def fetch_password(self, a_num):
        query = f"select pin from accounts where a_num = '{a_num}'"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
                return row[0]
        cur.close()
    def mail_fetcher(self,mailid):
         query = f"select a_num from accounts where mailid = '{mailid}'"
         cur = self.con.cursor()
         cur.execute(query)
         for row in cur:
                return row[0]
    # delete
    def delete_account(self, a_num):
        query = "delete from accounts where a_num='{}'".format(a_num)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    # update
    def change_password(self,newpin,mailid):
        query = f"update accounts set pin={newpin} where mailid = '{mailid}'"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()



    def update_balance(self,a_num,new_balance):
        query = f"update accounts set balance='{new_balance}' where a_num = '{a_num}'"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def last_value(self):
         query = '''SELECT a_num
                FROM accounts
                ORDER BY a_num DESC
                LIMIT 1;
                '''
         cur = self.con.cursor()
         cur.execute(query)
         for i in cur:
             for j in i:
                  return j+1
             
    def fetch_balance(self,a_num):
         query = f'''SELECT balance
                FROM accounts
                where a_num = {a_num};
                '''
         cur = self.con.cursor()
         cur.execute(query)
         for i in cur:
            for j in i:
                return j
            
    def fetch_name(self,a_num):
         query = f'''SELECT name
                FROM accounts
                where a_num = {a_num};
                '''
         cur = self.con.cursor()
         cur.execute(query)
         for i in cur:
            for j in i:
                return j
            
    def mail_fetcher_once_check_db_file(self,a_num):
         query = f'''SELECT mailid
                FROM accounts
                where a_num = {a_num};
                '''
         cur = self.con.cursor()
         cur.execute(query)
         for i in cur:
            for j in i:
                return j

ob = DBHelper()
