.PHONY: all clean

SVGS=$(wildcard *.svg)
SVGPDFS=$(patsubst %.svg,%.pdf,$(SVGS))

all: 171204.pdf

171204.pdf: 171204.tex $(filter-out 171204.pdf, $(wildcard *.tex 171204.*)) $(SVGPDFS)
	pdflatex -shell-escape "$<" && pdflatex -shell-escape "$<"

%.pdf: %.svg
	inkscape -D "--file=$<" "--export-pdf=$@"

clean:
	rm $(filter-out 171204.tex,$(wildcard 171204.*)) *.pdf >/dev/null 2>&1
