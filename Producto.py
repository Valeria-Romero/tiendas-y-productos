class Producto:

    def __init__(self, nombre_p, precio, categoria, id):
        self.nombre = nombre_p
        self.precio = precio
        self.categoria = categoria
        self.id = id

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado == True:
            self.precio = self.precio + (self.precio * cambio_porcentaje)
            print("El precio del producto",self.nombre,"se ha elevado a",self.precio)
        else:
            self.precio = self.precio - (self.precio * cambio_porcentaje)
            print("El precio del producto",self.nombre,"ha dismiuido a",self.precio)

    def print_info(self):
        print("Producto:",self.nombre,"; Precio:",self.precio,"; Categoría:",self.categoria,"; id:",self.id)