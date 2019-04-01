##  Commits in production - for 3 days, generated on: 2019-04-01 19:56:05 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5a85cf971fef)|Backed out changeset a7c0f3da75fa for linting opt failure in desktop_l10n.py CLOSED TREE|nerli@mozilla.com||2019-04-01 21:20:31|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a7c0f3da75fa)|No bug: [mozharness] Remove some dead code looking at substitutions in desktop l10n code; r=Callek There used to be various values that were substituted into the mozharness configuration for L10n jobs. All those substitutions have been removed, but the code to support them is still around. This removes that code. Differential Revision: https://phabricator.services.mozilla.com/D25143|mozilla@hocat.ca|Callek|2019-04-01 21:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=65bcb804a3e6)|Backed out changeset 1ccb52b0784e [Bug 1532560](https://bugzilla.mozilla.org/show_bug.cgi?id=1532560)  for causing Gecko Decision Task bustage CLOSED TREE|aiakab@mozilla.com||2019-04-01 20:57:13|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1ccb52b0784e)|Fix [Bug 1532560](https://bugzilla.mozilla.org/show_bug.cgi?id=1532560)  Only run raptor-tp6-3 tests on AARM64 in try r=jmaher,rwood,gbrown Differential Revision: https://phabricator.services.mozilla.com/D23193|sdonner@mozilla.com|jmaher,rwood,gbrown|2019-04-01 20:49:34|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=508dd8a22136)|No bug: [taskgraph] Remove unused code for varying build-tools repo to use; r=aki We don't actually use the build-tools repo in-tree anymore, so remove the support code for it. Differential Revision: https://phabricator.services.mozilla.com/D25631|mozilla@hocat.ca|aki|2019-04-01 20:46:46|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d067e0360843)|[Bug 1530493](https://bugzilla.mozilla.org/show_bug.cgi?id=1530493)  - Bump mingw-w64 version r=froydnj This is needed to bring dispatcherqueue.h in, which is needed for an ANGLE upgrade. It also ensures that overloads for secure string functions are always defined and removes redundant --enable-secure-api configure option and use of MINGW_HAS_SECURE_API Differential Revision: https://phabricator.services.mozilla.com/D25294|csabou@mozilla.com|froydnj|2019-03-30 09:03:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=08a3525d99d2)|[Bug 1536308](https://bugzilla.mozilla.org/show_bug.cgi?id=1536308)  - Apply a local patch to MinGW to get the needed winrt stuff for ANGLE r=froydnj We apply a local patch while we wait for upstream wine and mingw to review the changes to widl that are necessary to generate the correct headers. Here we just grab the generated headers and patch them into MinGW We can revert this when MinGW updates, but for now we would like to unblock the ANGLE update Depends on D25294 Differential Revision: https://phabricator.services.mozilla.com/D25295|csabou@mozilla.com|froydnj|2019-03-30 09:03:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b9654a90f60a)|[Bug 1535364](https://bugzilla.mozilla.org/show_bug.cgi?id=1535364)  - Enable PGO for Android nightly builds; r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D23532|cmanchester@mozilla.com|tomprince|2019-03-30 04:12:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=825e93bb4b13)|Backed out 3 changesets [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  [Bug 1539779](https://bugzilla.mozilla.org/show_bug.cgi?id=1539779)  [Bug 1536790](https://bugzilla.mozilla.org/show_bug.cgi?id=1536790)  for causing clang-tidy bustages CLOSED TREE Backed out changeset 7d058f3174e5 [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  Backed out changeset 8839622122ed [Bug 1539779](https://bugzilla.mozilla.org/show_bug.cgi?id=1539779)  Backed out changeset 9eb7867c1dd4 [Bug 1536790](https://bugzilla.mozilla.org/show_bug.cgi?id=1536790) |aciure@mozilla.com||2019-03-30 01:53:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=211b1706b5f1)|Backed out changeset dc3b81670b01 [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  for causing clang-tidy bustages CLOSED TREE|aciure@mozilla.com||2019-03-30 00:37:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=04bd7929b499)|Backed out changeset 963d97e812f9 [Bug 1535364](https://bugzilla.mozilla.org/show_bug.cgi?id=1535364)  for causing [Bug 1539933](https://bugzilla.mozilla.org/show_bug.cgi?id=1539933)  a=backout|opoprus@mozilla.com|backout|2019-03-30 00:07:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=69e9ee0ef3dd)|[Bug 1540132](https://bugzilla.mozilla.org/show_bug.cgi?id=1540132)  - Fix updates by telling release properties to ignore the '-shippable' suffix. r=tomprince a=ccoroiu Reviewers: tomprince Reviewed By: tomprince Bug #: 1540132 Differential Revision: https://phabricator.services.mozilla.com/D25397|opoprus@mozilla.com|tomprince|2019-03-30 00:07:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=dc3b81670b01)|[Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  - Update non-Windows builds to clang 8. r=froydnj Windows builds have been taken care of in [Bug 1535441](https://bugzilla.mozilla.org/show_bug.cgi?id=1535441)  Differential Revision: https://phabricator.services.mozilla.com/D25328|mh@glandium.org|froydnj|2019-03-29 23:39:37|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6c34f19750b8)|[Bug 1540210](https://bugzilla.mozilla.org/show_bug.cgi?id=1540210)  - Correct Android 4.3 pgo test's default tier to tier 1; r=Callek Differential Revision: https://phabricator.services.mozilla.com/D25459|gbrown@mozilla.com|Callek|2019-03-29 22:05:01|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b04716962902)|[Bug 1531412](https://bugzilla.mozilla.org/show_bug.cgi?id=1531412)  [wpt PR 14859] - Use the checks API with taskcluster jobs, a=testonly Automatic update from web-platform-tests Use the checks API with taskcluster jobs (#14859) -- wpt-commits: a9f087c1dc0bec1f322339926f7056d0ac47cd0b wpt-pr: 14859|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=bbf41de09c57)|[Bug 1531440](https://bugzilla.mozilla.org/show_bug.cgi?id=1531440)  [wpt PR 15576] - Revert "Use the checks API with taskcluster jobs (#14859)", a=testonly Automatic update from web-platform-tests Revert "Use the checks API with taskcluster jobs (#14859)" (#15576) There are no wpt.fyi checks on https://github.com/web-platform-tests/wpt/pull/15575. This reverts commit a9f087c1dc0bec1f322339926f7056d0ac47cd0b. -- wpt-commits: 112d3dc9f100deec62266c2a9c6dff74a799919f wpt-pr: 15576|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=92a12a4be4f6)|[Bug 1531903](https://bugzilla.mozilla.org/show_bug.cgi?id=1531903)  [wpt PR 15574] - Move the lint from Travis to TaskCluster, a=testonly Automatic update from web-platform-tests Move the lint from Travis to TaskCluster (#15574) -- wpt-commits: 218466a7883ab2130645e896bcd379f430eae1fd wpt-pr: 15574|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f32cbf1d56a5)|[Bug 1531905](https://bugzilla.mozilla.org/show_bug.cgi?id=1531905)  [wpt PR 15594] - Revert "Move the lint from Travis to TaskCluster", a=testonly Automatic update from web-platform-tests Revert "Move the lint from Travis to TaskCluster (#15574)" (#15594) This reverts commit 218466a7883ab2130645e896bcd379f430eae1fd. -- wpt-commits: 3353bc3aef96c7bccd4994685e63f4f3e35c12b7 wpt-pr: 15594|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=91d153fb4421)|[Bug 1531952](https://bugzilla.mozilla.org/show_bug.cgi?id=1531952)  [wpt PR 15601] - Move the lint from Travis to TaskCluster (#15574), a=testonly Automatic update from web-platform-tests Move the lint from Travis to TaskCluster (#15574) (#15601) -- wpt-commits: 04ad8dd6a1f6f5577841e4e7ccbe948892bd6ddf wpt-pr: 15601|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e593a0f11228)|[Bug 1531957](https://bugzilla.mozilla.org/show_bug.cgi?id=1531957)  [wpt PR 15593] - Add support for verifying taskcluster config, a=testonly Automatic update from web-platform-tests Add support for verifying taskcluster config (#15593) Adds as wpt tc-verify command that verifies that the TaskCluster config is a valid yaml file and computes the tasks that will run on a PR synchronize event. This can be expanded to more events and pushes in the future. -- wpt-commits: 5baef702c26b8580f5a4e5e1a34ac75bb9d496ae wpt-pr: 15593|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=818e7d359c5b)|[Bug 1531960](https://bugzilla.mozilla.org/show_bug.cgi?id=1531960)  [wpt PR 15619] - Fix taskcluster for master., a=testonly Automatic update from web-platform-tests Fix taskcluster for master. (#15619) A couple more properties we were accessing only made sense for pull request events -- wpt-commits: 21cc43a848a2d82cf351f029a0f4b91702e4c42a wpt-pr: 15619|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=70349e41deef)|[Bug 1536142](https://bugzilla.mozilla.org/show_bug.cgi?id=1536142)  [wpt PR 15771] - Send screenshots from Taskcluster to wpt.fyi, a=testonly Automatic update from web-platform-tests Send screenshots from Taskcluster to wpt.fyi Store screenshots on TC as wpt_screenshot.txt.gz and the wpt.fyi webhook will fetch it. -- wpt-commits: 25c26f30f3b29ecb742f4a562dad4914df332c5e wpt-pr: 15771|james@hoppipolla.co.uk|testonly|2019-04-01 17:00:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4338bf79beb2)|[Bug 1312823](https://bugzilla.mozilla.org/show_bug.cgi?id=1312823)  - Run console mocha tests on TRY. r=jdescottes. Differential Revision: https://phabricator.services.mozilla.com/D25045|opoprus@mozilla.com|jdescottes.|2019-04-01 13:04:43|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4338bf79beb2)|[Bug 1312823](https://bugzilla.mozilla.org/show_bug.cgi?id=1312823)  - Run console mocha tests on TRY. r=jdescottes. Differential Revision: https://phabricator.services.mozilla.com/D25045|opoprus@mozilla.com|jdescottes.|2019-04-01 12:46:51|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/57eef35d5ec9958120cd9651f5ec2c16bd5afbbd)|Merge pull request #517 from taskcluster/renovate/cron-parser-2.x  Update dependency cron-parser to v2.10.0|djmitche|N/A|2019-04-01 17:50:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/9d67dbbbcd46cc8d2e81eb333e690554b2efd280)|Merge pull request #502 from djmitche/bug1538961  Bug 1538961 - improve subscriptions support|djmitche|N/A|2019-04-01 17:08:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/85c603e28bbbbbc72f88e9a8f0d55a3766349cb6)|Merge pull request #514 from taskcluster/procs-yml-support  Procs yml support|imbstack|N/A|2019-04-01 17:07:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/718477370a239c9e9eac04ffbdf332cb91dad3da)|Merge pull request #518 from taskcluster/renovate/eslint-5.x  Update dependency eslint to v5.16.0|djmitche|N/A|2019-04-01 16:45:45|
|[Link](https://github.com/taskcluster/taskcluster/commit/3043d48df8f65fb7dd9652531ad917f0d2581607)|Bug 1538961 - PulseIterator: create pull promise in next method|djmitche|N/A|2019-04-01 16:40:46|
|[Link](https://github.com/taskcluster/taskcluster/commit/cf575738372ea70eda1d40a9a43c84faf132b757)|Bug 1538961 - set this.consumerTag in Subscription constructor|djmitche|N/A|2019-04-01 16:38:16|
|[Link](https://github.com/taskcluster/taskcluster/commit/9b37b8e37eaa079635a0ec6a83227630b131efd5)|Merge pull request #523 from djmitche/bug1540699  Bug 1540699 - fix calls to monitor.log.task |djmitche|N/A|2019-04-01 16:33:54|
|[Link](https://github.com/taskcluster/taskcluster/commit/b5d4ff0f16b5f2e955b0dda5cb0ddd977d9a251a)|Bug 1540699 - fix calls to monitor.log.task   And add tests for them.|djmitche|N/A|2019-04-01 14:20:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/4115a11b1e596e4edf5941344e55d25bb4e446a5)|Use MarkdownTextArea from @mozilla-frontend-infra/components (#521)|helfi92|N/A|2019-04-01 13:42:39|
|[Link](https://github.com/taskcluster/taskcluster/commit/e8f66b0809fd8c2034396788aeb9f1f22cb50113)|Update CODE_OF_CONDUCT.md|ccooper|N/A|2019-04-01 13:00:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/1122529f9c3dcfeb4fe9bbac8650b0bd1ba83619)|[UI] Treat task with status exception as failed (favicon) (#520)|helfi92|N/A|2019-04-01 11:57:35|

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)|FIC - BOT|Self Generated| - |

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)|FIC - BOT|Self Generated| - |

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)|FIC - BOT|Self Generated| - |

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)|FIC - BOT|Self Generated| - |

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)|FIC - BOT|Self Generated| - |

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)|FIC - BOT|Self Generated| - |

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)|FIC - BOT|Self Generated| - |

|	signingscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)|FIC - BOT|Self Generated| - |

|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)|FIC - BOT|Self Generated| - |

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |

|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla/release-services/commit/34cd93d06230f2ed0ac32fb5fd69f66c211c13c0)|treestatus/api: Dependencies update. (#2003)|garbas|N/A|2019-04-01 10:15:28|
|[Link](https://github.com/mozilla/release-services/commit/c6d9fa98407a93dab13b673efee1f15535efcd44)|tokens/api: Dependencies update. (#2001)|garbas|N/A|2019-04-01 09:56:08|

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)|FIC - BOT|Self Generated| - |

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
