all: practica.pdf

practica.pdf: practica.md requisitosproductos.md requisitosentidades.md requisitosusuario.md requisitosvaloraciones.md
	pandoc --filter pandoc-include $^ -o $@
