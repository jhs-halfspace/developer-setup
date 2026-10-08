# Git Aliases (inspired by Oh-My-Zsh git plugin)

# =============================================================================
# Helper Functions
# =============================================================================

function git_current_branch() {
  local ref
  ref=$(git symbolic-ref --quiet HEAD 2>/dev/null)
  local ret=$?
  if [[ $ret != 0 ]]; then
    [[ $ret == 128 ]] && return
    ref=$(git rev-parse --short HEAD 2>/dev/null) || return
  fi
  echo ${ref#refs/heads/}
}

function git_main_branch() {
  command git rev-parse --git-dir &>/dev/null || return
  local ref
  for ref in refs/{heads,remotes/{origin,upstream}}/{main,trunk,mainline,default,master}; do
    if command git show-ref -q --verify $ref; then
      echo ${ref:t}
      return 0
    fi
  done
  echo main
  return 1
}

# =============================================================================
# Basic
# =============================================================================

alias g='git'
alias gs='git status'

# =============================================================================
# Add
# =============================================================================

alias ga='git add'

# =============================================================================
# Branch
# =============================================================================

alias gb='git branch'
alias gba='git branch -a'
alias gbd='git branch -d'
alias gbD='git branch -D'

# =============================================================================
# Checkout / Switch
# =============================================================================

alias gco='git checkout'
alias gcb='git checkout -b'
alias gcm='git checkout $(git_main_branch)'

# =============================================================================
# Commit
# =============================================================================

alias gc='git commit -m'
alias gcv='git commit -v'

# =============================================================================
# Fetch
# =============================================================================

alias gf='git fetch'
alias gfo='git fetch origin'

# =============================================================================
# Merge
# =============================================================================

alias gm='git merge'
alias gma='git merge --abort'

# =============================================================================
# Push / Pull
# =============================================================================

alias gp='git push'
alias gl='git pull'
alias 'gpf!'='git push --force'
alias gpsup='git push --set-upstream origin $(git_current_branch)'
alias gpr='git pull --rebase'

# =============================================================================
# Worktrunk
# =============================================================================

alias wts='wt switch'
alias wtl='wt list'
