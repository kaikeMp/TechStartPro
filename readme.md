INSTRUÇÕES

Esse sistema é preferencialmente para rodar no sistema linux.

Antes de rodar o programa é necessário instalar o requirement_.txt com o comando no shell/cmd/PowerShell(windows, linux ou MacOs):

pip install -r requirement_.txt

Quando o programa abrir é necessário importar uma lista de categorias, que pode ser feita com o botão "Import", como o programa não faz refresh/update, é necessário fechar a tela e rodar o programa novamente. 
OBS: É necessário ter uma lista com categorias no formato csv, com uma categoria por linha.

Ao reabrir o programa já haverá uma lista de categorias que poderá ser usada para criar um novo produto para o data base. 

Não é necessário atribuir uma id para o produto cadastrado, o mesmo será feito automaticamente pelo programa. 

Ao clicar no botão search, com alguma informação, se essa informação for encontrada em algum produto, este será mostrado.
Ao clicar no botão "search" com o campo "search by" vazio, todos os produtos serão mostrados novamente.

Para limpar a tabela com os dados dos produtos, basta clicar no botão "read" com o campo product id vazio

Após a adição de produtos à lista, é possível, digitando a ID referente a a algum produto, clicando no botão "read", recuperar todas as informações do produto nos campos correspondentes. Com isso, nos botões "delete" e "update" é possível atualizar algum dado do produto ou deletar.

____________________________________________________________________________________________________

Este programa foi desenvolvido em um laptop acer, modelo aspire 3, AMD Ryzen 5,12 Gb Ram.
linguagem de programação usada foi Python 3.8.8, com o auxílio da IDE PyCharm 2021.2.1 (Community Edition).
As bibliotecas usadas nesse programa foram:
	Sys;
	SQLite3;
	PyQt5-Qt5==5.15.2
	Pandas==1.2.4


Desenvolvido por Kaike Pacheco.

kaikesoad.km@gmail.com
