

class Programa:
    def __init__(self, nome, ano, likes=0) -> None:
        self.__nome = nome
        self.__ano = ano
        self.__likes = likes
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, likes):
        self.__likes = likes
    
    def like(self):
        self.likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duraçao, likes=0) -> None:
       super().__init__(nome, ano, likes) 
       self.__duraçao = duraçao
       
    @property
    def duraçao(self):
        return self.__duraçao

    @duraçao.setter 
    def duraçao(self, duraçao):
        self.__duraçao = duraçao 
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas, likes=0) -> None:
       super().__init__(nome, ano, likes) 
       self.__temporadas = temporadas
       
    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter 
    def temporadas(self, temporadas):
        self.__temporadas = temporadas 