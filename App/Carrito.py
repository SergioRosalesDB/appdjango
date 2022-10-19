class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, product):
        id = str(product.ProductsKey)
        
        self.carrito[id]={
                "producto_id": product.ProductsKey,
                "matchkey": product.ProductsKey,
                "source": product.SourceKey,
                "brand": product.Brand,
                "modelnumber": product.ModelNumber,
                "productid": product.SourcesId,
                "producttitle": product.ProductTitle,
                "productdescription": product.ProductDescription,
                "cantidad": 1,
            
        }
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, product):
        id = str(product.ProductsKey)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, product):
        id = str(product.ProductsKey)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(product)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True