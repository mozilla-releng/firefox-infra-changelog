###  Last commits from every repository
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[autoland](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.md)|Bug 1503760: Changed browser.downloads.search({}) to return 0 byte downloads. r=aswan  Updated the totalBytesGreater property in browser.downloads.search({}) to default to -1 so files with a byte size of 0 will be returned.  Differential Revision: https://phabricator.services.mozilla.com/D12344|2018-11-26 22:54:49|
|[beta](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.md)|Bug 1508494: Update WNP with locales for 64; r=flod a=whats-new  Differential Revision: https://phabricator.services.mozilla.com/D13555|2018-12-01 06:00:21|
|[braindump](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.md)|add some partials to the unsigned mars params|2018-11-16 03:03:39|
|[ci-admin](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|Bug 1492665 - add modify_resources support r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6933|2018-10-22 17:52:14|
|[ci-configuration](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)|Bug 1510441: Use sparse profile in cron tasks; r=gps  Differential Revision: https://phabricator.services.mozilla.com/D13141|2018-11-30 13:01:34|
|[comm-esr60](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/comm-esr60.md)|Automatic version bump CLOSED TREE NO BUG a=release|2018-11-29 23:29:47|
|[inbound](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/inbound.md)|Merge mozilla-central to mozilla-inbound.  a=merge CLOSED TREE|2018-12-02 11:56:11|
|[mozilla-build](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-build.md)|Bug 1501406 - Update vswhere to version 2.5.2.|2018-10-23 19:12:46|
|[mozilla-central](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)|Backed out 2 changesets (bug 1501992) for browser_trackingUI_state.js perma fails a=backout  Backed out changeset 6cb8a465440a (bug 1501992) Backed out changeset b54b117c15e9 (bug 1501992)|2018-12-02 11:53:33|
|[mozilla-esr60](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-esr60.md)|Bug 1351940 - [marionette] Only convert a valid outerWindowID to a string. r=ato, a=test-only  Differential Revision: https://phabricator.services.mozilla.com/D13206|2018-11-28 20:48:42|
|[mozilla-release](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|Bug 1510441: Add `.cron.yml` to the taskgraph sparse profile; r=gps a=tomprince DONTBUILD  Differential Revision: https://phabricator.services.mozilla.com/D13142|2018-11-30 00:26:19|
|[try](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/try.md)|Fuzzy query=analysis  Pushed via `mach try fuzzy`|2018-12-02 17:50:30|
|[addonscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/addonscript.md)|Merge pull request #51 from Callek/one_dot_oh  Bump to 1.0 and align setup.py requirements with requirements.txt.in|2018-05-17 13:58:03|
|[balrogscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/balrogscript.md)|3.3.0|2018-11-26 17:29:44|
|[beetmoverscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)|8.0.0|2018-11-28 01:08:55|
|[bouncerscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)|Merge pull request #46 from Callek/3.3.0  Bump to 3.3.0 for MSI installer|2018-11-12 16:20:14|
|[build-cloud-tools](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)|Merge branch 'La0-buildhub'|2018-11-29 02:03:48|
|[build-puppet](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-puppet.md)|Bug 1511145: don't handle Firefox in releaserunner3 (#316)  Using fake values in case we don't hablde empty arrays properly|2018-11-30 17:10:54|
|[mozapkpublisher](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|0.9.2|2018-11-08 09:57:02|
|[OpenCloudConfig](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|Bug 1485628 - disable service pack updates & reboots  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:27:08|
|[pushapkscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|0.9.0|2018-11-23 14:54:01|
|[pushsnapscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)|0.2.4|2018-10-05 13:09:12|
|[scriptworker](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/scriptworker.md)|17.0.0|2018-11-27 17:46:52|
|[services](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/services.md)|staticanalysis/bot: Filter clang-format publishable issues by their path. (#1689)|2018-11-20 15:36:16|
|[ship-it](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/ship-it.md)|Add comment about syncing v1 and v2 configs (#246)|2018-11-30 19:20:47|
|[shipitscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/shipitscript.md)|Add support for Ship-it v2 (#14)|2018-11-21 16:33:53|
|[signingscript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signingscript.md)|9.5.1|2018-11-23 12:48:01|
|[signtool](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signtool.md)|3.2.1|2018-08-27 17:17:03|
|[taskcluster-auth](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.md)|Merge pull request #185 from djmitche/bug1509089  Bug 1509089 - remove LOCK_ROLES support|2018-11-30 02:24:43|
|[taskcluster-queue](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.md)|Merge pull request #304 from djmitche/bug1509189  Bug 1509189 - use unique table names to avoid conflicts|2018-11-30 02:12:03|
|[treescript](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/treescript.md)|Bump version.|2018-10-31 21:21:07|
