# LexicoGrammarPU-fr

**Automatic Detection of French Verbal Phraseological Units  
using Lexical and Lexico-Syntactic Approaches**

---

## 1. Overview

This repository accompanies a research project on the **automatic identification of French verbal phraseological units (PUs)**, with a particular focus on idiomatic expressions. The project proposes and compares a **lexical approach** and a **lexico-syntactic approach** for detecting PUs in large-scale corpora.

The methodology combines **curated lexicographic resources**, **morphosyntactic analysis**, and **dependency-based patterns**, drawing on the lexicon–grammar tradition and contemporary NLP tools. The code in this repository corresponds directly to the experiments and analyses described in the associated research article.

---

## 2. Scientific Contributions

This project makes the following contributions:

- A large-scale empirical study of French verbal idioms conducted on a corpus of approximately **15.8 million words**.
- The construction and use of a **validated reference list of 2,428 French verbal phraseological units**, derived from lexicographic resources developed at the **ATILF laboratory**.
- A systematic comparison between:
  - a **purely lexical detection approach**, and
  - a **lexico-syntactic approach** based on morphosyntactic patterns and dependency parsing.
- The integration of **spaCy** and **Stanza** to handle morphosyntactic variation and syntactic structure.
- An evaluation of the two approaches using **precision, recall, and F-measure (F1)**.

---

## 3. Theoretical Background

The project is grounded in:

- Lexicon–Grammar theory (Gross, 1975, 1982, 1996)
- Meaning–Text Theory (Mel’čuk, 2011, 2013)
- Phraseological research on fixedness, non-compositionality, and idiomaticity

Phraseological units are treated as lying on a **continuum of fixedness**, ranging from relatively free collocations to highly fixed idiomatic expressions.

---

## 4. Corpus

- **Source**: OPUS Wikipedia v1.0 (2018)
- **Language**: French
- **Size**: ~15.8 million words

To facilitate processing, the corpus was segmented into **200 chunks** of approximately equal size.

Relevant scripts:
- `chunks.py` – segmentation of large text files into chunks
- `convert_csv_to_txt.py` – conversion of CSV data into plain text format

---

## 5. Lexical Resources

- `atilf_source.csv`  
  Reference lexicographic resource developed at the **ATILF laboratory**, converted from XML to CSV format. This file constitutes the authoritative reference list of validated French verbal phraseological units used throughout the project.

- `idioms.txt`  
  Plain-text list of verbal idioms derived from the reference resource.

- `fp.csv`  
  Structured representation of phraseological units.

- `idioms_found_Atilf.txt`  
  List of idiomatic expressions detected in the corpus and matched against the ATILF reference list.

---

## 6. Methodology and Scripts

### 6.1 Lexical Approach

- `lexique_spacy_10.py`
- `lexique_spacy_50.py`

These scripts implement a **lexicon-based detection strategy** using spaCy. Idiomatic expressions are identified by matching corpus tokens against the reference list of phraseological units. This approach yields **high precision**, but limited recall due to its dependence on a closed lexicon.

---

### 6.2 Lexico-Syntactic Approach

- `syntaxe_verbes_noms10.py`
- `syntaxeverbe_noms_50.py`

These scripts implement a **lexico-syntactic detection strategy** based on:

- a predefined list of **pivot verbs** (e.g. *faire, mettre, prendre, casser*),
- thematic lexical classes (articles, comparison markers, etc.),
- dependency relations obtained through syntactic parsing.

Morphosyntactic patterns are encoded **directly in the scripts**, using combinations of target verbs, dependency relations, and contextual constraints (e.g. stoplists). This approach increases recall and enables the detection of idiomatic variants not explicitly listed in the lexicon, at the cost of increased noise.

---

### 6.3 Lexical Analysis of Pivot Verbs

- `verbefrequence.py`
- `frequence_verbes_fp.csv`

These files support a frequency-based analysis of verbs in the reference list of phraseological units. The results highlight highly productive verbs (e.g. *avoir, faire, mettre, prendre*), which play a central role in the formation of French verbal idioms and guide the design of syntactic patterns.

---

## 7. Evaluation

The evaluation focuses on comparing the **lexical** and **lexico-syntactic** approaches with respect to:

- **Precision**: proportion of detected candidates matching entries in the ATILF reference list.
- **Recall**: coverage of the reference list by the detected candidates.
- **F-measure (F1)**: harmonic mean of precision and recall.

Evaluation is conducted by matching detected candidates against the validated ATILF lexicon. The analysis does **not** distinguish between idiomatic and literal uses in context, as no manually annotated, context-sensitive gold standard is available. As a result, recall and F-measure are interpreted as indicators of **lexicon coverage** rather than full semantic disambiguation.

The results confirm a **complementary trade-off**:
- the lexical approach achieves very high precision but low recall,
- the lexico-syntactic approach substantially improves recall while introducing more false positives.

---

## 8. Repository Structure



LexicoGrammarPU-fr/
│
├── README.md
├── requirements.txt
│
├── atilf_source.csv
├── idioms.txt
├── fp.csv
├── frequence_verbes_fp.csv
├── idioms_found_Atilf.txt
│
├── chunks.py
├── convert_csv_to_txt.py
│
├── lexique_spacy_10.py
├── lexique_spacy_50.py
│
├── syntaxe_verbes_noms10.py
├── syntaxeverbe_noms_50.py
│
├── verbefrequence.py




---

## 9. Limitations and Future Work

- No distinction is currently made between idiomatic and literal uses in context.
- No comparison with supervised VMWE taggers (e.g. PARSEME) is provided.
- Future work will focus on:
  - post-processing filters (TF-IDF, PMI, embedding-based similarity),
  - dependency-pattern generalization,
  - extension to other corpora and languages.

---

## 10. License and Usage

This repository is intended for **research and academic use**.  
Please cite the associated article when using or adapting the code or resources.

## Author

**CHEN Lian (陈恋)**  
Affiliation: LLL University of Orleans & CRLAO-CNRS-INALCO
