set -x

# docker run --rm -it -v $PWD:/src klakegg/hugo:ubuntu new content\/posts\/$(date +%Y)/$(date +%G-%m-%d-%H%M).md
./hugo new posts\/$(date +%Y)/$(date +%G-%m-%d-%H%M%S).md
