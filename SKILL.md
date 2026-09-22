---
name: revise-paper-draft
description: Systematically diagnose, revise, and verify academic paper drafts through claim-evidence alignment, logical structure, reproducibility, figure storytelling, calibrated discussion, concise abstracts, and citation integrity. Use when the user asks to revise, polish, restructure, shorten, strengthen, or pre-submission-check a manuscript or a section such as the Introduction, Methods, Results, Discussion, Abstract, figures, captions, contributions, or references; especially suitable for engineering, mechanics, robotics, simulation, parameter-identification, optimization, and reliability papers.
---

# Revise Paper Draft

Revise a manuscript as an evidence-bearing scientific argument, not merely as polished prose. Preserve the author's technical meaning, notation, numerical values, and intended contribution while improving logic, clarity, reproducibility, and claim strength.

## Select the revision mode

Infer the mode from the request. Ask only when the missing choice would materially change the deliverable.

- **Diagnostic:** identify problems and prescribe fixes without rewriting the full text.
- **Targeted revision:** revise the requested paragraph, section, figure caption, or response.
- **Full-draft revision:** diagnose the paper globally, then revise section by section.
- **Pre-submission audit:** check internal consistency, evidence boundaries, reproducibility, figures, citations, and venue compliance.
- **Reviewer response:** use only when explicitly requested; answer comments point by point and permit respectful evidence-based disagreement.

If the user provides a document file and requests edits to that file, use the applicable document or PDF workflow as well. Preserve formatting and tracked changes when requested.

## Establish the evidence boundary

Before revising, identify:

1. Research question and manuscript type.
2. Target venue or style, if supplied.
3. Completed experiments, simulations, analyses, and available figures.
4. Statements that are observed, inferred, proposed, or unsupported.
5. The requested revision scope and output language.

Never invent experiments, data, parameter values, statistical significance, citations, DOIs, software settings, novelty, or validation. Do not convert planned work into completed work. Flag consequential missing evidence with a concrete action rather than filling the gap rhetorically.

## Apply the revision workflow

### 1. Form the central claim

Express the paper's main contribution in one falsifiable sentence. Then identify its boundary conditions. If this cannot be done from the draft, report the ambiguity before extensive rewriting.

### 2. Build a claim-evidence matrix

Map each major claim to:

- supporting figure, table, equation, experiment, simulation, or citation;
- relevant baseline or comparator;
- quantitative metric;
- applicable conditions;
- evidence gap or required revision.

Remove, soften, or label any claim without adequate support. Preserve legitimate uncertainty.

### 3. Repair the logical skeleton

Check that the paper follows this dependency:

`problem -> gap -> research question -> method -> evidence -> interpretation -> boundary -> contribution`

Verify that every Introduction promise is answered later and every conclusion is supported earlier. Reorder content when local sentence polishing cannot repair the argument.

### 4. Revise sections by scientific function

Read [references/revision-rubric.md](references/revision-rubric.md) when revising manuscript sections, figures, references, or reviewer responses. Do not force a fixed paragraph count; use the rubric as a functional test.

For mechanics, robotics, simulation, parameter identification, optimization, or reliability research, also read [references/engineering-robotics.md](references/engineering-robotics.md).

### 5. Rewrite at the requested scope

- Lead with the revised text when the user asks for a direct rewrite.
- Preserve symbols, units, equation numbering, factual values, and citation placeholders.
- Replace vague praise such as "good performance" with the available metric and condition.
- Distinguish correlation, prediction, explanation, and causation.
- Avoid inflated novelty words unless the literature search and evidence justify them.
- Use restrained academic language and coherent transitions; do not erase necessary technical terminology.

### 6. Verify the revision

Check at minimum:

- negation and causal meaning;
- numbers, units, percentages, and denominator consistency;
- equations, symbols, abbreviations, and terminology;
- method-result alignment;
- figure-text and table-text consistency;
- abstract-body and conclusion-body consistency;
- novelty and generalization boundaries;
- citation existence and actual support when sources are available.

When sources or target-journal rules must be checked and have not been supplied, retrieve authoritative sources rather than guessing.

## Return an actionable deliverable

Adapt the level of detail to the request. For a full revision, use this order:

1. **Overall diagnosis:** one paragraph stating the paper's current strength and central weakness.
2. **Priority issues:** a table with severity, location, issue, scientific impact, action, and confidence from 0.00 to 1.00.
3. **Revised manuscript text:** complete revised passages, not only suggestions.
4. **Claim-evidence matrix:** include unsupported and overextended claims.
5. **Outstanding work:** list only evidence, analysis, or source checks still needed.
6. **Verification note:** summarize what was preserved and what could not be verified.

For a targeted revision, return the revised passage first, followed by only material changes and unresolved scientific ambiguities.

## Respect scope and author judgment

Do not transform a language-edit request into an unsolicited whole-paper audit unless a local change exposes a material scientific inconsistency. Offer alternatives when a revision changes claim strength. The author retains final scientific judgment.
