#  Last five commits from every repository 

|	autoland	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=04a31c0080dc)|Bug 1508825 - Enable ESLint for dom/crypto (manual changes) r=Standard8,Ehsan  Differential Revision: https://phabricator.services.mozilla.com/D13694|2018-12-14 22:54:56|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2b3549145fc3)|Bug 1508825 - Enable ESLint for dom/crypto/ (automatic changes) r=Standard8,Ehsan  Differential Revision: https://phabricator.services.mozilla.com/D13693|2018-12-14 00:44:52|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=acefb73b4d60)|Bug 1492706 - Part 2: Cover common OOM causes in the Recent tabs panel. r=nalexander  Looking at Crash Stats, the most common causes of OOMs involving the RecentTabs- Adapter happen while reading the previous session store file into memory for parsing, respectively while stringifying the parsed data back into a flat String for further storage.  In the former case, we give up completely, because there's nothing we can do short of switching to a streaming JSON parser (which is out of scope for this bug), while in the latter case, we only skip the affected tab in the hope that at least some tabs might be small enough to not cause an OOM.  Differential Revision: https://phabricator.services.mozilla.com/D12963|2018-12-14 21:08:32|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=bfc4d495548f)|Bug 1492706 - Part 1: Catch OOM during startup session restore. r=nalexander  We just treat this like a defective session store file and first fall back to the backup (although if the OOM is caused by a too-large file, it is likely that the backup will be too large as well) and then turn off session restoring completely.  We don't plug those failures into the session restore telemetry, though, because that is supposed to only cover truly defective files.  Differential Revision: https://phabricator.services.mozilla.com/D12962|2018-12-14 21:07:39|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=00a5c85fba1e)|Merge mozilla-central to autoland. a=merge CLOSED TREE|2018-12-15 09:42:09|

|	beta	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=17686e2a8e10)|Bug 1508664 - Avoid importing Extension.jsm too early r=kmag a=test-only  The test failure from this bug was due to code that reads Services.appinfo running too early before our test code that overrides appinfo got a chance to run.  Addon Manager test code could use a more thorough cleanup pass, but this is a quick-and-dirty fix suitable for uplifting in the short term.  Differential Revision: https://phabricator.services.mozilla.com/D14656|2018-12-15 00:29:38|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=d2bd2bb0c329)|Backed out changeset 2c85064c240c (bug 1511818) for frequently failing xpc tests in services/sync/tests/unit/. a=backout|2018-12-15 03:06:11|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=9eff0feefcf9)|Bug 1508056 - Create function for determining autographing scope. r=aki a=release  The deferred mar signing feature in Bug 1501878 has a taskcluster scope value in mar_signing.py hardcoded to something Firefox specific. This patch introduces a new function, get_autograph_format_scope, that will produce the right value for Firefox and Thunderbird.  Differential Revision: https://phabricator.services.mozilla.com/D13567|2018-12-13 09:10:00|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=6f8e2bdfd8b6)|Bug 1513505 - Fix invoke getter on prototype's property; r=jdescottes a=RyanVM  This lands the fix done in the debugger Reps for ObjectInspector (https://github.com/devtools-html/debugger.html/pull/7484\), and add a test to ensure we don't regress this. We take this as an opportunity to put some object inspector helpers in head.js so we don't repeat ourselves too much.  Differential Revision: https://phabricator.services.mozilla.com/D14240|2018-12-12 14:50:16|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=0d66c5be649b)|Bug 1513500 - Fixed it so getCurrentDisplay also checks if a flex container is actually a flex item. r=pbro a=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D14312|2018-12-13 15:07:49|

|	braindump	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=535d3728de73)|Fix params layout.|2018-12-11 20:45:39|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=c4919d73df5a)|Make required-signoffs the default.|2018-12-05 16:32:54|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=c73fd4625695)|add some partials to the unsigned mars params|2018-11-16 03:03:39|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=2f1b5cddb5f6)|add params-required-signoffs for bug 1501878|2018-11-12 19:19:42|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=0d4a4254960b)|quote mr versions to avoid being treated as floats|2018-11-02 20:18:01|

|	ci-admin	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=99d859a7a655)|Bug 1492665 - add modify_resources support r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6933|2018-10-22 17:52:14|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=241f75b5d808)|Bug 1492665 - add support for environments.yml r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6932|2018-10-22 17:52:13|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=d1796b61fbd0)|Bug 1494320 - remove unnecessary resources.manage r=tomprince  These were in place in order to delete some old, now-unused roles.  They're gone, so no need to continue to manage those namespaces.  Differential Revision: https://phabricator.services.mozilla.com/D9166|2018-10-19 03:02:08|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=9d35e153d813)|Don't generate hooks for actions with cross trust-domain `.taskcluster.yml`s; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D6858|2018-09-26 02:48:44|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=c88ca415a1c6)|Bug 1489181: handle input_schema in actions.yml r=aki  Differential Revision: https://phabricator.services.mozilla.com/D5683|2018-09-12 18:07:53|

|	ci-configuration	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=e9634d8942ca)|Bug 1510441: Use sparse profile in cron tasks; r=gps  Differential Revision: https://phabricator.services.mozilla.com/D13141|2018-11-30 13:01:34|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=13cbc18135d2)|Bug 1503894 - reenable taskcluster-cron for comm-central repo. r=tomprince  This goes along with a .cron.yml update in comm-central that removes the periodic-file-update cron configuration. (Bug 1499590 comment 15)  This will get comm-central nightly builds working again.  Differential Revision: https://phabricator.services.mozilla.com/D10959|2018-11-06 21:44:29|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=38144ac82b0a)|Bug 1503894 - disable taskcluster-cron for comm-central repos r=tomprince  The cron hook expects that it is checking out a gecko tree.  Robustcheckout kind of loses its mind when it clones mozilla-unified, then finds no ancestor in common with a comm-central pull.  Differential Revision: https://phabricator.services.mozilla.com/D10595|2018-11-01 18:52:02|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=48d479b3411b)|Bug 1502976 - upgrade decision image to the latest r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D10124|2018-10-29 21:38:55|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=d56b6be4c4c1)|Bug 1499590 - Enable taskcluster-cron on additional comm- repos. r=dustin  The periodic-file-updates cron task is meant to run on comm-central, comm-beta, and comm-esr60 like it's mozilla- counterpart task.  Differential Revision: https://phabricator.services.mozilla.com/D9860|2018-10-26 17:55:26|

|	comm-esr60	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/comm-esr60.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/comm-esr60.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=3510ade6c2cb)|Bug 1512977 - Part 2: Stop relying on x-mac-croatian for testing. r=mkmelin a=jorgk|2018-12-11 22:01:43|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=c4abcd141b6c)|Bug 1512977 - Part 1: Remove charset aliases for unsupported x-mac-NNNNN and MUTF-7, remove hard-coded x-windows-949. r=hsivonen a=jorgk|2018-12-11 22:01:41|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=bf0d776d3044)|Bug 809513 - Only notify for new mail in Inbox and non-special/virtual folders. r=aceman a=jorgk|2018-11-30 21:39:30|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=076be5ca12a9)|Bug 1481052 - FileLink WebExtensions API; r=Fallen a=jorgk|2018-11-28 23:04:41|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=ece4d20e004b)|Bug 820767 - Recognize plausible legacy Java-style encoding names and comment the alias file. r+a=jorgk    ms-prefixed labels for code pages in common with DOS and Windows (excl 866)    cp-prefixed labels for code pages in common with DOS and Windows (group existing)    No-hyphen label for ISO-2022-JP    Underscore labels for Unix CJK encodings    Remove some aliases for encodings that aren't supported    Map ISO-8859-1 aliases to windows-1252    Correct the case of gbk to GBK    Group UTF-7 labels together    Document all entries (even old ones)|2018-12-09 00:47:00|

|	inbound	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/inbound.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/inbound.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8a6afcb74cd9)|Backed out changeset b6d7250b9df3 (bug 1514346) for sm fuzzing build bustage CLOSED TREE|2018-12-15 16:53:26|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b6d7250b9df3)|Bug 1514346 - Add --enable-gczeal to fuzzing builds, r=decoder|2018-12-14 19:47:30|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3ead21c6776b)|Bug 1506869 - Rename roundButtonBackground and roundButtonPressedBackground. r=jaws|2018-12-15 11:25:53|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f44070541fb6)|Backed out changeset 571c01c5f84b (bug 1511604) for causing mochitest failures CLOSED TREE|2018-12-15 10:58:28|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c328c00179a9)|Bug 1362841 - Mirror the theme icons in customize mode in RTL to match the UI, r=gijs|2018-12-15 09:40:19|

|	mozilla-build	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-build.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-build.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=c5a55cf36958)|Bug 1501406 - Update vswhere to version 2.5.2.|2018-10-23 19:12:46|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=400ec3910570)|Bug 1501403 - Update UPX to version 3.95.|2018-10-23 19:08:31|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=5b1cf2c85207)|Bug 1501399 - Update emacs to version 26.1.|2018-10-23 18:57:20|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=d45e1040d212)|Bug 1501395 - Update the bundled sqlite3 DLL to 3.25.2.|2018-10-23 18:55:33|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=1af5fbf9b763)|Bug 1501395 - Update python3 to version 3.7.1.|2018-10-23 18:53:23|

|	mozilla-central	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5b0b8a39d09e)|Merge inbound to mozilla-central.  a=merge|2018-12-15 09:39:40|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1b960c462dcb)|Bug 1498073 - Ensure each bookmark engine test cleans up. a=testonly|2018-12-15 05:32:20|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9016c136594b)|Merge mozilla-central to mozilla-inbound.|2018-12-15 02:58:47|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=99dac743207c)|Bug 1508664 Avoid importing Extension.jsm too early r=kmag  The test failure from this bug was due to code that reads Services.appinfo running too early before our test code that overrides appinfo got a chance to run.  Addon Manager test code could use a more thorough cleanup pass, but this is a quick-and-dirty fix suitable for uplifting in the short term.  Differential Revision: https://phabricator.services.mozilla.com/D14656|2018-12-15 00:29:38|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=10aa1d024484)|Bug 1513600 - Use elementFromPoint() to measure isMouseOverVideo r=jaws  The checkEventWithin method is broken by two bugs:  The first one is bug 1493525 because we ended up pass the proxy instance, instead of the element reference, as the parent node to compare. The second one is unknown and happened sometime after that bug. The |relatedTarget| of the mouse event is always <video>, instead of the element within Shadow DOM that the cursor is moving out to.  Instead of identify the second bug in the DOM, this patch employs a simpler fix by using elementFromPoint() to identify the cursor position.  Differential Revision: https://phabricator.services.mozilla.com/D14342|2018-12-15 02:56:27|

|	mozilla-esr60	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-esr60.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-esr60.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=4bcb64fd8fa1)|Bug 1513900 - Reformat everything on the ESR branch to the Google coding style r=ehsan a=liz # ignore-this-changeset|2018-12-14 09:28:50|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=54261d68de3b)|Added tag PRE_TREEWIDE_CLANG_FORMAT for changeset ff97c7a84632|2018-12-14 08:29:05|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=ff97c7a84632)|Bug 1513901 - Remove the virtual keyword from two fuctions on the ESR branch; r=froydnj a=lizzard  Differential Revision: https://phabricator.services.mozilla.com/D14423 |2018-12-13 14:18:19|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=cfcc65a371db)|Bug 1448382 - Add js/src/vtune/ to the ThirdPartyPaths and .clang-format-ignore. r=sylvestre  MozReview-Commit-ID: 4Tni5V4K9Tv|2018-03-23 19:38:55|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=1f86411acbf4)|Bug 1508773 - Add dom/media/platforms/ffmpeg/ffmpeg57 and dom/media/platforms/ffmpeg/ffmpeg58 to the list of third-party directories r=jya  Differential Revision: https://phabricator.services.mozilla.com/D12470|2018-11-20 21:19:36|

|	mozilla-release	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=979903e9e9a8)|Automatic version bump CLOSED TREE NO BUG a=release DONTBUILD|2018-12-14 15:32:54|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=333d8e9009d8)|No bug - Tagging 3864bee6b6ea0a9ea05474da7ee77c12bf680364 with FENNEC_64_0_1_RELEASE a=release CLOSED TREE DONTBUILD|2018-12-14 15:32:50|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=448b0b631dd9)|Bug 1507947 - Be more careful when unbinding child process services. r=geckoview-reviewers,esawin, a=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D14065|2018-12-12 14:54:03|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=d6d490529a82)|No Bug, mozilla-release repo-update blocklist remote-settings - a=repo-update r=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D14388|2018-12-13 10:07:04|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=755ccdb8118d)|No bug - Tagging 3864bee6b6ea0a9ea05474da7ee77c12bf680364 with FENNEC_64_0_1_BUILD1 a=release CLOSED TREE DONTBUILD|2018-12-13 15:52:48|

|	try	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/try.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/try.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=eb796058356f)|Fuzzy query=ccov build  Pushed via `mach try fuzzy`|2018-12-15 16:45:51|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=cf903df8ccaf)|Bug 1473067 - Parse coverage artifacts at the end of builds. r=ted|2018-12-10 12:29:43|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=3df4639f3366)|try: -b o -p linux64 -u mochitest-e10s-bc -t none --artifact|2018-12-15 16:44:53|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=b474ea43edb9)|Bug 1514497 - Remove unused autocomplete-result-popupset and <children includes="toolbarbutton"/> from the urlbar binding. r=mak  Differential Revision: https://phabricator.services.mozilla.com/D14681|2018-12-15 15:24:28|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=6e5678f045ea)|try: -b do -p all -u gtest,mochitest-media,mochitest-media-e10s,reftest,reftest-e10s,reftest-no-accel,web-platform-tests -t none  Pushed via `mach try syntax` |2018-12-15 16:33:05|

|	addonscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/addonscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/addonscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/e9dd5dac0a21fe1943165416ac2eda1ff4b85792)|Merge pull request #51 from Callek/one_dot_oh  Bump to 1.0 and align setup.py requirements with requirements.txt.in|2018-05-17 13:58:03|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/05578d0c3f916e9be44fd825cf94ed201c44dea2)|Bump to 1.0 and align setup.py requirements with requirements.txt.in|2018-05-15 16:57:02|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/24408061c1ff8cd2799a1865c56ce8659101bb3f)|Update scriptworker from 11.0.0 to 11.1.0|2018-05-17 09:57:29|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/34f18115164aec34814b23cf17dddbe99bd2efa1)|Update scriptworker from 11.0.0 to 11.1.0|2018-05-17 09:57:28|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/b73b44300f0558a663ed37e0a9eac9ff0347b5b7)|Update virtualenv from 15.2.0 to 16.0.0|2018-05-17 00:27:29|

|	balrogscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/18761ab899d94619ea2a36c0227f0b0cfb1c6dea)|3.3.0|2018-11-26 17:29:44|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/e7a10365ddf6a5b82b204c072dc22d7b5267954f)|Add newsfragment.|2018-11-22 20:46:22|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/69fc7601f1ea569c9e40640f78b56c7d97bff71f)|Add code to create multiple blobs with different `updateLine` info.|2018-11-22 20:42:08|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/7f820677b714da97f9eb5ab0298fe022a6a289ca)|Add code to update multiple blobs with different suffixes.|2018-11-22 20:41:18|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/af210e95451e950d9151e745ccc4d0f3965b91d7)|Merge pull request #42 from tp-tc/tools-tests  Import some tests.|2018-11-22 18:42:07|

|	beetmoverscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/beetmoverscript/commit/883524121b34c630533fbec8db73c08797dcc7be)|8.0.0|2018-11-28 01:08:55|
|[Link to commit](https://github.com/mozilla-releng/beetmoverscript/commit/240e7a6cf19f7e56c003e51a09e11f29c6696580)|Declarative artifacts, reworking lguo's PR (#185)    Declarative artifacts, reworking lguo's PR      Remove debugging      unused import, for debugging      Adjust for new artifactMap format.    I'm not too happy about the way taskId is currently handled,  I'd like to improve on that before production deploys.      Support for artifact map within push-to-maven      Improve test coverage      Adjust key for artifacts_to_beetmove for maven with map      Update comment for clarity      Add test for cot in taskId|2018-11-28 01:04:36|
|[Link to commit](https://github.com/mozilla-releng/beetmoverscript/commit/73eb1f663e5f25b629f429a9148bcf9d0ee8cf11)|Update requests|2018-11-26 16:34:29|
|[Link to commit](https://github.com/mozilla-releng/beetmoverscript/commit/e845c331e8c9ce250c05c8c16fab5b73975d0689)|Use pip-compile to define requirements-prod.txt|2018-11-26 16:33:40|
|[Link to commit](https://github.com/mozilla-releng/beetmoverscript/commit/b19b4a250c6388c4bafbbf883f28391db9ab18da)|Merge pull request #191 from Callek/bump_7_10_2  Bump to 7.10.2|2018-11-07 21:01:00|

|	bouncerscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/bouncerscript/commit/c3be67b9b8886f78514503b97ff055553fbe77f2)|Merge pull request #46 from Callek/3.3.0  Bump to 3.3.0 for MSI installer|2018-11-12 16:20:14|
|[Link to commit](https://github.com/mozilla-releng/bouncerscript/commit/14820782bf1f83eabfa396b036b60e78df596399)|Bump to 3.3.0 for MSI installer|2018-11-12 16:01:24|
|[Link to commit](https://github.com/mozilla-releng/bouncerscript/commit/3792c3106c05c09875cdf9634e6da305188a9b95)|Merge pull request #43 from Callek/msi  Support .msi in bouncerscript|2018-11-12 15:09:06|
|[Link to commit](https://github.com/mozilla-releng/bouncerscript/commit/3409785ede3fa3a0377b8cee3e5bca3ab49757ed)|Merge branch 'master' into msi|2018-11-10 09:49:19|
|[Link to commit](https://github.com/mozilla-releng/bouncerscript/commit/a88e5f643bd2671cc47c6240a2794d8d11a5d792)|Fix logging (#45)|2018-11-10 09:49:02|

|	build-cloud-tools	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 

|	build-puppet	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/76197e1675bcabec24fde207c44b08fe97939690)|Merge pull request #324 from mitchhentges/reference-browser-new-key  Replaces reference-browser's dep signing certificate|2018-12-14 18:43:27|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/17c83b242a45925172a545a01cb54925099519b1)|Merge pull request #323 from mitchhentges/gp-config-content-dep-references  Updates Pushapk dep g_p_a_config_content to always reference g_p_config|2018-12-14 18:42:13|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/9ce1ad658cb393750d4ca7fc3b2cbfef4a6f8911)|Scheduled weekly dependency update for week 49 (#321)    Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update requests from 2.20.1 to 2.21.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update six from 1.11.0 to 1.12.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update taskcluster from 5.0.0 to 6.0.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update yarl from 1.2.6 to 1.3.0      Update boto3 from 1.9.53 to 1.9.63      Update botocore from 1.12.53 to 1.12.63      Update google-api-python-client from 1.7.4 to 1.7.6      Update ipython from 7.1.1 to 7.2.0      Update paste from 3.0.4 to 3.0.5      Update pastedeploy from 1.5.2 to 2.0.1      Update kombu from 4.2.1 to 4.2.2      Update sqlalchemy from 1.2.14 to 1.2.15      Update datadog from 0.25.0 to 0.26.0      Update setuptools from 40.6.2 to 40.6.3      Update mercurial from 4.8 to 4.8.1      Update mercurial from 4.8 to 4.8.1|2018-12-14 17:23:00|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/73c94d180bbe3dd71ae349969d9cc33665855a83)|Scheduled weekly dependency update for week 48 (#319)    Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update certifi from 2018.10.15 to 2018.11.29      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update idna from 2.7 to 2.8      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update multidict from 4.5.1 to 4.5.2      Update boto3 from 1.9.53 to 1.9.59      Update botocore from 1.12.53 to 1.12.59      Update google-api-python-client from 1.7.4 to 1.7.5      Update ipython from 7.1.1 to 7.2.0      Update paste from 3.0.4 to 3.0.5      Update pastedeploy from 1.5.2 to 2.0.1      Update datadog from 0.25.0 to 0.26.0      Update mercurial from 4.8 to 4.8.1      Update mercurial from 4.8 to 4.8.1      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7      Reverted idna from 2.8 to 2.7|2018-12-14 16:44:03|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/44696fc6a375c2869376f8f0377f680118b721d1)|Replaces reference-browser's dep signing certificate|2018-12-14 01:06:04|

|	mozapkpublisher	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/ac653d9dccec8624f8ff25f31b994757cca5fd79)|0.9.2|2018-11-08 09:57:02|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/faf0e1d2f62664cf325375ae90e546a665d00544)|Add requirements.txt.in in package so setup.py can use it|2018-11-08 09:56:04|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/5e6e12b4f158efcfdc2b2e38f111087caf2c79d4)|0.9.1|2018-11-07 19:08:58|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/ac653d9dccec8624f8ff25f31b994757cca5fd79)|0.9.2|2018-11-08 09:57:02|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/faf0e1d2f62664cf325375ae90e546a665d00544)|Add requirements.txt.in in package so setup.py can use it|2018-11-08 09:56:04|

|	OpenCloudConfig	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/4053e2c3c0db9b63ff74ca32c9bb6c14ccc4f08a)|Bug 1485628 - disable service pack updates & reboots  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:27:08|
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/bbdfd298d8fed84fab86e30d4322b365fb01a604)|Bug 1485628 - disable service pack updates & reboots  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:18:59|
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/bcb4c6ddd1c4efdc7fc07eb079b934e7a76ca12d)|Bug 1485628 - disable service pack updates & reboots  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:10:22|
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/3c874a7b7ab236ec1939728b43451e44eb50ff6f)|Bug 1485628 - disable service pack updates & reboots (#216)  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:08:20|

|	pushapkscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/58b5746152105b09751139192ac63f89486b664b)|0.9.0|2018-11-23 14:54:01|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/c783b80979156bf3cb2c78369dce300e2f76e5b6)|Parse manifest to detect what digest algorithm was used|2018-11-23 13:58:08|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/654ff459c35c9100cb9da8176c0e431a459e57d8)|Removes stray comma from example task json (#51)|2018-11-12 09:10:41|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/0fa1fec2424cba14dfa2c22ab42e44e937ffedc4)|Merge pull request #50 from mitchhentges/fix-travis-jdk-switcher  Resolves Travis Xenial image using Java11 instead of Java8|2018-11-09 22:28:06|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/2e8cc150527906f7d9bd23658c96f5d4221fdcf9)|Manually adds java 8 to front of $PATH for xenial Travis builds|2018-11-09 21:41:37|

|	pushsnapscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/1de161f0b36d3840806fecf41c5b84f30e1ac8df)|0.2.4|2018-10-05 13:09:12|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/45c2f94c2cfc0852f996c68a94549298ba9eb4a6)|Bug 1491262 - part 2: Fix esr lookup|2018-10-05 13:05:20|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/46ce3fda359015916a55fb6c6e3eca19816597a2)|0.2.3|2018-09-25 08:43:04|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/ed0c6c0e2d432ffe6f9fdcacc9b02832ee61af08)|Fix deprecation warning|2018-09-25 08:35:36|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/09b8fccbeddb9c727d5b8df8fd95c00c86471c5f)|Bug 1491262 - Make snap store push idempotent|2018-09-21 14:35:37|

|	scriptworker	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/0b1e25dfc8c1a6d2b4de965fb1d1f3a6955e9a9f)|17.0.0|2018-11-27 17:46:52|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/ae4cc4de36bd59a235c7a48e17d15c827caa3024)|Merge pull request #269 from escapewindow/pip-compile-multi  Pip compile multi|2018-11-13 21:32:49|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/48f9c9ca3c0d1eaae3c41d76f9166224a6eee45f)|update pinned requirements|2018-11-13 21:10:04|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/f760315f4f9f06e9492f4c87d8b79cfa0bde61c6)|address review comments|2018-11-13 21:09:55|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/648de55b994a2fb9f57bd6991e7a8a54ef3a4790)|pin hashes via pip-compile-multi in docker  I've been pinning mac-specific wheel hashes in dephash, which is wrong.|2018-10-30 23:37:30|

|	services	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/services.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla/release-services/commit/ae0004b50d4d2252d5b8ed3d3d3aa232a1412d14)|staticanalysis/bot: Filter clang-format publishable issues by their path. (#1689)|2018-11-20 15:36:16|
|[Link to commit](https://github.com/mozilla/release-services/commit/f5434b1aff3d78db8bfceae7cfa872382c4b1d9f)|codecoverage/backend: Add test for codecoverage backend with mocked rq and Redis (#1673)|2018-11-20 11:57:13|
|[Link to commit](https://github.com/mozilla/release-services/commit/88b939c265b26fe9e960d7a3361648d9ea522af6)|uplift/bot: Add a BUGZILLA_COMMENT_ONLY setting in order to report failed uplifts without cancelling requests. (#1680)|2018-11-20 09:34:34|
|[Link to commit](https://github.com/mozilla/release-services/commit/3399eed333cb502e46c5a7b83f3673d0fb4faafb)|shipit/frontent: add testing config (#1687)  At this point it is the same as staging.js|2018-11-20 01:39:45|
|[Link to commit](https://github.com/mozilla/release-services/commit/37bc7cafe221c5cea7d33041125d95312fe7757f)|shipit/api: update release status (#1688)  In the future we will need to update the release status explicitly from  a in-tree scheduled task, so we mark a release as completed only after  all required tasks are done (bouncer, tests, etc).|2018-11-19 20:45:16|

|	ship-it	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/ship-it.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/ship-it.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/ship-it/commit/01e0a190cba5bb6d81949fabe71054ab6d1a7bde)|Bump TB version to 66. (#248)|2018-12-10 21:54:20|
|[Link to commit](https://github.com/mozilla-releng/ship-it/commit/4ff40330cb5221d24e76fa3c273ed4c549794bb5)|Nightly 66: Merge and deply when 66 builds are available for all locales (#247)|2018-12-10 16:49:45|
|[Link to commit](https://github.com/mozilla-releng/ship-it/commit/f8d9c823a7fc598ba5e6623dd1f4e65c1de38393)|Add comment about syncing v1 and v2 configs (#246)|2018-11-30 19:20:47|
|[Link to commit](https://github.com/mozilla-releng/ship-it/commit/f1a6646f20ef404c2667d3b714c3ef90b6719546)|Bug 1511159 - Disable firefox releases (#245)|2018-11-30 17:07:43|
|[Link to commit](https://github.com/mozilla-releng/ship-it/commit/6e63fa3ca7a575eb4b325d606f6652360fea20c7)|Bug 1508140 - Add 'trs' to product-details (#243)|2018-11-19 02:14:35|

|	shipitscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/4c89c1b239fd8415e1225ba738ba820342bd8081)|Add support for Ship-it v2 (#14)|2018-11-21 16:33:53|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/0c892801fc9ad80e3a12b80ab69a7e3527ec0eea)|Address comments|2018-11-21 15:44:59|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/3033ccfe619289bfd022df1250a924f995ac33b8)|Revert local temp canges|2018-11-20 04:44:21|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/fb22074bb0e5bc26373cf5c2305e89f2a45eae25)|Bump version to 3.0.0|2018-11-20 04:24:43|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/2032f7bfc6c1629fa783a1af52f42ac51668d7f2)|Add support for masrk as shipped v2|2018-11-20 04:20:35|

|	signingscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signingscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signingscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/c15e3121714bef54103d4d7b126b470054b79d39)|9.5.1|2018-11-23 12:48:01|
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/57943a9e24a28ecdfc74062a9adc523288d557e0)|Fix SHA1 detection for APKs|2018-11-23 12:46:38|
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/02621783091e6139d313b7ef27a33314f9e1b596)|9.5.0|2018-11-22 15:12:48|
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/75e15a0b743977c70e1b2ad1651d267706063f02)|Generalize APK format to  Keep autograph_focus for migration purpose|2018-11-22 14:49:05|

|	signtool	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signtool.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signtool.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|3.2.1|2018-08-27 17:17:03|
|[Link to commit](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|switch to python 3.7 release; try to fix coveralls|2018-08-25 01:41:10|
|[Link to commit](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|2018-08-25 00:50:23|
|[Link to commit](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|Merge pull request #11 from escapewindow/py36  py36 support|2018-05-10 22:50:07|
|[Link to commit](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|py36 support|2018-05-10 22:37:21|

|	taskcluster-auth	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/dbbcef916c53765e535d7cd9580367089cec3a17)|Merge pull request #185 from djmitche/bug1509089  Bug 1509089 - remove LOCK_ROLES support|2018-11-30 02:24:43|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/9babc5e6d48fc27013e58e8e67eb085bfaa6561e)|Merge pull request #186 from djmitche/bug1509154  Bug 1509154 - await row removals|2018-11-30 02:24:34|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/6375db436a015e587979ded3e94fe36cd90ec7c6)|Bug 1509154 - await row removals|2018-11-29 01:23:01|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/b8c3dfe5dc51e448e3c4773b7bd386e8db37ffe9)|Bug 1509089 - remove LOCK_ROLES support  This was a big old hack meant to block changes to roles during the transition to storing roles in a blob.  It's not needed anymore.|2018-11-28 22:01:44|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/5077077f2e4094d22eef527dc9883cb8dffa387e)|Merge pull request #188 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|2018-12-10 18:27:23|

|	taskcluster-queue	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/c3a424aa0811c0b8bef42219a485d5a179a14ba2)|Merge pull request #304 from djmitche/bug1509189  Bug 1509189 - use unique table names to avoid conflicts|2018-11-30 02:12:03|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/cb8f3946830b982b58d2f93b99202cab15f40719)|Bug 1509189 - use unique table names to avoid conflicts  Taskcluster-Github already does something like this.  The tables get cleaned out and should have no rows at test completion, so this doesn't use a lot of space.  There's no limit (aside from space) on the number of tables in an account.|2018-11-29 01:12:10|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/f16ab6658148efcac18434802525091f66359f42)|Merge pull request #305 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|2018-12-07 15:23:43|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/904a244e39a0d96488f7fe41f031355b0e01f018)|Bug 1510377 - use tc-lib-references to validate references|2018-12-06 00:01:53|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/f16ab6658148efcac18434802525091f66359f42)|Merge pull request #305 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|2018-12-07 15:23:43|

|	treescript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/5513bb6bfd14c076aadbf275c2a9f3cffb3fb30a)|Bump version.|2018-10-31 21:21:07|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/b34cbe8f210f55b9e29eb438f1cd34b6390250a7)|Bug 1495464: Update hg.mozilla.org fingerprint.|2018-10-31 21:18:25|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/4f9700637f3c90610207fea918f15e10b6dfa44b)|Update virtualenv from 16.0.0 to 16.1.0|2018-10-31 16:31:24|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/26f431b8a1c975156ca16e7ba4416203e912c89c)|Update virtualenv from 16.0.0 to 16.1.0|2018-10-31 16:31:22|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/340147bcf13fd0407c26491501ea6c8fe162598d)|Update pyparsing from 2.2.0 to 2.3.0|2018-10-31 08:27:23|
