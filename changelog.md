##  Commits in production - for one day, generated on: 2019-03-04 21:24:06 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8df68de51796)|[Bug 1532336 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532336) - Turn off optimizations for searchfox jobs. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D21964|kgupta@mozilla.com|tomprince|2019-03-04 20:18:41|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5cfbf5c1dbe7)|Backed out changeset 7fdcccd878ad (bug 1527895) for Gecko Decision Task failure. CLOSED TREE|dluca@mozilla.com||2019-03-04 19:41:57|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7fdcccd878ad)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add code-review-issues task in CI, r=dustin,marco,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21348|babadie@mozilla.com|dustin,marco,tomprince|2019-03-04 19:34:02|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5caf48a420eb)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add soft-dependencies to taskgraph, r=ahal,marco,tomprince,dustin Differential Revision: https://phabricator.services.mozilla.com/D19791|babadie@mozilla.com|ahal,marco,tomprince,dustin|2019-03-04 19:09:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=aeee5b2fac0f)|[Bug 1531178 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531178) - provide gls and safe browsing separate keys. r=tomprince Provide gls and safe browsine separate keys at build time. Differential Revision: https://phabricator.services.mozilla.com/D21536|mtabara@mozilla.com|tomprince|2019-03-04 18:57:18|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0ece01da444e)|[Bug 1532251 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532251) Add new xpcshell dependency to periodic updates r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D21912|sfraser@mozilla.com|mtabara|2019-03-04 16:12:06|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=817014bcd372)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) Improve logging and timeouts in partials generation r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D21909|sfraser@mozilla.com|mtabara|2019-03-04 16:10:59|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=0e53fe692658)|No bug: fix checks *without* --ci-configuration-directory, fix lint r=tomprince I have actually tested this one in a [try push](https://treeherder.mozilla.org/#/jobs?repo=ci-admin-try&revision=cf0bad5ab9271013f6920018e955daab76468957)! Differential Revision: https://phabricator.services.mozilla.com/D21985|dmitchell@mozilla.com|tomprince|2019-03-04 22:17:26|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=60bc15b47919)|[Bug 1526979 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526979) allow ignored payload.data.source, too, in triggering hook r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D21969|dmitchell@mozilla.com|tomprince|2019-03-04 20:38:07|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=e72a3935e409)|No bug: fix use of bindings in 'ci-admin apply' r=tomprince I missed this when refactoring the `bindings` property to use an object instead of a tuple. Differential Revision: https://phabricator.services.mozilla.com/D21963|dmitchell@mozilla.com|tomprince|2019-03-04 20:37:38|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=6a3895820e75)|No bug: capture absolute path for --ci-configuration-directory r=tomprince The `ci-admin check` command changes working directory, so it broke use of `--ci-configuration-directory`. Differential Revision: https://phabricator.services.mozilla.com/D21959|dmitchell@mozilla.com|tomprince|2019-03-04 19:42:19|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=a3f3c50c66ac)|No bug: fix black and flake8 issues r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D21951|dmitchell@mozilla.com|tomprince|2019-03-04 18:58:44|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=33d5ff352ae5)|[Bug 1526979 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526979) - add support for hg-push tasks r=tomprince This adds support for "bindings" in the Hooks API, and uses it to support hooks that run when a push is generated, with the hook template based on a file in ci-configuration. The hooks run tasks on a dedicated `hg-push` workerType which *only* runs this sort of task, and can thus run them quickly. The tasks themselves do not perform an hg clone or do anything terribly complicated, so once the docker image is loaded they only take a few seconds to execute. The docker image is generated on every push to the ci-admin repository. That could be attached to the ci-configuration repository, instead, but that repository does not yet use ci-taskgraph. This also adds some checks to be confident that nobody can trigger hg-push hooks, nor create tasks on the workerType. Differential Revision: https://phabricator.services.mozilla.com/D21282|dmitchell@mozilla.com|tomprince|2019-03-04 18:21:07|

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=9fa866d730ee)|[Bug 1526979 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526979) - Generate hg-push hooks. r=tomprince This includes a hook task template, as well as a small Python script embedded in a Docker image that creates decision tasks based on `.taskcluster.yml` This is currently gated behind a temporary feature in projects.yml. We can slowly add this feature to various projects as we disable them in mozilla-taskcluster, until everything is moved over. Differential Revision: https://phabricator.services.mozilla.com/D21283|dmitchell@mozilla.com|tomprince|2019-03-04 19:18:20|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)|FIC - BOT|Self Generated| - |

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)|FIC - BOT|Self Generated| - |

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)|FIC - BOT|Self Generated| - |

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)|FIC - BOT|Self Generated| - |

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)|FIC - BOT|Self Generated| - |

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)|FIC - BOT|Self Generated| - |

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)|FIC - BOT|Self Generated| - |

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/f543df8c734142d7338190354da5cebd1d5a0b62)|update to gw 13.0.2, tc-proxy 5.1.0 on win 7  deploy: gecko-t-win7-32 gecko-t-win7-32-gpu|grenade|N/A|2019-03-04 13:35:46|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/5e17c70ece9815221ef92dbd9edba41818979806)|update to gw 13.0.2, tc-proxy 5.1.0 on win 7  deploy: gecko-t-win7-32 gecko-t-win7-32-gpu gecko-t-win7-32-cu|grenade|N/A|2019-03-04 13:13:20|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/a86086a0d4a09e5155c64f150c9b67dfe0563bf4)|update to gw 13.0.2, tc-proxy 5.1.0 on win 7  deploy: gecko-t-win7-32 gecko-t-win7-32-gpu gecko-t-win7-32-cu|grenade|N/A|2019-03-04 12:54:22|

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)|FIC - BOT|Self Generated| - |

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)|FIC - BOT|Self Generated| - |

|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)|FIC - BOT|Self Generated| - |

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)|FIC - BOT|Self Generated| - |

|	signingscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)|FIC - BOT|Self Generated| - |

|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/9dae677b5232a551eea3caeae8e8119150cb0529)|Merge pull request #349 from taskcluster/renovate/eslint-5.x  Update dependency eslint to v5.15.0|djmitche|N/A|2019-03-04 20:40:39|
|[Link](https://github.com/taskcluster/taskcluster/commit/84a5d4efe47a8940fb80a8086c16a43695ebb9d1)|Merge pull request #348 from taskcluster/renovate/ajv-6.x  Update dependency ajv to v6.10.0|djmitche|N/A|2019-03-04 19:40:37|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
