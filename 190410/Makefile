.PHONY: all clean

SVGS=$(wildcard *.svg)
SVGPDFS=$(patsubst %.svg,%.pdf,$(SVGS))

all: 190410.pdf

190410.pdf: 190410.tex $(filter-out 190410.pdf, $(wildcard *.tex 190410.*)) $(SVGPDFS)
	pdflatex -shell-escape "$<" && pdflatex -shell-escape "$<"

%.pdf: %.svg
	inkscape -D "--file=$<" "--export-pdf=$@"

clean:
	rm $(filter-out 190410.tex,$(wildcard 190410.*)) *.pdf >/dev/null 2>&1
