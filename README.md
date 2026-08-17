# rocket-fuel

Runs Claude and OpenAI Codex as co-founders on the Visionary/Integrator
operating system from *Rocket Fuel* by Gino Wickman and Mark C. Winters,
packaged as a [Claude Code Skill](https://code.claude.com/docs/en/skills).

Claude takes the Visionary seat: it interviews you, writes the plan, sets
the standards, and reviews the result. Codex takes the Integrator seat: it
filters the plan, kills scope creep, builds the code in its own sandbox,
and reports honestly. They argue in a bounded meeting until the verdict
line says `SAME PAGE`, and only then does anyone write code.

You make exactly three decisions per run: the interview answers, rare
deadlock tie-breaks, and the final commit. The skill guides you through
everything else.

## What is in here

```
skills/
  rocket-fuel/
    SKILL.md                 entry point: detects the mode, drives the run
    CODEX-INTEGRATOR.md      the invocation contract for every Codex call
    SAME-PAGE-MEETING.md     the adversarial plan-review loop
```

## Install

Requires the [Codex CLI](https://github.com/openai/codex) 0.130+:

```bash
npm i -g @openai/codex@latest && codex login   # ChatGPT account works, no API key
./install.sh
```

This symlinks `skills/rocket-fuel` into `~/.claude/skills/`, so updates
land with a `git pull`. Pass `--copy` for an independent copy, `--project`
to install at the project level instead of user level. Restart Claude Code
once after installing.

To install manually, copy `skills/rocket-fuel` into `~/.claude/skills/`
(user-level) or `.claude/skills/` (project-level).

## Use

One command, plain English. The skill picks the right mode from context:

| You say | You get |
|---|---|
| `/rocket-fuel build me a habit tracker` | Full kickoff: interview → adversarial plan review → Codex builds → verified |
| `/rocket-fuel this repo is a mess, clean it up` | Codebase audit → ranked issue list → you pick 3-7 fixes → build |
| `/rocket-fuel review PLAN.md` | Codex attacks your plan read-only until it approves |
| `/rocket-fuel have codex add dark mode` | One scoped task, built by Codex, diff-reviewed and proof-run |

From there the skill walks you through it: one interview question at a
time with a recommended answer attached, live verdicts from Codex each
round, and a clear prompt before anything is committed. The full argument
between the two models is saved to `SAME-PAGE-LOG.md` in your repo, next
to `PLAN.md`.

## Credits

Based on the Visionary/Integrator operating system from *Rocket Fuel* by
Gino Wickman and Mark C. Winters. Skill originally authored by
[@NulightJens](https://github.com/NulightJens/rocket-fuel-skill), MIT
License.
