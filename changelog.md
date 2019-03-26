##  Commits in production - for 3 days, generated on: 2019-03-26 22:01:07 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=aea38cfc632a)|Backed out 19 changesets [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  for causing upload symbol bustages. CLOSED TREE Backed out changeset 4943b23813fe [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 4b9413d05816 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 3e2b6a495e8c [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 51ab82722846 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 4b027c970719 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 6b65273fab78 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset d7deec98601a [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset b95b3f4e5243 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 7cefe92f88d5 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset f64dfaf86a2e [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 686c228e3579 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset dd2eddef8b43 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset fc16a3ecfe68 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset b31cbe91bdf7 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 694eac65a72e [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 6044aedac9c4 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 456538d78b36 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 01699fb72384 [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  Backed out changeset 4a2e544fea0d [Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113) |csabou@mozilla.com||2019-03-26 22:27:29|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4a2e544fea0d)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - allow raptor tests to run for shippable (ends up scheduling shippable builds, due to deps. r=jmaher raptor-chrome is Google Chrome and only needs to run once per day, so mozilla-central pushes and try. raptor-profiling is primarily for devs to have up to date profile information and it too only needs to run once per day. TODO is to try and find a clean way to make them only run when we trigger Nightlies rather than every m-c push. Differential Revision: https://phabricator.services.mozilla.com/D22832|jwood@mozilla.com|jmaher|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=01699fb72384)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - utilize run-on-projects more for previously excluded tests. r=jmaher Effectively back out much of the run on projects from D22710 This also has the added affect of scheduling the shippable builds to run because of dependencies. Differential Revision: https://phabricator.services.mozilla.com/D22833|jwood@mozilla.com|jmaher|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=456538d78b36)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Start explicitly running shippable jobs per-push. r=aki Differential Revision: https://phabricator.services.mozilla.com/D22834|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6044aedac9c4)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Adjust tests to align shippable sets with what was on pgo (where pgo exists) and opt. r=jmaher I did a bunch of manual testing with this, the biggest uncertainties lie around beta and central/nightly. We are adding shippable-qr to beta because of replacing nightly too. Autoland and inbound should have the same sets of tasks. beta - - adds mochitest-plain-headless-{1..4} to beta (not currently run) - adds raptor to run on shippable for beta - currently runs on opt on beta, and for nightly tasks on beta only webaudio-chrome runs. - adds talos to shippable tasks, on beta talos only runs against opt. central - - adds browser-screenshots to nightly graph - adds mochitest-plain-headless-{1..4} to nightly graph - adds browser-instrumentation to shippable Differential Revision: https://phabricator.services.mozilla.com/D23122|jwood@mozilla.com|jmaher|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=694eac65a72e)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Switch l10n jobs to be based on shippable builds. r=aki Differential Revision: https://phabricator.services.mozilla.com/D23123|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b31cbe91bdf7)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Make source-test depend on shippable instead of pgo. r=aki This is useful in order to not have to run linux64/opt on push, especially on autoland/inbound when we need a source test. It is also required if we remove the linux64-pgo build type entirely. Differential Revision: https://phabricator.services.mozilla.com/D23124|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=fc16a3ecfe68)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Remove windows pgo entirely. r=jmaher,aki Differential Revision: https://phabricator.services.mozilla.com/D23125|jwood@mozilla.com|jmaher,aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=dd2eddef8b43)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Do not do linux32/opt build on integration. r=aki Differential Revision: https://phabricator.services.mozilla.com/D23248|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=686c228e3579)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Do not run linux32/opt tests, we now run them for linux32-shippable/opt. r=jmaher Should there end up being a need we can back out this patch and let them run, but :jmaher indicated he was happy with dropping them entirely and not duplicating. Differential Revision: https://phabricator.services.mozilla.com/D23383|jwood@mozilla.com|jmaher|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f64dfaf86a2e)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Do not do linux pgo either. r=jmaher,aki Differential Revision: https://phabricator.services.mozilla.com/D23126|jwood@mozilla.com|jmaher,aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7cefe92f88d5)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Don't run OSX opt builds by default on integration trees. r=aki Differential Revision: https://phabricator.services.mozilla.com/D23128|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b95b3f4e5243)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Do not run opt-only OSX tests on integration trees. r=jmaher This also relates to [Bug 1522111](https://bugzilla.mozilla.org/show_bug.cgi?id=1522111)  where we turned off opt tests in favor of pgo, shippable is like the new pgo so do that. This has a side affect of adding talos-tp6-stylo-threads to inbound for osx-shippable (previously was only on autoland). This has no practical affect after D23382 is applied (because of lack of OSX capacity) Differential Revision: https://phabricator.services.mozilla.com/D23129|jwood@mozilla.com|jmaher|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d7deec98601a)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Do not run any macosx64/opt or macosx64-qr/opt tests, leaving only shippable. r=jmaher Jmaher indicated we do not have the test capacity to incur this as a duplicated set Differential Revision: https://phabricator.services.mozilla.com/D23382|jwood@mozilla.com|jmaher|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4b027c970719)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - make only-for-attributes accept any() instead of all() in the set. r=aki Differential Revision: https://phabricator.services.mozilla.com/D23130|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=51ab82722846)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Support shippable where 'nightly' is used. r=aki Makes most kinds that reference nightly attribute reference the shippable attribute. Also makes most transforms that use nightly use shippable Transfers dependencies/ownership for some things to shippable from nightly where it was harder to support both. In no particular order, full list: Send shippable attribute down to dep tasks. Set tests as shippable attribute Add new signing routes Add shippable routes to repackage_routes transform Adjust target tasks Add shippable nightly-l10n Add nightly-signing and as a side affect add repackage and repackage-signing Add support for proper balrog platforms for shippable Add shippable to the nightly sccache guard Fix TC_PLATFORM_PER_FTP in partners.py to use shippable Add shippable to mozharness_test variants Only actually used for android which doesn't have shippable at this time. Add shippable variant to beetmover transforms Do nightly signing for mars on shippable Support shippable in partner-repack transform Support shippable in amo langpacks transform Use proper signing for shippable tasks in repackage transforms Set upload symbols to use shippable too Use shippable as deps for geckodriver extraction Use shippable as dep for autograph-stage signing Do not run beetmover-l10n for shippable Run shippable style jobs for repackage signing Set build_platform for update verify and uvc to be shippable Run repackage-msi for shippable Add shippable to osx partner repack signing add shippable to emefree repackage add shippable to emefree repackage signing add shippable to beetmover checksums Add shippable to partner repack repackage signing add partner repack beetmover Add shippable to mar signing Add shippable to mar-signing-l10n add shippable to eme free beetmover checksums Add shippable to upload-generated-sources Add beetmover langpacks to shippable Add repackage-l10n to shippable Add shippable to partner repack chunk-dummy Do eme free builds with shippable Add signing of language packs to shippable Add snap repackage for shippable Add shippable for release-eme-free repack signing Add partials for shippable Add partner repack repackage for shippable Add emefree beetmover for shippable Add checksums-signing to shippable Switch partner repacks to shippable Add shippable to beetmover-repackage Add secondary update verify configs for shippable secondary update verify for shippable Differential Revision: https://phabricator.services.mozilla.com/D24699|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3e2b6a495e8c)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Remove nightly build types replaced by shippable. r=aki Differential Revision: https://phabricator.services.mozilla.com/D24700|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4b9413d05816)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Update index routes for shippable. Try to be backwards compat where possible. r=aki Differential Revision: https://phabricator.services.mozilla.com/D24829|jwood@mozilla.com|aki|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4943b23813fe)|[Bug 1352113](https://bugzilla.mozilla.org/show_bug.cgi?id=1352113)  - Shippable Builds - Account for new declarative artifacts work. r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D24831|jwood@mozilla.com|mtabara|2019-03-26 20:36:08|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2aea0bb2df47)|[Bug 1521752](https://bugzilla.mozilla.org/show_bug.cgi?id=1521752)  - Run other DevTools jest tests on try;r=jlast,ahal Depends on D24145. Differential Revision: https://phabricator.services.mozilla.com/D24146|jdescottes@mozilla.com|jlast,ahal|2019-03-26 19:21:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=188ea7716008)|[Bug 1521752](https://bugzilla.mozilla.org/show_bug.cgi?id=1521752)  - Create jest test for aboutdebugging-new Message component;r=ladybenko Depends on D24146 Example of a try run with tests running: https://treeherder.mozilla.org/#/jobs?repo=try&revision=cca3978c6e3eb042c59e62b25b1946219cf3d74a&selectedJob=235873038 Differential Revision: https://phabricator.services.mozilla.com/D24721|jdescottes@mozilla.com|ladybenko|2019-03-26 19:21:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f755dfcfc421)|Backed out 3 changesets [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  for /css/css-* failures CLOSED TREE Backed out changeset e8758002d7d4 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  Backed out changeset 795287b1e059 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  Backed out changeset 9a680e886248 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804) |btara@mozilla.com||2019-03-26 18:43:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9e8fee5e4f3d)|[Bug 1519825](https://bugzilla.mozilla.org/show_bug.cgi?id=1519825)  - Update grcov to revision 9214a916805838265764f9c69eaed657ea3db021 r=marco This revision corresponds to grcov 0.4.2 Differential Revision: https://phabricator.services.mozilla.com/D16465|csabou@mozilla.com|marco|2019-03-25 19:17:14|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=775f40c959fc)|[Bug 1538134](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134)  [mozharness] Set repository path in taskcluster; r=aki Taskcluster has authorative information about the repository being built, so pass that to mozharness, rather than have mozharness reconstruct it from hand-maintained mozharness config. Differential Revision: https://phabricator.services.mozilla.com/D24561|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=db11228c8a38)|[Bug 1538134](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134)  [mozharness] Remove explicit setting of branches to use release promotion; r=aki The only thing this affects is the default update channel, but for shipping builds, this is set explicitly via taskcluster, and for other branches, defaults to `default`. Differential Revision: https://phabricator.services.mozilla.com/D24562|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3e4b58569126)|[Bug 1538134](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134)  [mozharness] Don't override PGO settings per-branch; r=aki The release mozconfigs set `MOZ_PGO` and all shipping builds set the `nightly` mozharness config, so we don't need to additionaly set PGO based on the branch. Differential Revision: https://phabricator.services.mozilla.com/D24563|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d5c2b9a1c215)|[Bug 1538134](https://bugzilla.mozilla.org/show_bug.cgi?id=1538134)  [mozharness] Remove support for unused `builds/branch_specifics.py` config; r=aki We have moved per-branch configuration to taskcluster, so we can remove that support in mozharness. Differential Revision: https://phabricator.services.mozilla.com/D24564|mozilla@hocat.ca|aki|2019-03-25 18:06:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=02b78c6e3ca7)|[Bug 1536839](https://bugzilla.mozilla.org/show_bug.cgi?id=1536839)  - Add json formatter to ./mach clang-format, r=ahal,marco Depends on D24193 Differential Revision: https://phabricator.services.mozilla.com/D24194|babadie@mozilla.com|ahal,marco|2019-03-25 17:04:23|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=486437866d00)|[Bug 1535679](https://bugzilla.mozilla.org/show_bug.cgi?id=1535679)  - switch Firefox nightlies to declarative artifacts. r=sfraser a=release Linter fixes. Differential Revision: https://phabricator.services.mozilla.com/D24214|mtabara@mozilla.com|sfraser|2019-03-25 15:50:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5a3f8b7e664c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D24676|sfraser@mozilla.com|sfraser|2019-03-25 13:08:53|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4d546ab0dc94)|[Bug 1538475](https://bugzilla.mozilla.org/show_bug.cgi?id=1538475)  - Add comma to 'central-to-beta' and 'beta-to-release' generators to prevent concatenation of two folder paths of files to modify r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D24602|archaeopteryx@coole-files.de|jlorenzo|2019-03-25 11:25:37|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=43ac43ba6cf4)|[Bug 1536836](https://bugzilla.mozilla.org/show_bug.cgi?id=1536836)  - Support multiple formatters with file output in ./mach lint, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24193|babadie@mozilla.com|ahal|2019-03-25 11:17:44|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=e8758002d7d4)|[Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  - Add a task for summarising wpt metadata, r=ahal This task runs on wpt metadata changes and uploads an artifact containing the summarised metadata. Depends on D24178 Differential Revision: https://phabricator.services.mozilla.com/D24179|dvarga@mozilla.com|ahal|2019-03-27 00:00:04|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=f755dfcfc421)|Backed out 3 changesets [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  for /css/css-* failures CLOSED TREE Backed out changeset e8758002d7d4 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  Backed out changeset 795287b1e059 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  Backed out changeset 9a680e886248 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804) |dvarga@mozilla.com||2019-03-27 00:00:04|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2aea0bb2df47)|[Bug 1521752](https://bugzilla.mozilla.org/show_bug.cgi?id=1521752)  - Run other DevTools jest tests on try;r=jlast,ahal Depends on D24145. Differential Revision: https://phabricator.services.mozilla.com/D24146|dvarga@mozilla.com|jlast,ahal|2019-03-27 00:00:04|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=188ea7716008)|[Bug 1521752](https://bugzilla.mozilla.org/show_bug.cgi?id=1521752)  - Create jest test for aboutdebugging-new Message component;r=ladybenko Depends on D24146 Example of a try run with tests running: https://treeherder.mozilla.org/#/jobs?repo=try&revision=cca3978c6e3eb042c59e62b25b1946219cf3d74a&selectedJob=235873038 Differential Revision: https://phabricator.services.mozilla.com/D24721|dvarga@mozilla.com|ladybenko|2019-03-27 00:00:04|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=43ac43ba6cf4)|[Bug 1536836](https://bugzilla.mozilla.org/show_bug.cgi?id=1536836)  - Support multiple formatters with file output in ./mach lint, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24193|aiakab@mozilla.com|ahal|2019-03-25 17:58:26|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4d546ab0dc94)|[Bug 1538475](https://bugzilla.mozilla.org/show_bug.cgi?id=1538475)  - Add comma to 'central-to-beta' and 'beta-to-release' generators to prevent concatenation of two folder paths of files to modify r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D24602|aiakab@mozilla.com|jlorenzo|2019-03-25 17:58:26|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5a3f8b7e664c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D24676|aiakab@mozilla.com|sfraser|2019-03-25 17:58:26|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e8758002d7d4)|[Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  - Add a task for summarising wpt metadata, r=ahal This task runs on wpt metadata changes and uploads an artifact containing the summarised metadata. Depends on D24178 Differential Revision: https://phabricator.services.mozilla.com/D24179|dvarga@mozilla.com|ahal|2019-03-26 23:49:44|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f755dfcfc421)|Backed out 3 changesets [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  for /css/css-* failures CLOSED TREE Backed out changeset e8758002d7d4 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  Backed out changeset 795287b1e059 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804)  Backed out changeset 9a680e886248 [Bug 1536804](https://bugzilla.mozilla.org/show_bug.cgi?id=1536804) |dvarga@mozilla.com||2019-03-26 23:49:44|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2aea0bb2df47)|[Bug 1521752](https://bugzilla.mozilla.org/show_bug.cgi?id=1521752)  - Run other DevTools jest tests on try;r=jlast,ahal Depends on D24145. Differential Revision: https://phabricator.services.mozilla.com/D24146|dvarga@mozilla.com|jlast,ahal|2019-03-26 23:49:44|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=188ea7716008)|[Bug 1521752](https://bugzilla.mozilla.org/show_bug.cgi?id=1521752)  - Create jest test for aboutdebugging-new Message component;r=ladybenko Depends on D24146 Example of a try run with tests running: https://treeherder.mozilla.org/#/jobs?repo=try&revision=cca3978c6e3eb042c59e62b25b1946219cf3d74a&selectedJob=235873038 Differential Revision: https://phabricator.services.mozilla.com/D24721|dvarga@mozilla.com|ladybenko|2019-03-26 23:49:44|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=43ac43ba6cf4)|[Bug 1536836](https://bugzilla.mozilla.org/show_bug.cgi?id=1536836)  - Support multiple formatters with file output in ./mach lint, r=ahal Differential Revision: https://phabricator.services.mozilla.com/D24193|aiakab@mozilla.com|ahal|2019-03-25 17:52:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4d546ab0dc94)|[Bug 1538475](https://bugzilla.mozilla.org/show_bug.cgi?id=1538475)  - Add comma to 'central-to-beta' and 'beta-to-release' generators to prevent concatenation of two folder paths of files to modify r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D24602|aiakab@mozilla.com|jlorenzo|2019-03-25 17:52:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5a3f8b7e664c)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D24676|aiakab@mozilla.com|sfraser|2019-03-25 17:52:30|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=b057c733c952)|[Bug 1535679](https://bugzilla.mozilla.org/show_bug.cgi?id=1535679)  - switch Firefox nightlies to declarative artifacts. r=sfraser a=release Linter fixes. Differential Revision: https://phabricator.services.mozilla.com/D24214|mtabara@mozilla.com|sfraser|2019-03-26 21:03:50|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

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
|[Link](https://github.com/taskcluster/taskcluster/commit/b3f58d533c090442d0de33841ee5264e2a52860b)|Merge pull request #495 from djmitche/bug1538996  Bug 1538996 - fix module loading with new raw loader|djmitche|N/A|2019-03-26 20:00:14|
|[Link](https://github.com/taskcluster/taskcluster/commit/143871d458b9d4c44f71f111c7fe3e9c805ae6bb)|Merge pull request #482 from djmitche/allcontributors-in-docs  Use allcontributors in docs|djmitche|N/A|2019-03-26 12:43:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/1da427860a8d2bc2f8c26e0487530891b268022c)|[UI] Add skip to content- keyboard accessibility (#496)  [UI] Add skip to content- keyboard accessibility|Aditya-Kolla|N/A|2019-03-26 12:22:56|
|[Link](https://github.com/taskcluster/taskcluster/commit/bd8f72a9ecc8ef68ee281955d20166024a44cb68)|Merge pull request #494 from taskcluster/typo-fix  Typo fix|djmitche|N/A|2019-03-25 19:13:06|
|[Link](https://github.com/taskcluster/taskcluster/commit/da10730fd46c720ad3db4acea74049a99e1d05db)|Tyop fxi ;)|petemoore|N/A|2019-03-25 19:06:48|
|[Link](https://github.com/taskcluster/taskcluster/commit/b3c5082752df072263c7da1d7b53a8fe0a8fbefe)|Merge pull request #481 from taskcluster/issue-479  Cleanup logs docs pages|imbstack|N/A|2019-03-25 18:47:11|
|[Link](https://github.com/taskcluster/taskcluster/commit/bed82c7c4881fab007eecb8bf1cfe1c6033810f5)|Show access token when creating a client (#489)|helfi92|N/A|2019-03-25 17:26:24|
|[Link](https://github.com/taskcluster/taskcluster/commit/02020bdea61450b4c3ec0cc0c21c507f7f0ab9e9)|Merge pull request #491 from taskcluster/renovate/raw-loader-2.x  Update dependency raw-loader to v2|djmitche|N/A|2019-03-25 13:51:44|
|[Link](https://github.com/taskcluster/taskcluster/commit/3cea3dd67620033912d99c9500a43d3af02d321c)|Merge pull request #463 from helfi92/nicer-getting-started-page  [UI] Add custom get started view|helfi92|N/A|2019-03-25 13:37:18|
|[Link](https://github.com/taskcluster/taskcluster/commit/aed11bbf3b0eba07caba51db539027090ce42ce0)|Update dependency raw-loader to v2|renovate-bot|N/A|2019-03-25 13:34:31|
|[Link](https://github.com/taskcluster/taskcluster/commit/182d385465c2abe482b18fcb15033715af7f3a88)|Merge pull request #493 from taskcluster/renovate/serialize-error-4.x  Update dependency serialize-error to v4|djmitche|N/A|2019-03-25 13:20:07|
|[Link](https://github.com/taskcluster/taskcluster/commit/6cc9ec0839d506243b5651a329d356abe8254db8)|Update dependency serialize-error to v4|renovate-bot|N/A|2019-03-25 13:05:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/d6d64d9ee9ea0e2fb7793a69259922b112067089)|Merge pull request #490 from taskcluster/renovate/eslint-5.x  Update dependency eslint to v5.15.3|djmitche|N/A|2019-03-25 13:04:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/fa15721bb6f1b9c0d91a20f72ce78ebcbe11aa31)|Adjust GetStarted url in markdown|helfi92|N/A|2019-03-25 12:47:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/a809600db384a67c6d7a18311d773cd0868dfe09)|Merge pull request #483 from djmitche/docs-error-handling  Simplify docs loading and improve error handling|djmitche|N/A|2019-03-23 22:46:38|

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
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)|FIC - BOT|Self Generated| - |

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
