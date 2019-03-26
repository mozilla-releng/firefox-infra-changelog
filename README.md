# Firefox Infra Changelog
CiDuty's tool which builds a changelog of commits happening on git and hg that could affect Firefox CI Infra.

# How does it work?
The tool uses py-github and github token and requests on all mozilla's Git/HG infra repositories and creates:
* A central [changelog.md](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/changelog.md) in which data is formatted in a set way. 
* A [changelog.json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/changelog.json) file which contains the entire commit data, starting from 1st December 2018.

# Install process:
1. After you clone the repository, please run `pip3 install -r requirements.txt`
2. Generate a Github [Personal access token](https://github.com/settings/tokens) and add an environment variable called `GIT_TOKEN` containing the generated token.
3. Run the script with `python3 client.py <optional-flags>`
4. **OPTIONAL**: You can add an optional environment variable called `LoggerLevel` to change the information which gets logged. Example: `LoggerLevel=WARNING`. This will give you extra information such as: [e7c515](https://github.com/mozilla-releng/firefox-infra-changelog/pull/263/commits/e7c515cd1249c60921a22cb2876deef44b5fe7a4#diff-55a742f2aefb0ba0012723d8409292b3R249)

# Flags
| Short Flag | Long Flag | Description |
|-----|-----|----------------------------------------------------------------------------|
| -c | --complete  | Runs script for all available repositories
| -g | --git  | Runs script only for repos that are on GitHub                              |
| -hg | --mercurial   | Runs script only for repos that are on Mercurial                           |
| -m | --manual    | Let the user choose for which repositories the script will run             |
| -l | --logger    | Activate logger output in the console             |
| -d | --days | Generate the **changelog.md** for `<int>` amount of days. |
| -u | --update | Runs script for all available repositories and auto push the changes to github

# Release schedule
Starting with 1st of March 2018, every **Friday** Firefox-Infra-Changelog will have a new release. 

You can treat the releases as our current stable version, were using the code from `master` is treated as night releases.

# Can I contribute?
Yes! We have a couple of [Issues Open](https://github.com/Akhliskun/firefox-infra-changelog/issues). 
Pick whichever you find fancy and make a PullRequest.

# Can I suggest edits and/or features? 
Absolutely! Please [Open an Issue, or more](https://github.com/Akhliskun/firefox-infra-changelog/issues). 




# Contributors
* [Danut Labici](https://github.com/Akhliskun)
* [Bogdan Crisan](https://github.com/bccrisan)
* [Roland Mutter](https://github.com/mutterroland)
* [Zsolt Fay](https://github.com/zsoltfay)
* [Radu Iman](https://github.com/raduiman)
* [Adrian Pop](https://github.com/popadrianc)
