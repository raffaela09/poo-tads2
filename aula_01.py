#em todas as linguagens de programacao, linguagens para desenvolvimento web, quanto mais puder aprender, melhor
#convencao de criacao de classes, em py n faz mt diferenca
#comeca a palavra com a letra maiuscula, primeiro conceito,
#construtor define os atributos da classe, o construtor é o primeiro metodo a ser chamado da classe, ele tambem reserva espaco na memoria, e retorna a referencia dele
#nao é permitido criar objetos sem valores nenhum, pra esse tipo de situacao
#podemos passar parametros para o inicializador
class Pessoa:
    def __init__(self, name, idade): #construtor, palavra self, nao precisa exatamente se chamar self, pq ela faz uma referencia aos proprios atributos da propria classe, metodo init nao pode ser criado sem a palavra self
        self.name = name
        self.idade = idade
        #metodo
    # def print(self):
    #     print(f'Nome: {self.name}, Idade: {self.idade}')
        #necessario imprimir pessoa1.print
        #outra opcao
        #utilizar o str
        #sobrecarga do metodo str
    def __str__(self): #esse metodo por padrao, imprime o nome estranho
        
        return f'Nome: {self.name}, Idade: {self.idade}'
    #sem os parenteses, pq pode ser uma tupla
        
class Aluno:
    def __init__(self, name, curso, turma, matricula):#primeiro parametro, sempre o self
        self.name = name
        self.curso = curso
        self.turma = turma
        self.matricula = matricula
        
    def __str__(self):
        return f'Nome: {self.name}, Curso: {self.curso}, Turma: {self.turma}, Matricula: {self.matricula}'
    #o metodo str ira sobrescrever
          
#metodo pra teste     
if __name__ == '__main__':
    #Crias uma instancia de pessoa
     pessoa1 = Pessoa('Rafa', 20) #chamando o construtor dessa classe - objeto, pessoa é uma instancia de pessoa, os parenteses indica que é um constructor
    #  pessoa1.name = 'Rafa'#cuidado com o nome do atributo, precisa ser igual  
    #  pessoa1.idade = 20 #mas isso é uma má pratica
     
     #objeto aluno
     rafaela = Aluno('rafa', 'tads', 'b', 1234) #proibe que vc crie instancia de valores, e obriga que os valores sejam colocados na criacao do objeto, objeto com parametros inicializados
    #  rafaela.name = 'Rafa'
    #  rafaela.curso = 'TADS'
    #  rafaela.turma = 'b'
    #  rafaela.matricula = 1234
    #  codigo mais legivel
     
    #pode utilizar o metodo de sobrescrita ou o print
    #só nao pode fazer isso, se for utilizar a posicao do objeto
    #  print(f'Nome: {pessoa1.name}, Idade: {pessoa1.idade}')
    #  print(f'Nome: {rafaela.name}, Curso: {rafaela.curso}, Turma: {rafaela.turma}, Matricula: {rafaela.matricula}')
     #codigo que sai é uma referencia do hexadecimal da memoria, isso é sempre ruim? nao
     #formas de contornar
     #melhora mas acaba saindo como vazio
     print(pessoa1)
     print(rafaela)
     
     # 
     

        
