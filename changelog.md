##  Commits in production - for 3 days, generated on: 2019-04-01 03:00:31 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=bdbf6856c91a)|[Bug 1536582](https://bugzilla.mozilla.org/show_bug.cgi?id=1536582)  - Update cbindgen. r=boris Differential Revision: https://phabricator.services.mozilla.com/D25520|ealvarez@mozilla.com|boris|2019-03-30 22:02:50|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d067e0360843)|[Bug 1530493](https://bugzilla.mozilla.org/show_bug.cgi?id=1530493)  - Bump mingw-w64 version r=froydnj This is needed to bring dispatcherqueue.h in, which is needed for an ANGLE upgrade. It also ensures that overloads for secure string functions are always defined and removes redundant --enable-secure-api configure option and use of MINGW_HAS_SECURE_API Differential Revision: https://phabricator.services.mozilla.com/D25294|csabou@mozilla.com|froydnj|2019-03-30 09:03:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=08a3525d99d2)|[Bug 1536308](https://bugzilla.mozilla.org/show_bug.cgi?id=1536308)  - Apply a local patch to MinGW to get the needed winrt stuff for ANGLE r=froydnj We apply a local patch while we wait for upstream wine and mingw to review the changes to widl that are necessary to generate the correct headers. Here we just grab the generated headers and patch them into MinGW We can revert this when MinGW updates, but for now we would like to unblock the ANGLE update Depends on D25294 Differential Revision: https://phabricator.services.mozilla.com/D25295|csabou@mozilla.com|froydnj|2019-03-30 09:03:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b9654a90f60a)|[Bug 1535364](https://bugzilla.mozilla.org/show_bug.cgi?id=1535364)  - Enable PGO for Android nightly builds; r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D23532|cmanchester@mozilla.com|tomprince|2019-03-30 04:12:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=825e93bb4b13)|Backed out 3 changesets [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  [Bug 1539779](https://bugzilla.mozilla.org/show_bug.cgi?id=1539779)  [Bug 1536790](https://bugzilla.mozilla.org/show_bug.cgi?id=1536790)  for causing clang-tidy bustages CLOSED TREE Backed out changeset 7d058f3174e5 [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  Backed out changeset 8839622122ed [Bug 1539779](https://bugzilla.mozilla.org/show_bug.cgi?id=1539779)  Backed out changeset 9eb7867c1dd4 [Bug 1536790](https://bugzilla.mozilla.org/show_bug.cgi?id=1536790) |aciure@mozilla.com||2019-03-30 01:53:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=211b1706b5f1)|Backed out changeset dc3b81670b01 [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  for causing clang-tidy bustages CLOSED TREE|aciure@mozilla.com||2019-03-30 00:37:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=04bd7929b499)|Backed out changeset 963d97e812f9 [Bug 1535364](https://bugzilla.mozilla.org/show_bug.cgi?id=1535364)  for causing [Bug 1539933](https://bugzilla.mozilla.org/show_bug.cgi?id=1539933)  a=backout|opoprus@mozilla.com|backout|2019-03-30 00:07:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=69e9ee0ef3dd)|[Bug 1540132](https://bugzilla.mozilla.org/show_bug.cgi?id=1540132)  - Fix updates by telling release properties to ignore the '-shippable' suffix. r=tomprince a=ccoroiu Reviewers: tomprince Reviewed By: tomprince Bug #: 1540132 Differential Revision: https://phabricator.services.mozilla.com/D25397|opoprus@mozilla.com|tomprince|2019-03-30 00:07:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=dc3b81670b01)|[Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  - Update non-Windows builds to clang 8. r=froydnj Windows builds have been taken care of in [Bug 1535441](https://bugzilla.mozilla.org/show_bug.cgi?id=1535441)  Differential Revision: https://phabricator.services.mozilla.com/D25328|mh@glandium.org|froydnj|2019-03-29 23:39:37|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6c34f19750b8)|[Bug 1540210](https://bugzilla.mozilla.org/show_bug.cgi?id=1540210)  - Correct Android 4.3 pgo test's default tier to tier 1; r=Callek Differential Revision: https://phabricator.services.mozilla.com/D25459|gbrown@mozilla.com|Callek|2019-03-29 22:05:01|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=bdbf6856c91a)|[Bug 1536582](https://bugzilla.mozilla.org/show_bug.cgi?id=1536582)  - Update cbindgen. r=boris Differential Revision: https://phabricator.services.mozilla.com/D25520|btara@mozilla.com|boris|2019-03-31 12:08:25|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=bdbf6856c91a)|[Bug 1536582](https://bugzilla.mozilla.org/show_bug.cgi?id=1536582)  - Update cbindgen. r=boris Differential Revision: https://phabricator.services.mozilla.com/D25520|btara@mozilla.com|boris|2019-03-31 11:58:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=603144bedadc)|[Bug 1532952](https://bugzilla.mozilla.org/show_bug.cgi?id=1532952)  - Add an optional linux64-aarch64 build on Taskcluster. r=froydnj This sets things enough things up to be able to push to try with an opt-in, but doesn't run the job on every push. This can be used as a template for future work on a fuzzing job. Differential Revision: https://phabricator.services.mozilla.com/D25069|ccoroiu@mozilla.com|froydnj|2019-03-29 11:44:33|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=14db4eae01f5)|[Bug 1539990](https://bugzilla.mozilla.org/show_bug.cgi?id=1539990)  - Move DocUp test to tier 2; r=dustin Run DocUp as tier 2 rather than tier 3, to make the task visible by default and get the benefit of at least some sheriffing. Differential Revision: https://phabricator.services.mozilla.com/D25319|ccoroiu@mozilla.com|dustin|2019-03-29 11:44:33|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=76fd580f2862)|[Bug 1538675](https://bugzilla.mozilla.org/show_bug.cgi?id=1538675)  - transform Android pgo test platform names so they show up as using 'pgo' as option on Treeherder r=bc Differential Revision: https://phabricator.services.mozilla.com/D25091|ncsoregi@mozilla.com|bc|2019-03-29 06:11:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3d678990e647)|[Bug 1539856](https://bugzilla.mozilla.org/show_bug.cgi?id=1539856)  - Properly avoid running on -ux hardware oustide of try/mozilla-central. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D25252|ncsoregi@mozilla.com|jmaher|2019-03-29 06:11:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f370e4380076)|Merge mozilla-central to autoland. a=merge CLOSED TREE|ncsoregi@mozilla.com|merge|2019-03-29 06:11:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=531d308db7e7)|[Bug 1536044](https://bugzilla.mozilla.org/show_bug.cgi?id=1536044)  - Fully disable jacoco builds for Android r=agi Differential Revision: https://phabricator.services.mozilla.com/D25216|ncsoregi@mozilla.com|agi|2019-03-29 06:11:36|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

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
|[Link](https://github.com/taskcluster/taskcluster/commit/0c36f07794ab4e074579eacf4ab6c13e262a852c)|Merge pull request #510 from taskcluster/nicer-logs-docs  Make logs documentation more useful|imbstack|N/A|2019-03-29 19:39:29|
|[Link](https://github.com/taskcluster/taskcluster/commit/80335b2328ed169bb3f166816cb2b6ec80140a1f)|Change home page wording (#509)|helfi92|N/A|2019-03-29 19:26:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/cf6a1a6f9102fc840e72e8b78014c8fad7e62e35)|(hotfix) fix links|djmitche|N/A|2019-03-29 18:56:51|
|[Link](https://github.com/taskcluster/taskcluster/commit/d0683c46ca792867e2d9f6b1385ea9d9dc4773e2)|Merge pull request #505 from djmitche/dev-docs-refactor  Dev docs refactor|djmitche|N/A|2019-03-29 18:53:39|
|[Link](https://github.com/taskcluster/taskcluster/commit/c4a4f8f4e4d2a491ddeecde5aa2b7119e63fd8d9)|Make logs documentation more useful|imbstack|N/A|2019-03-29 18:32:27|
|[Link](https://github.com/taskcluster/taskcluster/commit/fa50756dae8aa24336db6ded3a3288a4003942fb)|Include link to retrospectives in dev docs|djmitche|N/A|2019-03-29 17:14:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/ce446c31153c61cf8ffe264d8c338fedc7ddcefb)|check for and fix more typos|djmitche|N/A|2019-03-29 17:08:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/44ea552cf4b8d508a92b74072264545be102ffad)|Merge pull request #507 from djmitche/add-mrrrgn  Add @mrrrgn to contributors|djmitche|N/A|2019-03-29 17:00:48|
|[Link](https://github.com/taskcluster/taskcluster/commit/0bfccb189dad8e5160a2515518c3848199f37e2f)|Merge pull request #503 from djmitche/bug1538152  Bug 1538152 - "tell a story" about tasks in queue logging|djmitche|N/A|2019-03-29 16:34:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/30ffc9be39af2132d9796138f78e6f0b8139235d)|Add @mrrrgn now that the github user exists again..|djmitche|N/A|2019-03-29 16:23:30|
|[Link](https://github.com/taskcluster/taskcluster/commit/0fa92e05aedee4af1a67941dea1f7f9b2a73fe32)|Merge pull request #506 from taskcluster/all-contributors/add-OjaswinM  docs: add OjaswinM as a contributor|djmitche|N/A|2019-03-29 16:22:43|
|[Link](https://github.com/taskcluster/taskcluster/commit/bc6ce633d32c0e623cbc9a713c8373f3fc96443c)|docs: update .all-contributorsrc|allcontributors[bot]|N/A|2019-03-29 16:20:04|
|[Link](https://github.com/taskcluster/taskcluster/commit/0aa3bdb7c39b96f4c88ad4a6d2346f158b1d5602)|docs: update README.md|allcontributors[bot]|N/A|2019-03-29 16:20:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/f45b455b4cff090c1d24ac6caff695f2c7f90a60)|Move development section of the manual to be viewed via GitHub READMEs|djmitche|N/A|2019-03-29 16:08:54|
|[Link](https://github.com/taskcluster/taskcluster/commit/91abe996074be2ac74d5a32a83baf625e52c514d)|Refactor builder docs into a single README|djmitche|N/A|2019-03-29 15:34:36|

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
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/d0ae86a2bdb9ae9d402f68ff9412110c32c5c903)|1.0.0|mitchhentges|N/A|2019-03-29 12:30:28|

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
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=660ba33fb079)|No bug - amend ref browser master role to encompass dep signing. r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D25393|mtabara@mozilla.com|jlorenzo|2019-03-29 18:26:27|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=4eb38751b8be)|[Bug 1540168](https://bugzilla.mozilla.org/show_bug.cgi?id=1540168)  - Fix Reference-Browser nightly r=mtabara Fix Reference-Browser nightly Fixes https://tools.taskcluster.net/groups/LasmOd2xTp6Knn6xlkbmTA/tasks/LasmOd2xTp6Knn6xlkbmTA/runs/0/logs/public%2Flogs%2Flive_backing.log Differential Revision: https://phabricator.services.mozilla.com/D25413|jlorenzo@mozilla.com|mtabara|2019-03-29 18:10:46|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
