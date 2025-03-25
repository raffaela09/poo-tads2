#criar uma classe que representa um carro
#criar ao menos 4 atributos
#criar dois metodos
# --- ligar o carro
# --- desligar o carro
# --- Consumir combustivel (criar um laco para consumir o combustivel do carro)
#criar um metodo que retorna o valor do carro


class Carro:
   
    def __init__(self, modelo, cor, ano, combustivel, valor, combustivel_total, ligado=False, desligado=True):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.ligado = ligado
        self.desligado = desligado
        self.valor = valor
        self.combustivel_total = combustivel_total
        self.aceleracao = 0
        
#---------- Metodos da classe carro:    
 
    def ligar(self):
        if self.ligado:
            print(f'{self.modelo} já está ligado.')
            return
        self.ligado = True    
        self.desligado = False    
        print(f'O carro está ligado.')
        
    def desligar(self):
        if not self.desligado:
            print(f'{self.modelo} já está desligado.')
            return
        self.ligado = False
        self.desligado = True
        print(f'O {self.modelo} está desligado.')
        
    def consumir_combustivel(self, litros):
        if self.desligado:
            print(f'{self.modelo} está desligado, portanto, não pode consumir combustivel.')
            return
        if litros > self.combustivel_total:
            print(f'Não há combustivel suficiente para consumir, o carro só tem {self.combustivel_total}.')
        litros_restante = self.combustivel_total - litros
        print(f'O carro {self.modelo} consumiu {litros} litros de combustivel, restando {litros_restante} litros.')  
           
    def retornar_valor(self):
        return self.valor
    
    def acelerar(self, acelerado):
        if self.desligado:
            print(f'{self.modelo} não pode acelerar, pois está desligado.')
            return
        acelerou = self.aceleracao + acelerado
        if acelerou == 0:
            print(f'{self.modelo} o carro está parado.')
            return
        print(f'{self.modelo} acelerou {acelerou} km/h.')
        
c1 = Carro('Fusca', 2000, 'azul', 'gasolina', 1500, 15)

c1.ligar()
c1.consumir_combustivel(10)
c1.acelerar(10)
       
        
            