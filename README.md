# AceleradoraAgil_AgilStore
Programa da segunda etapa do processo seletivo.


O código em questão se trata de uma solução para o exercício: Gerenciamento de Produtos para a Loja AgilStore.
Para executá-lo você irá precisar de ter python 3.13 instalado no seu computador. Baixe o arquivo com extensão '.py' e abra o mesmo utilizando Python.

Caso não tenha Python instalado poderá baixar no seguinte link: https://www.python.org/downloads/release/python-3130/
O link de download se encontra no final da página mencionada.

Tenho mais experiência em programação em C, e um pouco de Python, por isso fiz o exercício dessa forma.

Feito em python, o programa é simples de utilizar e lê as entradas do usuário de forma rápida, permitindo-o facilmente identificar as opções que deseja e seleciona-las via números. Fora dos menus o programa irá pedir ao usuário informações que podem ser palavras ou apenas um Enter para seguir.

O código foi feito muito com a experiência do usuário em mente, garantindo que o mesmo sempre consiga digerir o feedback do código antes de preencher a tela com informações. Em diversos pontos o programa permite o usuário voltar ao menu anterior, dando o máximo de fluidez na experiência do usuário, procurando dar a sensação de controle sobre o programa para que o mesmo se sinta confortável.

Muito do código utiliza Match/Case para pois maior parte do código se trata de menus onde o usuário entra nas opções desejadas. 
A segunda parte mais importante do código é a validação de informações inseridas pelo usuário, como várias informações são específicas, exemplos: números não podem receber caracteres, menus tem limites de opções e nomes de produtos não podem ser repetidos. Por causa disso o código utiliza muitos testes de If/Else e loops While para repetir os inputs até que algo válido seja enviado.

Para que o código seja mais legível eu criei algumas funções para tarefas que seriam utilizadas diversas vezes dentro do código com mínimas alterações, dessa forma o corpo principal fica menos poluído.

