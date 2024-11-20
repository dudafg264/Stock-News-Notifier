# Tesla Stock and News Email Notifier

Este projeto recupera dados sobre as ações da Tesla (TSLA) e as últimas notícias sobre a empresa, e envia um e-mail com essas informações. Ele foi projetado para automatizar o processo de acompanhamento da variação das ações e as notícias relacionadas à Tesla, oferecendo um alerta diário por e-mail.

## Funcionalidades

- **Recupera dados sobre as ações da Tesla** a partir da API da Alpha Vantage.
- **Calcula a variação percentual** entre o fechamento das ações de ontem e do dia anterior, destacando se houve uma variação significativa.
- **Obtém as últimas 3 notícias** sobre a Tesla a partir da API do NewsAPI, filtrando por títulos e fornecendo links para mais informações.
- **Envia um e-mail diário** com as informações sobre a variação das ações e as notícias mais relevantes.
- Possui um **tratamento de erros** que lida com a falta de dados ou problemas com a API, garantindo que o script continue funcionando sem falhas.

## Requisitos

Antes de rodar o projeto, você precisa instalar o Python 3.x e as bibliotecas necessárias:

- **Python 3.x** (recomendado Python 3.6 ou superior)
- **Bibliotecas Python**:
    - `requests` – Para fazer requisições HTTP e obter dados das APIs.
    - `smtplib` – Para enviar e-mails via SMTP.
    - `os` – Para lidar com variáveis de ambiente.
    - `datetime` e `timedelta` – Para manipulação e formatação de datas.

Você pode instalar as dependências do projeto com o seguinte comando:

```bash
pip install requests
```

## Configuração

1. **Clone este repositório**:
    ```bash
    git clone https://github.com/seu-usuario/tesla-stock-notifier.git
    ```
    
2. **Instale as dependências**:
    Execute o comando abaixo para instalar a biblioteca `requests` e outras dependências:
    ```bash
    pip install requests
    ```

3. **Configuração das variáveis de ambiente**:
    O script requer algumas variáveis de ambiente para funcionar corretamente. Você pode armazená-las em um arquivo `.env` ou configurá-las diretamente no seu sistema. Aqui estão as variáveis necessárias:

    - **API_KEY_STOCKS**: Sua chave de API da Alpha Vantage para acessar os dados das ações.
    - **API_KEY_NEWS**: Sua chave de API do NewsAPI para acessar as notícias.
    - **MY_EMAIL**: O seu endereço de e-mail (utilizado para o envio do e-mail).
    - **PASSWORD**: A senha do seu e-mail (caso utilize Gmail, você pode precisar gerar uma senha de aplicativo).

    **Exemplo de arquivo `.env`**:
    ```bash
    API_KEY_STOCKS=your_alpha_vantage_api_key
    API_KEY_NEWS=your_news_api_key
    MY_EMAIL=your_email@example.com
    PASSWORD=your_email_password
    ```

4. **Configurando o SMTP**:
    O código usa o servidor SMTP do Gmail (`smtp.gmail.com`) para enviar o e-mail. Se você usar outro provedor de e-mail, será necessário ajustar o código para corresponder às configurações do seu provedor.

    - Caso utilize **Gmail**, você pode precisar **habilitar o acesso a apps menos seguros** ou gerar uma **senha de aplicativo** se estiver usando autenticação de dois fatores.

    **Informações importantes**:
    - Certifique-se de ter configurado corretamente as variáveis de ambiente para garantir que o script consiga acessar as chaves de API e os detalhes do e-mail.