## Commits in production - for 3 days
### Generated on: 2019-08-08 13:21:50 UTC

 | autoland |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/autoland.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/autoland.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6aff093ae164)|[Bug 1542046](https://bugzilla.mozilla.org/show_bug.cgi?id=1542046)  - Allow running JetStream2 via Raptor r=rwood,perftest-reviewersChanged the required yml, ini, json, js and html files to add Jetstream2 benchmark test to Raptor.The changes on the javascript files are on github.Differential Revision: https://phabricator.services.mozilla.com/D35418|Marian Raiciof |rwood,perftest-reviewers|2019-08-08 09:57:00
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e27bb201e739)|[Bug 1572327](https://bugzilla.mozilla.org/show_bug.cgi?id=1572327)  - Don't record sccache stats in perfherder per instance type. r=nalexanderBuild metrics where the instance type matters, like build times, areimportant to keep track of per instance type, but sccache stats are hitrates, number of non-cacheable requests, and number of write errors tothe cache, none of which are dependent on the instance type.Differential Revision: https://phabricator.services.mozilla.com/D41143|Mike Hommey |nalexander|2019-08-08 09:31:11
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3a6114f56960)|[Bug 1572017](https://bugzilla.mozilla.org/show_bug.cgi?id=1572017)  - Make mozharness aware of the new location of build_resources.json. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40943|Mike Hommey |nalexander|2019-08-07 20:44:12
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ae492dcd4e62)|[Bug 1571769](https://bugzilla.mozilla.org/show_bug.cgi?id=1571769)  - [marionette] Enable Mn jobs with Fission enabled on try. r=ahalDifferential Revision: https://phabricator.services.mozilla.com/D40862|Henrik Skupin |ahal|2019-08-07 20:40:27
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=50687ba1d4c7)|[Bug 1567311](https://bugzilla.mozilla.org/show_bug.cgi?id=1567311)  - Consolidate supporting raptor measurements into one perfherder output and artifact per type. r=perftest-reviewers,rwoodThis patch fixes four things at once:( 1 ) Consolidate supporting raptor measurements into one PERFHERDER_DATA output per type. For example, with this change, all power data will be grouped into one PERFHERDER_DATA output.( 2 ) Output perfherder-data-<DATA_TYPE>.json for each supporting measurement instead of overwriting perfherder-data.json which contains the regular raptor test results.( 3 ) Take an average of the supporting measurements when particular unit's are specified. In this case, the '%' unit makes us take the average instead of the sum of the measurements.( 4 ) Remove the redundant test name entry that prefixes all power subtest entries.Differential Revision: https://phabricator.services.mozilla.com/D40667|Gregory Mierzwinski |perftest-reviewers,rwood|2019-08-07 16:10:17

 | mozilla-inbound |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-inbound.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-inbound.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ae492dcd4e62)|[Bug 1571769](https://bugzilla.mozilla.org/show_bug.cgi?id=1571769)  - [marionette] Enable Mn jobs with Fission enabled on try. r=ahalDifferential Revision: https://phabricator.services.mozilla.com/D40862|Henrik Skupin |ahal|2019-08-08 09:38:55
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3a6114f56960)|[Bug 1572017](https://bugzilla.mozilla.org/show_bug.cgi?id=1572017)  - Make mozharness aware of the new location of build_resources.json. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40943|Mike Hommey |nalexander|2019-08-08 09:38:55
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5c3693e45bc1)|Merge mozilla-central to autoland. a=merge CLOSED TREE|Noemi Erli |merge|2019-08-07 21:56:41
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=50687ba1d4c7)|[Bug 1567311](https://bugzilla.mozilla.org/show_bug.cgi?id=1567311)  - Consolidate supporting raptor measurements into one perfherder output and artifact per type. r=perftest-reviewers,rwoodThis patch fixes four things at once:( 1 ) Consolidate supporting raptor measurements into one PERFHERDER_DATA output per type. For example, with this change, all power data will be grouped into one PERFHERDER_DATA output.( 2 ) Output perfherder-data-<DATA_TYPE>.json for each supporting measurement instead of overwriting perfherder-data.json which contains the regular raptor test results.( 3 ) Take an average of the supporting measurements when particular unit's are specified. In this case, the '%' unit makes us take the average instead of the sum of the measurements.( 4 ) Remove the redundant test name entry that prefixes all power subtest entries.Differential Revision: https://phabricator.services.mozilla.com/D40667|Gregory Mierzwinski |perftest-reviewers,rwood|2019-08-07 21:56:41
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b94a6b06c9b9)|Merge inbound to mozilla-central. a=merge|Noemi Erli |merge|2019-08-07 10:10:48
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d28c14caa7cc)|[Bug 1571986](https://bugzilla.mozilla.org/show_bug.cgi?id=1571986)  - Add some info to try to find what is going on. r=meMANUAL PUSH: because it starts happening with something that landed on inbound.|Mike Hommey |me|2019-08-07 07:53:31
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=cac35e682ab5)|[Bug 1570541](https://bugzilla.mozilla.org/show_bug.cgi?id=1570541)  - Use tarfile in fetch-content on Windows. r=tomprinceDifferential Revision: https://phabricator.services.mozilla.com/D40401|Mike Hommey |tomprince|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=df808b9785c6)|[Bug 1570541](https://bugzilla.mozilla.org/show_bug.cgi?id=1570541)  - Use git fetch tasks for clang. r=froydnjWhat this means is that the sources for clang/llvm are downloadedseparately from the toolchain build ( which also means we finally onlydownload a given version of clang once for all platforms ).In turn, this means the build-clang.py script needs to start with anexisting llvm-project tree, and we choose to make build-clang.py expectthat it's run from the llvm-project root directory.This also means we don't need to download git for the windows toolchaintask.Differential Revision: https://phabricator.services.mozilla.com/D40402|Mike Hommey |froydnj|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7624607672f1)|[Bug 1570541](https://bugzilla.mozilla.org/show_bug.cgi?id=1570541)  - Revert MOZ_FETCHES_DIR hacks from [Bug 1570240](https://bugzilla.mozilla.org/show_bug.cgi?id=1570240)  r=nalexanderThey're not required anymore now that build-clang.py doesn't forceits build directory location.Differential Revision: https://phabricator.services.mozilla.com/D40542|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4ac27c5c53d3)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Add missing tooltool-download.sh references as resources. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40711|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=74180d0a4d7c)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Make tooltool-download.sh download and extract to MOZ_FETCHES_DIR. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40712|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2499460f9d41)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Allow toolchains to use fetches from other toolchains. r=tomprinceThis also allows toolchain tasks to use aliases via fetches, which theycurrently aren't allowed via use_toolchain. There are more toolchainsnow than there were when the restriction was added, and it might beuseful to be able to use aliases. The flip side is that there are somerisks involved with aliases, which is why the restriction was there inthe first place. Let's see how things play out.Differential Revision: https://phabricator.services.mozilla.com/D40713|Mike Hommey |tomprince|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6e250d973608)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Use toolchain fetches instead of use_toolchain references in toolchain task definitions. r=nalexanderAnd remove the use of tooltool-download where it's not needed anymore.Differential Revision: https://phabricator.services.mozilla.com/D40714|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ee9072779abc)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Remove use_toolchain transform for toolchain kind. r=tomprinceNow that all toolchain tasks use toolchain fetches, they don't needthe transform.Differential Revision: https://phabricator.services.mozilla.com/D40715|Mike Hommey |tomprince|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=95f15f6c8fb9)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Use urlparse rather relying on just splitting on / being enough. r=tomprinceDifferential Revision: https://phabricator.services.mozilla.com/D40738|Mike Hommey |tomprince|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=44f285f40796)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Abstract opening a temporary file and renaming it after close. r=tomprinceAnd use that in git_checkout_archive.Differential Revision: https://phabricator.services.mozilla.com/D40739|Mike Hommey |tomprince|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a801d59b70a5)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Allow to repack downloaded archives "on the fly". [Bug 1479533](https://bugzilla.mozilla.org/show_bug.cgi?id=1479533)  was proposing to add a similar functionality, but thisiteration avoids actually unpacking anything, and ensuresreproducibility by relying on the reproducible bits from the originalarchives: file ordering, flags, etc. ( since they are checksummed, thoseare never going to change for a given archive ).Another notable difference is that this applies the repack on the fetchtask itself, rather than create a separate task to apply the repack. Thelatter has advantages, in that it allows to change the repacking withoutredownloading the original file from a third-party server, but inpractice, most changes to the repacking would trigger the download tasksanyways.This patch only takes care of changing the archive type ( zip->tar ), andthe compression type ( anything->zstandard ).Differential Revision: https://phabricator.services.mozilla.com/D40740|Mike Hommey |tomprince|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=dc8f0af3a4d6)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Allow simple manipulation of file paths in fetched archives. r=tomprinceNamely:- adding a prefix,- stripping path components.Differential Revision: https://phabricator.services.mozilla.com/D40741|Mike Hommey |tomprince|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=03d8fbec4f53)|[Bug 1571596](https://bugzilla.mozilla.org/show_bug.cgi?id=1571596)  - Repack GCC and related source tarballs. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40748|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e0a260c5ea2b)|[Bug 1571596](https://bugzilla.mozilla.org/show_bug.cgi?id=1571596)  - Reduce the number of toolchain scripts for GCC. r=nalexanderNow that all GCC and related source tarballs extract to pathsindependent of their version number, the scripts are all verylook-alike, so they can be consolidated.Differential Revision: https://phabricator.services.mozilla.com/D40749|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=39dbbccbb110)|[Bug 1571597](https://bugzilla.mozilla.org/show_bug.cgi?id=1571597)  - Use fetches tasks for ninja and cmake, instead of tooltool. r=nalexanderWe could keep the same versions of cmake and ninja, but there are fewenough tasks using them to really matter.Differential Revision: https://phabricator.services.mozilla.com/D40750|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=25e3755332fe)|[Bug 1571597](https://bugzilla.mozilla.org/show_bug.cgi?id=1571597)  - Consolidate toolchain task tooltool manifests. r=nalexanderThere are now only two left:- one for the OSX 10.11 SDK- one for Visual Studio 2017Differential Revision: https://phabricator.services.mozilla.com/D40751MANUAL PUSH: avoid closing autoland while all docker images andtoolchains are rebuilt.|Mike Hommey |nalexander|2019-08-07 05:06:36
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=fb0ae6ca7322)|[Bug 1536103](https://bugzilla.mozilla.org/show_bug.cgi?id=1536103)  - Fix Sphinx Warning for not referenced hyperlinks. r=ahalDifferential Revision: https://phabricator.services.mozilla.com/D39057|championshuttler |ahal|2019-08-07 04:39:23
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3fe035323cee)|[Bug 1571636](https://bugzilla.mozilla.org/show_bug.cgi?id=1571636)  - Expose build resources data from automation builds as artifacts. r=nalexanderThe build docker images need python-dev installed to build psutil, usedby the build resources monitor.Differential Revision: https://phabricator.services.mozilla.com/D40781|Mike Hommey |nalexander|2019-08-07 04:39:23
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=628c58d53615)|[Bug 1571587](https://bugzilla.mozilla.org/show_bug.cgi?id=1571587)  - Remove unused fetches. r=nalexanderMore leftovers from the removal of GCC 4.9.Differential Revision: https://phabricator.services.mozilla.com/D40737|Mike Hommey |nalexander|2019-08-07 04:39:23

 | mozilla-central |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-central.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-central.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ae492dcd4e62)|[Bug 1571769](https://bugzilla.mozilla.org/show_bug.cgi?id=1571769)  - [marionette] Enable Mn jobs with Fission enabled on try. r=ahalDifferential Revision: https://phabricator.services.mozilla.com/D40862|Henrik Skupin |ahal|2019-08-08 09:33:10
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3a6114f56960)|[Bug 1572017](https://bugzilla.mozilla.org/show_bug.cgi?id=1572017)  - Make mozharness aware of the new location of build_resources.json. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40943|Mike Hommey |nalexander|2019-08-08 09:33:10
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5c3693e45bc1)|Merge mozilla-central to autoland. a=merge CLOSED TREE|Noemi Erli |merge|2019-08-07 21:52:12
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=50687ba1d4c7)|[Bug 1567311](https://bugzilla.mozilla.org/show_bug.cgi?id=1567311)  - Consolidate supporting raptor measurements into one perfherder output and artifact per type. r=perftest-reviewers,rwoodThis patch fixes four things at once:( 1 ) Consolidate supporting raptor measurements into one PERFHERDER_DATA output per type. For example, with this change, all power data will be grouped into one PERFHERDER_DATA output.( 2 ) Output perfherder-data-<DATA_TYPE>.json for each supporting measurement instead of overwriting perfherder-data.json which contains the regular raptor test results.( 3 ) Take an average of the supporting measurements when particular unit's are specified. In this case, the '%' unit makes us take the average instead of the sum of the measurements.( 4 ) Remove the redundant test name entry that prefixes all power subtest entries.Differential Revision: https://phabricator.services.mozilla.com/D40667|Gregory Mierzwinski |perftest-reviewers,rwood|2019-08-07 21:52:12
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=cac35e682ab5)|[Bug 1570541](https://bugzilla.mozilla.org/show_bug.cgi?id=1570541)  - Use tarfile in fetch-content on Windows. r=tomprinceDifferential Revision: https://phabricator.services.mozilla.com/D40401|Mike Hommey |tomprince|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=df808b9785c6)|[Bug 1570541](https://bugzilla.mozilla.org/show_bug.cgi?id=1570541)  - Use git fetch tasks for clang. r=froydnjWhat this means is that the sources for clang/llvm are downloadedseparately from the toolchain build ( which also means we finally onlydownload a given version of clang once for all platforms ).In turn, this means the build-clang.py script needs to start with anexisting llvm-project tree, and we choose to make build-clang.py expectthat it's run from the llvm-project root directory.This also means we don't need to download git for the windows toolchaintask.Differential Revision: https://phabricator.services.mozilla.com/D40402|Mike Hommey |froydnj|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7624607672f1)|[Bug 1570541](https://bugzilla.mozilla.org/show_bug.cgi?id=1570541)  - Revert MOZ_FETCHES_DIR hacks from [Bug 1570240](https://bugzilla.mozilla.org/show_bug.cgi?id=1570240)  r=nalexanderThey're not required anymore now that build-clang.py doesn't forceits build directory location.Differential Revision: https://phabricator.services.mozilla.com/D40542|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4ac27c5c53d3)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Add missing tooltool-download.sh references as resources. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40711|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=74180d0a4d7c)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Make tooltool-download.sh download and extract to MOZ_FETCHES_DIR. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40712|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2499460f9d41)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Allow toolchains to use fetches from other toolchains. r=tomprinceThis also allows toolchain tasks to use aliases via fetches, which theycurrently aren't allowed via use_toolchain. There are more toolchainsnow than there were when the restriction was added, and it might beuseful to be able to use aliases. The flip side is that there are somerisks involved with aliases, which is why the restriction was there inthe first place. Let's see how things play out.Differential Revision: https://phabricator.services.mozilla.com/D40713|Mike Hommey |tomprince|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6e250d973608)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Use toolchain fetches instead of use_toolchain references in toolchain task definitions. r=nalexanderAnd remove the use of tooltool-download where it's not needed anymore.Differential Revision: https://phabricator.services.mozilla.com/D40714|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ee9072779abc)|[Bug 1571562](https://bugzilla.mozilla.org/show_bug.cgi?id=1571562)  - Remove use_toolchain transform for toolchain kind. r=tomprinceNow that all toolchain tasks use toolchain fetches, they don't needthe transform.Differential Revision: https://phabricator.services.mozilla.com/D40715|Mike Hommey |tomprince|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=95f15f6c8fb9)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Use urlparse rather relying on just splitting on / being enough. r=tomprinceDifferential Revision: https://phabricator.services.mozilla.com/D40738|Mike Hommey |tomprince|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=44f285f40796)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Abstract opening a temporary file and renaming it after close. r=tomprinceAnd use that in git_checkout_archive.Differential Revision: https://phabricator.services.mozilla.com/D40739|Mike Hommey |tomprince|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a801d59b70a5)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Allow to repack downloaded archives "on the fly". [Bug 1479533](https://bugzilla.mozilla.org/show_bug.cgi?id=1479533)  was proposing to add a similar functionality, but thisiteration avoids actually unpacking anything, and ensuresreproducibility by relying on the reproducible bits from the originalarchives: file ordering, flags, etc. ( since they are checksummed, thoseare never going to change for a given archive ).Another notable difference is that this applies the repack on the fetchtask itself, rather than create a separate task to apply the repack. Thelatter has advantages, in that it allows to change the repacking withoutredownloading the original file from a third-party server, but inpractice, most changes to the repacking would trigger the download tasksanyways.This patch only takes care of changing the archive type ( zip->tar ), andthe compression type ( anything->zstandard ).Differential Revision: https://phabricator.services.mozilla.com/D40740|Mike Hommey |tomprince|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=dc8f0af3a4d6)|[Bug 1571589](https://bugzilla.mozilla.org/show_bug.cgi?id=1571589)  - Allow simple manipulation of file paths in fetched archives. r=tomprinceNamely:- adding a prefix,- stripping path components.Differential Revision: https://phabricator.services.mozilla.com/D40741|Mike Hommey |tomprince|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=03d8fbec4f53)|[Bug 1571596](https://bugzilla.mozilla.org/show_bug.cgi?id=1571596)  - Repack GCC and related source tarballs. r=nalexanderDifferential Revision: https://phabricator.services.mozilla.com/D40748|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e0a260c5ea2b)|[Bug 1571596](https://bugzilla.mozilla.org/show_bug.cgi?id=1571596)  - Reduce the number of toolchain scripts for GCC. r=nalexanderNow that all GCC and related source tarballs extract to pathsindependent of their version number, the scripts are all verylook-alike, so they can be consolidated.Differential Revision: https://phabricator.services.mozilla.com/D40749|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=39dbbccbb110)|[Bug 1571597](https://bugzilla.mozilla.org/show_bug.cgi?id=1571597)  - Use fetches tasks for ninja and cmake, instead of tooltool. r=nalexanderWe could keep the same versions of cmake and ninja, but there are fewenough tasks using them to really matter.Differential Revision: https://phabricator.services.mozilla.com/D40750|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=25e3755332fe)|[Bug 1571597](https://bugzilla.mozilla.org/show_bug.cgi?id=1571597)  - Consolidate toolchain task tooltool manifests. r=nalexanderThere are now only two left:- one for the OSX 10.11 SDK- one for Visual Studio 2017Differential Revision: https://phabricator.services.mozilla.com/D40751MANUAL PUSH: avoid closing autoland while all docker images andtoolchains are rebuilt.|Mike Hommey |nalexander|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d28c14caa7cc)|[Bug 1571986](https://bugzilla.mozilla.org/show_bug.cgi?id=1571986)  - Add some info to try to find what is going on. r=meMANUAL PUSH: because it starts happening with something that landed on inbound.|Mike Hommey |me|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b94a6b06c9b9)|Merge inbound to mozilla-central. a=merge|Noemi Erli |merge|2019-08-07 09:57:05
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=fb0ae6ca7322)|[Bug 1536103](https://bugzilla.mozilla.org/show_bug.cgi?id=1536103)  - Fix Sphinx Warning for not referenced hyperlinks. r=ahalDifferential Revision: https://phabricator.services.mozilla.com/D39057|championshuttler |ahal|2019-08-07 04:33:53
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3fe035323cee)|[Bug 1571636](https://bugzilla.mozilla.org/show_bug.cgi?id=1571636)  - Expose build resources data from automation builds as artifacts. r=nalexanderThe build docker images need python-dev installed to build psutil, usedby the build resources monitor.Differential Revision: https://phabricator.services.mozilla.com/D40781|Mike Hommey |nalexander|2019-08-07 04:33:53
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=628c58d53615)|[Bug 1571587](https://bugzilla.mozilla.org/show_bug.cgi?id=1571587)  - Remove unused fetches. r=nalexanderMore leftovers from the removal of GCC 4.9.Differential Revision: https://phabricator.services.mozilla.com/D40737|Mike Hommey |nalexander|2019-08-07 04:33:53
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b85c920da19d)|[Bug 1568815](https://bugzilla.mozilla.org/show_bug.cgi?id=1568815)  [wpt PR 17651] - [ci] Disable terminal colors in Taskcluster, a=testonlyAutomatic update from web-platform-tests[ci] Disable terminal colors in Taskcluster--wpt-commits: 1d71e844de92839ca13d670657623d50c99dcdd5wpt-pr: 17651|Mike Pennisi |testonly|2019-08-05 22:00:30

 | mozilla-beta |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-beta.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-beta.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-beta.md) |

 | version-control-tools |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/version-control-tools.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/version-control-tools.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=307f3c286876)|ansible/hg-ssh: set Lando required list to correct values ( [Bug 1572128](https://bugzilla.mozilla.org/show_bug.cgi?id=1572128)  )I updated this manually during testing, then forgot to updateit after. This lead to the correct value being overridden duringthe following deploy.|Connor Sheehan |N/A|2019-08-07 15:45:12
|[Link](https://hg.mozilla.org/hgcustom/version-control-tools/pushloghtml?changeset=01ef6e45d821)|[Bug 1572072](https://bugzilla.mozilla.org/show_bug.cgi?id=1572072)  - Disable the `format-source` extension since it served it's purpose for Prettier, r=sheehanDifferential Revision: https://phabricator.services.mozilla.com/D40998|Victor Porof |sheehan|2019-08-07 14:25:16

 | relops-image-builder |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/relops-image-builder.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/relops-image-builder.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://api.github.com/repos/mozilla-platform-ops/relops-image-builder/commits/5d43cea5424f4d4445081502c6c4a1e3e8ed9009)|[Bug 1553572](https://bugzilla.mozilla.org/show_bug.cgi?id=1553572)  - install gcloud services|Rob Thijssen|N/A|2019-08-06 10:10:08
|[Link](https://api.github.com/repos/mozilla-platform-ops/relops-image-builder/commits/cdef7b88be0d7874e13b84c03d3755adbaee91ef)|[Bug 1553572](https://bugzilla.mozilla.org/show_bug.cgi?id=1553572)  - install gcloud services|Rob Thijssen|N/A|2019-08-06 09:28:02
|[Link](https://api.github.com/repos/mozilla-platform-ops/relops-image-builder/commits/94cef59c979fe16acf0f8810d396c83b692752f7)|[Bug 1553572](https://bugzilla.mozilla.org/show_bug.cgi?id=1553572)  - disable services debugging|Rob Thijssen|N/A|2019-08-06 08:15:42

 | OpenCloudConfig |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/OpenCloudConfig.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/OpenCloudConfig.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/OpenCloudConfig.md) |

 | relops-hardware-controller |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/relops-hardware-controller.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/relops-hardware-controller.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/relops-hardware-controller.md) |

 | ronin_puppet |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/ronin_puppet.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/ronin_puppet.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/ronin_puppet.md) |

 | mozilla-release |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-release.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-release.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozilla-release.md) |

 | balrogscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/balrogscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/balrogscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/balrogscript.md) |

 | build-puppet |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/build-puppet.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/build-puppet.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/0fbb5cb08f20bf3fc18f752ed823138cd13fced4)|Merge pull request #567 from lundjordan/google_oauth_api_keyremoves unused google_oauth_api_key from puppet configuration|Jordan Lund|N/A|2019-08-07 21:58:30
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/70b95b55863802a416680470dd36929fdfde55dc)|Merge pull request #568 from lundjordan/crash_stats_api_tokenremoves crash_stats_api_token from puppet configuration|Jordan Lund|N/A|2019-08-07 21:33:01
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/54ff7f48cafd386b126ebd1d7623b1e83f7691c1)|Scheduled weekly dependency update for week 31 ( #573 )* Update pyyaml from 5.1.1 to 5.1.2 * Update jsonschema from 3.0.1 to 3.0.2 * Update pyasn1 from 0.4.5 to 0.4.6 * Update taskcluster from 15.0.0 to 16.0.0 * Update mozilla-version from 0.3.4 to 0.4.1 * Update twisted from 19.2.1 to 19.7.0 * Update pyasn1-modules from 0.2.5 to 0.2.6 * Update pytz from 2019.1 to 2019.2 * Update mercurial from 5.0.2 to 5.1 * add future==0.17.1 as a new mozilla-version dep|pyup.io bot|N/A|2019-08-07 16:41:34
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/66aac47e6846eb078b56b233a6e4ac79e6ab3172)|Merge pull request #572 from Callek/langpackSupport Langpack Signing in Autograph for signingscript|Justin Wood (Callek)|N/A|2019-08-07 15:58:19
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/0967f14630293fcce1040966d58c13c81301578f)|Merge pull request #571 from [Bug 1564264](https://bugzilla.mozilla.org/show_bug.cgi?id=1564264)  - Move omnija dep signing to prod autograph|Justin Wood (Callek)|N/A|2019-08-07 15:58:08
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/22ed23a248c65f8ad0a45084cdc8915e56ad8fa6)|[Bug 1566298](https://bugzilla.mozilla.org/show_bug.cgi?id=1566298)  - Support Langpack Signing in Autograph|Justin Wood|N/A|2019-08-06 17:51:13
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/1b984a3d7c8ac4635d93f08ba371e2690c4b510d)|[Bug 1564264](https://bugzilla.mozilla.org/show_bug.cgi?id=1564264)  - Move omnija dep signing to prod autograph|Justin Wood|N/A|2019-08-06 17:45:37
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/e9475f9f19fbf35f5aef51bf5ad556997ce7697c)|Merge pull request #570 from [Bug 1562061](https://bugzilla.mozilla.org/show_bug.cgi?id=1562061)  completely remove mig module|Jacob Watkins|N/A|2019-08-06 16:22:12
|[Link](https://api.github.com/repos/mozilla-releng/build-puppet/commits/aca2371298ee9b736f70bca770a469c3042ce608)|[Bug 1562061](https://bugzilla.mozilla.org/show_bug.cgi?id=1562061)  completely remove mig module|Jake Watkins|N/A|2019-08-06 16:05:16

 | taskcluster |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/taskcluster.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/taskcluster.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/6682067b968a187e31a516195a0ae4f725515a09)|Merge pull request #1162 from [Bug 1553953](https://bugzilla.mozilla.org/show_bug.cgi?id=1553953)  - limit chars in provisionerId and workerType|Dustin J. Mitchell|N/A|2019-08-08 12:46:59
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/c4a4455abe771d50cd5c100a44f2cd4bd5ebc730)|[Bug 1553953](https://bugzilla.mozilla.org/show_bug.cgi?id=1553953)  - limit chars in provisionerId and workerTypeThis brings these symbols into correspondence with the limits onworkerPoolId, which are designed to be compatible with various cloudproviders.|Dustin J. Mitchell|N/A|2019-08-07 14:06:39
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/d6fddea345e02aa6075dc8cc80d89ddf47c949ce)|Merge pull request #1161 from grenade/patch-1fix broken link|Dustin J. Mitchell|N/A|2019-08-07 12:43:57
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/51e2451563eb24697267efaccc6934f691335ef4)|fix broken link|Rob Thijssen|N/A|2019-08-07 08:45:17
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/4a8fd1e62c5beb7b6697b016d4671dc674b2ce19)|clients/client-py/README.md is also generated ( #1146 )clients/client-py/README.md is also generated|Brian Stack|N/A|2019-08-06 17:25:47
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/ee6fdaf3468ab1d26f807d9a756ca8dabd1d313b)|renovate: ignore golang.org/x/tools ( #1121 )renovate: ignore golang.org/x/tools|Brian Stack|N/A|2019-08-06 17:23:32
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/3ea6281593e03b151f607499a1a53cc6a90156e9)|Merge pull request #1152 from taskcluster/renovate/node-10.xUpdate Node.js|Dustin J. Mitchell|N/A|2019-08-06 16:11:56
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/766a40a70bfedfed54816b6324310182be27671c)|Stopped rendering List & ListITem in `TableCellListItem` ( #1155 )* Updated DocsSidebarList.jsx * Updated DocsSidebarList.jsx * Update DocsSidebarList.jsx * Updated removeReadmeFromPath.js Fixed the documentation header tree highlighting for trailing slashes. * Restored the changes for DocsSidebarList.jsx * Updated removeReadmeFromPath.js * linted code * Stopped rendering a List & ListITem in * Rename List to Item|Ruchika|N/A|2019-08-06 14:45:44
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/ec202f6e63b3ade95fecd0a47778202b5632d2f8)|update remaining node versions that renovate doesn't see|Dustin J. Mitchell|N/A|2019-08-06 14:05:52
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/bfd3d8e8ec8ed5be4ab7d24a1609901db9b5a9db)|Merge pull request #1153 from taskcluster/renovate/lodash-monorepoUpdate dependency lodash to v4.17.15|Dustin J. Mitchell|N/A|2019-08-06 13:01:32
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/5c9e573ddd1e7d6b2649b0599a1a86dc3d45ea5f)|Merge pull request #1143 from djmitche/fix-lastfire-nameFix LastFire table name|Dustin J. Mitchell|N/A|2019-08-05 18:00:06
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/9a919000c8b372ff0615cbe8e0aebccd376dca7e)|Merge pull request #1160 from taskcluster/setdefaults-dev-initDon't overwrite dev config for defaults|Dustin J. Mitchell|N/A|2019-08-05 17:52:36
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/c4b89e74d57f34da6fd9826bd665d57ee96aabdb)|Don't overwrite dev config for defaults|Brian Stack|N/A|2019-08-05 17:36:40
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/6a028e97ec075f78c260fc52e74e2d2c77eab84f)|Minor improvements to google provider docs ( #1158 )Minor improvements to google provider docs|Brian Stack|N/A|2019-08-05 17:17:07
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/f869560c96b8894d16df3d991df04e39c21240c4)|Merge pull request #1157 from [Bug 1561679](https://bugzilla.mozilla.org/show_bug.cgi?id=1561679)  - bump dependency resolver timeouts to >30s in hopes of w…|Dustin J. Mitchell|N/A|2019-08-05 16:38:02
|[Link](https://api.github.com/repos/taskcluster/taskcluster/commits/cf522ca00f69829af4c47284035886ebf8000266)|Minor improvements to google provider docs|Dustin J. Mitchell|N/A|2019-08-05 16:37:05

 | beetmoverscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/beetmoverscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/beetmoverscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/beetmoverscript.md) |

 | addonscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/addonscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/addonscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/addonscript.md) |

 | pushsnapscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/pushsnapscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/pushsnapscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/pushsnapscript.md) |

 | pushapkscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/pushapkscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/pushapkscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/pushapkscript.md) |

 | shipitscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/shipitscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/shipitscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/shipitscript.md) |

 | bouncerscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/bouncerscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/bouncerscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/bouncerscript.md) |

 | scriptworker |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/scriptworker.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/scriptworker.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/scriptworker.md) |

 | treescript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/treescript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/treescript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/treescript.md) |

 | signingscript |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/signingscript.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/signingscript.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://api.github.com/repos/mozilla-releng/signingscript/commits/dae10488ff88595044612efd09beefd41235035c)|Merge pull request #122 from Callek/11.1.0Release 11.1.0|Justin Wood (Callek)|N/A|2019-08-07 15:51:46
|[Link](https://api.github.com/repos/mozilla-releng/signingscript/commits/d078b403beeac0097c2a83dede7b61fe5ec27671)|Release 11.1.0|Justin Wood|N/A|2019-08-07 12:21:54

 | signtool |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/signtool.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/signtool.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/signtool.md) |

 | services |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/services.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/services.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/services.md) |

 | build-cloud-tools |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/build-cloud-tools.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/build-cloud-tools.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/build-cloud-tools.md) |

 | ci-configuration |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/ci-configuration.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/ci-configuration.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=91740dfda4f4)|No bug: Gives fenix PRs access to "project/mobile/fenix/pr" r=mtabaraDifferential Revision: https://phabricator.services.mozilla.com/D40893|Mitchell Hentges |mtabara|2019-08-07 17:09:06
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=bfb4eb1624be)|No bug: removes unused Fenix secret r=mtabaraDifferential Revision: https://phabricator.services.mozilla.com/D40894|Mitchell Hentges |mtabara|2019-08-07 16:18:48
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=76219e37ffcf)|[Bug 1571029](https://bugzilla.mozilla.org/show_bug.cgi?id=1571029)  - part 2: Allow v3 mobile indexes r=mtabaraDifferential Revision: https://phabricator.services.mozilla.com/D40809|Johan Lorenzo |mtabara|2019-08-06 14:45:35

 | ci-admin |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/ci-admin.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/ci-admin.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=27fb6514f634)|No bug: Fix linting errors; r=me|Tom Prince |me|2019-08-08 01:08:29
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=41187e1ecefa)|[Bug 1552242](https://bugzilla.mozilla.org/show_bug.cgi?id=1552242)  - fix aws-provisioner support to operate in non-legacy environments r=tomprince,bstackThis fixes some bugs that occur when there is no AWS Provisioner service.Differential Revision: https://phabricator.services.mozilla.com/D40470|Dustin J. Mitchell |tomprince,bstack|2019-08-06 18:41:22
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=c4e72c13a55c)|[Bug 1552242](https://bugzilla.mozilla.org/show_bug.cgi?id=1552242)  - add support for worker-manager worker pools r=tomprince,bstackInvolving an update to the taskcluster library to get access to this APIDifferential Revision: https://phabricator.services.mozilla.com/D40471|Dustin J. Mitchell |tomprince,bstack|2019-08-06 18:41:22

 | mozapkpublisher |[Markdown](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozapkpublisher.md)|[Json](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozapkpublisher.json)| 
|:----------:|:-----------------------:|:--------:| 

| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| No commits in the past 3 days.. see the longer history [here](https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/mozapkpublisher.md) |
