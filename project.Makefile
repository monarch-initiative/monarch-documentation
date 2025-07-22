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

build-docs: genindex genpython genschemadoc genrepodocs geningestdoc gen-monarch-overview gen-monarch-resources registry-tables
	@cp -r src/docs/* docs/
	@echo
	@echo "Documentation built! Run 'mkdocs serve' to view it locally, or check the 'docs' folder to see the generated files."

############################################
### Provisional Monarch Asset Registry #####
############################################

src/docs/registry.md: src/monarch_documentation/resources/monarch_resources.md.jinja2 src/data/resources.yaml
	$(RUN) jinja2 $^ > $@

src/docs/registry_2.md: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-convert -f yaml -C ResourceRegistry -t ttl -s $^

src/docs/resources/registry-standards.tsv: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-convert -t tsv -f yaml -C ResourceRegistry --index-slot standards -s $^ -o $@

src/docs/resources/registry-tools.tsv: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-convert -t tsv -f yaml -C ResourceRegistry --index-slot tools -s $^ -o $@

src/docs/resources/registry-data.tsv: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-convert -t tsv -f yaml -C ResourceRegistry --index-slot data -s $^ -o $@

registry-tables: src/docs/resources/registry-standards.tsv src/docs/resources/registry-tools.tsv src/docs/resources/registry-data.tsv

validate-registry: $(SOURCE_SCHEMA_PATH) src/data/resources.yaml
	$(RUN) linkml-validate --target-class ResourceRegistry -s $^

test: validate-registry registry-tables

gen-monarch-overview:
	$(MAKE) src/docs/registry.md -B

src/docs/resources/monarch-app-resources.json: src/monarch_documentation/resources/monarch_app_resources.json.jinja2 src/data/resources.yaml
	mkdir -p src/docs/resources/
	$(RUN) jinja2 $^ | jq . > $@

src/docs/resources/monarch-app-infopages.json: src/monarch_documentation/resources/monarch_app_infopages.json.jinja2 src/data/resources.yaml
	mkdir -p src/docs/resources/
	$(RUN) jinja2 $^ | jq . > $@

src/docs/resources/monarch-app-infopages.tsv: src/monarch_documentation/resources/monarch_app_infopages.tsv.jinja2 src/data/resources.yaml
	mkdir -p src/docs/resources/
	$(RUN) jinja2 $^ > $@

gen-monarch-resources: src/docs/resources/monarch-app-resources.json \
	src/docs/resources/monarch-app-infopages.json \
	src/docs/resources/monarch-app-infopages.tsv
