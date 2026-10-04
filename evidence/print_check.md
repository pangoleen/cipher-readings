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


## 1. The viceroy of Sicily to King Ferdinand, Messina, 27 April 1503 (BnF Espagnol 318, no. 94)

**Verdict: content known in part (Zurita used the same correspondence), text not found. The original key is listed in print and is not printed.**

### Sources searched

| Source | Search | Result |
|---|---|---|
| Morel-Fatio, *Catalogue des manuscrits espagnols et des manuscrits portugais* (1892), no. 172 = Espagnol 318. https://archive.org/details/cataloguedesmanu00bibl_0 | Text file, words "chiffr", "vice-roi", "Lanuza" | p. 63, art. 94: "(Fol. 120-121.) Lettre en chiffre du vice-roi de Sicile au Roi Catholique. Messine, 27 avril 1503." No decipherment and no copy is noted. Other articles of the same volume have the note "en partie chiffrée"; none has "déchiffrement". |
| RAH, *Catálogo de la Colección Salazar y Castro* (text of the 49 volumes). https://archive.org/details/salazary-castro-22-nov-2016 | Text file (31 MB), words "Lanuza", "virrey de Sicilia", "visorrey", "Joya", "Andrada", "Cardona", "Calabria", "descifr", all dates 1503.03-05 | No decipherment and no copy of the letter of 27 April. Related entries found (see Findings). |
| Zurita, *Historia del rey don Hernando*, book V, ch. XXV and XXIX. https://archive.org/details/HistoriaDelReyDonFernandoElCatlico.DeLasEmpresasYLigasDeItalia | Text file, read ch. XXV in full and the end of ch. XXIX | Narrative that agrees with the letter in several points. No text of the letter. See the comparison. |
| Rodríguez Villa (ed.), *Crónicas del Gran Capitán* (1908). https://archive.org/details/crnicasdelgran00rodruoft | Text file, words "Joya", "Lanuza", "Cardona" | The battle and the taking of Gioia only ("les entraron por fuerza de armas y los despojaron y prendieron"). Nothing on the sack of the fortress or on don Hugo's disobedience. |
| Bergenroth, *Calendar of State Papers, Spain*, vol. 1: April and May 1503. https://www.british-history.ac.uk/cal-state-papers/spain/vol1/pp294-305 and `/pp305-306` | Page text, words "Sicil", "Lanuza", "viceroy", "Messina", "Aubign" | No entry. |
| Bergenroth, vol. 1, Introduction, "Remarks on the ciphered despatches". https://www.british-history.ac.uk/cal-state-papers/spain/vol1/lxxiii-cxlvi | Page text, words "viceroy", "Sicily", "key" | He names the keys of De Puebla and of Don Pedro de Ayala. He does not name a key of the viceroy of Sicily. |
| J. C. Galende Díaz, "La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V", *Cuadernos de Estudios Medievales* 18-19 (1993-94), pp. 159-178. https://digibug.ugr.es/handle/10481/30410 | PDF text | pp. 165-166: he lists the 12 keys of RAH 9/15, first "Cifra del visorrey (folios 1 a 6)". His appendix prints seven keys (documents 1-7: general cipher, Mauleón, two of Juan Manuel, Ruiz de Medina, the archbishop of Zaragoza, Medina Sidonia). The key of the viceroy has no note "ver documento": **it is listed, not printed.** |
| L. de Torre and R. Rodríguez Pascual, "Cartas y documentos relativos al Gran Capitán", *Revista de Archivos* vols. 34, 39, 44 on archive.org (`revistadearchivo34spaiuoft`, `revistadearchivo39spaiuoft`, `revistadearchivosbibliote44`) | Text files, words "Lanuza", "visorrey de Sicilia", "Joya" | No letter of the viceroy. The series prints letters of the Great Captain (vol. 34 is at 1500, vol. 44 at 1510). |
| archive.org full text | "Hugo de Cardona" Joya "Fernando de Andrada" Aubeni saco fortaleza; "fortaleza de Joya"; "saco de Joya"; "Joan de Vintemilla" Andrada Cardona; "don Ugo de Cardona" "Revista de archivos" 1503 | Only Zurita, Mariana (after Zurita) and the Crónicas. No printed letter. |
| Gallica SRU | `text adj "Hugo de Cardona" and text adj "Joya" and text adj "Andrada"` | 1 record (Ticknor, history of literature). Not relevant. |

### Findings

1. **Archive guide.** The RAH catalogue has no entry for this letter. It has the letters around it:
   - Salazar A-11, f. 373: "1503.04.26. Mesina. Carta de Juan de Lanuza, virrey de Sicilia, al secretario Miguel Pérez de Almazán, rogándole remitiese a Fernando el Católico la carta que le enviaba para él. Original." This is probably the cover letter of our letter (dated one day later) or of its first draft.
   - A-11, f. 347: "1503.04.15. Mesina. Carta de Juan de Lanuza ... a los Reyes Católicos ... su sentimiento por la muerte de Portocarrero ..."
   - A-8, ff. 45-46: Manuel de Benavides to Almazán, "(1503).04.22. Foya" [Joya], on the victory; A-8, ff. 30-31: Benavides to the Monarchs, "Sobre la Roca de Anguito", 29 April [1503].
   - A-11, ff. 351-353: undated "Fragmento de carta de Hugo de Moncada [sic] y de Juan de Cardona a Fernando el Católico ... la ocupación de Calabria".
   - A-15, ff. 1-6: "Cifra del visorrey." (same shelf as RAH 9/15).
2. **Zurita knew the matter**, most probably from the viceroy's letters. He does not print them.

### Comparison of our reading with Zurita (book V, ch. XXV; ch. XXIX)

Agreements (they support our reading):

- Our "Ferando de Valencia" who goes to court = Zurita: the captains "le enviaron a Hernando de Valencia" (to the viceroy).
- Our "contador Alonso Guerero" = Zurita: "el visorey de Sicilia envió con Lope de Moxica, y Alonso Guerrero, veedores del campo".
- The command: Zurita: "el visorey confirmó la eleción que se hizo de la persona de don Hernando, con gran sentimiento, e indignación de don Hugo, y de don Juan de Cardona". Our items 6 and 7.
- Gioia: "fue puesto a saco, y quemado: y los que se retrajeron a la fortaleza, que eran más de cuatrocientos hombres ... diéronse a merced de las vidas: y hubieron allí seiscientos caballos, y cuatrocientas acémilas, y muy gran despojo." Our "dandose a merced", "pusieron a fuego", "bestias de cariage".
- "Había pasado a Mesina, después de la batalla, para verse con el visorey, don Hernando de Andrada." Our l. 3.
- "la Roca de Angito" = our "roqua de Angito".
- The mutiny of the foot for pay before the battle, stopped by "don Hugo de Cardona, y el conde de Condiano": our "desorden de los peones".

Differences and what can fill gaps:

- Zurita judges don Hugo well ("la gran cordura, y sufrimiento de don Hugo"). The viceroy's letter judges him badly. This is a difference of view, not of fact.
- Zurita does not have: the night sack of the fortress by men of don Hugo's company before the inventory; the empty chamber of d'Aubigny; the inquiry under oath; the three chief prisoners sent to the castle of Messina; "stuvieron para darle de punyaladas"; the "conde Joan de Vintemilla". These points have no printed parallel that I found.
- Possible fills: Zurita's "Lope de Moxica" (veedor, with Guerrero) is a candidate for a code word near "Alonso Guerero". His list of French prisoners has "Agrenni" (after "Bilcorte"): compare our "mosse de Grani" (?). Zurita (ch. XXIX) says the Great Captain complained that the viceroy "le daba demasiado favor, y alas" to Andrada: context for our item 6.

### Not reached

- A. de la Torre, *Documentos sobre relaciones internacionales de los Reyes Católicos*, vol. 6 (1966): not online. Not checked.
- Serrano y Pineda, "Correspondencia de los Reyes Católicos con el Gran Capitán" (*Revista de Archivos*, 1909-1913): only the archive.org full-text search (no hit for "don Ugo de Cardona" with "visorrey"). Not read page by page.
- *Revista de Archivos* vols. 35-38 (the 1501-1509 part of the Torre and Rodríguez Pascual series): the text file of vol. 35 did not download; vols. 36-38 not opened.
- The RAH originals (A-11 f. 373; A-15 ff. 1-6) were not seen.

---

