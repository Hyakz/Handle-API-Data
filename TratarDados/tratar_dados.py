import json
import requests

class TratarDadosAPI:
    def fazer_requisicao(self, endpoint, parametros={}):
        url = f'https://rickandmortyapi.com/api/{endpoint}'
        resposta = requests.get(url, params=parametros)
        
        if resposta.status_code == 200:
            return resposta.json()
        else:
            raise Exception(f"Erro ao consultar dados na API: {resposta.status_code}")

    def salvar_dados(self, nome_arquivo, dados):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def buscar_dados(self, endpoint, filtros={}):
        nomes_personagens = []
        pagina = 1
        
        while True:
            filtros['page'] = pagina
            try:
                dados = self.fazer_requisicao(endpoint, filtros)
                nomes_personagens.extend([personagem['name'] for personagem in dados['results']])
                
                if not dados['info']['next']:
                    break
                
                pagina += 1
            except Exception as e:
                print(str(e))
                break
        
        self.salvar_dados('data/.json', nomes_personagens) 
        return nomes_personagens
