# Print check for three readings (4 October 2026)

Task: find an older clear text, a period decipherment, a summary, a calendar entry or an archive-guide
entry for three letters. All searches were made on 4 October 2026. The files that I downloaded are in `src/`.
The helper `fts.py` asks the full-text search of archive.org.

Words used in the verdicts: "text in print", "content known, text not found", "nothing found".

Limits that apply to all three:

- HathiTrust full-text search gives a bot check ("Just a moment...", HTTP 403). I did not try to pass it. Not searched.
- The Google Books API gives HTTP 429. I used the Google Books search page in the browser pane for a few phrases.
- Gallica: only the SRU service was used (phrase search with `text adj "..."`), one request each 10 seconds.
- A "not found" from a full-text search depends on the OCR. It is weaker than a page-by-page reading.

---


## 2. Philip II to Vargas Mexía, March 1578, on Stukeley (BnF Espagnol 132, f. 26r); three letters of Antonio Pérez (ff. 87, 157, 179)

**Verdict for f. 26r: content known, text not found.** The gift of 20,000 escudos, the secrecy and the date are in print since 1926 from the Vatican side. The minute is listed in the Simancas catalogue.
**Verdict for the cipher passages of the Pérez letters: nothing found** (beyond what our file already says: Gachard 1875, Rubino 2012, Cabinet Noir 2026).

### Sources searched

| Source | Search | Result |
|---|---|---|
| J. Paz, *Archivo de Simancas, Catálogo IV, Secretaría de Estado (Capitulaciones con Francia y negociaciones diplomáticas ...)* (1914). https://archive.org/details/catlogo4secret01spai | Text file, words "Stucley", "Arcanti", "Capelo", "Sotomayor", "Avila" | **p. 898: "K. 1556. (B. 50.) Correspondencia de D. Juan de Vargas. A. 1578. — Respuesta a Vargas sobre lo de Stucley y Secretario Villerroi."** This is the minute of our letter (Stukeley, then Villeroy: the same two subjects, in the same order). |
| *Calendar of State Papers, Rome*, vol. 2 (1572-1578), February to May 1578. https://www.british-history.ac.uk/cal-state-papers/vatican/vol2/pp387-396 , `/pp397-422`, `/pp422-448`, `/pp377-386` | Page text, words "20,000", "Palamos", "crowns" | The gift is fully documented (see Findings). |
| *Calendar of State Papers, Spain (Simancas)*, vol. 2, February to May 1578. https://www.british-history.ac.uk/cal-state-papers/simancas/vol2/pp561-573 (also `/pp560-561`, `/pp573-578`, `/pp578-587`) | Page text, words "Stukel", "Vargas", "Palam", "20,000", "Villeroy" | Only Mendoza's letters from London. p. 561: the Queen "is much alarmed at news from Florence that Stukeley had left Civita Vecchia". No letter of Philip II to Vargas. |
| Teulet, *Relations politiques de la France et de l'Espagne avec l'Écosse*, vol. 5. https://archive.org/details/relationspolitiq05teul | Text file, words "Stucl", "Estucl", "Palam", all items of 1578 | pp. 137-141: Vargas to the King, 16 February, 16 March and 27 March 1578 (Scottish matter only). The King's answer of March 1578 is not printed. "Estucley" appears only in 1571-1574. |
| Gachard, *La Bibliothèque nationale à Paris*, vol. 1 (1875), pp. 415-421 (notice of this manuscript). https://archive.org/details/labibliothque01gach ; vol. 2 https://archive.org/details/labibliothquen02gachuoft | Text files, words "Stucl", "Vargas" | He describes only the letters that are in clear. "à toutes celles qui sont chiffrées (sauf une seule) le déchiffrement manque. Les Archives nationales possèdent d'ailleurs, dans la collection dite de Simancas, toute la correspondance de Vargas avec Philippe II." No word on the letter of March 1578. p. 420: the one sentence of f. 87 ("recobrar á heredero"). |
| Morel-Fatio, *Catalogue* (1892), no. 184 = Espagnol 132, pp. 70-72. https://archive.org/details/cataloguedesmanu00bibl_0 | Text file | arts. 10-16: "Sept lettres ... En partie chiffrées", no content. Decipherments are noted only for art. 78 (f. 169, 22 January 1579) and art. 81 (f. 177). Art. 87 (f. 193, clear copy): Philip II "à «Pedro de Arcauti», au sujet du règlement de divers comptes". |
| *La Batalla del Mar Océano*, vol. I. https://archive.org/details/aa.-vv.-la-batalla-del-mar-oceano-2.-vol.-ii-2017_202310 | Text file, words "Stucley", "Estucley", "Palam" | Stukeley documents of 1570-1571 only. |
| archive.org full text (covers the CODOIN volumes that are there) | "desasosegarla por esta via"; "dexasse la agena"; "Estucley" "Palamos" 1578; "Stucley" "veinte mil escudos"; "regalo al secretario Villeroy"; "Vargas Mexia" Stucley Villeroy 1578 | No text of the letter. |
| Google Books (search page) | "Vargas Mexía" Stucley Palamós "veinte mil escudos"; Stukeley Palamós 1578 "Vargas" "20,000"; "quitar la leche de las amas"; "quatrumvirato" Vargas Mexía Pérez 1578 | No hit. |
| Gallica SRU | `text adj "Stucley" and text adj "Palamos" and text adj "Vargas"` | 0 records. |
| *História e Memórias da Academia das Sciências de Lisboa*, n.s., vol. XIV (1922), pp. 421-422. https://archive.org/details/historiaememoria14acaduoft | Text file | "Felipe, apesar de receoso da empresa, contribuiu com 20:000 escudos". The sum is common knowledge in the Stukeley literature. |

### Findings (f. 26r)

The Vatican side tells the same story, with more detail:

- CSP Rome 2, no. 770 (pp. 389-391), nuncio Sega to the cardinal of Como, Madrid, 22 March 1578: "they know not that it is his Majesty that dispenses the bounty, for all the moneys have been disbursed upon my account ... the paymaster, who is the bearer of the 20,000 crowns, and who departed on the 20th inst. ... his Majesty being minded that I should be the mainspring of all the business ... in order that he may reveal himself in nothing". The 20,000 crowns are "for the hire of 1,000 foot and 400 horse" in Ireland. The paymaster is Oberto Spinola. The same letter says that the haste was made "notwithstanding that from Paris by letters of Juan de Vargas ... it is understood that the Queen of England's ambassador ... had ... tidings of Stucley's departure".
- No. 779 (p. 397), Como to Sega, 4 April: "As to Stucley, if his Majesty has given him the 20,000 crowns of which you speak ...".
- No. 807 (pp. 417-418), 27 April: the Pope is pleased that the King takes part "by giving in aid thereof the 20,000 crowns which he has sent them".
- No. 824 (pp. 427-428), May: Sega proposes that "of the 20,000 crowns there might be spent 5,000" on the ship.

Comparison with our reading:

- Agreements: "veynte mill escudos en oro" = 20,000 crowns; "con persona propria, secretamente" = the paymaster Spinola and the King's wish to stay hidden; "alguna infanteria y cavalleria que pensava levantar en Yrlanda" = "1,000 foot and 400 horse"; "lo que me escrivis cerca de la yda de Stucley" = the letters of Vargas that Sega names; "Palamós" = letters dated "14 Feb., 1578. Porto Palamos" (CSP Rome 2, pp. 381 and 383).
- Date: the paymaster left on 20 March; the BnF notice gives 16-17 March for these letters. The docket "16 de março de 1578" fits.
- New in our text, not found in print: the King's own words on his motive ("desassossegarla por esta via ... dexasse la agena"), his statement that he had no part in the Pope's ship, and the order to Vargas to keep the secret. The Villeroy paragraph is named in Paz ("y Secretario Villerroi").
- The rest of the letter (ff. 26v-27, not online) is in Simancas K 1556 as a minute.

### Findings (Pérez letters): names that the Simancas catalogue can fix

- "Arcauti": Paz has "Pedro de Arcanti" (index "Arcanti (Pedro)": pp. 888, 898; also p. 900) and once "Pablo de Arcauti" (p. 884). Morel-Fatio read "Pedro de Arcauti" on f. 193. He is the accounts officer in Paris ("Arreglo de las cuentas de Curiel que hacía Pedro de Arcanti", K 1556, 1579). The reading with u or with n stays open; the person is certain.
- "Capelo" = Isoardo Capelo; "Curiel" = Alonso Curiel (both write to Vargas in K 1545, K 1546).
- "don Alonso de Sotomayor": K 1545 (1578): "Conveniencia de tratar con los Guisas por medio de D. Alonso de Sotomayor de palabra y no por escrito"; K 1556 (1579): "Llegada a París de D. Alonso de Sotomayor".
- "padre Avila" (f. 179v): candidate "fray Francisco Vázquez de Avila", who writes "advertencias" on the embassy (K 1544, p. 883) and letters in K 1552-53 and K 1557 (p. 900). Not proved.
- "Nazareth": "Arzobispo de Nazareth" among the correspondents of K 1545. "Mos de la Mota" = M. de la Motte (Gravelines), many entries.

### Not reached

- G. Marañón, *Antonio Pérez*: no full text. Only the Google Books phrase search (no hit).
- The CODOIN volumes were searched only through the archive.org full text, not by index.
- Z. N. Brooke (EHR 1913) and J. E. Tazón (2003): not opened. They rest on the Vatican papers that the Calendar prints.
- Simancas K 1556 itself (PARES): not opened.

---

