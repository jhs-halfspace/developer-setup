#!/bin/zsh
# Symlink the configs in this repo into place. Safe to re-run.

REPO_DIR=$(cd "$(dirname "$0")" && pwd)

echo "Setting up configs from: $REPO_DIR"

# Usage: link_config <path in repo> <destination>
# Existing symlinks are replaced; real files/dirs are moved to <dest>.backup.
link_config() {
  local src="$REPO_DIR/$1"
  local dest="$2"

  mkdir -p "$(dirname "$dest")"

  if [[ -L "$dest" ]]; then
    rm "$dest"
  elif [[ -e "$dest" ]]; then
    echo "Backing up $dest -> $dest.backup"
    mv "$dest" "$dest.backup"
  fi

  echo "Linking $src -> $dest"
  ln -s "$src" "$dest"
}

link_config "dotfiles/zshrc" "$HOME/.zshrc"
link_config "starship/starship.toml" "$HOME/.config/starship.toml"
link_config "ghostty" "$HOME/.config/ghostty"

# cmux embeds Ghostty but reads its own config file; point it at the same one.
link_config "ghostty/config" "$HOME/Library/Application Support/com.cmuxterm.app/config.ghostty"

if [[ ! -f "$HOME/.zshrc.local" ]]; then
  echo "Note: no ~/.zshrc.local found. Put machine/client-specific config there."
fi

echo "Setup complete! Restart your terminal or run 'exec zsh'"
