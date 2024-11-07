import re
from collections import Counter, defaultdict
import unittest

class UtilitariosAnaliseTexto:
    def __init__(self, texto):
        self.texto = texto

    def frequencia_caracteres(self):
        """Conta a frequência de cada caractere no texto, sem pontuações e sem acentos."""
        texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', self.texto.lower())
        return dict(Counter(texto_limpo))

    def palavras_unicas_ordenadas(self):
        """Retorna uma lista de palavras únicas em ordem alfabética, ignorando maiúsculas/minúsculas."""
        palavras = set(self.texto.lower().split())
        return sorted(palavras)

    def eh_anagrama(self, palavra1, palavra2):
        """Verifica se duas palavras são anagramas entre si, ignorando maiúsculas/minúsculas."""
        return sorted(palavra1.lower()) == sorted(palavra2.lower())

    def palavra_mais_longa(self):
        """Encontra a palavra mais longa no texto."""
        palavras = re.findall(r'\b\w+\b', self.texto)
        palavras_max = [p for p in palavras if len(p) == len(max(palavras, key=len))]
        return palavras_max

    def contar_frases(self):
        """Conta o número de frases no texto, considerando pontos, exclamações e interrogações."""
        frases = re.split(r'[.!?]+', self.texto)
        return len([frase for frase in frases if frase.strip()])

    def frequencia_palavras(self):
        """Conta a frequência de cada palavra no texto, desconsiderando pontuações."""
        palavras = re.findall(r'\b\w+\b', self.texto.lower())
        return dict(Counter(palavras))

    def detectar_palavras_chave(self, palavras_comuns=None):
        """Detecta palavras-chave no texto, ignorando palavras comuns fornecidas na lista palavras_comuns."""
        if palavras_comuns is None:
            palavras_comuns = {"de", "a", "o", "e", "do", "da"}
        palavras = [palavra.lower() for palavra in re.findall(r'\b\w+\b', self.texto) if
                    palavra.lower() not in palavras_comuns]
        return dict(Counter(palavras))

    def grupos_anagramas(self, lista_palavras):
        """Agrupa palavras que são anagramas entre si."""
        anagramas = defaultdict(list)
        for palavra in lista_palavras:
            chave = tuple(sorted(palavra.lower()))
            anagramas[chave].append(palavra)
        return [grupo for grupo in anagramas.values()]

# Testes com unittest
class TestUtilitariosAnaliseTexto(unittest.TestCase):
    def setUp(self):
        self.util = UtilitariosAnaliseTexto("Texto de exemplo para testes, com diversas palavras e frases.")

    def test_frequencia_caracteres(self):
        resultado = self.util.frequencia_caracteres()
        self.assertIsInstance(resultado, dict)

        if self.util.texto:
            self.assertTrue(any(resultado.values()))

    def test_palavras_unicas_ordenadas(self):
        resultado = self.util.palavras_unicas_ordenadas()
        self.assertIsInstance(resultado, list)
        self.assertTrue(all(isinstance(palavra, str) for palavra in resultado))

    def test_eh_anagrama(self):
        self.assertTrue(self.util.eh_anagrama("amor", "roma"))
        self.assertFalse(self.util.eh_anagrama("teste", "palavra"))

    def test_palavra_mais_longa(self):
        resultado = self.util.palavra_mais_longa()
        
        self.assertIsInstance(resultado, list)
        
        self.assertGreater(len(resultado), 0)
        
        for palavra in resultado:
            self.assertIsInstance(palavra, str)
        
        if self.util.texto:
            max_len = len(max(self.util.texto.split(), key=len))
            for palavra in resultado:
                self.assertEqual(len(palavra), max_len)

    def test_contar_frases(self):
        resultado = self.util.contar_frases()
        self.assertIsInstance(resultado, int)
        if self.util.texto:
            self.assertGreaterEqual(resultado, 1)

    def test_frequencia_palavras(self):
        resultado = self.util.frequencia_palavras()
        self.assertIsInstance(resultado, dict)
        if self.util.texto:
            self.assertTrue(any(resultado.values()))

    def test_detectar_palavras_chave(self):
        resultado = self.util.detectar_palavras_chave()
        self.assertIsInstance(resultado, dict)
        if self.util.texto:
            self.assertTrue(all(palavra not in {"de", "a", "o", "e", "do", "da"} for palavra in resultado.keys()))

    def test_grupos_anagramas(self):
        lista_palavras = ["amor", "roma", "mar", "ramo"]
        resultado = self.util.grupos_anagramas(lista_palavras)
        self.assertIsInstance(resultado, list)
        self.assertTrue(all(isinstance(grupo, list) for grupo in resultado))

if __name__ == "__main__":
    unittest.main()
