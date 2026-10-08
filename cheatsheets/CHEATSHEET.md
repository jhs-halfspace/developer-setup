# Dev Setup Cheat Sheet

Your setup: **LazyVim** (Neovim) inside **Zellij** (terminal multiplexer) on **macOS**.
Leader key: **Space**

### macOS Keyboard Reference

| Cheat sheet notation | Mac key            | Symbol |
|----------------------|--------------------|--------|
| `Ctrl`               | `control` (bottom-left) | `⌃` |
| `⌥`                 | `Option` (next to Cmd)  | `⌥` |
| `Shift`              | `shift`                 | `⇧` |

> **Important — Ghostty setup**: For the `⌥` (Option) shortcuts in Zellij to work,
> your Ghostty config must include `macos-option-as-alt = true`. Without this,
> macOS intercepts Option and types special characters instead of sending Alt.
> Add this line to your Ghostty config file (`~/.config/ghostty/config`).

---

## Zellij (terminal multiplexer)

Zellij starts in **locked mode** — most keys go straight to Neovim.
You must unlock it to use Zellij commands.

| Action                  | Keys                          |
|-------------------------|-------------------------------|
| Unlock (normal mode)    | `Ctrl+g`                      |
| Lock (back to Neovim)   | `Ctrl+g`                      |
| Switch tab left/right   | `⌥+i` / `⌥+o`               |
| New pane                | `⌥+n`                        |
| Focus pane (vim-style)  | `⌥+h/j/k/l`                  |
| Toggle floating pane    | `⌥+f`                        |
| Resize panes            | `⌥+-` / `⌥+=`               |
| Pane mode               | `Ctrl+p` (then arrows/hjkl)   |
| Tab mode                | `Ctrl+t` (then arrows/n/r)    |
| Scroll mode             | `Ctrl+s` (then j/k/PgUp/PgDn)|
| Session manager         | `Ctrl+b`                      |
| Detach session          | `Ctrl+x` (works while locked) |
| Quit                    | `Ctrl+q` (must be unlocked)   |

Your layout has 3 tabs: **Neovim** | **OpenCode** | **Terminal**.
Use `⌥+i` / `⌥+o` to switch between them without unlocking.

---

## Neovim — Modes

| Mode      | Enter with         | Back to Normal      |
|-----------|---------------------|----------------------|
| Normal    | `Esc`               | —                    |
| Insert    | `i` (before cursor) | `Esc`                |
| Insert    | `a` (after cursor)  | `Esc`                |
| Insert    | `o` (new line below)| `Esc`                |
| Insert    | `I` (start of line) | `Esc`                |
| Insert    | `A` (end of line)   | `Esc`                |
| Visual    | `v` (char select)   | `Esc`                |
| V-Line    | `V` (line select)   | `Esc`                |
| V-Block   | `Ctrl+v` (`⌃v`)    | `Esc`                |
| Command   | `:`                 | `Esc` or `Enter`     |

---

## Neovim — Basic Movement (Normal mode)

| Action                       | Keys              |
|------------------------------|--------------------|
| Move cursor (←↓↑→)          | `h` `j` `k` `l`   |
| Word forward / back          | `w` / `b`          |
| End of word                  | `e`                |
| Start / end of line          | `0` / `$`          |
| First non-blank char         | `^`                |
| Top / middle / bottom screen | `H` / `M` / `L`   |
| Half page down / up          | `Ctrl+d` / `Ctrl+u` |
| Go to line N                 | `{N}G` or `:{N}`   |
| Go to top / bottom of file   | `gg` / `G`         |
| Jump to matching bracket     | `%`                |

---

## Neovim — Editing Essentials (Normal mode)

| Action                     | Keys              |
|----------------------------|--------------------|
| Delete character           | `x`                |
| Delete word                | `dw`               |
| Delete line                | `dd`               |
| Delete to end of line      | `D`                |
| Change word (delete+insert)| `cw`               |
| Change line                | `cc`               |
| Change to end of line      | `C`                |
| Undo                       | `u`                |
| Redo                       | `Ctrl+r`           |
| Yank (copy) line           | `yy`               |
| Yank word                  | `yw`               |
| Paste after / before       | `p` / `P`          |
| Repeat last action         | `.`                |
| Join line below            | `J`                |
| Indent / unindent (visual) | `>` / `<`          |

---

## Neovim — Search & Replace

| Action                     | Keys                       |
|----------------------------|----------------------------|
| Search forward             | `/pattern` then `Enter`    |
| Search backward            | `?pattern` then `Enter`    |
| Next / previous match      | `n` / `N`                  |
| Clear search highlight     | `Esc` (LazyVim default)    |
| Search & replace (file)    | `:%s/old/new/g`            |
| Search & replace (confirm) | `:%s/old/new/gc`           |
| Flash jump (label-hop)     | `s` then type chars        |
| Project-wide search/replace| `<leader>sr` (grug-far)    |

---

## Neovim — File Navigation (Telescope & friends)

**All `<leader>` commands: press Space, then the key sequence.**

| Action                      | Keys               |
|-----------------------------|---------------------|
| **Find file** by name       | `<leader>ff`        |
| Find recent file             | `<leader>fr`        |
| Find file (git files)        | `<leader><space>`   |
| **Live grep** (search text)  | `<leader>sg`        |
| Live grep (incl. hidden)     | `<leader>sag`       |
| Search word under cursor     | `<leader>sw`        |
| Search buffers               | `<leader>,`         |
| Search help tags             | `<leader>sh`        |
| Search keymaps               | `<leader>sk`        |
| Search commands              | `<leader>:`         |

Inside Telescope:
| Action                       | Keys               |
|------------------------------|---------------------|
| Navigate results             | `Ctrl+j` / `Ctrl+k` or arrows |
| Open file                    | `Enter`             |
| Open in split                | `Ctrl+x`            |
| Open in vsplit               | `Ctrl+v`            |
| Close Telescope              | `Esc`               |

---

## Neovim — Buffers & Windows

| Action                     | Keys                       |
|----------------------------|----------------------------|
| Next / prev buffer         | `]b` / `[b`  or `Shift+l` / `Shift+h` |
| Close buffer               | `<leader>bd`               |
| Close other buffers        | `<leader>bo`               |
| List buffers               | `<leader>,`                |
| Split horizontal           | `<leader>-`                |
| Split vertical             | `<leader>\|`               |
| Navigate splits            | `Ctrl+h/j/k/l`            |
| Close window               | `<leader>wd`               |
| Equalize window sizes      | `Ctrl+w` then `=`          |

---

## Neovim — Harpoon (quick-access file marks)

| Action                     | Keys                       |
|----------------------------|----------------------------|
| Add file to harpoon        | `<leader>ha` (check which-key) |
| Toggle harpoon menu        | `<leader>hm` or `<leader>h` group |

*Press `<leader>` and look at the which-key popup for the exact Harpoon keys — the LazyVim Harpoon2 extra registers them under `<leader>h` or numbered keys.*

---

## Neovim — LSP (code intelligence)

| Action                       | Keys                |
|------------------------------|----------------------|
| Go to definition             | `gd`                 |
| Go to references             | `gr`                 |
| Go to implementation         | `gI`                 |
| Go to type definition        | `gy`                 |
| Hover documentation          | `K`                  |
| Signature help (insert mode) | `Ctrl+k`             |
| Rename symbol                | `<leader>cr`         |
| Code action                  | `<leader>ca`         |
| Format file                  | `<leader>cf`         |
| Next / prev diagnostic       | `]d` / `[d`          |
| Diagnostics list (Trouble)   | `<leader>xx`         |

---

## Neovim — Git (gitsigns)

| Action                      | Keys                |
|-----------------------------|----------------------|
| Next / prev hunk            | `]h` / `[h`         |
| Stage hunk                  | `<leader>ghs`       |
| Reset hunk                  | `<leader>ghr`       |
| Preview hunk                | `<leader>ghp`       |
| Blame line                  | `<leader>ghb`       |
| Git status (Telescope)      | `<leader>gs`         |

---

## Neovim — The Which-Key Cheat Code

**When in doubt, just press `<leader>` (Space) and wait.**
A popup (which-key) will show you every available command grouped by category:

| Prefix         | Category            |
|----------------|---------------------|
| `<leader>b`    | Buffers             |
| `<leader>c`    | Code (LSP)          |
| `<leader>d`    | Debug               |
| `<leader>f`    | File/Find           |
| `<leader>g`    | Git                 |
| `<leader>h`    | Harpoon             |
| `<leader>q`    | Quit/Session        |
| `<leader>s`    | Search              |
| `<leader>u`    | UI toggles          |
| `<leader>w`    | Windows             |
| `<leader>x`    | Diagnostics/Trouble |

---

## Survival Workflow

1. **Open your project**: run `workon <project>` (starts Zellij with Neovim tab)
2. **Find a file**: `Space` `f` `f` → type part of the filename → `Enter`
3. **Search for text**: `Space` `s` `g` → type your search → `Enter`
4. **Edit**: press `i` to insert, `Esc` when done
5. **Save**: `Space` → wait for which-key → look for save, or just `:w`
6. **Switch files**: `Space` `,` to pick from open buffers
7. **Go to definition**: hover cursor on a symbol, press `gd`
8. **Go back**: `Ctrl+o` (jump list back), `Ctrl+i` (forward)
9. **Terminal**: `⌥+o` to switch to the Terminal tab in Zellij
10. **Quit Neovim**: `:qa` (quit all) or `<leader>qq`
