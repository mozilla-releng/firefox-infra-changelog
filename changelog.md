##  Commits in production - for one day, generated on: 2019-03-08 02:49:49 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3fd4a7b0872e)|[Bug 1533445 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533445) - Make android tests shutdown faster when device unresponsive; r=bc Differential Revision: https://phabricator.services.mozilla.com/D22610|gbrown@mozilla.com|bc|2019-03-08 04:05:01|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ea4a69b40a66)|[Bug 1533565 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533565) - Increase max-run-time for osx ccov builds; r=marco Differential Revision: https://phabricator.services.mozilla.com/D22615|gbrown@mozilla.com|marco|2019-03-08 04:03:43|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3dc5de51e631)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Move Raptor chrome task definitions to separate file. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D21371|gmierz2@outlook.com|glandium|2019-03-08 04:02:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=225dab563b6d)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Add fetch tasks for raptor chromium builds. r=rwood,glandium,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21372|gmierz2@outlook.com|rwood,glandium,tomprince|2019-03-08 04:02:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d91c333553e4)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Add missing configuration for nasm on hazard and plain builds. r=dmajor Differential Revision: https://phabricator.services.mozilla.com/D22451|mh@glandium.org|dmajor|2019-03-08 00:31:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=707ec85ae54c)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Remove nasm Debian packages. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22257|mh@glandium.org|dustin|2019-03-08 00:31:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6c77b4a7cbd3)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Derive the diffoscope docker image from debian9-base. r=dustin Because the debian9-base apt configuration doesn't install recommended packages, we end up needing to install more packages than before. We could pass --install-recommended to apt-get, but that would make the image larger than it already was after the upcoming changes, because new versions of diffoscope come with more recommended dependencies. The side effect is that this makes the image much smaller than it used to be, while preserving all the useful recommended packages (we don't actually need all of them). Differential Revision: https://phabricator.services.mozilla.com/D22262|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b1e1e1bba900)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Unbreak mach-o diffs after [Bug 1513798 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1513798) r=dustin Depends on D22262 Differential Revision: https://phabricator.services.mozilla.com/D22455|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=88e8b3f52329)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Ensure the base Debian docker image is up-to-date wrt the snapshot used. r=dustin When the apt snapshot is more recent than the docker image on the docker hub, some packages may not be up-to-date. Depends on D22455 Differential Revision: https://phabricator.services.mozilla.com/D22263|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ed46ddfa23b7)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Update to a more recent snapshot for Debian stretch-based docker images. r=dustin This has the side effect of addressing [Bug 1524723 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1524723) for those images. Depends on D22263 Differential Revision: https://phabricator.services.mozilla.com/D22264|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4a6cb39329d1)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Install diffoscope from stretch-backports. r=dustin As of the update snapshot, stretch-backports contains version 112. Depends on D22264 Differential Revision: https://phabricator.services.mozilla.com/D22265|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8e48fdd65475)|No bug - build cbindgen for macos using rust 1.32. r=froydnj 1.32 includes https://github.com/rust-lang/rust/pull/49219, which means new cbindgen no longer depends on compiler internals, which fixes some reported build issues on IRC.|aiakab@mozilla.com|froydnj|2019-03-08 00:14:58|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=0c5a6ccbd8b9)|[Bug 1526979 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526979) - enable hg-hooks for inbound, autoland|dmitchell@mozilla.com||2019-03-07 17:47:30|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8e48fdd65475)|No bug - build cbindgen for macos using rust 1.32. r=froydnj 1.32 includes https://github.com/rust-lang/rust/pull/49219, which means new cbindgen no longer depends on compiler internals, which fixes some reported build issues on IRC.|aiakab@mozilla.com|froydnj|2019-03-07 23:58:58|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8e48fdd65475)|No bug - build cbindgen for macos using rust 1.32. r=froydnj 1.32 includes https://github.com/rust-lang/rust/pull/49219, which means new cbindgen no longer depends on compiler internals, which fixes some reported build issues on IRC.|emilio@crisal.io|froydnj|2019-03-07 17:03:21|

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
|[Link](https://github.com/mozilla/release-services/commit/688dd403d87226a42ac26b9fbec5e7111e198c00)|backend_common/auth: we shouldn't touch permissions in decorator (#1929)|garbas|N/A|2019-03-07 11:36:09|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/0f81a6e4345ec7e13667dc15cc138b580ae0400a)|Merge pull request #364 from ydidwania/bug-1523801  [Bug 1523801] Blacklist listening to some specific exchanges|djmitche|N/A|2019-03-07 23:00:34|
|[Link](https://github.com/taskcluster/taskcluster/commit/dcd2e2c8c46dfe1934a69496629b4314b5d5d6cf)|refactor: rename denyList to denylist. simplify format of denylsit in config.yml|ydidwania|N/A|2019-03-07 21:06:56|
|[Link](https://github.com/taskcluster/taskcluster/commit/b5c6d9d5940f0ed1cbaa7fa76142c7c32633f76d)|Merge pull request #368 from djmitche/bug1531753  Bug 1531753 - no more events, gce-provider, and delete lots of builder junk|djmitche|N/A|2019-03-07 17:45:20|
|[Link](https://github.com/taskcluster/taskcluster/commit/9676ea1aee9c300a7a21f6c353e27f3d54330c01)|Merge pull request #346 from taskcluster/renovate/node-10.x  Update Node.js to v10.15.2|imbstack|N/A|2019-03-07 17:24:13|
|[Link](https://github.com/taskcluster/taskcluster/commit/3473af1789a0e2dd1b77d3bb2dbf4999a0876bb5)|Bug 1531753 - remove tc-builder as a workspace|djmitche|N/A|2019-03-07 17:08:44|
|[Link](https://github.com/taskcluster/taskcluster/commit/42aa36042114cec715e48538f13cba982a496091)|Bug 1531753 - simply write out the monoimage docker image|djmitche|N/A|2019-03-07 16:59:27|
|[Link](https://github.com/taskcluster/taskcluster/commit/c543eca6f8b54bc557ab9d551e849764330bb0a2)|Bug 1531753 - run 'yarn build --dry-run' in CI  ..since what few tests there were are now gone|djmitche|N/A|2019-03-07 16:57:25|
|[Link](https://github.com/taskcluster/taskcluster/commit/d1fe8291b586fbe8dd7b124b7f15af6b52c0903c)|Bug 1531753 - remove use of ClusterSpec|djmitche|N/A|2019-03-07 16:52:28|
|[Link](https://github.com/taskcluster/taskcluster/commit/cfc2dd90704324a9c20d18d1c8167d0d5678cc6d)|Bug 1531753 - remove --target-service since there is only one image now|djmitche|N/A|2019-03-07 16:44:12|
|[Link](https://github.com/taskcluster/taskcluster/commit/16745c476570fe45d42ef1b7e341b37dae82726d)|Bug 1531753 - stop building or deploying the events service|djmitche|N/A|2019-03-07 16:41:04|
|[Link](https://github.com/taskcluster/taskcluster/commit/03f47d52c7db9cb662b8a5805f75b4f1df4d8758)|Bug 1532666 - stop building, deploying gce-provider|djmitche|N/A|2019-03-07 16:39:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/60d08da601b6d4ad1f7ee59f00b63da638bc8244)|Merge pull request #199 from arshadkazmi42/tc-v1-yml-quick  Bug 1515673 - YML changed for v1 in QuickStart|owlishDeveloper|N/A|2019-03-07 03:38:04|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
