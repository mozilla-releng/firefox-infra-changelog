##  Commits in production - for 3 days, generated on: 2019-04-03 16:26:38 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e3809f2c3cb2)|[Bug 1533010](https://bugzilla.mozilla.org/show_bug.cgi?id=1533010)  - Update Windows Rust to 1.34 beta r=glandium This is needed for cross-language LTO [Bug 1512723](https://bugzilla.mozilla.org/show_bug.cgi?id=1512723)  We don't want to block on waiting for 1.34's release, so we'll get a head start now, but we'll update to the final 1.34 release when available. Rust Forge estimates the release at 11 April. Differential Revision: https://phabricator.services.mozilla.com/D25851|dmajor@mozilla.com|glandium|2019-04-03 18:13:09|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=48ae682107da)|[Bug 1540262](https://bugzilla.mozilla.org/show_bug.cgi?id=1540262)  - increase UV chunks from 12 to 16, r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D25673|jlund@mozilla.com|tomprince|2019-04-02 20:05:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3134268f32cd)|[Bug 1539903](https://bugzilla.mozilla.org/show_bug.cgi?id=1539903)  Use linux worker types for android jobs r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D25272|catlee@mozilla.com|tomprince|2019-04-02 20:02:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a54e5e2802d7)|[Bug 1527620](https://bugzilla.mozilla.org/show_bug.cgi?id=1527620)  - Add youtube streaming tests - r=whimboo This patch introduces a new marionette media test along with a Youtube test. To run the Youtube streaming test locally: ./mach marionette-test dom/media/test/marionette/test_youtube.py -vv --gecko-log - Differential Revision: https://phabricator.services.mozilla.com/D23644|tziade@mozilla.com|whimboo|2019-04-02 19:48:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3dc567fb205c)|[Bug 1539264](https://bugzilla.mozilla.org/show_bug.cgi?id=1539264)  Enable caches for mingwclang builds r=glandium,tomprince Differential Revision: https://phabricator.services.mozilla.com/D24973|catlee@mozilla.com|glandium,tomprince|2019-04-02 19:46:59|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ea0977445697)|Merge autoland to mozilla-central. a=merge|cbrindusan@mozilla.com|merge|2019-04-02 18:50:58|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=813b970cd40b)|[Bug 1538770](https://bugzilla.mozilla.org/show_bug.cgi?id=1538770)  - Replace TRY_MODIFIED_FILES by mozversioncontrol usage, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24876|babadie@mozilla.com|ahal|2019-04-02 17:27:47|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cb394c9bb56d)|[Bug 1540325](https://bugzilla.mozilla.org/show_bug.cgi?id=1540325)  - Run clang tools tasks only on try & code-review, r=glandium,sylvestre Differential Revision: https://phabricator.services.mozilla.com/D25562|babadie@mozilla.com|glandium,sylvestre|2019-04-02 12:40:01|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cff212107d95)|Backed out changeset 9b9c50876092 [Bug 1540325](https://bugzilla.mozilla.org/show_bug.cgi?id=1540325)  for Linting failure on clang.yml. CLOSED TREE|nbeleuzu@mozilla.com||2019-04-02 12:29:34|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9b9c50876092)|[Bug 1540325](https://bugzilla.mozilla.org/show_bug.cgi?id=1540325)  - Run clang tools tasks only on try & code-review, r=glandium,sylvestre Differential Revision: https://phabricator.services.mozilla.com/D25562|babadie@mozilla.com|glandium,sylvestre|2019-04-02 11:44:31|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cf6c7c082dc3)|Backed out changeset 304b957afe29 [Bug 1527620](https://bugzilla.mozilla.org/show_bug.cgi?id=1527620)  for marionette-media failures on test_youtube.py. CLOSED TREE|nbeleuzu@mozilla.com||2019-04-02 11:19:47|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=304b957afe29)|[Bug 1527620](https://bugzilla.mozilla.org/show_bug.cgi?id=1527620)  - Add youtube streaming tests - r=whimboo This patch introduces a new marionette media test along with a Youtube test. To run the Youtube streaming test locally: ./mach marionette-test dom/media/test/marionette/test_youtube.py -vv --gecko-log - Differential Revision: https://phabricator.services.mozilla.com/D23644|tziade@mozilla.com|whimboo|2019-04-02 10:40:31|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b6ca4ac5caa8)|Backed out changeset 0d8cf467ed34 [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  for Toolchains bustages CLOSED TREE|nerli@mozilla.com||2019-04-02 04:55:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=dccd58970fb0)|No bug: [mozharness] Remove obsolete push-candidate-to-releases script; r=aki This functionality has been replaced by beetmover. Also remove `mozharness.mozilla.aws`, of which this was the only consumer. Differential Revision: https://phabricator.services.mozilla.com/D25676|mozilla@hocat.ca|aki|2019-04-02 04:42:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0d8cf467ed34)|[Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  - Update non-Windows builds to clang 8. r=froydnj Windows builds have been taken care of in [Bug 1535441](https://bugzilla.mozilla.org/show_bug.cgi?id=1535441)  Differential Revision: https://phabricator.services.mozilla.com/D25328|mh@glandium.org|froydnj|2019-04-02 04:41:33|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5dc1b2326d3a)|Backed out changeset c75b53bc557a [Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  for unnecessary fix CLOSED TREE|nerli@mozilla.com||2019-04-02 00:39:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c75b53bc557a)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Follow up: Fix f8 warning in awsy_script. CLOSED TREE r=noemi_erli Differential Revision: https://phabricator.services.mozilla.com/D25664|nerli@mozilla.com|noemi_erli|2019-04-02 00:26:58|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2c5ea4fadb85)|No bug: [mozharness] Remove some dead code looking at substitutions in desktop l10n code; r=Callek There used to be various values that were substituted into the mozharness configuration for L10n jobs. All those substitutions have been removed, but the code to support them is still around. This removes that code. Differential Revision: https://phabricator.services.mozilla.com/D25143|mozilla@hocat.ca|Callek|2019-04-02 00:24:56|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8cfba39a9c9b)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Follow up: Fix f8 warning in awsy_script. CLOSED TREE Reviewers: noemi_erli Reviewed By: noemi_erli Subscribers: reviewbot Bug #: 1532491 Differential Revision: https://phabricator.services.mozilla.com/D25664|nerli@mozilla.com||2019-04-01 23:48:28|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=63888044e37b)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Part 3: Enable running AWSY tp6 in automation. r=bc An `sy-tp6` variant is added to the AWSY test suite that runs against the tp6 pageset. Differential Revision: https://phabricator.services.mozilla.com/D24585|erahm@mozilla.com|bc|2019-04-01 23:00:46|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=945e4151de08)|[Bug 1539847](https://bugzilla.mozilla.org/show_bug.cgi?id=1539847)  - [mozharness] Remove unused testing/mozharness/configs/unittests/win_unittest.py, r=tomprince This also renames win_taskcluster_unittest.py to win_unittest.py for consistency with the other platforms. Differential Revision: https://phabricator.services.mozilla.com/D25401|ahalberstadt@mozilla.com|tomprince|2019-04-01 22:59:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c367d8ca7f3a)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [tryselect] Also read mac/win_unittest.py configs in test_mozharness_integration.py, r=gbrown There are a few windows/mac-only suites that were missed since we were only reading the linux variant. Depends on D25401 Differential Revision: https://phabricator.services.mozilla.com/D25432|ahalberstadt@mozilla.com|gbrown|2019-04-01 22:59:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d3ba5839e2c2)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [mozharness] Remove definitions for defunct *-addons suites, r=gbrown Depends on D25432 Differential Revision: https://phabricator.services.mozilla.com/D25433|ahalberstadt@mozilla.com|gbrown|2019-04-01 22:59:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a7c0f3da75fa)|No bug: [mozharness] Remove some dead code looking at substitutions in desktop l10n code; r=Callek There used to be various values that were substituted into the mozharness configuration for L10n jobs. All those substitutions have been removed, but the code to support them is still around. This removes that code. Differential Revision: https://phabricator.services.mozilla.com/D25143|mozilla@hocat.ca|Callek|2019-04-01 21:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=65bcb804a3e6)|Backed out changeset 1ccb52b0784e [Bug 1532560](https://bugzilla.mozilla.org/show_bug.cgi?id=1532560)  for causing Gecko Decision Task bustage CLOSED TREE|aiakab@mozilla.com||2019-04-01 20:57:13|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1ccb52b0784e)|Fix [Bug 1532560](https://bugzilla.mozilla.org/show_bug.cgi?id=1532560)  Only run raptor-tp6-3 tests on AARM64 in try r=jmaher,rwood,gbrown Differential Revision: https://phabricator.services.mozilla.com/D23193|sdonner@mozilla.com|jmaher,rwood,gbrown|2019-04-01 20:49:34|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=508dd8a22136)|No bug: [taskgraph] Remove unused code for varying build-tools repo to use; r=aki We don't actually use the build-tools repo in-tree anymore, so remove the support code for it. Differential Revision: https://phabricator.services.mozilla.com/D25631|mozilla@hocat.ca|aki|2019-04-01 20:46:46|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=813b970cd40b)|[Bug 1538770](https://bugzilla.mozilla.org/show_bug.cgi?id=1538770)  - Replace TRY_MODIFIED_FILES by mozversioncontrol usage, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24876|dvarga@mozilla.com|ahal|2019-04-03 09:18:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3dc567fb205c)|[Bug 1539264](https://bugzilla.mozilla.org/show_bug.cgi?id=1539264)  Enable caches for mingwclang builds r=glandium,tomprince Differential Revision: https://phabricator.services.mozilla.com/D24973|dvarga@mozilla.com|glandium,tomprince|2019-04-03 09:18:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a54e5e2802d7)|[Bug 1527620](https://bugzilla.mozilla.org/show_bug.cgi?id=1527620)  - Add youtube streaming tests - r=whimboo This patch introduces a new marionette media test along with a Youtube test. To run the Youtube streaming test locally: ./mach marionette-test dom/media/test/marionette/test_youtube.py -vv --gecko-log - Differential Revision: https://phabricator.services.mozilla.com/D23644|dvarga@mozilla.com|whimboo|2019-04-03 09:18:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3134268f32cd)|[Bug 1539903](https://bugzilla.mozilla.org/show_bug.cgi?id=1539903)  Use linux worker types for android jobs r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D25272|dvarga@mozilla.com|tomprince|2019-04-03 09:18:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=48ae682107da)|[Bug 1540262](https://bugzilla.mozilla.org/show_bug.cgi?id=1540262)  - increase UV chunks from 12 to 16, r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D25673|dvarga@mozilla.com|tomprince|2019-04-03 09:18:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c6c69b6aa0fd)|[Bug 1541081](https://bugzilla.mozilla.org/show_bug.cgi?id=1541081)  - add win64-rust-size to aarch64 windows builds; r=dmajor We weren't including this before, which was causing us to not track size metrics for nss.dll and xul.dll, which is suboptimal. Differential Revision: https://phabricator.services.mozilla.com/D25792|dvarga@mozilla.com|dmajor|2019-04-03 09:18:49|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=945e4151de08)|[Bug 1539847](https://bugzilla.mozilla.org/show_bug.cgi?id=1539847)  - [mozharness] Remove unused testing/mozharness/configs/unittests/win_unittest.py, r=tomprince This also renames win_taskcluster_unittest.py to win_unittest.py for consistency with the other platforms. Differential Revision: https://phabricator.services.mozilla.com/D25401|cbrindusan@mozilla.com|tomprince|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c367d8ca7f3a)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [tryselect] Also read mac/win_unittest.py configs in test_mozharness_integration.py, r=gbrown There are a few windows/mac-only suites that were missed since we were only reading the linux variant. Depends on D25401 Differential Revision: https://phabricator.services.mozilla.com/D25432|cbrindusan@mozilla.com|gbrown|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d3ba5839e2c2)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [mozharness] Remove definitions for defunct *-addons suites, r=gbrown Depends on D25432 Differential Revision: https://phabricator.services.mozilla.com/D25433|cbrindusan@mozilla.com|gbrown|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=63888044e37b)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Part 3: Enable running AWSY tp6 in automation. r=bc An `sy-tp6` variant is added to the AWSY test suite that runs against the tp6 pageset. Differential Revision: https://phabricator.services.mozilla.com/D24585|cbrindusan@mozilla.com|bc|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8cfba39a9c9b)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Follow up: Fix f8 warning in awsy_script. CLOSED TREE Reviewers: noemi_erli Reviewed By: noemi_erli Subscribers: reviewbot Bug #: 1532491 Differential Revision: https://phabricator.services.mozilla.com/D25664|cbrindusan@mozilla.com||2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2c5ea4fadb85)|No bug: [mozharness] Remove some dead code looking at substitutions in desktop l10n code; r=Callek There used to be various values that were substituted into the mozharness configuration for L10n jobs. All those substitutions have been removed, but the code to support them is still around. This removes that code. Differential Revision: https://phabricator.services.mozilla.com/D25143|cbrindusan@mozilla.com|Callek|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c75b53bc557a)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Follow up: Fix f8 warning in awsy_script. CLOSED TREE r=noemi_erli Differential Revision: https://phabricator.services.mozilla.com/D25664|cbrindusan@mozilla.com|noemi_erli|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5dc1b2326d3a)|Backed out changeset c75b53bc557a [Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  for unnecessary fix CLOSED TREE|cbrindusan@mozilla.com||2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=0d8cf467ed34)|[Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  - Update non-Windows builds to clang 8. r=froydnj Windows builds have been taken care of in [Bug 1535441](https://bugzilla.mozilla.org/show_bug.cgi?id=1535441)  Differential Revision: https://phabricator.services.mozilla.com/D25328|cbrindusan@mozilla.com|froydnj|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=dccd58970fb0)|No bug: [mozharness] Remove obsolete push-candidate-to-releases script; r=aki This functionality has been replaced by beetmover. Also remove `mozharness.mozilla.aws`, of which this was the only consumer. Differential Revision: https://phabricator.services.mozilla.com/D25676|cbrindusan@mozilla.com|aki|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b6ca4ac5caa8)|Backed out changeset 0d8cf467ed34 [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  for Toolchains bustages CLOSED TREE|cbrindusan@mozilla.com||2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=76b3bde564ff)|[Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  - Update non-Windows builds to clang 8. r=froydnj Windows builds have been taken care of in [Bug 1535441](https://bugzilla.mozilla.org/show_bug.cgi?id=1535441)  Differential Revision: https://phabricator.services.mozilla.com/D25328|cbrindusan@mozilla.com|froydnj|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ea0977445697)|Merge autoland to mozilla-central. a=merge|cbrindusan@mozilla.com|merge|2019-04-02 11:40:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4338bf79beb2)|[Bug 1312823](https://bugzilla.mozilla.org/show_bug.cgi?id=1312823)  - Run console mocha tests on TRY. r=jdescottes. Differential Revision: https://phabricator.services.mozilla.com/D25045|opoprus@mozilla.com|jdescottes.|2019-04-01 13:04:43|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c6c69b6aa0fd)|[Bug 1541081](https://bugzilla.mozilla.org/show_bug.cgi?id=1541081)  - add win64-rust-size to aarch64 windows builds; r=dmajor We weren't including this before, which was causing us to not track size metrics for nss.dll and xul.dll, which is suboptimal. Differential Revision: https://phabricator.services.mozilla.com/D25792|rgurzau@mozilla.com|dmajor|2019-04-03 07:07:39|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=813b970cd40b)|[Bug 1538770](https://bugzilla.mozilla.org/show_bug.cgi?id=1538770)  - Replace TRY_MODIFIED_FILES by mozversioncontrol usage, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24876|rgurzau@mozilla.com|ahal|2019-04-03 00:49:08|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3dc567fb205c)|[Bug 1539264](https://bugzilla.mozilla.org/show_bug.cgi?id=1539264)  Enable caches for mingwclang builds r=glandium,tomprince Differential Revision: https://phabricator.services.mozilla.com/D24973|rgurzau@mozilla.com|glandium,tomprince|2019-04-03 00:49:08|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a54e5e2802d7)|[Bug 1527620](https://bugzilla.mozilla.org/show_bug.cgi?id=1527620)  - Add youtube streaming tests - r=whimboo This patch introduces a new marionette media test along with a Youtube test. To run the Youtube streaming test locally: ./mach marionette-test dom/media/test/marionette/test_youtube.py -vv --gecko-log - Differential Revision: https://phabricator.services.mozilla.com/D23644|rgurzau@mozilla.com|whimboo|2019-04-03 00:49:08|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3134268f32cd)|[Bug 1539903](https://bugzilla.mozilla.org/show_bug.cgi?id=1539903)  Use linux worker types for android jobs r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D25272|rgurzau@mozilla.com|tomprince|2019-04-03 00:49:08|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=48ae682107da)|[Bug 1540262](https://bugzilla.mozilla.org/show_bug.cgi?id=1540262)  - increase UV chunks from 12 to 16, r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D25673|rgurzau@mozilla.com|tomprince|2019-04-03 00:49:08|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=945e4151de08)|[Bug 1539847](https://bugzilla.mozilla.org/show_bug.cgi?id=1539847)  - [mozharness] Remove unused testing/mozharness/configs/unittests/win_unittest.py, r=tomprince This also renames win_taskcluster_unittest.py to win_unittest.py for consistency with the other platforms. Differential Revision: https://phabricator.services.mozilla.com/D25401|cbrindusan@mozilla.com|tomprince|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c367d8ca7f3a)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [tryselect] Also read mac/win_unittest.py configs in test_mozharness_integration.py, r=gbrown There are a few windows/mac-only suites that were missed since we were only reading the linux variant. Depends on D25401 Differential Revision: https://phabricator.services.mozilla.com/D25432|cbrindusan@mozilla.com|gbrown|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d3ba5839e2c2)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [mozharness] Remove definitions for defunct *-addons suites, r=gbrown Depends on D25432 Differential Revision: https://phabricator.services.mozilla.com/D25433|cbrindusan@mozilla.com|gbrown|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=63888044e37b)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Part 3: Enable running AWSY tp6 in automation. r=bc An `sy-tp6` variant is added to the AWSY test suite that runs against the tp6 pageset. Differential Revision: https://phabricator.services.mozilla.com/D24585|cbrindusan@mozilla.com|bc|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8cfba39a9c9b)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Follow up: Fix f8 warning in awsy_script. CLOSED TREE Reviewers: noemi_erli Reviewed By: noemi_erli Subscribers: reviewbot Bug #: 1532491 Differential Revision: https://phabricator.services.mozilla.com/D25664|cbrindusan@mozilla.com||2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2c5ea4fadb85)|No bug: [mozharness] Remove some dead code looking at substitutions in desktop l10n code; r=Callek There used to be various values that were substituted into the mozharness configuration for L10n jobs. All those substitutions have been removed, but the code to support them is still around. This removes that code. Differential Revision: https://phabricator.services.mozilla.com/D25143|cbrindusan@mozilla.com|Callek|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c75b53bc557a)|[Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  - Follow up: Fix f8 warning in awsy_script. CLOSED TREE r=noemi_erli Differential Revision: https://phabricator.services.mozilla.com/D25664|cbrindusan@mozilla.com|noemi_erli|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5dc1b2326d3a)|Backed out changeset c75b53bc557a [Bug 1532491](https://bugzilla.mozilla.org/show_bug.cgi?id=1532491)  for unnecessary fix CLOSED TREE|cbrindusan@mozilla.com||2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0d8cf467ed34)|[Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  - Update non-Windows builds to clang 8. r=froydnj Windows builds have been taken care of in [Bug 1535441](https://bugzilla.mozilla.org/show_bug.cgi?id=1535441)  Differential Revision: https://phabricator.services.mozilla.com/D25328|cbrindusan@mozilla.com|froydnj|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=dccd58970fb0)|No bug: [mozharness] Remove obsolete push-candidate-to-releases script; r=aki This functionality has been replaced by beetmover. Also remove `mozharness.mozilla.aws`, of which this was the only consumer. Differential Revision: https://phabricator.services.mozilla.com/D25676|cbrindusan@mozilla.com|aki|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b6ca4ac5caa8)|Backed out changeset 0d8cf467ed34 [Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  for Toolchains bustages CLOSED TREE|cbrindusan@mozilla.com||2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=76b3bde564ff)|[Bug 1538060](https://bugzilla.mozilla.org/show_bug.cgi?id=1538060)  - Update non-Windows builds to clang 8. r=froydnj Windows builds have been taken care of in [Bug 1535441](https://bugzilla.mozilla.org/show_bug.cgi?id=1535441)  Differential Revision: https://phabricator.services.mozilla.com/D25328|cbrindusan@mozilla.com|froydnj|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ea0977445697)|Merge autoland to mozilla-central. a=merge|cbrindusan@mozilla.com|merge|2019-04-02 11:35:12|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=508dd8a22136)|No bug: [taskgraph] Remove unused code for varying build-tools repo to use; r=aki We don't actually use the build-tools repo in-tree anymore, so remove the support code for it. Differential Revision: https://phabricator.services.mozilla.com/D25631|csabou@mozilla.com|aki|2019-04-02 00:54:51|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1ccb52b0784e)|Fix [Bug 1532560](https://bugzilla.mozilla.org/show_bug.cgi?id=1532560)  Only run raptor-tp6-3 tests on AARM64 in try r=jmaher,rwood,gbrown Differential Revision: https://phabricator.services.mozilla.com/D23193|csabou@mozilla.com|jmaher,rwood,gbrown|2019-04-02 00:54:51|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=65bcb804a3e6)|Backed out changeset 1ccb52b0784e [Bug 1532560](https://bugzilla.mozilla.org/show_bug.cgi?id=1532560)  for causing Gecko Decision Task bustage CLOSED TREE|csabou@mozilla.com||2019-04-02 00:54:51|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a7c0f3da75fa)|No bug: [mozharness] Remove some dead code looking at substitutions in desktop l10n code; r=Callek There used to be various values that were substituted into the mozharness configuration for L10n jobs. All those substitutions have been removed, but the code to support them is still around. This removes that code. Differential Revision: https://phabricator.services.mozilla.com/D25143|csabou@mozilla.com|Callek|2019-04-02 00:54:51|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5a85cf971fef)|Backed out changeset a7c0f3da75fa for linting opt failure in desktop_l10n.py CLOSED TREE|csabou@mozilla.com||2019-04-02 00:54:51|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=7a9123da87cc)|[Bug 1539905](https://bugzilla.mozilla.org/show_bug.cgi?id=1539905)  Cache yaml loading r=mtabara a=release Differential Revision: https://phabricator.services.mozilla.com/D25273|mtabara@mozilla.com|mtabara|2019-04-02 09:15:57|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/5c4d9623c48e20032a3605f3fa788e7c767f69b3)|Bug 1531165: Deploy new signtool to get new sha2signcode support (#440)|catlee|N/A|2019-04-02 19:32:16|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/5c5050fe3c4c22b67bf0a1d808a17c8086d352c9)|Merge pull request #528 from owlishDeveloper/bug1487699  Add GCP provider object. Implement listWorkers method|owlishDeveloper|N/A|2019-04-02 23:19:05|
|[Link](https://github.com/taskcluster/taskcluster/commit/b889a7c1040fd0bbb90b09a384d4a55db9f710a8)|[UI] Ignore casing when filtering in task group view (#532)|helfi92|N/A|2019-04-02 22:29:55|
|[Link](https://github.com/taskcluster/taskcluster/commit/63a8b777ebb3e6c0c9d25af2195a3bbde5107a39)|Expand filter|owlishDeveloper|N/A|2019-04-02 21:40:31|
|[Link](https://github.com/taskcluster/taskcluster/commit/deb9f782ab1f658e4ec2da0491b7203f2bb82b51)|Add GCP provider object. Implement listWorkers method|owlishDeveloper|N/A|2019-04-01 23:48:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/6c3f74082109c7a0c1d9e88b904167356f6d9837)|Merge pull request #529 from owlishDeveloper/bug1540891  Change linting rules for switches|owlishDeveloper|N/A|2019-04-02 17:52:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/e46d3c87bcfaf50e9d983e6c39725ce9c31e916b)|[Bug 1520918] [UI] Add UI for the denylist (#311)|OjaswinM|N/A|2019-04-02 13:07:24|
|[Link](https://github.com/taskcluster/taskcluster/commit/e4b20cf57c1336b4795f93906749b5d20815aef8)|Display unscheduled task properly (#531)|helfi92|N/A|2019-04-02 13:04:13|
|[Link](https://github.com/taskcluster/taskcluster/commit/53a4c415ca19c0cb9aef44e0ce293938ec17a31a)|Fix ability to add new secrets (#522)|helfi92|N/A|2019-04-02 12:22:08|
|[Link](https://github.com/taskcluster/taskcluster/commit/fa98fddaaa00f82a83106c92a21b9c192ff8c575)|Merge pull request #525 from djmitche/bug1536863-c  Bug 1536863 - be a little more flexible in reading the chimeric Auth0 profiles|djmitche|N/A|2019-04-01 20:41:40|
|[Link](https://github.com/taskcluster/taskcluster/commit/27f2c5c237b63ce336929c0a7f9e584797110929)|Bug 1536863 - be a little more flexible in reading the chimeric Auth0 profiles|djmitche|N/A|2019-04-01 20:01:17|
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
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=4029545f150e)|No Bug - Fix Fenix decision task which requires indexes r=mtabara Fix Fenix decision task which requires indexes Fixes https://tools.taskcluster.net/groups/UOLk6QheTf6cIOjrxk47Qg/tasks/UOLk6QheTf6cIOjrxk47Qg/runs/0/logs/public%2Flogs%2Flive.log\#L595 Differential Revision: https://phabricator.services.mozilla.com/D25911|jlorenzo@mozilla.com|mtabara|2019-04-03 12:14:24|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=630afd38ba9c)|[Bug 1541067](https://bugzilla.mozilla.org/show_bug.cgi?id=1541067)  - Allow try to access secret project/relman/coverity. r=tomprince,sylvestre Differential Revision: https://phabricator.services.mozilla.com/D25817|jlorenzo@mozilla.com|tomprince,sylvestre|2019-04-03 12:14:07|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
