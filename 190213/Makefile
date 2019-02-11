.PHONY: all svgs clean

SVGS=$(wildcard *.svg)
SVGPDFS=$(patsubst %.svg,%.pdf,$(SVGS))
NAME=190213

all: $(NAME).pdf

svgs: $(SVGPDFS)

$(NAME).pdf: $(wildcard *.tex $(NAME).*) $(SVGPDFS)
	pdflatex -shell-escape "$<" && pdflatex -shell-escape "$<"

%.pdf: %.svg
	inkscape -D "--file=$<" "--export-pdf=$@"

clean:
	rm $(filter-out $(NAME).tex,$(wildcard $(NAME).*)) *.pdf >/dev/null 2>&1
