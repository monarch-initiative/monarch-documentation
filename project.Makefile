## Add your own custom Makefile targets here

.INCLUDE : Makefile

genpython:
	@echo ""
	@echo "Generating Python datamodel from project schema..."
	@echo ""
	$(RUN) gen-python $(SOURCE_SCHEMA_PATH) > $(PYMODEL)/monarch_technical_documentation.py

genindex:
	@echo ""
	@echo "Generating index.md..."
	@echo ""
	$(RUN) python scripts/generate_index.py

build-docs: genpython gendoc genindex
	@rm $(DOCDIR)/about.md
