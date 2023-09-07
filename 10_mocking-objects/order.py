
class Order:
    def __init__(self,name, quantity):
        self.name = name
        self.requestedQuantity = quantity

    def checkAvailability(self, warehouse):
        return warehouse.quantityOnStock(self.name)  >= self.requestedQuantity

    def setEmailService(self,service):
        self.service = service
    
    def sendByEmail(self):
        self.service.sendOrder(self.name + ":" +  str(self.requestedQuantity))
