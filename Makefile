SUBFILES:=$(wildcard **.md)
DIAS:=$(wildcard Diagramas/*.dia)
PNGS:=$(patsubst %.dia,%.png,$(DIAS))

all: practica.pdf

%.png: %.dia
	dia $< --export $@

practica.pdf: practica.md  $(SUBFILES) $(PNGS)
	pandoc --filter pandoc-include $< -o $@

clean:
	rm *.pdf Diagramas/*.png
