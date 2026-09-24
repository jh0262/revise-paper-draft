# Engineering and robotics revision checks

Apply this reference to mechanics, industrial robotics, finite-element simulation, multibody dynamics, control, parameter identification, optimization, reliability, and digital-twin papers. Select checks relevant to the claim and revision scope; do not demand every possible experiment for a local edit.

## Model definition

Check that the manuscript defines as applicable:

- mechanism or robot model, degrees of freedom, coordinate frames, and configuration;
- geometry, mass, center of mass, inertia, materials, and parameter sources;
- kinematic convention such as DH or POE and all sign conventions;
- rigid, flexible, friction, backlash, damping, and transmission assumptions;
- state variables, inputs, outputs, disturbances, constraints, and initial conditions;
- governing equations and the meaning and units of every symbol.

Require a reason for each major simplification and discuss its likely effect on the outputs. Report unresolved text/formula conflicts before proposing a substantive correction; do not silently change a sign or parameter.

## Simulation reproducibility

For finite-element, multibody, or coupled simulation, check:

- software and version;
- element or body formulation;
- contact, joint, constraint, load, and boundary definitions;
- material model and parameter source;
- mesh size and mesh-convergence evidence;
- modal truncation or model-reduction criterion;
- solver type, step size, tolerances, and convergence criterion;
- coupling direction, exchanged variables, synchronization, and interpolation;
- verification against an analytical case, independent solver, experiment, or benchmark.

Do not accept a visually plausible contour plot as validation by itself. A simulated test substructure or sensor signal is not a physical measurement merely because of its name.

## Experimental reproducibility

Check:

- specimen or robot configuration and payload;
- excitation trajectory, speed, acceleration, posture, and repetition count;
- sensors, range, accuracy, placement, mounting, calibration, and sampling frequency;
- synchronization, filtering, windowing, and preprocessing;
- environmental and operating conditions;
- uncertainty, repeatability, and error propagation;
- safety limits that constrain the tested operating envelope.

Separate numerical validation, hardware-in-the-loop, scaled prototypes, full-scale experiments, and field tests. Do not promote the evidence level during language editing.

## Parameter identification

Check:

- structural identifiability or practical identifiability rationale;
- excitation richness and parameter sensitivity;
- objective function and residual definition;
- parameter bounds, priors, constraints, and initial values;
- optimizer settings, random seeds, and termination criteria;
- calibration-validation separation;
- confidence intervals, covariance, sensitivity, or uncertainty estimates;
- residual structure and cross-condition validation.

Improved fitting error alone does not establish physically correct parameters. Population concentration does not alone establish proximity to an unknown true parameter.

## Optimization and surrogate modelling

Check:

- design variables, objectives, constraints, units, and feasible ranges;
- rationale for conflicting objectives;
- baseline algorithms and fair computational budgets;
- number of independent runs and randomness control;
- convergence, diversity, robustness, and computational-cost metrics;
- surrogate sampling strategy, validation set, prediction error, and update rule;
- Pareto-set decision rule and engineering feasibility of selected solutions;
- post-optimization reanalysis or experiment using the high-fidelity model.

Do not report only a visually better Pareto front. Seek quantitative evidence and repeatability appropriate to the claim. Use relevant [algorithm evidence checks](algorithm-evidence-audit.md) for archive, adaptive, RL, statistical, ablation, and complexity claims; use [Chinese algorithm writing](chinese-algorithm-writing.md) for Chinese prose.

## Reliability analysis

Check:

- random variables, distributions, dependence, and data basis;
- limit-state function and failure definition;
- sampling or approximation method and convergence;
- time dependence, load cases, and model uncertainty;
- reliability target and engineering interpretation;
- validation against direct simulation or sufficient sampling where feasible.

## Control and deployment boundaries

Distinguish offline tuning, online adaptation, and real-time execution. Timing claims need corresponding deadlines, measured latency, hardware, and operating conditions. An inverse-kinematics solver that avoids Jacobian inversion does not by itself eliminate physical singular configurations. Observed tracking improvement does not automatically establish global stability or safety.

## Recommended evidence sequence

Adapt rather than force this sequence:

1. problem mechanism and model assumptions;
2. modelling or identification workflow;
3. model verification and parameter validation;
4. comparison with baselines;
5. sensitivity or ablation analysis;
6. optimization or design result;
7. robustness, cross-condition, or experimental confirmation.

## Common overclaims

Flag and propose evidence-matched revisions for:

- treating a single robot posture as model-wide validation;
- treating simulation-experiment agreement at one load as general validity;
- equating lower prediction error with a correct physical mechanism;
- asserting fair optimizer superiority with unequal evaluations or one random run;
- treating random-seed repeatability as proof of noise, load, or parameter robustness;
- claiming a digital twin when the work only provides offline simulation;
- claiming real-time capability without measured latency and hardware conditions;
- claiming engineering deployability without constraints, safety, or computational cost.

## Code or algorithm additions

If the revision task expands into programming, control implementation, or algorithm code, present an Input/Output/Process analysis and flowchart logic before code. Keep proposed code separate from experimentally verified implementation.
