# Firefox Infra Changelog
Automated tool which builds a changelog of commits happening on git and hg that could affect Firefox CI Infra.

# How does it work?
The tool listens via webhooks on all mozilla's Git/HG infra repositories and creates:
* A central [changelog.md](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/changelog.md) in which data is preformated in a set way. Check [Issue #5](https://github.com/Akhliskun/firefox-infra-changelog/issues/5) for details on formating. 
* A [changelog.json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/changelog.json) file containg the same data changelog.md contains.

# Can I contribute?
Yes! We have a couple of [Issues Open](https://github.com/Akhliskun/taskcluster-worker-checker/issues). 
Pick whichever you find fancy and make a PullRequest.
**PLEASE** don't forget to select "`Allow edits from maintainers`" so we can have quicker merges!

## I have a issue I like, now what?
Fork the project (always make sure to be up-to-date) and start implementing, once done simply make a pull requests and @Akhliskun for review. 

# Contributers
* [Danut Labici](https://github.com/Akhliskun)
* [Bogdan Crisan](https://github.com/bccrisan)
* [Roland Mutter](https://github.com/mutterroland)
* [Zsolt Fay](https://github.com/zsoltfay)
* [Radu Iman](https://github.com/raduiman)
* [Adrian Pop](https://github.com/popadrianc)