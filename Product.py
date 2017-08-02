class Product():
    def  __init__(self,itemname,price,weight,brand,cost,status):
        self.status = "for sale"
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = "sold"
        print self.status
        return self
    def tax(self,tax):
        self.price = self.price + self.price * tax
        print self.price
        return self
    def Return(self,reason):
        if (reason == "defective"):
            self.status = "defective"
            self.price = 0
        elif (reason == "in box"):
            self.staus = "for sale"
        return self
    def displayinfo(self):
        print "Item name: " + self.itemname + " Price: " + str(self.price) + " weight: " + str(self.weight) + "lbs brand: " + self.brand + " cost: $" + str(self.cost) + " Status: " + self.status
        return self

Product("Pizza",10,12,"Nastyass Foods",5, "sold out").displayinfo()
