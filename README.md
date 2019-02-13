# Firefox Infra Changelog
CiDuty's tool which builds a changelog of commits happening on git and hg that could affect Firefox CI Infra.

# How does it work?
The tool uses py-github and github token and requests on all mozilla's Git/HG infra repositories and creates:
* A central [changelog.md](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/changelog.md) in which data is formatted in a set way. 
* A [changelog.json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/changelog.json) file which contains the same data changelog.md contains. TO-DE-ADDED [Issues 193](https://github.com/mozilla-releng/firefox-infra-changelog/issues/193)

# Can I contribute?
Yes! We have a couple of [Issues Open](https://github.com/Akhliskun/firefox-infra-changelog/issues). 
Pick whichever you find fancy and make a PullRequest.

# Can I suggest edits and/or features? 
Absolutely! Please [Open an Issue, or more](https://github.com/Akhliskun/firefox-infra-changelog/issues). 

# Install process:
1. After you clone the repository, please run `pip3 install -r requirements.txt`
2. Generate a Github token via this page and add an environment variable called `GIT_TOKEN`.
3. Run the script with `python3 client.py <optional-flags>`

# Flags
* --git - Runs script only for repos that are on GitHub
* --hg - Runs script only for repos that are on Mercurial
* --r - Let the user choose for which repositories the script will run
* --d - Let the user choose the amount of days the main markdown file will contain


# Contributors
* [Danut Labici](https://github.com/Akhliskun)
* [Bogdan Crisan](https://github.com/bccrisan)
* [Roland Mutter](https://github.com/mutterroland)
* [Zsolt Fay](https://github.com/zsoltfay)
* [Radu Iman](https://github.com/raduiman)
* [Adrian Pop](https://github.com/popadrianc)
