# Conversor de Moedas

![Vercel](https://vercelbadge.vercel.app/api/ppnunes/projetofinal2-match)

Projeto voltado para Programa Match! projeto final 2.

O projeto está disponível em https://projeto-final2.vercel.app/

## Requisitos pedidos:

Neste projeto, os alunos criarão um conversor de moedas em Python. A aplicação incluirá
as seguintes etapas:

#### Entrada de Dados:
 - Os usuários fornecerão o valor a ser convertido e as moedas de origem e
destino.
#### Validação de Dados:
-  A aplicação verificará se as moedas inseridas são válidas de acordo com uma
lista predefinida.
#### Conversão de Moedas:
- A aplicação buscará as taxas de câmbio atualizadas da internet e realizará a
conversão.
#### Exibição dos Resultados:
- A aplicação exibirá o valor convertido na moeda de destino.

## Preparação de Ambiente

As dependencias estão listadas no arquivo [requirements.txt](requirements.txt)  e podem ser instaladas com:

```bash
pip install -r requirements.txt
```

Recomenda-se o uso de ambientes virtuals ([venv](https://docs.python.org/pt-br/3/library/venv.html), [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)) para a proteção do sistema.

## Execução da aplicação

### CLI

Essa aplicação apresenta um grupo de comandos disponíveis que podem ser executados diretamento do terminal. Todas as entradas de moedas podem ser feitas em caixa alta ou baixa.


##### *Lista de Moedas disponíveis*

```bash
python conversor.py all_codes
```
Retorna uma lista de moedas disponíveis

##### *Verificação de disponibilidade de moeda*

```bash
python conversor.py is_available <MOEDA>
```
Retorna `True` se tiver suporte a moeda ou `False` caso contrário

##### *Lista de disponibilidade de conversão direta*

```bash
python conversor.py all_conversions <MOEDA>
```
Lista todas as conversões **diretas** disponíveis. 

##### *Taxa*

```bash
python conversor.py get_rate <MOEDA ORIGEM> <MOEDA DESTINO>
```
Retorna a taxa de cambio de converção da `<MOEDA ORIGEM>` para `<MOEDA DESTINO>`.

##### *Conversão*

```bash
python conversor.py convert <MOEDA ORIGEM> <MOEDA DESTINO> <VALOR> [--use_usd,-u]
```
Retorna o valor convertido da `<MOEDA ORIGEM>` para `<MOEDA DESTINO>`. Caso a conversão direta não esteja disponível, será apresentado um erro apontando a indisponibilidade direta e oferecendo o uso da flag `--use_usd`. Ao usar essa flag, será usada a taxa de conversão em dolar como intermediário para conseguir a taxa completa da conversão.

### WEB

Foi utiliazada a biblioteca Flask como web framework. Instaladas as dependências, é possível executar o servidor com:

```bash
flask run
```

Ou com:

```bash
python app.py
```

Depois, para ver o conteúdo, basta acessar o endereço http://127.0.0.1:5000