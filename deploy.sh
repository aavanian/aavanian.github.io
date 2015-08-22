#!/usr/bin/env bash

if [ ! -d "$OUTPUTDIR" ]; then
  echo "SOURCE_DIR ($OUTPUTDIR) does not exist, build the source directory before deploying"
  exit 1
fi

if [ -n "$TRAVIS_BUILD_ID" ]; then
  if [ "$TRAVIS_BRANCH" != "$GITHUB_PAGES_ORIGIN" ]; then
    echo "Travis should only deploy from the DEPLOY_BRANCH ($GITHUB_PAGES_ORIGIN) branch"
    exit 0
  else
    if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
        echo -e "Starting to deploy to Github Pages\n"
        if [ "$TRAVIS" == "true" ]; then
            git config --global user.email "$GIT_EMAIL"
            git config --global user.name "$GIT_NAME"
        fi
        ghp-import -b ${GITHUB_PAGES_BRANCH} -m "$(python write_next_commit_msg.py)" ${OUTPUTDIR}
      	git push -q https://${GH_TOKEN}@github.com/${TARGET_REPO} +${GITHUB_PAGES_BRANCH} > /dev/null
      	[ ! -d ${OUTPUTDIR} ] || rm -rf ${OUTPUTDIR}
        echo -e "Deploy completed\n"
    else
      echo "Travis should not deploy from pull requests"
      exit 0
    fi
  fi
fi
