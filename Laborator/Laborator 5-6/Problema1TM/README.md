# 🧠 Turing Machine Simulator
---

## 🔧 How it works

The simulator reads a `.json` file which contains:
- a list of **states** (`stari`)
- the **tape alphabet** (`alfabet_banda`)
- the **blank symbol** (`simbol_vid`)
- the **initial state** (`stare_initiala`)
- the list of **final states** (`stari_finale`)
- a set of **transition rules** (`reguli`)

Each transition rule specifies:
- current state and symbol read
- the next state
- symbol to write
- movement direction (L = left, D = right, N/S = stay)

---

## 📁 JSON Programs (Turing Machines)

### `config_bitadder.json`

- **What it does:** Adds 1 to a binary number on the tape (e.g., `111` → `1000`).
- **Input format:** A binary string ending with `_` (e.g., `101_`)
- **Output:** The incremented binary value.

---

### `config_2noadder.json`

- **What it does:** Adds two binary numbers separated by a `+` (e.g., `1+1`)
- **Input format:** `0+0`, `1+0`, or `1+1` (followed by `_`)
- **Output:** Binary result after `=` (e.g., `1+1=` → `10`)

---

### `config_copy.json`

- **What it does:** Copies a binary string from before `$` to after `#`
- **Input format:** A binary string like `101$#_`
- **Output:** Tape contains the copied version after `#`, e.g., `101$#101`

---

### `conif_equalitycheck.json`

- **What it does:** Compares two binary numbers separated by `$` and accepts only if they are equal.
- **Input format:** e.g., `101$101`
- **Output:** Machine halts in accept state only if both numbers match.

---

### `palindromecheck.json`

- **What it does:** Checks if a binary string is a palindrome.
- **Input format:** Any binary string (e.g., `101`, `1001`)
- **Output:** Accepts only if the string is a palindrome.

