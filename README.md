# Self-Driving RC Car

Senior Project (CENG 4265) — University of Houston–Clear Lake (UHCL)

A self-driving RC car that follows a controlled course and obeys traffic signs.

- **Fall semester:** stationary traffic-sign recognition system.
- **Spring semester:** full autonomous vehicle.

## Hardware

- **Compute:** Raspberry Pi Compute Module 5 (4 GB Lite) on the CM5 IO Board (custom carrier PCB planned for spring)
- **Storage:** M.2 NVMe SSD (boots the CM5)
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
| `Weekly Reports/` | Weekly status reports (`.docx` + `.pdf`), the TA's template, and the report generator |
| `Hardware/` | Parts list (`partslist.md`) and wiring schematics |
| `Model Training/` | Traffic-sign classifier training code (GTSRB dataset is gitignored — see its README) |

### Weekly reports

Reports follow the TA's required template (`Weekly Reports/project_name.docx`). The working copy is
`Weekly Reports/Self_Driving_RC_Car.docx` / `.pdf` — rebuilt each week from `Weekly Reports/build_report.py`
and submitted as PDF. Dated archive copies are kept as `Self_Driving_RC_Car - Week N.pdf`. See
`Weekly Reports/context.md` for the full build/format guide.
