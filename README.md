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

### Capítulo 5 - Banco de Dados
Trata sobre como utilizar banco de dados e escolher com quais ferramentas manusea-los. Observando diversos pontos, a escolha ficou pelo **Flask Sql-Alchemy** e para conectar com um banco de dados mysql utiliza o seguinte padrão:
`mysql://username:password@hostname/database`  
No Sql_alchemy existem _session_'s que são as transactions do SQL, ou seja, elas precisam de commit para serem finalizadas e possuem roolback para voltar atrás.  

Para poder trabalhar com novas tabelas, o flask trabalha destruindo a existente e construindo uma nova, para evitar perdas de dados é necessário usar instâncias de migração, utilizaremos o `flask-migrate`. Ele cria automaticamente a migração, porém é necessário sempre conferir pois em casos que o nome da coluna seja atualizado ele não entenda a atualização e simq ue foi criada uma nova coluna por exemplo.  
Utilizamos os seguintes comandos para migração: 
1. `flask db init`
2. `flask db -m "MENSAGEM"`
3. Revisa as modificações
4. `flask db upgrade` ou `flask db downgrade`(Remove última migração) 

Caso já existe o banco de dados, assinale ele como atual usando `flask db stamp`.

---

### Capítulo 6 - Email
Trata de como trabalhar com e-mail no flask utilizando o `flask-mail`.  
Além de trabalhar o envio do e-mail, focou-se em como evitar atrasos no envio, rodando o e-mail em segundo plano por uma **thread**. Esse "atraso" gerado pelo flask é devido ele rodar em um contexto, sempre no current_app.  

---

### Capítulo 7 - Estrutura da Aplicação
Conforme a aplicação cresça, sua estrutura em um único arquivo se torna inviável, então a transformação dessa estrutura em uma padrão será ensinada nesse capítulo.  
Um grande desafio na separação do código é como separar as rotas, para solucionar esse desafio o flask possui uma solução chamada **Blueprint** que nela você consegue armazenar handle de erros e rotas da aplicação, é necessário defini-lo em seu arquivo main e na própria pasta main.  
Observação: o uso de `app_errohandler` ao invés de `errohandler` torna o erro capturado globalmente, enquando _errohandler_ seria chamado apenas em rotas definidas pelo blueprint.  
Informação importante é a construção do arquivo **config.py** que define em qual ambiente está rodando a aplicação.

---

### Capítulo 8 - Autenticação do Usuário
O segredo das autenticações são as senhas que são guardadas com hash. Para se utilizar geralmente opta-se por bibliotecas, pois implementar manualmente é muito complexo e a criticidade de manter seguro é muito importante.  

Para criação do Hash utilizaremos o **Werkzeug**.
Para guardar o estado da autenticação utilizaremos **flask-login**. Ela é iniciada junto ao aplicativo e acessa o banco de dados para obter o id do usuário. E para evitar acessos de usuário sem login se utiliza `@login_required` na rota.  

O flask-login guarda dados de login no cook, se quiser alterar o tempo default de 1 ano, só passar item opcional de `REMEMBER_COOKIE_DURATION` no __login_user__.  

É bom se criar um token para confirmação do e-mail, para isso utiliza-se a biblioteca `itsdangerous`.  

Além da criação do token temos que poder usa-lo no nosso programa, por isso criamos uma confirmação, tal confirmação é enviada por e-mail com um link com o token (tal token é o argumento de uma nova rota), que torna o usuário como confirmado no banco de dados.