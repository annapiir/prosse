# Prosse - Työprosessien seurantasovellus

Osoite: https://prosse.herokuapp.com/

## Kuvaus

Sovelluksen avulla voidaan määritellä erilaisista tehtävistä koostuvia työprosesseja sekä seurata näiden etenemistä. 

Organisaatiossa on työprosesseja, jotka koostuvat tehtävistä. Sovelluksessa määritellään tehtäviä, muodostetaan tehtävistä työprosesseja ja seurataan prosessien etenemistä tehtäväkohtaisesti.  

Prosessista vastaava henkilö määrittelee tehtäviä ja kokoaa niistä työprosesseja. Hän myös määrittää tehtäville tekijät. Lisäksi prosessivastaava saa järjestelmältä raportteja työn etenemisestä ja tehtäviin sekä työprosessiin käytetystä ajasta.

Työntekijät merkkaavat käynnistetyistä prosesseista tehtävät aloitetuiksi ja lopetetuiksi ja voivat myös kommentoida työprosessikierrokseen liittyviä tehtäviä. Koska työntekijä voi tehdä samanaikaisesti töitä usean työprosessin parissa, hän saa järjestelmältä nähtäväkseen raportin, jossa on tietoja hänen tehtävistään (tehdyistä, tekeillä olevista ja hänelle osoitetuista).  

Toimintoja:
* Kirjautuminen 
* Käyttäjien lisääminen/poistaminen/muuttaminen
* Tehtävien määrittely/poistaminen/muuttaminen
* Työprosessien kokoaminen tehtävistä
* Tekijöiden määrittely työprosessiin kuuluville tehtäville
* Prosessiin kuuluvien tehtävien aloittaminen/lopettaminen
* Prosessivastaavan raportit
* Työntekijän raportit


## Kehitysdokumentaatio
* [Tietokantakaavio](../documentation/prosse_db.png)
* Käyttäjätarinat
** [Tehtävän lisääminen](../documentation/userstory/tehtava_lisays.md)
** [Tehtävien listaus](../documentation/userstory/tehtava_listaus.md)
** [Tehtävän muokkaus](../documentation/userstory/tehtava_muokkaus.md)
** [Käyttäjän lisääminen](../documentation/userstory/kayttaja_lisays.md)
** [Työprosessin lisääminen](../documentation/userstory/prosessi_lisays.md)
** [Työprosessin tehtävien päivittäminen](../documentation/userstory/pt_statuksen_paivittaminen.md)
