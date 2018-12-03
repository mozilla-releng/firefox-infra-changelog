#  Last five commits from every repository 

|	try	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/try.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/try.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=681e43225721)|try: -b do -p win32,win64,linux64,linux -u web-platform-tests-e10s-1[linux64-stylo,Ubuntu,10.10,Windows 10],web-platform-tests-1[linux64-stylo,Ubuntu,10.10,Windows 10] -t none --artifact --try-test-paths web-platform-tests:testing/web-platform/tests/web-animations/animation-model/animation-types/accumulation-per-property.html web-platform-tests:testing/web-platform/tests/web-animations/animation-model/animation-types/addition-per-property.html web-platform-tests:testing/web-platform/tests/web-animations/animation-model/animation-types/interpolation-per-property.html|2018-12-03 19:36:25|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=ebaa8ea0b039)|Bug 1509898 [wpt PR 14236] - Simplify interpolation of 2-D matrix transforms., a=testonly  The decomposition of a transformation matrix into translations, rotation, scale and skew transforms is not unique. In some cases, the generalized 3-D decomposition does not align with the working draft for CSS transforms (https://drafts.csswg.org/css-transforms/).  In the special case where the transforms being interpolated are both 2-D, a simplified model provides more restricted set of decomposition transforms with less computational overhead.  Bug: 797472 Change-Id: I2b8ba99fe02c2eef878d94f5dfaea55c39652759 Reviewed-on: https://chromium-review.googlesource.com/c/1332253 Commit-Queue: Kevin Ellis <kevers@chromium.org> Commit-Queue: Ian Vollick <vollick@chromium.org> Reviewed-by: Ian Vollick <vollick@chromium.org> Cr-Commit-Position: refs/heads/master@{#613191}  wpt-commit: a8ce772c68778cfb2c273fffb81e61da62d77bef wpt-pr: 14236 |2018-12-03 19:31:48|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=ad2c0b8a5d45)|try: -b do -p win32,win64,linux64,linux -u web-platform-tests-e10s-1[linux64-stylo,Ubuntu,10.10,Windows 10],web-platform-tests-1[linux64-stylo,Ubuntu,10.10,Windows 10] -t none --artifact --rebuild 10 --try-test-paths web-platform-tests:testing/web-platform/tests/web-animations/animation-model/animation-types/accumulation-per-property.html web-platform-tests:testing/web-platform/tests/web-animations/animation-model/animation-types/addition-per-property.html web-platform-tests:testing/web-platform/tests/web-animations/animation-model/animation-types/interpolation-per-property.html|2018-12-03 19:08:16|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=ed96a106a834)|try: -b do -p win32,win64,linux64,linux -u web-platform-tests-e10s-1[linux64-stylo,Ubuntu,10.10,Windows 10],web-platform-tests-1[linux64-stylo,Ubuntu,10.10,Windows 10] -t none --artifact --rebuild 10 --try-test-paths web-platform-tests:testing/web-platform/tests/webrtc/RTCRtpSender-transport.https.html|2018-12-03 19:01:24|
|[Link to commit](https://hg.mozilla.org/try/pushloghtml?changeset=d78db7bc9f93)|Bug 1511855 [wpt PR 14341] - Update wpt metadata, a=testonly  wpt-pr: 14341 wpt-type: metadata |2018-12-03 19:01:07|

|	ci-configuration	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=e9634d8942ca)|Bug 1510441: Use sparse profile in cron tasks; r=gps  Differential Revision: https://phabricator.services.mozilla.com/D13141|2018-11-30 13:01:34|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=13cbc18135d2)|Bug 1503894 - reenable taskcluster-cron for comm-central repo. r=tomprince  This goes along with a .cron.yml update in comm-central that removes the periodic-file-update cron configuration. (Bug 1499590 comment 15)  This will get comm-central nightly builds working again.  Differential Revision: https://phabricator.services.mozilla.com/D10959|2018-11-06 21:44:29|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=38144ac82b0a)|Bug 1503894 - disable taskcluster-cron for comm-central repos r=tomprince  The cron hook expects that it is checking out a gecko tree.  Robustcheckout kind of loses its mind when it clones mozilla-unified, then finds no ancestor in common with a comm-central pull.  Differential Revision: https://phabricator.services.mozilla.com/D10595|2018-11-01 18:52:02|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=48d479b3411b)|Bug 1502976 - upgrade decision image to the latest r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D10124|2018-10-29 21:38:55|
|[Link to commit](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=d56b6be4c4c1)|Bug 1499590 - Enable taskcluster-cron on additional comm- repos. r=dustin  The periodic-file-updates cron task is meant to run on comm-central, comm-beta, and comm-esr60 like it's mozilla- counterpart task.  Differential Revision: https://phabricator.services.mozilla.com/D9860|2018-10-26 17:55:26|

|	mozilla-build	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-build.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-build.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=c5a55cf36958)|Bug 1501406 - Update vswhere to version 2.5.2.|2018-10-23 19:12:46|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=400ec3910570)|Bug 1501403 - Update UPX to version 3.95.|2018-10-23 19:08:31|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=5b1cf2c85207)|Bug 1501399 - Update emacs to version 26.1.|2018-10-23 18:57:20|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=d45e1040d212)|Bug 1501395 - Update the bundled sqlite3 DLL to 3.25.2.|2018-10-23 18:55:33|
|[Link to commit](https://hg.mozilla.org/mozilla-build/pushloghtml?changeset=1af5fbf9b763)|Bug 1501395 - Update python3 to version 3.7.1.|2018-10-23 18:53:23|

|	ci-admin	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=99d859a7a655)|Bug 1492665 - add modify_resources support r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6933|2018-10-22 17:52:14|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=241f75b5d808)|Bug 1492665 - add support for environments.yml r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6932|2018-10-22 17:52:13|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=d1796b61fbd0)|Bug 1494320 - remove unnecessary resources.manage r=tomprince  These were in place in order to delete some old, now-unused roles.  They're gone, so no need to continue to manage those namespaces.  Differential Revision: https://phabricator.services.mozilla.com/D9166|2018-10-19 03:02:08|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=9d35e153d813)|Don't generate hooks for actions with cross trust-domain `.taskcluster.yml`s; r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D6858|2018-09-26 02:48:44|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=c88ca415a1c6)|Bug 1489181: handle input_schema in actions.yml r=aki  Differential Revision: https://phabricator.services.mozilla.com/D5683|2018-09-12 18:07:53|

|	beta	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=e9b94ebee2e7)|Bug 1511232 - Adjust test expectations of test_window_define_nonconfigurable.html for non-Trunk trees. a=test-only|2018-12-03 17:08:37|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=f9bba4d1865f)|Backed out changeset 8461e2f532ed (bug 1488554) to prevent talos xperf permafailures on 65 beta. a=backout|2018-10-16 17:26:55|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=c9f6bd2a826d)|Bug 1500274 - Bump the timeout for Windows opt builds to 3hr to match other PGO-enabled builds. r=me, a=release|2018-10-22 12:47:37|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=e6d60ab6b013)|Bug 1510678 - Change recommended addons for Firefox 64 CFR release. r=k88hudson	a=jcristau on a CLOSED TREE  Differential Revision: https://phabricator.services.mozilla.com/D13437|2018-11-29 17:43:06|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=32d14aa23dce)|Bug 1502530 - Part 2: Update tzdata in ICU data files to 2018g. r=Waldo a=jcristau|2018-11-06 13:18:26|

|	autoland	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a002d2b3408b)|Bug 1062128 - set tooltiptext for new tab button directly for a11y reasons, r=johannh  Differential Revision: https://phabricator.services.mozilla.com/D13406|2018-12-03 18:22:05|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e4e25a7e681f)|Bug 1511496 - Let the autohiding menu bar match the tab bar's height. r=mconley  Differential Revision: https://phabricator.services.mozilla.com/D13595|2018-12-03 17:03:21|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cac01bf33732)|Bug 1505063 - Only flip remoteness in RDM if we're switching from the privileged content process. r=ochameau  This means that for the File URI content process, we end up closing RDM if the page navigates. This appears to be an acceptable trade-off, as this is the behaviour we've been shipping since bug 1453519 landed (Firefox 61).  Differential Revision: https://phabricator.services.mozilla.com/D13331|2018-12-03 17:00:20|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1a6f9251c41f)|Bug 1491808 - [Linux/CSD/Titlebar] Force toplevel window repaint when titlebar rendering is enabled and its state changes, r=bzbarsky  Titlebar (StyleAppearance::MozWindowTitlebar) style depends on toplevel window focus and we need to redraw it when toplevel window focus changes.  Unfortunately according to https://gitlab.gnome.org/GNOME/gtk/issues/1395 the toplevel window focus can't be used here as we can have active but unfocused toplevel window during drag & drop.  Gtk+ controls window active appearance by window-state-event signal but gecko uses focus-in/out signals, so we need to repaint the titlebar when window-state-event comes  after  focus-in/out signals.  We can't call mWidgetListener->WindowActivated() (and WindowDeactivated()) as it was already called from focus-in/out handlers before window-state-event.  Depends on D13051  Differential Revision: https://phabricator.services.mozilla.com/D13052|2018-12-03 12:48:52|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d1fc8c77ad7f)|Bug 1491808 - Listen on window-state-event to set titlebar active/inactive state, r=jhorak  This is a workaround for https://gitlab.gnome.org/GNOME/gtk/issues/1395 Gtk+ controls window active appearance by window-state-event signal but gecko uses focus-in/out signals.  So we need to set the the titlebar state when window-state-event comes  after  focus-in/out signals.  Differential Revision: https://phabricator.services.mozilla.com/D13051|2018-12-03 12:48:35|

|	inbound	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/inbound.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/inbound.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4f08283a2e3a)|Bug 1510911 - Part 3: Backout changeset d0997972e4d4 (bug 1493563 - Part 4) for regressing performance |2018-11-29 15:50:38|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=82236b4be4c9)|Bug 1510911 - Part 2: Backout changeset f8849239da42 (bug 1493563 - Part 5) for regressing performance |2018-11-29 15:46:08|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c259bf672187)|Bug 1510911 - Part 1: Backout changeset cdb8932d1d8d (bug 1493563 - Part 11) for regressing performance |2018-11-29 15:37:54|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6ff23eb2892a)|Bug 1511714 - Unbreak on platform without GeckoProfiler after bug 1509571. r=mconley|2018-12-02 09:56:00|
|[Link to commit](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=decb54eeaa7d)|Bug 1503175 - Restore the previous inspector layout when reopening. r=gl|2018-11-09 17:56:05|

|	mozilla-central	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=60b122ce38e6)|No bug - Tagging mozilla-central 9ad82455dcee2bc1d438e46016b8db00e88758a8 with FIREFOX_BETA_65_BASE a=release DONTBUILD CLOSED TREE|2018-12-03 15:59:35|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9ad82455dcee)|Bug 1510689.  Only define IsNonConfigurableReadonlyPrimitiveGlobalProp if we plan to use it.  r=peterv a=Aryx,beta-fix|2018-12-03 14:14:15|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=01d0813d8203)|Merge inbound to mozilla-central.  a=merge|2018-12-03 09:30:40|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=290a2b092c01)|Bug 1452527: Un-skip reftest svg/outline.html on mac/linux, and mark it as fuzzy in general. (no review, just adjusting test annotation)  The fuzzy() annotation here is using the max-difference from the Windows failures in bug 1452527, and the number-of-mismatching-pixels from mac/linux failures in bug 1503525.|2018-12-03 01:09:25|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=016950978d66)|Revert "Backed out changeset d0fb1493b28b (bug 1511717) for devtools failures in browser_webconsole_eval_in_debugger_stackframe.js"  This reverts commit fd12a44e915d4e06f4509588ff4667dd9646e2dd. |2018-12-03 00:33:06|

|	mozilla-release	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=321f1fb3b41f)|Bug 1510678 - Change recommended addons for Firefox 64 CFR release. r=k88hudson	a=jcristau  Differential Revision: https://phabricator.services.mozilla.com/D13437|2018-11-29 17:43:06|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=fa624a63f7d9)|Bug 1502530 - Part 2: Update tzdata in ICU data files to 2018g. r=Waldo a=jcristau|2018-11-06 13:18:26|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=4498eed63436)|Bug 1502530 - Part 1: Update tzdata updater to use new location. r=Waldo a=jcristau|2018-11-06 10:48:56|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=d27d733d06cf)|Bug 1507433 - Avoid shape teleporting if any uncacheable prototypes. r=jandem a=jcristau  These cases are rare and uncacheable prototype shapes are tricky to get right so simplify code instead. The impact is that accessing non-own properties of an object that mutates its prototype will have a few more shape / group guards than are strictly needed.  Differential Revision: https://phabricator.services.mozilla.com/D12806|2018-11-27 13:10:49|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=f4770816becd)|Bug 1509810 - ASR Snippets: FxA signup template issues. r=ursula a=jcristau  Differential Revision: https://phabricator.services.mozilla.com/D13445|2018-11-29 17:49:59|

|	comm-esr60	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/comm-esr60.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/comm-esr60.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=c088b10cdb9d)|No bug - Pin mozilla-esr60 version for release. a=jorgk|2018-08-15 21:36:04|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=17f398c01f88)|Bug 1510913 - Remove the chromeclass-toolbar's unneeded margin-inline-start. r+a=jorgk|2018-12-01 10:12:18|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=04fee377d47e)|Bug 1509483 - Set a background color for #calendar-task-details-container on macOS. r+a=philipp|2018-11-23 18:28:23|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=fea596d791df)|Automatic version bump CLOSED TREE NO BUG a=release|2018-11-29 23:29:47|
|[Link to commit](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=bd67cdfc2e40)|No bug - Tagging 0ba73c30a3d9f213323766057d2176cd253efdd3 with THUNDERBIRD_60_3_2_BUILD1, THUNDERBIRD_60_3_2_RELEASE a=release CLOSED TREE|2018-11-29 23:29:46|

|	mozilla-esr60	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-esr60.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-esr60.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=5311a17b136e)|Bug 1510183 - Make HTMLEditor treat empty string attribute of style as nullptr of nsAtom rather than nsGkAtoms::_empty. r=m_kato a=jorgk DONTBUILD  After fixing bug 1427060, HTMLEditor treats attribute of style as nullptr. However, if empty string is used to call NS_Atomize(), it returns nsGkAtoms::_empty.  Therefore, HTMLEditor fails to check whether attribute is specified or not with nullptr check since some root callers sets nsGkAtoms::_empty instead of nullptr.  This patch makes HTMLEditor always use nullptr for empty string of attribute of style with wrapping NS_Atomize() with AtomzieAttribute().  Additionally, for safer change, this patch makes PropItem and TypeInState treat nsGkAtom::_empty as nullptr.|2018-11-30 01:21:59|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=6cc5fc0eaeaf)|Update configs. IGNORE BROKEN CHANGESETS CLOSED TREE NO BUG a=release ba=release|2018-12-03 16:38:03|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=d428d2b8f585)|Bug 1511495 - Update Firefox ESR60 to NSS 3.36.6. r=jcj, a=lizzard UPGRADE_NSS_RELEASE|2018-12-02 21:32:17|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=42791ed04461)|Bug 1505911 - Use IsAlpha/IsDigit instead of IsAsciiAlpha/IsAsciiDigit for full Unicode support. r=valentin a=jorgk DONTBUILD|2013-09-01 09:23:43|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-esr60/pushloghtml?changeset=3e8c9f8c5307)|Bug 1351940 - [marionette] Only convert a valid outerWindowID to a string. r=ato, a=test-only  Differential Revision: https://phabricator.services.mozilla.com/D13206|2018-11-28 20:48:42|

|	braindump	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=c73fd4625695)|add some partials to the unsigned mars params|2018-11-16 03:03:39|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=2f1b5cddb5f6)|add params-required-signoffs for bug 1501878|2018-11-12 19:19:42|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=0d4a4254960b)|quote mr versions to avoid being treated as floats|2018-11-02 20:18:01|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=56f54e63a30d)|Bug 1500897 - taskgraph-diff: Add "hg_branch" data|2018-10-23 14:46:00|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=b5f69b20179d)|No bug - Remove check_servo filter r=tomprince  Deleted in https://hg.mozilla.org/mozilla-central/rev/6c2ca1a524e6|2018-10-26 13:07:04|

|	balrogscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/18761ab899d94619ea2a36c0227f0b0cfb1c6dea)|3.3.0|2018-11-26 17:29:44|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/e7a10365ddf6a5b82b204c072dc22d7b5267954f)|Add newsfragment.|2018-11-22 20:46:22|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/69fc7601f1ea569c9e40640f78b56c7d97bff71f)|Add code to create multiple blobs with different `updateLine` info.|2018-11-22 20:42:08|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/7f820677b714da97f9eb5ab0298fe022a6a289ca)|Add code to update multiple blobs with different suffixes.|2018-11-22 20:41:18|
|[Link to commit](https://github.com/mozilla-releng/balrogscript/commit/af210e95451e950d9151e745ccc4d0f3965b91d7)|Merge pull request #42 from tp-tc/tools-tests  Import some tests.|2018-11-22 18:42:07|

|	shipitscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/4c89c1b239fd8415e1225ba738ba820342bd8081)|Add support for Ship-it v2 (#14)|2018-11-21 16:33:53|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/0c892801fc9ad80e3a12b80ab69a7e3527ec0eea)|Address comments|2018-11-21 15:44:59|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/3033ccfe619289bfd022df1250a924f995ac33b8)|Revert local temp canges|2018-11-20 04:44:21|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/fb22074bb0e5bc26373cf5c2305e89f2a45eae25)|Bump version to 3.0.0|2018-11-20 04:24:43|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/2032f7bfc6c1629fa783a1af52f42ac51668d7f2)|Add support for masrk as shipped v2|2018-11-20 04:20:35|

|	services	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/services.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla/release-services/commit/ae0004b50d4d2252d5b8ed3d3d3aa232a1412d14)|staticanalysis/bot: Filter clang-format publishable issues by their path. (#1689)|2018-11-20 15:36:16|
|[Link to commit](https://github.com/mozilla/release-services/commit/f5434b1aff3d78db8bfceae7cfa872382c4b1d9f)|codecoverage/backend: Add test for codecoverage backend with mocked rq and Redis (#1673)|2018-11-20 11:57:13|
|[Link to commit](https://github.com/mozilla/release-services/commit/88b939c265b26fe9e960d7a3361648d9ea522af6)|uplift/bot: Add a BUGZILLA_COMMENT_ONLY setting in order to report failed uplifts without cancelling requests. (#1680)|2018-11-20 09:34:34|
|[Link to commit](https://github.com/mozilla/release-services/commit/3399eed333cb502e46c5a7b83f3673d0fb4faafb)|shipit/frontent: add testing config (#1687)  At this point it is the same as staging.js|2018-11-20 01:39:45|
|[Link to commit](https://github.com/mozilla/release-services/commit/37bc7cafe221c5cea7d33041125d95312fe7757f)|shipit/api: update release status (#1688)  In the future we will need to update the release status explicitly from  a in-tree scheduled task, so we mark a release as completed only after  all required tasks are done (bouncer, tests, etc).|2018-11-19 20:45:16|

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

|	treescript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/5513bb6bfd14c076aadbf275c2a9f3cffb3fb30a)|Bump version.|2018-10-31 21:21:07|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/b34cbe8f210f55b9e29eb438f1cd34b6390250a7)|Bug 1495464: Update hg.mozilla.org fingerprint.|2018-10-31 21:18:25|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/4f9700637f3c90610207fea918f15e10b6dfa44b)|Update virtualenv from 16.0.0 to 16.1.0|2018-10-31 16:31:24|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/26f431b8a1c975156ca16e7ba4416203e912c89c)|Update virtualenv from 16.0.0 to 16.1.0|2018-10-31 16:31:22|
|[Link to commit](https://github.com/mozilla-releng/treescript/commit/340147bcf13fd0407c26491501ea6c8fe162598d)|Update pyparsing from 2.2.0 to 2.3.0|2018-10-31 08:27:23|

|	ship-it	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/ship-it.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/ship-it.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/ship-it/commit/f8d9c823a7fc598ba5e6623dd1f4e65c1de38393)|Add comment about syncing v1 and v2 configs (#246)|2018-11-30 19:20:47|
|[Link to commit](https://github.com/mozilla-releng/ship-it/commit/f1a6646f20ef404c2667d3b714c3ef90b6719546)|Bug 1511159 - Disable firefox releases (#245)|2018-11-30 17:07:43|

|	addonscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/addonscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/addonscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/e9dd5dac0a21fe1943165416ac2eda1ff4b85792)|Merge pull request #51 from Callek/one_dot_oh  Bump to 1.0 and align setup.py requirements with requirements.txt.in|2018-05-17 13:58:03|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/05578d0c3f916e9be44fd825cf94ed201c44dea2)|Bump to 1.0 and align setup.py requirements with requirements.txt.in|2018-05-15 16:57:02|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/24408061c1ff8cd2799a1865c56ce8659101bb3f)|Update scriptworker from 11.0.0 to 11.1.0|2018-05-17 09:57:29|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/34f18115164aec34814b23cf17dddbe99bd2efa1)|Update scriptworker from 11.0.0 to 11.1.0|2018-05-17 09:57:28|
|[Link to commit](https://github.com/mozilla-releng/addonscript/commit/b73b44300f0558a663ed37e0a9eac9ff0347b5b7)|Update virtualenv from 15.2.0 to 16.0.0|2018-05-17 00:27:29|

|	signingscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signingscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signingscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/c15e3121714bef54103d4d7b126b470054b79d39)|9.5.1|2018-11-23 12:48:01|
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/57943a9e24a28ecdfc74062a9adc523288d557e0)|Fix SHA1 detection for APKs|2018-11-23 12:46:38|
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/02621783091e6139d313b7ef27a33314f9e1b596)|9.5.0|2018-11-22 15:12:48|
|[Link to commit](https://github.com/mozilla-releng/signingscript/commit/75e15a0b743977c70e1b2ad1651d267706063f02)|Generalize APK format to  Keep autograph_focus for migration purpose|2018-11-22 14:49:05|

|	pushapkscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/58b5746152105b09751139192ac63f89486b664b)|0.9.0|2018-11-23 14:54:01|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/c783b80979156bf3cb2c78369dce300e2f76e5b6)|Parse manifest to detect what digest algorithm was used|2018-11-23 13:58:08|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/654ff459c35c9100cb9da8176c0e431a459e57d8)|Removes stray comma from example task json (#51)|2018-11-12 09:10:41|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/0fa1fec2424cba14dfa2c22ab42e44e937ffedc4)|Merge pull request #50 from mitchhentges/fix-travis-jdk-switcher  Resolves Travis Xenial image using Java11 instead of Java8|2018-11-09 22:28:06|
|[Link to commit](https://github.com/mozilla-releng/pushapkscript/commit/2e8cc150527906f7d9bd23658c96f5d4221fdcf9)|Manually adds java 8 to front of $PATH for xenial Travis builds|2018-11-09 21:41:37|

|	taskcluster-queue	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/c3a424aa0811c0b8bef42219a485d5a179a14ba2)|Merge pull request #304 from djmitche/bug1509189  Bug 1509189 - use unique table names to avoid conflicts|2018-11-30 02:12:03|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/cb8f3946830b982b58d2f93b99202cab15f40719)|Bug 1509189 - use unique table names to avoid conflicts  Taskcluster-Github already does something like this.  The tables get cleaned out and should have no rows at test completion, so this doesn't use a lot of space.  There's no limit (aside from space) on the number of tables in an account.|2018-11-29 01:12:10|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/eae5a8ff58e6edaac15fd95d273509c8045da3f6)|Bug 1509186 - remove references to taskcluster.net from the API description|2018-11-26 18:08:58|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/9595f61cd17ad72c315e52d7d950026527ded5c6)|Merge pull request #303 from djmitche/bug1456909  Bug 1456909 - use monitor.oneShot()|2018-11-26 22:05:11|

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
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/68bd2858a24e54fb079e76b8997b1ef19bfb5f88)|Merge pull request #184 from djmitche/bug1456909  Bug 1456909 - use monitor.oneShot|2018-11-26 22:08:53|

|	pushsnapscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/1de161f0b36d3840806fecf41c5b84f30e1ac8df)|0.2.4|2018-10-05 13:09:12|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/45c2f94c2cfc0852f996c68a94549298ba9eb4a6)|Bug 1491262 - part 2: Fix esr lookup|2018-10-05 13:05:20|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/46ce3fda359015916a55fb6c6e3eca19816597a2)|0.2.3|2018-09-25 08:43:04|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/ed0c6c0e2d432ffe6f9fdcacc9b02832ee61af08)|Fix deprecation warning|2018-09-25 08:35:36|
|[Link to commit](https://github.com/mozilla-releng/pushsnapscript/commit/09b8fccbeddb9c727d5b8df8fd95c00c86471c5f)|Bug 1491262 - Make snap store push idempotent|2018-09-21 14:35:37|

|	build-puppet	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/9f3cf327c3a20d1954ee2627a15b2e8dfa86ea8d)|Force reboot linux workers (#305)    Force reboot linux workers      Force reboot linux workers      Force reboot linux workers      Force reboot linux workers      Create a separate reboot command for OSX and Linux workers      Create a separate reboot command for OSX and Linux workers      Create a separate reboot command for OSX and Linux workers|2018-12-03 08:28:30|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/6d735b7ae012510bd96641ae01587eefa19fa744)|Bug 1511145: don't handle Firefox in releaserunner3 (#316)  Using fake values in case we don't hablde empty arrays properly|2018-11-30 17:10:54|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/0b8d96d712cfc710e2ca3d08ecaa5682369be068)|Bump scriptworker to 17.0.1 (#315)|2018-11-29 17:12:10|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/de413d0e22b0f5d478efc9dc1ef5dc3233f1eec3)|Merge pull request #312 from mitchhentges/pushapk-mobile-dep-settings  Adds mobile-dep pushapk env config|2018-11-28 23:14:51|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/3f41e7d42861eab53e8533a9ade6cfce509e12d8)|Adds note that taskcluster_client_id should be simplified|2018-11-28 21:17:31|

|	scriptworker	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/0b1e25dfc8c1a6d2b4de965fb1d1f3a6955e9a9f)|17.0.0|2018-11-27 17:46:52|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/ae4cc4de36bd59a235c7a48e17d15c827caa3024)|Merge pull request #269 from escapewindow/pip-compile-multi  Pip compile multi|2018-11-13 21:32:49|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/48f9c9ca3c0d1eaae3c41d76f9166224a6eee45f)|update pinned requirements|2018-11-13 21:10:04|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/f760315f4f9f06e9492f4c87d8b79cfa0bde61c6)|address review comments|2018-11-13 21:09:55|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/648de55b994a2fb9f57bd6991e7a8a54ef3a4790)|pin hashes via pip-compile-multi in docker  I've been pinning mac-specific wheel hashes in dephash, which is wrong.|2018-10-30 23:37:30|

|	build-cloud-tools	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/build-cloud-tools/commit/cb2ede208a3dda6df742eb0f251827762931f1d1)|Merge branch 'La0-buildhub'|2018-11-29 02:03:48|
|[Link to commit](https://github.com/mozilla-releng/build-cloud-tools/commit/62d5a4b0cf4c9d52836bc196680cca8ca08a4d53)|Add CNAME for buildhub.moz.tools|2018-11-27 09:13:51|

|	mozapkpublisher	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/ac653d9dccec8624f8ff25f31b994757cca5fd79)|0.9.2|2018-11-08 09:57:02|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/faf0e1d2f62664cf325375ae90e546a665d00544)|Add requirements.txt.in in package so setup.py can use it|2018-11-08 09:56:04|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/5e6e12b4f158efcfdc2b2e38f111087caf2c79d4)|0.9.1|2018-11-07 19:08:58|

|	OpenCloudConfig	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/4053e2c3c0db9b63ff74ca32c9bb6c14ccc4f08a)|Bug 1485628 - disable service pack updates & reboots  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:27:08|
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/bbdfd298d8fed84fab86e30d4322b365fb01a604)|Bug 1485628 - disable service pack updates & reboots  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:18:59|
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/bcb4c6ddd1c4efdc7fc07eb079b934e7a76ca12d)|Bug 1485628 - disable service pack updates & reboots  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:10:22|
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/3c874a7b7ab236ec1939728b43451e44eb50ff6f)|Bug 1485628 - disable service pack updates & reboots (#216)  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-28 17:08:20|
|[Link to commit](https://github.com/mozilla-releng/OpenCloudConfig/commit/c421eb84b254a74a84916ad5bd1d957bea060f33)|Bug 1510220 - defer upgrades in registry  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|2018-11-27 13:39:44|
