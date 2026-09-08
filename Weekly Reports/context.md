# Weekly Report — Context & Build Guide
_For the next Claude instance: how to produce the next weekly report given only Ethan's list of what the team did that week._

## What to produce
A file `Self_Driving_RC_Car.docx` and a matching `Self_Driving_RC_Car.pdf` in this folder, in the TA's required template format. Ethan will give you a plain list of what the team did that week plus per-person hours; you turn it into the report. **Submit the PDF only** — see Submission rules.

> **FORMAT CHANGED as of Week 3 (Sep 8 2026).** The old advisor format (title + subtitle + 2-col header table + `Goals`/`Progress`, no next-week goals) is DEAD. TA Ruben Ramirez issued a mandatory template — `project_name.docx` in this folder. The current format is described in "Required format" below; the old build script is kept at the bottom under "OLD format (retired)" only for reference.

## Project facts
- **Project name** (document title + used in filenames): **Self Driving RC Car**
- **Course:** CENG 4265 — Senior Project  (confirmed by Ethan; the Week 1 report's "CENG 4266" was a typo)
- **School:** University of Houston – Clear Lake (UHCL)
- **Faculty advisor (the "client"):** Professor Nguyen
- **Team (list in this order):** Ethan Wells, Alexis Perez, Ethan Bishop, Abigail Duran  (Alexis is male)
- **Terminology — fix Ethan's occasional slips:**
  - Compute: **Raspberry Pi Compute Module 5 (CM5)** on a custom carrier PCB — NOT "Arduino"
  - Prototyping board: **Raspberry Pi Compute Module I/O Board** — NOT "breadboard"
  - Sensors: camera (primary, reads signs) + ultrasonic (obstacle/wall distance) + IMU (heading/turns); no LiDAR
  - Scope: self-driving RC car that follows a controlled course AND obeys traffic signs. Fall = stationary recognition system; Spring = autonomous vehicle.
- **Ethan's voice:** plain, concrete, sequential, honest, no embellishment.
  - **Before writing, ingest Ethan's voice from his internship reports.** Read the `.docx` files in `~/Desktop/Senior Project/Internship Reports/` (`Ethan_Wells_Internship_Report1.docx`–`6.docx`) with python-docx to calibrate tone and diction, then write the weekly report in that voice.
  - Path note: Ethan keeps the originals under `~/Documents/internship_for_elective_credit/internship_reports/`, but the **local Claude Code session cannot read `~/Documents/` (macOS returns "Operation not permitted")**. Use the in-project copy in `~/Desktop/Senior Project/Internship Reports/` instead. If that copy is missing, ask Ethan to copy the reports onto the Desktop where the session can reach them.

## File conventions
- This folder: `~/Desktop/Senior Project/Weekly Reports` on Ethan's Mac (the local Claude Code session works here directly via the Bash tool).
- Output filenames (TA's rule — project name, underscores, no week number): `Self_Driving_RC_Car.docx` / `Self_Driving_RC_Car.pdf`. Canvas versions per submission, so the same filename each week is correct.
- **The undated `Self_Driving_RC_Car.docx` / `.pdf` are the WORKING copies — they get rebuilt and overwritten in place each week, and `Self_Driving_RC_Car.pdf` is the file submitted to Canvas.** Each week, update the data in `build_report.py` and rerun; it overwrites these undated files.
- **After the report is final each week, save a dated archive copy of the PDF as `Self_Driving_RC_Car - Week N.pdf`** (e.g. `cp "Self_Driving_RC_Car.pdf" "Self_Driving_RC_Car - Week N.pdf"`). These dated copies are frozen history — never edit them; only the undated copy is edited/rebuilt.
- TEMPLATE: `project_name.docx` in this folder — the exact file the TA distributed. The build script edits a copy of it in place, so fonts/margins/styles stay identical to what the TA expects (12 pt throughout; section headers bold + underlined). Do NOT hand-rebuild from scratch.

## Submission rules (from Ruben's email, Sep 8 2026)
- **Only the group leader (Ethan Wells) submits on Canvas** — one report per group, NOT one per student.
- **PDF only**, filename = project name (`Self_Driving_RC_Car.pdf`).
- Questions go to Ruben Ramirez (TA) or Dr. Nguyen.

## Required format (do NOT deviate — mirrors `project_name.docx`)
Header block (each on its own line; label prefix bold, section headers bold+underlined):
1. `WEEKLY REPORT :` (bold+underline)
2. `Project Title: Self Driving RC Car`
3. `Date: M/D/YYYY`  (the report/class date Ethan gives)
4. `Instructor: Dr. Nguyen`
5. `TA: Ruben Ramirez`
6. `Project Members:` (bold+underline) then one line per member; mark Ethan as `(Group Leader)`.

Then four sections, each header bold+underlined:
7. `Weekly Summary (M/D/YYYY):` — one paragraph, group-level, what got done in the last week, WITH specifics (name each part and its purpose — e.g. "Raspberry Pi Compute Module I/O Board", "ultrasonic sensor for wall distance").
8. `Proposed Plan for Next Week:` — **next-week goals are now REQUIRED** (opposite of the old rule). One line per member: underlined `Name:` + a specific, non-ambiguous goal. No vague goals. For reports after the first, this is what next week's report updates against.
9. `Weekly Contributions:` — per member: an underlined `Name:` subhead, then one line per task in the form `M/D/YYYY – <what they did> (N hours)`. Every task needs a date and hours.
10. `Hour Tracker:` — the table in the template: `Name | Hours For the Week | Cumulative Hours`, one row per member.

## Turning Ethan's input into content
- Ethan gives: what each person did, and hours (with rough dates). Map each task to its owner for both `Weekly Contributions` (dated + hours) and the `Weekly Summary` (fold into the group paragraph).
- **Hours you cannot infer — always ask** for per-person hours/dates and cumulative totals if not given. Cumulative = prior cumulative + this week (hour tracking started Week 3, Sep 8 2026, so Week 3 cumulative == weekly).
- `Proposed Plan for Next Week`: if Ethan doesn't dictate goals, draft specific ones from the obvious next steps (e.g. receive & bench-test an ordered sensor; get a first TensorFlow training run going) and have him approve.
- For reports after the first: open each member's contribution/summary by updating the previous week's `Proposed Plan` — say how the goal was met, or explain in detail what was done and why it wasn't (damage, shipping delays, other roadblocks). The email explicitly wants this.
- Dates/cadence: Week 1 = Aug 18–24 2026; Week 2 = Aug 25–31 2026; Week 3 = Sep 1–7 2026 (report dated Sep 8). Continue ~weekly or ask Ethan for the exact date to stamp.

## Environment note (execution context matters)
- This workflow has run in two different environments. The `device_bash` sandbox (folder mounted at `$HOME/mnt/Weekly Reports`) had LibreOffice preinstalled. The **local Claude Code session runs commands directly in Ethan's macOS zsh** via the Bash tool, working out of `~/Desktop/Senior Project/Weekly Reports`.
- LibreOffice is now installed on the Mac (`brew install --cask libreoffice`, Sep 8 2026). The `soffice` binary is NOT on PATH — invoke it by full path: `/Applications/LibreOffice.app/Contents/MacOS/soffice`.
- python-docx is available to `python3` on the Mac.

## Build script (CURRENT — new format; run on the Mac, python-docx + LibreOffice installed — see Environment note)
Edits a copy of `project_name.docx` in place so formatting stays identical, then save as `Self_Driving_RC_Car.docx`. Fill the five data blocks (`members`, `summary`, `plan`, `contributions`, `hours`) and the two dates, then run. Runs are written at 12 pt (`w:sz` val `24`); `Name:` subheads/plan names are underlined; section headers keep the template's bold+underline.
```python
import copy
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

PROJECT = "Self Driving RC Car"
DATE = "9/8/2026"
SUMMARY_DATE = "9/8/2026"

members = ["Ethan Wells (Group Leader)", "Alexis Perez", "Ethan Bishop", "Abigail Duran"]

summary = ("One group-level paragraph. Name each part and its purpose.")

plan = [   # next-week goals, one per member, specific
    ("Ethan Wells", "..."),
    ("Alexis Perez", "..."),
    ("Ethan Bishop", "..."),
    ("Abigail Duran", "..."),
]

contributions = [   # (name, [(date, text, hours), ...])
    ("Ethan Wells", [("9/8/2026", "...", 5)]),
    ("Alexis Perez", [("9/7/2026", "...", 3)]),
    ("Ethan Bishop", [("9/7/2026", "...", 3)]),
    ("Abigail Duran", [("9/7/2026", "...", 3), ("9/8/2026", "...", 3)]),
]

hours = [   # (name, hours_this_week, cumulative)
    ("Ethan Wells", "5", "5"), ("Alexis Perez", "3", "3"),
    ("Ethan Bishop", "3", "3"), ("Abigail Duran", "6", "6"),
]

d = Document("project_name.docx")

def para_by(pred):
    for p in d.paragraphs:
        if pred(p.text):
            return p
    raise SystemExit("anchor not found")

def add_run(p_el, text, bold=False, underline=False):
    r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
    if bold: rpr.append(OxmlElement('w:b'))
    if underline:
        u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rpr.append(u)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '24'); rpr.append(sz)   # 12pt
    r.append(rpr)
    t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = text; r.append(t)
    p_el.append(r); return r

p_sum_head = para_by(lambda t: t.startswith("Weekly Summary"))
sum_instr = p_sum_head._p.getnext()
normal_tmpl = copy.deepcopy(sum_instr)

def new_normal():
    el = copy.deepcopy(normal_tmpl)
    for r in el.findall(qn('w:r')): el.remove(r)
    return el

def line_para(runs):
    el = new_normal()
    for text, b, u in runs: add_run(el, text, b, u)
    return el

# Project Title / Date
p_title = para_by(lambda t: t.startswith("Project Title"))
rs = p_title.runs; rs[0].text = "Project Title: "; rs[1].text = PROJECT
for r in rs[2:]: r.text = ""
p_date = para_by(lambda t: t.startswith("Date:"))
rs = p_date.runs; rs[0].text = "Date: "; rs[1].text = DATE
for r in rs[2:]: r.text = ""

# Project Members
p_mem = para_by(lambda t: t.strip() == "Project Members:")
anchor = p_mem._p
nxt = anchor.getnext()
if nxt is not None and nxt.tag == qn('w:p') and not nxt.findall(qn('w:r')):
    nxt.getparent().remove(nxt)
for m in members:
    el = line_para([(m, False, False)]); anchor.addnext(el); anchor = el

# Weekly Summary
for r in p_sum_head.runs:
    r.text = "Weekly Summary (%s):" % SUMMARY_DATE if r is p_sum_head.runs[0] else ""
for r in list(sum_instr.findall(qn('w:r'))): sum_instr.remove(r)
add_run(sum_instr, summary, False, False)

# Proposed Plan
p_plan_head = para_by(lambda t: t.startswith("Proposed Plan"))
plan_instr = p_plan_head._p.getnext()
for r in list(plan_instr.findall(qn('w:r'))): plan_instr.remove(r)
n0, g0 = plan[0]; add_run(plan_instr, n0 + ": ", False, True); add_run(plan_instr, g0, False, False)
anchor = plan_instr
for n, g in plan[1:]:
    el = line_para([(n + ": ", False, True), (g, False, False)]); anchor.addnext(el); anchor = el

# Weekly Contributions (wipe everything between the heading and Hour Tracker, rebuild)
p_contrib = para_by(lambda t: t.strip() == "Weekly Contributions:")
p_hour = para_by(lambda t: t.strip() == "Hour Tracker:")
start = p_contrib._p; stop = p_hour._p
cur = start.getnext(); to_remove = []
while cur is not None and cur is not stop:
    to_remove.append(cur); cur = cur.getnext()
for el in to_remove: el.getparent().remove(el)
anchor = start
for name, entries in contributions:
    head = line_para([(name + ":", False, True)]); anchor.addnext(head); anchor = head
    for date, text, hrs in entries:
        unit = "hour" if hrs == 1 else "hours"
        el = line_para([("%s – %s (%d %s)" % (date, text, hrs, unit), False, False)])
        anchor.addnext(el); anchor = el
anchor.addnext(new_normal())   # spacer before Hour Tracker

# Hour Tracker table
tbl = d.tables[0]
def set_cell(cell, text):
    p = cell.paragraphs[0]
    for r in list(p._p.findall(qn('w:r'))): p._p.remove(r)
    add_run(p._p, text, False, False)
for i, (name, wk, cum) in enumerate(hours):
    row = tbl.rows[i + 1]
    set_cell(row.cells[0], name); set_cell(row.cells[1], wk); set_cell(row.cells[2], cum)

d.save("Self_Driving_RC_Car.docx")
print("saved")
```
The live copy of this script is saved as `build_report.py` in this folder.

## OLD format (retired — for reference only, do NOT use)
```python
import copy, re
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

WEEK = 3
PERIOD = "September 1 – September 7, 2026"
PREPARED = "September 8, 2026"
goals = [
    ("Ethan Wells", "..."),
    ("Alexis Perez", "..."),
    ("Ethan Bishop", "..."),
    ("Abigail Duran", "..."),
]
progress = [
    ("Ethan Wells", "..."),
    ("Alexis Perez", "..."),
    ("Ethan Bishop", "..."),
    ("Abigail Duran", "..."),
    ("Team", "..."),
]

d = Document("Self Driving RC Car - Week 1.docx")   # template
paras = d.paragraphs
old_els = [p._p for p in paras[3:]]                  # remove everything after the Heading 1

def set_first_run(p_el, text):
    runs = p_el.findall(qn('w:r'))
    if not runs:
        r = OxmlElement('w:r'); p_el.append(r); runs=[r]
    first = runs[0]
    for extra in runs[1:]: p_el.remove(extra)
    for t in first.findall(qn('w:t')): first.remove(t)
    t = OxmlElement('w:t'); t.set(qn('xml:space'),'preserve'); t.text=text; first.append(t)

set_first_run(paras[0]._p, "Self Driving RC Car")
for r in paras[1].runs:
    if '#' in r.text: r.text = re.sub(r'#\d+', '#%d' % WEEK, r.text)

def set_cell(cell, text):
    p = cell.paragraphs[0]
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]: r.text = ''
    else:
        p.add_run(text)

tbl = d.tables[0]
for row in tbl.rows:
    k = row.cells[0].text.strip()
    if k=='Course':   set_cell(row.cells[1], 'CENG 4265 — Senior Project')
    elif k=='Project':set_cell(row.cells[1], 'Self Driving RC Car')
    elif k=='Report': set_cell(row.cells[1], 'Weekly Report #%d' % WEEK)
    elif k=='Period': set_cell(row.cells[1], PERIOD)
    elif k=='Prepared':set_cell(row.cells[1], PREPARED)

heading_tmpl = copy.deepcopy(paras[2]._p)
normal_tmpl  = copy.deepcopy(paras[10]._p)

def make_heading(text):
    el = copy.deepcopy(heading_tmpl); set_first_run(el, text); return el

def make_person(name, text):
    el = copy.deepcopy(normal_tmpl)
    for r in el.findall(qn('w:r')): el.remove(r)
    r1 = OxmlElement('w:r'); rpr = OxmlElement('w:rPr'); rpr.append(OxmlElement('w:b')); r1.append(rpr)
    t1 = OxmlElement('w:t'); t1.set(qn('xml:space'),'preserve'); t1.text = name+': '; r1.append(t1); el.append(r1)
    r2 = OxmlElement('w:r'); t2 = OxmlElement('w:t'); t2.set(qn('xml:space'),'preserve'); t2.text = text; r2.append(t2); el.append(r2)
    return el

set_first_run(paras[2]._p, 'Goals for the week')
anchor = paras[2]._p
for n,t in goals:
    el = make_person(n,t); anchor.addnext(el); anchor = el
ph = make_heading('Progress for the week'); anchor.addnext(ph); anchor = ph
for n,t in progress:
    el = make_person(n,t); anchor.addnext(el); anchor = el
for el in old_els:
    el.getparent().remove(el)

d.save("Self Driving RC Car - Week %d.docx" % WEEK)
print("saved")
```

## PDF
Run from inside the Weekly Reports folder (use the full soffice path — it is not on PATH):
```
/Applications/LibreOffice.app/Contents/MacOS/soffice --headless -env:UserInstallation=file:///tmp/lo_pf --convert-to pdf --outdir "$PWD" "Self_Driving_RC_Car.docx"
```
Fontconfig "no <cachedir>" warnings are harmless; the PDF still writes. If it errors with an Io/Abort lock, the .docx/.pdf is open in an Office app on the Mac — ask Ethan to close it, then retry. A stale `.~lock.*#` file left behind can just be removed with `rm`.

## Gotchas
- Editing the SharePoint / Word-online doc through the Chrome computer tool is unreliable (keystrokes land in the document; Ctrl+F types into the page). Work the local .docx with python-docx instead.
- The local Claude Code session CANNOT read `~/Documents/` (macOS "Operation not permitted"); it works fine inside `~/Desktop/Senior Project`. Keep any files Claude needs (internship reports, proposal) under the Desktop project folder.
- The proposal lives locally at `~/Desktop/Senior Project/Proposal/Self_Driving_RC_Proposal.docx` (also in SharePoint). It confirms the stack: train the traffic-sign vision model and run it via **TensorFlow Lite** on the CM5 (trained on public sign datasets, e.g. LISA), with **OpenCV** for the camera/image pipeline. Check new tech claims against it.
- Don't copy the template's example wording ("Arduino Nano, raspberry pi") — that's placeholder text in `project_name.docx`, not our hardware.
