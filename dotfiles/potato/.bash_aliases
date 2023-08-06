# variablez
export TOOLSDIR="/home/cas/code/my-silly-tools"

if [ ! -d "$TOOLSDIR" ]
then
    echo "WARNING: my-silly-tools repo is missing!"
fi

# silly commands
alias pinit="bash $TOOLSDIR/tasks/potato_init.sh"

# tmux attach shortcuts
alias tw="tmux a -t web"
alias tb="tmux a -t casbot"
