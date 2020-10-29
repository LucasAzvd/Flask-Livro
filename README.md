# Flasky Project

Código desenvolvido sobre orientações do livro Desenvolvimento Web com Flask.

## Capítulos:
### Capítulo 1
Trata de como instalar o ambiente virtual e a biblioteca.  
---
### Capítulo 2
Trata da estrutura da aplicação.  
Uma maneira interessante de saber como estão estruturados os endpoints é importando o app de outro arquivo e observando o seu mapa de url:  
```py
from aplicacao import app
app.url_map
# Vizualiza todos os endpoints e suas regras
```  
Nos informa também dos _hooks_ do flask que podem ser `before_request`, `before_first_request`, `after_request` e `teardown_request`.
---
### Capítulo 3
Tratou do uso de templates, o Flask possui templates muito utilizados para desenvolvimento web como `flask_bootstrap` para montagem da aparência das páginas e `flask_moment` para tratamento de datas.  
Também tratou da extensão de página com `{% extends "SEU_HTML.html"}` o que facilita o carregamento das páginas e montagem de um layout padrão. E de loops no próprio HTML, com exemplos temos o arquivo `anotacoes_extras.html`.  
Temos o tratamento de erros de requisição, nesse código tratamos de 2:
1. Erro 404 - erro de página não encontrada   
2. Erro 500 - erro do servidor interno   

Ambos os erros utilizam a tratativa `@app.errorhandler(STATUS)`, então ao encontrar uma requisição com esse estado o Flask retorna uma resposta.   
É válido lembrar também que para url's dinâmicas o flask utilizada do comando `{url_for('PASTA', 'ARQUIVO')}` evitando erros.  
Outro ponto importante é está ciente que para expansão de templates padrões do Jinja2 devemos usar o método super `{{ super() }}` após a alteração (Exemplos de blocos padrões temos blocos de estilos e scripts (Styles, Scripts)).
---
### Capítulo 4 - Formulários
Tratou do `Flask WTF` que é uma biblioteca para administrar formulários do flask, único pré-requisito é ter uma **Secret Key** para ter mais segurança na aplicação. Ele funciona criando TOKENS para todos os formulários, previnindo ataques CSRF(Cross-Site Request Forgery).  
Para implementar tal proteção, antes dos formulários deve-se colocar `{{ form.hidden_tag() }}`, essa tag oculta garante a proteção contra CSRF.    
  
A classe **FlaskForm** é mãe das demais classes de formulários e ela define validações e os campos dos forms.  
  
O padrão **Post/Redirect/Get** é um padrão onde após a requisição POST é realizado uma requisição GET para evitar que o navegador gere algum problema. Para não se perder essa variável, o flask utiliza de sessions que dados salvos no próprio navegar (cookies) e criptografados pela chave secreta. 
  
Além de trabalhar forms, falou-se do _flash_ que são mensagens de alerta que você pode enviar com o flask, para elas você em geral as deixa no template base para está em todas as páginas e para enviar basta utilizar:
```py
flash("SUA MENSAGEM")
```
```html
<!-- E no HTML inserir -->
{% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
    </div>
{% endfor %}
```
---
#### Capítulo 5 - Banco de Dados
Trata sobre como utilizar banco de dados e escolher com quais ferramentas manusea-los. Observando diversos pontos, a escolha ficou pelo **Flask Sql-Alchemy** e para conectar com um banco de dados mysql utiliza o seguinte padrão:
`mysql://username:password@hostname/database`