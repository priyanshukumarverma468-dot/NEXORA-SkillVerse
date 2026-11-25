# Agent compatibility

## Canonical format

Each guide is plain Markdown at `skills/<category>/<skill>/SKILL.md` with a name, description, workflow and safety boundaries. This makes the content readable by humans and portable to assistants that accept attached or pasted task context.

The repository does **not** assume all AI agents share an automatic skill-discovery protocol, frontmatter schema, file location, tool permissions or context window. Confirm the target agent's official, current instructions before installation. Metadata fields beyond `name` and `description` may be ignored by some agents.

## Use without native skills support

Open the relevant guide and include its contents in the task context. Ask the agent to follow its workflow, preserve its security constraints and report checklist evidence. For large guides, provide only the guide relevant to the current task.

## Install where a skills directory is supported

Use the target agent's documented directory and the included installer, for example:

```sh
python scripts/install_skill.py video-editing/ffmpeg --destination <documented-agent-skills-directory>
```

The installer copies the unchanged `SKILL.md` beneath the selected destination. It does not configure or claim compatibility with any particular agent. Review and test discovery in the target agent.

## Adapter guidance

If an agent requires a different format, create a thin adapter that points to or faithfully carries the canonical guide's workflow and safety rules. Keep the canonical `SKILL.md` as source of truth. Do not weaken approval, authorization, privacy, cost or verification constraints to fit an agent's tool behavior.

## Tested compatibility

Repository tests validate Markdown structure and local links, not automatic loading by proprietary agents. Native discovery has not been independently tested across ChatGPT, Claude, Gemini, Cursor or VS Code; their support and file conventions may change.
