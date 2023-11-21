# import pymoni 
# class Money:
#     owo = 'sapa'
#     def __init__(self, xrate, watermark, bills):
#         self.xrate = xrate

#     def dollar():
#             ego = 'owu'

#     def __str__(self):
#          print(f'')

# aza = Money()
# aza.dollar()

# wallet = Money()
# wallet.dollar()

class Gadget:
    def __init__(self,m_phone, laptop):
        self.m_phone = m_phone
        self.laptop = laptop

class Laptop(Gadget):
    def __init__(self, m_phone, laptop, airpod):
        super().__init__(m_phone, laptop)
        self.airpod = airpod
        
class Phone(Laptop):
     pass