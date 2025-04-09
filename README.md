# Projeto Tratar Dados API - Rick and Morty

Este projeto foi desenvolvido com o objetivo de **aprender a tratar dados de APIs**. Ele faz requisições à API pública do **Rick and Morty** para extrair os nomes dos personagens com base em filtros especificados. Os dados são então salvos em um arquivo `.json` para posterior análise ou uso.

## Funcionalidades

- **Busca de dados**: Permite buscar informações sobre os personagens da série Rick and Morty com base em filtros como nome.
- **Paginação**: O código lida com a paginação da API, garantindo que todos os dados sejam coletados, mesmo que estejam distribuídos em várias páginas.
- **Salvar dados**: Os nomes dos personagens encontrados são salvos em um arquivo `.json` para facilitar o acesso posterior.

## Objetivo

Este projeto tem como principal objetivo **ensinar e praticar o tratamento de dados obtidos de APIs**. O código aborda conceitos como requisição HTTP, tratamento de erros, paginação e armazenamento dos dados em um arquivo JSON.

## Estrutura do Projeto

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
