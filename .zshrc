export PATH=$PATH:~/.local/bin:~/dev/dotfiles/bin

eval "$(pyenv init -)"

eval "$(starship init zsh)"

export NVM_DIR="$HOME/.nvm"
[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && . "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
[ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && . "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion


#################
# ZSH completions
#

# activate syntax highlighting
source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# activate fancier history search
source /opt/homebrew/share/zsh-history-substring-search/zsh-history-substring-search.zsh
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

# activate autocompletions
# source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh
# export ZSH_AUTOSUGGEST_STRATEGY=(completion history)

######
# cmus
#

# open cmus in tmux to allow easy detaching
# after this, run
# :bind -f common q shell tmux detach-client -s cmus
# inside cmus
alias cmus='cmus-start'

# cmus-remote aliases
alias cc='cmus-remote --pause'
alias ccc='cmus-remote --play'
alias cz='cmus-remote --next'
alias cx=' cmus-remote --stop && cmus-remote --play'
alias cv='cmus-remote --stop'
alias cb='cmus-remote --prev'


