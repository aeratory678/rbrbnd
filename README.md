# rbrbnd

a FOSS content/app blocker since we spend most of our time looking at digital devices while forgetting to notice the small things.

built to make you feel more alive without being drained by your screen.

---
<img width="407" height="640" alt="Screenshot 2026-07-27 222431" src="https://github.com/user-attachments/assets/b5a32d7e-dafa-427f-ac27-dfad788a2152" />
<img width="407" height="644" alt="Screenshot 2026-07-27 222516" src="https://github.com/user-attachments/assets/907572eb-ebdf-4703-9e7c-e2bc5006aa0b" />
<img width="1241" height="670" alt="Screenshot 2026-07-27 222617" src="https://github.com/user-attachments/assets/ac2a9c1b-40f7-4b99-b892-ed9b4903b1ef" />

---

### features

* **website + app blocking**: blocks websites across all browsers by editing the Windows OS `hosts` file locally, plus process-killing for desktop apps.
* **no-nonsense ui**: minimal interface inspired by zune OS, powered by `pywebview` with dynamic, procedural background visuals.
* **lightweight**: fast with minimal resource footprint.

---

### safety protection

* **one-time backup**: creates a clean backup of your original `hosts` file before modifying anything.
* **tamper guard**: checks and re-applies the blocklist during an active session if it gets modified mid-way.
* **panic button**: includes a standalone executable (`rbrbnd-panic.exe`) that instantly restores your original `hosts` file if the main app crashes or gets stuck.

---

### roadmap & future ideas

* [x] windows desktop launch (`.exe`)
* [ ] cross-platform support (macOS / linux)
* [ ] **proof of focus (PoF)**: a slightly unrealistic idea of converting focus hours into real rewards (e.g. *focus x hours $\rightarrow$ get y products*).

---

### how to run

#### pre-compiled binary (windows)
Grab `rbrbnd.exe` and `rbrbnd-panic.exe` from the [Releases](../../releases) tab. run `rbrbnd.exe` as Administrator so it can manage system hosts and processes.

#### from source
```bash
# clone the repo
git clone [https://github.com/your-username/rbrbnd.git](https://github.com/your-username/rbrbnd.git)
cd rbrbnd

# install requirements
pip install -r requirements.txt

# run as admin / root
python main.py
