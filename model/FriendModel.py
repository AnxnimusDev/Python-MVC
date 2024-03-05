import psycopg2
import sys
from model.Friend import Friend

class FriendModel:
    
    def __init__(self) -> None:
        pass
    
    #Connection to DB
    try:
        conn = psycopg2.connect("host = 'localhost' dbname = 'friends' user = 'postgres' password = 'postgres'")
        if(conn):
            cursor = conn.cursor()
            print("Connection succesful!")
    except psycopg2.Error as error:
        print("Connection failed!")
        print(error)
        conn.close()
        sys.exit()
        
    #Funciones del Modelo
    
    #Checks if a user with the data of the given students exists in the data source.
    def find(self, friend) -> Friend:
        try:
            query = "SELECT * FROM friends WHERE phone = %s;"
            self.cursor.execute(query, friend.getPhone())
            result = self.cursor.fetchone()
            if result:
                phone = result[0]
                name = result[1]
                age = result[2]
                foundFriend = Friend(phone, name, age)
                return foundFriend
            else:
                return None
        except psycopg2.Error as error:
            print(error)
            return None
        
    #Adds a new user. This won't be implemented, just data cases
    def add(self, friend) -> int:
        try:
            query = "INSERT INTO friends (phone, name, age) VALUES (%s, %s, %s);"
            self.cursor.execute(query, (friend.getPhone(), friend.getName(), friend.getAge()))
            self.conn.commit()
            return 1
        except psycopg2.Error as error:
            print(error)
            return 0

    #Method that updates the oldFriend data with the newFriend data.
    def modify(self, oldFriend, newFriend) -> int:
        try:
            query = "UPDATE friends SET phone = %s, name = %s, age = %s WHERE phone = %s AND name = %s AND age = %s;"
            self.cursor.execute(query, (newFriend.getPhone(), newFriend.getName(), newFriend.getAge(),
                                         oldFriend.getPhone(), oldFriend.getName(), oldFriend.getAge()))
            self.conn.commit()
            return 1
        except psycopg2.Error as error:
            print(error)
            return 0
        
    #Removes a Friend from data source
    def remove(self, friend):
        try:
            query = "DELETE FROM friends WHERE phone = %s AND name = %s AND age = %s;"
            self.cursor.execute(query, (friend.getPhone(), friend.getName(), friend.getAge()))
            self.conn.commit()
            return 1
        except psycopg2.Error as error:
            print(error)
            return 0
        
    #Finds all Friends from the data source.
    def findAll(self):
        try:
            query = "SELECT * FROM friends;"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            result = []
            for row in result:
                phone = row[0]
                name = row[1]
                age = row[2]
                friend = Friend(phone, name, age)
                result.append(friend)
            return result
        except psycopg2.Error as error:
            print(error)
            return None
        
        
    def findFriendByName(self, givenName):
        try:
            query = "SELECT * FROM friends WHERE name = %s;"
            self.cursor.execute(query, (givenName,))
            result = self.cursor.fetchall()
            nameFilteredFriends = []
            for row in result:
                phone = row[0]
                name = row[1]
                age = row[2]
                friend = Friend(phone, name, age)
                nameFilteredFriends.append(friend)
            return nameFilteredFriends
        except psycopg2.Error as error:
            print(error)
            return None
    
    def closeConnection(self):
        self.conn.close()