SUBFILES:=$(shell find -type f -name '*.md')
DIAS:=$(wildcard Diagramas/*.dia)
PNGS:=$(patsubst %.dia,%.png,$(DIAS))

all: practica.pdf presentacion.pdf

%.png: %.dia
	dia $< --export $@

practica.pdf: practica.md  $(SUBFILES) $(PNGS)
	pandoc --filter pandoc-include $< -o $@

presentacion.pdf: presentacion.md Presentacion/instalacion.md Presentacion/funcionalidades.md
	pandoc --filter pandoc-include -t beamer $< -o $@

clean:
	rm *.pdf Diagramas/*.png
