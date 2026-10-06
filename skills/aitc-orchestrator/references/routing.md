# Choose skills from the deliverable

Read this table when receiving a brief or when the brief changes the output. Paths in the table are relative to this file. A skill is an instruction for the current agent; it does not create extra agents/machines.

Common flow: [brief-decoder](../../aitc-brief-decoder/SKILL.md) → [production-planner](../../aitc-production-planner/SKILL.md) → the task's skill → [artifact-critic](../../aitc-artifact-critic/SKILL.md) → [final-qa](../../aitc-final-qa/SKILL.md). Use [concept-choice](../../aitc-concept-choice/SKILL.md) if a creative direction must be chosen; skip the selection step once the direction is locked.

| Output the brief requires | Execution skill / reference to read | Required helper/API | Evidence of pass |
|---|---|---|---|
| Article, summary, script | [text-producer](../../aitc-text-producer/SKILL.md) | [Text](../../../docs/api-guides/02-text-generation.md) | UTF-8 file; check content, length, sources |
| Poster or image set | [image-director](../../aitc-image-director/SKILL.md); text-producer when there is text | [Image](../../../docs/api-guides/03-image-generation.md) | View the actual image and check size/text |
| Video with narration | [video-director](../../aitc-video-director/SKILL.md), text-producer, [audio-producer](../../aitc-audio-producer/SKILL.md); image-director only when frames are needed | [Video](../../../docs/api-guides/04-video-generation.md), [TTS](../../../docs/api-guides/05-text-to-speech.md), FFprobe | Fully assembled MP4, duration, watched/listened to from start to end |
| Voice-over or transcript | [audio-producer](../../aitc-audio-producer/SKILL.md) | [TTS](../../../docs/api-guides/05-text-to-speech.md) / [STT](../../../docs/api-guides/06-speech-to-text.md) | Audio/transcript, proper names, listening-check time |
| Content that needs fresh information | [text-producer](../../aitc-text-producer/SKILL.md) | [Grounding](../../../docs/api-guides/07-web-grounding.md) | Real sources supporting each claim, lookup date |
| Document Q&A / semantic search | Planner with [RAG workflow](../../aitc-production-planner/references/rag-workflow.md), text-producer for answers | [Embedding](../../../docs/api-guides/08-embeddings.md) and Gateway text | Retrieves the correct source; questions outside the documents must not be fabricated |
| App, interactive demo, or API requested | Planner with [app workflow](../../aitc-production-planner/references/app-workflow.md), producers by function | BTC Gateway; build the UI as required | One user flow runs end to end and is tested as required |
| Web/game/app that judges must open or play via a link | As the row above, plus [deploy-publisher](../../aitc-deploy-publisher/SKILL.md) and [DEPLOY](../../../docs/DEPLOY.md) | Team VPS prepared in advance; [deploy-checklist](../../../templates/deploy-checklist.md) | URL opens from another machine, main flow runs on the live link, record URL + time + commit/hash |

Read [context-review](../../aitc-vietnam-context-review/SKILL.md) only when the content needs context/claim review; [debug](../../aitc-systematic-debug/SKILL.md) when an error occurs; [reflection](../../aitc-solution-reflection/SKILL.md) and [submission](../../aitc-submission-controller/SKILL.md) when reaching that step. When the brief type matches a topic (tourism website, educational game, financial report, legal infographic, comic, video news bulletin, flyer, podcast, song, marketing), read exactly one matching topic from [topics/INDEX](../../../topics/INDEX.md) or the [2025 archive](../../../topics-archive-2025/INDEX.md), and always apply [LESSONS](../../../topics/LESSONS.md). Do not load all 16 skills, the whole topic set, the whole guide set, or the GitHub source code at the start of the session.

## From plan to action

1. Lock the workspace and the minimum output that meets all requirements. Fill in the [execution-plan](../../../templates/execution-plan.md); a small task may use a short table in the same brief.
2. Open the SKILL.md of the first task, the guide for the exact operation, and [how to run helpers](../../../docs/SKILL_EXECUTION.md). Record the specific command/check in the plan.
3. If asked to execute, make one sample or one end-to-end flow, verify it for real, then expand. Load the next reference only when that task starts.
4. Continue with the chosen task after its check passes; fix locally on error. Clearly mark parts that have not been run live.

## Decision examples

- Submit a 300–350 word TXT: text + QA; do not scaffold an app. An agent already running through the Gateway can write it directly; do not call an extra LLM wrapper just to write the same piece.
- 60-second MP4 with narration: text → video scenes and TTS → assemble → QA. 60 seconds is the duration of the assembled cut, not a single 60-second video request.
- Q&A demo over 3 documents: verify that retrieval is needed → chunks with source IDs → embedding → retrieval → text with source citations → UI if the brief needs it.
