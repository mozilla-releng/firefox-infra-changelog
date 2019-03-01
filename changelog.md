##  Commits in production - for one day, generated on: 2019-03-01 18:15:47 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b37ec76ca307)|Bug 1531072 - Use better timeout for l10n. r=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D21586|jwood@mozilla.com|RyanVM|2019-02-28 22:14:35|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1a272d807e84)|Bug 1524495 - Disble Raptor ugl geckoview job b/c of permafail; r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D21572|rwood@mozilla.com|davehunt|2019-02-28 22:21:31|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cdd251b5b7f1)|Bug 1530737 - Run windows10-aarch64 talos/raptor tasks on bitbar laptops; r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D21574|gbrown@mozilla.com|jmaher|2019-03-01 02:26:28|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9ce8f26f311b)|Bug 1513000 - expose revision as an attribute on the openh264 jobs. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D21606|jwood@mozilla.com|tomprince|2019-03-01 05:06:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=81a50b35b482)|Bug 1513000 - Sign openh264 binaries. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20763|jwood@mozilla.com|tomprince|2019-03-01 05:06:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=26021d8ebb27)|Bug 1513000 - Create action to trigger Openh264. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20850|jwood@mozilla.com|tomprince|2019-03-01 05:06:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=dcfebc36f75c)|Bug 1531441 - Re-enable Raptor android ugl temporarily as tier 3, pending benchmark upgrade; r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D21713|rwood@mozilla.com|davehunt|2019-03-01 20:00:32|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=f4552aaf7083)|Bug 1515990: Grant access to all `aws-provisioner/mozillaonline-L-*` to MozillaOnline; r=me|mozilla@hocat.ca|me|2019-03-01 19:13:48|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=fb0ffd7766a2)|Bug 1451860 - Rename the tps Talos test to tabswitch. r=mconley,davehunt  Differential Revision: https://phabricator.services.mozilla.com/D20096|opoprus@mozilla.com|mconley,davehunt|2019-02-28 23:44:07|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4024f3814d18)|Bug 1523877 Add Instagram and bing to tp6-m r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D18072|opoprus@mozilla.com|davehunt|2019-02-28 23:44:07|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=694837e25cc6)|Bug 1526584: [win64-aarch64] Only add win64-aarch64 platform to balrog blog for firefox; r=mtabara  This reverts the refactoring in 0734f7d57cd81464053e7ffacc8897fce1a27d61 so only the firefox blob gets the new platform. This was causing failure in the subsequent release promotion task, as it made assumptions about the structure of the balrog blob.  Differential Revision: https://phabricator.services.mozilla.com/D21494|opoprus@mozilla.com|mtabara|2019-02-28 23:44:07|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=73298bafb7ae)|Bug 1496341 - Run debugger tests on try. r=loganfsmyth,ahal  Differential Revision: https://phabricator.services.mozilla.com/D21217|opoprus@mozilla.com|loganfsmyth,ahal|2019-02-28 23:44:07|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b37ec76ca307)|Bug 1531072 - Use better timeout for l10n. r=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D21586|opoprus@mozilla.com|RyanVM|2019-03-01 07:20:57|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1a272d807e84)|Bug 1524495 - Disble Raptor ugl geckoview job b/c of permafail; r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D21572|opoprus@mozilla.com|davehunt|2019-03-01 07:20:57|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cdd251b5b7f1)|Bug 1530737 - Run windows10-aarch64 talos/raptor tasks on bitbar laptops; r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D21574|opoprus@mozilla.com|jmaher|2019-03-01 07:20:57|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9ce8f26f311b)|Bug 1513000 - expose revision as an attribute on the openh264 jobs. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D21606|rgurzau@mozilla.com|tomprince|2019-03-01 14:56:42|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=81a50b35b482)|Bug 1513000 - Sign openh264 binaries. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20763|rgurzau@mozilla.com|tomprince|2019-03-01 14:56:42|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=26021d8ebb27)|Bug 1513000 - Create action to trigger Openh264. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20850|rgurzau@mozilla.com|tomprince|2019-03-01 14:56:42|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=08157bb630a6)|Merge mozilla-central to inbound.  a=merge CLOSED TREE|rgurzau@mozilla.com|merge|2019-03-01 15:06:03|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=fb0ffd7766a2)|Bug 1451860 - Rename the tps Talos test to tabswitch. r=mconley,davehunt  Differential Revision: https://phabricator.services.mozilla.com/D20096|opoprus@mozilla.com|mconley,davehunt|2019-03-01 00:09:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4024f3814d18)|Bug 1523877 Add Instagram and bing to tp6-m r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D18072|opoprus@mozilla.com|davehunt|2019-03-01 00:09:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=694837e25cc6)|Bug 1526584: [win64-aarch64] Only add win64-aarch64 platform to balrog blog for firefox; r=mtabara  This reverts the refactoring in 0734f7d57cd81464053e7ffacc8897fce1a27d61 so only the firefox blob gets the new platform. This was causing failure in the subsequent release promotion task, as it made assumptions about the structure of the balrog blob.  Differential Revision: https://phabricator.services.mozilla.com/D21494|opoprus@mozilla.com|mtabara|2019-03-01 00:09:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=73298bafb7ae)|Bug 1496341 - Run debugger tests on try. r=loganfsmyth,ahal  Differential Revision: https://phabricator.services.mozilla.com/D21217|opoprus@mozilla.com|loganfsmyth,ahal|2019-03-01 00:09:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=08157bb630a6)|Merge mozilla-central to inbound.  a=merge CLOSED TREE|opoprus@mozilla.com|merge|2019-03-01 00:09:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9ce8f26f311b)|Bug 1513000 - expose revision as an attribute on the openh264 jobs. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D21606|rgurzau@mozilla.com|tomprince|2019-03-01 15:23:13|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=81a50b35b482)|Bug 1513000 - Sign openh264 binaries. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20763|rgurzau@mozilla.com|tomprince|2019-03-01 15:23:13|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=26021d8ebb27)|Bug 1513000 - Create action to trigger Openh264. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D20850|rgurzau@mozilla.com|tomprince|2019-03-01 15:23:13|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/43dbf66e7573a9685345d3af8b520ecbdb180d33)|Update @mozilla-frontend-infra/components (#333)  Also remove global background color on pre elements. elements with pre  tags should be formatted with highlight.js|helfi92|N/A|2019-03-01 16:28:44|
|[Link](https://github.com/taskcluster/taskcluster/commit/340f496f1c7afdffd8d17c623875148c6d77ed34)|Make docs theme consistent with site (#332)|helfi92|N/A|2019-03-01 16:00:29|
|[Link](https://github.com/taskcluster/taskcluster/commit/2e5ea8038ce24b771d398bb2c64c3d7118675319)|[UI] Reopen docs section menu when clicking "next" (#331)|sudipt1999|N/A|2019-03-01 13:19:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/f295cb3302140cfe163763bea2f9d798a6d68144)|Merge pull request #323 from djmitche/bug1527424  Bug 1527424 - clean up error handling in TaskCreator|djmitche|N/A|2019-02-28 18:55:17|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
