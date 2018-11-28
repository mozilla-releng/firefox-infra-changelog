## TRY COMMIT MARKDOWN TABLE SINCE 2018-11-21 06:32:53.472188

| Commit Number | Commiter | Commit Message | Node | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|20|Tooru Fujisawa |try: -b do -p sm-plain-linux64 -u none -t none|https://hg.mozilla.org/try/pushloghtml?changeset=34f5d6b72c57|2018-11-28 04:28:35
|19|Tooru Fujisawa |Bug 1508063 - Part 4: Move non-auto-generated part of BinASTParser into BinASTParserPerTokenizer.|https://hg.mozilla.org/try/pushloghtml?changeset=7b9283b53fb5|2018-11-28 04:25:43
|18|Tooru Fujisawa |Bug 1508063 - Part 3: Fix typo in Binsource.yaml.|https://hg.mozilla.org/try/pushloghtml?changeset=0c8799b14244|2018-11-28 04:16:14
|17|Tooru Fujisawa |Bug 1508063 - Part 2: Move auto-generated enum to BinASTEnum.h.|https://hg.mozilla.org/try/pushloghtml?changeset=46acabefea88|2018-11-28 04:15:33
|16|Tooru Fujisawa |Bug 1508063 - Part 1: Move BinASTParserBase into its own files.|https://hg.mozilla.org/try/pushloghtml?changeset=af6136b99502|2018-11-28 00:57:55
|15|Nico Grunbaum |Fuzzy query=!pgo !ccov !stylo !reftest !wdspec !qr mochitest-browser | mochitest-media | web-platform  Pushed via `mach try again`|https://hg.mozilla.org/try/pushloghtml?changeset=adfe21dfa146|2018-11-28 04:16:31
|14|Nico Grunbaum |Bug 1328194 - remove deprecated PeerConnection.getStats callback and legacy stats|https://hg.mozilla.org/try/pushloghtml?changeset=881ad99ca1fb|2018-11-28 04:16:11
|13|Kartikaya Gupta |try: -b do -p android-api-16,win64,macosx64,linux64,linux64-base-toolchains,linux -u all[linux64-qr,windows10-64-qr,macosx64-qr] -t all[linux64-qr,windows10-64-qr,macosx64-qr]  Pushed via `mach try syntax`|https://hg.mozilla.org/try/pushloghtml?changeset=90fcfc11baca|2018-11-28 04:02:07
|12|Kartikaya Gupta |placeholder for try push  MozReview-Commit-ID: LKDk2deY2x7|https://hg.mozilla.org/try/pushloghtml?changeset=b9be19e6cb7a|2018-11-28 04:02:02
|11|Kartikaya Gupta |Placeholder  MozReview-Commit-ID: LhRD1MOzjK|https://hg.mozilla.org/try/pushloghtml?changeset=644116821b7c|2018-11-28 04:01:09
|10|WR Updater Bot |Bug 1510376 - Update webrender to commit 3d73e3885907ae3d48b46fba891073abdb59e76d (WR PR #3359). r?kats  https://github.com/servo/webrender/pull/3359|https://hg.mozilla.org/try/pushloghtml?changeset=d628f4282540|2018-11-28 04:01:07
|9|Matthew Noorenberghe |Bug 1510470 - Disable OS re-auth for credit cards by default. r=timdream  Differential Revision: https://phabricator.services.mozilla.com/D13169|https://hg.mozilla.org/try/pushloghtml?changeset=75d25888cc91|2018-11-28 01:08:35
|8|Kyle Machulis |Bug 1505601 - Turn nsIDocShell XPIDL const lists into cenums; r=bzbarsky  Turn all const lists and related attributes into cenums, to provide a vague sense of type safety.  Depends on D11715  Differential Revision: https://phabricator.services.mozilla.com/D11716|https://hg.mozilla.org/try/pushloghtml?changeset=b99cfc042c4f|2018-11-28 03:30:56
|7|Kyle Machulis |Bug 1505601 - Move nsIDocShell INTERNAL_LOAD consts to nsDocShell; r=bzbarsky  Consts aren't used in JS anyways, so there's no reason for them to be in the IDL.  Differential Revision: https://phabricator.services.mozilla.com/D11715|https://hg.mozilla.org/try/pushloghtml?changeset=62089e4c3cc0|2018-11-28 03:30:54
|6|Thomas Daede |Bug 1501796 - Add nasm to debian7-build dockerfile. r=glandium  Differential Revision: https://phabricator.services.mozilla.com/D9747|https://hg.mozilla.org/try/pushloghtml?changeset=bba74d02a136|2018-11-28 03:23:08
|5|Thomas Daede |Bug 1510113 - Never inline SaveToEnv or SaveWordToEnv. r=karlt  This allows Valgrind to recognize the call stacks to this function, avoiding Valgrind warnings in intentional leaks in these functions.  Differential Revision: https://phabricator.services.mozilla.com/D13036|https://hg.mozilla.org/try/pushloghtml?changeset=d085db32a53d|2018-11-28 03:10:55
|4|Timothy Guan-tin Chien |Bug 1508000 - Dispatch UAWidgetUnbindFromTree event before calling nsGenericHTMLElement::UnbindFromTree() r=emilio  Differential Revision: https://phabricator.services.mozilla.com/D12205|https://hg.mozilla.org/try/pushloghtml?changeset=3d6e1fe4c371|2018-11-28 02:29:38
|3|Hiroyuki Ikezoe |Bug 1504065 - Drop text in the child element inside background-color animated element to avoid fuzziness on Windows 7 GPU. r=birtles  Depends on D13002  Differential Revision: https://phabricator.services.mozilla.com/D13171|https://hg.mozilla.org/try/pushloghtml?changeset=94ecc40729d0|2018-11-28 01:43:55
|2|Hiroyuki Ikezoe |Bug 1504065 - Support background-color animations on the compositor for nsIDOMWindowUtils::GetOMTAValue. r=birtles  Depends on D13001  Differential Revision: https://phabricator.services.mozilla.com/D13002|https://hg.mozilla.org/try/pushloghtml?changeset=a30f77050399|2018-11-28 00:59:15
|1|Hiroyuki Ikezoe |Bug 1504065 - Run background-color animations on the compositor. r=birtles  Changes for nsIDOMWindowUtils.getOMTAValue is in the next commit with come test cases.  Differential Revision: https://phabricator.services.mozilla.com/D13001|https://hg.mozilla.org/try/pushloghtml?changeset=d99d8f275d8b|2018-11-28 00:58:46


