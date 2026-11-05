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

## What is in it

| Chapter | What it covers |
|---|---|
| 1 · Start with one assistant | Choose a private working folder and write a one-edit job contract |
| 2 · Connect it to your tools | Trace a search and fetch, inspect the SensAI Blender demo and choose a read-only starting point |
| 3 · Give it a memory | Build Small Worlds Gallery, compare two outputs, inspect a UE5 material override and test a restart |
| Homework | Build the fictional gallery, change one thing, restart the assistant |

## Things to Try

1. Open the deck and press **→** to step through it; chapter 1 opens on "Start With One Assistant."
2. Press **N** for speaker notes on any slide.
3. Open `index.html?notes` on a phone to use it as a presenter remote view.
4. Revisit “Find the actual recipe,” “Keep both versions” and “Follow the red material” to replay their diagrams. Reduced-motion and PDF views show the completed diagrams.
5. Try another look with `index.html?look=swiss` (browse them in `styles/index.html`).

## Credits

**Alex Coulombe Presents** · framework: [Spatial Deck](https://github.com/ibrews/spatial-deck). Class kit: ACP Second Brain.

The Blender example comes from [SensAI Hackademy](https://github.com/ibrews/sensai-2026-mcp-engines). The renderer comparison and material test come from [Data Interchange in UE5](https://github.com/ibrews/data-interchange-ue5-class).
