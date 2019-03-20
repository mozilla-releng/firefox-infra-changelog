##  Commits in production - for 3 days, generated on: 2019-03-20 07:13:13 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=708979f9c3f3)|[Bug 1535355 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535355) - Add clang-tidy & clang-format in CI for code-review, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D23524|babadie@mozilla.com|ahal|2019-03-20 08:26:10|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=13e9a230eb25)|[Bug 1246594 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1246594) - Enable ESLint rule no-throw-literal by default. r=Standard8 Differential Revision: https://phabricator.services.mozilla.com/D24088|mbanner@mozilla.com|Standard8|2019-03-20 00:27:55|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f45661298ac3)|[Bug 1535417 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535417) - Set dynamic mozinfo fields in Android test-verify; r=bc In the mochitest harness, is_fennec is populated by examining harness options, and is_emulator and android_version are populated by examining the device via mozdevice. The per-test code doesn't have those options and the emulator may not be available yet, so I've opted for populated those fields from mozharness configuration. In practice, we only run Android TV on Android 4.3, where is_fennec=True, is_emulator=True, and android_version=18. I'd like to run TV on Android 7.0/geckoview eventually, where is_fennec=False, is_emulator=True, and android_version=24. Since I was here, I also removed 'stylo' from the per-test mozinfo, since that field is obsolete now. Differential Revision: https://phabricator.services.mozilla.com/D23595|gbrown@mozilla.com|bc|2019-03-19 20:25:13|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=85bd45178007)|[Bug 1519851 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519851) - Create --enable-fuzzing debug build job for MacOSX. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D19862|ccoroiu@mozilla.com|dustin|2019-03-19 19:25:18|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e16d27f25d45)|[Bug 1535011 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535011) update `versioncontrol.rst` r=dustin Small updates to the version control documents regarding upgrading `robustcheckout.py`. I noticed that we still reference `build-puppet` from it's former home on hgmo and don't include OpenCloudConfig in our list of places we need to vendor `robustcheckout` changes. Differential Revision: https://phabricator.services.mozilla.com/D23742|cosheehan@mozilla.com|dustin|2019-03-18 19:59:44|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=551c42866143)|[Bug 1535016 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535016) - Don't treat any Android job as new job r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23674|igoldan@mozilla.com|jmaher|2019-03-18 14:36:33|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cee5e58bcf61)|[Bug 1534956 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534956) - Add Cristiano's facebook page to tp6-m r=Bebe Differential Revision: https://phabricator.services.mozilla.com/D23317|dhunt@mozilla.com|Bebe|2019-03-18 13:28:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d35d63ce1957)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D23832|sfraser@mozilla.com|sfraser|2019-03-18 13:04:22|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=85bd45178007)|[Bug 1519851 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519851) - Create --enable-fuzzing debug build job for MacOSX. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D19862|rmaries@mozilla.com|dustin|2019-03-20 00:11:19|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=85bd45178007)|[Bug 1519851 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519851) - Create --enable-fuzzing debug build job for MacOSX. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D19862|rmaries@mozilla.com|dustin|2019-03-19 23:51:47|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d35d63ce1957)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D23832|rgurzau@mozilla.com|sfraser|2019-03-18 23:36:40|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cee5e58bcf61)|[Bug 1534956 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534956) - Add Cristiano's facebook page to tp6-m r=Bebe Differential Revision: https://phabricator.services.mozilla.com/D23317|rgurzau@mozilla.com|Bebe|2019-03-18 23:36:40|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=551c42866143)|[Bug 1535016 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535016) - Don't treat any Android job as new job r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23674|rgurzau@mozilla.com|jmaher|2019-03-18 23:36:40|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c1674c1e4e7c)|[Bug 1535011 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535011) vendor latest `robustcheckout` from version-control-tools r=Callek This commit vendors `robustcheckout` from the version-control-tools repository, revision 8e3bb142dfa9. Differential Revision: https://phabricator.services.mozilla.com/D23566|aciure@mozilla.com|Callek|2019-03-17 11:42:17|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7e14986df45a)|[Bug 1533133 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533133) - Split up macOS JIT tests in more chunks. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23116|aciure@mozilla.com|jmaher|2019-03-17 11:42:17|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2ce6dd37ff59)|[Bug 1535016 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535016) - Don't treat any Android job as new job r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23674|aciure@mozilla.com|jmaher|2019-03-17 11:42:17|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=9a96eceffaee)|[Bug 1535580 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535580) - update linux/mac searchfox jobs for clang changes; r=kats We need to install a new enough binutils for both of these jobs and ensure that it's properly found on the linux job. Differential Revision: https://phabricator.services.mozilla.com/D23678|aciure@mozilla.com|kats|2019-03-17 11:42:17|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=de3d7088cbc5)|Backed out changeset 2ce6dd37ff59 (bug 1535016) for mozlint failure on taskcluster/taskgraph/util/seta.py CLOSED TREE|aciure@mozilla.com||2019-03-17 11:42:17|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=893781729409)|[Bug 1534737 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534737) use new tooltool packages with updates to adb r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D23534|aciure@mozilla.com|gbrown|2019-03-17 11:42:17|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=a1d4c53a4b80)|[Bug 1527206 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527206) - roll-out declarative artifacts for Fennec beta and release. r=sfraser a=release|mtabara@mozilla.com|sfraser|2019-03-19 00:10:25|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/50c33007df4dfc3b8149f2fbcc39e6d00b815b9e)|Bug 1533791 - Bump scriptworker to 22.1.0 (#432)|JohanLorenzo|N/A|2019-03-19 12:28:46|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/a4416687b6fdf1988491ade1cb1dbe52f6434fad)|Merge pull request #431 from escapewindow/bump-slugid  bump slugid+taskcluster|escapewindow|N/A|2019-03-19 00:21:13|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/814aad825d73e9d664b1b764f4dd8cdcb025bc6f)|Merge pull request #461 from taskcluster/bug1533591-tf  Bug 1533591 - set WEBSOCKTUNNEL_SECRET and expose as output|djmitche|N/A|2019-03-19 16:52:22|
|[Link](https://github.com/taskcluster/taskcluster/commit/8b77ccceb545211355a3cbd2d6482fc8a3b5b734)|Merge pull request #467 from djmitche/bug1536435  Bug 1536435 - support linked identities|djmitche|N/A|2019-03-19 16:35:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/42f09baa5cd5a17828ed4460040b040f99d2a5c6)|Merge pull request #464 from djmitche/restrict-wst-client-id  Restrict the allowable charcters for wstClient|djmitche|N/A|2019-03-19 15:44:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/490e42b07da287062f215fdd3d51cc906c834352)|Merge pull request #451 from taskcluster/apologies  Fix my wrong review|imbstack|N/A|2019-03-19 15:42:54|
|[Link](https://github.com/taskcluster/taskcluster/commit/e34e6e40208f797e689aed78b8846b567e8395ad)|Bug 1536435 - support linked identities  Now that we link identities, the format of the `identities` property has changed, invalidating some assumptions.  Happily those assumptions were represented with assertions so we got errors instead of undefined behavior!  In particular, an account with a github identity now has an identity like:  ```     {       "provider": "github",       "connection": "github",       "profileData": {         "userId": 1234,         "nickname": "developer1234"       }     }, ```  and an account with a firefoxaccounts sign-in has  ```     {       "profileData": {         "email": "foo@bar.com",         "fxa_sub": "97ff4ba365255c2a92d362ea017baa15",         ...       },       "provider": "oauth2",       "user_id": "firefoxaccounts|97ff4ba365255c2a92d362ea017baa15",       "connection": "firefoxaccounts",       "isSocial": true     } ```|djmitche|N/A|2019-03-19 14:44:57|
|[Link](https://github.com/taskcluster/taskcluster/commit/a6939bf2add7110531a1c23dbfcfdc2a2f3a1899)|client-web: bump version|helfi92|N/A|2019-03-19 13:44:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/2afacb0d9f74300cfff15f485e44459a28dc6b51)|Merge pull request #445 from helfi92/client-web-neutrino-v9  client-web neutrino v9, esm output, share linting|helfi92|N/A|2019-03-19 13:31:02|
|[Link](https://github.com/taskcluster/taskcluster/commit/9971f02dbaafeda1bc292bf0d36f8f994cf719ff)|Add requested changes|helfi92|N/A|2019-03-18 15:58:49|
|[Link](https://github.com/taskcluster/taskcluster/commit/6aa43f2ce1a6e0f3f19e7766a0b4da01dc12b334)|Nit: .taskcluster.yml|helfi92|N/A|2019-03-18 15:57:36|
|[Link](https://github.com/taskcluster/taskcluster/commit/f1d03671b9f632745e568f7a60d7c9380d29f0f9)|Merge pull request #465 from taskcluster/all-contributors/add-djmitche  docs: add contributors|djmitche|N/A|2019-03-19 12:44:50|
|[Link](https://github.com/taskcluster/taskcluster/commit/1ef077eafa5103ece64a783081f1aae1a32454af)|Fix weird focus state in task group view (FF only) (#455)|helfi92|N/A|2019-03-18 17:55:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/eaec8042dce5b572a0dfe91c4b99fd3061fae3ca)|Merge pull request #436 from taskcluster/update-config  Simplify lib-config|djmitche|N/A|2019-03-18 17:13:47|
|[Link](https://github.com/taskcluster/taskcluster/commit/4ff92aae900479c4676ee72adb43d75a71a71f47)|Merge pull request #452 from taskcluster/one-more-gitversion-fix  Add gitversion to root as well|djmitche|N/A|2019-03-18 17:13:24|
|[Link](https://github.com/taskcluster/taskcluster/commit/e78a1ae35381b558fac539375121843c0f73e898)|Merge pull request #172 from taskcluster/bug1524187  Bug 1524187 - Internal Server Errors when calling queue.completeArtifact|djmitche|N/A|2019-03-18 17:12:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/e5bbac637806fcd917c154409c8728780e6e629f)|Add title back to every docs page (#454)|littlebobby|N/A|2019-03-18 13:42:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/5a81a00711383d0089e5fda0d1a5bea275fe24ee)|Update dependency dotenv to v7 (#457)|renovate[bot]|N/A|2019-03-18 13:04:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/ccbceea0f806aadad7741289033bf25892d1c8e5)|Update dependency dotenv-cli to v2 (#458)|renovate[bot]|N/A|2019-03-18 13:03:30|
|[Link](https://github.com/taskcluster/taskcluster/commit/d6cdebccf30b7970b5c17afcc4bd9fac68b4c835)|Merge pull request #456 from taskcluster/renovate/eslint-5.x  Update dependency eslint to v5.15.2|djmitche|N/A|2019-03-18 12:32:17|

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
|[Link](https://github.com/mozilla-releng/scriptworker/commit/6c3698449ec5ae8ca363862d41c4a370cd101912)|22.1.0|JohanLorenzo|N/A|2019-03-19 10:43:07|
|[Link](https://github.com/mozilla-releng/scriptworker/commit/30a54b0c8092698f23b570cf81560f8e1af3322c)|Bug 1533791 - Support "assume" scopes|JohanLorenzo|N/A|2019-03-18 17:55:11|

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
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)|FIC - BOT|Self Generated| - |

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
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=8980c7a103df)|[Bug 1471367 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1471367) - add subcommand to print taskcluster.yml hashes r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22358|dmitchell@mozilla.com|dustin|2019-03-17 15:28:56|
