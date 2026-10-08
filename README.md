# developer-setup

My macOS dev environment: zsh, git aliases, starship prompt, Ghostty/cmux.

## Layout

| Path | What | Linked to |
|---|---|---|
| `dotfiles/zshrc` | Shell config | `~/.zshrc` |
| `dotfiles/git_aliases.zsh` | Oh-My-Zsh style git aliases (`gs`, `gco`, `gcm`, ...) | sourced by `zshrc` |
| `starship/starship.toml` | Prompt | `~/.config/starship.toml` |
| `ghostty/config` | Terminal theme | `~/.config/ghostty/` and cmux's `config.ghostty` |
| `cheatsheets/` | Notes, not linked | — |

## Setup on a new machine

```bash
# 1. Homebrew + packages
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"
brew install starship zsh-autosuggestions zsh-syntax-highlighting nvm
brew install --cask ghostty font-jetbrains-mono-nerd-font

# 2. Clone (any location works; zshrc finds the repo through its own symlink)
git clone git@github.com:jhs-halfspace/developer-setup.git ~/workspace/repos/developer-setup

# 3. Link everything
~/workspace/repos/developer-setup/install.sh
exec zsh
```

Check it worked: `type gcm` should print the alias.

## Machine-specific config

Anything client- or machine-specific (GCP projects, client helper functions) goes in
`~/.zshrc.local`, which `zshrc` sources if it exists. It is not in this repo — keep a copy
somewhere safe.

`install.sh` never deletes real files: anything that isn't already a symlink is moved to
`<name>.backup` first.
