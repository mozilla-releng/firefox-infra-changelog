##  Commits in production - for one day, generated on: 2019-01-26 04:42:16 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloggerhtml?changeset=871d54b791a3)|Bug 1518570 - Update task cluster configuration for oak. r=tomprince  The intent is to land this on central, to minimize the merge conflicts on oak  Oak is going to be used for Updater testing so needs release keys and such, and does not need android. This approach is different than the previous oak approach in that it amends how we calculate 'trunk' and 'release' projects to include 'oak', and then makes full nightlies produced on each push.  Differential Revision: https://phabricator.services.mozilla.com/D17440|jwood@mozilla.com|tomprince|2019-01-25 16:19:42|
|[Link](https://hg.mozilla.org/integration/autoland/pushloggerhtml?changeset=da2115631f1b)|Bug 1522631 - Expand existing Raptor profiling jobs to include tp6-7, tp6-8, tp6-9, and tp6-10; r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D17538|rwood@mozilla.com|davehunt|2019-01-25 21:32:52|
|[Link](https://hg.mozilla.org/integration/autoland/pushloggerhtml?changeset=4c4c607eebde)|Bug 1518570 - Missed followup item, no need to mark oak as a trunk project. r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D17685|jwood@mozilla.com|tomprince|2019-01-25 22:59:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloggerhtml?changeset=1bb6959a6990)| Bug 1522803: Use a stable Rust version for the aarch64 Windows repack; r=froydnj|ccoroiu@mozilla.com|froydnj|2019-01-25 23:53:06|
|[Link](https://hg.mozilla.org/integration/autoland/pushloggerhtml?changeset=ad292914ca7e)|Bug 1514806: Point partner repack repackage tasks at partner repackage configs. r=aki  They were incorrectly pointed at the non-partner configs in 2e27f3f1ebc6f38d98ddd42b6955083f637e2b1b.  Differential Revision: https://phabricator.services.mozilla.com/D17716|mozilla@hocat.ca|aki|2019-01-26 03:19:09|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloggerhtml?changeset=de779760a956)|Bug 1522143 - Enable buildbot and taskcluster for the cedar project branch. r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D17608|dmitchell@mozilla.com|dustin|2019-01-25 16:26:22|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloggerhtml?changeset=0905dd1fbcbb)|Backed out changeset de779760a956|dmitchell@mozilla.com||2019-01-25 17:25:45|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloggerhtml?changeset=2b9e4ff2aa09)|Bug 1522143 - Enable taskcluster for the cedar project branch. r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D17608|mozilla@hocat.ca|dustin|2019-01-25 19:31:53|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloggerhtml?changeset=871d54b791a3)|Bug 1518570 - Update task cluster configuration for oak. r=tomprince  The intent is to land this on central, to minimize the merge conflicts on oak  Oak is going to be used for Updater testing so needs release keys and such, and does not need android. This approach is different than the previous oak approach in that it amends how we calculate 'trunk' and 'release' projects to include 'oak', and then makes full nightlies produced on each push.  Differential Revision: https://phabricator.services.mozilla.com/D17440|ccoroiu@mozilla.com|tomprince|2019-01-25 23:48:48|
|[Link](https://hg.mozilla.org/mozilla-central/pushloggerhtml?changeset=1bb6959a6990)| Bug 1522803: Use a stable Rust version for the aarch64 Windows repack; r=froydnj|ccoroiu@mozilla.com|froydnj|2019-01-25 23:50:13|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloggerhtml?changeset=1bb6959a6990)| Bug 1522803: Use a stable Rust version for the aarch64 Windows repack; r=froydnj|bbouvier@mozilla.com|froydnj|2019-01-25 19:09:19|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloggerhtml?changeset=871d54b791a3)|Bug 1518570 - Update task cluster configuration for oak. r=tomprince  The intent is to land this on central, to minimize the merge conflicts on oak  Oak is going to be used for Updater testing so needs release keys and such, and does not need android. This approach is different than the previous oak approach in that it amends how we calculate 'trunk' and 'release' projects to include 'oak', and then makes full nightlies produced on each push.  Differential Revision: https://phabricator.services.mozilla.com/D17440|ccoroiu@mozilla.com|tomprince|2019-01-25 23:56:18|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/addonscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/addonscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/balrogscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/balrogscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/beetmoverscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/beetmoverscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/f55ca9aef7ab6a4e1e5d5c246beff1085d201fe0)|Merge pull request #206 from mozilla-releng/bug-1522581  Bug 1522581 - Bump max size of zip file to 300MB|mitchhentges|N/A|2019-01-25 18:29:36|
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/b74438929aaa119dd6ca3def99cadfb39d6a4559)|8.3.1|JohanLorenzo|N/A|2019-01-25 13:25:55|
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/002b073054a74e3f7dd2fcf0faf282e50ab4a942)|Bug 1522581 - Bump max size of zip file to 300MB|JohanLorenzo|N/A|2019-01-25 13:11:21|

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/bouncerscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/bouncerscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/build-cloud-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/build-puppet.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/fcf7b1016d091b118ed747e2cda9082e19f29384)|Merge pull request #373 from mitchhentges/beetmoverscript-bump-file-size  Bumps beetmoverscript version|mitchhentges|N/A|2019-01-25 18:50:04|

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/mozapkpublisher.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/pushapkscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/pushsnapscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/scriptworker.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/services.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/services.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla/release-services/commit/981d853ccfa054bac79247bca4e5aedc81d1ab14)|shipit/api: fixes for product details (#1814)|garbas|N/A|2019-01-25 18:00:49|

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/shipitscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	signingscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/signingscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/signingscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/signtool.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/signtool.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/taskcluster.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/taskcluster.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/1469bc7c6d19e11792657ec9f1734f65241cdd92)|Merge pull request #151 from taskcluster/update-readme  Update READMEs|imbstack|N/A|2019-01-25 21:49:30|
|[Link](https://github.com/taskcluster/taskcluster/commit/15ea79a78cc21068b9fe8f5f3c9bfc7a8d02b798)|Bug 1522913 - Update "Extra" section when changing taskIds (#153)|helfi92|N/A|2019-01-25 18:54:56|
|[Link](https://github.com/taskcluster/taskcluster/commit/912e0d6f0a86335871bb742436ee74a9eac69d4c)|Bug 1516347 - new images|djmitche|N/A|2019-01-25 18:27:38|
|[Link](https://github.com/taskcluster/taskcluster/commit/ac6ad8e8de17ce623e34cf816ee952a0be37383f)|Merge pull request #129 from djmitche/bug1516347  Bug 1516347 - monoimage|djmitche|N/A|2019-01-25 18:13:46|
|[Link](https://github.com/taskcluster/taskcluster/commit/fdff4fa703c2d0652021ebad577d5723537db0bb)|Merge pull request #150 from taskcluster/add-pr-template  Create pull_request_template.md|imbstack|N/A|2019-01-25 18:04:40|
|[Link](https://github.com/taskcluster/taskcluster/commit/22a956fa3ea04d34ee0bbef5b06fa056e9d8ec84)|Update pull_request_template.md|imbstack|N/A|2019-01-25 18:04:25|
|[Link](https://github.com/taskcluster/taskcluster/commit/f4e4fc80a26c30af7d69c51ff2a5b6063b4bbb44)|Update READMEs|imbstack|N/A|2019-01-25 17:43:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/36553b808fddf55a15b5739fa2912787a65af83a)|Update dependency karma-cli to v2 (#138)|renovate[bot]|N/A|2019-01-25 18:00:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/ada68546df8335a30352ec9970c3c62b4cd471fc)|Create pull_request_template.md  This is pretty simple. We can get more complex later if we want|imbstack|N/A|2019-01-25 17:20:26|
|[Link](https://github.com/taskcluster/taskcluster/commit/45acc854a52475540703d99dfd2aa45d95381c60)|Bug 1516347 - set up web-server to run in dev mode too|djmitche|N/A|2019-01-25 16:52:54|
|[Link](https://github.com/taskcluster/taskcluster/commit/ef86a1d1d05522a60a6292d8a4f30f9cd9d69515)|Configure renovate to send PRs on a weekly basis (#149)|helfi92|N/A|2019-01-25 16:14:16|
|[Link](https://github.com/taskcluster/taskcluster/commit/dfee9af2438503514b00b0df8dbbfb8032bda517)|Update dependency karma to v4 (#137)|renovate[bot]|N/A|2019-01-25 15:56:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/cb3a73b9ac39953eb1ce878da97febb6be7291e1)|Update dependency bufferutil to v4 (#136)|renovate[bot]|N/A|2019-01-25 15:53:22|
|[Link](https://github.com/taskcluster/taskcluster/commit/41d9a1944543cc7234fa34ce98d1d0571a8984e1)|Update dependency taskcluster-lib-urls to v12 (#144)|renovate[bot]|N/A|2019-01-25 15:51:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/7e2a677dd624bacd1ea70c4ebb4e313407df27b6)|Update dependency lint-staged to v8 (#139)|renovate[bot]|N/A|2019-01-25 14:55:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/433e8cde5340ae4c98bded7e3a246550ed7c04d8)|Update dependency resolve-pathname to v3 (#143)|renovate[bot]|N/A|2019-01-25 14:11:22|
|[Link](https://github.com/taskcluster/taskcluster/commit/3d916d45912e2ad902a2887a88caf41e0d0bff20)|Fix: Worker types view modal not opening (#148)|helfi92|N/A|2019-01-25 14:05:09|
|[Link](https://github.com/taskcluster/taskcluster/commit/aca0d33455922bbcea325d597bf54d3991e77ada)|[web-server] Include hooks listlastFire api support (#121)|Biboswan|N/A|2019-01-25 13:42:05|
|[Link](https://github.com/taskcluster/taskcluster/commit/1338ad83d3ae63a1c1c992481253f626bdd2c3a1)|Update dependency utf-8-validate to v5 (#145)|renovate[bot]|N/A|2019-01-25 13:18:34|
|[Link](https://github.com/taskcluster/taskcluster/commit/5a0e8af004921efe7b08847d598ea8ad207ca04b)|Update yarn.lock for the ui (#147)|helfi92|N/A|2019-01-25 12:32:53|
|[Link](https://github.com/taskcluster/taskcluster/commit/79ec514d9392094d89d31fe98e1a412d56ac04c5)|Update netlify node version (#146)|helfi92|N/A|2019-01-25 12:17:40|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelogger/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day..|FIC - BOT|Self Generated| - |
