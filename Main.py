from TratarDados import TratarDadosAPI

def main():
    tratador = TratarDadosAPI()  
    filtros  = {'name': 'Rick'}

    dados_personagens = tratador.buscar_dados('character', filtros)

    if dados_personagens:
        print("Nomes obtidos e salvos no arquivo .json")
    else:
        print("Não foi possível obter os dados.")

if __name__ == '__main__':
    main()