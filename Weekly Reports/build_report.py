import copy
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

PROJECT = "Self Driving RC Car"
DATE = "9/8/2026"
SUMMARY_DATE = "9/8/2026"

members = ["Ethan Wells (Group Leader)", "Alexis Perez", "Ethan Bishop", "Abigail Duran"]

summary = ("This week the team moved into buying hardware and starting on the software side. "
    "We bought the Raspberry Pi Compute Module I/O Board, which came in this week, so we have a board to prototype the CM5 carrier design on. "
    "Abigail drew up the schematic Professor Nguyen asked for. "
    "We also ordered the rest of the core sensors: an ultrasonic sensor for measuring distance to obstacles and walls, "
    "an IMU for tracking heading and turns, and the camera that reads the traffic signs. "
    "Ethan Wells started researching how to train the traffic-sign model in TensorFlow, which is the framework the proposal calls for, "
    "and set up a GitHub repository to hold the training code. "
    "As a group we settled on standing weekly meeting times in the Robotics Lab in the Delta Building: "
    "Mondays 4:00 to 7:00 PM, Wednesdays 1:00 to 6:00 PM, and Thursdays 10:00 AM to 12:00 PM.")

plan = [
    ("Ethan Wells", "Get a first training run going in TensorFlow on a public traffic-sign dataset (LISA), push the training script to the GitHub repo, and start figuring out how to convert the model to TensorFlow Lite so it can run on the CM5."),
    ("Alexis Perez", "Get the ultrasonic sensor in and test it on the bench, make sure it returns distance readings, and figure out its usable range and how it reads against a wall."),
    ("Ethan Bishop", "Get the IMU in and test it on the bench, make sure it reports heading and orientation, and check how noisy the readings are."),
    ("Abigail Duran", "Get the camera in and make sure it captures frames, and rework the schematic based on Professor Nguyen's feedback so it is ready to lay out the carrier board."),
]

contributions = [
    ("Ethan Wells", [("9/8/2026", "Bought the Compute Module I/O Board (it came in this week), started researching how to train the traffic-sign model in TensorFlow, and set up a GitHub repository for the training code", 5)]),
    ("Alexis Perez", [("9/7/2026", "Researched ultrasonic sensor options and ordered one to measure distance to obstacles and walls", 3)]),
    ("Ethan Bishop", [("9/7/2026", "Researched IMU options and ordered one to track heading and turns", 3)]),
    ("Abigail Duran", [("9/7/2026", "Worked on the schematic Professor Nguyen asked for", 2),
                        ("9/8/2026", "Finished the schematic and ordered the camera", 3)]),
]

hours = [("Ethan Wells", "5", "5"), ("Alexis Perez", "3", "3"),
         ("Ethan Bishop", "3", "3"), ("Abigail Duran", "5", "5")]

d = Document("project_name.docx")

def para_by(pred):
    for p in d.paragraphs:
        if pred(p.text):
            return p
    raise SystemExit("anchor not found: " + repr(pred))

def add_run(p_el, text, bold=False, underline=False):
    r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
    if bold:
        rpr.append(OxmlElement('w:b'))
    if underline:
        u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rpr.append(u)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '24'); rpr.append(sz)   # 12pt
    r.append(rpr)
    t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = text; r.append(t)
    p_el.append(r)
    return r

# normal-body paragraph template (clone the summary instruction paragraph, keep its pPr)
p_sum_head = para_by(lambda t: t.startswith("Weekly Summary"))
sum_instr = p_sum_head._p.getnext()          # the instruction paragraph after the heading
normal_tmpl = copy.deepcopy(sum_instr)

def new_normal():
    el = copy.deepcopy(normal_tmpl)
    for r in el.findall(qn('w:r')): el.remove(r)
    return el

def line_para(runs):
    """runs = list of (text, bold, underline)"""
    el = new_normal()
    for text, b, u in runs:
        add_run(el, text, b, u)
    return el

# 1) Project Title
p_title = para_by(lambda t: t.startswith("Project Title"))
rs = p_title.runs
rs[0].text = "Project Title: "
rs[1].text = PROJECT
for r in rs[2:]: r.text = ""

# 2) Date
p_date = para_by(lambda t: t.startswith("Date:"))
rs = p_date.runs
rs[0].text = "Date: "
rs[1].text = DATE
for r in rs[2:]: r.text = ""

# 3) Project Members -> insert one line per member after the heading
p_mem = para_by(lambda t: t.strip() == "Project Members:")
anchor = p_mem._p
# remove the single blank paragraph the template puts right after members, if present
nxt = anchor.getnext()
if nxt is not None and nxt.tag == qn('w:p') and not nxt.findall(qn('w:r')):
    nxt.getparent().remove(nxt)
for m in members:
    el = line_para([(m, False, False)])
    anchor.addnext(el); anchor = el

# 4) Weekly Summary heading date + body
for r in p_sum_head.runs:
    r.text = "Weekly Summary (%s):" % SUMMARY_DATE if r is p_sum_head.runs[0] else ""
# replace instruction paragraph content with the summary
for r in list(sum_instr.findall(qn('w:r'))): sum_instr.remove(r)
add_run(sum_instr, summary, False, False)

# 5) Proposed Plan -> per-member lines replacing the instruction paragraph
p_plan_head = para_by(lambda t: t.startswith("Proposed Plan"))
plan_instr = p_plan_head._p.getnext()
# turn the instruction paragraph into the first member's line
for r in list(plan_instr.findall(qn('w:r'))): plan_instr.remove(r)
n0, g0 = plan[0]
add_run(plan_instr, n0 + ": ", False, True)
add_run(plan_instr, g0, False, False)
anchor = plan_instr
for n, g in plan[1:]:
    el = line_para([(n + ": ", False, True), (g, False, False)])
    anchor.addnext(el); anchor = el

# 6) Weekly Contributions -> remove everything between the heading and Hour Tracker, rebuild
p_contrib = para_by(lambda t: t.strip() == "Weekly Contributions:")
p_hour = para_by(lambda t: t.strip() == "Hour Tracker:")
start = p_contrib._p
stop = p_hour._p
# collect elements strictly between start and stop
to_remove = []
cur = start.getnext()
while cur is not None and cur is not stop:
    to_remove.append(cur)
    cur = cur.getnext()
for el in to_remove:
    el.getparent().remove(el)
# rebuild contributions after the heading
anchor = start
for name, entries in contributions:
    head = line_para([(name + ":", False, True)])
    anchor.addnext(head); anchor = head
    for date, text, hrs in entries:
        unit = "hour" if hrs == 1 else "hours"
        el = line_para([("%s – %s (%d %s)" % (date, text, hrs, unit), False, False)])
        anchor.addnext(el); anchor = el
# one blank spacer before Hour Tracker
spacer = new_normal()
anchor.addnext(spacer)

# 7) Hour Tracker table
tbl = d.tables[0]
def set_cell(cell, text):
    p = cell.paragraphs[0]
    for r in list(p._p.findall(qn('w:r'))): p._p.remove(r)
    add_run(p._p, text, False, False)
for i, (name, wk, cum) in enumerate(hours):
    row = tbl.rows[i + 1]
    set_cell(row.cells[0], name)
    set_cell(row.cells[1], wk)
    set_cell(row.cells[2], cum)

d.save("Self_Driving_RC_Car.docx")
print("saved")
