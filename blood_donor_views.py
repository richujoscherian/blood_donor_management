from mysql import connector
import datetime

class BloodDonorManager:

    def __init__(self):
        self.connection = connector.connect(
            host="localhost",
            user="root",
            password="Richu@2003",
            database="blood_db_b3"
        )

        print("Connection successful")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """INSERT INTO donor
                       (name, blood_group, phone, city, last_donation)
                       VALUES (%s, %s, %s, %s, %s)"""

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)

            self.connection.commit()

            print("Donor added successfully...!")

        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            return records
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id= %s "
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record != None:
                query="delete from donor where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor deleted successfully")
            else:
                print("donor not found")
        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id =%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None


    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record != None:#if a record is found ,then record will not be none.so the update operation continues

                self.cursor = self.connection.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE donor SET {placeholder} WHERE id=%s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)

                self.connection.commit()

                print("Donor details updated Successfully..!")

            else:
                print("Donor not found")

        except Exception as e:
            print(e)



# Create object
# donor_instance = BloodDonorManager()
# donor_instance.retrieve(3)

# # Add donor
# donor_instance.post(
#     name="Suraj",
#     blood_group="O+",
#     phone="987211780",
#     city="Kochi",
#     last_donation=datetime.date.today()
# )
# donor_instance.post(
#     name="Anjali",
#     blood_group="A+",
#     phone="9876543210",
#     city="Kochi",
#     last_donation=datetime.date(2026, 7, 15)
# )
#
# donor_instance.post(
#     name="Rahul",
#     blood_group="B+",
#     phone="9123456780",
#     city="Thrissur",
#     last_donation=datetime.date(2026, 6, 20)
# )
#
# donor_instance.post(
#     name="Meera",
#     blood_group="AB+",
#     phone="9988776655",
#     city="Ernakulam",
#     last_donation=datetime.date(2026, 8, 5)
# )