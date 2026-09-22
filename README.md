# Self-Driving RC Car

Senior Project (CENG 4265) — University of Houston–Clear Lake (UHCL)

A self-driving RC car that follows a controlled course and obeys traffic signs.

- **Fall semester:** stationary traffic-sign recognition system.
- **Spring semester:** full autonomous vehicle.

## Hardware

- **Compute:** Raspberry Pi Compute Module 5 (4 GB Lite) on the CM5 IO Board (custom carrier PCB planned for spring)
- **Storage:** M.2 NVMe SSD — boots the CM5 with Raspberry Pi OS Lite (64-bit)
- **Networking:** USB Wi-Fi dongle for headless SSH (the CM5 has no onboard wireless)
- **Sensors:** camera (reads signs), ultrasonic (obstacle/wall distance), IMU (heading/turns)
- **Display:** 16×2 I²C LCD

Full parts list, prices, and wiring: [`Hardware/partslist.md`](Hardware/partslist.md) and the schematic in `Hardware/`.

## Software

- Traffic-sign **classifier** trained in **TensorFlow**, later deployed to the CM5 via **TensorFlow Lite**
- Training data: **GTSRB** (German signs) first to prove out the pipeline, then **LISA** (US signs)
- **OpenCV** finds/crops the sign in the frame and hands it to the classifier

## Team

- Ethan Wells (Group Leader)
- Alexis Perez
- Ethan Bishop
- Abigail Duran

**Faculty advisor:** Dr. Nguyen · **TA:** Ruben Ramirez

## Repository layout

| Path | Contents |
| --- | --- |
| `Proposal/` | Project proposal and Gantt charts |
| `Weekly Reports/` | Rolling working report + presentation, the TA's template, the report generator, and a `Week N/` folder of frozen deliverables per week |
| `Hardware/` | Parts list (`partslist.md`) and wiring schematics |
| `Model Training/` | Traffic-sign classifier training code (GTSRB dataset is gitignored — see its README) |
| `Learning/` | Self-directed learning side-quests, separate from the main project |
| `setup.sh` | Installs the shared software prerequisites (git, python3, pip, venv) on a fresh board |
| `CLAUDE.md` | Working agreement for AI assistants used on this repo |

### Weekly reports

Reports follow the TA's required template (`Weekly Reports/project_name.docx`). Everything at the top level of
`Weekly Reports/` is a live working copy:

- `Self_Driving_RC_Car.docx` / `.pdf` — the rolling report, rebuilt each week from `build_report.py` and submitted as PDF.
- `Self-Driving-RC-Car.pptx` — the rolling presentation deck (started Week 4). **Generated — do not hand-edit.**

The deck is assembled from one file per person in `Weekly Reports/slides/` (`0-title.pptx`, `1-ethan-wells.pptx`, …).
A `.pptx` is a binary file, so git cannot merge two people's edits to the same deck — everyone edits only their own
file, which makes conflicts impossible. Whoever assembles the deck runs `python3 assemble_deck.py` from inside
`Weekly Reports/`, which stitches the slide files in filename order into `Self-Driving-RC-Car.pptx`. See
`Weekly Reports/slides/README.md`.

Each week's frozen deliverables are archived in a `Week N/` subfolder — the dated report PDF and docx, plus the
dated presentation from Week 4 on:

```
Weekly Reports/
  build_report.py  context.md  project_name.docx       ← tooling + template
  assemble_deck.py                                     ← builds the deck from slides/
  slides/  0-title.pptx  1-ethan-wells.pptx  …         ← one file per person (edit yours)
  Self_Driving_RC_Car.docx / .pdf                      ← rolling report (working)
  Self-Driving-RC-Car.pptx                             ← rolling deck (generated)
  Week 1/ … Week 3/   frozen report .pdf + .docx
  Week 4/             frozen report + frozen .pptx
```

See `Weekly Reports/context.md` for the full build/format guide.
