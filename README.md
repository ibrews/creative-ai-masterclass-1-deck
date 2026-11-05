# Creative AI Workflow Masterclass, Part 1: Set Up From Scratch

**Alex Coulombe Presents · Thursday, November 5, 2026 · noon–2 p.m. Eastern.** Part 2, *Let It Run*, meets Wednesday, November 11 at 11 a.m. Eastern.

[Open the presentation](https://ibrews.github.io/creative-ai-masterclass-1-deck/) · [Read the self-paced student workbook](https://ibrews.github.io/creative-ai-masterclass-1-deck/classroom/start-here.html)

## Start here as a student

1. Open the Google Drive folder shared with your class. Download the **Small Worlds Workshop – Part 1 student kit – 2026-11-05.zip** file, then extract it. This is the same download for members and one-class students.
2. Inside **Small Worlds Workshop**, double-click **Start Here.html**. Its 19 steps include software download links, exact requests to paste into either desktop app, expected results, and recovery instructions. The workbook PDF in Drive is the printable edition.
3. Open the enclosing workshop folder as a local project in **Codex** or **Claude Desktop → Code**. The first steps guide you through installing one assistant, Python 3.11+, Blender and Godot 4 Standard. Android Studio is an optional follow-on.
4. Connect the local course library, quiz it on three workflows, install the two project skills, build and review your gallery, and check that a new conversation can resume. Then take the Paper City scene from Blender into a playable Godot exhibit. The assistant operates the build tools while you inspect the results.

The ZIP includes the ACP Second Brain reference kit, private working copies of the gallery and templates, the SW-17 exhibition brief, both skill folders, a Blender scene and builder, a Godot project, an Android Studio postcard project, and the offline slide deck with its recordings. The class Drive folder is the distribution point for the student kit.

## Teaching edition

The first six chapters follow the workbook. Begin software downloads early. A possible two-hour route gives 15 minutes to desktop setup, 15 to the second brain and retrieval quiz, 15 to skills, 25 to gallery work and restart, 35 to Blender and Godot, and 15 to review and questions. Students can defer Android, the original SensAI and Data Interchange demonstrations, and the technical MCP appendix. Unreal returns in Part 2.

## Things to Try

- Click **Open the self-paced workbook** on the cover, or open a specific step directly from a teaching slide. Each prompt is selectable and copyable in the workbook.
- Ask for the archive code and three tower heights. Check the answer against the local brief. Then test the restart recipe using a nickname you chose yourself.
- In Godot, orbit the city and reveal the wall label. Swap in your own jade-rail Blender export and repeat both checks.
- Use **→** to advance the presentation, **N** for speaker notes, or **G** for the grid. Append `?look=swiss` to try another look. Broadside is the default.

## Maintaining this fork

The presentation runs from `index.html` with bundled media and no build step. Course steps live in `classroom/lessons.json`; the matching core slides are baked into `SECTIONS`. The workbook generator is `tools/build_student_workbook.py`. Use `tools/export_pdf.py` for the slide PDF. The versioned workshop additions are under `classroom/Creative`, `classroom/Studio`, and `classroom/Skills`. The private release ZIP is supplied separately during student packaging.

Framework: [Spatial Deck](https://github.com/ibrews/spatial-deck). Reference demonstrations: [SensAI Hackademy](https://github.com/ibrews/sensai-2026-mcp-engines) and [Data Interchange in UE5](https://github.com/ibrews/data-interchange-ue5-class).
