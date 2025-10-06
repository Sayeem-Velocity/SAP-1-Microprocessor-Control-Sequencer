import re

# Opcodes by class
packed_ops = {  # base byte + 4-bit operand (0..15)
    "LDA": 0x10, "LDB": 0x20, "OUT": 0x30, "SUB": 0x40, "SHT": 0x60,
    "STA": 0x70, "RTE": 0x80, "JMP": 0x90
}
single_ops = {  # single-byte opcodes
    "HLT": 0x50
}

# (Optional) Immediate operations if you later add them
immediate_ops = {}  # keep empty unless needed

def parse_byte_token(tok: str) -> int:
    """Parse a standalone byte: hex ('55','0x55') or decimal ('85')."""
    tok = tok.strip()
    if tok.lower().startswith("0x"):
        return int(tok, 16) & 0xFF
    if re.fullmatch(r"[0-9A-Fa-f]{2}", tok):
        return int(tok, 16) & 0xFF
    return int(tok, 10) & 0xFF


input_file = "input.txt"
output_file = "output"

with open(input_file, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

bytes_out = []
i = 0
while i < len(raw_lines):
    line = raw_lines[i].strip()
    i += 1

    # Insert 00 for any blank line
    if not line:
        bytes_out.append("00")
        continue

    parts = line.split()
    up0 = parts[0].upper()

    # Literal byte line (e.g., "00", "55", "0x1A")
    if re.fullmatch(r"(?:0x)?[0-9A-Fa-f]{2}", parts[0]) or parts[0].isdigit():
        b = parse_byte_token(parts[0])
        bytes_out.append(f"{b:02x}")
        continue

    # Packed (nibble) ops
    if up0 in packed_ops:
        if len(parts) < 2:
            raise ValueError(f"Missing operand for {up0}")
        op_str = parts[1]
        try:
            if op_str.lower().startswith("0x"):
                operand = int(op_str, 16)
            elif re.fullmatch(r"[0-9A-Fa-f]{1,2}", op_str) and not op_str.isdigit():
                operand = int(op_str, 16)
            else:
                operand = int(op_str, 10)
        except ValueError:
            raise ValueError(f"Bad operand '{op_str}' for {up0}")
        if not (0 <= operand <= 15):
            raise ValueError(f"Operand for {up0} must be 0..15, got {operand}")
        b = (packed_ops[up0] + (operand & 0x0F)) & 0xFF
        bytes_out.append(f"{b:02x}")
        continue

    # Single-byte ops
    if up0 in single_ops:
        bytes_out.append(f"{single_ops[up0]:02x}")
        continue

    # Immediate ops (if ever added)
    if up0 in immediate_ops:
        bytes_out.append(f"{immediate_ops[up0]:02x}")
        if len(parts) >= 2:
            imm_tok = parts[1]
        else:
            while i < len(raw_lines) and not raw_lines[i].strip():
                i += 1
            if i >= len(raw_lines):
                raise ValueError(f"Missing immediate byte after {up0}")
            imm_tok = raw_lines[i].strip()
            i += 1
        imm_val = parse_byte_token(imm_tok)
        bytes_out.append(f"{imm_val:02x}")
        continue

    raise ValueError(f"Unrecognized opcode or token: '{line}'")

# Emit in v3.0 format
out_lines = ["v3.0 hex words addressed", f"0: {' '.join(bytes_out)}"]
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
