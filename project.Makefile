## Add your own custom Makefile targets here

.INCLUDE : Makefile

genpython:
	@$(RUN) gen-python $(SOURCE_SCHEMA_PATH) > $(PYMODEL)/monarch_technical_documentation.py

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

############################################
### Provisional Monarch Asset Registry #####
############################################

src/docs/registry.md: src/monarch_technical_documentation/resources/monarch_resources.md.jinja2 src/data/resources.yaml
	$(RUN) j2 $^ > $@

src/docs/registry_2.md: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-convert -f yaml -C ResourceRegistry -t ttl -s $^

validate-registry: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-validate --target-class ResourceRegistry -s $^

gen-monarch-overview:
	$(MAKE) src/docs/registry.md -B

src/docs/resources/monarch-app-resources.json: src/monarch_technical_documentation/resources/monarch_app_resources.json.jinja2 src/data/resources.yaml
	mkdir -p src/docs/resources/
	$(RUN) j2 $^ > $@

gen-monarch-resources: src/docs/resources/monarch-app-resources.json