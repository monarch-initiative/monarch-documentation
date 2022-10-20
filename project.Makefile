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

genschemadoc: $(DOCDIR)
	$(RUN) gen-doc -d $(DOCDIR)/Documentation-Schema $(SOURCE_SCHEMA_PATH)

build-docs: genpython genschemadoc genindex
	@rm -f $(DOCDIR)/Documentation-Schema/about.md
