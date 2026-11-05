# Creative AI Workflow Masterclass, Part 1: Set Up From Scratch

The slides for **Creative AI Workflow Masterclass, Part 1**, a live class by [Alex Coulombe Presents](https://alexcoulombepresents.com/classes/2026-11-04-creative-ai-masterclass-part-1) on Thursday, November 5, 2026, noon–2 p.m. ET. Use **ACP Second Brain** to find a reviewed recipe, build a local gallery, verify one edit and resume from private memory. The exercise requires Python 3.11+ and a terminal. Unreal, Blender and Godot are optional. Part 2 meets Wednesday, November 11 at 11 a.m. ET.

**▶ View the deck:** https://ibrews.github.io/creative-ai-masterclass-1-deck/

Built on [Spatial Deck](https://github.com/ibrews/spatial-deck), the single-file HTML presentation framework.

## Quickstart

```bash
git clone https://github.com/ibrews/creative-ai-masterclass-1-deck
cd creative-ai-masterclass-1-deck
python3 -m http.server 8750   # then open http://localhost:8750/
```

Open `index.html` directly to present offline. Broadside is the default look. Its typefaces, diagrams, animated plates and gallery screenshot ship with the deck. Edit the `SECTIONS` array near the top of `index.html`.

## Student quickstart

Sign in at the [ACP Second Brain member portal](https://alexcoulombepresents.com/members/second-brain) using the email associated with your membership or November class purchase. Download the ZIP and extract it. Open the folder containing `start-here`, `reference`, `examples` and `templates`. The commands below start in that folder. Keep your work in its sibling `class-work`. Use a fresh name if you already have a working copy.

**Mac or Linux (Bash or zsh).** In Terminal, type `cd` followed by a space, drag in the extracted folder or enter its quoted path, then press Return. Check for Python 3.11 or newer.

```sh
pwd
ls
python3 --version
mkdir ../class-work
cp -R examples/local-gallery ../class-work/
cp templates/{project-memory,job-contract,completion-receipt}.md ../class-work/
ls ../class-work
```

**Windows (PowerShell).** In File Explorer, open the extracted folder, type `powershell` in the address bar and press Enter.

```powershell
pwd
ls
py -3 --version
mkdir ../class-work
Copy-Item examples/local-gallery ../class-work/ -Recurse
Copy-Item templates/*.md ../class-work/
ls ../class-work
```

**Connect any file-reading assistant.** Start a new chat and attach `start-here/README.md`, `reference/support-matrix.md` and `start-here/private-project-memory.md`. If attachments are unavailable, paste the text with its relative path above it. Ask:

> Which course route can I use? Give the title, document ID and relative path of the reviewed memory recipe. Read only.

Match the answer to `Keep Private Project Memory`, `SB-01-memory` and `start-here/private-project-memory.md`. A file-only chat is enough. You can run every gallery command yourself.

**Build and inspect.** From the kit folder:

```sh
cd ../class-work/local-gallery
python3 build.py --output output
python3 verify.py --output output
```

On Windows use `py -3` instead of `python3`, or use `python` if that is your Python 3.11+ command. Look for `Checkpoint: 3/3 exhibits.` and `PASS: 3 exhibits`. Open the page with `open output/index.html` on macOS, `Start-Process ./output/index.html` in PowerShell or `xdg-open output/index.html` on Linux. Double-clicking the file also works. Record the verifier result and the three titles you see in the private `project-memory.md`. If a previous output folder is nonempty, keep it and choose the same fresh destination for build, verification and viewing.

### Optional read-only MCP connection

With a configured Claude Code CLI and `uv` on a supported POSIX system, open a **new terminal in the extracted kit folder**. The file-only route above also works without these tools.

```sh
KIT="$PWD"
uv sync --locked --extra dev
uv run acp-kit validate
```

Continue only if validation reports `"valid": true`. A hash or path failure requires a clean copy. Then run:

```sh
cd ../class-work
claude mcp add --scope local --transport stdio acp-second-brain -- uv run --project "$KIT" acp-kit serve
claude mcp get acp-second-brain
claude
```

In the client, inspect the server with `/mcp`. Ask it to search for private project memory, fetch the matching page and give the title, ID, review status and path. Compare the result with the actual page. The course server offers `search`, `fetch` and `status`. The deck screenshots show a rehearsal with Claude Code and a local model against the extracted course ZIP.

## What is in it

| Chapter | What it covers |
|---|---|
| 1 · Start with one assistant | Download and extract the kit, give a chat three files, build a private gallery and open the verified page |
| 2 · Connect it to your tools | Optionally register a local Claude Code connector, check its connection and verify a real search/fetch |
| 3 · Engine demos | Play the SensAI Unreal edit, Blender city orbit, Forage flythrough and megaplant experiment |
| 4 · Gallery lab | Build and inspect a baseline, edit a title, peer-review the result and recover an interrupted job |
| 5 · Export lab | Follow the USD composition and unit-conversion diagrams, diagnose a broken import and inspect the RealityKit recording |
| 6 · Memory | Write a receipt and challenge it in a fresh session |
| Homework | Build the fictional gallery, change one thing, restart the assistant |

The 62-slide teaching edition includes reserve material. One possible two-hour run gives 15 minutes to setup, 15 to connectors, 20 to engine demos, 25 to the gallery, 25 to export inspection, 15 to the restart exercise and 5 to questions. The engine demos are instructor-led. Learners can complete every gallery step with the course kit.

## Things to Try

1. Open the deck and press **→** to step through it; chapter 1 opens on "Start With One Assistant."
2. Press **N** for speaker notes on any slide.
3. Open `index.html?notes` on a phone to use it as a presenter remote view.
4. Revisit “Find the actual recipe,” “Keep both versions” and “Follow the red material” to replay their diagrams. Reduced-motion and PDF views show the completed diagrams.
5. Play or pause any of the five local demo clips with its video controls. Each recording has a still for the PDF.
6. Try another look with `index.html?look=swiss` (browse them in `styles/index.html`).

## Credits

**Alex Coulombe Presents** · framework: [Spatial Deck](https://github.com/ibrews/spatial-deck). Class kit: ACP Second Brain.

The four engine recordings, city and tree studies, and three diagrams are adapted from [SensAI Hackademy](https://github.com/ibrews/sensai-2026-mcp-engines). The simulator recording, export captures, three diagram sequences and observed material results come from [Data Interchange in UE5](https://github.com/ibrews/data-interchange-ue5-class).
