# Auto generated from monarch_documentation.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-01-03T12:29:16
# Schema: monarch-documentation-schema
#
# id: https://w3id.org/monarch-initiative/monarch-documentation
# description: Technical documentation for all Monarch applications, packages, services and related projects.
# license: GNU GPL v3.0

import dataclasses
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
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MTD = CurieNamespace('mtd', 'https://w3id.org/monarch-initiative/monarch-documentation/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MTD


# Types

# Class references
class ResourceId(URIorCURIE):
    pass


class DataAssetId(ResourceId):
    pass


class StandardId(ResourceId):
    pass


class ToolId(ResourceId):
    pass


class DocumentationId(ResourceId):
    pass


class ProjectBoardId(ResourceId):
    pass


class RepositoryId(ResourceId):
    pass


class ResourceRegistryId(ResourceId):
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
    short_name: Optional[str] = None
    description: Optional[str] = None
    grants: Optional[Union[Union[str, "GrantEnum"], List[Union[str, "GrantEnum"]]]] = empty_list()
    documentation: Optional[Union[str, URIorCURIE]] = None
    monarch_contribution: Optional[Union[str, "MonarchContributionEnum"]] = None
    repository: Optional[Union[str, URIorCURIE]] = None
    monarch_role: Optional[Union[str, "MonarchRoleEnum"]] = None
    citation: Optional[Union[str, URIorCURIE]] = None
    contact: Optional[Union[dict, "Contact"]] = None
    project_boards: Optional[Union[Dict[Union[str, ProjectBoardId], Union[dict, "ProjectBoard"]], List[Union[dict, "ProjectBoard"]]]] = empty_dict()
    icon: Optional[str] = None
    url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.grants, list):
            self.grants = [self.grants] if self.grants is not None else []
        self.grants = [v if isinstance(v, GrantEnum) else GrantEnum(v) for v in self.grants]

        if self.documentation is not None and not isinstance(self.documentation, URIorCURIE):
            self.documentation = URIorCURIE(self.documentation)

        if self.monarch_contribution is not None and not isinstance(self.monarch_contribution, MonarchContributionEnum):
            self.monarch_contribution = MonarchContributionEnum(self.monarch_contribution)

        if self.repository is not None and not isinstance(self.repository, URIorCURIE):
            self.repository = URIorCURIE(self.repository)

        if self.monarch_role is not None and not isinstance(self.monarch_role, MonarchRoleEnum):
            self.monarch_role = MonarchRoleEnum(self.monarch_role)

        if self.citation is not None and not isinstance(self.citation, URIorCURIE):
            self.citation = URIorCURIE(self.citation)

        if self.contact is not None and not isinstance(self.contact, Contact):
            self.contact = Contact(**as_dict(self.contact))

        self._normalize_inlined_as_list(slot_name="project_boards", slot_type=ProjectBoard, key_name="id", keyed=True)

        if self.icon is not None and not isinstance(self.icon, str):
            self.icon = str(self.icon)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        super().__post_init__(**kwargs)


@dataclass
class DataAsset(Resource):
    """
    A data asset is a resource that contains data, either manually curated, or generated by a computational (ETL)
    process. Data are raw facts (associations) generated by observations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.DataAsset
    class_class_curie: ClassVar[str] = "mtd:DataAsset"
    class_name: ClassVar[str] = "DataAsset"
    class_model_uri: ClassVar[URIRef] = MTD.DataAsset

    id: Union[str, DataAssetId] = None
    category: Union[str, "DataAssetEnum"] = None
    download: Optional[Union[Union[dict, "Download"], List[Union[dict, "Download"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAssetId):
            self.id = DataAssetId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, DataAssetEnum):
            self.category = DataAssetEnum(self.category)

        if not isinstance(self.download, list):
            self.download = [self.download] if self.download is not None else []
        self.download = [v if isinstance(v, Download) else Download(**as_dict(v)) for v in self.download]

        super().__post_init__(**kwargs)


@dataclass
class Standard(Resource):
    """
    Standards are agreed-upon conventions or guidelines that ensure uniformity, consistency, and compatibility in
    various fields and practices. They are like the common languages or rulebooks that different parties use to ensure
    they understand each other and can work together efficiently. Standards include both exchange standards, like KGX
    or SSSOM, and ontologies, like HPO or Mondo.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Standard
    class_class_curie: ClassVar[str] = "mtd:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = MTD.Standard

    id: Union[str, StandardId] = None
    category: Union[str, "StandardEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardId):
            self.id = StandardId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, StandardEnum):
            self.category = StandardEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Tool(Resource):
    """
    A software tool is a computer program designed to help users perform specific tasks or functions, typically making
    complex or time-consuming processes more efficient and user-friendly. These tasks can range from simple data
    manipulation to sophisticated design and analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Tool
    class_class_curie: ClassVar[str] = "mtd:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = MTD.Tool

    id: Union[str, ToolId] = None
    category: Union[str, "ToolAssetEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ToolId):
            self.id = ToolId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, ToolAssetEnum):
            self.category = ToolAssetEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Documentation(Resource):
    """
    A resource that contains documentation, like a wiki, a webpage with training materials, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Documentation
    class_class_curie: ClassVar[str] = "mtd:Documentation"
    class_name: ClassVar[str] = "Documentation"
    class_model_uri: ClassVar[URIRef] = MTD.Documentation

    id: Union[str, DocumentationId] = None
    category: Union[str, "DocumentationAssetEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DocumentationId):
            self.id = DocumentationId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, DocumentationAssetEnum):
            self.category = DocumentationAssetEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass
class ProjectBoard(Resource):
    """
    A reference to a project board, like a kanban board.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.ProjectBoard
    class_class_curie: ClassVar[str] = "mtd:ProjectBoard"
    class_name: ClassVar[str] = "ProjectBoard"
    class_model_uri: ClassVar[URIRef] = MTD.ProjectBoard

    id: Union[str, ProjectBoardId] = None
    url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectBoardId):
            self.id = ProjectBoardId(self.id)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Repository(Resource):
    """
    A reference to a version control repository.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Repository
    class_class_curie: ClassVar[str] = "mtd:Repository"
    class_name: ClassVar[str] = "Repository"
    class_model_uri: ClassVar[URIRef] = MTD.Repository

    id: Union[str, RepositoryId] = None
    depends_on: Optional[Union[str, RepositoryId]] = None
    repo_url: Optional[str] = None
    organization: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepositoryId):
            self.id = RepositoryId(self.id)

        if self.depends_on is not None and not isinstance(self.depends_on, RepositoryId):
            self.depends_on = RepositoryId(self.depends_on)

        if self.repo_url is not None and not isinstance(self.repo_url, str):
            self.repo_url = str(self.repo_url)

        if self.organization is not None and not isinstance(self.organization, str):
            self.organization = str(self.organization)

        super().__post_init__(**kwargs)


@dataclass
class ResourceRegistry(Resource):
    """
    A registry of different types of data assets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.ResourceRegistry
    class_class_curie: ClassVar[str] = "mtd:ResourceRegistry"
    class_name: ClassVar[str] = "ResourceRegistry"
    class_model_uri: ClassVar[URIRef] = MTD.ResourceRegistry

    id: Union[str, ResourceRegistryId] = None
    name: Optional[str] = None
    data: Optional[Union[Dict[Union[str, DataAssetId], Union[dict, DataAsset]], List[Union[dict, DataAsset]]]] = empty_dict()
    standards: Optional[Union[Dict[Union[str, StandardId], Union[dict, Standard]], List[Union[dict, Standard]]]] = empty_dict()
    tools: Optional[Union[Dict[Union[str, ToolId], Union[dict, Tool]], List[Union[dict, Tool]]]] = empty_dict()
    documentations: Optional[Union[Dict[Union[str, DocumentationId], Union[dict, Documentation]], List[Union[dict, Documentation]]]] = empty_dict()
    repositories: Optional[Union[Dict[Union[str, ResourceId], Union[dict, Resource]], List[Union[dict, Resource]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceRegistryId):
            self.id = ResourceRegistryId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="data", slot_type=DataAsset, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="standards", slot_type=Standard, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tools", slot_type=Tool, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="documentations", slot_type=Documentation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="repositories", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Download(YAMLRoot):
    """
    A downloadable asset, i.e. a data file, an software component, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Download
    class_class_curie: ClassVar[str] = "mtd:Download"
    class_name: ClassVar[str] = "Download"
    class_model_uri: ClassVar[URIRef] = MTD.Download

    url: Optional[Union[str, URIorCURIE]] = None
    release_status: Optional[Union[str, "ReleaseStatusEnum"]] = None
    file_format: Optional[Union[str, "FileFormatEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.release_status is not None and not isinstance(self.release_status, ReleaseStatusEnum):
            self.release_status = ReleaseStatusEnum(self.release_status)

        if self.file_format is not None and not isinstance(self.file_format, FileFormatEnum):
            self.file_format = FileFormatEnum(self.file_format)

        super().__post_init__(**kwargs)


@dataclass
class Contact(YAMLRoot):
    """
    The person responsible for a resources.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Contact
    class_class_curie: ClassVar[str] = "mtd:Contact"
    class_name: ClassVar[str] = "Contact"
    class_model_uri: ClassVar[URIRef] = MTD.Contact

    name: Optional[str] = None
    orcid: Optional[Union[str, URIorCURIE]] = None
    github: Optional[str] = None
    email: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.orcid is not None and not isinstance(self.orcid, URIorCURIE):
            self.orcid = URIorCURIE(self.orcid)

        if self.github is not None and not isinstance(self.github, str):
            self.github = str(self.github)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


# Enumerations
class ReleaseStatusEnum(EnumDefinitionImpl):

    public = PermissibleValue(text="public")

    _defn = EnumDefinition(
        name="ReleaseStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "development snapshot",
            PermissibleValue(text="development snapshot"))

class FileFormatEnum(EnumDefinitionImpl):

    tsv = PermissibleValue(text="tsv")
    csv = PermissibleValue(text="csv")
    ttl = PermissibleValue(text="ttl")
    json = PermissibleValue(text="json")
    rdfxml = PermissibleValue(text="rdfxml")

    _defn = EnumDefinition(
        name="FileFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "nt.gz",
            PermissibleValue(text="nt.gz"))

class StandardEnum(EnumDefinitionImpl):

    Ontology = PermissibleValue(text="Ontology")

    _defn = EnumDefinition(
        name="StandardEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data Standard",
            PermissibleValue(text="Data Standard"))
        setattr(cls, "Data Exchange",
            PermissibleValue(text="Data Exchange"))
        setattr(cls, "Ontology Curation",
            PermissibleValue(text="Ontology Curation"))

class DataAssetEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DataAssetEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Biomedical Data",
            PermissibleValue(text="Biomedical Data"))
        setattr(cls, "Knowledge Graph Ingestibles",
            PermissibleValue(text="Knowledge Graph Ingestibles"))
        setattr(cls, "Knowledge Graph",
            PermissibleValue(text="Knowledge Graph"))

class ToolAssetEnum(EnumDefinitionImpl):

    Mapping = PermissibleValue(text="Mapping")
    Benchmarking = PermissibleValue(text="Benchmarking")

    _defn = EnumDefinition(
        name="ToolAssetEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Clinical Diagnosis",
            PermissibleValue(text="Clinical Diagnosis"))
        setattr(cls, "Ontology Maintenance",
            PermissibleValue(text="Ontology Maintenance"))
        setattr(cls, "Ontology Use",
            PermissibleValue(text="Ontology Use"))
        setattr(cls, "Data Curation",
            PermissibleValue(text="Data Curation"))

class DocumentationAssetEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DocumentationAssetEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Technical Documentation",
            PermissibleValue(text="Technical Documentation"))
        setattr(cls, "Training Materials",
            PermissibleValue(text="Training Materials"))

class MonarchContributionEnum(EnumDefinitionImpl):

    Lead = PermissibleValue(text="Lead")
    Contributor = PermissibleValue(text="Contributor")

    _defn = EnumDefinition(
        name="MonarchContributionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Co-Lead",
            PermissibleValue(text="Co-Lead"))

class GrantEnum(EnumDefinitionImpl):

    HPO = PermissibleValue(text="HPO")
    Exomiser = PermissibleValue(text="Exomiser")
    TBD = PermissibleValue(text="TBD")

    _defn = EnumDefinition(
        name="GrantEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Phenomics First",
            PermissibleValue(
                text="Phenomics First",
                description="The Phenomics First Grant"))
        setattr(cls, "Monarch R24",
            PermissibleValue(text="Monarch R24"))
        setattr(cls, "Bosch Gift",
            PermissibleValue(text="Bosch Gift"))

class MonarchRoleEnum(EnumDefinitionImpl):

    Flagship = PermissibleValue(
        text="Flagship",
        description="""A flagship product is a product that fulfills a strategic role for the Monarch Initiative. In particular it (1) *directly* supports the Monarch mission (excluding products of general utility) (2) has stakeholders outside of the Monarch Initiative (3) has stakeholders among most major member organisations of the Monarch Initiative An important corrolary of (3) is that all major member organisations of the Monarch Initiative should feel a sense of commitment to contributing to the success of the flagship product.""")
    Core = PermissibleValue(
        text="Core",
        description="""A core product is a product that contributes to the Monarch mission, but is not a flagship product. In particular it (1) may support the Monarch mission in an indirect manner, such as core infrastructure for ontology lifecycle management or querying (2) has stakeholders outside of the Monarch Initiative (3) has stakeholders among at least one major member organisation of the Monarch Initiative An important corrolary of (3) is that at least one major member organisation of the Monarch Initiative should feel a sense of commitment to contributing to the success of the core product.""")
    Support = PermissibleValue(
        text="Support",
        description="""A support product is a product that only indirectly contributes to the Monarch mission, usually by supporting the development of a flagship or core product. A support product (1) does not directly support the Monarch mission, but is essential for the development of a flagship or core product (2) has few stakeholders outside of the Monarch Initiative""")
    Research = PermissibleValue(
        text="Research",
        description="""A research product is a product that supports our own research efforts. The research outcome may or may not be used in a flagship, core or support product. A research product (1) does not directly support the Monarch mission, but leads to insights that support our mission (2) has no stakeholders outside of the Monarch Initiative (the research itself may!)""")
    Community = PermissibleValue(
        text="Community",
        description="""A community product is a product that does not directly support the Monarch mission, but supports community efforts towards the mission. A community product (1) is usually a community resource, such as training materials, a community website, a standard specification, etc. (2) is usually more *general-purpose* (3) is community-driven, rather than mission-driven""")

    _defn = EnumDefinition(
        name="MonarchRoleEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MTD.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MTD.name, domain=None, range=Optional[str])

slots.short_name = Slot(uri=MTD.short_name, name="short_name", curie=MTD.curie('short_name'),
                   model_uri=MTD.short_name, domain=None, range=Optional[str])

slots.email = Slot(uri=MTD.email, name="email", curie=MTD.curie('email'),
                   model_uri=MTD.email, domain=None, range=Optional[str])

slots.github = Slot(uri=MTD.github, name="github", curie=MTD.curie('github'),
                   model_uri=MTD.github, domain=None, range=Optional[str])

slots.orcid = Slot(uri=MTD.orcid, name="orcid", curie=MTD.curie('orcid'),
                   model_uri=MTD.orcid, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MTD.description, domain=None, range=Optional[str])

slots.contact = Slot(uri=MTD.contact, name="contact", curie=MTD.curie('contact'),
                   model_uri=MTD.contact, domain=None, range=Optional[Union[dict, Contact]])

slots.download = Slot(uri=MTD.download, name="download", curie=MTD.curie('download'),
                   model_uri=MTD.download, domain=None, range=Optional[Union[Union[dict, Download], List[Union[dict, Download]]]])

slots.citation = Slot(uri=MTD.citation, name="citation", curie=MTD.curie('citation'),
                   model_uri=MTD.citation, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.grants = Slot(uri=MTD.grants, name="grants", curie=MTD.curie('grants'),
                   model_uri=MTD.grants, domain=None, range=Optional[Union[Union[str, "GrantEnum"], List[Union[str, "GrantEnum"]]]])

slots.project_boards = Slot(uri=MTD.project_boards, name="project_boards", curie=MTD.curie('project_boards'),
                   model_uri=MTD.project_boards, domain=None, range=Optional[Union[Dict[Union[str, ProjectBoardId], Union[dict, ProjectBoard]], List[Union[dict, ProjectBoard]]]])

slots.release_status = Slot(uri=MTD.release_status, name="release_status", curie=MTD.curie('release_status'),
                   model_uri=MTD.release_status, domain=None, range=Optional[Union[str, "ReleaseStatusEnum"]])

slots.repository = Slot(uri=MTD.repository, name="repository", curie=MTD.curie('repository'),
                   model_uri=MTD.repository, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.file_format = Slot(uri=MTD.file_format, name="file_format", curie=MTD.curie('file_format'),
                   model_uri=MTD.file_format, domain=None, range=Optional[Union[str, "FileFormatEnum"]])

slots.url = Slot(uri=MTD.url, name="url", curie=MTD.curie('url'),
                   model_uri=MTD.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.category = Slot(uri=MTD.category, name="category", curie=MTD.curie('category'),
                   model_uri=MTD.category, domain=None, range=str)

slots.icon = Slot(uri=MTD.icon, name="icon", curie=MTD.curie('icon'),
                   model_uri=MTD.icon, domain=None, range=Optional[str])

slots.documentation = Slot(uri=MTD.documentation, name="documentation", curie=MTD.curie('documentation'),
                   model_uri=MTD.documentation, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.monarch_contribution = Slot(uri=MTD.monarch_contribution, name="monarch_contribution", curie=MTD.curie('monarch_contribution'),
                   model_uri=MTD.monarch_contribution, domain=None, range=Optional[Union[str, "MonarchContributionEnum"]])

slots.monarch_role = Slot(uri=MTD.monarch_role, name="monarch_role", curie=MTD.curie('monarch_role'),
                   model_uri=MTD.monarch_role, domain=None, range=Optional[Union[str, "MonarchRoleEnum"]])

slots.data = Slot(uri=MTD.data, name="data", curie=MTD.curie('data'),
                   model_uri=MTD.data, domain=None, range=Optional[Union[Dict[Union[str, DataAssetId], Union[dict, DataAsset]], List[Union[dict, DataAsset]]]])

slots.standards = Slot(uri=MTD.standards, name="standards", curie=MTD.curie('standards'),
                   model_uri=MTD.standards, domain=None, range=Optional[Union[Dict[Union[str, StandardId], Union[dict, Standard]], List[Union[dict, Standard]]]])

slots.tools = Slot(uri=MTD.tools, name="tools", curie=MTD.curie('tools'),
                   model_uri=MTD.tools, domain=None, range=Optional[Union[Dict[Union[str, ToolId], Union[dict, Tool]], List[Union[dict, Tool]]]])

slots.documentations = Slot(uri=MTD.documentations, name="documentations", curie=MTD.curie('documentations'),
                   model_uri=MTD.documentations, domain=None, range=Optional[Union[Dict[Union[str, DocumentationId], Union[dict, Documentation]], List[Union[dict, Documentation]]]])

slots.repositories = Slot(uri=MTD.repositories, name="repositories", curie=MTD.curie('repositories'),
                   model_uri=MTD.repositories, domain=None, range=Optional[Union[Dict[Union[str, ResourceId], Union[dict, Resource]], List[Union[dict, Resource]]]])

slots.depends_on = Slot(uri=MTD.depends_on, name="depends_on", curie=MTD.curie('depends_on'),
                   model_uri=MTD.depends_on, domain=Repository, range=Optional[Union[str, RepositoryId]])

slots.repo_url = Slot(uri=MTD.repo_url, name="repo_url", curie=MTD.curie('repo_url'),
                   model_uri=MTD.repo_url, domain=None, range=Optional[str])

slots.organization = Slot(uri=MTD.organization, name="organization", curie=MTD.curie('organization'),
                   model_uri=MTD.organization, domain=None, range=Optional[str])

slots.DataAsset_category = Slot(uri=MTD.category, name="DataAsset_category", curie=MTD.curie('category'),
                   model_uri=MTD.DataAsset_category, domain=DataAsset, range=Union[str, "DataAssetEnum"])

slots.Standard_category = Slot(uri=MTD.category, name="Standard_category", curie=MTD.curie('category'),
                   model_uri=MTD.Standard_category, domain=Standard, range=Union[str, "StandardEnum"])

slots.Tool_category = Slot(uri=MTD.category, name="Tool_category", curie=MTD.curie('category'),
                   model_uri=MTD.Tool_category, domain=Tool, range=Union[str, "ToolAssetEnum"])

slots.Documentation_category = Slot(uri=MTD.category, name="Documentation_category", curie=MTD.curie('category'),
                   model_uri=MTD.Documentation_category, domain=Documentation, range=Union[str, "DocumentationAssetEnum"])
