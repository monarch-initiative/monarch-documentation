# Auto generated from monarch_technical_documentation.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-18T17:44:22
# Schema: monarch-documentation-schema
#
# id: https://w3id.org/monarch-initiative/monarch-technical-documentation
# description: Technical documentation for all Monarch applications, packages, services and related projects.
# license: GNU GPL v3.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MTD = CurieNamespace('mtd', 'https://w3id.org/monarch-initiative/monarch-technical-documentation/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MTD


# Types

# Class references
class ResourceId(URIorCURIE):
    pass


@dataclass
class Resource(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = MTD.Resource

    id: Union[str, ResourceId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ResourceCollection(YAMLRoot):
    """
    A holder for Resource objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.ResourceCollection
    class_class_curie: ClassVar[str] = "mtd:ResourceCollection"
    class_name: ClassVar[str] = "ResourceCollection"
    class_model_uri: ClassVar[URIRef] = MTD.ResourceCollection

    entries: Optional[Union[Dict[Union[str, ResourceId], Union[dict, Resource]], List[Union[dict, Resource]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MTD.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MTD.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MTD.description, domain=None, range=Optional[str])

slots.resourceCollection__entries = Slot(uri=MTD.entries, name="resourceCollection__entries", curie=MTD.curie('entries'),
                   model_uri=MTD.resourceCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ResourceId], Union[dict, Resource]], List[Union[dict, Resource]]]])
