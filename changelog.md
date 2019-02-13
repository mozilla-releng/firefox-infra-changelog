##  Commits in production - for one day, generated on: 2019-02-12 08:14:54 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f7716de1fce5)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser  Differential Revision: https://phabricator.services.mozilla.com/D19338|sfraser@mozilla.com|sfraser|2019-02-11 12:15:52|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=68526e6afbd2)|Bug 1525931 - Don't run Raptor on mozilla-release; r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D19216|rwood@mozilla.com|jmaher|2019-02-11 16:13:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5041739e5a5b)|Bug 1525733 - Require rust 1.32 to build. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19244|cmanchester@mozilla.com|firefox-build-system-reviewers,ted|2019-02-11 21:44:56|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9cc8cc20982c)|Bug 1526505 - Update mozharness stats parsing code for per-language stats. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19247|cmanchester@mozilla.com|firefox-build-system-reviewers,ted|2019-02-11 22:02:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=bb243f4edd88)|Bug 1492279 - Only fetch target task for actions that require it r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D19273|dmitchell@mozilla.com|dustin|2019-02-11 22:28:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=036604abf1e5)|Bug 1519472 - [taskgraph] Factor logic for adding a cache in job.common to a new function, r=tomprince  We add caches at various places in common.py. This consolidates the logic into a re-useable function. This is in preparation for adding generic-worker cache support.  This also adds a test. The test is not terribly useful, but I've been looking for an excuse to lay some groundwork for further tests in the 'job' submodule. This will do.  Differential Revision: https://phabricator.services.mozilla.com/D17689|ahalberstadt@mozilla.com|tomprince|2019-02-12 01:36:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2053a035eee6)|Bug 1519472 - [ci] Opt out of caching for generic-worker based Windows builds, r=tomprince  The hosts don't have enough disk space to cache mozilla-central.  Differential Revision: https://phabricator.services.mozilla.com/D18738|ahalberstadt@mozilla.com|tomprince|2019-02-12 01:36:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=887cc76ba189)|Bug 1519472 - [taskgraph] Support generic-worker caches in run_task, r=tomprince  This implements support for adding generic-worker caches. As a consequence this also turns on caching for the gecko checkout if present.  Differential Revision: https://phabricator.services.mozilla.com/D17690|ahalberstadt@mozilla.com|tomprince|2019-02-12 01:36:16|

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
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=66570654c0f2)|Bug 1525931 - Don't run Raptor on mozilla-release; r=jmaher a=test-only  Differential Revision: https://phabricator.services.mozilla.com/D19216|archaeopteryx@coole-files.de|jmaher|2019-02-11 16:59:48|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=be6554246c50)|Bug 1520705 - Enable mochitest-chrome on WebRender r=kats  Enable mochitest-chrome, but skip test_bug331215.xul and test_bug304188.xul because of frequent intermittent failures on WebRener. The intermittent failures already exist and the failure seems not directly related to WebRender implementation.  Differential Revision: https://phabricator.services.mozilla.com/D19115|cbrindusan@mozilla.com|kats|2019-02-11 11:27:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f7716de1fce5)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser  Differential Revision: https://phabricator.services.mozilla.com/D19338|btara@mozilla.com|sfraser|2019-02-11 23:54:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=68526e6afbd2)|Bug 1525931 - Don't run Raptor on mozilla-release; r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D19216|btara@mozilla.com|jmaher|2019-02-11 23:54:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5041739e5a5b)|Bug 1525733 - Require rust 1.32 to build. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19244|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9cc8cc20982c)|Bug 1526505 - Update mozharness stats parsing code for per-language stats. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19247|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=bb243f4edd88)|Bug 1492279 - Only fetch target task for actions that require it r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D19273|btara@mozilla.com|dustin|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=036604abf1e5)|Bug 1519472 - [taskgraph] Factor logic for adding a cache in job.common to a new function, r=tomprince  We add caches at various places in common.py. This consolidates the logic into a re-useable function. This is in preparation for adding generic-worker cache support.  This also adds a test. The test is not terribly useful, but I've been looking for an excuse to lay some groundwork for further tests in the 'job' submodule. This will do.  Differential Revision: https://phabricator.services.mozilla.com/D17689|btara@mozilla.com|tomprince|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2053a035eee6)|Bug 1519472 - [ci] Opt out of caching for generic-worker based Windows builds, r=tomprince  The hosts don't have enough disk space to cache mozilla-central.  Differential Revision: https://phabricator.services.mozilla.com/D18738|btara@mozilla.com|tomprince|2019-02-12 07:25:24|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=887cc76ba189)|Bug 1519472 - [taskgraph] Support generic-worker caches in run_task, r=tomprince  This implements support for adding generic-worker caches. As a consequence this also turns on caching for the gecko checkout if present.  Differential Revision: https://phabricator.services.mozilla.com/D17690|btara@mozilla.com|tomprince|2019-02-12 07:25:24|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=be6554246c50)|Bug 1520705 - Enable mochitest-chrome on WebRender r=kats  Enable mochitest-chrome, but skip test_bug331215.xul and test_bug304188.xul because of frequent intermittent failures on WebRener. The intermittent failures already exist and the failure seems not directly related to WebRender implementation.  Differential Revision: https://phabricator.services.mozilla.com/D19115|cbrindusan@mozilla.com|kats|2019-02-11 11:36:45|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f7716de1fce5)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser  Differential Revision: https://phabricator.services.mozilla.com/D19338|btara@mozilla.com|sfraser|2019-02-12 00:01:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=68526e6afbd2)|Bug 1525931 - Don't run Raptor on mozilla-release; r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D19216|btara@mozilla.com|jmaher|2019-02-12 00:01:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5041739e5a5b)|Bug 1525733 - Require rust 1.32 to build. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19244|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9cc8cc20982c)|Bug 1526505 - Update mozharness stats parsing code for per-language stats. r=firefox-build-system-reviewers,ted  Differential Revision: https://phabricator.services.mozilla.com/D19247|btara@mozilla.com|firefox-build-system-reviewers,ted|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=bb243f4edd88)|Bug 1492279 - Only fetch target task for actions that require it r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D19273|btara@mozilla.com|dustin|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=036604abf1e5)|Bug 1519472 - [taskgraph] Factor logic for adding a cache in job.common to a new function, r=tomprince  We add caches at various places in common.py. This consolidates the logic into a re-useable function. This is in preparation for adding generic-worker cache support.  This also adds a test. The test is not terribly useful, but I've been looking for an excuse to lay some groundwork for further tests in the 'job' submodule. This will do.  Differential Revision: https://phabricator.services.mozilla.com/D17689|btara@mozilla.com|tomprince|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2053a035eee6)|Bug 1519472 - [ci] Opt out of caching for generic-worker based Windows builds, r=tomprince  The hosts don't have enough disk space to cache mozilla-central.  Differential Revision: https://phabricator.services.mozilla.com/D18738|btara@mozilla.com|tomprince|2019-02-12 07:32:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=887cc76ba189)|Bug 1519472 - [taskgraph] Support generic-worker caches in run_task, r=tomprince  This implements support for adding generic-worker caches. As a consequence this also turns on caching for the gecko checkout if present.  Differential Revision: https://phabricator.services.mozilla.com/D17690|btara@mozilla.com|tomprince|2019-02-12 07:32:32|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=6ca6cebc1377)|Bug 1525931 - Don't run Raptor on mozilla-release. r=jmaher, a=test-only  Differential Revision: https://phabricator.services.mozilla.com/D19216|ryanvm@gmail.com|jmaher,|2019-02-11 17:05:00|

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
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/56d247d42d33af2d3fc9b69dfcb13a30e980e6b5)|Bug 1522896 - use update gw 11.1.0 with 1803 patch  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|grenade|N/A|2019-02-11 11:12:16|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/8353604b9cdff902749945fa1ab2d797a54d1cc8)|Bug 1522896 - use update gw 11.1.0 with 1803 patch  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|grenade|N/A|2019-02-11 10:38:32|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/933438f76cdb07af6b4f7fd3b8fc034195a66312)|Bug 1522896 - use update gw 11.1.0 with 1803 patch  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|grenade|N/A|2019-02-11 10:32:15|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/732ff6c8cf8020335c2e7d170b3a6dbdb0387b2a)|Merge pull request #207 from djmitche/omit-debug-testing-subprocess  Omit DEBUG when running a node subprocess|djmitche|N/A|2019-02-12 00:44:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/34f400ec4f68f24f5641e39bba9c4d929a944139)|Refactor   (#197)    Reduce amount of functions in the code    Improve clarity of boolean expressions    Fix tests      Fix tests      Make comments more sensical      Always check if user is active|owlishDeveloper|N/A|2019-02-11 20:50:24|
|[Link](https://github.com/taskcluster/taskcluster/commit/10a04e575cfd4e30d8d8fc1f53816a2408fe0cf7)|Merge pull request #210 from djmitche/bug1524406  Bug 1524406 - Fix keys for LastFire table|djmitche|N/A|2019-02-11 19:50:31|
|[Link](https://github.com/taskcluster/taskcluster/commit/e023b92968e1c49d70d773ed5993a63005cf69fb)|Bug 1524406 - Fix keys for LastFire table  Since this changes the keys, we cannot use the same table.  So this also updates the table name in the Terraform configuration to point to a fresh new table.|djmitche|N/A|2019-02-11 17:39:50|
|[Link](https://github.com/taskcluster/taskcluster/commit/38a72f405d52068bd04fa294da43ef3788258531)|Omit DEBUG when running a node subprocess  Without this, the DEBUG output obscures the expected stdout.|djmitche|N/A|2019-02-11 14:20:36|
|[Link](https://github.com/taskcluster/taskcluster/commit/96cfee05116ea2931b6842dee297176d7582a0d4)|Merge pull request #195 from djmitche/bug1525786  Bug 1525786 - generate tc-client-web|djmitche|N/A|2019-02-11 17:02:20|
|[Link](https://github.com/taskcluster/taskcluster/commit/c5325122eca07b9b4af3bee424ad09699a3dbe38)|Switch to Node 10.15.1 (#198)    Switch to Node 10.15.1      Mention jq in the README|owlishDeveloper|N/A|2019-02-11 16:55:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/8d1ec510060978b1cdc81e234ba1f1ad36a8875e)|Add missing README (#209)    Add missing README    This could be filled out later but for the time being, this is needed to  make sure navigation works properly in the docs when generating the  table of content.      Run `yarn generate`|helfi92|N/A|2019-02-11 15:35:57|
|[Link](https://github.com/taskcluster/taskcluster/commit/e3516eae173232065cb73d69636123feba08fcd1)|Notify user when an interactive task is ready (#156)  Closes https://github.com/taskcluster/taskcluster-web/issues/332.|ededals|N/A|2019-02-11 14:18:44|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
