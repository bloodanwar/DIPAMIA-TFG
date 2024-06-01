.PHONY: analyse extract compile

analyse:
	@echo "*******************"
	@echo "Analysing video"
	@echo "*******************"
	-mkdir ./tmp
	-python ./videoAnalizer.py $(video)
	extract

extract:
	@echo "*******************"
	@echo "Extracting data"
	@echo "*******************"
	-python ./angleExtractor.py
	-python ./lenExtractor.py

compile:
	@echo "*******************"
	@echo "Compiling data"
	@echo "*******************"	
	-python ./dataCompiler.py $(diagn)
