from Tienda import Tienda
from Producto import Producto

# Tienda = Tienda()
# Tienda.producto1 = Producto("Mesa", 20000, "Casa y Jardín", 75001)
# Tienda.producto2 = Producto("Silla", 10000, "Casa y Jardín", 75002)

# Tienda.producto1.actualizar_precio(0.05, True)
# Tienda.producto1.print_info()

# Tienda.producto2.actualizar_precio(0.05, False)
# Tienda.producto2.print_info()

# Tienda.inflacion(0.1)

# Tienda.hacer_liquidacion("Casa y Jardín", 0.3)

# Tienda.imprime_lista()

# """Producto.agregar_producto("Estante",30000,"Interiores",75003)
# Producto.imprime_lista()"""

# """Tienda.producto3 = Producto("Estante", 30000, "Interiores", 75003)
# Producto.imprime_lista()"""

# """Producto.vender_producto(75003)
# Producto.imprime_lista()"""

lampara = Producto("Lampara", 100, "hogar", 111)
atun = Producto("Atun", 5, "comida", 222)
zapato = Producto("Zapato", 150, "vestimenta", 333)
blusa = Producto("Blusa", 50, "vestimenta", 444)
tenedor = Producto("Tenedor", 7, "cocina", 555)

shoppingcenter = Tienda()

# Agregamos los 5 productos que creamos a la lista y la imprimimos
shoppingcenter.agregar_producto(lampara).agregar_producto(atun).agregar_producto(zapato).agregar_producto(blusa).agregar_producto(tenedor).imprime_lista()

# Eliminamos el producto lampara que tiene el id 111 e imprimimos la lista
shoppingcenter.vender_producto(444).imprime_lista()
# Nota que ya la blusa no aparece en la lista

# Bonus
# Para ver la información antes de hacer la liquidación
zapato.print_info()
blusa.print_info()
# Hace la liquidación e imprime la info nueva
shoppingcenter.hacer_liquidacion("vestimenta", 0.05)

# Bonus 
shoppingcenter.inflacion(0.03)
