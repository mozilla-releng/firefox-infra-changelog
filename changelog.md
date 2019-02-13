##  Commits in production - for one day, generated on: 2019-02-13 19:16:14 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=34f33ae5913e)|Backed out 3 changesets (bug 1525959, bug 1526002) for failing android  Backed out changeset de0efca1118e (bug 1526002) Backed out changeset 503cbc86e442 (bug 1525959) Backed out changeset 33ea61c54aea (bug 1525959)|apavel@mozilla.com||2019-02-12 23:53:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=de25d2f1abef)|Bug 1505538 - Release x86_64 Fennec Nightly in the Google Play Store r=mtabara  Release x86_64 Fennec Nightly in the Google Play Store  Differential Revision: https://phabricator.services.mozilla.com/D19534|mtabara@mozilla.com|mtabara|2019-02-13 01:00:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a90e2dd8b1a5)|Bug 1525738 - Stop running Android 7.0 x86_64 geckoview-junit tests; r=mbrubeck|rmaries@mozilla.com|mbrubeck|2019-02-13 07:24:43|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=636d2c00234d)|Bug 1527011 - Support win64-aarch64 artifact builds; r=nalexander|rmaries@mozilla.com|nalexander|2019-02-13 07:24:43|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1af69c96ec5f)|Merge mozilla-central to autoland. a=merge on a CLOSED TREE|rmaries@mozilla.com|merge|2019-02-13 07:24:43|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e7603feb2252)|Bug 1527118: Ensure all tests are using tooltool caches r=aki  respect TOOLTOOL_CACHE environment variable in mixin  Differential Revision: https://phabricator.services.mozilla.com/D19444|mozilla@hocat.ca|aki|2019-02-13 08:26:42|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=dbf72abf5597)|Bug 1472589 - Fix parent process crash reporting in the Snap package environment. r=ted,jlorenzo  1. The unsetting of LD_LIBRARY_PATH is removed, because it's no longer necessary and interferes with environments where it's necessary to find "system" libraries like GTK; see bug 1472589 comment #1 through #4.  2. The Snap package manifest adds a dependency on the libcurl package, so that the crash reporter can send the report.  This uses the GnuTLS variant because we're already pulling in GnuTLS as a dependency of some other packages (FFmpeg and CUPS, but also the non-GnuTLS cURL packages depend on it anyway via OpenLDAP).  Differential Revision: https://phabricator.services.mozilla.com/D18625|jedavis@mozilla.com|ted,jlorenzo|2019-02-13 18:08:25|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=529fc3665945)|Backed out changeset c6dddbdcedb6 (bug 1465844) for breaking mozilla-taskcluster|mozilla@hocat.ca||2019-02-13 08:06:03|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a90e2dd8b1a5)|Bug 1525738 - Stop running Android 7.0 x86_64 geckoview-junit tests; r=mbrubeck|rmaries@mozilla.com|mbrubeck|2019-02-13 06:27:59|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=636d2c00234d)|Bug 1527011 - Support win64-aarch64 artifact builds; r=nalexander|rmaries@mozilla.com|nalexander|2019-02-13 06:27:59|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=33ea61c54aea)|Bug 1525959 - Run GeckoView mochitests on x86_64 emulators in automation r=gbrown  Differential Revision: https://phabricator.services.mozilla.com/D19015|opoprus@mozilla.com|gbrown|2019-02-13 11:48:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=34f33ae5913e)|Backed out 3 changesets (bug 1525959, bug 1526002) for failing android  Backed out changeset de0efca1118e (bug 1526002) Backed out changeset 503cbc86e442 (bug 1525959) Backed out changeset 33ea61c54aea (bug 1525959)|opoprus@mozilla.com||2019-02-13 11:48:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=de25d2f1abef)|Bug 1505538 - Release x86_64 Fennec Nightly in the Google Play Store r=mtabara  Release x86_64 Fennec Nightly in the Google Play Store  Differential Revision: https://phabricator.services.mozilla.com/D19534|opoprus@mozilla.com|mtabara|2019-02-13 11:48:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1af69c96ec5f)|Merge mozilla-central to autoland. a=merge on a CLOSED TREE|opoprus@mozilla.com|merge|2019-02-13 11:48:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e7603feb2252)|Bug 1527118: Ensure all tests are using tooltool caches r=aki  respect TOOLTOOL_CACHE environment variable in mixin  Differential Revision: https://phabricator.services.mozilla.com/D19444|opoprus@mozilla.com|aki|2019-02-13 11:48:26|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=636d2c00234d)|Bug 1527011 - Support win64-aarch64 artifact builds; r=nalexander|gbrown@mozilla.com|nalexander|2019-02-13 03:03:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=33ea61c54aea)|Bug 1525959 - Run GeckoView mochitests on x86_64 emulators in automation r=gbrown  Differential Revision: https://phabricator.services.mozilla.com/D19015|opoprus@mozilla.com|gbrown|2019-02-13 12:39:30|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=34f33ae5913e)|Backed out 3 changesets (bug 1525959, bug 1526002) for failing android  Backed out changeset de0efca1118e (bug 1526002) Backed out changeset 503cbc86e442 (bug 1525959) Backed out changeset 33ea61c54aea (bug 1525959)|opoprus@mozilla.com||2019-02-13 12:39:30|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=de25d2f1abef)|Bug 1505538 - Release x86_64 Fennec Nightly in the Google Play Store r=mtabara  Release x86_64 Fennec Nightly in the Google Play Store  Differential Revision: https://phabricator.services.mozilla.com/D19534|opoprus@mozilla.com|mtabara|2019-02-13 12:39:30|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=1af69c96ec5f)|Merge mozilla-central to autoland. a=merge on a CLOSED TREE|opoprus@mozilla.com|merge|2019-02-13 12:39:30|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e7603feb2252)|Bug 1527118: Ensure all tests are using tooltool caches r=aki  respect TOOLTOOL_CACHE environment variable in mixin  Differential Revision: https://phabricator.services.mozilla.com/D19444|opoprus@mozilla.com|aki|2019-02-13 12:39:30|

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
|[Link](https://github.com/mozilla-releng/build-puppet/commit/f839f7ec5d2b7ba0889c423f014a722e98dcfb95)|Scheduled weekly dependency update for week 06 (#396)    Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update arrow from 0.13.0 to 0.13.1      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update virtualenv from 16.3.0 to 16.4.0      Update boto3 from 1.9.88 to 1.9.93      Update botocore from 1.12.88 to 1.12.93      Update s3transfer from 0.1.13 to 0.2.0      Update lxml from 4.3.0 to 4.3.1      Update mozapkpublisher from 0.14.1 to 1.0.1      Update parso from 0.3.3 to 0.3.4|pyup-bot|N/A|2019-02-13 15:27:26|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/658e6337ad59c3193387771d2eef35ce9a199e06)|Merge pull request #213 from djmitche/bug1527183  Bug 1527183 - fix schema for bindings|djmitche|N/A|2019-02-13 19:03:11|
|[Link](https://github.com/taskcluster/taskcluster/commit/8d2cd6d94fc53c04cd79772e379cbce4775c67d6)|Web server on kube (#194)    Exclude docs from build      Add configuration for web-server      Add ingress rule for web-server      Point web-ui to the web-server in Kube|owlishDeveloper|N/A|2019-02-13 16:51:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/7d712337608d7806bdd6d8632ed23bd349994cde)|Merge pull request #212 from djmitche/bug1527416  Bug 1527416 - get a fresh copy of the hook before triggering|djmitche|N/A|2019-02-13 01:18:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/a17d0f0b0a012049cb3023c6863c2c9be83a6b26)|Bug 1527416 - get a fresh copy of the hook before triggering|djmitche|N/A|2019-02-12 20:07:32|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
