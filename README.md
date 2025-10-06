```markdown
# SAP-1 Microprocessor Control Sequencer

### Enhanced 8-bit SAP-1 Implementation with Shift, Rotate, and Jump Instructions

---

## Project Overview

This repository presents an **enhanced implementation of the SAP-1 (Simple-As-Possible) Microprocessor**, designed and simulated using **Logisim-Evolution v3.9.0**.  
The project demonstrates complete instruction-cycle execution — from **Fetch → Decode → Execute** — using discrete digital components such as logic gates, multiplexers, decoders, and flip-flops.

This enhanced design extends the traditional SAP-1 with advanced functionalities for improved flexibility, automation, and computational capability.

---

## Key Features

| Category | Description |
|-----------|-------------|
| **Architecture** | 8-bit Data Bus, 4-bit Address Bus, Von Neumann Architecture |
| **Instruction Set** | 14 total operations including arithmetic, logic, shift/rotate, and control flow |
| **Enhanced Operations** | Bitwise **Shift** (SHT) and **Rotate** (RTE) with configurable direction and amount |
| **Control System** | Advanced **Control Sequencer** with ring counter (T₁–T₆) timing pulses |
| **Automation** | Automatic RAM bootloading and integrated **assembler/compiler** |
| **Optimization** | **Ring-reset system** to reduce instruction execution cycles |
| **Assembler Integration** | Converts assembly mnemonics to hexadecimal machine code |
| **Simulation Tool** | Logisim-Evolution v3.9.0 |

---

## Demonstration Video

Click below to view the full **Control Sequencer demonstration** on YouTube:

[![SAP-1 Control Sequencer Demonstration](https://img.youtube.com/vi/epArGkpsPSU/maxresdefault.jpg)](https://youtu.be/epArGkpsPSU)

---

## Repository Structure

| File / Folder | Description |
|----------------|-------------|
| **Sayeem_CS.circ** | Main Logisim-Evolution circuit file — complete SAP-1 microprocessor implementation |
| **assembler.py** | Python-based assembler that converts human-readable assembly code to machine-readable hexadecimal format |
| **input.txt** | Input file containing assembly code (used by assembler) |
| **sample_program_1.txt** | Demonstrates **Shift (SHT)** and **Rotate (RTE)** instructions |
| **sample_program_2.txt** | Demonstrates **Jump (JMP)** instruction functionality |
| **final_report.pdf** | Detailed project report with architecture, methodology, schematics, and results |
| **README.md** | Project documentation (this file) |
| **.gitignore** | Git ignore configuration |

---

## Implementation Details

### 1. **Architecture**

The processor comprises five core subsystems:
- **Program Counter (PC)** – Sequential address generation and direct address jump
- **Registers (A & B)** – Operand storage for arithmetic and bitwise operations
- **Arithmetic Logic Unit (ALU)** – Performs subtraction and logical operations
- **Control Sequencer** – Generates control signals and synchronizes timing (T₁–T₆)
- **SRAM Memory** – 16×8 dual-purpose memory for program and data

The system follows a **6-phase ring-counter timing** for synchronized instruction execution.

---

### 2. **Instruction Enhancements**

| Operation | Description | Encoding |
|------------|--------------|-----------|
| **SHT n** | Logical shift operation (MSB = direction: 0 = right, 1 = left; 3 LSBs = shift amount) | Example: `%0010` → shift right by 2 |
| **RTE a** | Bitwise rotation (MSB = direction: 0 = right, 1 = left; 3 LSBs = rotate amount) | Example: `%1010` → rotate left by 2 |
| **JMP addr** | Jump to any program memory address for looped or conditional execution | |

---

### 3. **Assembler Functionality**

`assembler.py` translates `.txt` assembly programs into **Logisim-readable hex code**.  
The output follows the standard Logisim format:

```

v3.0 hex words addressed
0: <hex values>

```

#### Example 1 — *Shift & Rotate Program* (`sample_program_1.txt`)
**Assembly:**
```

LDA 15
SHT 2    %0010  (0 = right shift)
STA 11
LDA 15
RTE a    %1010  (1 = left rotate)
STA 12
HLT

10101010

```

**Assembler Output:**
```

v3.0 hex words addressed
0: 1f 62 7b 1f 8c 7c 50 00 00 00 00 00 00 00 00 12

```

---

#### Example 2 — *Jump Instruction Program* (`sample_program_2.txt`)
**Assembly:**
```

LDA 15
LDB 14
OUT 13
SUB 12
JMP 10
SHT 2
STA 11
HLT

11111111
10101010

```

**Assembler Output:**
```

v3.0 hex words addressed
0: 1f 2e 3d 4c 9a 62 7b 00 00 00 50 00 00 00 c7 12

```

These hexadecimal outputs are **automatically generated** by the assembler and **uploaded to the RAM bootloader** in Logisim to verify processor execution.

---

## Final Report Summary

The **final_report.pdf** contains:
- Complete system schematics (Registers, ALU, Control Sequencer, Decoder, and RAM)
- Timing analysis for each instruction
- Fetch–Decode–Execute cycle explanation
- Bitwise operation hardware (Shift and Rotate circuits)
- Execution trace of sample programs
- Optimization discussion (ring-reset performance improvement)
- Results and future enhancement scope

---

## Technical Specifications

| Component | Specification |
|------------|----------------|
| **Processor Type** | 8-bit Enhanced SAP-1 |
| **Address Bus** | 4-bit (16 memory locations) |
| **Clock Cycles** | T₁–T₆ with ring-reset optimization |
| **Software** | Logisim-Evolution v3.9.0 |
| **Assembler Language** | Python |
| **System Used** | HP Elitebook 840 G7 (Core i7 10th Gen) |

---

## How to Run the Project

1. **Open Logisim-Evolution v3.9.0**  
   - Load the file `Sayeem_CS.circ`.

2. **Generate machine code**  
   - Place your program in `input.txt`.  
   - Run `assembler.py` to convert it to `.hex` format.

3. **Load into Logisim Bootloader**  
   - Copy the generated hex output into Logisim’s **RAM initialization** window.

4. **Simulate Execution**  
   - Step through control signals using the clock.  
   - Observe register values, memory updates, and control sequencing.

---

## Results

| Program | Operation | Output (Hex) | Description |
|----------|------------|---------------|--------------|
| **sample_program_1.txt** | Shift & Rotate | `1f 62 7b 1f 8c 7c 50 ...` | Performs right-shift and left-rotate on stored data |
| **sample_program_2.txt** | Jump Instruction | `1f 2e 3d 4c 9a 62 7b ...` | Demonstrates instruction flow control using JMP |

---

## Author

**Developer:** Sayeem (Velocity)  
**Institution:** Department of Electronics and Telecommunication Engineering, CUET  
**Project:** SAP-1 Microprocessor Control Sequencer (Enhanced Implementation)

---

## License

This project is released under the **MIT License** — free for educational and research use.

---

## Reference

- *Final Report:* Detailed architecture, methodology, and design documentation (see `final_report.pdf`)  
- *Video Demonstration:* [YouTube Link](https://youtu.be/epArGkpsPSU)

---

**© 2025 Sayeem-Velocity — All rights reserved.**
```

---

### Notes:

* This README is fully **Markdown-compliant** and renders perfectly on GitHub.
* The YouTube video has a **preview thumbnail** (clickable, opens on YouTube).
* Each section (Overview → Implementation → Results) aligns with your `final_report.pdf`.
