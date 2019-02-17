##  Commits in production - for one day, generated on: 2019-02-17 05:47:36 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=cdefcc66972a)|Bug 1527798 - Upgrade toolchain tasks using MSVC to 15.8.4. r=froydnj  It turns out version 15.4.2 spawns a vctip process that sticks after the build, and since bug 1527798, that breaks unmounting caches because the process has a handle on msvcp140.dll, which lies in the source directory. The problem goes away with 15.8.4, so upgrade all toolchain tasks to that.  That's the same version as we're using on x86/x86-64 MSVC builds.  Differential Revision: https://phabricator.services.mozilla.com/D19752 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1527e2d84ff9)|Bug 1527798 - Kill mspdbsrv at the end of gn build. r=froydnj  It keeps running and prevents the worker from unmounting, failing the task.  Differential Revision: https://phabricator.services.mozilla.com/D19910 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ac565cc75295)|Bug 1431523 - Use docker images for debian package tasks. r=dustin  We however leave moving the packages building to a script for another day.  Differential Revision: https://phabricator.services.mozilla.com/D19624|ccoroiu@mozilla.com|dustin|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0605b508a2c6)|Bug 1528150 - Build gn from https://gn.googlesource.com/gn/. r=froydnj  Make some adjustments to make the build work: - On Linux, a newer GCC is needed, and -lrt is missing for   clock_gettime. - On Mac, ninja expect AR be accept ar arguments, which clang doesn't,   so use llvm-ar. - On Windows, remove the /WX flag that upstream sets (warnings as   errors) because there _are_ warnings in the code, and remove the   explicit /MACHINE:x64 linker flag because we're building for x86.   (we could build for x64, but I'd rather leave that to a followup)  Differential Revision: https://phabricator.services.mozilla.com/D19911 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=02bef0e09a3c)|Backout changesets cdefcc66972a, 1527e2d84ff9 (bug 1527798), ac565cc75295 (bug 1431523) and 0605b508a2c6 (bug 1528150)  to give time to docker images and toolchains to build. |ccoroiu@mozilla.com||2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=09ba3e3539e8)|Bug 1527798 - Upgrade toolchain tasks using MSVC to 15.8.4. r=froydnj  It turns out version 15.4.2 spawns a vctip process that sticks after the build, and since bug 1527798, that breaks unmounting caches because the process has a handle on msvcp140.dll, which lies in the source directory. The problem goes away with 15.8.4, so upgrade all toolchain tasks to that.  That's the same version as we're using on x86/x86-64 MSVC builds.  Differential Revision: https://phabricator.services.mozilla.com/D19752 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=446683e9ed32)|Bug 1527798 - Kill mspdbsrv at the end of gn build. r=froydnj  It keeps running and prevents the worker from unmounting, failing the task.  Differential Revision: https://phabricator.services.mozilla.com/D19910 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=fd0b6ef065d0)|Bug 1431523 - Use docker images for debian package tasks. r=dustin  We however leave moving the packages building to a script for another day.  Differential Revision: https://phabricator.services.mozilla.com/D19624|ccoroiu@mozilla.com|dustin|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e7698adc8e90)|Bug 1528150 - Build gn from https://gn.googlesource.com/gn/. r=froydnj  Make some adjustments to make the build work: - On Linux, a newer GCC is needed, and -lrt is missing for   clock_gettime. - On Mac, ninja expect AR be accept ar arguments, which clang doesn't,   so use llvm-ar. - On Windows, remove the /WX flag that upstream sets (warnings as   errors) because there _are_ warnings in the code, and remove the   explicit /MACHINE:x64 linker flag because we're building for x86.   (we could build for x64, but I'd rather leave that to a followup)  Differential Revision: https://phabricator.services.mozilla.com/D19911 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d9b2f663c85b)|Bug 1528155 - Use sparse profiles in Windows toolchain tasks. r=tomprince  Also fix support_vcs_checkout call for docker-image based toolchain tasks.  Differential Revision: https://phabricator.services.mozilla.com/D19912 |ccoroiu@mozilla.com|tomprince|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c5cddbea80c9)|Backout changeset d9b2f663c85b (bug 1528155) to leave time to toolchain jobs to run. |ccoroiu@mozilla.com||2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7ab4a0c9980f)|Merge inbound to mozilla-central a=merge|ccoroiu@mozilla.com|merge|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=939d6ac72fed)|Merge mozilla-central to autoland a=merge|ccoroiu@mozilla.com|merge|2019-02-16 11:41:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0daaa7d0b092)|Bug 1528380 - Add nasm dependency to searchfox Windows jobs. r=TD-Linux  Differential Revision: https://phabricator.services.mozilla.com/D20003|kgupta@mozilla.com|TD-Linux|2019-02-16 22:07:28|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)|FIC - BOT|Self Generated| - |

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6fbfc8bc2388)|Bug 1522111 - disable opt builds/tests when we have pgo builds/tests for integration branches. r=ahal  Differential Revision: https://phabricator.services.mozilla.com/D18104|ccoroiu@mozilla.com|ahal|2019-02-16 11:36:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cc97d772a8db)|Bug 1522111 - Make -qr tests depend on -pgo where applicable, leaving old -qr sets in place. r=gbrown  Also set the run-on-projects for various tests to be central/try when opt  Differential Revision: https://phabricator.services.mozilla.com/D19742|ccoroiu@mozilla.com|gbrown|2019-02-16 11:36:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c10783ea070b)|Bug 1522111 - fix SETA to account for new tests, so we still filter them out even if SETA data doesn't include them. r=gbrown  Differential Revision: https://phabricator.services.mozilla.com/D19838|ccoroiu@mozilla.com|gbrown|2019-02-16 11:36:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=14e9ed41b8be)|Bug 1522111 - Make l10n kind depend on -pgo where available instead of opt. r=tomprince  This avoids opt being pulled in even when l10n is optimized out  Differential Revision: https://phabricator.services.mozilla.com/D19840|ccoroiu@mozilla.com|tomprince|2019-02-16 11:36:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b64fc884fc84)|Bug 1508379 Add BinAST version of Instagram to tp6 r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D18824|ccoroiu@mozilla.com|davehunt|2019-02-16 11:36:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=aa6103c8ef0f)|Bug 1522111 - Followup, ensure test sets align between opt and pgo. r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D19968|ccoroiu@mozilla.com|jmaher|2019-02-16 11:36:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6a145b0bf8e4)|Backed out 5 changesets (bug 1522111) for breaking windows opt wpts  Backed out changeset aa6103c8ef0f (bug 1522111) Backed out changeset 14e9ed41b8be (bug 1522111) Backed out changeset c10783ea070b (bug 1522111) Backed out changeset cc97d772a8db (bug 1522111) Backed out changeset 6fbfc8bc2388 (bug 1522111)|ccoroiu@mozilla.com||2019-02-16 11:36:04|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cdefcc66972a)|Bug 1527798 - Upgrade toolchain tasks using MSVC to 15.8.4. r=froydnj  It turns out version 15.4.2 spawns a vctip process that sticks after the build, and since bug 1527798, that breaks unmounting caches because the process has a handle on msvcp140.dll, which lies in the source directory. The problem goes away with 15.8.4, so upgrade all toolchain tasks to that.  That's the same version as we're using on x86/x86-64 MSVC builds.  Differential Revision: https://phabricator.services.mozilla.com/D19752 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1527e2d84ff9)|Bug 1527798 - Kill mspdbsrv at the end of gn build. r=froydnj  It keeps running and prevents the worker from unmounting, failing the task.  Differential Revision: https://phabricator.services.mozilla.com/D19910 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ac565cc75295)|Bug 1431523 - Use docker images for debian package tasks. r=dustin  We however leave moving the packages building to a script for another day.  Differential Revision: https://phabricator.services.mozilla.com/D19624|ccoroiu@mozilla.com|dustin|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0605b508a2c6)|Bug 1528150 - Build gn from https://gn.googlesource.com/gn/. r=froydnj  Make some adjustments to make the build work: - On Linux, a newer GCC is needed, and -lrt is missing for   clock_gettime. - On Mac, ninja expect AR be accept ar arguments, which clang doesn't,   so use llvm-ar. - On Windows, remove the /WX flag that upstream sets (warnings as   errors) because there _are_ warnings in the code, and remove the   explicit /MACHINE:x64 linker flag because we're building for x86.   (we could build for x64, but I'd rather leave that to a followup)  Differential Revision: https://phabricator.services.mozilla.com/D19911 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=02bef0e09a3c)|Backout changesets cdefcc66972a, 1527e2d84ff9 (bug 1527798), ac565cc75295 (bug 1431523) and 0605b508a2c6 (bug 1528150)  to give time to docker images and toolchains to build. |ccoroiu@mozilla.com||2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=09ba3e3539e8)|Bug 1527798 - Upgrade toolchain tasks using MSVC to 15.8.4. r=froydnj  It turns out version 15.4.2 spawns a vctip process that sticks after the build, and since bug 1527798, that breaks unmounting caches because the process has a handle on msvcp140.dll, which lies in the source directory. The problem goes away with 15.8.4, so upgrade all toolchain tasks to that.  That's the same version as we're using on x86/x86-64 MSVC builds.  Differential Revision: https://phabricator.services.mozilla.com/D19752 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=446683e9ed32)|Bug 1527798 - Kill mspdbsrv at the end of gn build. r=froydnj  It keeps running and prevents the worker from unmounting, failing the task.  Differential Revision: https://phabricator.services.mozilla.com/D19910 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=fd0b6ef065d0)|Bug 1431523 - Use docker images for debian package tasks. r=dustin  We however leave moving the packages building to a script for another day.  Differential Revision: https://phabricator.services.mozilla.com/D19624|ccoroiu@mozilla.com|dustin|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e7698adc8e90)|Bug 1528150 - Build gn from https://gn.googlesource.com/gn/. r=froydnj  Make some adjustments to make the build work: - On Linux, a newer GCC is needed, and -lrt is missing for   clock_gettime. - On Mac, ninja expect AR be accept ar arguments, which clang doesn't,   so use llvm-ar. - On Windows, remove the /WX flag that upstream sets (warnings as   errors) because there _are_ warnings in the code, and remove the   explicit /MACHINE:x64 linker flag because we're building for x86.   (we could build for x64, but I'd rather leave that to a followup)  Differential Revision: https://phabricator.services.mozilla.com/D19911 |ccoroiu@mozilla.com|froydnj|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d9b2f663c85b)|Bug 1528155 - Use sparse profiles in Windows toolchain tasks. r=tomprince  Also fix support_vcs_checkout call for docker-image based toolchain tasks.  Differential Revision: https://phabricator.services.mozilla.com/D19912 |ccoroiu@mozilla.com|tomprince|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c5cddbea80c9)|Backout changeset d9b2f663c85b (bug 1528155) to leave time to toolchain jobs to run. |ccoroiu@mozilla.com||2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7ab4a0c9980f)|Merge inbound to mozilla-central a=merge|ccoroiu@mozilla.com|merge|2019-02-16 11:37:16|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=939d6ac72fed)|Merge mozilla-central to autoland a=merge|ncsoregi@mozilla.com|merge|2019-02-16 23:45:13|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6fbfc8bc2388)|Bug 1522111 - disable opt builds/tests when we have pgo builds/tests for integration branches. r=ahal  Differential Revision: https://phabricator.services.mozilla.com/D18104|ccoroiu@mozilla.com|ahal|2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=cc97d772a8db)|Bug 1522111 - Make -qr tests depend on -pgo where applicable, leaving old -qr sets in place. r=gbrown  Also set the run-on-projects for various tests to be central/try when opt  Differential Revision: https://phabricator.services.mozilla.com/D19742|ccoroiu@mozilla.com|gbrown|2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c10783ea070b)|Bug 1522111 - fix SETA to account for new tests, so we still filter them out even if SETA data doesn't include them. r=gbrown  Differential Revision: https://phabricator.services.mozilla.com/D19838|ccoroiu@mozilla.com|gbrown|2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=14e9ed41b8be)|Bug 1522111 - Make l10n kind depend on -pgo where available instead of opt. r=tomprince  This avoids opt being pulled in even when l10n is optimized out  Differential Revision: https://phabricator.services.mozilla.com/D19840|ccoroiu@mozilla.com|tomprince|2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b64fc884fc84)|Bug 1508379 Add BinAST version of Instagram to tp6 r=davehunt  Differential Revision: https://phabricator.services.mozilla.com/D18824|ccoroiu@mozilla.com|davehunt|2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=aa6103c8ef0f)|Bug 1522111 - Followup, ensure test sets align between opt and pgo. r=jmaher  Differential Revision: https://phabricator.services.mozilla.com/D19968|ccoroiu@mozilla.com|jmaher|2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6a145b0bf8e4)|Backed out 5 changesets (bug 1522111) for breaking windows opt wpts  Backed out changeset aa6103c8ef0f (bug 1522111) Backed out changeset 14e9ed41b8be (bug 1522111) Backed out changeset c10783ea070b (bug 1522111) Backed out changeset cc97d772a8db (bug 1522111) Backed out changeset 6fbfc8bc2388 (bug 1522111)|ccoroiu@mozilla.com||2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7ab4a0c9980f)|Merge inbound to mozilla-central a=merge|ccoroiu@mozilla.com|merge|2019-02-16 11:42:42|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b759c45d1f01)|No bug - Disable caches on Windows toolchain tasks |mh@glandium.org||2019-02-16 13:32:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=834d38825814)|Bug 1528155 - Use sparse profiles in Windows toolchain tasks. r=tomprince  Also fix support_vcs_checkout call for docker-image based toolchain tasks.  Differential Revision: https://phabricator.services.mozilla.com/D19912 |mh@glandium.org|tomprince|2019-02-16 13:32:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d6a48567ce7f)|Backout changeset 834d38825814 (bug 1528155) and b759c45d1f01 to give time to toolchains to build. |mh@glandium.org||2019-02-16 13:36:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=939d6ac72fed)|Merge mozilla-central to autoland a=merge|ncsoregi@mozilla.com|merge|2019-02-17 00:14:37|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	addonscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/addonscript.md)|FIC - BOT|Self Generated| - |

|	balrogscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/balrogscript.md)|FIC - BOT|Self Generated| - |

|	beetmoverscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/beetmoverscript.md)|FIC - BOT|Self Generated| - |

|	bouncerscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/bouncerscript.md)|FIC - BOT|Self Generated| - |

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)|FIC - BOT|Self Generated| - |

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)|FIC - BOT|Self Generated| - |

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)|FIC - BOT|Self Generated| - |

|	services	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/services.md)|FIC - BOT|Self Generated| - |

|	shipitscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/shipitscript.md)|FIC - BOT|Self Generated| - |

|	signingscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signingscript.md)|FIC - BOT|Self Generated| - |

|	signtool	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/signtool.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/64a3808496e6c99e0c28195118a606354e2b77d5)|UI: Add missing view titles (#265)|iFlameing|N/A|2019-02-16 11:56:42|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
