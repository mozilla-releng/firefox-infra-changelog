#  Last five commits from every repository 

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=34970df80385)|Merge mozilla-inbound to mozilla-central a=merge|Razvan Maries |merge|2019-01-01 09:44:07|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=389460801c5c)|Bug 1501584 - Run jittests for opt js shell for arm7, arm64 on android-hw-p2, r=jmaher.|Bob Clary |jmaher.|2018-12-31 22:15:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c19c61fee4ec)|Merge mozilla-central to mozilla-inbound. a=merge on a CLOSED TREE|Daniel Varga |merge|2018-12-31 21:27:53|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d39f40e695de)|Bug 1392946 - backout 61eca43af2dffc3ba19cf343210d851c638694d5 since it was not effective|Geoff Brown ||2018-12-31 20:24:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8d7a5d1ab4d8)|Bug 1516441 - backout f2dc090551f076387b984a670fe9eb7be9c8d460 since it was not effective|Geoff Brown ||2018-12-31 20:24:23|

<<<<<<< HEAD
|	beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=17686e2a8e10)|Bug 1508664 - Avoid importing Extension.jsm too early r=kmag a=test-only  The test failure from this bug was due to code that reads Services.appinfo running too early before our test code that overrides appinfo got a chance to run.  Addon Manager test code could use a more thorough cleanup pass, but this is a quick-and-dirty fix suitable for uplifting in the short term.  Differential Revision: https://phabricator.services.mozilla.com/D14656|Andrew Swan |kmag|2018-12-15 00:29:38|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=d2bd2bb0c329)|Backed out changeset 2c85064c240c (bug 1511818) for frequently failing xpc tests in services/sync/tests/unit/. a=backout|Cosmin Sabou |backout|2018-12-15 03:06:11|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=9eff0feefcf9)|Bug 1508056 - Create function for determining autographing scope. r=aki a=release  The deferred mar signing feature in Bug 1501878 has a taskcluster scope value in mar_signing.py hardcoded to something Firefox specific. This patch introduces a new function, get_autograph_format_scope, that will produce the right value for Firefox and Thunderbird.  Differential Revision: https://phabricator.services.mozilla.com/D13567|Rob Lemley |aki|2018-12-13 09:10:00|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=6f8e2bdfd8b6)|Bug 1513505 - Fix invoke getter on prototype's property; r=jdescottes a=RyanVM  This lands the fix done in the debugger Reps for ObjectInspector (https://github.com/devtools-html/debugger.html/pull/7484\), and add a test to ensure we don't regress this. We take this as an opportunity to put some object inspector helpers in head.js so we don't repeat ourselves too much.  Differential Revision: https://phabricator.services.mozilla.com/D14240|Nicolas Chevobbe |jdescottes|2018-12-12 14:50:16|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=0d66c5be649b)|Bug 1513500 - Fixed it so getCurrentDisplay also checks if a flex container is actually a flex item. r=pbro a=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D14312|Micah Tigley |pbro|2018-12-13 15:07:49|

|	braindump	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/braindump.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/braindump.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=535d3728de73)|Fix params layout.|Tom Prince ||2018-12-11 20:45:39|
|[Link](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=c4919d73df5a)|Make required-signoffs the default.|Tom Prince ||2018-12-05 16:32:54|
|[Link](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=c73fd4625695)|add some partials to the unsigned mars params|Aki Sasaki ||2018-11-16 03:03:39|
|[Link](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=2f1b5cddb5f6)|add params-required-signoffs for bug 1501878|Aki Sasaki ||2018-11-12 19:19:42|
|[Link](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=0d4a4254960b)|quote mr versions to avoid being treated as floats|Aki Sasaki ||2018-11-02 20:18:01|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=99d859a7a655)|Bug 1492665 - add modify_resources support r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6933|Dustin J. Mitchell |Callek,bstack|2018-10-22 17:52:14|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=241f75b5d808)|Bug 1492665 - add support for environments.yml r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6932|Dustin J. Mitchell |Callek,bstack|2018-10-22 17:52:13|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=d1796b61fbd0)|Bug 1494320 - remove unnecessary resources.manage r=tomprince  These were in place in order to delete some old, now-unused roles.  They're gone, so no need to continue to manage those namespaces.  Differential Revision: https://phabricator.services.mozilla.com/D9166|Dustin J. Mitchell |tomprince|2018-10-19 03:02:08|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=9d35e153d813)|Don't generate hooks for actions with cross trust-domain `.taskcluster.yml`s; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D6858|Tom Prince |dustin|2018-09-26 02:48:44|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=c88ca415a1c6)|Bug 1489181: handle input_schema in actions.yml r=aki  Differential Revision: https://phabricator.services.mozilla.com/D5683|Dustin J. Mitchell |aki|2018-09-12 18:07:53|

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=e9634d8942ca)|Bug 1510441: Use sparse profile in cron tasks; r=gps  Differential Revision: https://phabricator.services.mozilla.com/D13141|Tom Prince |gps|2018-11-30 13:01:34|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=13cbc18135d2)|Bug 1503894 - reenable taskcluster-cron for comm-central repo. r=tomprince  This goes along with a .cron.yml update in comm-central that removes the periodic-file-update cron configuration. (Bug 1499590 comment 15)  This will get comm-central nightly builds working again.  Differential Revision: https://phabricator.services.mozilla.com/D10959|Rob Lemley |tomprince|2018-11-06 21:44:29|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=38144ac82b0a)|Bug 1503894 - disable taskcluster-cron for comm-central repos r=tomprince  The cron hook expects that it is checking out a gecko tree.  Robustcheckout kind of loses its mind when it clones mozilla-unified, then finds no ancestor in common with a comm-central pull.  Differential Revision: https://phabricator.services.mozilla.com/D10595|Dustin J. Mitchell |tomprince|2018-11-01 18:52:02|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=48d479b3411b)|Bug 1502976 - upgrade decision image to the latest r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D10124|Dustin J. Mitchell |tomprince|2018-10-29 21:38:55|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=d56b6be4c4c1)|Bug 1499590 - Enable taskcluster-cron on additional comm- repos. r=dustin  The periodic-file-updates cron task is meant to run on comm-central, comm-beta, and comm-esr60 like it's mozilla- counterpart task.  Differential Revision: https://phabricator.services.mozilla.com/D9860|Rob Lemley |dustin|2018-10-26 17:55:26|

|	comm-esr60	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/comm-esr60.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/comm-esr60.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=3510ade6c2cb)|Bug 1512977 - Part 2: Stop relying on x-mac-croatian for testing. r=mkmelin a=jorgk|Jorg K |mkmelin|2018-12-11 22:01:43|
|[Link](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=c4abcd141b6c)|Bug 1512977 - Part 1: Remove charset aliases for unsupported x-mac-NNNNN and MUTF-7, remove hard-coded x-windows-949. r=hsivonen a=jorgk|Jorg K |hsivonen|2018-12-11 22:01:41|
|[Link](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=bf0d776d3044)|Bug 809513 - Only notify for new mail in Inbox and non-special/virtual folders. r=aceman a=jorgk|Jorg K |aceman|2018-11-30 21:39:30|
|[Link](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=076be5ca12a9)|Bug 1481052 - FileLink WebExtensions API; r=Fallen a=jorgk|Geoff Lankow |Fallen|2018-11-28 23:04:41|
|[Link](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=ece4d20e004b)|Bug 820767 - Recognize plausible legacy Java-style encoding names and comment the alias file. r+a=jorgk    ms-prefixed labels for code pages in common with DOS and Windows (excl 866)    cp-prefixed labels for code pages in common with DOS and Windows (group existing)    No-hyphen label for ISO-2022-JP    Underscore labels for Unix CJK encodings    Remove some aliases for encodings that aren't supported    Map ISO-8859-1 aliases to windows-1252    Correct the case of gbk to GBK    Group UTF-7 labels together    Document all entries (even old ones)|Henri Sivonen |jorgk|2018-12-09 00:47:00|

|	inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8a6afcb74cd9)|Backed out changeset b6d7250b9df3 (bug 1514346) for sm fuzzing build bustage CLOSED TREE|Bogdan Tara ||2018-12-15 16:53:26|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b6d7250b9df3)|Bug 1514346 - Add --enable-gczeal to fuzzing builds, r=decoder|Steve Fink |decoder|2018-12-14 19:47:30|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3ead21c6776b)|Bug 1506869 - Rename roundButtonBackground and roundButtonPressedBackground. r=jaws|D�o Gottwald |jaws|2018-12-15 11:25:53|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f44070541fb6)|Backed out changeset 571c01c5f84b (bug 1511604) for causing mochitest failures CLOSED TREE|Noemi Erli ||2018-12-15 10:58:28|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c328c00179a9)|Bug 1362841 - Mirror the theme icons in customize mode in RTL to match the UI, r=gijs|P Kausthubh S |gijs|2018-12-15 09:40:19|

|	mozilla-build	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-build.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-build.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=c5a55cf36958)|Bug 1501406 - Update vswhere to version 2.5.2.|Ryan VanderMeulen ||2018-10-23 19:12:46|
|[Link](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=400ec3910570)|Bug 1501403 - Update UPX to version 3.95.|Ryan VanderMeulen ||2018-10-23 19:08:31|
|[Link](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=5b1cf2c85207)|Bug 1501399 - Update emacs to version 26.1.|Ryan VanderMeulen ||2018-10-23 18:57:20|
|[Link](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=d45e1040d212)|Bug 1501395 - Update the bundled sqlite3 DLL to 3.25.2.|Ryan VanderMeulen ||2018-10-23 18:55:33|
|[Link](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=1af5fbf9b763)|Bug 1501395 - Update python3 to version 3.7.1.|Ryan VanderMeulen ||2018-10-23 18:53:23|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a77e8f3efc4c)|Merge inbound to mozilla-central a=merge|arthur.iakab |merge|2018-12-27 21:56:49|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=96499feeb5bf)|Bug 1433892 - Disable browser_ext_menus_events.js on Linux for frequent failures. r=jmaher|Cosmin Sabou |jmaher|2018-12-26 15:39:00|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ee0e1df960c4)|Bug 1516334 - don't draw emoji as paths when they are too big. r=rhunt|Lee Salzman |rhunt|2018-12-27 18:30:27|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3487b5f2f426)|Bug 1515963 - Add vixl::GdbDisassembleInstruction. r=sstangl  This add a simple function made to be called from gdb, which uses the vixl decoder to output in a static buffer the string corresponding to a single instruction.  This is useful when breaking at vixl::Simulator::ExecuteInstruction function, as follow:  (gdb) b vixl::Simulator::ExecuteInstruction Breakpoint 1 at 0x...: file ../jit/arm64/vixl/MozSimulator-vixl.cpp. (gdb) command 1 > call vixl::GdbDisassembleInstruction(this->pc_) > end |Nicolas B. Pierron |sstangl|2018-12-21 16:50:47|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=89834b056ca0)|Bug 1515704 - ARM64: Generate code for LPowHalfD. r=sstangl |Nicolas B. Pierron |sstangl|2018-12-20 17:53:41|

|	mozilla-esr60	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-esr60.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-esr60.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=4bcb64fd8fa1)|Bug 1513900 - Reformat everything on the ESR branch to the Google coding style r=ehsan a=liz # ignore-this-changeset|Sylvestre Ledru |ehsan|2018-12-14 09:28:50|
|[Link](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=54261d68de3b)|Added tag PRE_TREEWIDE_CLANG_FORMAT for changeset ff97c7a84632|Sylvestre Ledru ||2018-12-14 08:29:05|
|[Link](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=ff97c7a84632)|Bug 1513901 - Remove the virtual keyword from two fuctions on the ESR branch; r=froydnj a=lizzard  Differential Revision: https://phabricator.services.mozilla.com/D14423 |Ehsan Akhgari |froydnj|2018-12-13 14:18:19|
|[Link](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=cfcc65a371db)|Bug 1448382 - Add js/src/vtune/ to the ThirdPartyPaths and .clang-format-ignore. r=sylvestre  MozReview-Commit-ID: 4Tni5V4K9Tv|Andi-Bogdan Postelnicu |sylvestre|2018-03-23 19:38:55|
|[Link](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=1f86411acbf4)|Bug 1508773 - Add dom/media/platforms/ffmpeg/ffmpeg57 and dom/media/platforms/ffmpeg/ffmpeg58 to the list of third-party directories r=jya  Differential Revision: https://phabricator.services.mozilla.com/D12470|Ehsan Akhgari |jya|2018-11-20 21:19:36|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=979903e9e9a8)|Automatic version bump CLOSED TREE NO BUG a=release DONTBUILD|Mozilla Releng Treescript |release|2018-12-14 15:32:54|
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=333d8e9009d8)|No bug - Tagging 3864bee6b6ea0a9ea05474da7ee77c12bf680364 with FENNEC_64_0_1_RELEASE a=release CLOSED TREE DONTBUILD|Mozilla Releng Treescript |release|2018-12-14 15:32:50|
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=448b0b631dd9)|Bug 1507947 - Be more careful when unbinding child process services. r=geckoview-reviewers,esawin, a=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D14065|James Willcox |geckoview-reviewers,esawin,|2018-12-12 14:54:03|
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=d6d490529a82)|No Bug, mozilla-release repo-update blocklist remote-settings - a=repo-update r=RyanVM  Differential Revision: https://phabricator.services.mozilla.com/D14388|ffxbld |RyanVM|2018-12-13 10:07:04|
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=755ccdb8118d)|No bug - Tagging 3864bee6b6ea0a9ea05474da7ee77c12bf680364 with FENNEC_64_0_1_BUILD1 a=release CLOSED TREE DONTBUILD|Mozilla Releng Treescript |release|2018-12-13 15:52:48|

|	try	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/try.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/try.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/try/pushloghtml?changeset=eb796058356f)|Fuzzy query=ccov build  Pushed via `mach try fuzzy`|Marco Castelluccio ||2018-12-15 16:45:51|
|[Link](https://hg.mozilla.org/try/pushloghtml?changeset=cf903df8ccaf)|Bug 1473067 - Parse coverage artifacts at the end of builds. r=ted|Marco Castelluccio |ted|2018-12-10 12:29:43|
|[Link](https://hg.mozilla.org/try/pushloghtml?changeset=3df4639f3366)|try: -b o -p linux64 -u mochitest-e10s-bc -t none --artifact|D�o Gottwald ||2018-12-15 16:44:53|
|[Link](https://hg.mozilla.org/try/pushloghtml?changeset=b474ea43edb9)|Bug 1514497 - Remove unused autocomplete-result-popupset and <children includes="toolbarbutton"/> from the urlbar binding. r=mak  Differential Revision: https://phabricator.services.mozilla.com/D14681|D�o Gottwald |mak|2018-12-15 15:24:28|
|[Link](https://hg.mozilla.org/try/pushloghtml?changeset=6e5678f045ea)|try: -b do -p all -u gtest,mochitest-media,mochitest-media-e10s,reftest,reftest-e10s,reftest-no-accel,web-platform-tests -t none  Pushed via `mach try syntax` |Jean-Yves Avenard ||2018-12-15 16:33:05|

=======
>>>>>>> master
|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/3962e62c72251ae9fc531bdb5b14ba40243a5b70)|Merge branch 'La0-buildhub-cert'|dividehex|Placeholder|2018-12-04 16:30:17|
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/7fe44bf80d48b949c4d65c7642e3e4b69780af84)|Add CNAME record for DigiCert on buildhub.moz.tools|La0|Placeholder|2018-12-04 15:48:33|

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	| 
<<<<<<< HEAD
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/7dd2e3be0ad46789d7c94d3ad8ce28057e2e219e)|Merge pull request #327 from mitchhentges/pushapk-indentation  Indents all pushapk puppet config with 4 spaces|mitchhentges|Placeholder|2018-12-17 20:09:51|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/e8e82430350418b103b06894c6abc17e14d58eb3)|Indents all pushapk puppet config with 4 spaces|mitchhentges|Placeholder|2018-12-17 19:52:21|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/67141303a3ed94d660a7a29b5f83bd41e1e7ae93)|Merge pull request #310 from MihaiTabara/snapshots  Snapshots|MihaiTabara|Placeholder|2018-12-17 17:06:09|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/d2287bfc06c78a549c20fee9e48b95d715816c24)|Merge pull request #325 from mitchhentges/reference-browser-puppet-secrets-underscore  Uses underscores for hiera content|mitchhentges|Placeholder|2018-12-17 17:05:13|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/50b02de5c90a7ba1b7a5866ec127dd0b46da4865)|Roll-out production credentials as well.|MihaiTabara|Placeholder|2018-12-17 16:46:33|

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/3539ea1a35edcd244d3aef7d11027376f47cd4a8)|Merge pull request #142 from mitchhentges/reference-browser-compat  Removes firefox_  extraction for reference-browser|mitchhentges|Placeholder|2018-12-14 18:43:13|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/60212bc7f1ec194e89ced2e6fd84fc2eb4fb9b50)|Adds calculation of architecture and locales for r-b|mitchhentges|Placeholder|2018-12-13 23:18:55|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/b743a7822390682f5f1bc3934558c2a396167acd)|Removes "application.ini" extraction from reference browser apk|mitchhentges|Placeholder|2018-12-13 22:23:46|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/1fb14864d5118d3fc448ba6c9da0dbc9915e4269)|Merge pull request #139 from mitchhentges/reference-browser-compat  Adds reference-browser as another focus-esque publishable browser|mitchhentges|Placeholder|2018-12-12 00:08:13|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/979da90f37b107b3c511029896e89428be7efb39)|Removes reference-browser from the set of focus types|mitchhentges|Placeholder|2018-11-30 22:10:11|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
=======
>>>>>>> master
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

<<<<<<< HEAD
|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	| 
=======
|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
>>>>>>> master
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

<<<<<<< HEAD
|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	| 
=======
|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
>>>>>>> master
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

<<<<<<< HEAD
|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.json)	| 
=======
|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	| 
>>>>>>> master
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla/release-services/commit/bdebc7818475c6a3a8a60127b152cefc33beb7b9)|setup: Update dependencies (and a bit more) (#1730)  Along with updating dependencies I'm also addressing few other issues which will take full rebuild:    - upgrade to python 3.7, fixes #1715   - switch from Flask-Cache to Flask-Caching, fixes #1285   - sharing pypi2nix cache between containers, fixes #1070|garbas|Placeholder|2018-12-06 16:54:16|

|	taskcluster-auth	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/0ed7720082264fffa76b613de3bc18d888a8ae67)|Add listRoleIds() to paginate roles  (#189)    Add a listRoleIds endpoint      Fixed description in list-role-ids-response.yml      Return continuationToken only when limit is specified      Add tests      Improve tests and implement hashids      Add tests for invalid continuationToken|OjaswinM|Placeholder|2018-12-19 15:44:04|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/5077077f2e4094d22eef527dc9883cb8dffa387e)|Merge pull request #188 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|djmitche|Placeholder|2018-12-10 18:27:23|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/325de3bc38bed1b8800668f0eed6e0d2ec8b73e7)|Bug 1510377 - use tc-lib-references to validate references|djmitche|Placeholder|2018-12-06 00:00:09|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/d6424744e5f48b20255bac0083889508d3ab95a2)|(hotfix) upgrade tc-lib-api for previous change|djmitche|Placeholder|2018-12-05 23:45:07|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/4c1447920ffafd15bdbc32cc5a243cd97c62684c)|Merge pull request #187 from arshadkazmi42/bug-1400999  204 response changed to use res.reply|djmitche|Placeholder|2018-12-05 23:38:19|

|	taskcluster-queue	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/883b49e1b8954897910a658da78fa9d437023025)|Merge pull request #307 from taskcluster/monorepo-fixes  Monorepo fixes|imbstack|Placeholder|2018-12-20 20:28:27|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/53857be3999ed4ea579530f58e40901e361385cc)|Allow tests to complete|imbstack|Placeholder|2018-12-20 01:26:25|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/d26369bd567d61dbdedad529be877597e6738e7b)|Fix engines to be more permissive|imbstack|Placeholder|2018-12-20 01:24:59|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/1e47a960a34cd36322900cad5bfc2834fcea7b8f)|Merge pull request #306 from djmitche/bug1502892  Bug 1502892 - refactor create/defineTask to check authorization before validation|djmitche|Placeholder|2018-12-14 17:22:13|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/98f3728774245c48582184e4ba49dc7a00f84b9a)|Bug 1502892 - refactor create/defineTask to check authorization before validating|djmitche|Placeholder|2018-12-13 21:36:40|
