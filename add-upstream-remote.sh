#!/bin/bash

# Detta script uppdaterar det lokala Git-arkivet med eventuella
# ändringar som har gjorts "centralt", i upstream-arkivet, efter
# att ditt eget arkiv skapades.  Om du behöver köra scriptet
# kommer vi att säga till!

# Exit script upon failure
set -e

# Is the upstream already set?
# If not, add it.
git config remote.upstream.url || git remote add upstream git@gitlab.liu.se:tdde23-24/python-tdde24-base.git

# Update from the "upstream" repo defined above
git checkout main
git fetch upstream
git pull upstream main

# Push updates to gitlab
git push origin main

