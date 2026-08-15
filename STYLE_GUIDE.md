# SHARED STYLE GUIDE — MPT Community Physiotherapy Notes

**This guide is BINDING for all 11 chapters. Every agent must follow it exactly so all PDFs look and read as one coherent set.**

## Audience & register
- Reader: postgraduate (MPT) physiotherapy students preparing 20-mark long-answer exam questions, authored for a community physiotherapy professor.
- Tone: academic, precise, evidence-based, exam-oriented. No filler, no padding, no repetition to inflate length.
- Every lettered sub-topic (a, b, c …) in a chapter is ONE 20-mark question and must be answered as a self-contained model answer of **8–12 dense pages**.

## File output
- Write ONLY GitHub-flavoured Markdown to: `chapters/chapter-XX.md` (zero-padded number, e.g. `chapter-01.md`).
- Do NOT generate PDF yourself — the coordinator converts all chapters centrally for consistent styling.
- UTF-8. Use real Markdown tables. Do not use raw HTML except `<div class="callout">…</div>` blocks defined below.

## Mandatory chapter skeleton
```
# Chapter N — <Chapter Title>

*MPT Community Physiotherapy · Long-Answer Model Notes*

<1–2 paragraph chapter overview + list of the questions covered>

---

## Q<letter>. <Full question text, phrased as an exam question — 20 marks>

### 1. Introduction & Definitions
### 2. Conceptual / Theoretical Framework
### 3. <Main body — one ### subheading per key dimension of the answer>
   (add as many ### subheadings as the topic needs; use tables & described diagrams)

<div class="callout callout-india">

**🇮🇳 Indian Context**
<policy, NHM/Ayushman Bharat/RCI/NCAHP, epidemiology, real Indian programmes & data>
</div>

<div class="callout callout-advance">

**🔬 Recent Advances (2020–2026)**
<latest evidence, guidelines, technology, systematic reviews>
</div>

### Exam Key Points (rapid revision)
- 6–10 crunched bullets a student can memorise.

### References
1. Vancouver/ICMJE numbered style (see below).

---
(repeat for every lettered question)
```

## Content requirements per question (non-negotiable)
1. **Definitions** anchored to authoritative sources (WHO, ICF, APTA, WCPT/World Physiotherapy, IAP, MCI/NMC, RCI, ICMR).
2. **Frameworks/models** named explicitly (e.g., ICF, PRECEDE-PROCEED, Health Belief Model, RE-AIM, Knowledge-to-Action, WHO Rehabilitation 2030).
3. At least **one Markdown table** where content is comparative or stepwise.
4. **Indian Context callout** — cite real Indian policy/programmes: NHM, Ayushman Bharat, HWCs/Ayushman Arogya Mandir, RCI Act, NCAHP Act 2021, National Programmes (NPCDCS/NP-NCD, NPHCE, RBSK, NPPCD), ICMR, state examples, DALY/GBD-India data. Use realistic figures; if unsure of an exact number, describe the trend rather than inventing a precise statistic.
5. **Recent Advances callout** — 2020–2026: tele-rehabilitation, digital health/ABDM, WHO Package of Interventions for Rehabilitation (PIR), recent Cochrane/systematic reviews, mHealth, AI, wearables — whatever fits the topic.
6. **References**: 8–15 per question, Vancouver numbered. Mix of WHO/UN docs, landmark textbooks, and journal articles. Format:
   `Author AA, Author BB. Title. Journal. Year;Vol(Issue):pages.` or for reports `WHO. Title. Geneva: WHO; Year.`
   Prefer genuinely well-known, verifiable sources (WHO reports, Cochrane reviews, landmark papers, standard PT textbooks — O'Sullivan, Kisner & Colby, Tidy's, WHO CBR Guidelines, WHO Rehabilitation in Health Systems). Do NOT fabricate DOIs or invent obscure papers; if uncertain, cite the authoritative body/textbook generically but correctly.

## Formatting rules (identical across chapters)
- H1 (`#`) only once (chapter title). Questions are H2 (`##`). Sections H3 (`###`). Sub-sections H4 (`####`).
- One blank line before/after every heading, list, table, and callout div.
- Callout divs: leave a blank line after the opening `<div>` and before the closing `</div>` so Markdown renders inside.
- Bold key terms on first use. Use tables, not ASCII art. Describe figures in prose as *"Figure: …"* italic captions.
- Separate each question with a horizontal rule `---`.
- British/Indian spelling (programme, organisation, paediatric).
- Do not include a "word count" or meta commentary in the output.

## Length discipline
- Target 8–12 pages per question **through substance, not padding**. If a topic is genuinely short, write a tight excellent answer rather than repeating yourself. Quality > page count.
