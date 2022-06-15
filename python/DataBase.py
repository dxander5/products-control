import pymysql

class DataBase:
    def __init__(self):
        self.conection = pymysql.connect(
            host='localhost',
            user='root',
            password='Db1123',
            db='ejercicios'
        )

        self.cursor = self.conection.cursor()
        print('conexion exitosa')

    def addProduct(self, nombre, precio, cantidad):
        sql = f"INSERT INTO productos (nombre, precio, cantidad) VALUES ('{nombre}', {precio},{cantidad})"
        try:
            self.cursor.execute(sql)
            self.conection.commit()
            print('Se agrego el producto')
        except Exception as e:
            raise
    def seleciionarDato(self, id):
        sql = f'SELECT * FROM registro WHERE id={id}'
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            print("Id: ", user[0], " nombre: ", user[1], " edad ", user[2])
        except Exception as e:
            raise

    def selectAllData(self):
        sql = 'SELECT * FROM productos'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
            # for user in users:
            #     print("Id: ", user[0], " nombre: ", user[1], " precio ", user[2], " cantidad ", user[3])
            #     # print('\n')
        except Exception as e:
            raise

    def updateProduct(self, id, newName, newPrice, newQuantity):
        sql = f"UPDATE productos set nombre='{newName}', precio={newPrice}, cantidad={newQuantity} WHERE id={id}"

        try:
            self.cursor.execute(sql)
            self.conection.commit()
            # print('Se actualizo el dato con el id', id)
        except Exception as e:
            raise

    def deleteProduct(self, id):
        sql = f"DELETE FROM productos WHERE id={id}"
        try:
            self.cursor.execute(sql)
            self.conection.commit()
            # print('Se elimino el producto con el id', id)
        except Exception as e:
            raise
    def closeConnection(self):
        print('conexion cerrada')
        self.conection.close()