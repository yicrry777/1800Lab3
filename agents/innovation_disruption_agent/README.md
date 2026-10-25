# Week 5 / Assignment 3 — Innovation and Disruption Agent

This is a specialist of the unchanged MASY1800 scaffold. Its decision rules are in `specialist_instructions.md`; no code under `core/` or shared input/output contract was changed. The three cases are explicitly fictional teaching scenarios, so organization economics are assumptions rather than discovered company facts.

## Run the course workflow

From the repository root:

```sh
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/innovation_disruption_agent --case agents/innovation_disruption_agent/cases/primary.json
python3 tools/build_prompt.py --agent agents/innovation_disruption_agent --case agents/innovation_disruption_agent/cases/contrast_1.json
python3 tools/build_prompt.py --agent agents/innovation_disruption_agent --case agents/innovation_disruption_agent/cases/contrast_2.json
python3 tools/validate_response.py agents/innovation_disruption_agent/responses/primary_response.json
python3 tools/validate_response.py agents/innovation_disruption_agent/responses/contrast_1_response.json
python3 tools/validate_response.py agents/innovation_disruption_agent/responses/contrast_2_response.json
python3 -m unittest discover -s agents/innovation_disruption_agent/tests -v
```

The prompt builder writes packets under ignored `work/`. ChatGPT/Codex generated and critically revised the representative JSON outputs; the scaffold does not run an API or independently reproduce model wording. The saved tests verify the frozen output shape and the intended context contrast. They do not prove performance on arbitrary new cases.

## Test result and revision evidence

| Trial | Business-model judgment | Reason |
| --- | --- | --- |
| Primary: hourly-billed outsourced support | High, conditional | Potential pressure on a core revenue unit; contract, margin, and pilot effects remain unknown. |
| Contrast 1: internal manufacturer warranty desk | Low, conditional | Support is a cost center; product sales remain the revenue unit. |
| Contrast 2: mixed-pricing outsourced support | Moderate, provisional; High plausible | Missing contract and margin split prevents a firm severity call. |

The same technology and application appear in all three cases. Their saved `general_et_finding` and `application_finding` are identical by design; organizational business-model exposure changes. `responses/primary_pre_revision_weak.json` is the preserved failed trial. It passed JSON validation but incorrectly inferred certain existential disruption from hourly-revenue exposure. `records/pre_revision_diagnosis.md` explains the failure; version 1.0 instructions require an explicit exposure-to-outcome mechanism, a competing interpretation, and discriminating evidence.

## Evidence and integration note

Conceptual criteria come from the instructor's Chapter 5 (provided separately with the course materials) and the [OECD/Eurostat Oslo Manual 2018](https://www.oecd.org/en/publications/oslo-manual-2018_9789264304604-en/full-report/component-9.html). Technical-origin evidence comes from the [2017 Transformer paper](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf). The [NBER customer-support field study](https://www.nber.org/papers/w31161) supports the possibility of agent-assist productivity gains in its observed setting, not a forecast for these fictional firms. The [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) supports bounded risk review, not the severity label. Sources checked 2026-10-12.

For team integration, preserve the separation between technical novelty, application workflow change, and business-model impact. A breakthrough technology can support an incremental local workflow; neither label alone establishes creative destruction. Promethean significance, diffusion, adoption timing, readiness, and current competitor mapping belong to the other specialists.
