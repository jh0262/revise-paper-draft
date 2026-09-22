# Manuscript revision rubric

Use only the sections relevant to the user's request.

## Introduction

Test the Introduction by function:

1. **Consensus:** establish the accepted phenomenon or engineering need.
2. **Gap:** identify a specific unresolved limitation, not merely that few studies exist.
3. **Consequence:** explain why the gap affects theory, prediction, design, safety, cost, or deployment.
4. **Response:** state the research question, approach, evidence, and contributions.

Prefer synthesis over author-by-author lists. Group literature by assumptions, methods, evidence, or limitations. Ensure the stated gap is supported by inspected literature and is exactly the gap addressed by the paper.

Reject these patterns:

- citations listed without comparison;
- novelty asserted only with "few studies";
- a broad gap followed by a narrow method with no bridge;
- contributions described as routine workflow steps;
- "first" or "unprecedented" without comprehensive support.

## Figures and tables

Give each main figure one principal claim. Write its intended takeaway before revising the graphic or caption.

Check:

- visual hierarchy makes the comparison obvious;
- identical variables retain identical encodings across figures;
- baseline or control is visually subordinate but legible;
- axes, units, uncertainty, sample size, and statistical marks are defined;
- captions explain what, conditions, encodings, and takeaway without reproducing the Results section;
- secondary sweeps and diagnostic plots move to supplementary material when appropriate.

Do not claim that a figure must be understandable with literally no text. Require it to remain interpretable with the axes, legend, and caption.

## Methods

Write Methods as a reproducible protocol. Specify the information necessary to repeat the work, including materials or systems, parameter sources, boundary and initial conditions, instrumentation, calibration, software versions, solver settings, algorithms, stopping criteria, random seeds, data splits, metrics, and uncertainty treatment as applicable.

Separate:

- measured parameters from assumed parameters;
- identified parameters from fixed parameters;
- training or calibration cases from validation cases;
- exploratory choices from preregistered or predefined choices;
- primary analysis from sensitivity or robustness analysis.

State code and data availability accurately. Do not imply that all journals require full public release or that restricted data imply misconduct. When public release is impossible, describe the restriction and provide the most reproducible lawful alternative.

## Results

Organize Results by research question or claim, not by the chronological order of experiments. For each unit:

1. state the question or comparison;
2. report the result with metric and condition;
3. direct the reader to the figure or table;
4. state the immediate inference without extended speculation.

Report absolute values alongside relative improvements when meaningful. Identify the baseline, uncertainty, sample size, and statistical or engineering significance. Do not hide negative or mixed results that alter the main claim.

## Discussion

Use this five-move structure as needed:

1. summarize the central finding with quantitative evidence;
2. explain the plausible mechanism;
3. compare agreements with prior work;
4. explain disagreements and alternative interpretations;
5. define limitations, applicability, and implications.

Create intellectual tension only when the evidence supports it. Agreement with prior work is legitimate when it clarifies external validity. Do not repeat the Results section or exaggerate a mechanism that was not directly tested.

## Abstract

Build a self-contained abstract from:

1. one sentence of context;
2. one sentence defining the gap;
3. one or two sentences describing the approach;
4. one or two sentences stating the most important quantitative findings;
5. one sentence defining the contribution or implication.

Adapt length and structure to the venue. Prefer specific results over generic claims such as "important theoretical and practical value." Limit repeated self-reference, but do not apply a universal ban on "we," "this study," or "this paper."

## Conclusion

Answer the research question without introducing new evidence. State the contribution, strongest result, applicable conditions, and next research need. Do not duplicate the abstract or expand the scope beyond the validated cases.

## References

Build a functional citation set containing, where relevant:

- foundational work;
- recent representative work;
- the closest competing approaches;
- conflicting or boundary-setting evidence;
- sources for methods, datasets, metrics, and models.

Judge a source by relevance, originality, methodological quality, and support for the local claim—not by journal prestige alone. Verify bibliographic details and whether each source actually supports the sentence citing it.

## Reviewer responses

Use only when requested. For each comment:

1. reproduce or precisely identify the comment;
2. thank the reviewer without excessive flattery;
3. state whether the manuscript was changed;
4. explain the action and scientific rationale;
5. give exact section, page, line, figure, or table locations;
6. quote the revised passage briefly when helpful.

If disagreeing, remain respectful and support the position with analysis, data, or authoritative literature. Follow the venue's revision-marking instructions rather than applying highlighting automatically.

## Claim-strength calibration

Use verbs consistent with evidence:

| Evidence supports | Prefer | Avoid unless directly established |
|---|---|---|
| association | is associated with, correlates with | causes, determines |
| predictive performance | predicts, estimates | explains the mechanism |
| simulation agreement | reproduces, agrees under tested conditions | proves universal validity |
| controlled mechanism test | supports, demonstrates within conditions | definitively establishes |
| limited cases | is effective in the tested cases | is generally applicable |

## Full-revision issue levels

- **Critical:** invalidates the central claim, evidence chain, method, or reproducibility.
- **Major:** materially weakens interpretation, novelty, comparison, or generalization.
- **Moderate:** obscures logic, metrics, conditions, or figure meaning.
- **Minor:** local wording, notation, formatting, or style issue.

