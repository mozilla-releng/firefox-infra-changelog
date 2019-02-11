##  Commits in production - for one day, generated on: 2019-02-11 03:24:28 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cdcbd5b13210)|Bug 1525760 - Add a clang-based base toolchains task. r=froydnj  These are copies of the corresponding gcc-based base toolchain tasks, with FORCE_GCC and the gcc dependency removed.  We also tweak things a little for those builds to actually end up green.  Differential Revision: https://phabricator.services.mozilla.com/D18903|ealvarez@mozilla.com|froydnj|2019-02-10 04:57:04|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d6a025216838)|Bug 1394825 - Update minimum clang version to 4.0. r=glandium  libclang 3.9 has a bug that makes bindgen unable to distinguish some typedefs from the underlying type, which matters for bug 1523071.  We have had quite a few workarounds for this bug and I don't really want to add more, since in this case it is non-trivial. I think requiring libclang 4.0+ is reasonable at this point.  Of the distros that can't build Firefox out of the box with clang, dropping support for clang 3.9 would only break Ubuntu 14.04 LTS, which support ends April 2019, right before we release 67.  Differential Revision: https://phabricator.services.mozilla.com/D18889|ealvarez@mozilla.com|glandium|2019-02-10 04:57:04|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=be2938cc03f3)|Bug 1523071 - Update cbindgen. r=glandium,jwatt  Gonna need it to use https://github.com/eqrion/cbindgen/pull/275.  Differential Revision: https://phabricator.services.mozilla.com/D17736 |emilio@crisal.io|glandium,jwatt|2019-02-10 08:13:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1b147d9934f1)|Bug 1525760 - Disable base-toolchains-clang jobs for now. a=ccoroiu r=bustage  For failing in ways I cannot reason about.  It hits linker errors sometimes, and in two revisions without any single source code change between them it's green:    https://treeherder.mozilla.org/#/jobs?repo=mozilla-central&revision=952b928f1605ad5676ae4ccfd41612b34523bae5  And red:    https://treeherder.mozilla.org/#/jobs?repo=autoland&revision=952b928f1605ad5676ae4ccfd41612b34523bae5  At the same time. Which is quite baffling.  Disable the new jobs on CI for now in order to avoid backing out the whole stack of dependent patches (bug 1394825, bug 1523071 and bug 1523140) that landed afterwards. |rmaries@mozilla.com|bustage|2019-02-10 16:41:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=50309e384ceb)|Bug 1525760 - followup: Make linters happy about a comment. a=ccoroiu r=bustage-fix-bustage |rmaries@mozilla.com|bustage-fix-bustage|2019-02-10 16:41:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=674fa918ee39)|Merge mozilla-central to mozilla-inbound. a=merge on a CLOSED TREE|nerli@mozilla.com|merge|2019-02-10 23:41:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=be6554246c50)|Bug 1520705 - Enable mochitest-chrome on WebRender r=kats  Enable mochitest-chrome, but skip test_bug331215.xul and test_bug304188.xul because of frequent intermittent failures on WebRener. The intermittent failures already exist and the failure seems not directly related to WebRender implementation.  Differential Revision: https://phabricator.services.mozilla.com/D19115|sikeda@mozilla.com|kats|2019-02-11 03:35:07|

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
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cdcbd5b13210)|Bug 1525760 - Add a clang-based base toolchains task. r=froydnj  These are copies of the corresponding gcc-based base toolchain tasks, with FORCE_GCC and the gcc dependency removed.  We also tweak things a little for those builds to actually end up green.  Differential Revision: https://phabricator.services.mozilla.com/D18903|rmaries@mozilla.com|froydnj|2019-02-10 11:41:47|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d6a025216838)|Bug 1394825 - Update minimum clang version to 4.0. r=glandium  libclang 3.9 has a bug that makes bindgen unable to distinguish some typedefs from the underlying type, which matters for bug 1523071.  We have had quite a few workarounds for this bug and I don't really want to add more, since in this case it is non-trivial. I think requiring libclang 4.0+ is reasonable at this point.  Of the distros that can't build Firefox out of the box with clang, dropping support for clang 3.9 would only break Ubuntu 14.04 LTS, which support ends April 2019, right before we release 67.  Differential Revision: https://phabricator.services.mozilla.com/D18889|rmaries@mozilla.com|glandium|2019-02-10 11:41:47|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=be2938cc03f3)|Bug 1523071 - Update cbindgen. r=glandium,jwatt  Gonna need it to use https://github.com/eqrion/cbindgen/pull/275.  Differential Revision: https://phabricator.services.mozilla.com/D17736 |rmaries@mozilla.com|glandium,jwatt|2019-02-10 11:41:47|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1b147d9934f1)|Bug 1525760 - Disable base-toolchains-clang jobs for now. a=ccoroiu r=bustage  For failing in ways I cannot reason about.  It hits linker errors sometimes, and in two revisions without any single source code change between them it's green:    https://treeherder.mozilla.org/#/jobs?repo=mozilla-central&revision=952b928f1605ad5676ae4ccfd41612b34523bae5  And red:    https://treeherder.mozilla.org/#/jobs?repo=autoland&revision=952b928f1605ad5676ae4ccfd41612b34523bae5  At the same time. Which is quite baffling.  Disable the new jobs on CI for now in order to avoid backing out the whole stack of dependent patches (bug 1394825, bug 1523071 and bug 1523140) that landed afterwards. |emilio@crisal.io|bustage|2019-02-10 15:21:33|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=50309e384ceb)|Bug 1525760 - followup: Make linters happy about a comment. a=ccoroiu r=bustage-fix-bustage |emilio@crisal.io|bustage-fix-bustage|2019-02-10 15:34:03|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=674fa918ee39)|Merge mozilla-central to mozilla-inbound. a=merge on a CLOSED TREE|nerli@mozilla.com|merge|2019-02-10 23:38:44|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=cdcbd5b13210)|Bug 1525760 - Add a clang-based base toolchains task. r=froydnj  These are copies of the corresponding gcc-based base toolchain tasks, with FORCE_GCC and the gcc dependency removed.  We also tweak things a little for those builds to actually end up green.  Differential Revision: https://phabricator.services.mozilla.com/D18903|rmaries@mozilla.com|froydnj|2019-02-10 11:51:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d6a025216838)|Bug 1394825 - Update minimum clang version to 4.0. r=glandium  libclang 3.9 has a bug that makes bindgen unable to distinguish some typedefs from the underlying type, which matters for bug 1523071.  We have had quite a few workarounds for this bug and I don't really want to add more, since in this case it is non-trivial. I think requiring libclang 4.0+ is reasonable at this point.  Of the distros that can't build Firefox out of the box with clang, dropping support for clang 3.9 would only break Ubuntu 14.04 LTS, which support ends April 2019, right before we release 67.  Differential Revision: https://phabricator.services.mozilla.com/D18889|rmaries@mozilla.com|glandium|2019-02-10 11:51:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=be2938cc03f3)|Bug 1523071 - Update cbindgen. r=glandium,jwatt  Gonna need it to use https://github.com/eqrion/cbindgen/pull/275.  Differential Revision: https://phabricator.services.mozilla.com/D17736 |rmaries@mozilla.com|glandium,jwatt|2019-02-10 11:51:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=674fa918ee39)|Merge mozilla-central to mozilla-inbound. a=merge on a CLOSED TREE|rmaries@mozilla.com|merge|2019-02-10 11:51:32|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=1b147d9934f1)|Bug 1525760 - Disable base-toolchains-clang jobs for now. a=ccoroiu r=bustage  For failing in ways I cannot reason about.  It hits linker errors sometimes, and in two revisions without any single source code change between them it's green:    https://treeherder.mozilla.org/#/jobs?repo=mozilla-central&revision=952b928f1605ad5676ae4ccfd41612b34523bae5  And red:    https://treeherder.mozilla.org/#/jobs?repo=autoland&revision=952b928f1605ad5676ae4ccfd41612b34523bae5  At the same time. Which is quite baffling.  Disable the new jobs on CI for now in order to avoid backing out the whole stack of dependent patches (bug 1394825, bug 1523071 and bug 1523140) that landed afterwards. |rmaries@mozilla.com|bustage|2019-02-10 16:43:25|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=50309e384ceb)|Bug 1525760 - followup: Make linters happy about a comment. a=ccoroiu r=bustage-fix-bustage |rmaries@mozilla.com|bustage-fix-bustage|2019-02-10 16:43:25|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/68c9b94fa94bdf197664520767572f5a40e1eed8)|Merge pull request #205 from taskcluster/renovate/got-9.x  Update dependency got to v9|djmitche|N/A|2019-02-11 03:13:48|
|[Link](https://github.com/taskcluster/taskcluster/commit/e07c158dd1084ebe3c5b04f7a76a6fdb9ac40215)|Update dependency got to v9|renovate-bot|N/A|2019-02-11 03:11:45|
|[Link](https://github.com/taskcluster/taskcluster/commit/1ec65c9abdde8d03ae869036f6a73e812bd49cdb)|Merge pull request #206 from taskcluster/renovate/tar-fs-2.x  Update dependency tar-fs to v2|djmitche|N/A|2019-02-11 03:10:21|
|[Link](https://github.com/taskcluster/taskcluster/commit/1c6663518f0ec697b52f6fba03c0c0b26519adaa)|Update dependency tar-fs to v2|renovate-bot|N/A|2019-02-11 02:49:22|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
