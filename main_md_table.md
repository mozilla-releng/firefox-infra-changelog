##  Commits in production. 

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=b2d0f7af52d2)|Bug 1485680 - if we modify the action hook task logic, we need to update scriptworker. r=dustin  Differential Revision: https://phabricator.services.mozilla.com/D15482|Aki Sasaki |dustin|2019-01-01 12:38:58|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=0f4b1e9e03cd)|Bug 1515137 - pass environment rootUrl to cron context r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D14882|Dustin J. Mitchell |tomprince|2018-12-18 19:45:56|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=99d859a7a655)|Bug 1492665 - add modify_resources support r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6933|Dustin J. Mitchell |Callek,bstack|2018-10-22 17:52:14|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=241f75b5d808)|Bug 1492665 - add support for environments.yml r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6932|Dustin J. Mitchell |Callek,bstack|2018-10-22 17:52:13|
|[Link](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=d1796b61fbd0)|Bug 1494320 - remove unnecessary resources.manage r=tomprince  These were in place in order to delete some old, now-unused roles.  They're gone, so no need to continue to manage those namespaces.  Differential Revision: https://phabricator.services.mozilla.com/D9166|Dustin J. Mitchell |tomprince|2018-10-19 03:02:08|

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=e7c0152d0dc4)|Bug 1515137 - set TASKCLUSTER_ROOT_URL for cron hooks r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D14883|Dustin J. Mitchell |tomprince|2018-12-18 19:46:03|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=e9634d8942ca)|Bug 1510441: Use sparse profile in cron tasks; r=gps  Differential Revision: https://phabricator.services.mozilla.com/D13141|Tom Prince |gps|2018-11-30 13:01:34|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=13cbc18135d2)|Bug 1503894 - reenable taskcluster-cron for comm-central repo. r=tomprince  This goes along with a .cron.yml update in comm-central that removes the periodic-file-update cron configuration. (Bug 1499590 comment 15)  This will get comm-central nightly builds working again.  Differential Revision: https://phabricator.services.mozilla.com/D10959|Rob Lemley |tomprince|2018-11-06 21:44:29|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=38144ac82b0a)|Bug 1503894 - disable taskcluster-cron for comm-central repos r=tomprince  The cron hook expects that it is checking out a gecko tree.  Robustcheckout kind of loses its mind when it clones mozilla-unified, then finds no ancestor in common with a comm-central pull.  Differential Revision: https://phabricator.services.mozilla.com/D10595|Dustin J. Mitchell |tomprince|2018-11-01 18:52:02|
|[Link](https://hg.mozilla.org/build/ci-configuration/pushloghtml?changeset=48d479b3411b)|Bug 1502976 - upgrade decision image to the latest r=tomprince  Differential Revision: https://phabricator.services.mozilla.com/D10124|Dustin J. Mitchell |tomprince|2018-10-29 21:38:55|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0dcf945b3871)|Merge inbound to mozilla-central. a=merge|Oana Pop Rus |merge|2019-01-07 09:30:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=00e735944f33)|Bug 1479782 - Disable devtools/client/netmonitor/test/browser_net_frame.js on win10. r=jmaher|Cosmin Sabou |jmaher|2019-01-07 00:41:17|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=28134941aac4)|Bug 1518045 - Update owning_ref to 0.4.  This cherry-picks https://github.com/servo/servo/pull/22534, plus the relevant re-vendoring. |Bastien Orivel ||2018-12-22 20:02:42|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b14405139835)|Bug 1518045 - Rustfmt recent changes. |Emilio Cobos Álvarez ||2019-01-06 23:00:55|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=91e7ea77c846)|Bug 1518045 - Publish selectors 0.21.0 on crates.io. r=emilio  This cherry-picks https://github.com/servo/servo/pull/22577, with the relevant lockfile update. |Simon Sapin |emilio|2018-12-31 00:01:49|

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/balrogscript/commit/2385c55447fad6264645db77368fbd4649a936ea)|Merge pull request #47 from mitchhentges/release-3.5.0  3.5.0|mitchhentges|Placeholder|2019-01-03 19:50:17|
|[Link](https://github.com/mozilla-releng/balrogscript/commit/875537fc60b40ecd3ae72c833b88f933f2b6c7b7)|3.5.0|mitchhentges|Placeholder|2019-01-02 18:02:59|
|[Link](https://github.com/mozilla-releng/balrogscript/commit/9c10524c6565320b1a0d318d056f7fd303376a29)|Merge pull request #46 from mitchhentges/remove-schema-from-config  Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2019-01-02 17:14:42|
|[Link](https://github.com/mozilla-releng/balrogscript/commit/441a9aeb77979f3df5ac0433e9557af89797e3de)|Adds TODO about using sync_main(...) like other scripts|mitchhentges|Placeholder|2019-01-02 17:06:47|
|[Link](https://github.com/mozilla-releng/balrogscript/commit/e869556984b250c500edd0b3c226ebb16643fbc0)|Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2018-12-24 21:32:14|

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/7ee86337210f78bea022243da1c84253c65a1e94)|Merge pull request #203 from mitchhentges/release-8.3.0  8.3.0|mitchhentges|Placeholder|2019-01-03 18:30:51|
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/11be66989b2fe50e9fe2c7e7337c5abdf05a0ff1)|8.3.0|mitchhentges|Placeholder|2019-01-03 17:06:41|
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/9424a33ecc5a6abbe4f9d1cca84e0bac3c686415)|Adds changelog entry for 8.2.1|mitchhentges|Placeholder|2019-01-03 17:06:18|
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/21a801a934b714316ea475b3cc312048ba9cdc2b)|Merge pull request #201 from mitchhentges/remove-schema-from-config  Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2019-01-02 17:11:16|
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/a721342ccd6b3eda02f836f5d7da91a930925a30)|Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2018-12-24 21:45:34|

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/bouncerscript/commit/cf3b10f96874db1bb8107458b3ece1e281e902ea)|Merge pull request #48 from mitchhentges/release-3.4.0  3.4.0|mitchhentges|Placeholder|2019-01-03 19:57:59|
|[Link](https://github.com/mozilla-releng/bouncerscript/commit/1db10557cc46f331af59c27fd33943c12af0e856)|3.4.0|mitchhentges|Placeholder|2019-01-02 18:23:32|
|[Link](https://github.com/mozilla-releng/bouncerscript/commit/bc709e70a78a49f94e775141137518997d9ad18b)|Merge pull request #47 from mitchhentges/remove-schema-from-config  Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2019-01-02 17:12:19|
|[Link](https://github.com/mozilla-releng/bouncerscript/commit/efd2c06441d325a5556a758923cd7a099e627df4)|Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2018-12-24 22:03:13|

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/3962e62c72251ae9fc531bdb5b14ba40243a5b70)|Merge branch 'La0-buildhub-cert'|dividehex|Placeholder|2018-12-04 16:30:17|
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/7fe44bf80d48b949c4d65c7642e3e4b69780af84)|Add CNAME record for DigiCert on buildhub.moz.tools|La0|Placeholder|2018-12-04 15:48:33|

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	| 
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
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/b6706efa7f759a60feec456e74a12fa36bf4c1ce)|0.10.1|JohanLorenzo|Placeholder|2018-12-20 11:07:55|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/3f8624b739ec4cda708283b8de735ff98b22227f)|Reference browser: Remove broken check about API levels and processor architecture|JohanLorenzo|Placeholder|2018-12-20 10:41:14|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/7508711e3f3fa0fbefe699bf341bfbd6bd333652)|Merge pull request #144 from mitchhentges/release-0.10.0  Release 0.10.0|mitchhentges|Placeholder|2018-12-19 17:44:46|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/f956752aa12fcecd37dc342b57adbdd2ff7244bc)|0.10.0|mitchhentges|Placeholder|2018-12-19 17:36:03|
|[Link](https://github.com/mozilla-releng/mozapkpublisher/commit/3539ea1a35edcd244d3aef7d11027376f47cd4a8)|Merge pull request #142 from mitchhentges/reference-browser-compat  Removes firefox_  extraction for reference-browser|mitchhentges|Placeholder|2018-12-14 18:43:13|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/3c874a7b7ab236ec1939728b43451e44eb50ff6f)|Bug 1485628 - disable service pack updates & reboots (#216)  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|grenade|Placeholder|2018-11-28 17:08:20|

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/67c2714b27037f3f5b602b0a35f73bfee75dbdff)|Merge pull request #68 from mitchhentges/release-0.11.0  0.11.0|mitchhentges|Placeholder|2019-01-03 19:57:20|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/9aaf19547241dcb8b356d2df37e31a3c370a595b)|0.11.0|mitchhentges|Placeholder|2019-01-02 18:21:01|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/edae04d0d4d208b0d14438ec3abedc568ea0a984)|Merge pull request #67 from mitchhentges/path-join-no-slashes  Removes "/" from os.path.join|mitchhentges|Placeholder|2019-01-02 16:58:14|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/fd38d6e7f7bf92f9af3c3821fc99fd494c116523)|Removes "/" from os.path.join|mitchhentges|Placeholder|2018-12-24 20:26:27|
|[Link](https://github.com/mozilla-releng/pushapkscript/commit/5b2258d529caf79b49aa4014fd77d1b39db9a571)|Merge pull request #64 from mitchhentges/59-schema-file-reference  Fixes #59, schema_file no longer recommended in config|mitchhentges|Placeholder|2018-12-21 17:06:40|

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/shipitscript/commit/b7762c589dde16808d83296009f017010264839f)|Merge pull request #19 from mitchhentges/release-3.1.0  3.1.0|mitchhentges|Placeholder|2019-01-03 19:56:09|
|[Link](https://github.com/mozilla-releng/shipitscript/commit/e1019db21833ca4356101436c6cf4d50d37ac81f)|3.1.0|mitchhentges|Placeholder|2019-01-02 18:11:03|
|[Link](https://github.com/mozilla-releng/shipitscript/commit/af894d0590b12b0b5b76f7e2285eeeef69c5ef30)|Merge pull request #18 from mitchhentges/remove-schema-from-config  Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2019-01-02 17:11:44|
|[Link](https://github.com/mozilla-releng/shipitscript/commit/456ce8f3797c22f4a449baa4db76c11b7cd86fa7)|Removes task schema from example config, adds to default config|mitchhentges|Placeholder|2018-12-24 21:37:25|
|[Link](https://github.com/mozilla-releng/shipitscript/commit/7c5698e73369eaaadeb03e17ab763e3635d7f47f)|Merge pull request #17 from garbas/fix-default-nix-argument  nix: use pkgs as a parameter, use layered docker image|rail|Placeholder|2018-12-11 14:08:55|

|	signingscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 

|	taskcluster-auth	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-auth.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/20c5209b7f570dc85949002127a5c11e8144fe15)|Repository is archived and moved to monorepo|djmitche|Placeholder|2019-01-04 20:22:38|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/d3ab1cab41d2378aac46975005508fb1b907f14e)|Merge pull request #190 from djmitche/bug1515547  Bug 1515547 - rename webhooktunnel to websocktunnel|djmitche|Placeholder|2019-01-02 18:30:18|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/0ed7720082264fffa76b613de3bc18d888a8ae67)|Add listRoleIds() to paginate roles  (#189)    Add a listRoleIds endpoint      Fixed description in list-role-ids-response.yml      Return continuationToken only when limit is specified      Add tests      Improve tests and implement hashids      Add tests for invalid continuationToken|OjaswinM|Placeholder|2018-12-19 15:44:04|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/5077077f2e4094d22eef527dc9883cb8dffa387e)|Merge pull request #188 from djmitche/bug1510377  Bug 1510377 - use tc-lib-references to validate references|djmitche|Placeholder|2018-12-10 18:27:23|
|[Link](https://github.com/taskcluster/taskcluster-auth/commit/325de3bc38bed1b8800668f0eed6e0d2ec8b73e7)|Bug 1510377 - use tc-lib-references to validate references|djmitche|Placeholder|2018-12-06 00:00:09|

|	taskcluster-queue	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster-queue.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/eb6efaa57b1f7fb2181a8f56124f98579998d151)|Repository is archived and moved to monorepo|djmitche|Placeholder|2019-01-04 20:15:47|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/84a800f5f7ad0a3c154eafa6a29b61b32fdef5e3)|Merge pull request #310 from taskcluster/more-monorepo-fixes  More monorepo fixes|imbstack|Placeholder|2019-01-03 18:49:28|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/4f4f0ec844a31e5ad0580e2a8dfc76d68fe7be64)|Merge pull request #308 from djmitche/superagent-dep  Superagent is a production dep, for ec2regionresolver.js|djmitche|Placeholder|2019-01-03 18:46:09|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/5f9ccb77b47861769fe420d5e16eaa656a571920)|Update aws-sdk to get more recent xml2js|imbstack|Placeholder|2019-01-02 01:20:20|
|[Link](https://github.com/taskcluster/taskcluster-queue/commit/c16f6e9cf3591285f199d96a9c0fa6873bbeb008)|Update azure-storage|imbstack|Placeholder|2019-01-02 01:18:13|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
