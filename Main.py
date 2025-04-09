from TratarDados import TratarDadosAPI

def main():
    filtros = {"name": "Rick"} 
    tratador = TratarDadosAPI()  
    dados_personagens = tratador.buscar_dados('character', filtros)

    if dados_personagens:
        print("Dados obtidos e salvos no arquivo .json")
    else:
        print("Não foi possível obter os dados.")

if __name__ == '__main__':
    main()