##  Commits in production - for one day, generated on: 2019-02-13 04:53:36 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=33ea61c54aea)|Bug 1525959 - Run GeckoView mochitests on x86_64 emulators in automation r=gbrown  Differential Revision: https://phabricator.services.mozilla.com/D19015|jwillcox@mozilla.com|gbrown|2019-02-12 18:27:35|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8b2e8f177263)|Bug 1525760 - Followup: re-enable the tasks without sccache. r=me  And refresh rust dependency after bug 1525733. |ccoroiu@mozilla.com|me|2019-02-12 18:35:42|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=76639dcdef8f)|Bug 1527227 - Update Rust nightly version. r=chmanchester a=Aryx|ccoroiu@mozilla.com|chmanchester|2019-02-12 18:35:42|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=34f33ae5913e)|Backed out 3 changesets (bug 1525959, bug 1526002) for failing android  Backed out changeset de0efca1118e (bug 1526002) Backed out changeset 503cbc86e442 (bug 1525959) Backed out changeset 33ea61c54aea (bug 1525959)|apavel@mozilla.com||2019-02-12 23:53:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=de25d2f1abef)|Bug 1505538 - Release x86_64 Fennec Nightly in the Google Play Store r=mtabara  Release x86_64 Fennec Nightly in the Google Play Store  Differential Revision: https://phabricator.services.mozilla.com/D19534|mtabara@mozilla.com|mtabara|2019-02-13 01:00:25|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)|FIC - BOT|Self Generated| - |

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5041739e5a5b)|Bug 1525733 - Require rust 1.32 to build. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19244|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9cc8cc20982c)|Bug 1526505 - Update mozharness stats parsing code for per-language stats. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19247|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=bb243f4edd88)|Bug 1492279 - Only fetch target task for actions that require it r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D19273|btara@mozilla.com|dustin|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=036604abf1e5)|Bug 1519472 - [taskgraph] Factor logic for adding a cache in job.common to a new function, r=tomprince  We add caches at various places in common.py. This consolidates the logic into a re-useable function. This is in preparation for adding generic-worker cache support.  This also adds a test. The test is not terribly useful, but I've been looking for an excuse to lay some groundwork for further tests in the 'job' submodule. This will do.  Differential Revision: https://phabricator.services.mozilla.com/D17689|btara@mozilla.com|tomprince|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2053a035eee6)|Bug 1519472 - [ci] Opt out of caching for generic-worker based Windows builds, r=tomprince  The hosts don't have enough disk space to cache mozilla-central.  Differential Revision: https://phabricator.services.mozilla.com/D18738|btara@mozilla.com|tomprince|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=887cc76ba189)|Bug 1519472 - [taskgraph] Support generic-worker caches in run_task, r=tomprince  This implements support for adding generic-worker caches. As a consequence this also turns on caching for the gecko checkout if present.  Differential Revision: https://phabricator.services.mozilla.com/D17690|btara@mozilla.com|tomprince|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=76639dcdef8f)|Bug 1527227 - Update Rust nightly version. r=chmanchester a=Aryx|ccoroiu@mozilla.com|chmanchester|2019-02-12 18:14:20|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8b2e8f177263)|Bug 1525760 - Followup: re-enable the tasks without sccache. r=me  And refresh rust dependency after bug 1525733. |ccoroiu@mozilla.com|me|2019-02-12 18:29:08|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a90e2dd8b1a5)|Bug 1525738 - Stop running Android 7.0 x86_64 geckoview-junit tests; r=mbrubeck|rmaries@mozilla.com|mbrubeck|2019-02-13 06:27:59|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=636d2c00234d)|Bug 1527011 - Support win64-aarch64 artifact builds; r=nalexander|rmaries@mozilla.com|nalexander|2019-02-13 06:27:59|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5041739e5a5b)|Bug 1525733 - Require rust 1.32 to build. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19244|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9cc8cc20982c)|Bug 1526505 - Update mozharness stats parsing code for per-language stats. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19247|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=bb243f4edd88)|Bug 1492279 - Only fetch target task for actions that require it r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D19273|btara@mozilla.com|dustin|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=036604abf1e5)|Bug 1519472 - [taskgraph] Factor logic for adding a cache in job.common to a new function, r=tomprince  We add caches at various places in common.py. This consolidates the logic into a re-useable function. This is in preparation for adding generic-worker cache support.  This also adds a test. The test is not terribly useful, but I've been looking for an excuse to lay some groundwork for further tests in the 'job' submodule. This will do.  Differential Revision: https://phabricator.services.mozilla.com/D17689|btara@mozilla.com|tomprince|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2053a035eee6)|Bug 1519472 - [ci] Opt out of caching for generic-worker based Windows builds, r=tomprince  The hosts don't have enough disk space to cache mozilla-central.  Differential Revision: https://phabricator.services.mozilla.com/D18738|btara@mozilla.com|tomprince|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=887cc76ba189)|Bug 1519472 - [taskgraph] Support generic-worker caches in run_task, r=tomprince  This implements support for adding generic-worker caches. As a consequence this also turns on caching for the gecko checkout if present.  Differential Revision: https://phabricator.services.mozilla.com/D17690|btara@mozilla.com|tomprince|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8b2e8f177263)|Bug 1525760 - Followup: re-enable the tasks without sccache. r=me  And refresh rust dependency after bug 1525733. |mh@glandium.org|me|2019-02-12 10:19:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a90e2dd8b1a5)|Bug 1525738 - Stop running Android 7.0 x86_64 geckoview-junit tests; r=mbrubeck|gbrown@mozilla.com|mbrubeck|2019-02-12 18:24:37|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=76639dcdef8f)|Bug 1527227 - Update Rust nightly version. r=chmanchester a=Aryx|ccoroiu@mozilla.com|chmanchester|2019-02-12 18:37:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=636d2c00234d)|Bug 1527011 - Support win64-aarch64 artifact builds; r=nalexander|gbrown@mozilla.com|nalexander|2019-02-13 03:03:53|

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
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/b7c71acd64d624882248f088e83ad8a8a8130add)|Bug 1527134 - disable windows update (again)  deploy: gecko-t-win10-64|grenade|N/A|2019-02-12 07:52:33|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/7d712337608d7806bdd6d8632ed23bd349994cde)|Merge pull request #212 from djmitche/bug1527416  Bug 1527416 - get a fresh copy of the hook before triggering|djmitche|N/A|2019-02-13 01:18:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/a17d0f0b0a012049cb3023c6863c2c9be83a6b26)|Bug 1527416 - get a fresh copy of the hook before triggering|djmitche|N/A|2019-02-12 20:07:32|
|[Link](https://github.com/taskcluster/taskcluster/commit/5da8dc490e6bb765de0825d9ac209b8af2fc5081)|Merge pull request #211 from djmitche/bug1523376  Bug 1523376 - use crypto-js instead of stealing Hawk's copy|djmitche|N/A|2019-02-12 18:15:53|
|[Link](https://github.com/taskcluster/taskcluster/commit/a43655812caf70da8c4d0983b86c5d96193a48f9)|Bug 1523376 - include links to taskcluster-client|djmitche|N/A|2019-02-12 17:24:46|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
