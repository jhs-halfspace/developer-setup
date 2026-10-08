# developer-setup

My macOS dev environment: zsh, git aliases, starship prompt, Ghostty/cmux.

## Layout

| Path | What | Linked to |
|---|---|---|
| `dotfiles/zshrc` | Shell config | `~/.zshrc` |
| `dotfiles/git_aliases.zsh` | Oh-My-Zsh style git aliases (`gs`, `gco`, `gcm`, ...) | sourced by `zshrc` |
| `starship/starship.toml` | Prompt | `~/.config/starship.toml` |
| `ghostty/config` | Terminal theme | `~/.config/ghostty/` and cmux's `config.ghostty` |
| `Brewfile` | Core packages the configs above depend on | — |
| `Brewfile.extra` | Optional work tooling (Azure, k8s, docker, Postgres, Flutter, VS Code extensions) | — |
| `cheatsheets/` | Notes, not linked | — |

## Setup on a new machine

Do the steps in order — each one depends on the one before.

### 1. Xcode Command Line Tools

Gives you `git` and a compiler; Homebrew needs them.

```bash
xcode-select --install
```

### 2. Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Make brew available in this shell (the zshrc does this permanently once linked)
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 3. Clone this repo

There are no SSH keys on a fresh machine yet, so clone over HTTPS. You can switch
to SSH later (step 7).

```bash
mkdir -p ~/workspace/repos
git clone https://github.com/jhs-halfspace/developer-setup.git ~/workspace/repos/developer-setup
cd ~/workspace/repos/developer-setup
```

Any location works — `zshrc` finds the repo through its own symlink.

### 4. Install packages

```bash
brew bundle --file=Brewfile          # core — required
brew bundle --file=Brewfile.extra    # optional — work tooling, takes a while
```

| Core package | Needed for |
|---|---|
| `starship` | The prompt |
| `zsh-autosuggestions`, `zsh-syntax-highlighting` | Sourced by `zshrc` — **the shell errors on startup without them** |
| `git`, `gh` | Git + GitHub auth |
| `worktrunk` | `wt`, and the `wts` / `wtl` aliases |
| `neovim` | `$EDITOR` |
| `fzf`, `fd` | Fuzzy finding |
| `uv`, `poetry` | Python |
| `nvm` | Node versions |
| `ghostty`, `cmux` | Terminals |
| `font-jetbrains-mono-nerd-font` | Icons in the prompt — without it you get boxes |
| `claude-code` | Claude Code |

Everything else `zshrc` references (Postgres, Java, Android SDK, Azure CLI, mise/go, bun) is
optional — it's guarded or harmless when missing.

### 5. Check for existing config files

`install.sh` replaces these with symlinks. Real files are moved to `<name>.backup`, never
deleted — but look first if you've customised anything:

```bash
ls -la ~/.zshrc ~/.config/starship.toml ~/.config/ghostty \
  ~/Library/Application\ Support/com.cmuxterm.app/config.ghostty
```

### 6. Run the install script

```bash
./install.sh
exec zsh
```

Verify:

```bash
type gcm        # → gcm is an alias for git checkout $(git_main_branch)
type wts        # → wts is an alias for wt switch
ls -l ~/.zshrc  # → points into this repo
```

Then set the terminal font to **JetBrainsMono Nerd Font** if the prompt shows boxes.

### 7. Things that are not in this repo

These hold identities, secrets or client details, so restore them by hand (from an encrypted
backup) or recreate them:

| File | What | How |
|---|---|---|
| `~/.zshrc.local` | Client/machine-specific env vars and functions | Restore from backup. `zshrc` sources it if present. |
| `~/.gitconfig` | Git name/email | `git config --global user.name ...`, `user.email`, `init.defaultBranch main`, `push.autoSetupRemote true` |
| `~/.ssh/` | Keys + `config` (incl. the `lbf-github` host alias) | Restore, or generate new keys and add them to GitHub |
| `~/.kube/*.config` | Cluster contexts | Restore, then re-auth with `kubelogin` |

Then:

```bash
gh auth login                       # GitHub
nvm install --lts                   # Node — versions don't come with brew
uv python install 3.14 3.12         # Python interpreters
uv tool install pre-commit
az login                            # if you installed Brewfile.extra

# Switch this repo to SSH now that keys exist
git remote set-url origin git@github.com:jhs-halfspace/developer-setup.git
```

## Keeping it up to date

Installed something worth keeping? Add it to `Brewfile` (or `Brewfile.extra`) and commit.
To see what's installed but not listed in either Brewfile:

```bash
# Dry run — removes nothing without --force. Also lists dependencies of unlisted packages.
brew bundle cleanup --file=<(cat Brewfile Brewfile.extra)
```
