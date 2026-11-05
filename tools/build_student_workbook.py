#!/usr/bin/env python3
"""Render the offline student workbook using only the Python standard library."""

import argparse
import base64
from collections import defaultdict
from html import escape
import json
import mimetypes
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "classroom/lessons.json"
DEFAULT_OUTPUT = ROOT / "classroom/start-here.html"

# Captions describe each plate in context. Diagrams also have text alternatives.
CAPTIONS = {
    "how-brain": "Read the course recipes in Brain. Keep your own notes and outputs in Studio.",
    "invoke": "A recipe describes a command. You decide whether the assistant may run it.",
    "baseline": "The baseline opens with Paper City, followed by Moon Garden and Quiet Machine.",
    "edit": "In the edited gallery, the first card reads Paper City at Dusk.",
    "restart": "A restart note records the goal, accepted checkpoint, limits, next step and evidence.",
    "scene": "The starter scene has three cream towers and vermilion rails along the footbridge.",
    "make-scene": "Compare the jade rails with the starter render. The framing stays fixed.",
    "play": "The Godot visitor view includes two orbit controls and a wall-label button.",
    "handoff": "The revised visitor view carries the jade rails into Godot.",
    "phone": "Use this jade-rail postcard as the image in your Android project.",
    "next": "The workflow repeats: choose a recipe, agree on a job, make a change, inspect and save.",
}

STYLE = """
:root {
  --paper: #f7f1e4; --sheet: #fffaf0; --ink: #241e19; --muted: #564b40;
  --red: #9b3024; --faint: #d1c5b0; --display: Broadside, Georgia, serif;
  color-scheme: light; font-family: Book, Georgia, serif; color: var(--ink);
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--paper); font-size: 21px; line-height: 1.38; }
a { color: var(--red); text-decoration-thickness: 1px; text-underline-offset: .14em; }
a:hover { text-decoration-thickness: 2px; }
:focus-visible { outline: 3px solid #176375; outline-offset: 3px; }
p, h1, h2, h3, h4, figure, ol { margin: 0; }
h1, h2 { font-family: var(--display); font-weight: 400; line-height: 1.08; text-wrap: balance; }
h1 { font-size: clamp(3rem, 7vw, 6.7rem); letter-spacing: -.035em; }
h2 { font-size: clamp(1.85rem, 4vw, 3.5rem); letter-spacing: -.025em; }
h3 { font-size: 1.28em; line-height: 1.14; }
p, li, pre, code { overflow-wrap: anywhere; }
.skip { position: fixed; top: 0; left: 0; z-index: 5; transform: translateY(-150%); background: white; padding: .6em; }
.skip:focus { transform: none; }
main { width: min(1100px, 100%); margin: auto; padding: 24px clamp(18px, 5vw, 64px) 5rem; }
.cover, .lesson { border-top: 6px double var(--ink); padding-top: 12px; scroll-margin-top: 16px; }
.runhead { display: flex; flex-wrap: wrap; gap: 4px 1em; justify-content: space-between; align-items: baseline; }
.small, .runhead, figcaption, .stepnav, .button, .group-title, .toc a span {
  font-family: system-ui, sans-serif; font-size: .69em; line-height: 1.4;
}
.runhead, .small, .group-title { font-weight: 700; letter-spacing: .07em; text-transform: uppercase; }
.runhead .accent, .group-title, .small { color: var(--red); }
.cover-hero { display: grid; grid-template-columns: 1fr 41%; gap: 6%; align-items: center; margin: 42px 0; }
.cover-hero img { display: block; width: 100%; border: 1px solid var(--ink); }
.cover-hero h1 { margin: .16em 0 .22em; }
.deck { font-size: 1.24em; line-height: 1.24; color: var(--muted); }
figcaption { color: var(--muted); margin-top: .5em; }
.toc { border-block: 1px solid var(--ink); padding: 1rem 0 1.4rem; }
.toc-header { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; margin-bottom: .9em; }
.toc-header h2 { font-size: 1.6em; }
.toc-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .9em 1.3em; }
.group-title { margin: 0 0 .48em; }
.toc ol { list-style: none; padding: 0; }
.toc li + li { margin-top: .25em; }
.toc a { display: grid; grid-template-columns: 1.5em 1fr; gap: .25em; align-items: baseline; color: var(--ink); font-size: .95em; line-height: 1.15; }
.toc a span { color: var(--red); font-weight: 700; }
.button { background: var(--ink); color: var(--sheet); border: 1px solid var(--ink); padding: .55em .85em; cursor: pointer; font-weight: 600; }
.button:hover { background: var(--red); }
.lesson { margin-top: 4rem; }
.lesson-header { margin: 1.3em 0 1em; }
.lesson-header h2 { margin-bottom: .18em; }
.work { display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: 4%; align-items: start; }
.work ol { padding-left: 1.35em; }
.work li { padding-left: .15em; margin-bottom: .55em; }
.work li::marker { color: var(--red); font-weight: bold; }
.plate { background: #ede3ce; border: 1px solid var(--ink); padding: 1em; }
.plate pre { white-space: pre-wrap; font: .71em/1.62 ui-monospace, Menlo, Consolas, monospace; margin: 0; }
.illustration img { width: 100%; display: block; border: 1px solid var(--faint); }
.references { margin: .45em 0 0; display: flex; gap: .2em .8em; flex-wrap: wrap; font-size: .9em; }
.prompt { background: var(--sheet); border: 1px solid var(--faint); border-left: 4px solid var(--red); padding: .7em 1em .85em; margin-top: 1em; }
.prompt-head { display: flex; align-items: center; gap: .8em; flex-wrap: wrap; justify-content: space-between; margin-bottom: .4em; }
.prompt pre { font: .8em/1.5 ui-monospace, Menlo, Consolas, monospace; margin: 0; white-space: pre-wrap; }
.status { font: .7em/1.3 system-ui, sans-serif; }
.copy-tools { display: flex; align-items: center; gap: .5em; }
.outcomes { display: grid; grid-template-columns: 1fr 1fr; gap: 4%; margin-top: 1.2em; }
.outcomes > div { border-top: 1px solid var(--ink); padding-top: .55em; }
.outcomes h3 { margin-bottom: .25em; color: var(--red); }
.stepnav { border-top: 1px solid var(--faint); display: flex; justify-content: space-between; gap: 1rem; margin-top: 2em; padding-top: .8em; }
@media (max-width: 760px) {
  .toc-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .cover-hero { gap: 4%; }
  .work { grid-template-columns: 1fr; gap: .65em; }
  .illustration, .plate { max-width: 540px; }
}
@media (max-width: 550px) {
  body { font-size: 19px; }
  .cover-hero, .outcomes, .toc-grid { grid-template-columns: 1fr; }
  .cover-hero { gap: 1rem; margin: 1.5rem 0; }
  .outcomes { gap: .8em; }
  .toc a { padding: .15em 0; }
  .lesson { margin-top: 2.5rem; }
}
.write-in { display: none; }
@page { size: Letter; margin: .52in .57in .48in; }
@media print {
  :root { --paper: white; --sheet: #f7f3eb; }
  * { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  body { background: white; font-size: 14pt; line-height: 1.28; }
  main { width: 100%; margin: 0; padding: 0; }
  .skip, .button, .copy-tools, .stepnav { display: none !important; }
  .cover, .lesson { border-top-width: 4pt; padding-top: 6pt; }
  .lesson { break-before: page; margin-top: 0; min-height: 9.96in; display: flex; flex-direction: column; }
  .write-in { display: block; margin-top: auto; padding-top: 14pt; }
  .write-in::after { content: ""; display: block; height: 16pt; border-bottom: 1px solid var(--faint); }
  .runhead, .small, .group-title, figcaption { font-size: 8.1pt; }
  .cover-hero { display: grid; grid-template-columns: 1fr 39%; margin: 26pt 0; gap: 18pt; }
  h1 { font-size: 45pt; }
  h2 { font-size: 28pt; }
  .cover .deck { font-size: 14pt; }
  .toc { padding: 12pt 0 18pt; }
  .toc-header { margin-bottom: 10pt; }
  .toc-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 13pt 22pt; }
  .toc a { font-size: 11.4pt; padding: 0; }
  .lesson-header { margin: 17pt 0 13pt; }
  .deck { font-size: 14pt; }
  .work { display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); gap: 14pt; }
  .plate { padding: 8pt; }
  .plate pre { font-size: 8.2pt; }
  .work li { margin-bottom: 5pt; }
  .references { margin-top: 4pt; font-size: 10pt; }
  .prompt { margin-top: 12pt; padding: 8pt 10pt; }
  .prompt pre { font-size: 10.5pt; line-height: 1.36; }
  .outcomes { display: grid; grid-template-columns: 1fr 1fr; gap: 16pt; margin-top: 14pt; }
  .outcomes p { font-size: 12.8pt; }
}
"""

SCRIPT = """
document.querySelectorAll('.copy').forEach(button => {
  button.hidden = false;
  button.addEventListener('click', async () => {
    const text = document.getElementById(button.getAttribute('aria-controls'));
    const status = button.parentElement.querySelector('.status');
    try {
      await navigator.clipboard.writeText(text.textContent);
      status.textContent = 'Copied.';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(text);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      try {
        if (document.execCommand('copy')) {
          status.textContent = 'Copied.';
          return;
        }
      } catch { /* The selected prompt can still be copied manually. */ }
      status.textContent = 'Selected. Press Ctrl+C or ⌘C.';
    }
  });
});
document.querySelector('#print').hidden = false;
document.querySelector('#print').addEventListener('click', () => window.print());
"""


def data_uri(relative_path):
    path = ROOT / relative_path
    kind = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{kind};base64,{encoded}"


def font_styles():
    fonts = (
        ("Book", "eb-garamond/EBGaramond.ttf", "400 800"),
        ("Broadside", "alfa-slab-one/AlfaSlabOne-Regular.ttf", "400"),
    )
    styles = []
    for name, filename, weight in fonts:
        font = Path("media/type") / filename
        license_text = (ROOT / font.parent / "OFL.txt").read_text()
        styles.append(f"/* {license_text} */\n@font-face {{font-family: '{name}'; "
                      f"src: url('{data_uri(font)}') format('truetype'); font-weight: {weight};}}")
    return "\n".join(styles)


def table_of_contents(lessons):
    groups = defaultdict(list)
    for index, lesson in enumerate(lessons, 1):
        groups[lesson["group"]].append(
            f'<li><a href="#{escape(lesson["id"])}"><span>{index:02}</span>'
            f'{escape(lesson["title"])}</a></li>'
        )
    return "".join(
        f'<section><h3 class="group-title">{escape(group)}</h3><ol>{"".join(entries)}</ol></section>'
        for group, entries in groups.items()
    )


def render_lesson(lesson, index, total, next_id):
    title = escape(lesson["title"])
    slug = escape(lesson["id"])
    actions = "".join(f"<li>{escape(action)}</li>" for action in lesson["actions"])
    if lesson["image"]:
        caption = escape(CAPTIONS[lesson["id"]])
        # The visible caption supplies the image's equivalent in the reading order.
        visual = (f'<figure class="illustration"><img src="{data_uri(lesson["image"])}" alt="">'
                  f'<figcaption>{caption}</figcaption></figure>')
    else:
        plate = "\n".join(escape(line) for line in lesson["plate"])
        visual = f'<div class="plate"><pre>{plate}</pre></div>'
    links = "".join(f'<a href="{escape(url)}">{escape(label)}</a>'
                    for label, url in lesson["links"])
    references = f'<p class="references">{links}</p>' if links else ""
    prompt = ""
    if lesson["prompt"]:
        prompt = f"""
        <section class="prompt"><div class="prompt-head"><h3>Prompt to copy</h3>
        <div class="copy-tools"><span class="status" role="status"></span>
        <button class="button copy" type="button" aria-controls="prompt-{slug}" hidden>Copy prompt</button></div></div>
        <pre id="prompt-{slug}">{escape(lesson["prompt"])}</pre></section>"""
    forward = f'<a href="#{escape(next_id)}">Next step →</a>' if next_id else ""
    return f"""
    <article id="{slug}" class="lesson" aria-labelledby="title-{slug}">
      <div class="runhead"><span class="accent">{escape(lesson["group"])}</span><span>Step {index:02} / {total:02}</span></div>
      <header class="lesson-header"><h2 id="title-{slug}">{title}</h2><p class="deck">{escape(lesson["subtitle"])}</p></header>
      <div class="work"><div><ol>{actions}</ol>{references}</div>{visual}</div>
      {prompt}
      <div class="outcomes"><div><h3>Check your work</h3><p>{escape(lesson["check"])}</p></div>
      <div><h3>If you get stuck</h3><p>{escape(lesson["fix"])}</p></div></div>
      <p class="write-in small">My checkpoint</p>
      <nav class="stepnav" aria-label="Navigation for step {index}"><a href="#contents">↑ Contents</a>{forward}</nav>
    </article>"""


def build(source, output):
    lessons = json.loads(source.read_text(encoding="utf-8"))
    total = len(lessons)
    sections = []
    for index, lesson in enumerate(lessons, 1):
        next_id = lessons[index]["id"] if index < total else None
        sections.append(render_lesson(lesson, index, total, next_id))
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Small Worlds Workshop · Part 1 desktop workbook</title>
<style>{font_styles()}\n{STYLE}</style></head>
<body><a class="skip" href="#contents">Skip to contents</a><main>
<section class="cover" aria-labelledby="cover-title">
<div class="runhead"><span>Creative AI Masterclass</span><span>Part 1 · Student workbook</span></div>
<header class="cover-hero"><div><p class="small">Set up from scratch</p>
<h1 id="cover-title">Small Worlds Workshop</h1>
<p class="deck">Give your desktop assistant an exhibition brief. Together you’ll build a gallery, revise a paper city in Blender and open it to visitors in Godot.</p></div>
<figure><img src="{data_uri('images/desktop-class/paper-city.png')}" alt="Three folded-roof towers and a footbridge in a miniature paper city.">
<figcaption>Paper City · Starter scene for brief SW-17</figcaption></figure></header>
<nav id="contents" class="toc" aria-labelledby="contents-title"><div class="toc-header"><h2 id="contents-title">Contents</h2>
<button class="button" id="print" type="button" hidden>Print workbook</button></div>
<div class="toc-grid">{table_of_contents(lessons)}</div></nav></section>
{''.join(sections)}
</main><script>{SCRIPT}</script></body></html>
"""
    output.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build(args.source, args.output)
