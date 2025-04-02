import uuid

class Cliente:
    def __init__(self, id: str, cpf:str, nome:str, email:str, data_nascimento:str):
        self.__id = id
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__data_nascimento = data_nascimento

    @property #tem a propriedade de tornar um metodo propriedade
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.id = id



    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf



    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.email = email

    def __str__(self):
        pass


class Funcionario:
    def __init__(self, id: str, cpf:str, nome:str, matricula:str, dt_nasc:str):
        self.__id = id
        self.__cpf = cpf
        self.__nome = nome
        self.__matricula = matricula
        self.__dt_nasc = dt_nasc

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.id = id

class Conta_Corrente:
    def __init__(self, numero: int, saldo: float, limite: float, cliente: Cliente):
        self.__numero = str(uuid.uuid4())
        self.__saldo = saldo
        self.__limite = limite
        self.__cliente = cliente

class Conta_poupanca:
     def __init__(self, numero, saldo, limite, cliente:Cliente):
        self.__numero = numero
        self.__agencia = agencia
        self.__banco = banco
        self.__cliente = cliente

class Banco:
    def __init__(self, cnpj: str, nome:str, agencia:str):
        self.__cnjp = cnpj
        self.__nome = nome
        self.__agencia = agencia

        self.contas = []
        self.funcionarios = []

cliente_x = Cliente("a43v", "435.542.543-65", "xyz", "a@gmail.com", "10/03/2004")
print(cliente_x.nome)
print(cliente_x.id)
print(cliente_x.cpf)
print(cliente_x.email)
print("\n")

cliente_y = Cliente("43c24", "764.765.423-65", "abc", "y@gmail.com", "43/76/1009")
print(cliente_y.nome)
print(cliente_y.id)

Funcionario_a = Funcionario("a324b", "098.987.875-45", "cleber", "3434", "28/05/2054")
print(Funcionario_a.nome)
print(Funcionario_a.id)

Conta_coco_1 = Conta_Corrente ("a", "brasil", "cliente_x")

conta_poup_1 = Conta_poupanca("3245", "a", "itau", "cliente_y")

banc_1 = Banco("cliente_x", "brasil", "cleber", "a")
