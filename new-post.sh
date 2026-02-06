set -x

# docker run --rm -it -v $PWD:/src klakegg/hugo:ubuntu new content\/posts\/$(date +%Y)/$(date +%G-%m-%d-%H%M).md
hugo new content.en\/posts\/$(date +%Y)/$(date +%G-%m-%d-%H%M%S).md && hugo new content.fr\/posts\/$(date +%Y)/$(date +%G-%m-%d-%H%M%S).md
