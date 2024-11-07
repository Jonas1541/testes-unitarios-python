from collections import Counter, defaultdict


class UtilitariosAnaliseTexto:
    def frequencia_caracteres(self):
        pass

    def palavras_unicas_ordenadas(self):
        """Retorna uma lista de palavras únicas em ordem alfabética, ignorando maiúsculas/minúsculas."""
        palavras = set(self.texto.lower().split())
        return sorted(palavras)

    def eh_anagrama(self, palavra1, palavra2):
        """Verifica se duas palavras são anagramas entre si, ignorando maiúsculas/minúsculas."""
        return sorted(palavra1.lower()) == sorted(palavra2.lower())

    def palavra_mais_longa(self):
        pass

    def contar_frases(self):
        """Conta o número de frases no texto, considerando pontos, exclamações e interrogações."""
        frases = re.split(r'[.!?]+', self.texto)
        return len([frase for frase in frases if frase.strip()])

    def frequencia_palavras(self):
        pass

    def detectar_palavras_chave(self, palavras_comuns=None):
        """Detecta palavras-chave no texto, ignorando palavras comuns fornecidas na lista palavras_comuns."""
        if palavras_comuns is None:
            palavras_comuns = {"de", "a", "o", "e", "do", "da"}
        palavras = [palavra.lower() for palavra in re.findall(r'\b\w+\b', self.texto) if
                    palavra.lower() not in palavras_comuns]
        return dict(Counter(palavras))

    def grupos_anagramas(self, lista_palavras):
        pass
