# @/dev/null blog

## To-Dos
* ~~clean-up master branch since source has been created~~
  * ~~update README.md~~
  * ~~remove everything but README.md, .travis.yml and .gitmodules and move output dir up one level~~
  * ~~submodules stay in place~~
* ~~Automatize commit messages from pelican builds~~
* design and test make publish
  * ~~synchronize confs~~
  * set-up ghp-import
    * process should be:
      * `bash test-git-status.sh` (not really needed as we do not commit on `source` branch)
      * `make github`
      * ~~commit in current? (would prefer not)~~
      * `ghp-import -b $(GITHUB_PAGES_BRANCH) -m $(shell python write_next_commit_msg.py) $(OUTPUTDIR) `
      * `[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)`
      * `bash test-git-status.sh` <- optional after the process is confirmed
    * ~~dependancy for travis~~
  * perform proper commits and rebase on all branches
  * ~~design the .travis.yml process (particularly the pre-build status check)~~
  * recheck and test the push function
  * once it works, delete current aavanian.github.io and rename -source
* Investigate robots.txt file and build one.
* Build a custom favicon (and others for most browsers)
* ~~Add favicon.ico and robots.txt to the content/extra folder and add the following to pelicanconf.py:~~
```python
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }
```

## Known issues
* Liquid_Tags header for notebook
  * need to add html lines to theme header, some themes already include them, some not so need a way to insert these few lines dynamically (for travis builds).
  * No solution yet (probably shell/sed driven but with a custom list of themes to process: [theme1, header1, ...])
* I would like to find a way to remove the submodules from the master branch (but keeping theme of course for all other branches)
* I would like to be able to keep a README.md file specific to the master branch. Worst-case scenario, I can copy the source README.md to the master branch with some additional listing in the `STATIC_PATHS` and `EXTRA_PATH_METADATA` variables

## Guidelines
* Branch structure
  * **master**: pubishing branch
    * copy of output dir
    * no source
    * no .travis.yml
    * README.md should describe the blog and point to dependancies, build docs, etc...
  * **source**: production branch
    * where article and pages are built
    * publish to master with ghp-import call + push
    * .travis.yml to trigger builds
    * README.md (this doc) describes To-Dos and various notes
    * Only commits here should be about building the blog, updates to the README.md and PR merges
  * **tinker-theme**: theme adjustment branch
    * should be rebased off source frequently to keep up-to-date with new articles
    * should only be used to adjust theme configuration
    * merge into source when satisfied and keep the branch alive
    * for deep theme changes, use an ad-hoc temporary branch derived from this one
* see if i can use a dedicated branch for local make html so that output commits don't pollute main branch (another way is to have in master only output commits)
  need to publish on master branch
see if i can use only one repo for travis
tinker with theme bootstrap3 (check bootswatch stufF)

## Build process (memento)
* pelican-quickstart
* git submodule add theme-url themes/theme
* git submodule add url-aavanian-pelican-plugins pelican-plugins
* git submodule update --init -- recursive
* modifs to pelicanconf.py
  * blog setup
  * theme = 'themes/theme'
  * plugin-path = pelican-plugins
  * plugins = [ ...]
