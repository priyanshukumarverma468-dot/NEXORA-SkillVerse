# Security policy

## Scope

Security reports may concern repository code, example integrations, unsafe agent workflows or accidentally exposed repository data. Skill instructions are not a substitute for a security assessment of the system where they are used.

## Reporting

Please use GitHub's private vulnerability reporting feature for this repository when available. If unavailable, contact the repository maintainers privately through GitHub. Do not open a public issue containing exploit details, credentials, personal information or a live target.

Include the affected file or commit, impact, prerequisites, reproduction evidence using a controlled environment, and any suggested mitigation. Allow maintainers reasonable time to investigate before public disclosure.

## Secret handling

- Never place real API keys, private certificates, signing keystores, passwords, phone numbers or production data in this repository.
- Revoke and rotate exposed credentials immediately; deleting a visible value from the latest commit does not remove it from history.
- The OpenRouter example reads its key from `OPENROUTER_API_KEY`; it must run only in a trusted environment.
- Test security and automation guidance only on systems you own or are explicitly authorized to assess.

## Supported versions

This repository has no continuously running service or guaranteed response-time SLA. Review current third-party product documentation and supported versions before production use.
