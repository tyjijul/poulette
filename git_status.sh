#!/bin/sh

[ $(git rev-parse HEAD) = $(git ls-remote $(git rev-parse --abbrev-ref @{u} | sed 's/\// /g') | cut -f1) ] && echo up-to-date || echo not-up-to-date
# UPSTREAM=${1:-'@{u}'}
# LOCAL=$(git rev-parse @)
# REMOTE=$(git rev-parse "$UPSTREAM")
# BASE=$(git merge-base @ "$UPSTREAM")

# if [ $LOCAL = $REMOTE ]; then
#     echo "Up-to-date"
# elif [ $LOCAL = $BASE ]; then
#     echo "Need-to-pull"
# elif [ $REMOTE = $BASE ]; then
#     echo "Need-to-push"
# else
#     echo "Diverged"
# fi
