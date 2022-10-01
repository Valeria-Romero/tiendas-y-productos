from Producto import Producto

class Tienda:

    def __init__(self):
        self.nombre = "Shopping Center"
        self.producto = []

    def imprime_lista(self):
        print("Total de productos:",len(self.producto))
        for producto in self.producto:
            # self.producto.append(producto) Esto haría que tu producto se duplicara en la lista que ya existe
            print(producto.nombre)
    
    # Para cambiar el precio ya ese método existe en la clase de producto, entonces hacemos un ciclo en la lista de productos que tenemos en la tienda y llamamos al método en la clase producto con los valores que pide
    def inflacion(self, porcentaje_aumento):
        for producto in self.producto:
            producto.actualizar_precio(porcentaje_aumento, True)
        return self

    def hacer_liquidacion(self, categoria_p, porcentaje_descuento):
        for producto in self.producto:
            if producto.categoria == categoria_p:
                producto.actualizar_precio(porcentaje_descuento, False)
        return self

    # Para agregar un producto primero se crea una instancia del producto y luego se añade a la lista en la clase tienda
    def agregar_producto(self, nuevo_producto):
        self.producto.append(nuevo_producto)
        return self
    
    # Para eliminar un elemento en una lista se usa el metodo remove(), como se necesita que sea muy especifico, hacemos un ciclo revisando si el id del producto corresponde con el que se llamo la funcion y una vez ubicado se hace el remove de ese objeto especifico
    def vender_producto(self, id):
        for elemento in self.producto:
            if elemento.id == id:
                self.producto.remove(elemento)
        return self