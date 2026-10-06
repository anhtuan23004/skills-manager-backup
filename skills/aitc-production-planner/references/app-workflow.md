# Build an app per the brief

Read only when the brief/user asks for an app, API, or interaction. Use together with the planner; this is execution guidance for the current agent.

1. From the requirements, write a short flow: user input → processing/AI → output → pass criteria. State which outputs need a demo, source, or deploy; add deploy only when the brief requires an online link, and when it does, create the task per [deploy-publisher](../../aitc-deploy-publisher/SKILL.md) from the first plan (get a skeleton onto a real link early, not at the end of the session).
2. Inspect the existing source first. Build a suitable interface: CLI for batch/scripts, Streamlit for a demo panel, FastAPI when an HTTP API is needed. A custom UI can still be built directly on the Gateway; do not force every frontend requirement into Streamlit.
3. Call the BTC Gateway API (BTC = the organizers) directly per the [API guide](../../../docs/api-guides/README.md) and [SKILL_EXECUTION](../../../docs/SKILL_EXECUTION.md). When a project already exists, integrate into the current code; when none exists, create the minimum needed to run the brief's flow.
4. In the execution-plan, each task has the file to change, the required behavior, and an observable test. Prefer one input → output flow working end to end before adding pages/features.
5. Use the exact payload/operation from the [API guide](../../../docs/api-guides/README.md). Keep the key and live permission server-side; never put the key in browser JS. Mock the transport in tests; do not auto-retry a paid POST.
6. Check the happy path, empty/invalid input, timeout/Gateway errors, and the output artifact. A UI must be run and operated in a real browser when the environment supports it; compiling does not replace a runtime/browser test. If a dependency is missing, record what remains unverified.
7. Hand over the run command, required configuration, test results, and remaining limitations. Reuse [final-qa](../../aitc-final-qa/SKILL.md) to match each requirement against evidence.

Do not add auth, a database, a queue, or a vector database just because the sample project has them. Choose them only when the requirements or the actual data/flow need them. The agent builds the necessary functions from the plan and the existing helpers.
