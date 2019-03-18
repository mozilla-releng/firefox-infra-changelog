##  Commits in production - for 3 days, generated on: 2019-03-18 05:27:18 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c6d92a71240c)|[Bug 1529052 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1529052) [wpt PR 15422] - Do not throw from taskcluster-run.py if wpt fails, a=testonly Automatic update from web-platform-tests Do not throw from taskcluster-run.py if wpt fails Previously when `wpt run` stability check fails, the wrapper script taskcluster-run.py would throw an uncaught exception, which might be confused with an infra error. This change makes taskcluster-run.py return a non-zero exit code without printing the traceback. -- wpt-commits: 322981aed92da3b8fa13eb53f25acb8d3a9cb467 wpt-pr: 15422|aciure@mozilla.com|testonly|2019-03-17 11:47:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=de3d7088cbc5)|Backed out changeset 2ce6dd37ff59 (bug 1535016) for mozlint failure on taskcluster/taskgraph/util/seta.py CLOSED TREE|aiakab@mozilla.com||2019-03-15 18:08:22|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9a96eceffaee)|[Bug 1535580 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535580) - update linux/mac searchfox jobs for clang changes; r=kats We need to install a new enough binutils for both of these jobs and ensure that it's properly found on the linux job. Differential Revision: https://phabricator.services.mozilla.com/D23678|nfroyd@mozilla.com|kats|2019-03-15 17:34:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2ce6dd37ff59)|[Bug 1535016 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535016) - Don't treat any Android job as new job r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23674|igoldan@mozilla.com|jmaher|2019-03-15 17:32:48|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7e14986df45a)|[Bug 1533133 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533133) - Split up macOS JIT tests in more chunks. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23116|gpascutto@mozilla.com|jmaher|2019-03-15 17:09:22|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c1674c1e4e7c)|[Bug 1535011 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535011) vendor latest `robustcheckout` from version-control-tools r=Callek This commit vendors `robustcheckout` from the version-control-tools repository, revision 8e3bb142dfa9. Differential Revision: https://phabricator.services.mozilla.com/D23566|cosheehan@mozilla.com|Callek|2019-03-15 16:03:12|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c1674c1e4e7c)|[Bug 1535011 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535011) vendor latest `robustcheckout` from version-control-tools r=Callek This commit vendors `robustcheckout` from the version-control-tools repository, revision 8e3bb142dfa9. Differential Revision: https://phabricator.services.mozilla.com/D23566|aciure@mozilla.com|Callek|2019-03-17 11:50:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7e14986df45a)|[Bug 1533133 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533133) - Split up macOS JIT tests in more chunks. r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23116|aciure@mozilla.com|jmaher|2019-03-17 11:50:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2ce6dd37ff59)|[Bug 1535016 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535016) - Don't treat any Android job as new job r=jmaher Differential Revision: https://phabricator.services.mozilla.com/D23674|aciure@mozilla.com|jmaher|2019-03-17 11:50:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=9a96eceffaee)|[Bug 1535580 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535580) - update linux/mac searchfox jobs for clang changes; r=kats We need to install a new enough binutils for both of these jobs and ensure that it's properly found on the linux job. Differential Revision: https://phabricator.services.mozilla.com/D23678|aciure@mozilla.com|kats|2019-03-17 11:50:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=de3d7088cbc5)|Backed out changeset 2ce6dd37ff59 (bug 1535016) for mozlint failure on taskcluster/taskgraph/util/seta.py CLOSED TREE|aciure@mozilla.com||2019-03-17 11:50:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=893781729409)|[Bug 1534737 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534737) use new tooltool packages with updates to adb r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D23534|aciure@mozilla.com|gbrown|2019-03-17 11:50:10|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=97385559862c)|[Bug 1529052 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1529052) [wpt PR 15422] - Do not throw from taskcluster-run.py if wpt fails, a=testonly Automatic update from web-platform-tests Do not throw from taskcluster-run.py if wpt fails Previously when `wpt run` stability check fails, the wrapper script taskcluster-run.py would throw an uncaught exception, which might be confused with an infra error. This change makes taskcluster-run.py return a non-zero exit code without printing the traceback. -- wpt-commits: 322981aed92da3b8fa13eb53f25acb8d3a9cb467 wpt-pr: 15422|james@hoppipolla.co.uk|testonly|2019-03-15 20:18:45|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=292ed1bb9143)|[Bug 1451104 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1451104) - part 4 - sync up gcc-related toolchains and linux64-binutils binutils version; r=glandium We're going to copy an x86_64-unknown-linux-gnu ld into the clang build, which clang will then use in preference to things on PATH. We therefore need to ensure that this ld is the same ld as would be used for other builds, such as PGO. This change is the most expedient way to do that; future work will make the gcc job(s) depend on linux64-binutils directly. Differential Revision: https://phabricator.services.mozilla.com/D22882|opoprus@mozilla.com|glandium|2019-03-15 11:46:56|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=858b68d306f2)|[Bug 1451104 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1451104) - part 5 - move toolchains off GCC 4.9; r=glandium Firefox itself has moved on to GCC 6.x; we can move our toolchains along too. Differential Revision: https://phabricator.services.mozilla.com/D22883|opoprus@mozilla.com|glandium|2019-03-15 11:46:56|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=76a3b7b0c9d7)|[Bug 1451104 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1451104) - part 6 - don't remove the libstdc++ files from the mingw build; r=glandium History does not disclose why we needed this, but in the brave new GCC 6-compiled world, deleting these files means that host links can no longer find libstdc++, which causes problems. Let's put the files back. Differential Revision: https://phabricator.services.mozilla.com/D22884|opoprus@mozilla.com|glandium|2019-03-15 11:46:56|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c6d92a71240c)|[Bug 1529052 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1529052) [wpt PR 15422] - Do not throw from taskcluster-run.py if wpt fails, a=testonly Automatic update from web-platform-tests Do not throw from taskcluster-run.py if wpt fails Previously when `wpt run` stability check fails, the wrapper script taskcluster-run.py would throw an uncaught exception, which might be confused with an infra error. This change makes taskcluster-run.py return a non-zero exit code without printing the traceback. -- wpt-commits: 322981aed92da3b8fa13eb53f25acb8d3a9cb467 wpt-pr: 15422|aciure@mozilla.com|testonly|2019-03-17 11:45:26|
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
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=0607c72b4d88)|[Bug 1535026 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535026) - [marionette] 'mach marionette-test' should force e10s disabled for Fennec. r=ato Differential Revision: https://phabricator.services.mozilla.com/D23401|nbeleuzu@mozilla.com|ato|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=203ed6d898c1)|[Bug 1533043 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533043) - [python-test] Add ability for individual tests to have pypi dependencies, r=davehunt Sometimes tools install pypi at runtime via mach (e.g self.install_pip_package / self.install_pip_requirements). It's difficult to test these modules with pytest because we usually won't be going through mach. This gives tests the ability to depend on external pypi packages the same way they might get installed when running via mach. Note, I only added support for requirements.txt here because python/mozbuild/mozbuild/virtualenv.py's 'install_pip_package' function is completely busted with modern pip. And the pip used with |mach python-test| is more modern than the one used with the regular build venv due to pipenv. We'll need to fix this eventually, but that's another bug for another day. Differential Revision: https://phabricator.services.mozilla.com/D22784|nbeleuzu@mozilla.com|davehunt|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=8a144ea41396)|[Bug 1533043 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533043) - [chooser] Use a requirements file to install |mach try chooser| dependencies, r=davehunt Not only is it best practice to pin dependencies and check hashes, but this will allow tests to install these dependencies as well. Depends on D22784 Differential Revision: https://phabricator.services.mozilla.com/D22785|nbeleuzu@mozilla.com|davehunt|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=88f164145918)|No bug: [mozharness] Use the absolute path when download secretes, to aid debugging; r=aki Differential Revision: https://phabricator.services.mozilla.com/D23465|nbeleuzu@mozilla.com|aki|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=210d55a03877)|[Bug 1535350 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535350) - remove win32-clang-tidy job; r=dmajor Updating clang indicates that 32-bit compilation is substantially longer than 64-bit compilation, perhaps due to swapping. The compilation process is hitting the timeout limit shortly before the compilation process completes (~3681/3695 tasks according to ninja). We could tweak our clang build process to accommodate this job. But we don't support building on 32-bit Windows anymore, and we don't produce a 32-bit Windows clang either. So we shouldn't support a 32-bit Windows clang-tidy job either. Let's get rid of it. Differential Revision: https://phabricator.services.mozilla.com/D23517|nbeleuzu@mozilla.com|dmajor|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=eb2a987c6ba2)|[Bug 1534283 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534283) - add a 'tasks_for' property; r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D23569|nbeleuzu@mozilla.com|tomprince|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=e44be7f40c6d)|[Bug 1534283 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534283) - filter out tasks when DONT-BUILD is in the message r=aki,tomprince (without the dash, because I want *this* push to build) This filters out all tasks, but that means that several things will still run: * docker images and tasks they depend on (debian packages) * always_run tasks (various python-y things) Differential Revision: https://phabricator.services.mozilla.com/D23020|nbeleuzu@mozilla.com|aki,tomprince|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=6e05f81a2f8f)|[Bug 1534283 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534283) - use default parameters for mach try fuzzy r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D23225|nbeleuzu@mozilla.com|tomprince|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=292ed1bb9143)|[Bug 1451104 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1451104) - part 4 - sync up gcc-related toolchains and linux64-binutils binutils version; r=glandium We're going to copy an x86_64-unknown-linux-gnu ld into the clang build, which clang will then use in preference to things on PATH. We therefore need to ensure that this ld is the same ld as would be used for other builds, such as PGO. This change is the most expedient way to do that; future work will make the gcc job(s) depend on linux64-binutils directly. Differential Revision: https://phabricator.services.mozilla.com/D22882|nbeleuzu@mozilla.com|glandium|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=858b68d306f2)|[Bug 1451104 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1451104) - part 5 - move toolchains off GCC 4.9; r=glandium Firefox itself has moved on to GCC 6.x; we can move our toolchains along too. Differential Revision: https://phabricator.services.mozilla.com/D22883|nbeleuzu@mozilla.com|glandium|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=76a3b7b0c9d7)|[Bug 1451104 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1451104) - part 6 - don't remove the libstdc++ files from the mingw build; r=glandium History does not disclose why we needed this, but in the brave new GCC 6-compiled world, deleting these files means that host links can no longer find libstdc++, which causes problems. Let's put the files back. Differential Revision: https://phabricator.services.mozilla.com/D22884|nbeleuzu@mozilla.com|glandium|2019-03-15 22:00:07|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=c594aee5b7a4)|Merge mozilla-central to mozilla-beta. a=same-version-merge l10n=same-version-merge on a CLOSED TREE|nbeleuzu@mozilla.com|same-version-merge|2019-03-15 22:00:07|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=d5aae246f088)|[Bug 1534283 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534283) - add a 'tasks_for' property; r=tomprince, a=tomprince Differential Revision: https://phabricator.services.mozilla.com/D23569|dmitchell@mozilla.com|tomprince,|2019-03-15 16:41:25|
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=1936822aea92)|[Bug 1525421 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1525421) - parse out just the try syntax from the commit message r=tomprince This mirrors what mozilla-taskcluster does in https://github.com/taskcluster/mozilla-taskcluster/blob/cb3de4c31e418f7dc1d89cffeeb28ad6a9dae610/src/jobs/taskcluster_graph.js#L46-L58 Differential Revision: https://phabricator.services.mozilla.com/D18748|dmitchell@mozilla.com|tomprince|2019-03-15 16:41:25|
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=2f877e90ff57)|[Bug 1534283 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534283) - filter out tasks when DONT-BUILD is in the message r=aki,tomprince, a=tomprince (without the dash, because I want *this* push to build) This filters out all tasks, but that means that several things will still run: * docker images and tasks they depend on (debian packages) * always_run tasks (various python-y things) Differential Revision: https://phabricator.services.mozilla.com/D23020|dmitchell@mozilla.com|aki,tomprince,|2019-03-15 16:41:25|
|[Link](https://hg.mozilla.org/releases/mozilla-release/pushloghtml?changeset=980321059007)|[Bug 1534283 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1534283) - use default parameters for mach try fuzzy r=tomprince, a=tomprince, DONTBUILD Differential Revision: https://phabricator.services.mozilla.com/D23225|dmitchell@mozilla.com|tomprince,|2019-03-15 16:41:25|

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/0a04738519cd8b1157ebbe908923dd8c6ef0d17f)|Merge pull request #446 from djmitche/bug1533591-b  Bug 1533591 - minor fixes|djmitche|N/A|2019-03-15 21:33:36|
|[Link](https://github.com/taskcluster/taskcluster/commit/aefcb9c347e65f5802a693129013fd4a310fae86)|Merge pull request #430 from owlishDeveloper/bug1534294  Retry 404 and higher errors|owlishDeveloper|N/A|2019-03-15 21:17:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/9aad62e957e693249b21d31a06ee510411630788)|Bug 1533591 - minor fixes|djmitche|N/A|2019-03-15 20:24:16|
|[Link](https://github.com/taskcluster/taskcluster/commit/2e79eecd3d11ee6fe1f6e838d4999edb3082bbd6)|Merge pull request #437 from djmitche/bug1533591  Bug 1533591 - issue JWTs with a user-specified audience / wstClient|djmitche|N/A|2019-03-15 20:10:26|
|[Link](https://github.com/taskcluster/taskcluster/commit/d719bec93451d02fa5af40e87d8e2afc5b616034)|Nit: Search padding (#434)|helfi92|N/A|2019-03-15 12:57:06|
|[Link](https://github.com/taskcluster/taskcluster/commit/93cae097359a853ce4f54d2289cbe49d10a43c9b)|Reduce padding in Search component (#433)|helfi92|N/A|2019-03-15 12:50:58|
|[Link](https://github.com/taskcluster/taskcluster/commit/79e54aae1eeb70cba46defb4e6de0c975a66bb57)|Make live logs button more prominent (#432)|helfi92|N/A|2019-03-15 12:28:24|

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
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=76ec900ec82d)|[Bug 1535635 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1535635) - make features.taskcluster-push enable hg-pushes; r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D23722|dmitchell@mozilla.com|tomprince|2019-03-15 23:37:51|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=90efa66ecf6e)|[Bug 1526979 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526979) - enable push-via-hooks for try-comm-central; a=tomprince|dmitchell@mozilla.com|tomprince|2019-03-15 16:53:37|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=8980c7a103df)|[Bug 1471367 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1471367) - add subcommand to print taskcluster.yml hashes r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22358|dmitchell@mozilla.com|dustin|2019-03-17 15:28:56|
