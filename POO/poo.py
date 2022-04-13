class Cachorro:
        def __init__(self, nome, cor_de_pelo, idade, tamanho):
            self.cor_de_pelo = cor_de_pelo
            self.nome = nome
            self.idade = idade
            self.tamanho = tamanho
        def latir(self):
            print("Au Au!!!")
        def correr(self):
            print(f"{self.nome} esta correndo!!!")


cachorro1 = Cachorro("Pandora", "Escuro", 10, "Grande")
cachorro2 = Cachorro("Dogman", "Preto", 115, "Gigante")

#print(cachorro1.idade)
print(cachorro1.nome)
cachorro1.latir()
cachorro1.correr()
print(cachorro2.nome)
cachorro2.correr()