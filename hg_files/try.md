## TRY COMMIT MARKDOWN TABLE SINCE 2018-11-29 14:15:49.858547

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|20|vinoth |try: -b do -p all -u all -t none  Pushed via `mach try syntax`|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=04ffa65bae2a)|2018-12-13 12:15:13
|19|vinoth |Bug 1508282 - Temporary whitelist of files to skip Eval Assertion|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=5e45710cfdda)|2018-12-13 12:14:55
|18|André Bargull |try: -b do -p all -u jsreftest -t none|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=80676ed904cd)|2018-12-13 12:11:21
|17|André Bargull |Bug 1512989 - Part 2: Fix browser jstests failures. r=jorendorff|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=7bbba5f30423)|2018-12-13 12:10:06
|16|André Bargull |Bug 1512989 - Part 1: Pass correct test type. r=ahal|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=b051e7bd174f)|2018-12-13 10:24:56
|15|Dale Harvey |try: -b o -p linux64 -u mochitests,xpcshell -t none  Pushed via `mach try syntax` |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=68a0c0657413)|2018-12-13 12:04:12
|14|Dale Harvey |Bug 1488946 - Remove about:searchreset. r=mkaply |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=08c7330f395f)|2018-12-12 23:33:57
|13|Kartikaya Gupta |try: -b o -p linux64 -u all[linux64-qr] -t none  Pushed via `mach try syntax` |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=a1dceb0d0abc)|2018-12-13 12:03:39
|12|Kartikaya Gupta |test |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=9e10edf0f953)|2018-12-13 12:01:37
|11|Kartikaya Gupta |Bug 1507884 - Add tasks for linux-based testing of webrender standalone. r?jrmuizel   Differential Revision: https://phabricator.services.mozilla.com/D14407|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=b436ff9b51cb)|2018-12-13 11:46:17
|10|Kartikaya Gupta |Bug 1507884 - Add a wrench-deps toolchain to provide a tarball of crates wrench depends on. r?tomprince  Although this task technically doesn't build a toolchain, the set of steps it needs to do is very similar to what a toolchain build does, so we're shoehorning this task into the toolchain kind. The task basically runs `cargo vendor` on the gfx/wr/Cargo.lock file (if/when it changes) and exports a tarball of the resulting vendored crates. This allows downstream tasks that build stuff in gfx/wr to not have to re-fetch these crates from crates.io on every test run.  Differential Revision: https://phabricator.services.mozilla.com/D14406|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=4590a9e0e9b5)|2018-12-13 11:46:06
|9|Kartikaya Gupta |Bug 1507884 - Add a docker image for building and testing webrender standalone. r?glandium   Differential Revision: https://phabricator.services.mozilla.com/D14405|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=aa8c87f49f7c)|2018-12-13 11:45:52
|8|Dale Harvey |try: -b o -p linux64 -u mochitests,xpcshell -t none  Pushed via `mach try syntax` |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=c9302b4e9c8b)|2018-12-13 12:01:18
|7|Dale Harvey |Bug 1488946 - Remove about:searchreset. r=mkaply |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=7016c769d0a7)|2018-12-12 23:33:57
|6|moz-wptsync-bot |try: -b do -p win32,win64,linux64,linux -u web-platform-tests-e10s-1[linux64-stylo,Ubuntu,10.10,Windows 10],web-platform-tests-1[linux64-stylo,Ubuntu,10.10,Windows 10] -t none --artifact --try-test-paths web-platform-tests:testing/web-platform/tests/custom-elements/reactions/HTMLBaseElement.html|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=65cff62d58e7)|2018-12-13 11:48:19
|5|kaixinjxq |Bug 1513857 [wpt PR 14491] - Add CEReactions tests for HTMLBaseElement, a=testonly  wpt-commit: 91265abdedc9bcb0e79ae17fa6a9f0cbf3e3a90e wpt-pr: 14491 |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=e3bcc1b4198b)|2018-12-13 11:43:15
|4|Kartikaya Gupta |Fuzzy query='webren  Pushed via `mach try fuzzy` |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=c42a7d56f684)|2018-12-13 11:31:47
|3|Dão Gottwald |try: -b o -p win64 -u mochitest-e10s-bc -t none|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=ed13962ecd60)|2018-12-13 11:28:35
|2|moz-wptsync-bot |try: -b do -p win32,win64,linux64,linux -u web-platform-tests-e10s-1[linux64-stylo,Ubuntu,10.10,Windows 10],web-platform-tests-1[linux64-stylo,Ubuntu,10.10,Windows 10] -t none --artifact --try-test-paths web-platform-tests:testing/web-platform/tests/web-nfc/idlharness.https.window.js|[URL](https://hg.mozilla.org/try/pushloghtml?changeset=c8e250027640)|2018-12-13 11:26:02
|1|moz-wptsync-bot |Bug 1512580 [wpt PR 14411] - Update wpt metadata, a=testonly  wpt-pr: 14411 wpt-type: metadata |[URL](https://hg.mozilla.org/try/pushloghtml?changeset=9bb1f08040bb)|2018-12-07 09:03:46


