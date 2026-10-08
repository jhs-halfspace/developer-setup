# Cursor Vim Cheatsheet

Your setup: **VSCodeVim** in **Cursor** on **macOS**.
Leader key: **Space**

> This cheatsheet covers motions, editing, and navigation within a single file.
> Your config delegates `Ctrl+A/C/X/F/Z` to Cursor (native copy/paste/find/undo work as usual).

---

## Modes

| Mode         | Enter with          | Back to Normal        |
|--------------|---------------------|-----------------------|
| Normal       | `Esc`               | —                     |
| Insert       | `i` / `a` / `o`     | `Esc`                 |
| Insert       | `I` (line start) / `A` (line end) / `O` (line above) | `Esc` |
| Visual       | `v` (char)          | `Esc`                 |
| Visual Line  | `V` (line)          | `Esc`                 |
| Visual Block | `Ctrl+v`            | `Esc`                 |

---

## Basic Movement (Normal mode)

| Action                      | Keys               |
|-----------------------------|---------------------|
| Move cursor (←↓↑→)         | `h` `j` `k` `l`   |
| Word forward / back         | `w` / `b`          |
| End of word                 | `e`                |
| Start / end of line         | `0` / `$`          |
| First non-blank char        | `^`                |
| Half page down / up         | `Ctrl+d` / `Ctrl+u` |
| Go to line N                | `{N}G` or `:{N}`   |
| Go to top / bottom of file  | `gg` / `G`         |
| Jump to matching bracket    | `%`                |
| Jump list back / forward    | `Ctrl+o` / `Ctrl+i` |

> `j` and `k` move by **display line** (wrapped lines), matching LazyVim behavior.

---

## Search & Jump

| Action                      | Keys                       |
|-----------------------------|----------------------------|
| Search forward              | `/pattern` then `Enter`    |
| Search backward             | `?pattern` then `Enter`    |
| Next / previous match       | `n` / `N`                  |
| Clear search highlight      | `Esc`                      |
| Incremental search          | enabled (matches show as you type) |

### Sneak (2-char jump, similar to flash.nvim)

| Action                      | Keys                       |
|-----------------------------|----------------------------|
| Jump forward to `xy`        | `s` then `x` `y`          |
| Jump backward to `xy`       | `S` then `x` `y`          |
| Operator forward             | `z` then `x` `y` (e.g. `dz..`) |
| Operator backward            | `Z` then `x` `y`          |

### EasyMotion (label-hop, `<leader><leader>` prefix)

| Action                      | Keys                       |
|-----------------------------|----------------------------|
| Search character             | `Space Space s {char}`     |
| Word forward                 | `Space Space w`            |
| Word backward                | `Space Space b`            |
| Line forward                 | `Space Space j`            |
| Line backward                | `Space Space k`            |
| Find char forward            | `Space Space f {char}`     |
| Find char backward           | `Space Space F {char}`     |
| 2-char search                | `Space Space 2s {char}{char}` |

---

## Editing (Normal mode)

| Action                      | Keys               |
|-----------------------------|---------------------|
| Delete character            | `x`                |
| Delete word                 | `dw`               |
| Delete line                 | `dd`               |
| Delete to end of line       | `D`                |
| Change word (delete+insert) | `cw`               |
| Change line                 | `cc`               |
| Change to end of line       | `C`                |
| Change inside quotes        | `ci"` / `ci'`      |
| Change inside parens        | `ci(` / `ci{` / `ci[` |
| Delete inside quotes        | `di"` / `di'`      |
| Delete inside parens        | `di(` / `di{` / `di[` |
| Undo                        | `u`                |
| Redo                        | `Ctrl+r`           |
| Yank (copy) line            | `yy`               |
| Yank word                   | `yw`               |
| Paste after / before        | `p` / `P`          |
| Repeat last action          | `.`                |
| Join line below             | `J`                |
| Toggle comment              | `gcc` (line) / `gc{motion}` |
| Block comment               | `gCi)` (inside parens, etc.) |

---

## Surround (vim-surround, built-in)

| Action                      | Keys                       |
|-----------------------------|----------------------------|
| Add surround                | `ys{motion}{char}`         |
| Delete surround             | `ds{char}`                 |
| Change surround             | `cs{old}{new}`             |
| Surround selection (visual) | `S{char}`                  |

Examples:
- `ysiw"` — surround word with `"`
- `cs"'` — change `"hello"` to `'hello'`
- `ds(` — remove surrounding parens
- `yss)` — surround entire line with `()`
- Visual: select text, then `S<div>` to wrap in tag

---

## Text Objects

Use with operators (`d`, `c`, `y`, `v`): `{operator}{a|i}{object}`

| Object    | `i` (inner)         | `a` (around, includes delimiters) |
|-----------|---------------------|-----------------------------------|
| Word      | `iw`                | `aw`                              |
| WORD      | `iW`                | `aW`                              |
| Sentence  | `is`                | `as`                              |
| Paragraph | `ip`                | `ap`                              |
| `"` `'` `` ` `` | `i"` `i'` `` i` `` | `a"` `a'` `` a` ``          |
| `()` `{}`  `[]` | `i(` `i{` `i[`    | `a(` `a{` `a[`                   |
| Tag       | `it`                | `at`                              |
| Indentation | `ii`              | `ai` / `aI` (includes line above/below) |

Examples:
- `ci"` — change inside double quotes
- `dap` — delete entire paragraph
- `yat` — yank around HTML tag
- `>ii` — indent this indentation block

---

## Visual Mode

| Action                      | Keys               |
|-----------------------------|---------------------|
| Enter char visual           | `v`                |
| Enter line visual           | `V`                |
| Enter block visual          | `Ctrl+v`           |
| Expand selection (VS Code)  | `af`               |
| Indent (repeatable)         | `>`                |
| Outdent (repeatable)        | `<`                |
| Move lines down             | `J`                |
| Move lines up               | `K`                |
| Paste (keeps register)      | `p`                |
| Reselect last selection     | `gv`               |
| Select to end of line       | `v$`               |
| Select inner word           | `viw`              |

---

## Custom Bindings (Normal mode)

These are your custom remaps from `settings.json`:

| Action                      | Keys               |
|-----------------------------|---------------------|
| Clear search highlight      | `Esc`              |
| Previous tab                | `H` (Shift+h)     |
| Next tab                    | `L` (Shift+l)     |
| Split vertical              | `Space \|`         |
| Split horizontal            | `Space -`          |
| Go to references            | `gr`               |
| Hover documentation         | `K`                |
| Code action / quick fix     | `Space c a`        |
| Next diagnostic             | `]d`               |
| Previous diagnostic         | `[d`               |

---

## Code (LSP) — Built-in

These work out of the box with VSCodeVim:

| Action                      | Keys               |
|-----------------------------|---------------------|
| Go to definition            | `gd`               |
| Go to references            | `gr` (custom remap) |
| Hover documentation         | `K` (custom remap) |
| Code action / quick fix     | `Space c a` (custom remap) |
| Rename symbol               | `F2` (Cursor native) |
| Format file                 | `Cmd+Shift+F` or `Shift+Option+F` (Cursor native) |
| Next / prev diagnostic      | `]d` / `[d` (custom remap) |

---

## Multi-Cursor

| Action                      | Keys               |
|-----------------------------|---------------------|
| Add cursor at next match    | `gb`               |
| Add cursor above            | `Cmd+Option+Up`    |
| Add cursor below            | `Cmd+Option+Down`  |

---

## Differences from Your Neovim Setup

| Feature              | Neovim (LazyVim)         | Cursor (VSCodeVim)           |
|----------------------|--------------------------|-------------------------------|
| Escape insert        | `Esc`                    | `Esc`                        |
| Jump (2-char)        | `s` (flash.nvim)         | `s` (sneak) + EasyMotion     |
| Surround             | `ys`/`ds`/`cs` + `gz*`  | `ys`/`ds`/`cs` only          |
| Clear highlight      | `Esc`                    | `Esc`                        |
| Buffer navigation    | `Shift+H/L`, `[b`/`]b`  | `Shift+H/L` (tabs)           |
| Visual block         | `Ctrl+v`                 | `Ctrl+v`                     |
| Which-key popup      | press `Space` and wait   | N/A (memorize keys)          |
| Telescope            | `Space f f`, etc.        | use `Cmd+P` (Cursor native)  |
| Live grep            | `Space s g`              | use `Cmd+Shift+F` (Cursor)   |
| Terminal / Panes     | Zellij `Alt+...`         | Cursor integrated terminal   |
| Flash labels         | `s` + type + label       | `s` + 2 chars (sneak style)  |
| Save file            | `Space w` or `:w`        | `:w` or `Cmd+S`              |
| Close buffer         | `Space b d`              | `Cmd+W`                      |
| Rename symbol        | `Space c r`              | `F2`                         |
| Format file          | `Space c f`              | `Shift+Option+F`             |

---

## Quick Equivalents: Neovim → Cursor

| Neovim                | Cursor equivalent          |
|-----------------------|----------------------------|
| `Space f f` (find file) | `Cmd+P`                  |
| `Space s g` (grep)    | `Cmd+Shift+F`             |
| `Space ,` (buffers)   | `Cmd+P` then type         |
| `Space :` (commands)  | `Cmd+Shift+P`             |
| `Space e` (explorer)  | `Cmd+Shift+E` (sidebar)   |
| `Space q q` (quit)    | `Cmd+Q`                   |
| `:w` (save)           | `:w` or `Cmd+S`           |
| `gcc` (comment)       | `gcc` (same!)              |
| `gd` (go to def)      | `gd` (same!)               |
| `K` (hover)           | `K` (same!)                |

---

## Performance Tip

The `extensions.experimental.affinity` setting is enabled in your config,
which runs VSCodeVim in a dedicated thread for better responsiveness.
