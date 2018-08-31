### Mitä jäi toteuttamatta
* Prosessista ei voi poistaa tehtäviä eikä tehtäviltä tekijöitä
* Monilta lomakkeilta jäi puuttumaan validointeja
* ORMia ei ole hyödynnetty riittävästi. Tosin yritystä kyllä oli, mutta tämä ei näy lopputulemassa, kun tuntien turhan yrittämisen tulos oli edelleen pelkkää virheilmoitusta ja sitten piti kuitenkin turvautua SQL-kyselyyn
* Käytettävyydessä olisi vielä hiomista etenkin sivujen rakenteen osalta. Ei ole menty siis suoranaisesti siitä, missä aita on matalin, vaan siitä mistä on rajallisilla HTML-taidoilla ja ajankäytöllä saatu toimiva sivu kursittua kasaan
** Sivutus puuttuu
* Autorisointia 
** Adminille eri näkymä kuin muille käyttäjille (esim. vain käyttäjähallinta admineille näkyviin) 
** Prosessia saa muokata vain sen omistaja ja prosessin tehtäviä vain prosessin omistaja tai tehtävälle tekijöiksi nimetyt henkilöt
* Refaktorointia
** Copypastea on turhan paljon
** Funktioita pitäisi muutenkin purkaa useampaan osaan
* Raportteja
** Prosessin omistajan raportit (toisaalta prosessinseurantasivusta tuli parempi kuin arvelin, tämä pitkälti kattaa nuo tarpeet)
** Työntekijän raportit osittain



