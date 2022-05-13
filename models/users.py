

class Telespectador:
    def __init__(self, nome, email) -> None:
        self.username = nome
        self.email = email

    def assistir_programa(self, programa):
        print(f"assistindo programa {programa.nome}") 
        return 0


class Produtor:
    def adicionar_programa(self, programa, playlist):
        playlist.adicionar(programa)
        return 0

 
class Administrador(Telespectador, Produtor):
    def remover_programa(self, programa, playlist):
        playlist.remover(programa)
        return 0
    