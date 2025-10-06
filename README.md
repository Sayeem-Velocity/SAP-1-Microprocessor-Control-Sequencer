# Enhanced SAP-1 Microprocessor with Bitwise Operations

A fully functional 8-bit microprocessor implementation with advanced bitwise operations (rotation and shifting), automated bootloading, and custom assembler support. Built entirely from fundamental digital components in Logisim-Evolution v3.9.0.

## Video Demonstration

[![SAP-1 Microprocessor Demo](https://img.youtube.com/vi/epArGkpsPSU/maxresdefault.jpg)](https://youtu.be/epArGkpsPSU)

*Click to watch the complete demonstration on YouTube*

---

## Quick Start

### Clone and Run

```bash
# Clone the repository
git clone https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer.git

# Navigate to project directory
cd SAP-1-Microprocessor-Control-Sequencer

# Open the circuit in Logisim-Evolution
logisim-evolution Sayeem_CS.circ
```

### Using the Assembler

```bash
# Write your assembly code in input.txt
# Then run the assembler
python assembler.py

# The output will be generated in 'output' file
# Copy the hex output and paste into Logisim RAM component
```

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation and Usage](#installation-and-usage)
- [Instruction Set](#instruction-set)
- [Sample Programs](#sample-programs)
- [Technical Specifications](#technical-specifications)
- [Design Methodology](#design-methodology)
- [Performance Analysis](#performance-analysis)
- [Documentation](#documentation)
- [Hardware and Software Requirements](#hardware-and-software-requirements)
- [Author](#author)
- [License](#license)

---

## Overview

The Enhanced SAP-1 (Simple-As-Possible) Microprocessor extends the classical educational processor architecture with modern computational capabilities. This implementation demonstrates fundamental computer architecture principles through gate-level digital design while incorporating advanced features typically found in more sophisticated processors.

**Core Enhancements:**
- Hardware-accelerated bitwise rotation (left/right) with 0-7 position encoding
- Hardware-accelerated bitwise shifting (left/right) with zero-fill
- Flexible jump instruction for program flow control
- Automatic RAM bootloading mechanism
- Custom Python-based assembler for assembly-to-hex conversion
- Ring-reset optimization reducing execution cycles by 15-19%

---

## Key Features

### Core Architectural Features

| Feature | Description |
|---------|-------------|
| **Data Bus** | 8-bit unified data path |
| **Address Bus** | 4-bit addressing (16 memory locations) |
| **Architecture** | Von Neumann (shared instruction/data memory) |
| **Instruction Cycle** | Six-phase (T₁-T₆) with ring-reset optimization |
| **Registers** | Two general-purpose registers (A, B) |
| **Memory** | 16×8 SRAM with dual read/write capability |

### Advanced Operations

**Bitwise Rotation**
- **Rotate Right (RTE)**: Circular right shift preserving all bits
- **Rotate Left (RTL)**: Circular left shift preserving all bits
- **Encoding**: MSB determines direction (0=right, 1=left), bits [2:0] specify amount (0-7)

**Bitwise Shifting**
- **Shift Right (SHR)**: Logical right shift with zero-fill from left
- **Shift Left (SHL)**: Logical left shift with zero-fill from right
- **Encoding**: MSB determines direction (0=right, 1=left), bits [2:0] specify amount (0-7)

**Control Flow**
- **Jump (JMP)**: Unconditional jump to any address (0-15)
- Early cycle termination (4 cycles vs. standard 6)

### Automation Features

- **Auto Bootloading**: Logisim RAM auto-loads program at initialization
- **Custom Assembler**: Python script converts assembly to Logisim-compatible hex
- **Ring Reset**: Dynamic cycle optimization based on instruction type

---

## Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                       8-bit Data Bus                        │
└─────────────────────────────────────────────────────────────┘
   │      │      │      │      │      │      │      │
   ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼
  PC    SRAM   Reg-A  Reg-B   ALU   Rotate  Shift   IR
   │      │      │      │      │      │      │      │
   └──────┴──────┴──────┴──────┴──────┴──────┴──────┘
                         │
                    Control Sequencer
                         │
                    Ring Counter (T₁-T₆)
```

### Component Descriptions

| Component | Function |
|-----------|----------|
| **Program Counter (PC)** | Maintains next instruction address, supports sequential increment and direct loading |
| **SRAM (16×8)** | Stores both program instructions and data with read/write control |
| **Instruction Register (IR)** | Holds fetched instruction, splits into opcode (4 MSB) and operand (4 LSB) |
| **General Purpose Registers (A, B)** | Temporary storage for operands and computational results |
| **ALU** | Executes arithmetic operations (addition, subtraction) |
| **Rotate Unit** | Performs circular bit rotation with direction/amount decoding |
| **Shift Unit** | Performs logical bit shifting with zero-fill |
| **Control Sequencer** | Generates micro-operation control signals from instruction/timing |
| **Ring Counter** | Six-phase timing signal generator (T₁-T₆) |
| **4-to-16 Decoder** | Translates 4-bit addresses to one-hot 16-bit output |

---

## Project Structure

```
SAP-1-Microprocessor-Control-Sequencer/
│
├── Sayeem_CS.circ              # Main Logisim circuit file
├── assembler.py                # Python assembler (assembly → hex)
├── script.py                   # Assembly processing script
├── input.txt                   # Assembly code input for assembler
├── output                      # Compiled output file
├── sample_program_1.txt        # Example: Shift and Rotate operations
├── sample_program_2.txt        # Example: Jump operation
├── final_report.pdf            # Complete technical documentation
├── README.md                   # This file
└── .gitignore                  # Git ignore configuration
```

---

## Installation and Usage

### Prerequisites

- **Logisim-Evolution v3.9.0** or later
- **Python 3.x** (for assembler)

### Running the Processor

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer.git
   cd SAP-1-Microprocessor-Control-Sequencer
   ```

2. **Open the circuit:**
   ```bash
   logisim-evolution Sayeem_CS.circ
   ```

3. **Load a program:**
   - Use the assembler to convert assembly code to hex
   - Load hex output into Logisim bootloader RAM
   - Enable simulation clock

### Using the Assembler

1. **Write assembly code in `input.txt`:**
   ```assembly
   LDA 15
   SHT 2
   STA 11
   HLT
   10101010
   ```

2. **Run the assembler:**
   ```bash
   python assembler.py
   ```

3. **Copy hex output:**
   ```
   v3.0 hex words addressed
   0: 1f 62 7b 50 00 00 00 00 00 00 00 00 00 00 00 aa
   ```

4. **Paste into Logisim bootloader RAM**

---

## Instruction Set

### Complete Instruction Reference

| Opcode | Mnemonic | Format | Description | Cycles |
|--------|----------|--------|-------------|--------|
| 0001 | LDA addr | 1XXX | Load Register A from memory | 6 |
| 0010 | LDB addr | 2XXX | Load Register B from memory | 6 |
| 0100 | STA addr | 4XXX | Store Register A to memory | 6 |
| 0011 | OUT addr | 3XXX | Output ALU result to memory | 5 |
| 0101 | SUB addr | 5XXX | Subtract B from A | 6 |
| 0110 | SHT n | 6XXX | Shift Register A (MSB=dir, [2:0]=amount) | 6 |
| 0111 | RTE n | 7XXX | Rotate Register A (MSB=dir, [2:0]=amount) | 6 |
| 1001 | JMP addr | 9XXX | Jump to address | 4 |
| 0101 | HLT | 5000 | Halt processor execution | 5 |

### Bitwise Operation Encoding

**Shift Instruction (SHT):**
- Operand format: `DXXX`
- `D=0`: Shift Right (SHR) with zero-fill
- `D=1`: Shift Left (SHL) with zero-fill
- `XXX`: Amount (0-7 positions)

**Rotate Instruction (RTE):**
- Operand format: `DXXX`
- `D=0`: Rotate Right (RTE) circular
- `D=1`: Rotate Left (RTL) circular
- `XXX`: Amount (0-7 positions)

**Examples:**
```
SHT 2  → 0010 (shift right 2)
SHT a  → 1010 (shift left 2)
RTE 2  → 0010 (rotate right 2)
RTE a  → 1010 (rotate left 2)
```

---

## Sample Programs

### Program 1: Shift and Rotate Operations

**File:** `sample_program_1.txt`

**Assembly Code:**
```assembly
LDA 15      ; Load 10101010 (0xAA)
SHT 2       ; Shift right by 2 → 00101010 (0x2A)
STA 11      ; Store result at address 11
LDA 15      ; Reload original value
RTE a       ; Rotate left by 2 → 10101000 (0xA8)
STA 12      ; Store result at address 12
HLT         ; Halt
10101010    ; Data at address 15
```

**Hex Code:**
```
v3.0 hex words addressed
0: 1f 62 7b 1f 8c 7c 50 00 00 00 00 00 00 00 00 aa
```

**Expected Results:**
- Memory[11] = 0x2A (shifted result)
- Memory[12] = 0xA8 (rotated result)
- Register A = 0xA8

**Binary Transformations:**
```
Original:  10101010 (170 decimal)
SHR 2:     00101010 (42 decimal)
ROL 2:     10101000 (168 decimal)
```

---

### Program 2: Jump Operation

**File:** `sample_program_2.txt`

**Assembly Code:**
```assembly
LDA 15      ; Load 11111111 (0xFF)
LDB 14      ; Load 10101010 (0xAA)
OUT 13      ; Output ALU result
SUB 12      ; Subtract (placeholder)
JMP 10      ; Jump to address 10 (skips next instructions)
SHT 2       ; Skipped
STA 11      ; Skipped
HLT         ; Execution continues from address 10
11111111    ; Data at address 15
10101010    ; Data at address 14
```

**Hex Code:**
```
v3.0 hex words addressed
0: 1f 2e 3d 4c 9a 62 7b 00 00 00 50 00 00 00 aa ff
```

**Expected Results:**
- Instructions at addresses 5-7 are skipped
- Program continues execution from address 10 (HLT)
- Demonstrates control flow manipulation

---

## Technical Specifications

### Timing Characteristics

| Instruction Type | Standard Cycles | Optimized Cycles | Savings |
|------------------|----------------|------------------|---------|
| LDA, LDB, STA | 6 | 6 | 0% |
| RTE, SHT | 6 | 6 | 0% |
| SUB, OUT | 6 | 5 | 16.7% |
| JMP | 6 | 4 | 33.3% |
| HLT | 6 | 5 | 16.7% |

**Average Performance Improvement:** 15-19% throughput increase

### Instruction Cycle Phases

**Fetch Stage (T₁-T₃):** Common to all instructions
- T₁: PC → MAR (address transfer)
- T₂: Memory → IR (instruction fetch)
- T₃: PC++ (increment counter)

**Execute Stage (T₄-T₆):** Instruction-specific
- T₄: Decode and address calculation
- T₅: Data operation (read/write/compute)
- T₆: Ring reset (or earlier for short instructions)

---

## Design Methodology

### Development Approach

1. **Component-Level Design**
   - Individual modules built from basic gates (AND, OR, NOT, XOR)
   - Flip-flops for state storage
   - Verification of isolated components

2. **Subsystem Integration**
   - Bus architecture with tri-state buffers
   - Interconnection of major functional units
   - Control signal routing

3. **Control Logic Implementation**
   - Ring counter for timing generation
   - Control sequencer for signal coordination
   - Boolean logic for micro-operations

4. **Enhancement Integration**
   - Bitwise operation units (rotate/shift)
   - Bootloader mechanism
   - Ring-reset optimization logic

5. **Testing and Validation**
   - Step-by-step instruction execution
   - Timing analysis and verification
   - Comprehensive program testing

### Key Design Decisions

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| **Bus Architecture** | Single 8-bit shared bus | Simplifies routing, reduces complexity |
| **Addressing** | 4-bit (16 locations) | Educational focus, manageable scope |
| **Timing** | Six-phase with optimization | Balance between simplicity and efficiency |
| **Bitwise Ops** | Dedicated hardware units | Single-cycle execution, no software loops |
| **Control** | Sequencer-based | Automated, synchronized operation |

---

## Performance Analysis

### Strengths

- **Functional Correctness**: All 14 instructions execute reliably across test scenarios
- **Bitwise Efficiency**: Hardware acceleration eliminates software loop overhead
- **Execution Optimization**: Ring-reset mechanism reduces average cycle time to ~5.2 cycles
- **Automation**: Auto bootloader and compiler eliminate manual programming errors
- **Modularity**: Independent subsystems enable isolated testing and debugging

### Limitations

- **Memory Constraint**: 4-bit addressing limits to 16 memory locations
- **Single Register Operations**: Bitwise operations only affect Register A
- **Encoding Limit**: 3-bit amount encoding restricts shifts/rotates to 0-7 positions
- **No Conditional Branching**: Lacks flag register for conditional operations
- **Educational Scope**: Optimized for instruction set demonstration rather than practical computation

### Future Enhancements

1. **Immediate Improvements**
   - Flag register (Zero, Carry, Negative, Overflow)
   - 8-bit addressing (256-byte memory)
   - Conditional branch instructions
   - Indexed addressing modes

2. **Advanced Extensions**
   - Stack pointer with push/pop operations
   - Subroutine support (CALL/RETURN)
   - I/O peripheral interfaces
   - Interrupt handling system
   - Microcoded control unit

---

## Documentation

### Complete Technical Report

The `final_report.pdf` provides comprehensive documentation including:
- Detailed architectural diagrams for all components
- Complete instruction set implementation with timing diagrams
- Micro-operation equations and control signal descriptions
- Step-by-step execution traces for sample programs
- Performance analysis and design trade-offs
- Comprehensive circuit schematics

### Component Schematics

All major components documented with:
- Structural design specifications
- Behavioral analysis
- Input/output signal descriptions
- Timing characteristics
- Integration details

---

## Hardware and Software Requirements

### Development Environment

| Component | Specification |
|-----------|--------------|
| **Hardware** | HP EliteBook 840 G7, Intel Core i7 10th Gen |
| **Software** | Logisim-Evolution v3.9.0 |
| **Assembler** | Python 3.x |
| **Operating System** | Windows/Linux/macOS compatible |

### Simulation Requirements

- Minimum 4GB RAM
- 1280×720 display resolution or higher
- Java Runtime Environment (for Logisim)

---

## Author

**S M Shahriar**

Computer Architecture and Digital System Design  
Enhanced SAP-1 Microprocessor Project

### Connect With Me

- **GitHub**: [Sayeem-Velocity](https://github.com/Sayeem-Velocity)
- **LinkedIn**: [S M Shahriar](https://www.linkedin.com/in/s-m-shahriar-26s/)
- **Portfolio Website**: [sm-shahriar.netlify.app](https://sm-shahriar.netlify.app/)
- **Project Repository**: [SAP-1-Microprocessor-Control-Sequencer](https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer)
- **Video Demonstration**: [YouTube](https://youtu.be/epArGkpsPSU)

---

## License

This project is provided for educational purposes. Feel free to use, modify, and distribute with proper attribution.

---

## Acknowledgments

This project builds upon the foundational SAP-1 architecture concept while introducing modern enhancements for educational and practical exploration of computer architecture principles.

---

**Last Updated:** October 6, 2025  
**Version:** 1.0  
**Status:** Complete and Functional

---

*For issues, questions, or contributions, please open an issue on the [GitHub repository](https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer).*