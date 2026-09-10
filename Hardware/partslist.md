# Parts List

Running list of hardware for the Self-Driving RC Car. Status: **Have** / **Ordered** / **Need** / **TBD**.

Wiring: current [Autonomous Car Schematic.png](Autonomous%20Car%20Schematic.png) · earlier Pico version [Schematic_with_pico.jpeg](Schematic_with_pico.jpeg).

| Component | Qty | Purpose | Status | Price (USD) | Date Purchased | Link |
|---|---|---|---|---|---|---|
| Raspberry Pi Compute Module 5 (4 GB, Lite) | 1 | Main compute — runs vision model | Have | 100.00 | 8/26 | [seeedstudio](https://www.seeedstudio.com/Raspberry-Pi-Compute-Module-CM5004000-p-6275.html) |
| Raspberry Pi Compute Module 5 IO Board | 1 | Carrier/prototyping board (M.2, camera, GPIO) | Have | 20.00 | 9/3 | [canakit](https://www.canakit.com/raspberry-pi-compute-module-5-io-board.html) |
| Raspberry Pi Camera Module 3 Standard (12MP AF) | 1 | Reads traffic signs | Need | 29.25 | 9/7 | [adafruit 5657](https://www.adafruit.com/product/5657) |
| Adafruit ICM-20948 9-DoF IMU (STEMMA QT) | 1 | Heading / turns | Need | 19.95 | 9/7 | [adafruit 4554](https://www.adafruit.com/product/4554) |
| STEMMA QT → male header cable, 150 mm | 1 | Wires IMU to CM5 header | Need | 0.95 | 9/9 | [adafruit 4209](https://www.adafruit.com/product/4209) |
| Ultrasonic distance sensor, HC-SR04 (3.3 V) | 1 | Obstacle / wall distance (more later) | Need | 6.95 | 9/7 | [sparkfun](https://www.sparkfun.com/ultrasonic-distance-sensor-3-3v-hc-sr04.html) |
| Waveshare LCD1602 RGB (I²C) | 1 | Status display | Need | 17.99 | 9/9 | [amazon](https://www.amazon.com/dp/B095HBY7YP) |
| KIOXIA BG4 128 GB M.2 2230 NVMe SSD (KBG40ZNS128G) | 1 | Boot media | Need | 44.89 | 9/9 | [amazon](https://www.amazon.com/KIOXIA-Toshiba-128GB-KBG40ZNS128G-Package/dp/B09CR818J2) |
| UGREEN M.2 NVMe enclosure (USB) | 1 | Flash/interface the SSD from a PC | Have | 17.99 | 9/9 | [amazon](https://www.amazon.com/UGREEN-Enclosure-Tool-Free-Thunderbolt-Compatible/dp/B09T97Z7DM) |
| RPi 5 FPC camera cable (22-pin↔15-pin, 200 mm) | 1 | Connect Camera Module 3 to CM5 IO board | Need | 2.70 | 9/9 | [adafruit 5818](https://www.adafruit.com/product/5818) |
| RC car chassis | 1 | Vehicle frame | TBD | — | — | |
| Drive motor(s) | 1 | Propulsion | TBD | — | — | |
| Steering servo | 1 | Steering | TBD | — | — | |
| Wheels | 1 | Set of wheels/tires | TBD | — | — | |
| Battery | 1 | Power source | TBD | — | — | |
| Battery charger | 1 | Charge the battery | TBD | — | — | |
| Custom carrier PCB | 1 | Final CM5 carrier board (spring) | TBD | — | — | |
| **Running total (priced items only)** | | | | **260.67** | | |

Pricing may vary depending on current market; prices listed were from time of purchase.

**Maybe later:** Raspberry Pi Pico as a real-time co-processor — only if the Pi 5's reaction time for the ultrasonic/motor timing isn't good enough.
