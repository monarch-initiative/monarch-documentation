

CREATE TABLE "DataAsset" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	grant VARCHAR(15), 
	documentation TEXT, 
	monarch_contribution VARCHAR(4), 
	download TEXT, 
	category VARCHAR(15), 
	PRIMARY KEY (id)
);

CREATE TABLE "Download" (
	url TEXT, 
	release_status TEXT, 
	file_format TEXT, 
	PRIMARY KEY (url, release_status, file_format)
);

CREATE TABLE "Resource" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	grant VARCHAR(15), 
	documentation TEXT, 
	monarch_contribution VARCHAR(4), 
	PRIMARY KEY (id)
);

CREATE TABLE "ResourceRegistry" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	grant VARCHAR(15), 
	monarch_contribution VARCHAR(4), 
	data TEXT, 
	standards TEXT, 
	tools TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Standard" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	grant VARCHAR(15), 
	documentation TEXT, 
	monarch_contribution VARCHAR(4), 
	category VARCHAR(13), 
	PRIMARY KEY (id)
);

CREATE TABLE "Tool" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	grant VARCHAR(15), 
	documentation TEXT, 
	monarch_contribution VARCHAR(4), 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Documentation" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	grant VARCHAR(15), 
	documentation TEXT, 
	monarch_contribution VARCHAR(4), 
	url TEXT, 
	"ResourceRegistry_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ResourceRegistry_id") REFERENCES "ResourceRegistry" (id)
);
