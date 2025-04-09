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
        personagens_detalhes = []
        pagina = 1
        
        while True:
            filtros['page'] = pagina  
            try:
                dados = self.fazer_requisicao(endpoint, filtros)
                
                for personagem in dados['results']:
                    detalhes = {}
                    for chave in filtros.keys():  
                        if chave in personagem:
                            detalhes[chave] = personagem[chave]
                        else:
                            detalhes[chave] = 'Desconhecido'
                    personagens_detalhes.append(detalhes)
                
                if not dados['info']['next']:
                    break
                
                pagina += 1  

            except Exception as e:
                print(str(e))
                break
        
        for personagem in personagens_detalhes:
            personagem.pop('page', None)

        self.salvar_dados('Data/.json', personagens_detalhes)  
        return personagens_detalhes