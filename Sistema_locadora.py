class Veiculos:
    def __init__(self, id_veiculo, modelo, placa, cor, ano, status):
        self.__id_veiculo = id_veiculo
        self.__modelo = modelo
        self.__placa = placa
        self.__cor = cor
        self.__ano = ano
        self.__status = status
    @property
    def id_veiculo(self):
        return self.__id_veiculo
    @id_veiculo.setter
    def id_veiculo(self, id_veiculo):
        self.id_veiculo = id_veiculo

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.modelo = modelo
    
    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, placa):
        self.placa = placa
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.cor = cor

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, ano):
        self.ano = ano

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.status = status

    def exibir_detalhes_veiculo(self):
        return f'DETALHES DO VEICULO:\nModelo: {self.modelo}\nPlaca: {self.placa}\nCor: {self.cor}\nStatus: {self.status}\n'


    
class Cliente:
    def __init__(self, id_cliente, nome, cpf, telefone, email):
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.id_cliente = id_cliente
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.telefone = telefone

    @property 
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.email = email
    
    def exibir_detalhes_cliente(self):
        return f'DETALHES DO CLIENTE:\nNome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}\n'



class Reserva:
    def __init__(self, id_reserva, data_inicio, data_fim, status, valor_total):
        self.__id_reserva = id_reserva
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__status = status
        self.__valor_total = valor_total

    @property 
    def id_reserva(self):
        return self.__id_reserva
    @id_reserva.setter
    def id_reserva(self, id_reserva):
        self.id_reserva = id_reserva
    @property
    def data_inicio(self):
        return self.__data_inicio
    @data_inicio.setter
    def data_inicio(self, data_incio):
        self.data_inicio = data_incio
    @property
    def data_fim(self):
        return self.__data_fim
    @data_fim.setter
    def data_fim(self, data_fim):
        self.data_fim = data_fim

    @property 
    def valor_total(self):
        return self.__valor_total
    @valor_total.setter
    def valor_total(self, valor_total):
        self.valor_total = valor_total

    def exibir_detalhes_reserva(self):
        return f'DETALHES DA RESERVA:\nData de inicio: {self.data_inicio}\nData final: {self.data_fim}\nValor da reserva: {self.valor_total}\n'

class Pagamento:
    def __init__(self, id_pagamento, id_reserva, data_pagamento, valor_pago, metodo_pagamento):
        self.__id_pagamento = id_pagamento
        self.__id_reserva = id_reserva
        self.__data_pagamento = data_pagamento
        self.__valor_pago = valor_pago
        self.__metodo_pagamento = metodo_pagamento

class Manutencao:
    def __init__(self, id_manutencao, id_veiculo, data_inicio, data_fim, descricao):
        self.__id_manutencao = id_manutencao
        self.__id_veiculo = id_veiculo
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__descricao = descricao

carro1 = Veiculos(123, 'Fusca', 1234, 'Azul', 2004, 'Alugado')
print(carro1.exibir_detalhes_veiculo())
cliente1 = Cliente(1233, 'Maria', 1234, 12445, 'maria@gmail.com')
print(cliente1.exibir_detalhes_cliente())
reserva1 = Reserva(1223, 12, 15, 'Alugado', 750)
print(reserva1.exibir_detalhes_reserva())