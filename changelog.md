##  Commits in production - for 3 days, generated on: 2019-03-26 15:45:38 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e8758002d7d4)|[Bug 1536804 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804) - Add a task for summarising wpt metadata, r=ahal This task runs on wpt metadata changes and uploads an artifact containing the summarised metadata. Depends on D24178 Differential Revision: https://phabricator.services.mozilla.com/D24179|james@hoppipolla.co.uk|ahal|2019-03-26 17:28:48|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9e8fee5e4f3d)|[Bug 1519825 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519825) - Update grcov to revision 9214a916805838265764f9c69eaed657ea3db021 r=marco This revision corresponds to grcov 0.4.2 Differential Revision: https://phabricator.services.mozilla.com/D16465|csabou@mozilla.com|marco|2019-03-25 19:17:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=775f40c959fc)|[Bug 1538134 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134) [mozharness] Set repository path in taskcluster; r=aki Taskcluster has authorative information about the repository being built, so pass that to mozharness, rather than have mozharness reconstruct it from hand-maintained mozharness config. Differential Revision: https://phabricator.services.mozilla.com/D24561|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=db11228c8a38)|[Bug 1538134 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134) [mozharness] Remove explicit setting of branches to use release promotion; r=aki The only thing this affects is the default update channel, but for shipping builds, this is set explicitly via taskcluster, and for other branches, defaults to `default`. Differential Revision: https://phabricator.services.mozilla.com/D24562|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3e4b58569126)|[Bug 1538134 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134) [mozharness] Don't override PGO settings per-branch; r=aki The release mozconfigs set `MOZ_PGO` and all shipping builds set the `nightly` mozharness config, so we don't need to additionaly set PGO based on the branch. Differential Revision: https://phabricator.services.mozilla.com/D24563|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d5c2b9a1c215)|[Bug 1538134 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134) [mozharness] Remove support for unused `builds/branch_specifics.py` config; r=aki We have moved per-branch configuration to taskcluster, so we can remove that support in mozharness. Differential Revision: https://phabricator.services.mozilla.com/D24564|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=02b78c6e3ca7)|[Bug 1536839 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1536839) - Add json formatter to ./mach clang-format, r=ahal,marco Depends on D24193 Differential Revision: https://phabricator.services.mozilla.com/D24194|babadie@mozilla.com|ahal,marco|2019-03-25 17:04:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=486437866d00)|[Bug 1535679 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535679) - switch Firefox nightlies to declarative artifacts. r=sfraser a=release Linter fixes. Differential Revision: https://phabricator.services.mozilla.com/D24214|mtabara@mozilla.com|sfraser|2019-03-25 15:50:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5a3f8b7e664c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D24676|sfraser@mozilla.com|sfraser|2019-03-25 13:08:53|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4d546ab0dc94)|[Bug 1538475 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1538475) - Add comma to 'central-to-beta' and 'beta-to-release' generators to prevent concatenation of two folder paths of files to modify r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D24602|archaeopteryx@coole-files.de|jlorenzo|2019-03-25 11:25:37|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=43ac43ba6cf4)|[Bug 1536836 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1536836) - Support multiple formatters with file output in ./mach lint, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24193|babadie@mozilla.com|ahal|2019-03-25 11:17:44|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9e8fee5e4f3d)|[Bug 1519825 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519825) - Update grcov to revision 9214a916805838265764f9c69eaed657ea3db021 r=marco This revision corresponds to grcov 0.4.2 Differential Revision: https://phabricator.services.mozilla.com/D16465|rgurzau@mozilla.com|marco|2019-03-26 11:57:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=402c24bed346)|[Bug 1519825 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519825) Update grcov to version 0.4.3 on macosx r=marco The patch https://phabricator.services.mozilla.com/D16465 just updated windows and linux version of grcov, so here we update macosx version too. Differential Revision: https://phabricator.services.mozilla.com/D24753|rgurzau@mozilla.com|marco|2019-03-26 11:57:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=43ac43ba6cf4)|[Bug 1536836 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1536836) - Support multiple formatters with file output in ./mach lint, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24193|aiakab@mozilla.com|ahal|2019-03-25 17:58:26|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4d546ab0dc94)|[Bug 1538475 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1538475) - Add comma to 'central-to-beta' and 'beta-to-release' generators to prevent concatenation of two folder paths of files to modify r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D24602|aiakab@mozilla.com|jlorenzo|2019-03-25 17:58:26|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5a3f8b7e664c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D24676|aiakab@mozilla.com|sfraser|2019-03-25 17:58:26|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9e8fee5e4f3d)|[Bug 1519825 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519825) - Update grcov to revision 9214a916805838265764f9c69eaed657ea3db021 r=marco This revision corresponds to grcov 0.4.2 Differential Revision: https://phabricator.services.mozilla.com/D16465|rgurzau@mozilla.com|marco|2019-03-26 11:51:47|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=402c24bed346)|[Bug 1519825 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519825) Update grcov to version 0.4.3 on macosx r=marco The patch https://phabricator.services.mozilla.com/D16465 just updated windows and linux version of grcov, so here we update macosx version too. Differential Revision: https://phabricator.services.mozilla.com/D24753|rgurzau@mozilla.com|marco|2019-03-26 11:51:47|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=43ac43ba6cf4)|[Bug 1536836 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1536836) - Support multiple formatters with file output in ./mach lint, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24193|aiakab@mozilla.com|ahal|2019-03-25 17:52:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4d546ab0dc94)|[Bug 1538475 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1538475) - Add comma to 'central-to-beta' and 'beta-to-release' generators to prevent concatenation of two folder paths of files to modify r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D24602|aiakab@mozilla.com|jlorenzo|2019-03-25 17:52:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5a3f8b7e664c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D24676|aiakab@mozilla.com|sfraser|2019-03-25 17:52:30|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=37273deb744f)|[Bug 1485680 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1485680) - make the relpro action a hook. r=dustin a=tomprince make the relpro action a hook. Differential Revision: https://phabricator.services.mozilla.com/D5581|mozilla@hocat.ca|dustin|2019-03-25 23:22:08|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/143871d458b9d4c44f71f111c7fe3e9c805ae6bb)|Merge pull request #482 from djmitche/allcontributors-in-docs  Use allcontributors in docs|djmitche|N/A|2019-03-26 12:43:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/1da427860a8d2bc2f8c26e0487530891b268022c)|[UI] Add skip to content- keyboard accessibility (#496)  [UI] Add skip to content- keyboard accessibility|Aditya-Kolla|N/A|2019-03-26 12:22:56|
|[Link](https://github.com/taskcluster/taskcluster/commit/bd8f72a9ecc8ef68ee281955d20166024a44cb68)|Merge pull request #494 from taskcluster/typo-fix  Typo fix|djmitche|N/A|2019-03-25 19:13:06|
|[Link](https://github.com/taskcluster/taskcluster/commit/da10730fd46c720ad3db4acea74049a99e1d05db)|Tyop fxi ;)|petemoore|N/A|2019-03-25 19:06:48|
|[Link](https://github.com/taskcluster/taskcluster/commit/b3c5082752df072263c7da1d7b53a8fe0a8fbefe)|Merge pull request #481 from taskcluster/issue-479  Cleanup logs docs pages|imbstack|N/A|2019-03-25 18:47:11|
|[Link](https://github.com/taskcluster/taskcluster/commit/bed82c7c4881fab007eecb8bf1cfe1c6033810f5)|Show access token when creating a client (#489)|helfi92|N/A|2019-03-25 17:26:24|
|[Link](https://github.com/taskcluster/taskcluster/commit/02020bdea61450b4c3ec0cc0c21c507f7f0ab9e9)|Merge pull request #491 from taskcluster/renovate/raw-loader-2.x  Update dependency raw-loader to v2|djmitche|N/A|2019-03-25 13:51:44|
|[Link](https://github.com/taskcluster/taskcluster/commit/3cea3dd67620033912d99c9500a43d3af02d321c)|Merge pull request #463 from helfi92/nicer-getting-started-page  [UI] Add custom get started view|helfi92|N/A|2019-03-25 13:37:18|
|[Link](https://github.com/taskcluster/taskcluster/commit/aed11bbf3b0eba07caba51db539027090ce42ce0)|Update dependency raw-loader to v2|renovate-bot|N/A|2019-03-25 13:34:31|
|[Link](https://github.com/taskcluster/taskcluster/commit/182d385465c2abe482b18fcb15033715af7f3a88)|Merge pull request #493 from taskcluster/renovate/serialize-error-4.x  Update dependency serialize-error to v4|djmitche|N/A|2019-03-25 13:20:07|
|[Link](https://github.com/taskcluster/taskcluster/commit/6cc9ec0839d506243b5651a329d356abe8254db8)|Update dependency serialize-error to v4|renovate-bot|N/A|2019-03-25 13:05:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/d6d64d9ee9ea0e2fb7793a69259922b112067089)|Merge pull request #490 from taskcluster/renovate/eslint-5.x  Update dependency eslint to v5.15.3|djmitche|N/A|2019-03-25 13:04:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/fa15721bb6f1b9c0d91a20f72ce78ebcbe11aa31)|Adjust GetStarted url in markdown|helfi92|N/A|2019-03-25 12:47:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/3d8177c3c34f2d9111059310d4f83dd676d39dc8)|Linting|helfi92|N/A|2019-03-23 17:41:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/91e836d45b624a5e46045d0fc93ad6dbd5a3a9b1)|Add section for the people behind taskcluster in docs|helfi92|N/A|2019-03-23 17:40:18|
|[Link](https://github.com/taskcluster/taskcluster/commit/bce0d8df52fcc4c6b273a8ba644dcca3185a689b)|Make card clickable instead of "See more" button|helfi92|N/A|2019-03-23 17:30:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/a809600db384a67c6d7a18311d773cd0868dfe09)|Merge pull request #483 from djmitche/docs-error-handling  Simplify docs loading and improve error handling|djmitche|N/A|2019-03-23 22:46:38|

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)|FIC - BOT|Self Generated| - |

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)|FIC - BOT|Self Generated| - |

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)|FIC - BOT|Self Generated| - |

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)|FIC - BOT|Self Generated| - |

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)|FIC - BOT|Self Generated| - |

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)|FIC - BOT|Self Generated| - |

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)|FIC - BOT|Self Generated| - |

|	signingscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)|FIC - BOT|Self Generated| - |

|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)|FIC - BOT|Self Generated| - |

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |

|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)|FIC - BOT|Self Generated| - |

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)|FIC - BOT|Self Generated| - |

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
