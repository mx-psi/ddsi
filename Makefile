all: practica.pdf

practica.pdf: practica.md
	pandoc --filter pandoc-include $^ -o $@
