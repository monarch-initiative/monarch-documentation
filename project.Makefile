## Add your own custom Makefile targets here

.INCLUDE : Makefile

genpython:
	$(RUN) gen-python $(SOURCE_SCHEMA_PATH) > $(PYMODEL)/monarch_technical_documentation.py

genindex:
	$(RUN) python scripts/generate_index.py

genrepodocs:
	$(RUN) python scripts/generate_repo_pages.py

genschemadoc: $(DOCDIR)
	$(RUN) gen-doc -d $(DOCDIR)/Documentation-Schema $(SOURCE_SCHEMA_PATH)

build-docs: genpython genschemadoc genindex genrepodocs
	@rm -f $(DOCDIR)/Documentation-Schema/about.md
