### Create table -lauseet ja indeksit

CREATE TABLE kayttaja (
	id INTEGER NOT NULL, 
	pvm_luonti DATETIME, 
	pvm_muokkaus DATETIME, 
	kayttajan_nimi VARCHAR(144) NOT NULL, 
	tunnus VARCHAR(144) NOT NULL, 
	salasana VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

 
CREATE TABLE tehtava (
	id INTEGER NOT NULL, 
	pvm_luonti DATETIME, 
	pvm_muokkaus DATETIME, 
	nimi VARCHAR(144) NOT NULL, 
	kuvaus VARCHAR(300), 
	PRIMARY KEY (id)
)


CREATE TABLE prosessi (
	id INTEGER NOT NULL, 
	pvm_luonti DATETIME, 
	pvm_muokkaus DATETIME, 
	prosessin_nimi VARCHAR(144) NOT NULL, 
	pvm_alku DATETIME, 
	pvm_loppu DATETIME, 
	owner_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES kayttaja (id)
)

CREATE INDEX idx_prosessi ON prosessi (prosessin_nimi, owner_id)


CREATE TABLE prosessitehtava (
	id INTEGER NOT NULL, 
	pvm_luonti DATETIME, 
	pvm_muokkaus DATETIME, 
	pvm_alku DATETIME, 
	pvm_loppu DATETIME, 
	pvm_kommentti DATETIME, 
	kommentti VARCHAR(300), 
	aloitettu BOOLEAN NOT NULL, 
	valmis BOOLEAN NOT NULL, 
	kuittaaja_alku_id INTEGER, 
	kuittaaja_loppu_id INTEGER, 
	kommentoija_id INTEGER, 
	prosessi_id INTEGER, 
	tehtava_id INTEGER, 
	PRIMARY KEY (id), 
	CHECK (aloitettu IN (0, 1)), 
	CHECK (valmis IN (0, 1)), 
	FOREIGN KEY(kuittaaja_alku_id) REFERENCES kayttaja (id), 
	FOREIGN KEY(kuittaaja_loppu_id) REFERENCES kayttaja (id), 
	FOREIGN KEY(kommentoija_id) REFERENCES kayttaja (id), 
	FOREIGN KEY(prosessi_id) REFERENCES prosessi (id), 
	FOREIGN KEY(tehtava_id) REFERENCES tehtava (id)
)


CREATE TABLE tekija (
	id INTEGER NOT NULL, 
	pt_id INTEGER, 
	tekija_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(pt_id) REFERENCES prosessitehtava (id), 
	FOREIGN KEY(tekija_id) REFERENCES kayttaja (id)
)

