class Disciplinas:
  
    def __init__(self, nome):
        self.nome = nome
        self.avaliacoes = []
        
    if opcao == 1:

        def registrar_avaliacoes(self, tipo, dia, peso=1,  entregue=False, nota=0):
            nova = Avaliacao(tipo, dia, float(peso), entregue, float(nota))
            self.avaliacoes.append(nova)
            for avaliacao in self.avaliacoes:
                if avaliacao.dia == dia:
                    return False
            self.avaliacoes.append(nova)
                return True

    if opcao == 2:

        def calcular_media(self):
            media = 0.0
            peso_total = 0.0
            for avaliacao in self.avaliacoes:
                peso_total += avaliacao.peso
            for avaliacao in self.avaliacoes:
                media += (avaliacao.nota*(avaliacao.peso/peso_total))
            return media
        
    if opcao == 3:

        def registrar_nota(self, dia, nota):
            for avaliacao in self.avaliacoes:
                if avaliacao.dia == dia:
                    avaliacao.nota = nota

    if opcao == 4:

        def registrar_entrega(self, dia):
            for avaliacao in self.avaliacoes:
                if avaliacao.dia == dia:
                    avaliacao.entregue = True

class Avaliacao:
  
  def __init__(self, tipo, dia, peso, entregue, nota):
    self.tipo = tipo
    self.nota = nota
    self.dia = dia
    self.entregue = entregue
    self.peso = peso

if __name__ == "__main__":
    prog1 = Disciplinas("Programação I")
    prog1.registrar_avaliacoes("escrita", "27/08/2019", 1,  False, 8)
    prog1.registrar_avaliacoes("escrita", "27/08/2019", 2,  False, 4)
    print(prog1.calcular_media())

    print("Opções de funções")
    print("1- Registrar avaliações")
    print("2- Calcular média")
    print("3- Registrar nota")
    print("4- Registrar entrega")

    opcao = int(input("Insira a opção: "))

    if opcao == 1:

        tipo = input("Entre com o tipo da avaliação: ") 
        dia = float(input("Entre com a data da avaliação"))
        registro = registrar_avaliacoes(self, tipo, dia, peso=1,  entregue=False, nota=0)
        print(registro)


    if opcao == 2 :

        media = calcular_media(self)
        print(media)

    if opcao == 3: 

        dia = input("Entre com o dia da avaliação: ")
        nota = float(input("Entre com a nota da avaliação: "))
        nota = registrar_nota(self, dia, nota)
        print(nota)


    if opcao == 4: 

        dia = input("Entrega com a data de entrega da avaliação: ")
        entrega = registrar_entrega(self, dia)
        print(entrega)
