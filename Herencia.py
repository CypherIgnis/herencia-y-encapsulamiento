class Programmer:
  
    company_name='Sodimac'
    company_domain='@sodimac.cl'


    def __init__(self,id,first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name    
        self.mail = self.first_name+'.'+self.last_name+self.company_domain

    def print_info(self):
        return print("Te damos la bienvenida a ",self.company_name," ",self.first_name,' ',self.last_name,'Y su correo laboral es',self.mail)

class Chief(Programmer):
    def __init__(self,id,first_name,last_name,language):
        super().__init__(id,first_name,last_name)        
        self.language = language
        
    def print_language(self):
        return print("El lenguaje de programación que se manejar es el:",self.language)


