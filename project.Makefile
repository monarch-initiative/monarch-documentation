## Add your own custom Makefile targets here

.INCLUDE : Makefile

genpython:
	@$(RUN) gen-python $(SOURCE_SCHEMA_PATH) > $(PYMODEL)/monarch_documentation.py

genindex:
	@$(RUN) python scripts/generate_index.py

genrepodocs:
	@$(RUN) python scripts/generate_repo_pages.py

geningestdoc:
	@$(RUN) python scripts/generate_ingest_page.py

genschemadoc: $(DOCDIR)
	@$(RUN) gen-doc -d $(DOCDIR)/Documentation-Schema $(SOURCE_SCHEMA_PATH)

build-docs: genindex genpython genschemadoc genrepodocs geningestdoc gen-monarch-overview
	@cp -r src/docs/* docs/
	@echo
	@echo "Documentation built! Run 'mkdocs serve' to view it locally, or check the 'docs' folder to see the generated files."

############################################
### Provisional Monarch Asset Registry #####
############################################

src/docs/registry.md: src/monarch_documentation/resources/monarch_resources.md.jinja2 src/data/resources.yaml
	$(RUN) j2 $^ > $@

src/docs/registry_2.md: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-convert -f yaml -C ResourceRegistry -t ttl -s $^

validate-registry: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-validate --target-class ResourceRegistry -s $^

gen-monarch-overview:
	$(MAKE) src/docs/registry.md
