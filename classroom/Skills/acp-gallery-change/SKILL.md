---
name: acp-gallery-change
description: Apply one approved gallery edit from a local exhibition brief, preserve the accepted baseline, verify the new build, and write a private receipt.
---
Read Studio/show-brief.md and Brain/workflows/part-1-exercise.md. Work only in Studio. Locate the baseline in Studio/local-gallery/output. If it is missing, ask the learner to finish the baseline step. If output-edited exists, preserve it and ask for a fresh destination. Ask for one approved field and value unless the request already supplies them.

For the SW-17 title task, change only the title of the exhibit whose ID is paper-city in Studio/local-gallery/exhibits.json. Keep JSON structure, IDs, order, accent and other text. Build using the existing build.py and an available Python 3.11+ interpreter with --output output-edited, working in Studio/local-gallery. Run verify.py against that same output. Stop on unexpected changes or after one failed correction. If the interpreter is unavailable, report what is missing.

In Studio/receipt.md record the source citation, changed field, output paths, actual verifier result and what still needs the learner's visual judgment. Preserve an existing receipt by appending a dated entry. Point to both index.html files. Leave the acceptance decision open until the learner inspects the page. Do not publish or install anything.
