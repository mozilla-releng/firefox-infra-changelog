##  Commits in production - for 3 days, generated on: 2019-03-21 19:37:37 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=bb60a18552f3)|[Bug 1491371 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1491371) 1512188 - use new decision task image, with new options r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D24401|dmitchell@mozilla.com|tomprince|2019-03-21 21:20:47|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=73912c794410)|[Bug 1536230 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1536230) Speed up extraction of tarballs r=marco Differential Revision: https://phabricator.services.mozilla.com/D23938|catlee@mozilla.com|marco|2019-03-21 14:42:45|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=74b3bf36f5e8)|[Bug 1527463 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527463) - Enable EME on win64-aarch64 nightlies. r=tomprince, a=CristianB [Bug 1534522 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534522) added win64-aarch64-eme/opt builds, which are artifact builds that glue together a win64-aarch64/opt build and a win32/opt build. This enables EME on the corresponding nightlies in a slightly different way: - this adds a no-eme build that corresponds to win64-aarch64/opt. - this turns the existing nightly into an artifact build that glues together that no-eme build and the win32 nightly. The no-eme build cannot have the nightly attribute set, first because the beetmover transform fails in that case, and because that would imply shipping those builds, but they're not meant to be shipped this way. It also has run-on-projects set to an empty list so that it doesn't appear by default in `mach try fuzzy`, while still being triggered when needed due to being a dependency of the nightly build. It is preferable to keep the win64-aarch64{,-eme}/opt builds untouched to make things easier for try (the win64-aarch64 ones being the main ones to try; also, the -eme builds currently fail with --artifacts). Ideally, like in [Bug 1534522 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534522) we'd add a diffoscope build to ensure the variations between the nightly and its base no-eme build are within control, but currently, that would trigger nightlies on every push, which is not desirable. Ideally, they'd trigger whenever both their dependencies are in the target task graph. We leave that to a followup. Differential Revision: https://phabricator.services.mozilla.com/D23640|ncsoregi@mozilla.com|tomprince,|2019-03-21 12:51:56|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e1350f7a1914)|Merge mozilla-central to inbound. a=merge CLOSED TREE|ncsoregi@mozilla.com|merge|2019-03-21 12:51:56|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0f9e3bff5575)|[Bug 1473602 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1473602) - Add u2f-devices plug to snap package. r=jlorenzo This allows the confined snap to interact with Universal 2nd Factor devices, such as Yubikeys. Differential Revision: https://phabricator.services.mozilla.com/D24147|jlorenzo@mozilla.com|jlorenzo|2019-03-20 16:21:05|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d7e6fff52db3)|Backed out 12 changesets (bug 632954) for causing Android Bpgo(run) pending jobs CLOSED TREE Backed out changeset 429c96e4de32 (bug 632954) Backed out changeset de8beacc5eb4 (bug 632954) Backed out changeset c151ebf303ca (bug 632954) Backed out changeset b96dd954a456 (bug 632954) Backed out changeset 26031d362333 (bug 632954) Backed out changeset 097f141a499d (bug 632954) Backed out changeset 6f5fc0d644dd (bug 632954) Backed out changeset 53d3443e55d9 (bug 632954) Backed out changeset 503bcac73583 (bug 632954) Backed out changeset 142ae187478d (bug 632954) Backed out changeset 0615c775a0cf (bug 632954) Backed out changeset 3dfc0e4f8e7c (bug 632954)|nerli@mozilla.com||2019-03-20 11:58:50|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=13e9a230eb25)|[Bug 1246594 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1246594) - Enable ESLint rule no-throw-literal by default. r=Standard8 Differential Revision: https://phabricator.services.mozilla.com/D24088|mbanner@mozilla.com|Standard8|2019-03-20 00:27:55|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f45661298ac3)|[Bug 1535417 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535417) - Set dynamic mozinfo fields in Android test-verify; r=bc In the mochitest harness, is_fennec is populated by examining harness options, and is_emulator and android_version are populated by examining the device via mozdevice. The per-test code doesn't have those options and the emulator may not be available yet, so I've opted for populated those fields from mozharness configuration. In practice, we only run Android TV on Android 4.3, where is_fennec=True, is_emulator=True, and android_version=18. I'd like to run TV on Android 7.0/geckoview eventually, where is_fennec=False, is_emulator=True, and android_version=24. Since I was here, I also removed 'stylo' from the per-test mozinfo, since that field is obsolete now. Differential Revision: https://phabricator.services.mozilla.com/D23595|gbrown@mozilla.com|bc|2019-03-19 20:25:13|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=85bd45178007)|[Bug 1519851 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519851) - Create --enable-fuzzing debug build job for MacOSX. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D19862|ccoroiu@mozilla.com|dustin|2019-03-19 19:25:18|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e16d27f25d45)|[Bug 1535011 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535011) update `versioncontrol.rst` r=dustin Small updates to the version control documents regarding upgrading `robustcheckout.py`. I noticed that we still reference `build-puppet` from it's former home on hgmo and don't include OpenCloudConfig in our list of places we need to vendor `robustcheckout` changes. Differential Revision: https://phabricator.services.mozilla.com/D23742|cosheehan@mozilla.com|dustin|2019-03-18 19:59:44|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d7e6fff52db3)|Backed out 12 changesets (bug 632954) for causing Android Bpgo(run) pending jobs CLOSED TREE Backed out changeset 429c96e4de32 (bug 632954) Backed out changeset de8beacc5eb4 (bug 632954) Backed out changeset c151ebf303ca (bug 632954) Backed out changeset b96dd954a456 (bug 632954) Backed out changeset 26031d362333 (bug 632954) Backed out changeset 097f141a499d (bug 632954) Backed out changeset 6f5fc0d644dd (bug 632954) Backed out changeset 53d3443e55d9 (bug 632954) Backed out changeset 503bcac73583 (bug 632954) Backed out changeset 142ae187478d (bug 632954) Backed out changeset 0615c775a0cf (bug 632954) Backed out changeset 3dfc0e4f8e7c (bug 632954)|shindli@mozilla.com||2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7df96a607be8)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Explicitly set NEED_XVFB to false if need-xvfb isn't set; r=tomprince test-linux.sh defaults to true for NEED_XVFB, while build-linux.sh defaults to false. If we are using test-linux.sh from mozharness (rather than mozharness-test), we need to explicitly set NEED_XVFB to false in order to not use xvfb. Differential Revision: https://phabricator.services.mozilla.com/D22820|shindli@mozilla.com|tomprince|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a257e15d267f)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add execute bit to test-linux.sh; r=tomprince In order to call test-linux.sh with the job-script parameter, it needs to have executable permissions. Differential Revision: https://phabricator.services.mozilla.com/D22821|shindli@mozilla.com|tomprince|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=0450380b2693)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add support for MOZHARNESS_OPTIONS to test-linux.sh; r=tomprince The mozharness.py transform passes in "options" parameters through the MOZHARNESS_OPTIONS environment variable. This will allow the Android PGO run task to pass in the mozharness script name to test-linux.sh Differential Revision: https://phabricator.services.mozilla.com/D22822|shindli@mozilla.com|tomprince|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=831b503b1e5c)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add Android PGO-instrumented build task; r=tomprince This is the first stage of the Android PGO task pipeline to generate an instrumented build. Differential Revision: https://phabricator.services.mozilla.com/D22824|shindli@mozilla.com|tomprince|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=407f264cc3ee)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add Android profile generation task; r=tomprince,gbrown This introduces a mozharness script, android_emulator_pgo.py, to run the profileserver suite with the PGO-instrumented Android build, and collect the profile data and jarlog. The mozharness script contains some redundancy with build/pgo/profileserver.py, but the additional requirements for Android to use adb and existing mozharness classes to control the emulator made it difficult to share the desktop profileserver implementation. Differential Revision: https://phabricator.services.mozilla.com/D22825|shindli@mozilla.com|tomprince,gbrown|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d78d224fbb3f)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add final Android PGO task; r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D22826|shindli@mozilla.com|tomprince|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d8203a0665d2)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Enable tests on Android PGO; r=jmaher CLOSED TREE Differential Revision: https://phabricator.services.mozilla.com/D22827|shindli@mozilla.com|jmaher|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=0f9e3bff5575)|[Bug 1473602 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1473602) - Add u2f-devices plug to snap package. r=jlorenzo This allows the confined snap to interact with Universal 2nd Factor devices, such as Yubikeys. Differential Revision: https://phabricator.services.mozilla.com/D24147|shindli@mozilla.com|jlorenzo|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c12cc38850b7)|[Bug 1535947 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535947) [taskgraph] Remove a redundant condition in name_sanity transform; r=aki In [Bug 1501776 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1501776) the `single_dep` and `multi_dep` schemas were aligned, which made both branch in name_sanity identical. Simplify the code to reflect that. Differential Revision: https://phabricator.services.mozilla.com/D24109|shindli@mozilla.com|aki|2019-03-21 06:37:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=74b3bf36f5e8)|[Bug 1527463 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527463) - Enable EME on win64-aarch64 nightlies. r=tomprince, a=CristianB [Bug 1534522 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534522) added win64-aarch64-eme/opt builds, which are artifact builds that glue together a win64-aarch64/opt build and a win32/opt build. This enables EME on the corresponding nightlies in a slightly different way: - this adds a no-eme build that corresponds to win64-aarch64/opt. - this turns the existing nightly into an artifact build that glues together that no-eme build and the win32 nightly. The no-eme build cannot have the nightly attribute set, first because the beetmover transform fails in that case, and because that would imply shipping those builds, but they're not meant to be shipped this way. It also has run-on-projects set to an empty list so that it doesn't appear by default in `mach try fuzzy`, while still being triggered when needed due to being a dependency of the nightly build. It is preferable to keep the win64-aarch64{,-eme}/opt builds untouched to make things easier for try (the win64-aarch64 ones being the main ones to try; also, the -eme builds currently fail with --artifacts). Ideally, like in [Bug 1534522 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534522) we'd add a diffoscope build to ensure the variations between the nightly and its base no-eme build are within control, but currently, that would trigger nightlies on every push, which is not desirable. Ideally, they'd trigger whenever both their dependencies are in the target task graph. We leave that to a followup. Differential Revision: https://phabricator.services.mozilla.com/D23640|shindli@mozilla.com|tomprince,|2019-03-21 06:37:39|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e1350f7a1914)|Merge mozilla-central to inbound. a=merge CLOSED TREE|ncsoregi@mozilla.com|merge|2019-03-21 12:41:32|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d7e6fff52db3)|Backed out 12 changesets (bug 632954) for causing Android Bpgo(run) pending jobs CLOSED TREE Backed out changeset 429c96e4de32 (bug 632954) Backed out changeset de8beacc5eb4 (bug 632954) Backed out changeset c151ebf303ca (bug 632954) Backed out changeset b96dd954a456 (bug 632954) Backed out changeset 26031d362333 (bug 632954) Backed out changeset 097f141a499d (bug 632954) Backed out changeset 6f5fc0d644dd (bug 632954) Backed out changeset 53d3443e55d9 (bug 632954) Backed out changeset 503bcac73583 (bug 632954) Backed out changeset 142ae187478d (bug 632954) Backed out changeset 0615c775a0cf (bug 632954) Backed out changeset 3dfc0e4f8e7c (bug 632954)|shindli@mozilla.com||2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7df96a607be8)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Explicitly set NEED_XVFB to false if need-xvfb isn't set; r=tomprince test-linux.sh defaults to true for NEED_XVFB, while build-linux.sh defaults to false. If we are using test-linux.sh from mozharness (rather than mozharness-test), we need to explicitly set NEED_XVFB to false in order to not use xvfb. Differential Revision: https://phabricator.services.mozilla.com/D22820|shindli@mozilla.com|tomprince|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a257e15d267f)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add execute bit to test-linux.sh; r=tomprince In order to call test-linux.sh with the job-script parameter, it needs to have executable permissions. Differential Revision: https://phabricator.services.mozilla.com/D22821|shindli@mozilla.com|tomprince|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0450380b2693)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add support for MOZHARNESS_OPTIONS to test-linux.sh; r=tomprince The mozharness.py transform passes in "options" parameters through the MOZHARNESS_OPTIONS environment variable. This will allow the Android PGO run task to pass in the mozharness script name to test-linux.sh Differential Revision: https://phabricator.services.mozilla.com/D22822|shindli@mozilla.com|tomprince|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=831b503b1e5c)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add Android PGO-instrumented build task; r=tomprince This is the first stage of the Android PGO task pipeline to generate an instrumented build. Differential Revision: https://phabricator.services.mozilla.com/D22824|shindli@mozilla.com|tomprince|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=407f264cc3ee)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add Android profile generation task; r=tomprince,gbrown This introduces a mozharness script, android_emulator_pgo.py, to run the profileserver suite with the PGO-instrumented Android build, and collect the profile data and jarlog. The mozharness script contains some redundancy with build/pgo/profileserver.py, but the additional requirements for Android to use adb and existing mozharness classes to control the emulator made it difficult to share the desktop profileserver implementation. Differential Revision: https://phabricator.services.mozilla.com/D22825|shindli@mozilla.com|tomprince,gbrown|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d78d224fbb3f)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Add final Android PGO task; r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D22826|shindli@mozilla.com|tomprince|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d8203a0665d2)|[Bug 632954 ](https://bugzilla.mozilla.org/show_bug.cgi?id=632954) - Enable tests on Android PGO; r=jmaher CLOSED TREE Differential Revision: https://phabricator.services.mozilla.com/D22827|shindli@mozilla.com|jmaher|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0f9e3bff5575)|[Bug 1473602 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1473602) - Add u2f-devices plug to snap package. r=jlorenzo This allows the confined snap to interact with Universal 2nd Factor devices, such as Yubikeys. Differential Revision: https://phabricator.services.mozilla.com/D24147|shindli@mozilla.com|jlorenzo|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c12cc38850b7)|[Bug 1535947 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535947) [taskgraph] Remove a redundant condition in name_sanity transform; r=aki In [Bug 1501776 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1501776) the `single_dep` and `multi_dep` schemas were aligned, which made both branch in name_sanity identical. Simplify the code to reflect that. Differential Revision: https://phabricator.services.mozilla.com/D24109|shindli@mozilla.com|aki|2019-03-21 06:34:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d35d63ce1957)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D23832|rgurzau@mozilla.com|sfraser|2019-03-18 23:36:40|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cee5e58bcf61)|[Bug 1534956 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534956) - Add Cristiano's facebook page to tp6-m r=Bebe Differential Revision: https://phabricator.services.mozilla.com/D23317|rgurzau@mozilla.com|Bebe|2019-03-18 23:36:40|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=551c42866143)|[Bug 1535016 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535016) - Don't treat any Android job as new job r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23674|rgurzau@mozilla.com|jmaher|2019-03-18 23:36:40|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=515db7d56834)|[Bug 1473602 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1473602) - Add u2f-devices plug to snap package. r=jlorenzo a=release This allows the confined snap to interact with Universal 2nd Factor devices, such as Yubikeys. Differential Revision: https://phabricator.services.mozilla.com/D24147|jlorenzo@mozilla.com|jlorenzo|2019-03-21 16:10:37|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/3f80d852385b3485e43919668cb0e85e1d11b77c)|Scheduled weekly dependency update for week 11 (#433)    Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update pyyaml from 3.13 to 5.1      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update dictdiffer from 0.7.2 to 0.8.0      Update boto3 from 1.9.112 to 1.9.117      Update botocore from 1.12.113 to 1.12.117      Update decorator from 4.3.2 to 4.4.0      Update decorator from 4.3.2 to 4.4.0      Update mercurial from 4.9 to 4.9.1      Update mercurial from 4.9 to 4.9.1|pyup-bot|N/A|2019-03-21 01:11:28|
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
|[Link](https://github.com/taskcluster/taskcluster/commit/fe07c130a166c4ca422504841c50f0f8fc0ec7d5)|Merge pull request #474 from taskcluster/up-the-waiting-time  Increase deadline for tasks|imbstack|N/A|2019-03-21 16:16:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/21fc92f5075fea2fd840f0a1c12e8b7a25a828b4)|Merge pull request #475 from taskcluster/bug-1536927  [Bug 1536927] Only log taskIds|imbstack|N/A|2019-03-20 22:29:48|
|[Link](https://github.com/taskcluster/taskcluster/commit/6ecc12e6a17267b6c441d4077f982a439f2ffc7d)|Only log taskIds|imbstack|N/A|2019-03-20 22:14:39|
|[Link](https://github.com/taskcluster/taskcluster/commit/763bd2799b46d1fe4213f95c0ef54557b1b160de)|Merge pull request #473 from taskcluster/stop-listening-to-brian  Actually fix retries this time (again)|imbstack|N/A|2019-03-20 18:03:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/61a1bf21159925904fd511d28910103d26dd9d85)|Merge pull request #417 from taskcluster/bug-1535125-pt-1  [Bug 1535125] Part 1: Update critical part of lib-api and auth/queue|imbstack|N/A|2019-03-20 17:56:27|
|[Link](https://github.com/taskcluster/taskcluster/commit/20b2d4aa67a28d21516d0835147e29378363f1d5)|Actually fix retries this time (again)|imbstack|N/A|2019-03-20 17:16:13|
|[Link](https://github.com/taskcluster/taskcluster/commit/9bdbc3e7824a7604e2e0935843499de380f64238)|Merge pull request #462 from djmitche/bug1531871  Bug 1531871 - upgrade azure-blob-storage|djmitche|N/A|2019-03-20 15:28:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/814aad825d73e9d664b1b764f4dd8cdcb025bc6f)|Merge pull request #461 from taskcluster/bug1533591-tf  Bug 1533591 - set WEBSOCKTUNNEL_SECRET and expose as output|djmitche|N/A|2019-03-19 16:52:22|
|[Link](https://github.com/taskcluster/taskcluster/commit/8b77ccceb545211355a3cbd2d6482fc8a3b5b734)|Merge pull request #467 from djmitche/bug1536435  Bug 1536435 - support linked identities|djmitche|N/A|2019-03-19 16:35:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/42f09baa5cd5a17828ed4460040b040f99d2a5c6)|Merge pull request #464 from djmitche/restrict-wst-client-id  Restrict the allowable charcters for wstClient|djmitche|N/A|2019-03-19 15:44:17|
|[Link](https://github.com/taskcluster/taskcluster/commit/490e42b07da287062f215fdd3d51cc906c834352)|Merge pull request #451 from taskcluster/apologies  Fix my wrong review|imbstack|N/A|2019-03-19 15:42:54|
|[Link](https://github.com/taskcluster/taskcluster/commit/e34e6e40208f797e689aed78b8846b567e8395ad)|Bug 1536435 - support linked identities  Now that we link identities, the format of the `identities` property has changed, invalidating some assumptions.  Happily those assumptions were represented with assertions so we got errors instead of undefined behavior!  In particular, an account with a github identity now has an identity like:  ```     {       "provider": "github",       "connection": "github",       "profileData": {         "userId": 1234,         "nickname": "developer1234"       }     }, ```  and an account with a firefoxaccounts sign-in has  ```     {       "profileData": {         "email": "foo@bar.com",         "fxa_sub": "97ff4ba365255c2a92d362ea017baa15",         ...       },       "provider": "oauth2",       "user_id": "firefoxaccounts|97ff4ba365255c2a92d362ea017baa15",       "connection": "firefoxaccounts",       "isSocial": true     } ```|djmitche|N/A|2019-03-19 14:44:57|
|[Link](https://github.com/taskcluster/taskcluster/commit/a6939bf2add7110531a1c23dbfcfdc2a2f3a1899)|client-web: bump version|helfi92|N/A|2019-03-19 13:44:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/2afacb0d9f74300cfff15f485e44459a28dc6b51)|Merge pull request #445 from helfi92/client-web-neutrino-v9  client-web neutrino v9, esm output, share linting|helfi92|N/A|2019-03-19 13:31:02|
|[Link](https://github.com/taskcluster/taskcluster/commit/f1d03671b9f632745e568f7a60d7c9380d29f0f9)|Merge pull request #465 from taskcluster/all-contributors/add-djmitche  docs: add contributors|djmitche|N/A|2019-03-19 12:44:50|

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
|[Link](https://github.com/mozilla-releng/build-cloud-tools/commit/f033efed161948ac58fcf8d27dd0916c850da112)|Merge pull request #375 from garbas/product-details-prod  terraform: add cname for prod instance of product details|dividehex|N/A|2019-03-20 19:38:02|

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=63f55ad7e4bf)|[Bug 1534463 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534463) grant read access for hgmointernal config to all entities with read access to hg fingerprint r=tomprince The private hgweb mirror config we intend to store in a Taskcluster secret will need to be accessed by `run-task`, which also access the hg fingerprint secret. Grant read access to the hgmointernal config to all groups and projects which have access to the hg fingerprint secret. Differential Revision: https://phabricator.services.mozilla.com/D23980|cosheehan@mozilla.com|tomprince|2019-03-21 19:19:40|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=b38a52ee4e61)|[Bug 1534463 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534463) allow `vpn_hg_admin` group to set Mercurial related secrets r=tomprince Now that we have given scopes to the correct contexts, we need to provide the relevant parties with the ability to modify the secrets. This commit grants write access for these secrets to the `vpn_hg_admin` group. This group defines the set of people with SSH access to the hgweb/hgssh cluster behind hgmo. We also give this group the rights to change the `hgfingerprint` secret. Previously this secret was managed by Greg, and I'm not sure who else has access to change it. Now seems like an appropriate time to give access to the relevant parties. Differential Revision: https://phabricator.services.mozilla.com/D23981|cosheehan@mozilla.com|tomprince|2019-03-21 19:19:40|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=324ddaed637c)|[Bug 1533791 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533791) - Remove all priorities scopes, now that mobile projects use "assume:" r=tomprince Remove all priorities scopes, now that mobile projects use "assume:" Differential Revision: https://phabricator.services.mozilla.com/D24376|jlorenzo@mozilla.com|tomprince|2019-03-21 18:25:01|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
