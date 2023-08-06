#!/bin/bash

if [[ -z "$TOOLSDIR" ]]; then
    export TOOLSDIR="/home/cas/code/my-silly-tools"
fi

cp "$TOOLSDIR/dotfiles/potato/.bash_aliases" "$HOME"
bash "$TOOLSDIR/tasks/potato_tmux.sh"
