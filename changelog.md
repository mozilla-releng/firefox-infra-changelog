##  Commits in production - for one day, generated on: 2019-02-24 03:22:12 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7a18c5eda62a)|Backed out 2 changesets (bug 1529921) due to a high probability of breaking nightlies CLOSED TREE  Backed out changeset 1c9d01a6fbb8 (bug 1529921) Backed out changeset fea99e80e861 (bug 1529921)|aciure@mozilla.com||2019-02-23 03:38:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6e669b1b1835)|Bug 1500941 - Add searchfox task for Android (ARMv7/API16). r=nalexander  The bulk of this is copy/pasted from a standard android-api-16 debug build. The only changes are a few extra environment variables in the taskcluster config, the subconfig file, and the mozconfig, as well as the --enable-mozsearch-plugin flag in the mozconfig.  Depends on D20766  Differential Revision: https://phabricator.services.mozilla.com/D20767|kgupta@mozilla.com|nalexander|2019-02-23 14:18:46|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=10ffd49d0adf)|Bug 1500941 - Enable Android searchfox job as part of the daily cron. r=emilio  Depends on D20767  Differential Revision: https://phabricator.services.mozilla.com/D20768|kgupta@mozilla.com|emilio|2019-02-23 14:18:46|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=07c7cd57cc90)|Bug 1527394: Squash docker images before exporting/compressing them r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D19541|nbeleuzu@mozilla.com|tomprince|2019-02-24 00:49:34|

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
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=abcb8be12adf)|Bug 1521879 - Part 7: Create new CI jobs for media mochitests with socket process enabled. r=ahal  Differential Revision: https://phabricator.services.mozilla.com/D17942|rmaries@mozilla.com|ahal|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d73453c15f88)|Bug 1529781 - Increase test chunks for linux64 jsreftests; r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D20777|rmaries@mozilla.com|jmaher|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a19e904c615c)|Bug 1529948: Switch default for actions from `task` to `hook`; r=Callek  Support for `kind='task'` is still around to support Thunderbird release promotion, which uses releaserunner3. Other actions shouldn't be using it.  Differential Revision: https://phabricator.services.mozilla.com/D20842|rmaries@mozilla.com|Callek|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2238d806904d)|Bug 1529948: Remove obsolete documetation about action tasks; r=Callek  Support for them was removed in Bug 1415868 (a891a10ca4d9).  Differential Revision: https://phabricator.services.mozilla.com/D20843|rmaries@mozilla.com|Callek|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=be65446f94a5)|Bug 1529948: Update action documentation to have correct imports; r=Callek  Differential Revision: https://phabricator.services.mozilla.com/D20845|rmaries@mozilla.com|Callek|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d62b974d529c)|Bug 1529948: Fix refernce to `mach test-action-callback`; r=Callek  Differential Revision: https://phabricator.services.mozilla.com/D20846|rmaries@mozilla.com|Callek|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b892c1e3909f)|Bug 1520523 - Update Raptor Chromium rev; r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D20814|rmaries@mozilla.com|davehunt|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e89b6e3d3de8)|Bug 1520163 - Add linux64-nasm toolchain. r=glandium  Differential Revision: https://phabricator.services.mozilla.com/D20037|rmaries@mozilla.com|glandium|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4978133d6226)|Backed out changeset e89b6e3d3de8 (bug 1520163) for profile-guided optimization builds bustage CLOSED TREE|rmaries@mozilla.com||2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e9e880f7aee4)|Bug 1520163 - Add linux64-nasm toolchain. r=glandium  Differential Revision: https://phabricator.services.mozilla.com/D20037|rmaries@mozilla.com|glandium|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=bd636f4cd2a4)|Bug 1528405 - Increase max-run-time for some linux builds; r=jmaher  Increase max-run-time to avoid intermittent task timeouts.  Differential Revision: https://phabricator.services.mozilla.com/D20882|rmaries@mozilla.com|jmaher|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5612534374b4)|Bug 1529921: Use secrets from taskcluster for windows builds; r=aki  Differential Revision: https://phabricator.services.mozilla.com/D20849|rmaries@mozilla.com|aki|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=136df62ef081)|Backed out changeset 5612534374b4 (bug 1529921) for causing build bustages CLOSED TREE|rmaries@mozilla.com||2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=fea99e80e861)|Bug 1529921: Use secrets from taskcluster for windows builds; r=aki  Differential Revision: https://phabricator.services.mozilla.com/D20849|rmaries@mozilla.com|aki|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1c9d01a6fbb8)|Bug 1529921: Pass `scm_level` to mozharness tasks on windows; r=aki  Differential Revision: https://phabricator.services.mozilla.com/D20893|rmaries@mozilla.com|aki|2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7a18c5eda62a)|Backed out 2 changesets (bug 1529921) due to a high probability of breaking nightlies CLOSED TREE  Backed out changeset 1c9d01a6fbb8 (bug 1529921) Backed out changeset fea99e80e861 (bug 1529921)|rmaries@mozilla.com||2019-02-23 06:13:22|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6e669b1b1835)|Bug 1500941 - Add searchfox task for Android (ARMv7/API16). r=nalexander  The bulk of this is copy/pasted from a standard android-api-16 debug build. The only changes are a few extra environment variables in the taskcluster config, the subconfig file, and the mozconfig, as well as the --enable-mozsearch-plugin flag in the mozconfig.  Depends on D20766  Differential Revision: https://phabricator.services.mozilla.com/D20767|csabou@mozilla.com|nalexander|2019-02-23 23:38:35|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=10ffd49d0adf)|Bug 1500941 - Enable Android searchfox job as part of the daily cron. r=emilio  Depends on D20767  Differential Revision: https://phabricator.services.mozilla.com/D20768|csabou@mozilla.com|emilio|2019-02-23 23:38:35|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=abcb8be12adf)|Bug 1521879 - Part 7: Create new CI jobs for media mochitests with socket process enabled. r=ahal  Differential Revision: https://phabricator.services.mozilla.com/D17942|rmaries@mozilla.com|ahal|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d73453c15f88)|Bug 1529781 - Increase test chunks for linux64 jsreftests; r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D20777|rmaries@mozilla.com|jmaher|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a19e904c615c)|Bug 1529948: Switch default for actions from `task` to `hook`; r=Callek  Support for `kind='task'` is still around to support Thunderbird release promotion, which uses releaserunner3. Other actions shouldn't be using it.  Differential Revision: https://phabricator.services.mozilla.com/D20842|rmaries@mozilla.com|Callek|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2238d806904d)|Bug 1529948: Remove obsolete documetation about action tasks; r=Callek  Support for them was removed in Bug 1415868 (a891a10ca4d9).  Differential Revision: https://phabricator.services.mozilla.com/D20843|rmaries@mozilla.com|Callek|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=be65446f94a5)|Bug 1529948: Update action documentation to have correct imports; r=Callek  Differential Revision: https://phabricator.services.mozilla.com/D20845|rmaries@mozilla.com|Callek|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d62b974d529c)|Bug 1529948: Fix refernce to `mach test-action-callback`; r=Callek  Differential Revision: https://phabricator.services.mozilla.com/D20846|rmaries@mozilla.com|Callek|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b892c1e3909f)|Bug 1520523 - Update Raptor Chromium rev; r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D20814|rmaries@mozilla.com|davehunt|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e89b6e3d3de8)|Bug 1520163 - Add linux64-nasm toolchain. r=glandium  Differential Revision: https://phabricator.services.mozilla.com/D20037|rmaries@mozilla.com|glandium|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4978133d6226)|Backed out changeset e89b6e3d3de8 (bug 1520163) for profile-guided optimization builds bustage CLOSED TREE|rmaries@mozilla.com||2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e9e880f7aee4)|Bug 1520163 - Add linux64-nasm toolchain. r=glandium  Differential Revision: https://phabricator.services.mozilla.com/D20037|rmaries@mozilla.com|glandium|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=bd636f4cd2a4)|Bug 1528405 - Increase max-run-time for some linux builds; r=jmaher  Increase max-run-time to avoid intermittent task timeouts.  Differential Revision: https://phabricator.services.mozilla.com/D20882|rmaries@mozilla.com|jmaher|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5612534374b4)|Bug 1529921: Use secrets from taskcluster for windows builds; r=aki  Differential Revision: https://phabricator.services.mozilla.com/D20849|rmaries@mozilla.com|aki|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=136df62ef081)|Backed out changeset 5612534374b4 (bug 1529921) for causing build bustages CLOSED TREE|rmaries@mozilla.com||2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=fea99e80e861)|Bug 1529921: Use secrets from taskcluster for windows builds; r=aki  Differential Revision: https://phabricator.services.mozilla.com/D20849|rmaries@mozilla.com|aki|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=1c9d01a6fbb8)|Bug 1529921: Pass `scm_level` to mozharness tasks on windows; r=aki  Differential Revision: https://phabricator.services.mozilla.com/D20893|rmaries@mozilla.com|aki|2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7a18c5eda62a)|Backed out 2 changesets (bug 1529921) due to a high probability of breaking nightlies CLOSED TREE  Backed out changeset 1c9d01a6fbb8 (bug 1529921) Backed out changeset fea99e80e861 (bug 1529921)|rmaries@mozilla.com||2019-02-23 06:28:17|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6e669b1b1835)|Bug 1500941 - Add searchfox task for Android (ARMv7/API16). r=nalexander  The bulk of this is copy/pasted from a standard android-api-16 debug build. The only changes are a few extra environment variables in the taskcluster config, the subconfig file, and the mozconfig, as well as the --enable-mozsearch-plugin flag in the mozconfig.  Depends on D20766  Differential Revision: https://phabricator.services.mozilla.com/D20767|csabou@mozilla.com|nalexander|2019-02-23 23:43:14|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=10ffd49d0adf)|Bug 1500941 - Enable Android searchfox job as part of the daily cron. r=emilio  Depends on D20767  Differential Revision: https://phabricator.services.mozilla.com/D20768|csabou@mozilla.com|emilio|2019-02-23 23:43:14|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=588497dfa9c0)|Bug 1530115 - Add nasm to searchfox builds. r=me |kgupta@mozilla.com|me|2019-02-23 23:58:51|

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
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)|FIC - BOT|Self Generated| - |

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
