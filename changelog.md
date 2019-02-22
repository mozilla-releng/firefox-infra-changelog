##  Commits in production - for one day, generated on: 2019-02-22 03:04:56 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6939a3b5e2e4)|Bug 1529339 - replace test-provisioner with permanent bitbar provisioner id r=jmaher  Changes:  - replaced existing references to `test-provisioner/bitbar` with `bitbar/gecko-t-win10-aarch64` (proposed permanent provisioner-id)  Differential Revision: https://phabricator.services.mozilla.com/D20536|egao@mozilla.com|jmaher|2019-02-21 05:18:31|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=897cb0bac95e)|Bug 1528362: [taskgraph] Change scheduler-id to include the trust-domain; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D20048|mozilla@hocat.ca|dustin|2019-02-21 09:35:04|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=424f97dc01db)|Bug 1528362: [taskgraph] Use trust-domain prefixed caches; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D20049|mozilla@hocat.ca|dustin|2019-02-21 09:35:04|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=708d79591ac5)|Bug 1522100 - Add Raptor support for running tests locally on the android-components reference browser; r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D20414|rwood@mozilla.com|davehunt|2019-02-21 16:28:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5f7a214a91d7)|Bug 1522625 - Promote Raptor tp6-7 to tier 1; r=Bebe  Differential Revision: https://phabricator.services.mozilla.com/D20348|rwood@mozilla.com|Bebe|2019-02-21 17:29:52|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ee5fa9cfca43)|Bug 1529339: Enable signing for win64-aarch64 builds, for xpcshell tests; r=Callek  Differential Revision: https://phabricator.services.mozilla.com/D20543|mozilla@hocat.ca|Callek|2019-02-21 17:57:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ddb817eed3bc)|Bug 1513000 - Updates to mozharness openh264 scripts and configs; r=callek  Differential Revision: https://phabricator.services.mozilla.com/D19817|nbeleuzu@mozilla.com|callek|2019-02-21 18:09:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=471db22054e7)|Bug 1513000 - Add taskcluster configuration for building openh264 plugin; r=callek  Differential Revision: https://phabricator.services.mozilla.com/D19818|nbeleuzu@mozilla.com|callek|2019-02-21 18:09:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6982b26698b4)|Merge mozilla-central to autoland. a=merge CLOSED TREE|nbeleuzu@mozilla.com|merge|2019-02-21 18:09:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=54ac1b47b736)|Bug 1521879 - Part 7: Create new CI jobs for media mochitests with socket process enabled. r=ahal  Differential Revision: https://phabricator.services.mozilla.com/D17942|bcampen@mozilla.com|ahal|2019-02-21 19:03:41|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=679b06a8a1aa)|Bug 1526777 - [mozharness] Restrict success_codes hack in desktop_unittest.py to Windows 7 reftests, r=jmaher  Bug 1120644 will be used to look into why Windows 7 reftests are still returning 1.  Differential Revision: https://phabricator.services.mozilla.com/D20665|ahalberstadt@mozilla.com|jmaher|2019-02-21 19:09:04|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a20e8e924046)|Backed out 9 changesets (bug 1521879) for flake failures at /transforms/tests.py. CLOSED TREE  Backed out changeset baac167868b3 (bug 1521879) Backed out changeset 54ac1b47b736 (bug 1521879) Backed out changeset 94b62c6f22e2 (bug 1521879) Backed out changeset d44f15fd4529 (bug 1521879) Backed out changeset 761fca0514fb (bug 1521879) Backed out changeset 0b85b1a7c1ce (bug 1521879) Backed out changeset 5dc76e863a02 (bug 1521879) Backed out changeset 604b9a007fe5 (bug 1521879) Backed out changeset c414d82a5325 (bug 1521879)|cbrindusan@mozilla.com||2019-02-21 19:33:34|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8dbdd56ebab4)|Bug 1528985 - [ci] Fix typo in raptor task's try-name, r=rwood  This was causing a JavaScript error in the |mach try chooser| interface since the space resulted in invalid CSS selectors being used.  Differential Revision: https://phabricator.services.mozilla.com/D20710|ahalberstadt@mozilla.com|rwood|2019-02-22 00:01:20|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f7e68519a296)|Bug 1529655 - Have Raptor pixel 2 arm7 jobs run on mozilla-central and try only; r=jmaher,davehunt  Differential Revision: https://phabricator.services.mozilla.com/D20708|dhunt@mozilla.com|jmaher,davehunt|2019-02-22 00:02:40|

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
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=866b41f7bb69)|Bug 1472589 - Fix parent process crash reporting in the Snap package environment. r=ted,jlorenzo a=lizzard  1. The unsetting of LD_LIBRARY_PATH is removed, because it's no longer necessary and interferes with environments where it's necessary to find "system" libraries like GTK; see bug 1472589 comment #1 through #4.  2. The Snap package manifest adds a dependency on the libcurl package, so that the crash reporter can send the report.  This uses the GnuTLS variant because we're already pulling in GnuTLS as a dependency of some other packages (FFmpeg and CUPS, but also the non-GnuTLS cURL packages depend on it anyway via OpenLDAP).  Differential Revision: https://phabricator.services.mozilla.com/D18625|aiakab@mozilla.com|ted,jlorenzo|2019-02-21 04:38:27|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=872914c3d0b9)|Bug 1527066: Add new ConsoleLogger type, and make it the default r=aki  Differential Revision: https://phabricator.services.mozilla.com/D19408|csabou@mozilla.com|aki|2019-02-21 05:41:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=fe259096e7ed)|Bug 1529033 - Update gn build to pick up MSVC /WX fix r=glandium  Differential Revision: https://phabricator.services.mozilla.com/D20375|csabou@mozilla.com|glandium|2019-02-21 05:41:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5f8330e12825)|Backed out changeset fe259096e7ed (bug 1529033) for failing toolchains on a CLOSED TREE|csabou@mozilla.com||2019-02-21 05:41:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=eca15205ecb1)|Bug 1528427: Optimize tasks scheduled with try syntax r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20403|csabou@mozilla.com|tomprince|2019-02-21 05:41:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f4bd1f216081)|Bug 1522111 - Followup, improve SETA algorithm a bit more by treating opt low value as low value for pgo as well. Unless there is a high value task to override. r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D20390|csabou@mozilla.com|jmaher|2019-02-21 05:41:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6939a3b5e2e4)|Bug 1529339 - replace test-provisioner with permanent bitbar provisioner id r=jmaher  Changes:  - replaced existing references to `test-provisioner/bitbar` with `bitbar/gecko-t-win10-aarch64` (proposed permanent provisioner-id)  Differential Revision: https://phabricator.services.mozilla.com/D20536|opoprus@mozilla.com|jmaher|2019-02-21 11:28:57|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ddb817eed3bc)|Bug 1513000 - Updates to mozharness openh264 scripts and configs; r=callek  Differential Revision: https://phabricator.services.mozilla.com/D19817|nbeleuzu@mozilla.com|callek|2019-02-21 17:56:54|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=471db22054e7)|Bug 1513000 - Add taskcluster configuration for building openh264 plugin; r=callek  Differential Revision: https://phabricator.services.mozilla.com/D19818|nbeleuzu@mozilla.com|callek|2019-02-21 17:56:54|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=897cb0bac95e)|Bug 1528362: [taskgraph] Change scheduler-id to include the trust-domain; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D20048|nbeleuzu@mozilla.com|dustin|2019-02-21 17:59:59|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=424f97dc01db)|Bug 1528362: [taskgraph] Use trust-domain prefixed caches; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D20049|nbeleuzu@mozilla.com|dustin|2019-02-21 17:59:59|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=872914c3d0b9)|Bug 1527066: Add new ConsoleLogger type, and make it the default r=aki  Differential Revision: https://phabricator.services.mozilla.com/D19408|csabou@mozilla.com|aki|2019-02-21 05:45:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=fe259096e7ed)|Bug 1529033 - Update gn build to pick up MSVC /WX fix r=glandium  Differential Revision: https://phabricator.services.mozilla.com/D20375|csabou@mozilla.com|glandium|2019-02-21 05:45:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5f8330e12825)|Backed out changeset fe259096e7ed (bug 1529033) for failing toolchains on a CLOSED TREE|csabou@mozilla.com||2019-02-21 05:45:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=eca15205ecb1)|Bug 1528427: Optimize tasks scheduled with try syntax r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20403|csabou@mozilla.com|tomprince|2019-02-21 05:45:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f4bd1f216081)|Bug 1522111 - Followup, improve SETA algorithm a bit more by treating opt low value as low value for pgo as well. Unless there is a high value task to override. r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D20390|csabou@mozilla.com|jmaher|2019-02-21 05:45:15|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6939a3b5e2e4)|Bug 1529339 - replace test-provisioner with permanent bitbar provisioner id r=jmaher  Changes:  - replaced existing references to `test-provisioner/bitbar` with `bitbar/gecko-t-win10-aarch64` (proposed permanent provisioner-id)  Differential Revision: https://phabricator.services.mozilla.com/D20536|opoprus@mozilla.com|jmaher|2019-02-21 11:45:58|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ddb817eed3bc)|Bug 1513000 - Updates to mozharness openh264 scripts and configs; r=callek  Differential Revision: https://phabricator.services.mozilla.com/D19817|dminor@mozilla.com|callek|2019-02-21 14:12:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=471db22054e7)|Bug 1513000 - Add taskcluster configuration for building openh264 plugin; r=callek  Differential Revision: https://phabricator.services.mozilla.com/D19818|dminor@mozilla.com|callek|2019-02-21 14:12:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=897cb0bac95e)|Bug 1528362: [taskgraph] Change scheduler-id to include the trust-domain; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D20048|nbeleuzu@mozilla.com|dustin|2019-02-21 18:13:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=424f97dc01db)|Bug 1528362: [taskgraph] Use trust-domain prefixed caches; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D20049|nbeleuzu@mozilla.com|dustin|2019-02-21 18:13:01|

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
|[Link](https://github.com/mozilla-releng/build-puppet/commit/4e838bf6382357c6cd4e5ab3ec0d2280885e9f7b)|scriptworker 20.0.1 (#403)|escapewindow|N/A|2019-02-21 18:32:51|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/52dc060760c81bd7bd19b5c63cbeeb321670c300)|Bump scriptworker to 20.0.0 (#391)  Provide Github token to request API more than 60 times an hour|JohanLorenzo|N/A|2019-02-21 14:25:23|

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

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
|[Link](https://github.com/taskcluster/taskcluster/commit/c7670d403092259fe67ac1010e95275a09088e92)|Merge pull request #152 from taskcluster/bug-1307271  [Bug 1307271] Move to structured logging|imbstack|N/A|2019-02-21 21:59:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/7787589899ee23fdd955e3a389510af1bab96365)|Turn down default process reporting freq|imbstack|N/A|2019-02-21 17:27:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/5b6a39db2786c90f3da50dc688939cedbe0cf359)|Update logging format to work with more gke tooling|imbstack|N/A|2019-02-21 05:48:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/a63ba4023aac2fdc5ac4859ded30d2e72754ae26)|Update references|imbstack|N/A|2019-02-21 04:55:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/a9220b9daa023acb7acba1f100cd57ec9b2be223)|Add top-level Message field|imbstack|N/A|2019-02-21 04:54:28|
|[Link](https://github.com/taskcluster/taskcluster/commit/12515e3826b1d903865eff0a8cc93b2b1273b91e)|Couple of followups from review|imbstack|N/A|2019-02-21 04:46:49|
|[Link](https://github.com/taskcluster/taskcluster/commit/9297b41a27f0c785ef3b9338757dd65b6d61446d)|A couple quality-of-life fixes for monitor|imbstack|N/A|2019-02-21 04:43:28|
|[Link](https://github.com/taskcluster/taskcluster/commit/2ddcdd5ef08c3b8a27856d7f7aa2245fabdacd72)|Add a bit more usage to README|imbstack|N/A|2019-02-21 04:33:44|
|[Link](https://github.com/taskcluster/taskcluster/commit/777bc5fb8bd6503ad48e357a35ea70311a4a56dc)|Make monitor not patch things when disabled|imbstack|N/A|2019-02-21 04:29:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/ccee7eabe3e2e6246bdce3f3e3eddb3cd2ce0672)|Fix some issues with logging type names|imbstack|N/A|2019-02-21 04:25:23|
|[Link](https://github.com/taskcluster/taskcluster/commit/c52f486559e7a2ddd7556cecbadd9bec828aea8a)|Fix old cases in README of monitor|imbstack|N/A|2019-02-21 03:39:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/d6ac06a5ee8f3f892a79fa0906edb19c185089be)|Pass through pretty logging via env var|imbstack|N/A|2019-02-21 03:37:13|
|[Link](https://github.com/taskcluster/taskcluster/commit/ef48c20c2ae65cfe669bdbd3914fbf0be20d8410)|Make irc message work with verification|imbstack|N/A|2019-02-21 03:20:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/e1c98fede093acd473365472cf483768aaf3a906)|[Bug 1520918] Add denylist queries to web-server (#270)|OjaswinM|N/A|2019-02-21 20:07:21|
|[Link](https://github.com/taskcluster/taskcluster/commit/8984c751f92b7e0a0d2c3a257ce48864fe266bd1)|Add 'follow log' to TaskLog (#276)|Aditya-Kolla|N/A|2019-02-21 18:09:22|
|[Link](https://github.com/taskcluster/taskcluster/commit/f58547365656bbae578f8d554bc98e41703fee5f)|Add Search feature to Secrets (#273)|Aditya-Kolla|N/A|2019-02-21 18:06:05|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
