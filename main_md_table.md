##  Commits in production - for one day, generated on: 2019-02-08 09:33:27 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e8dc8aa65fbb)|Bug 1525731 - Cleanup taskcluster config for Android tests; r=me,a=test-only  Removing skipped test suites that we have no immediate plans to run, and adding comments and bug pointers for remaining skipped suites.|rmaries@mozilla.com|me,a=test-only|2019-02-07 23:50:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3c7c50fba283)|Bug 1515746 - [flake8] Upgrade flake8 and dependencies, r=egao  This bumps flake8 to version 3.7.5.  This also ignores the new lint rules that were added in the new versions. These rules are de-marked via comment so we know that they should be enabled at some point (as opposed to the other rules that are (presumably) ignored intentionally.  Differential Revision: https://phabricator.services.mozilla.com/D18353|ahalberstadt@mozilla.com|egao|2019-02-08 04:46:38|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f96c1460ffc0)|Bug 1515746 - [flake8] Unsupport subdir .flake8 files and use new 'per-file-ignores' config instead, r=egao  This removes all .flake8 files except for the one at the root of the repo. Instead we use the new 'per-file-ignores' config introduced in 3.7. To ignore specific errors in a subdirectory, add a line like this to the root .flake8:  [per-file-ignores]     path/to/subdir/*: E100, F200, ...  The reasons for this change are:  1. Unblock flake8 blacklist (bug 1367092). 2. Simplify configuration and code. 3. Encourage more consistent styling. 4. Improve performance. 5. Greater editor consistency.  Differential Revision: https://phabricator.services.mozilla.com/D18354|ahalberstadt@mozilla.com|egao|2019-02-08 04:46:38|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0b8097689bb5)|Bug 1519472 - [taskgraph] Factor logic for adding a cache in job.common to a new function, r=tomprince  We add caches at various places in common.py. This consolidates the logic into a re-useable function. This is in preparation for adding generic-worker cache support.  This also adds a test. The test is not terribly useful, but I've been looking for an excuse to lay some groundwork for further tests in the 'job' submodule. This will do.  Differential Revision: https://phabricator.services.mozilla.com/D17689|ahalberstadt@mozilla.com|tomprince|2019-02-08 04:48:10|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b6e19a5b0ab9)|Bug 1519472 - [ci] Opt out of caching for generic-worker based Windows builds, r=tomprince  The hosts don't have enough disk space to cache mozilla-central.  Depends on D17689  Differential Revision: https://phabricator.services.mozilla.com/D18738|ahalberstadt@mozilla.com|tomprince|2019-02-08 04:48:10|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2ceeee1915ae)|Bug 1519472 - [taskgraph] Support generic-worker caches in run_task, r=tomprince  This implements support for adding generic-worker caches. As a consequence this also turns on caching for the gecko checkout if present.  Differential Revision: https://phabricator.services.mozilla.com/D17690|ahalberstadt@mozilla.com|tomprince|2019-02-08 04:48:10|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0e6997e8f365)|Bug 1525987: [taskgraph] Allow docker images to not be cached; r=dustin  This allows images to be built on every commit. This is useful for the out-of-tree taskgraph, that builds a docker image with the taskgraph code installed.  Differential Revision: https://phabricator.services.mozilla.com/D19031|mozilla@hocat.ca|dustin|2019-02-08 04:50:35|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0b0101621dcf)|Bug 1525987: [taskgraph] Allow docker images to be indexed as build products; r=dustin  This is useful for the out-of-tree taskgraph code. Downstream products can pin the generated decision task image by revision, rather than contents.  Differential Revision: https://phabricator.services.mozilla.com/D19032|mozilla@hocat.ca|dustin|2019-02-08 04:50:35|

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
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7d289fe21aec)|Bug 1525421 - parse out just the try syntax from the commit message r=tomprince  This mirrors what mozilla-taskcluster does in https://github.com/taskcluster/mozilla-taskcluster/blob/cb3de4c31e418f7dc1d89cffeeb28ad6a9dae610/src/jobs/taskcluster_graph.js#L46-L58  Differential Revision: https://phabricator.services.mozilla.com/D18748|opoprus@mozilla.com|tomprince|2019-02-07 11:46:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e8dc8aa65fbb)|Bug 1525731 - Cleanup taskcluster config for Android tests; r=me,a=test-only  Removing skipped test suites that we have no immediate plans to run, and adding comments and bug pointers for remaining skipped suites.|rmaries@mozilla.com|me,a=test-only|2019-02-07 23:44:23|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7d289fe21aec)|Bug 1525421 - parse out just the try syntax from the commit message r=tomprince  This mirrors what mozilla-taskcluster does in https://github.com/taskcluster/mozilla-taskcluster/blob/cb3de4c31e418f7dc1d89cffeeb28ad6a9dae610/src/jobs/taskcluster_graph.js#L46-L58  Differential Revision: https://phabricator.services.mozilla.com/D18748|opoprus@mozilla.com|tomprince|2019-02-07 11:58:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e8dc8aa65fbb)|Bug 1525731 - Cleanup taskcluster config for Android tests; r=me,a=test-only  Removing skipped test suites that we have no immediate plans to run, and adding comments and bug pointers for remaining skipped suites.|gbrown@mozilla.com|me,a=test-only|2019-02-07 18:32:50|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6df68ae82295)|Bug 1523562 [wpt PR 14981] - Use fluxbox as window manager for xvfb in CI (14938), a=testonly  Automatic update from web-platform-tests Use fluxbox as window manager for xvfb in CI (#14981)  --  wpt-commits: 8b4c3d8215517554199d7f35f686be12e69473d5 wpt-pr: 14981 |james@hoppipolla.co.uk|testonly|2019-02-08 00:12:57|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=48e765f7795c)|Bug 1523562 [wpt PR 15073] - Add a retry to the initial git checkout, a=testonly  Automatic update from web-platform-tests Add a retry to the initial git checkout  -- Update docker image  --  wpt-commits: aa94ec995bdf6de55dca6dc51fc83dc0a66c31e9, 68f47dfce55536c861d4e28220de4d296a5472c7 wpt-pr: 15073 |james@hoppipolla.co.uk|testonly|2019-02-08 00:12:57|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c55f99389f89)|Bug 1523562 [wpt PR 15074] - Enable full logging for verify runs on taskcluster, a=testonly  Automatic update from web-platform-tests Enable full logging for verify runs on taskcluster  --  wpt-commits: c456b7df5d0978d1036399dbb50cdcbc2517c825 wpt-pr: 15074 |james@hoppipolla.co.uk|testonly|2019-02-08 00:12:57|

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
|[Link](https://github.com/mozilla/release-services/commit/334bfb59a9cb55a92022f600bee1e4ed41dc485f)|tooltool/api: fix all flask subcommands|rail|N/A|2019-02-07 20:21:33|
|[Link](https://github.com/mozilla/release-services/commit/60bc6fbdf7dcee8afa20d3e5ae7193a1d0e95873)|setup: fixing update hooks due to intreehooks needed as setup require (#1854)|garbas|N/A|2019-02-07 19:35:50|
|[Link](https://github.com/mozilla/release-services/commit/ccf864e32ddf8b462450082d1859b2bb5d93d1d7)|tooltool/api: remove redundant workerType specification (#1855)|garbas|N/A|2019-02-07 17:09:07|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/150b40d50c35f9e05685fe72a7ce1774bb173acb)|Merge pull request #191 from djmitche/fix-built-in-workers-startup  Bug 1522307 - fix startup of built-in-workers|djmitche|N/A|2019-02-07 23:19:40|
|[Link](https://github.com/taskcluster/taskcluster/commit/faf54692367a4eda3934ce95b4bbbad258c9efd6)|Bug 1522307 - fix startup of built-in-workers|djmitche|N/A|2019-02-07 21:28:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/79ee65e91d30f813285c8425a906a56368b3ba0e)|Merge pull request #189 from djmitche/bug1523807  Bug 1523807 - bring tc-client-web into the monorepo|djmitche|N/A|2019-02-07 16:26:51|
|[Link](https://github.com/taskcluster/taskcluster/commit/0f16280bf569ae5757cc940830a99bb4bc93baec)|Update README (#190)|helfi92|N/A|2019-02-07 16:06:10|
|[Link](https://github.com/taskcluster/taskcluster/commit/5a88bd8fa50883aefa3ab19dcee7f5f0c0a1b17c)|Bug 1523807 - include subdirectory in the repository links for clients|djmitche|N/A|2019-02-07 14:16:48|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
