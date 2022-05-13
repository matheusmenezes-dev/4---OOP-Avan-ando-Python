class Playlist:
    def __init__(self, nome:str, programas:list) -> None:
        self.nome = nome
        self.__programas = programas
    
    def __iter__(self):
        return self.__programas.__iter__()
    
    def __len__(self):
        return len(self.__programas)
    
    def adicionar(self, programa):
        self.__programas.append(programa)

    def remover(self, programa):
        self.__programas.remove(programa)