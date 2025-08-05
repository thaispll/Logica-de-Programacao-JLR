class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    def get_nome(self): #permite acessar atributo 
        return self.__nome
    
    def set_nome(self,nome): #permite modificar atributo
        if nome.strip(): #remove espaço no inicio e no fim
            self.__nome = nome
        else:
            print("Nome inválido")
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email=email
        else:
            print("Email inválido")

usuario = Usuario("Carlos", "carlos@email.com")
print(usuario.get_nome())

usuario.set_nome("Carlos André")
print(usuario.get_nome())

usuario.set_email("email errado")
print(usuario.get_email())
    

