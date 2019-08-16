TEX = latex -halt-on-error #-interaction=nonstopmode
BIB = bibtex
DVIP = dvips -q
CONV = ps2pdf
STDOUT = /dev/null
debug:
	$(TEX) numfunc
report:
	echo 'LaTeX'
	$(TEX) numfunc > $(STDOUT)
	$(TEX) numfunc > $(STDOUT)
	echo 'Converting to PDF'
	$(DVIP) numfunc.dvi
	sed -i 's/Title: numfunc.dvi/Title: 2G03/g' numfunc.ps
	$(CONV) numfunc.ps
	rm -f numfunc.dvi numfunc.ps
clean :
	rm -f *.aux *.bbl *.blg *.aux *.log *.lof *.lot
