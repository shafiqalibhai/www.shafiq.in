set -x
hugo new content\/en\/posts\/$(date +%Y)/$(date +%G-%m-%d-%H%M%S).md && hugo new content\/fr\/posts\/$(date +%Y)/$(date +%G-%m-%d-%H%M%S).md
