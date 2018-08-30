### Tehtävän lisääminen

Käyttäjä lisää uuden tehtävän tehtävälistaan

Hyväksymiskriteerit:
* Tehtävän lisäämisen valinta päävalikosta
* Tehtävälle annetaan nimi ja kuvaus
* Uusi tehtävä tallennetaan painikkeella
* Tehtävä saa lisäys- ja muokkauspäiväksi tallennushetken


### Tehtävien listaus

Käyttäjä saa nähdäkseen listan järjestelmään lisätyistä tehtävistä

Hyväksymiskriteerit:
* Pääsivulta pääsee linkin kautta listaukseen
* Sovellus näyttää listan kaikista järjestelmään kirjatuista tehtävistä


### Tehtävän muokkaus

Käyttäjä voi muokata järjestelmään lisätyn tehtävän kuvausta

Hyväksymiskriteerit:
* Käyttäjä voi valita tehtävälistauksesta tehtävän muokattavaksi
* Sovellus näyttää valitun tehtävän tiedot
* Käyttäjä voi muokata tehtävän kuvaustietoja
* Tiedot tallennetaan tallennuspainikkeella
* Tehtävän muokkauspäivä päivittyy tallennushetkeen


### Käyttäjän lisääminen

Käyttäjä lisää sovellukseen käyttäjiä

Hyväksymiskriteerit:
* Sovelluksen pääsivulta pääsee käyttäjien lisäämiseen
* Lomakkeelle täydennetään käyttäjätunnus, etunimi ja sukunimi
* Tiedot tallennetaan 
* Tallennettaessa luonti- ja muokkauspäiväksi tulee tallennushetki


### Käyttäjän tietojen muokkaus

Käyttäjä muokkaa muiden käyttäjien ja omia tietojaan, koska tiedot ovat muuttuneet tai salasana unohtunut

Hyväksymiskriteerit:
* Käyttäjä voi valita oman tai muun käyttäjän tiedot muokattavaksi
* Sovellus antaa käyttäjän senhetkiset tiedot lomakkeella
* Käyttäjän nimeä ja salasanaa voi muokata 


### Työprosessin lisääminen

Käyttäjä lisää uuden työprosessin

Hyväksymiskriteerit:
* Päävalikosta pääsee työprosessin lisäyssivulle
* Prosessille määritellään nimi, alkupäivä, loppupäivä ja omistajaksi prosessin lisääjä


### Työprosessin ja siihen liittyvien tehtävien listaus (prosessinseuranta)

Käyttäjä pääsee tarkastelemaan prosessin ja siihen liitettyjen tehtävien tietoja

Hyväksymiskriteerit:
* Käyttäjä valitsee listalta olemassa olevan prosessin, jonka tiedot tulevat näytölle
* Näytetään sekä prosessin tiedot että siihen liitetyt tehtävät listauksena


### Tehtävien lisääminen työprosessiin

Käyttäjä voi lisätä valitsemaansa työprosessiin tehtäviä

Hyväksymiskriteerit:
* Prosessinseurantanäytöllä on painike, josta lisätään uusi tehtävä
* Tehtävälistan jatkeeksi tulee uusi rivi, josta valitaan tehtävätyyppi, alkamisaika ja päättymisaika
* Tiedot tallennetaan osaksi prosessin tehtäviä
* Prosessikohtaisille tehtäville määritellään tekijät


### Työprosessin tehtävien päivittäminen

Käyttäjät voivat päivittää työprosessin tehtäviä aloitetuiksi ja tehdyiksi, lisätä niihin kommentija muokata alku- ja loppupäiviä

Hyväksymiskriteerit:
* Käyttäjä voi muokata tehtävän tietoja tehtävälistauksessa
* Käyttäjä voi päivittää tehtävän aloitetuksi (jos aloittamatta) ja tehdyksi (jos aloitettu)
** Sovellus päivittää aloitus- ja valmistumisajat vastaavasti
** Samalla päivitetään myös kuittaus tehtävän aloittaneesta/lopettaneesta käyttäjästä

### Tekijöiden lisääminen työprosessin tehtäville

Käyttäjät voivat lisätä tekijöitä työprosessin tehtäville

Hyväksymiskriteerit:
* Käyttäjälle näytetään lista tekijöistä, jotka tehtävällä jo on
* Käyttäjä voi valita pudotusvalikosta lisätekijän tehtävälle
** Valikossa näytetään vain ne käyttäjät, joita ei ole vielä lisätty tekijöiksi tehtävälle
* Uusi käyttäjä tallennetaan Tallenna-painikkeella
