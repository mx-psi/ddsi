SUBFILES:=$(shell find -type f -name '*.md')
DIAS:=$(wildcard Diagramas/*.dia)
PNGS:=$(patsubst %.dia,%.png,$(DIAS))

all: presentacion.pdf practica.pdf

%.png: %.dia
	dia $< --export $@

practica.pdf: practica.md  $(SUBFILES) $(PNGS)
	pandoc --filter pandoc-include $< -o $@

presentacion.pdf: presentacion.md $(SUBFILES)
	pandoc --filter pandoc-include -t beamer $< -o $@

clean:
	rm *.pdf Diagramas/*.png
