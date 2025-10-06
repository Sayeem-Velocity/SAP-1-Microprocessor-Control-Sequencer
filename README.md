# SAP-1 Microprocessor Control Sequencer

A complete SAP-1 (Simple As Possible) microprocessor architecture implementation with interactive web-based assembler and Python compiler.

## 📁 Project Structure

```
SAP1-Architecture/
├── assembler.py              # Python-based assembler script
├── assembler.html            # Advanced interactive web assembler
├── assembler_interface.html  # Standalone web interface
├── script.py                 # Assembly processing script
├── input.txt                 # Assembly input file
├── output                    # Compiled output file
├── Sayeem_CS.circ           # Logisim circuit file
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🚀 Features

### Web-Based Assembler
- **Interactive HTML Interface** with modern dark theme
- **Real-time compilation** with syntax validation
- **Opcode configuration** with JSON upload support
- **Export options**: Copy to clipboard, download .hex files
- **Smart labels** and jump instructions
- **Blank line handling** (auto-converts to 0x00)
- **Error detection** with helpful messages

### Python Assembler
- Command-line assembly compilation
- Multiple number formats (hex, decimal, binary)
- v3.0 hex format output for Logisim
- Packed and single-byte opcodes

## 📋 Supported Instructions

| Instruction | Opcode | Description | Format |
|-------------|--------|-------------|--------|
| **LDA** | 0x10 + operand | Load A Register | `LDA address` |
| **LDB** | 0x20 + operand | Load B Register | `LDB address` |
| **OUT** | 0x30 + operand | Output | `OUT port` |
| **SUB** | 0x40 + operand | Subtract | `SUB address` |
| **HLT** | 0x50 | Halt | `HLT` |
| **SHT** | 0x60 + operand | Shift | `SHT amount` |
| **STA** | 0x70 + operand | Store A | `STA address` |
| **RTE** | 0x80 + operand | Return | `RTE address` |
| **JMP** | 0x90 + operand | Jump | `JMP address` |

**Note**: Operands must be in range 0-15 (4-bit nibble)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.x (for Python assembler)
- Modern web browser (for HTML interface)
- Git (for version control)

### Clone Repository
```bash
git clone https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer.git
cd SAP-1-Microprocessor-Control-Sequencer
```

### Python Setup
```bash
# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 💻 Usage

### Option 1: Web Interface (Recommended)

1. **Open the interactive assembler:**
   ```bash
   # Simply open in browser
   start assembler.html
   # or
   start assembler_interface.html
   ```

2. **Enter assembly code** in the left panel
3. **Click "Compile Assembly"** or press `Ctrl+Enter`
4. **View output** in the right panel
5. **Export**: Copy to clipboard or download as .hex file

**Features:**
- Upload custom opcode mappings (JSON format)
- Real-time error detection
- Syntax highlighting
- Example code templates

### Option 2: Python CLI

1. **Create your assembly code** in `input.txt`:
   ```assembly
   LDA 1
   LDB 2
   OUT 0
   SUB 3
   STA 10
   JMP 0
   HLT
   ```

2. **Run the assembler:**
   ```bash
   python assembler.py
   ```

3. **Output** is generated in the `output` file in v3.0 format:
   ```
   v3.0 hex words addressed
   0: 11 22 30 43 7a 90 50
   ```

### Option 3: Script Mode

```bash
python script.py
```

## 📝 Assembly Language Syntax

### Basic Format
```assembly
OPCODE operand    # Comment
```

### Examples

**Simple Program:**
```assembly
LDA 5        # Load value from address 5
LDB 6        # Load value from address 6
SUB 0        # Subtract B from A
OUT 0        # Output result
HLT          # Halt execution
```

**With Labels:**
```assembly
START:  LDA 1
        LDB 2
        SUB 0
LOOP:   OUT 0
        JMP LOOP
        HLT
```

**With Blank Lines (auto 0x00):**
```assembly
LDA 1

LDB 2

HLT
```

**Data Declarations:**
```assembly
ORG 0
        LDA 10
        OUT 0
        HLT

ORG 10
        DEC 42    # Decimal data
        DEC 0xFF  # Hex data
```

### Number Formats
- **Decimal**: `42`, `255`
- **Hexadecimal**: `0xFF`, `0x1A`, `FF`
- **Binary**: `0b11010`

## 🔧 Opcode Configuration

### Upload Custom Opcodes (Web Interface)

1. Create a JSON file (`opcodes.json`):
   ```json
   {
     "LDA": "0x1",
     "LDB": "0x2",
     "OUT": "0x3",
     "SUB": "0x4",
     "HLT": "0x5",
     "SHT": "0x6",
     "STA": "0x7",
     "RTE": "0x8",
     "JMP": "0x9"
   }
   ```

2. Click **"Upload Mapping"** button
3. Select your JSON file
4. Opcodes are updated automatically

### Modify Python Opcodes

Edit `assembler.py`:
```python
packed_ops = {
    "LDA": 0x10, "LDB": 0x20, "OUT": 0x30, 
    "SUB": 0x40, "SHT": 0x60, "STA": 0x70, 
    "RTE": 0x80, "JMP": 0x90
}
single_ops = {
    "HLT": 0x50
}
```

## 🎯 Git Commands Reference

### Initial Setup
```bash
# Initialize repository
git init

# Add remote origin
git remote add origin https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer.git

# Check remote
git remote -v
```

### Daily Workflow
```bash
# Check status
git status

# Add files
git add .                    # Add all files
git add assembler.py         # Add specific file
git add *.html              # Add all HTML files

# Commit changes
git commit -m "Add interactive web assembler"
git commit -m "Fix opcode parsing bug"
git commit -m "Update documentation"

# Push to GitHub
git push origin main
git push -u origin main     # First time push

# Pull latest changes
git pull origin main
```

### Branch Management
```bash
# Create new branch
git branch feature-name
git checkout -b feature-name  # Create and switch

# Switch branches
git checkout main
git checkout feature-name

# List branches
git branch -a

# Merge branch
git checkout main
git merge feature-name

# Delete branch
git branch -d feature-name
```

### View History
```bash
# View commit history
git log
git log --oneline
git log --graph --oneline --all

# View changes
git diff
git diff HEAD~1              # Compare with previous commit
git diff branch-name         # Compare with branch
```

### Undo Changes
```bash
# Discard local changes
git checkout -- filename
git restore filename

# Unstage files
git reset HEAD filename
git restore --staged filename

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

### Stash Changes
```bash
# Save work in progress
git stash
git stash save "Work in progress"

# List stashes
git stash list

# Apply stash
git stash apply
git stash pop               # Apply and remove

# Clear stash
git stash clear
```

### Collaboration
```bash
# Fork workflow
git clone https://github.com/YOUR-USERNAME/SAP-1-Microprocessor-Control-Sequencer.git
git remote add upstream https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer.git

# Sync fork
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Tags & Releases
```bash
# Create tag
git tag v1.0.0
git tag -a v1.0.0 -m "First stable release"

# Push tags
git push origin v1.0.0
git push origin --tags

# List tags
git tag -l

# Delete tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## 🐛 Troubleshooting

### Common Issues

**Error: "Missing operand for LDA"**
- Ensure all packed operations have an operand (0-15)
- Example: `LDA 5` not just `LDA`

**Error: "Operand must be 0-15"**
- Packed operations use 4-bit operands
- Range: 0-15 (decimal) or 0x0-0xF (hex)

**Error: "Unrecognized opcode"**
- Check spelling and capitalization
- Verify opcode is in the supported instruction set

**Python Import Error**
- Run `pip install -r requirements.txt`
- Check Python version (3.x required)

**Git Push Rejected**
```bash
# Pull first, then push
git pull origin main --rebase
git push origin main
```

## 📚 Additional Resources

- [SAP-1 Architecture Overview](https://en.wikipedia.org/wiki/Simple_As_Possible_computer)
- [Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution)
- [Assembly Language Basics](https://en.wikipedia.org/wiki/Assembly_language)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Sayeem-Velocity**
- GitHub: [@Sayeem-Velocity](https://github.com/Sayeem-Velocity)
- Repository: [SAP-1-Microprocessor-Control-Sequencer](https://github.com/Sayeem-Velocity/SAP-1-Microprocessor-Control-Sequencer)

## 🙏 Acknowledgments

- Inspired by the SAP-1 (Simple As Possible) architecture
- Built for educational purposes and microprocessor design learning

---

**Last Updated**: October 6, 2025

For issues or questions, please open an issue on GitHub.
