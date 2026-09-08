# Self-Driving RC Car

Senior Project (CENG 4265) — University of Houston–Clear Lake (UHCL)

A self-driving RC car that follows a controlled course and obeys traffic signs.

- **Fall semester:** stationary traffic-sign recognition system.
- **Spring semester:** full autonomous vehicle.

## Hardware

- **Compute:** Raspberry Pi Compute Module 5 (CM5) on a custom carrier PCB
- **Prototyping:** Raspberry Pi Compute Module I/O Board
- **Sensors:**
  - Camera (primary) — reads traffic signs
  - Ultrasonic — distance to obstacles and walls
  - IMU — heading and turns

## Software

- Traffic-sign vision model trained in **TensorFlow**, deployed to the CM5 via **TensorFlow Lite** (trained on public traffic-sign datasets, e.g. LISA)
- **OpenCV** for the camera / image pipeline

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

### Weekly reports

Reports follow the TA's required template (`Weekly Reports/project_name.docx`). The working copy is
`Weekly Reports/Self_Driving_RC_Car.docx` / `.pdf` — rebuilt each week from `Weekly Reports/build_report.py`
and submitted as PDF. Dated archive copies are kept as `Self_Driving_RC_Car - Week N.pdf`. See
`Weekly Reports/context.md` for the full build/format guide.
