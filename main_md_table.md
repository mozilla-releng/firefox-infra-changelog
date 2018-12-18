#  Last five commits from every repository 

|	mozilla-central	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d65d6d242070)|Bug 1514735 - Update webrender to commit 4de718f9ea3435c099cabafc02e8b51da539bc62 (WR PR #3428). r=kats  https://github.com/servo/webrender/pull/3428  Differential Revision: https://phabricator.services.mozilla.com/D14823|2018-12-18 01:32:52|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c4eb9f94bc4c)|Bug 1514844 - Remove the per-process notification cache. r=asuth  This assumes that all of the notifications for a given origin must be in the same process. With this patch, we'll always go back to the parent process to get the notifications. Up next is limiting our search in the parent process to only the notifications we're looking for.  Differential Revision: https://phabricator.services.mozilla.com/D14774|2018-12-17 22:18:59|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c30fafd98c6f)|Bug 1514844 - Fix notification events in service workers. r=asuth  The current code assumes that it can get the ServiceWorkerManager in the child process to send a message to the proper service worker. That isn't true, we need to ask the parent to do it for us.  Differential Revision: https://phabricator.services.mozilla.com/D14773|2018-12-18 00:42:53|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4fcceeb6a1eb)|Bug 1514352 - Add "hidden focus" functionality to URLbar r=adw  Adds hiddenFocus() and removeHiddenFocus() methods and some CSS selector tweaking to enable focusing without visible changes.  MozReview-Commit-ID: Dq66TET4AVR  Differential Revision: https://phabricator.services.mozilla.com/D14733|2018-12-18 00:38:21|
|[Link to commit](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b350b5b4781e)|Bug 1514393 - Correct formatting in nsJPEGEncoder.cpp r=aosmond  Differential Revision: https://phabricator.services.mozilla.com/D14771|2018-12-17 23:50:23|

|	build-cloud-tools	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/build-cloud-tools/commit/3962e62c72251ae9fc531bdb5b14ba40243a5b70)|Merge branch 'La0-buildhub-cert'|2018-12-04 16:30:17|
|[Link to commit](https://github.com/mozilla-releng/build-cloud-tools/commit/7fe44bf80d48b949c4d65c7642e3e4b69780af84)|Add CNAME record for DigiCert on buildhub.moz.tools|2018-12-04 15:48:33|

|	build-puppet	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/7dd2e3be0ad46789d7c94d3ad8ce28057e2e219e)|Merge pull request #327 from mitchhentges/pushapk-indentation  Indents all pushapk puppet config with 4 spaces|2018-12-17 20:09:51|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/e8e82430350418b103b06894c6abc17e14d58eb3)|Indents all pushapk puppet config with 4 spaces|2018-12-17 19:52:21|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/67141303a3ed94d660a7a29b5f83bd41e1e7ae93)|Merge pull request #310 from MihaiTabara/snapshots  Snapshots|2018-12-17 17:06:09|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/d2287bfc06c78a549c20fee9e48b95d715816c24)|Merge pull request #325 from mitchhentges/reference-browser-puppet-secrets-underscore  Uses underscores for hiera content|2018-12-17 17:05:13|
|[Link to commit](https://github.com/mozilla-releng/build-puppet/commit/50b02de5c90a7ba1b7a5866ec127dd0b46da4865)|Roll-out production credentials as well.|2018-12-17 16:46:33|

|	mozapkpublisher	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/3539ea1a35edcd244d3aef7d11027376f47cd4a8)|Merge pull request #142 from mitchhentges/reference-browser-compat  Removes firefox_  extraction for reference-browser|2018-12-14 18:43:13|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/60212bc7f1ec194e89ced2e6fd84fc2eb4fb9b50)|Adds calculation of architecture and locales for r-b|2018-12-13 23:18:55|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/b743a7822390682f5f1bc3934558c2a396167acd)|Removes "application.ini" extraction from reference browser apk|2018-12-13 22:23:46|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/1fb14864d5118d3fc448ba6c9da0dbc9915e4269)|Merge pull request #139 from mitchhentges/reference-browser-compat  Adds reference-browser as another focus-esque publishable browser|2018-12-12 00:08:13|
|[Link to commit](https://github.com/mozilla-releng/mozapkpublisher/commit/979da90f37b107b3c511029896e89428be7efb39)|Removes reference-browser from the set of focus types|2018-11-30 22:10:11|

|	OpenCloudConfig	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 

|	scriptworker	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/a1e005a297d7990fdeb56b3ed803d52dcb9137c3)|Create mobile contexts to make tests closer to reality|2018-12-12 09:41:52|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/7b6716c0cd8302bf61cfeb1be74562d6c154b567)|Rename _get_additional_ _jsone_context into  _hg_ |2018-12-11 14:12:07|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/01549549503f93f93de586248abec117de8e5c46)|Merge pull request #285 from escapewindow/pytest-warnings  silence non-scriptworker test warnings|2018-12-13 00:15:03|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/84cec4e53646e0ae131920859abbe3bd5c6d3a47)|silence non-scriptworker test warnings|2018-12-12 23:25:32|
|[Link to commit](https://github.com/mozilla-releng/scriptworker/commit/931a23b64e40cd913a629b65f6e9ade989a33765)|Merge pull request #283 from escapewindow/docker-entrypoint  docker entrypoint for unittests + gpg testing|2018-12-11 22:43:53|

|	services	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/services.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla/release-services/commit/8ecd55d9668ffe527c23d3fdb8a7849f927a5017)|cli_common: mark artifact as completed when uploaded manually, fixes #1755, refs #1758|2018-12-18 08:34:14|
|[Link to commit](https://github.com/mozilla/release-services/commit/70bbd3d3fb477821bf6303ae7dd973e9fc272fd9)|staticanalysis/bot: Do not use improvement patches from before, fixes #1747, refs #1752.|2018-12-17 16:02:42|
|[Link to commit](https://github.com/mozilla/release-services/commit/02078ef90d3559b71dfa1ccb2a8d28876b2aad6e)|shipit/api: add tests (#1749)|2018-12-13 16:06:46|
|[Link to commit](https://github.com/mozilla/release-services/commit/3d778a4e4ee931be254efe2254e0036639e8d1db)|shipit/api: do not iterate over None (#1748)  This fixes the case when we have no partials (Fennec) but stil want to  use the `is_rc()` function|2018-12-13 15:07:14|
|[Link to commit](https://github.com/mozilla/release-services/commit/3ee50c9cdd4df8948fb8b59f561a5a75d6227277)|staticanalysis/bot: Better clang-format patch publication (#1729)|2018-12-13 06:44:47|

|	shipitscript	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/7c5698e73369eaaadeb03e17ab763e3635d7f47f)|Merge pull request #17 from garbas/fix-default-nix-argument  nix: use pkgs as a parameter, use layered docker image|2018-12-11 14:08:55|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/121f4dadb55daf3a19eaebbba364d5dbb89e1df1)|nix: use pkgs as a parameter, use layered docker image|2018-12-11 09:49:02|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/348311c6289c13257415a07ac8924798f0fa1826)|Merge pull request #16 from rail/nix|2018-12-11 02:05:15|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/1dce963106879a83e98bb3e2c8c320b5853a78fe)|Pass nixpkgs|2018-12-10 21:07:26|
|[Link to commit](https://github.com/mozilla-releng/shipitscript/commit/baca137b1ff147a6ddf5beea7bb51b0e3e2a7014)|Update the dependencies|2018-12-10 17:08:29|

|	signtool	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signtool.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/signtool.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 

|	taskcluster-auth	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/5077077f2e4094d22eef527dc9883cb8dffa387e)|Merge pull request #188 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|2018-12-10 18:27:23|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/325de3bc38bed1b8800668f0eed6e0d2ec8b73e7)|Bug 1510377 - use tc-lib-references to validate references|2018-12-06 00:00:09|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/d6424744e5f48b20255bac0083889508d3ab95a2)|(hotfix) upgrade tc-lib-api for previous change|2018-12-05 23:45:07|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/4c1447920ffafd15bdbc32cc5a243cd97c62684c)|Merge pull request #187 from arshadkazmi42/bug-1400999  204 response changed to use res.reply|2018-12-05 23:38:19|
|[Link to commit](https://github.com/taskcluster/taskcluster-auth/commit/2a6d46d36e0b7e2fb4b6fc4ee59914033238506f)|204 response changed to use res.reply|2018-12-02 18:34:01|

|	taskcluster-queue	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/1e47a960a34cd36322900cad5bfc2834fcea7b8f)|Merge pull request #306 from djmitche/bug1502892  Bug 1502892 - refactor create/defineTask to check authorization before validation|2018-12-14 17:22:13|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/98f3728774245c48582184e4ba49dc7a00f84b9a)|Bug 1502892 - refactor create/defineTask to check authorization before validating|2018-12-13 21:36:40|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/45bbf334a67982ff9cd6bd58b2ad0e502879cd89)|Bug 1502892 - add some more tests around createTask and priorities|2018-12-13 21:20:09|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/f16ab6658148efcac18434802525091f66359f42)|Merge pull request #305 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|2018-12-07 15:23:43|
|[Link to commit](https://github.com/taskcluster/taskcluster-queue/commit/904a244e39a0d96488f7fe41f031355b0e01f018)|Bug 1510377 - use tc-lib-references to validate references|2018-12-06 00:01:53|
