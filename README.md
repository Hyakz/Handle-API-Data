# Projeto Tratar Dados API - Rick and Morty

Este projeto foi desenvolvido com o objetivo de **aprender a tratar dados de APIs**. Ele faz requisições à API pública do **Rick and Morty** para extrair os nomes dos personagens com base em filtros especificados. Os dados são então salvos em um arquivo `.json` para posterior análise ou uso.

## Funcionalidades

- **Busca de dados**: Permite buscar informações sobre os personagens da série Rick and Morty com base em filtros como nome.
- **Paginação**: O código lida com a paginação da API, garantindo que todos os dados sejam coletados, mesmo que estejam distribuídos em várias páginas.
- **Salvar dados**: Os nomes dos personagens encontrados são salvos em um arquivo `.json` para facilitar o acesso posterior.

## Objetivo

Este projeto tem como principal objetivo **ensinar e praticar o tratamento de dados obtidos de APIs**. O código aborda conceitos como requisição HTTP, tratamento de erros, paginação e armazenamento dos dados em um arquivo JSON.

## Estrutura do Projeto

<img align="right" src="https://cdn.discordapp.com/attachments/1352494396163096637/1359643764095975464/Design_sem_nome.png?ex=67f83a6e&is=67f6e8ee&hm=2025be0c6624f6225c764d6e609991cc973b548eab2196c69b8845f83db8f725&" width="190" height="190">

```
├── Data/
│   └── .json
│
├── TratarDados/
│   ├── tratar_dados.py
│
├── Main.py
└── README.md
```
