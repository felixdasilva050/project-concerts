## Introdução 
Bem-vindo à documentação do projeto de nosso Bot de Pesquisa de Eventos no Google. Este projeto representa um esforço dedicado à automação e simplificação do processo de busca e obtenção de informações sobre eventos, por meio da plataforma Google. Nosso bot, é projetado para simplificar a vida de usuários, oferecendo uma maneira rápida e eficiente de descobrir eventos relevantes em sua região.

À medida que a tecnologia continua a moldar nossa maneira de interagir com o mundo, os assistentes virtuais e bots desempenham um papel cada vez mais importante em nossas vidas diárias. Nosso Bot de Pesquisa de Eventos no Google é uma resposta inovadora a essa tendência, permitindo que os usuários obtenham informações atualizadas sobre eventos, datas e locais.

Neste documento, forneceremos uma visão abrangente do projeto, incluindo sua finalidade, funcionalidades, arquitetura, requisitos e instruções de uso. Você aprenderá como nosso bot foi desenvolvido, como ele funciona e como pode ser integrado às suas aplicações ou usos pessoais.
Os dados estão sendo obtidos pelo site do Recife ingresso. Vale salientar que esse projeto tem cunho completamente acadêmico.

## Requisitos é necessário 
- ter o python 3.12.0 instalado na sua máquina
- instalar as seguintes bibliotecas 
- - flask 
    ```
    pip install flask
    ```
- - bibliotecas Google 
    ```
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```
- - request
    ```
    pip install requests
    ```

## Dica

recomendamos que utilize algum gerenciador de ambiente virtual como o [conda](https://docs.conda.io/en/latest/) para melhor organização. **Isso não é um requisito**

## Como rodar rodar programa

Após as instalar as bibliotecas necessárias basta abrir a pasta app no seu prompt de comando e digitar

```
python app.py
```
caso não funcione, verifique sua versão do python.

## Linguagem usada:

- **Python**

## Ferramentas do Google:

- **Google Sheets**
- **Google Drive**
- **Google Firebase como SGDB**


## Endpoints
|Tipo requisição | Descrição | exemplo params |
| --- | --- | --- |
|`GET /eventos` | Recupera todos os eventos. | === |
|`GET /eventos/<id>` | Recupera um evento específico por ID. | eventos/-NiLBgEcmNyfiExe1CQy
|`GET /eventos/date/<date>` | Recupera eventos por data específica. |eventos/date/15-02 <br> ou eventos/date/02 |
|`GET /eventos/location/<location>` | Recupera eventos por localização.| eventos/location/Recife |
|`GET /reloadDataBase/<password>` | Recarrega e atualiza a base de dados de eventos. Necessita de uma senha para isso | Senha no script|

## Descrições de função
A descrição das funcionalidades estão contidas em bloco de comentários logo acima das funções indicando tipo do parâmetro esperado, tipo de retorno e o que executa.

## Mais informações
Para mais informações ou solicitações referente a API e/ou Bot você pode entrar em contato direto pelo e-mail: guilhermefelix.ofwork@gmail.com ou fhenriquev1842@gmail.com