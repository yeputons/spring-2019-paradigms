.PHONY: all clean

SVGS=$(wildcard *.svg)
SVGPDFS=$(patsubst %.svg,%.pdf,$(SVGS))

all: 190508.pdf

190508.pdf: 190508.tex $(filter-out 190508.pdf, $(wildcard *.tex 190508.*)) $(SVGPDFS)
	pdflatex -shell-escape "$<" && pdflatex -shell-escape "$<"

%.pdf: %.svg
	inkscape -D "--file=$<" "--export-pdf=$@"

clean:
	rm $(filter-out 190508.tex,$(wildcard 190508.*)) *.pdf >/dev/null 2>&1
