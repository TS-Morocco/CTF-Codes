#!/bin/sh
tmux has-session -t info
if [ $? != 0 ]; then
    tmux new-session -s info -d
    tmux rename-window 'network'
    tmux split-window -v
    tmux split-pane -t 0 -v 
    tmux split-pane -t 0 -h -p 35
    tmux split-pane -t 2 -h -p 35
    tmux split-pane -t 4 -v
    tmux split-pane -t 4 -h -p 35
    tmux split-pane -t 5 -v
    tmux resize-pane -t 0 -D 1
    tmux resize-pane -t 2 -D 1
    tmux resize-pane -t 4 -D 1
    tmux resize-pane -t 6 -U 1
    tmux send-keys -t 0 "echo 1" C-m
    tmux send-keys -t 1 "echo 2" C-m
    tmux send-keys -t 2 "echo 3" C-m
    tmux send-keys -t 3 "echo 4" C-m
    tmux send-keys -t 4 "echo 5" C-m
    tmux send-keys -t 5 "echo 6" C-m
    tmux send-keys -t 6 "echo 7" C-m
    tmux send-keys -t 7 "echo 8" C-m
    tmux new-window -t info:1 -n 'logs'
    tmux select-window -t info:1
    tmux split-window -t info:1 -v
    tmux split-window -t info:1 -v
    tmux split-window -t info:1 -v
    tmux split-window -t info:1 -v
    tmux send-keys -t 0 "echo 1" C-m
    tmux send-keys -t 1 "echo 2" C-m
    tmux send-keys -t 2 "echo 3" C-m
    tmux send-keys -t 3 "echo 4" C-m
fi
tmux attach -t info
