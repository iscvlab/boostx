---
name: planx
description: >
  Custom implementation planner (/planx, /plan). Use when the user requests an implementation plan,
  constructing implementation_plan.md with inline structured grilling questions, options, recommendations,
  and doc references without asking questions directly in the chat.
  Do NOT use for direct code execution (/boostx) or documentation sync (/syncx).
---

# Custom Implementation Planner (`/planx`)

When triggered (e.g. by `/planx`, `/plan`, or "create implementation plan"), you must follow this behavior:

## 1. No Direct Questions in Chat
- Do **NOT** ask clarifying questions directly in the agent chat.
- All questions, uncertainties, or design decisions must be written directly inside the `implementation_plan.md` artifact.

## 2. Structured Questions in the Plan
- In the **Open Questions** or **User Review Required** sections of the `implementation_plan.md` artifact, structure every inquiry as follows:
  - **Question / Decision Point**: Explain the challenge or ambiguity.
  - **Options**: Enumerate the possible paths/options (e.g., Option A, Option B).
  - **Recommendation**: Highlight a specific recommended choice (prefixing with `(Recommended)`) and explain the rationale.
  - **Doc/File References**: Reference relevant project guidelines (e.g. project protocol docs, design guidelines) or local code symbols/files.

## 3. Planning Workflow Conformance
- Save the plan as `implementation_plan.md` in the current conversation artifacts directory: `<appDataDir>/brain/<conversation-id>/implementation_plan.md`.
- Set `RequestFeedback = true` and `UserFacing = true` in the `ArtifactMetadata` of the tool call.
- Do not re-summarize the plan in the chat. Tell the user the plan is ready for their review and options selection.
