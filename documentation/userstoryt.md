### Tehtävän lisääminen

Käyttäjä lisää uuden tehtävän tehtävälistaan

Hyväksymiskriteerit:
* Tehtävän lisäämisen valinta päävalikosta
* Tehtävälle annetaan nimi ja kuvaus
* Uusi tehtävä tallennetaan painikkeella
* Tehtävä saa lisäys- ja muokkauspäiväksi tallennushetken

```
INSERT INTO Tehtava (nimi, kuvaus, pvm_luonti, pvm_muokkaus) VALUES ('Tehtävän nimi', 'Tehtävän kuvaus', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) 
```


### Tehtävien listaus

Käyttäjä saa nähdäkseen listan järjestelmään lisätyistä tehtävistä

Hyväksymiskriteerit:
* Pääsivulta pääsee linkin kautta listaukseen
* Sovellus näyttää listan kaikista järjestelmään kirjatuista tehtävistä

'''
SELECT * FROM Tehtava
'''


### Tehtävän muokkaus

Käyttäjä voi muokata järjestelmään lisätyn tehtävän kuvausta

Hyväksymiskriteerit:
* Käyttäjä voi valita tehtävälistauksesta tehtävän muokattavaksi
* Sovellus näyttää valitun tehtävän tiedot
* Käyttäjä voi muokata tehtävän kuvaustietoja
* Tiedot tallennetaan tallennuspainikkeella
* Tehtävän muokkauspäivä päivittyy tallennushetkeen

Valinta:
'''
SELECT * FROM Tehtava WHERE Tehtava.id = tehtava_id
'''

Muokkaus:
'''
UPDATE Tehtava SET pvm_muokkaus=CURRENT_TIMESTAMP, kuvaus='Uusi kuvaus'
WHERE id = tehtavan_id
'''

### Tehtävän poistaminen

Käyttäjä voi poistaa tehtävän

Hyväksymiskriteerit:
* Käyttäjä voi valita poistettavan tehtävän
* Tehtävä poistetaan

'''
DELETE FROM Tehtava WHERE Tehtava.id = tehtavan_id
'''


### Käyttäjän lisääminen

Käyttäjä lisää sovellukseen käyttäjiä

Hyväksymiskriteerit:
* Sovelluksen pääsivulta pääsee käyttäjien lisäämiseen
* Lomakkeelle täydennetään käyttäjätunnus, etunimi ja sukunimi
* Tiedot tallennetaan 
* Tallennettaessa luonti- ja muokkauspäiväksi tulee tallennushetki

Haetaan listaus:
'''
SELECT * FROM Kayttaja
'''

Lisätään käyttäjä:
'''
INSER INTO Kayttaja (kayttajan_nimi, tunnus, salasana, pvm_luonti, pvm_muokkaus)
VALUES ('Nimi', 'tunnus', 'salasana', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) 
'''


### Käyttäjän tietojen muokkaus

Käyttäjä muokkaa muiden käyttäjien ja omia tietojaan, koska tiedot ovat muuttuneet tai salasana unohtunut

Hyväksymiskriteerit:
* Käyttäjä voi valita oman tai muun käyttäjän tiedot muokattavaksi
* Sovellus antaa käyttäjän senhetkiset tiedot lomakkeella
* Käyttäjän nimeä ja salasanaa voi muokata 

Valinta:
'''
SELECT * FROM Kayttaja WHERE id = kayttajan_id
'''

Muokkaus:
'''
UPDATE Kayttaja SET tunnus='Tunnus', kayttajan_nimi='Uusi nimi', salasana='Uusi salasana', pvm_muokkaus=CURRENT_TIMESTAMP
'''


### Työprosessin lisääminen

Käyttäjä lisää uuden työprosessin

Hyväksymiskriteerit:
* Päävalikosta pääsee työprosessisivulle jossa listataan prosessit
* Painikkeella pääsee lisäämään uuden prosessin
* Prosessille määritellään nimi, alkupäivä, loppupäivä ja omistajaksi prosessin lisääjä

Listaus:
'''
SELECT * FROM Prosessi
'''

Lisäys:
'''
INSERT INTO Prosessi (prosessin_nimi, owner_id, pvm_alku, pvm_loppu, pvm_luonti, pvm_muokkaus)
VALUES ('Prosessin nimi', id_nro, '2018-08-31', '2018-09-01', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
'''


### Työprosessin ja siihen liittyvien tehtävien listaus (prosessinseuranta)

Käyttäjä pääsee tarkastelemaan prosessin ja siihen liitettyjen tehtävien tietoja

Hyväksymiskriteerit:
* Käyttäjä valitsee listalta olemassa olevan prosessin, jonka tiedot tulevat näytölle
* Näytetään sekä prosessin tiedot että siihen liitetyt tehtävät listauksena

Näytä prosessilista:
'''
SELECT * FROM Prosessi
'''

Näytä prosessinseuranta:
'''
SELECT * FROM Prosessi WHERE id = prosessin_id

SELECT * FROM Prosessitehtava WHERE prosessi_id = prosessin_id

SELECT Kayttaja.tunnus FROM Kayttaja
INNER JOIN Tekija ON Kayttaja.id = Tekija.tekija_id
INNER JOIN Prosessitehtava ON Tekija.pt_id = Prosessitehtava.id
WHERE Prosessitehtava.prosessi_id = prosessin_id
'''


### Tehtävien lisääminen työprosessiin

Käyttäjä voi lisätä valitsemaansa työprosessiin tehtäviä

Hyväksymiskriteerit:
* Prosessinseurantanäytöllä on painike, josta lisätään uusi tehtävä
* Tehtävälistan jatkeeksi tulee uusi rivi, josta valitaan tehtävätyyppi, alkamisaika ja päättymisaika
* Tiedot tallennetaan osaksi prosessin tehtäviä
* Prosessikohtaisille tehtäville määritellään tekijä

'''
INSERT INTO Prosessitehtava (pvm_luonti, pvm_muokkaus, pvm_alku, pvm_loppu, prosessi_id, tehtava_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '2018-08-31', '2018-09-01', prosessin_id, tehtavan_id)

INSERT INTO Tekija (pt_id, tekija_id)
VALUES (prosessin_id, tekijan_id)
'''


### Työprosessin tehtävien päivittäminen

Käyttäjät voivat päivittää työprosessin tehtäviä aloitetuiksi ja tehdyiksi, lisätä niihin kommentija muokata alku- ja loppupäiviä

Hyväksymiskriteerit:
* Käyttäjä voi muokata tehtävän tietoja tehtävälistauksessa
* Käyttäjä voi päivittää tehtävän aloitetuksi (jos aloittamatta) ja tehdyksi (jos aloitettu)
** Sovellus päivittää aloitus- ja valmistumisajat vastaavasti
** Samalla päivitetään myös kuittaus tehtävän aloittaneesta/lopettaneesta käyttäjästä

'''
UPDATE prosessitehtava 
SET pvm_muokkaus=CURRENT_TIMESTAMP, pvm_alku=annettu_pvm, pvm_loppu=annettu_pvm, pvm_kommentti=CURRENT_TIMESTAMP, kommentti='Kommenttiteksti', aloitettu=1, kuittaaja_alku_id=kayttajan_id, kommentoija_id=kayttajan_id WHERE prosessitehtava.id = prosessitehtavan_id
'''


### Tekijöiden lisääminen työprosessin tehtäville

Käyttäjät voivat lisätä tekijöitä työprosessin tehtäville

Hyväksymiskriteerit:
* Käyttäjälle näytetään lista tekijöistä, jotka tehtävällä jo on
* Käyttäjä voi valita pudotusvalikosta lisätekijän tehtävälle
** Valikossa näytetään vain ne käyttäjät, joita ei ole vielä lisätty tekijöiksi tehtävälle
* Uusi käyttäjä tallennetaan Tallenna-painikkeella

Listaus lisäysmahdollisuuksista:
'''
SELECT Kayttaja.id, Kayttaja.tunnus FROM Kayttaja
WHERE Kayttaja.id NOT IN 
(SELECT Tekija.tekija_id FROM Tekija WHERE Tekija.pt_id = prosessitehtavan_id)
'''

Tekijän lisääminen:
'''
INSERT Tekija (pt_id, tekija_id) VALUES (prosessitehtavan_id, kayttajan_id)
'''

### Käyttäjän raportit
Käyttäjä näkee etusivulla raportin omistamistaan prosesseista ja keskeneräisten tehtäviensä lukumäärän

Hyväksymiskriteerit:
* Etusivulla näytetään kirjautuneen käyttäjän omistamien prosessien lukumäärä ja listaus näistä
* Etusivulla näytetään käyttäjälle nimettyjen keskeneräisten tehtävien lukumäärä

Prosessit:
'''
SELECT COUNT(Prosessi.id) as lkm FROM Kayttaja
LEFT JOIN Prosessi ON Prosessi.owner_id = Kayttaja.id
WHERE Kayttaja.id = kayttajan_id
GROUP BY Kayttaja.id

SELECT Prosessi.id as prosessi_id, Prosessi.prosessin_nimi as prosessin_nimi FROM Prosessi
LEFT JOIN Kayttaja ON Prosessi.owner_id = Kayttaja.id
WHERE Kayttaja.id = kayttajan_id
'''

Tehtävät:
'''
SELECT COUNT(Prosessitehtava.id) as lkm FROM Prosessitehtava
JOIN Tekija ON Tekija.pt_id = Prosessitehtava.id
WHERE Tekija.tekija_id = kayttajan_id
AND Prosessitehtava.aloitettu"
AND NOT Prosessitehtava.valmis
'''
