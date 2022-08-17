class area:
    def find_area(self,side):
        self.a=side*side
        return self.a
    def find_area(self,l,b):
        self.a=l*b
        return self.a
a=area()
result=a.find_area(8,8)
print("Area is: ",result)
