# Skill catalog

Start with the [orchestrator](aitc-orchestrator/SKILL.md) and the [brief-based skill selection map](aitc-orchestrator/references/routing.md). Main flow: read the brief → plan with executable tasks → load the skills needed → produce output → verification. The table below is a lookup catalog, not 16 mandatory steps. Experience by brief type is kept separately in [topics/INDEX](../topics/INDEX.md) (lessons and base template) and the [2025 topic archive](../topics-archive-2025/INDEX.md).

Each task records its skill, helper/API guide, output file, and check per the [execution-plan](../templates/execution-plan.md). [How to run helpers](../docs/SKILL_EXECUTION.md) allows working directly in the workspace. The agent builds the app per the plan when the brief needs it; skills do not depend on installing FastAPI/Streamlit.

| ID and name | Open file | When to use |
|---|---|---|
| 00 — Exam orchestration | [aitc-orchestrator](aitc-orchestrator/SKILL.md) | Orchestrate the whole exam run when receiving a brief or when the next step is needed; choose skills by image, video, text, audio; control the two machines and time marks. |
| 01 — Brief decoding | [aitc-brief-decoder](aitc-brief-decoder/SKILL.md) | Analyze the verbatim brief, extract deliverables and rubric, state clearly what is undetermined; use as soon as the brief is opened and whenever BTC (the organizers) add requirements. |
| 02 — Concept and selection | [aitc-concept-choice](aitc-concept-choice/SKILL.md) | Propose and select a meaningful, distinctive, feasible concept for solving the brief; use after the brief is approved, before production. |
| 03 — Vietnamese context and content responsibility | [aitc-vietnam-context-review](aitc-vietnam-context-review/SKILL.md) | Review fit with Vietnam, public meaning, factual claims, symbols, and AI transparency; use when choosing a concept and before submitting media products. |
| 04 — Execution plan | [aitc-production-planner](aitc-production-planner/SKILL.md) | Tie each task to a skill/helper/output/check; has separate references for app and RAG when the brief needs them. |
| 05 — Text production | [aitc-text-producer](aitc-text-producer/SKILL.md) | Write scripts, content, or Vietnamese output text from the approved brief; use for text deliverables, voice-over, subtitles, or wording inside images/video. |
| 06 — Image direction | [aitc-image-director](aitc-image-director/SKILL.md) | Design the visual direction, prompts, and image checks per the brief; use for posters, key visuals, image sets, or frames for video. |
| 07 — Video direction | [aitc-video-director](aitc-video-director/SKILL.md) | Write shot prompts, generate video via the Gateway, track jobs, and maintain visual continuity; use when the brief requires video or moving segments. |
| 08 — Audio production | [aitc-audio-producer](aitc-audio-producer/SKILL.md) | Prepare narration, Vietnamese pronunciation, TTS/STT, and audio checks; use when the exam entry has voice-over or audio. |
| 09 — Output critique | [aitc-artifact-critic](aitc-artifact-critic/SKILL.md) | Critique drafts against the original brief and real viewing/listening evidence; use after each complete draft and before the final fix. |
| 10 — Incident handling | [aitc-systematic-debug](aitc-systematic-debug/SKILL.md) | Diagnose Gateway, file, export, or sync errors during the exam; use when a request fails, a clip cannot be downloaded, or output cannot be opened. |
| 11 — Final version check | [aitc-final-qa](aitc-final-qa/SKILL.md) | Check the submission against the requirements, actual files, and fresh evidence; use before freeze; does not replace checking by eye/ear. |
| 12 — Reflection and meaning | [aitc-solution-reflection](aitc-solution-reflection/SKILL.md) | Give an honest summary of how the brief was solved, the reasons for choices, and the meaning of the output to prepare the post-exam video; use when the final version is nearly stable, before T+120. |
| 13 — Freeze and submit | [aitc-submission-controller](aitc-submission-controller/SKILL.md) | Package, check against the manifest, and guide the submitter to meet the deadline; use after final QA and before/after the human's submit action. |
| 14 — Pre-exam toolkit evaluation | [aitc-toolkit-evaluator](aitc-toolkit-evaluator/SKILL.md) | Test skills, MCP, and the whole two-machine flow before exam day; use when preparing or changing the toolkit; do not run costly benchmarks during exam time. |
| 15 — Deploy and publish | [aitc-deploy-publisher](aitc-deploy-publisher/SKILL.md) | Put the web/game/app on an accessible link, check the live link, and prepare a fallback; use only when the brief requires an online-running product. |
