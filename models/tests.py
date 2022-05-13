import unittest
from unittest.mock import Mock
from models.playlist import Playlist
from models.programas import Serie, Filme
from models.users import Telespectador, Administrador, Produtor


class TestPlaylist(unittest.TestCase):
    def setUp(self) -> None:
        programa_a = Mock()
        programa_b = Mock()
        self.playlist = Playlist("MyPlaylist", [programa_a, programa_b]) 
    
    def testPlaylist(self):
        self.assertEqual(len(self.playlist), 2)
        programa_c = Mock()
        self.playlist.adicionar(programa_c)
        self.assertEqual(len(self.playlist), 3)
        self.playlist.remover(programa_c)
        self.assertEqual(len(self.playlist), 2)


class TestPrograma(unittest.TestCase):
    def setUp(self) -> None:
        self.serie = Serie("Serie A", 1998, 4)
        self.filme = Filme("Filme A", 2001, 144)

    def testSerie(self):
       self.serie.ano = 1997 
       self.serie.likes = 14
       self.serie.nome = "Serie A atualizado"
       self.serie.temporadas = 5
       self.serie.like()

       self.assertEqual(self.serie.ano, 1997)
       self.assertEqual(self.serie.likes, 15)
       self.assertEqual(self.serie.nome, "Serie A atualizado")
       self.assertEqual(self.serie.temporadas, 5)


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.telespectador = Telespectador("JoaoNormal", "thisisatest")
        self.produtor = Produtor()
        self.administrador = Administrador("JoaoAdm", "thisisatest")

    def testAssistirFilme(self):
        filme = Mock()
        filme.nome = "FilmeMock"
        
        self.assertEqual(self.telespectador.assistir_programa(filme), 0)
        self.assertEqual(self.administrador.assistir_programa(filme), 0)
        