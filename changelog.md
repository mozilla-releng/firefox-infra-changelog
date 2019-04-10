##  Commits in production - for 3 days, generated on: 2019-04-10 10:39:33 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ca42d5764b08)|[Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  - Elevate the new debugger one directory. r=jlast|nbeleuzu@mozilla.com|jlast|2019-04-10 01:27:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=86b54cfca31f)|Backed out changeset ca42d5764b08 [Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  for failures in browser_dbg_worker-console-04.js|nbeleuzu@mozilla.com||2019-04-10 01:27:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e9408a26af67)|[Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  - Elevate the new debugger one directory. r=jlast|nbeleuzu@mozilla.com|jlast|2019-04-10 01:27:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=82054c3d9cad)|[Bug 1541955](https://bugzilla.mozilla.org/show_bug.cgi?id=1541955)  Update Android 7.0 emulator r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D26383|gbrown@mozilla.com|gbrown|2019-04-09 23:48:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=17b96c33164e)|[Bug 1542707](https://bugzilla.mozilla.org/show_bug.cgi?id=1542707)  - Don't replace 'nightly' jobs with artifact builds on try. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D26658|cmanchester@mozilla.com|glandium|2019-04-09 20:09:02|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3b10487587c3)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Package mar and mbsdiff as a toolchain; r=glandium Differential Revision: https://phabricator.services.mozilla.com/D24229|mozilla@hocat.ca|glandium|2019-04-09 19:51:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cc06a7beb3d1)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Make linux64-upx toolchain tier 1; r=glandium This also switches it to use the generic toolchain build image, as it is no longer being used exclusively by mingw builds. Differential Revision: https://phabricator.services.mozilla.com/D24230|mozilla@hocat.ca|glandium|2019-04-09 19:51:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f7791b680d46)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Update linux-upx to 3.9.5; r=glandium This matches the version that exists in mozilla-build (see [Bug 1501403](https://bugzilla.mozilla.org/show_bug.cgi?id=1501403)  Differential Revision: https://phabricator.services.mozilla.com/D26413|mozilla@hocat.ca|glandium|2019-04-09 19:51:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=09338587b68e)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Repackage windows builds on linux. r=glandium,Callek This only uses cross-platform tools, so switch to running these on linux, which cuts the runtime down from ~20m to ~3m. Differential Revision: https://phabricator.services.mozilla.com/D1080|mozilla@hocat.ca|glandium,Callek|2019-04-09 19:51:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b979e271d955)|[Bug 1540152](https://bugzilla.mozilla.org/show_bug.cgi?id=1540152)  - Run checks done in push-apk in promote-phase, instead of the very last task of the pipeline r=mtabara Run checks done in push-apk in promote-phase, instead of the very last task of the pipeline Differential Revision: https://phabricator.services.mozilla.com/D26328|jlorenzo@mozilla.com|mtabara|2019-04-09 17:59:40|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a024c4370f28)|[Bug 1541917](https://bugzilla.mozilla.org/show_bug.cgi?id=1541917)  - Mac Talos tests are running on every push to integration branches. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D26265|jwood@mozilla.com|jmaher|2019-04-09 15:21:13|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=21e7aa527584)|[Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  - Elevate the new debugger one directory. r=jlast|nerli@mozilla.com|jlast|2019-04-09 13:01:41|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=db09a6f1febb)|Backed out changeset 21e7aa527584 [Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  for debugger, clipboard and dt failures on a CLOSED TREE|nerli@mozilla.com||2019-04-09 13:01:41|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5cc56532ff4a)|Merge mozilla-central to mozilla-inbound. a=merge on a CLOSED TREE|nerli@mozilla.com|merge|2019-04-09 13:01:41|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f6bf51e87b1a)|[Bug 1534647](https://bugzilla.mozilla.org/show_bug.cgi?id=1534647)  - Switch python3 version to 3.6 on osx hosts; r=ahal Quick fix for python3 mozbase perma-fail on osx: Use python 3.6 explicitly, rather than the system default 3.7, which appears to be broken currently (lacking ssl support). Differential Revision: https://phabricator.services.mozilla.com/D26345|gbrown@mozilla.com|ahal|2019-04-08 23:05:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0fbc141c1004)|[Bug 1542824](https://bugzilla.mozilla.org/show_bug.cgi?id=1542824)  - [Coverity] Limit Coverity to run only on try. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26571|bpostelnicu@mozilla.com|bastien|2019-04-08 23:04:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=390bf9dcba1a)|[Bug 1532545](https://bugzilla.mozilla.org/show_bug.cgi?id=1532545)  Add support for running page load tests against Fennec r=rwood Differential Revision: https://phabricator.services.mozilla.com/D25723|dhunt@mozilla.com|rwood|2019-04-08 21:33:36|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d689bb3db16e)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [tryselect] Extend test_mozharness_integration.py to include the 'android_emulator_unittest' script, r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D26133|ahalberstadt@mozilla.com|gbrown|2019-04-08 17:36:06|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b306079acdcb)|[Bug 1541693](https://bugzilla.mozilla.org/show_bug.cgi?id=1541693)  Stop marking releases as started r=mtabara Ship-it v1 is going away soon and we won't need to create new releases in Ship-it v1 in parallel with Ship-it v2. It's time to prep patches to remove this functionality. Differential Revision: https://phabricator.services.mozilla.com/D26044|raliiev@mozilla.com|mtabara|2019-04-08 17:15:33|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=248454418988)|Backed out changeset 7e2aef09165a [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  on request by Andy|ccoroiu@mozilla.com||2019-04-08 13:25:05|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7e2aef09165a)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|bpostelnicu@mozilla.com|bastien|2019-04-08 13:16:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c9d95a544902)|[Bug 1503453](https://bugzilla.mozilla.org/show_bug.cgi?id=1503453)  - Temporarily disable permafailing Windows static analysis builds: Add one more whitespace because the linting gods demand this. a=permafail CLOSED TREE|archaeopteryx@coole-files.de|permafail|2019-04-08 11:14:28|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=13b40bbdb45c)|[Bug 1503453](https://bugzilla.mozilla.org/show_bug.cgi?id=1503453)  - Temporarily disable permafailing Windows static analysis builds. a=permafail|archaeopteryx@coole-files.de|permafail|2019-04-08 10:55:34|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a024c4370f28)|[Bug 1541917](https://bugzilla.mozilla.org/show_bug.cgi?id=1541917)  - Mac Talos tests are running on every push to integration branches. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D26265|nbeleuzu@mozilla.com|jmaher|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3b8444793f55)|[Bug 1436457](https://bugzilla.mozilla.org/show_bug.cgi?id=1436457)  - Add a group policy file to disable app updates, as those are handled by snapd. r=jlorenzo,mkaply Differential Revision: https://phabricator.services.mozilla.com/D26281|nbeleuzu@mozilla.com|jlorenzo,mkaply|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b979e271d955)|[Bug 1540152](https://bugzilla.mozilla.org/show_bug.cgi?id=1540152)  - Run checks done in push-apk in promote-phase, instead of the very last task of the pipeline r=mtabara Run checks done in push-apk in promote-phase, instead of the very last task of the pipeline Differential Revision: https://phabricator.services.mozilla.com/D26328|nbeleuzu@mozilla.com|mtabara|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=20c86313e332)|[Bug 1542242](https://bugzilla.mozilla.org/show_bug.cgi?id=1542242)  - [taskgraph] Hack required mozbase module onto PYTHONPATH rather than run 'mach python' for Windows builds, r=marco This is a hack to get around Windows ccov build hangs caused by [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  [Bug 1543149](https://bugzilla.mozilla.org/show_bug.cgi?id=1543149)  will track the investigation of the hang and removal of this hack. Differential Revision: https://phabricator.services.mozilla.com/D26750|nbeleuzu@mozilla.com|marco|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3b10487587c3)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Package mar and mbsdiff as a toolchain; r=glandium Differential Revision: https://phabricator.services.mozilla.com/D24229|nbeleuzu@mozilla.com|glandium|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=cc06a7beb3d1)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Make linux64-upx toolchain tier 1; r=glandium This also switches it to use the generic toolchain build image, as it is no longer being used exclusively by mingw builds. Differential Revision: https://phabricator.services.mozilla.com/D24230|nbeleuzu@mozilla.com|glandium|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f7791b680d46)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Update linux-upx to 3.9.5; r=glandium This matches the version that exists in mozilla-build (see [Bug 1501403](https://bugzilla.mozilla.org/show_bug.cgi?id=1501403)  Differential Revision: https://phabricator.services.mozilla.com/D26413|nbeleuzu@mozilla.com|glandium|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=09338587b68e)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Repackage windows builds on linux. r=glandium,Callek This only uses cross-platform tools, so switch to running these on linux, which cuts the runtime down from ~20m to ~3m. Differential Revision: https://phabricator.services.mozilla.com/D1080|nbeleuzu@mozilla.com|glandium,Callek|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=17b96c33164e)|[Bug 1542707](https://bugzilla.mozilla.org/show_bug.cgi?id=1542707)  - Don't replace 'nightly' jobs with artifact builds on try. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D26658|nbeleuzu@mozilla.com|glandium|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d6bbb316b768)|Merge mozilla-central to inbound. a=merge CLOSED TREE|nbeleuzu@mozilla.com|merge|2019-04-10 01:28:41|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e9408a26af67)|[Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  - Elevate the new debugger one directory. r=jlast|jlaster@mozilla.com|jlast|2019-04-09 20:17:16|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ca42d5764b08)|[Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  - Elevate the new debugger one directory. r=jlast|jlaster@mozilla.com|jlast|2019-04-09 17:31:57|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b306079acdcb)|[Bug 1541693](https://bugzilla.mozilla.org/show_bug.cgi?id=1541693)  Stop marking releases as started r=mtabara Ship-it v1 is going away soon and we won't need to create new releases in Ship-it v1 in parallel with Ship-it v2. It's time to prep patches to remove this functionality. Differential Revision: https://phabricator.services.mozilla.com/D26044|rmaries@mozilla.com|mtabara|2019-04-09 00:03:16|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d689bb3db16e)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [tryselect] Extend test_mozharness_integration.py to include the 'android_emulator_unittest' script, r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D26133|rmaries@mozilla.com|gbrown|2019-04-09 00:03:16|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=390bf9dcba1a)|[Bug 1532545](https://bugzilla.mozilla.org/show_bug.cgi?id=1532545)  Add support for running page load tests against Fennec r=rwood Differential Revision: https://phabricator.services.mozilla.com/D25723|rmaries@mozilla.com|rwood|2019-04-09 00:03:16|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5cc56532ff4a)|Merge mozilla-central to mozilla-inbound. a=merge on a CLOSED TREE|rmaries@mozilla.com|merge|2019-04-09 00:03:16|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=db09a6f1febb)|Backed out changeset 21e7aa527584 [Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  for debugger, clipboard and dt failures on a CLOSED TREE|apavel@mozilla.com||2019-04-08 23:16:21|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=21e7aa527584)|[Bug 1500987](https://bugzilla.mozilla.org/show_bug.cgi?id=1500987)  - Elevate the new debugger one directory. r=jlast|jlaster@mozilla.com|jlast|2019-04-08 22:12:20|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7e2aef09165a)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|dvarga@mozilla.com|bastien|2019-04-08 19:30:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=248454418988)|Backed out changeset 7e2aef09165a [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  on request by Andy|dvarga@mozilla.com||2019-04-08 19:30:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=674a4d255565)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|dvarga@mozilla.com|bastien|2019-04-08 19:30:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8b80520b0ca7)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D26482|dvarga@mozilla.com|sfraser|2019-04-08 19:30:07|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d6bbb316b768)|Merge mozilla-central to inbound. a=merge CLOSED TREE|ncsoregi@mozilla.com|merge|2019-04-10 13:00:20|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=82054c3d9cad)|[Bug 1541955](https://bugzilla.mozilla.org/show_bug.cgi?id=1541955)  Update Android 7.0 emulator r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D26383|ncsoregi@mozilla.com|gbrown|2019-04-10 12:58:56|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a024c4370f28)|[Bug 1541917](https://bugzilla.mozilla.org/show_bug.cgi?id=1541917)  - Mac Talos tests are running on every push to integration branches. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D26265|nbeleuzu@mozilla.com|jmaher|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3b8444793f55)|[Bug 1436457](https://bugzilla.mozilla.org/show_bug.cgi?id=1436457)  - Add a group policy file to disable app updates, as those are handled by snapd. r=jlorenzo,mkaply Differential Revision: https://phabricator.services.mozilla.com/D26281|nbeleuzu@mozilla.com|jlorenzo,mkaply|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b979e271d955)|[Bug 1540152](https://bugzilla.mozilla.org/show_bug.cgi?id=1540152)  - Run checks done in push-apk in promote-phase, instead of the very last task of the pipeline r=mtabara Run checks done in push-apk in promote-phase, instead of the very last task of the pipeline Differential Revision: https://phabricator.services.mozilla.com/D26328|nbeleuzu@mozilla.com|mtabara|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=20c86313e332)|[Bug 1542242](https://bugzilla.mozilla.org/show_bug.cgi?id=1542242)  - [taskgraph] Hack required mozbase module onto PYTHONPATH rather than run 'mach python' for Windows builds, r=marco This is a hack to get around Windows ccov build hangs caused by [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  [Bug 1543149](https://bugzilla.mozilla.org/show_bug.cgi?id=1543149)  will track the investigation of the hang and removal of this hack. Differential Revision: https://phabricator.services.mozilla.com/D26750|nbeleuzu@mozilla.com|marco|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3b10487587c3)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Package mar and mbsdiff as a toolchain; r=glandium Differential Revision: https://phabricator.services.mozilla.com/D24229|nbeleuzu@mozilla.com|glandium|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cc06a7beb3d1)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Make linux64-upx toolchain tier 1; r=glandium This also switches it to use the generic toolchain build image, as it is no longer being used exclusively by mingw builds. Differential Revision: https://phabricator.services.mozilla.com/D24230|nbeleuzu@mozilla.com|glandium|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f7791b680d46)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Update linux-upx to 3.9.5; r=glandium This matches the version that exists in mozilla-build (see [Bug 1501403](https://bugzilla.mozilla.org/show_bug.cgi?id=1501403)  Differential Revision: https://phabricator.services.mozilla.com/D26413|nbeleuzu@mozilla.com|glandium|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=09338587b68e)|[Bug 1458385](https://bugzilla.mozilla.org/show_bug.cgi?id=1458385)  Repackage windows builds on linux. r=glandium,Callek This only uses cross-platform tools, so switch to running these on linux, which cuts the runtime down from ~20m to ~3m. Differential Revision: https://phabricator.services.mozilla.com/D1080|nbeleuzu@mozilla.com|glandium,Callek|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=17b96c33164e)|[Bug 1542707](https://bugzilla.mozilla.org/show_bug.cgi?id=1542707)  - Don't replace 'nightly' jobs with artifact builds on try. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D26658|nbeleuzu@mozilla.com|glandium|2019-04-10 01:08:13|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e6d48028244b)|[Bug 1540907](https://bugzilla.mozilla.org/show_bug.cgi?id=1540907)  - Bump MinGW version to pick up MFVideoTransferMatrix constants r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D26530|nerli@mozilla.com|froydnj|2019-04-09 12:54:40|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b306079acdcb)|[Bug 1541693](https://bugzilla.mozilla.org/show_bug.cgi?id=1541693)  Stop marking releases as started r=mtabara Ship-it v1 is going away soon and we won't need to create new releases in Ship-it v1 in parallel with Ship-it v2. It's time to prep patches to remove this functionality. Differential Revision: https://phabricator.services.mozilla.com/D26044|aciure@mozilla.com|mtabara|2019-04-08 22:00:29|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d689bb3db16e)|[Bug 1523303](https://bugzilla.mozilla.org/show_bug.cgi?id=1523303)  - [tryselect] Extend test_mozharness_integration.py to include the 'android_emulator_unittest' script, r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D26133|aciure@mozilla.com|gbrown|2019-04-08 22:00:29|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=390bf9dcba1a)|[Bug 1532545](https://bugzilla.mozilla.org/show_bug.cgi?id=1532545)  Add support for running page load tests against Fennec r=rwood Differential Revision: https://phabricator.services.mozilla.com/D25723|aciure@mozilla.com|rwood|2019-04-08 22:00:29|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7e2aef09165a)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|dvarga@mozilla.com|bastien|2019-04-08 19:16:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=248454418988)|Backed out changeset 7e2aef09165a [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  on request by Andy|dvarga@mozilla.com||2019-04-08 19:16:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=674a4d255565)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|dvarga@mozilla.com|bastien|2019-04-08 19:16:26|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8b80520b0ca7)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D26482|dvarga@mozilla.com|sfraser|2019-04-08 19:16:26|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=2a4306fc8442)|[Bug 1541693](https://bugzilla.mozilla.org/show_bug.cgi?id=1541693)  Stop marking releases as started r=mtabara a=release Ship-it v1 is going away soon and we won't need to create new releases in Ship-it v1 in parallel with Ship-it v2. It's time to prep patches to remove this functionality. Differential Revision: https://phabricator.services.mozilla.com/D26044|raliiev@mozilla.com|mtabara|2019-04-09 04:47:53|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=9bae80c354eb)|[Bug 1540262](https://bugzilla.mozilla.org/show_bug.cgi?id=1540262)  - increase UV chunks from 12 to 16, NPOTB DONTBUILD r=tomprince, a=testing Differential Revision: https://phabricator.services.mozilla.com/D25673|jlund@mozilla.com|tomprince,|2019-04-08 22:17:21|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=f3f3f82b2d8b)|[Bug 1529948](https://bugzilla.mozilla.org/show_bug.cgi?id=1529948)  Switch default for actions from `task` to `hook`; r=Callek a=release Support for `kind='task'` is still around to support Thunderbird release promotion, which uses releaserunner3. Other actions shouldn't be using it. Differential Revision: https://phabricator.services.mozilla.com/D20842|asasaki@mozilla.com|Callek|2019-04-09 23:24:11|

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/c6173db2f17c35e81ac63e62735bb9aded5c3fc7)|Update shipitscript to stop handling shipit v1 (#447)|rail|N/A|2019-04-09 14:17:27|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/d78f3680c1fd6ef0be2d8c5c79993625d49a7a0c)|Merge pull request #445 from srfraser/bug_1542500_beetmover_bump  Bug 1542500 bump beetmover version|srfraser|N/A|2019-04-08 13:51:53|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/bbb291789b7732de1739c40546b0405555b826fd)|Bug 1542500 bump beetmover version|srfraser|N/A|2019-04-08 13:36:17|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/2f86f676007e49c2b92201104b02cc37b2e976a3)|Testing generic-worker 14.0.2 / taskcluster-proxy 5.1.0 on  STAGING   This change does _not_ affect any production workers. Commit made with:      ./gecko-try.sh 14.0.2 5.1.0  See https://github.com/taskcluster/generic-worker/blob/3a55d5bc23974e00372ae67cd1f632a4fe92301c/mozilla-try-scripts/gecko-try.sh  deploy: gecko-1-b-win2012-beta gecko-t-win10-64-beta gecko-t-win10-64-cu gecko-t-win10-64-gpu-b gecko-t-win10-64-hw-b gecko-t-win10-64-ux-b gecko-t-win10-a64-beta gecko-t-win7-32-beta gecko-t-win7-32-cu gecko-t-win7-32-gpu-b|petemoore|N/A|2019-04-09 16:27:55|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/83039fa1108d302a1187fe29f3a38917fd8e97a6)|Remove openpgpSigningKeyLocation config setting from generic-worker 14.0.1 workers  deploy:gecko-1-b-win2012-beta gecko-t-win10-64-beta gecko-t-win10-64-cu gecko-t-win10-64-gpu-b gecko-t-win10-64-hw-b gecko-t-win10-64-ux-b gecko-t-win10-a64-beta gecko-t-win7-32-beta gecko-t-win7-32-cu gecko-t-win7-32-gpu-b|petemoore|N/A|2019-04-09 05:33:06|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/f8cf39be79842ada5b2b0e15e5b1ae938ef53d31)|Testing generic-worker 14.0.1 / taskcluster-proxy 5.1.0 on  STAGING   This change does _not_ affect any production workers. Commit made with:      ./gecko-try.sh 14.0.1 5.1.0  See https://github.com/taskcluster/generic-worker/blob/d6198468456a3af8b90265d62eb0b10cc19cbba3/mozilla-try-scripts/gecko-try.sh  deploy: gecko-1-b-win2012-beta gecko-t-win10-64-beta gecko-t-win10-64-cu gecko-t-win10-64-gpu-b gecko-t-win10-64-hw-b gecko-t-win10-64-ux-b gecko-t-win10-a64-beta gecko-t-win7-32-beta gecko-t-win7-32-cu gecko-t-win7-32-gpu-b|petemoore|N/A|2019-04-08 17:15:02|

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/767c510bd178586b599b5d2d989de2342bc0b425)|Merge pull request #540 from taskcluster/not-reported-to-sentry  remove now-redundant-and-incorrect logging about error|djmitche|N/A|2019-04-09 18:49:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/5cf7005f53d41c6b5a8a1e85130389fdd3542dde)|Merge pull request #555 from djmitche/use-index-for-libraries  rename libraries' index files to index.js|djmitche|N/A|2019-04-09 15:12:55|

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
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=f8735bbb7de9)|[Bug 1514903](https://bugzilla.mozilla.org/show_bug.cgi?id=1514903)  - add dep-iscript to level 1 r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D26385|asasaki@mozilla.com|tomprince|2019-04-08 22:43:15|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=ee754847e3c8)|[Bug 1522225](https://bugzilla.mozilla.org/show_bug.cgi?id=1522225)  - part 1: Temporily allow reference-browser to schedule autophone tasks on PRs r=mhentges part 1: Temporily allow reference-browser to schedule autophone tasks on PRs Differential Revision: https://phabricator.services.mozilla.com/D26525|jlorenzo@mozilla.com|mhentges|2019-04-08 17:19:39|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=99bb5249719c)|[Bug 1542697](https://bugzilla.mozilla.org/show_bug.cgi?id=1542697)  - Add secret project/relman/coverity to L1, L2 and L3 access. r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D26478|jlorenzo@mozilla.com|jlorenzo|2019-04-08 12:18:53|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
