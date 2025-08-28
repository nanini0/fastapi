from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from typing import List


app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"hola mundo con FastAPI"}

#validacion
class Producto(BaseModel):
    id : Optional[int] = None
    nombre: str
    precio: float
    stock: int

#base de datos en memoria
productos = []
contador_id = 1

#endpoints crud
#get listar los productos
@app.get("/productos", response_model=List[Producto])
def Listar_productos():
    return productos

#get por id
@app.get("/productos/{productos_id}",response_model=Producto)
def obtener_productos(producos_id: int):
    for prod in productos:
        if prod.id == producos_id:
            return prod
        
    raise HTTPException(status_code=404,detail="Productos no encontrado")


#post crear
@app.post("/prodctos",response_model=Producto)
def crear_productos(producto:Producto):
    global contador_id
    producto.id = contador_id
    contador_id+=1
    productos.append(producto)
    return producto


#put actualizar

@app.put("/productos/{producto_id}",response_model=Producto)
def actualizar_producto(producto_id: int, datos: Producto):
    for i, prod in enumerate(productos):
        if prod.id == producto_id:
            datos.id = producto_id
            productos[i]=datos
            return datos
    raise HTTPException(status_code=404,detail="producto no encontrado")

#delete

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    for i, prod in enumerate(productos):
        if prod.id == producto_id:
            productos.pop(i)
            return {"message":"Producto {prod.id} eliminado"}
    raise HTTPException(status_code=404,detail="productos no encontrado")






