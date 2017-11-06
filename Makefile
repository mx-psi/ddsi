SUBFILES:=$(wildcard **.md)

all: practica.pdf

practica.pdf: practica.md  $(SUBFILES)
	pandoc --filter pandoc-include $< -o $@

clean:
	rm *.pdf
