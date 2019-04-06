##  Commits in production - for 3 days, generated on: 2019-04-06 14:29:56 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a765634b9ec2)|Backed out changeset ac130652ae81 [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  for Gecko Decision Task bustages. CLOSED TREE|rmaries@mozilla.com||2019-04-06 10:26:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=50447a9c4347)|[Bug 1529774](https://bugzilla.mozilla.org/show_bug.cgi?id=1529774)  - Upgrade builders to rust 1.33. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D24830|mh@glandium.org|froydnj|2019-04-06 01:21:26|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2e359f02ea62)|[Bug 1538703](https://bugzilla.mozilla.org/show_bug.cgi?id=1538703)  - roll-out declarative artifacts in Firefox. r=sfraser a=release|shindli@mozilla.com|sfraser|2019-04-06 00:51:45|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8cc6d083001b)|Merge inbound to mozilla-central. a=merge|shindli@mozilla.com|merge|2019-04-06 00:51:45|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=50495a5da9f6)|[Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  - [ci] Use 'mach python' to run mozharness scripts when we have a srcdir r=catlee This makes sure that the mozharness scripts have access to all the packages in the build system virtualenv (namely mozbase). Differential Revision: https://phabricator.services.mozilla.com/D22184|ahalberstadt@mozilla.com|catlee|2019-04-05 23:04:09|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c28c538fca0a)|[Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  - [mozharness] Remove copies of mozbase from testing/mozharness r=catlee Differential Revision: https://phabricator.services.mozilla.com/D22185|ahalberstadt@mozilla.com|catlee|2019-04-05 23:04:09|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e5ebda0bbbf1)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Specify bouncer-prefix in cron bouncer check as well; r=mtabara The previous changes only changed the check in the release process. This also updates the periodic check. Differential Revision: https://phabricator.services.mozilla.com/D26199|mozilla@hocat.ca|mtabara|2019-04-05 20:55:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=26eb65cf9325)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Don't restrict the branch that cron-bouncer-check runs on; r=mtabara We only run the cron job on release branches, so it will only get scheduled there. By not otherwise restricting the job, it makes it easier to test the cron job on other branches (like try). Differential Revision: https://phabricator.services.mozilla.com/D26200|mozilla@hocat.ca|mtabara|2019-04-05 20:55:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=648001848ed2)|[Bug 1539905](https://bugzilla.mozilla.org/show_bug.cgi?id=1539905)  Ensure a copy is taken of memoized values r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D26306|sfraser@mozilla.com|mtabara|2019-04-05 18:14:30|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4de00f3a05ad)|[Bug 1531032](https://bugzilla.mozilla.org/show_bug.cgi?id=1531032)  disable tier2 jobs from running with try syntax unless specifically enabled. r=tomprince Enable WPT-reftests as tier1 Differential Revision: https://phabricator.services.mozilla.com/D21786|catlee@mozilla.com|tomprince|2019-04-05 17:12:11|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0913f775a771)|Backed out changeset e2a6e9aafcf6 [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  for gecko decision task failure. CLOSED TREE|ncsoregi@mozilla.com||2019-04-05 16:20:15|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e2a6e9aafcf6)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|ncsoregi@mozilla.com|bastien|2019-04-05 16:15:19|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7b3fc26d7fbb)|Backed out changeset 3779175a4d7f [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  for gecko decision bustage. CLOSED TREE|ncsoregi@mozilla.com||2019-04-05 15:54:21|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3779175a4d7f)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|bpostelnicu@mozilla.com|bastien|2019-04-05 15:27:43|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b948a38f204a)|[Bug 1541957](https://bugzilla.mozilla.org/show_bug.cgi?id=1541957)  - [ci] Fix regression causing geckoview tests to run without e10s, r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D26240|ahalberstadt@mozilla.com|gbrown|2019-04-05 15:13:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=93075ec49df3)|Backed out 2 changesets [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  for l10n bustages a=backout Backed out changeset 9645ac1a9851 [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  Backed out changeset 4de7f94119fd [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299) |btara@mozilla.com|backout|2019-04-05 14:13:50|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=230bb363f2f3)|Merge mozilla-central to inbound|btara@mozilla.com||2019-04-05 12:56:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=83c38c0e430b)|Merge mozilla-central to inbound a=merge|btara@mozilla.com|merge|2019-04-05 12:56:32|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=20750a2dc85b)|[Bug 1541943](https://bugzilla.mozilla.org/show_bug.cgi?id=1541943)  - Temporarily switch libFuzzer builds back to clang-7. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D26194|choller@mozilla.com|froydnj|2019-04-05 09:55:21|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6373b5616e00)|[Bug 1541131](https://bugzilla.mozilla.org/show_bug.cgi?id=1541131)  - 'try -b o -p macosx64 -u all' should trigger Mac opt tests to be run, on shippable. r=ahal With the shift to shippable builds we no longer run tests on osx/opt though many still push to try with old try syntax using -p macosx64 and get surprised by no tests. This patch fixes it as a bandaid by appending macosx64-shippable as a platform when macosx64 is specified, making the tests run in the appropriate cases. The expectation with the methodology of this patch is that we'll be killing try syntax support in the near future, eliminating the need for these sorts of bandaids Differential Revision: https://phabricator.services.mozilla.com/D26048|jwood@mozilla.com|ahal|2019-04-04 19:04:13|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=425aab7d1e5a)|[Bug 1541835](https://bugzilla.mozilla.org/show_bug.cgi?id=1541835)  - Turn off mochitest webgl and media on arm64 for integration. r=aryx Turn off mochitest webgl and media on arm64 for integration. Differential Revision: https://phabricator.services.mozilla.com/D26122|jmaher@mozilla.com|aryx|2019-04-04 16:02:24|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b2f3367509f9)|[Bug 1541835](https://bugzilla.mozilla.org/show_bug.cgi?id=1541835)  - only run windows/aarch64 tests on m-c/try, not autoland/inbound. r=aryx only run windows/aarch64 tests on m-c/try, not autoland/inbound Differential Revision: https://phabricator.services.mozilla.com/D26093|jmaher@mozilla.com|aryx|2019-04-04 13:43:44|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6dc5bafd6649)|[Bug 1536555](https://bugzilla.mozilla.org/show_bug.cgi?id=1536555)  - run tc win builds on gcp at tier 3 r=coop,pmoore this change adds support for parallel gcp builds for the following windows build configurations: - win32 - opt - debug - pgo - win64 - opt - debug - pgo gcp builds are triggered with a treeherder tier 3 flag so that they are only displayed in the treeherder ui when the user has a tier 3 flag set. gcp builds use a th build symbol of "Bg" to make them easy to differentiate from ec2 builds in the treeherder ui. gcp builds use a perfherder "gcp" flag to make them easier to differentiate from ec2 builds in the perfherder ui. Differential Revision: https://phabricator.services.mozilla.com/D24865|nerli@mozilla.com|coop,pmoore|2019-04-04 09:59:50|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=29ca2ad7266b)|[Bug 1541121](https://bugzilla.mozilla.org/show_bug.cgi?id=1541121)  [try-staging] Simplify the logic for getting partial update configration; r=aki The original code was converting to json, then comparing against `{}`. This switches things around so that json is only generated where it is directly used a json. Differential Revision: https://phabricator.services.mozilla.com/D24833|mozilla@hocat.ca|aki|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=948b7b1003af)|[Bug 1541121](https://bugzilla.mozilla.org/show_bug.cgi?id=1541121)  [try-staging] Allow staging release to not have partials; r=aki We check that partials as a safety check. But we don't need that for staging builds, and it is often useful to be able to test things that don't depend on partials. The shipit UI currently still requires partials, but that can be worked around using the react dev tools. Differential Revision: https://phabricator.services.mozilla.com/D24834|mozilla@hocat.ca|aki|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0ff766eb6349)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  Support generating update-verify-config for new configuration; r=aki When adding a new platform, the first release will be at the watershed, and there will be no update paths. Rather than failing in this case (requiring the update-verify setup happen after the first release), generate an empty config which will allow the later tasks to turn green. Differential Revision: https://phabricator.services.mozilla.com/D25833|mozilla@hocat.ca|aki|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0c4e9114a199)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  Add win64-aarch64 update verify configuration; r=aki Differential Revision: https://phabricator.services.mozilla.com/D25834|mozilla@hocat.ca|aki|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1339cb993b08)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Support bouncer-check in staging; r=aki Differential Revision: https://phabricator.services.mozilla.com/D25835|mozilla@hocat.ca|aki|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0e5ad75bf07d)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [mozharness] Remove unused bouncer_check config entries; r=mtabara I beleive these entries date from when bouncer config was handled by mozharness rather than bounerscript and are now obsolete. Differential Revision: https://phabricator.services.mozilla.com/D25836|mozilla@hocat.ca|mtabara|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=111aa230d41e)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [mozharness] Remove unused bouncer configuration for fennect; r=mtabara Fennec doesn't have a bouncer check task, and bouncer is update via bouncerscript. Differential Revision: https://phabricator.services.mozilla.com/D25837|mozilla@hocat.ca|mtabara|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4daa02d1aa20)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [mozharness] Simplify bouncer-check configuration to not include paths; r=mtabara These existed for when bouncer was updated via mozharness, and they are unused in bouncer-check. By removing the paths, we make the configuration easier to read and update. Differential Revision: https://phabricator.services.mozilla.com/D25838|mozilla@hocat.ca|mtabara|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=310d07e69df5)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  Don't create fresh virtualenv for bouncer-check; r=mtabara In automation, the script is run with `mach python`, and all the dependencies are vendored, so just use them directly. Differential Revision: https://phabricator.services.mozilla.com/D25839|mozilla@hocat.ca|mtabara|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=e847d4ed0e22)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  [win64-aarch64] Add win64 aarch64 bouner-check configuration; r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D25840|mozilla@hocat.ca|mtabara|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=f9d9fb959d89)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  [win64-aarch64] Point win64-aarch64 stub bounce entries at the correct path; r=mtabara There was special case logic to map the win64 platform to win32, for stub entries. When win64-aarch64 was added no special case was added for that plaform, so they stub entries pointed at the incorrect place. This changes the configuration so that all stub entries point at the win32 paths, without needing special case code. Differential Revision: https://phabricator.services.mozilla.com/D25841|mozilla@hocat.ca|mtabara|2019-04-04 01:13:51|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=60420822a632)|[Bug 1540213](https://bugzilla.mozilla.org/show_bug.cgi?id=1540213)  - turn on green suites of windows10-aarch64 on taskgraph r=jmaher,gbrown Enables the list of suites as defined in [Bug 1540213](https://bugzilla.mozilla.org/show_bug.cgi?id=1540213)  - added new item in `test-sets.yml` for windows10-aarch64. - reference the new test-set in `test-platforms.yml`. Differential Revision: https://phabricator.services.mozilla.com/D25979|egao@mozilla.com|jmaher,gbrown|2019-04-04 01:12:27|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=486395fabe66)|[Bug 1532747](https://bugzilla.mozilla.org/show_bug.cgi?id=1532747)  - [ci] Create try-only raptor reference-browser tasks, r=jmaher,rwood These will run on android-hw against the latest reference browser nightly. Since they are try-only, they can only be scheduled with |mach try fuzzy --full|. Differential Revision: https://phabricator.services.mozilla.com/D25801|ahalberstadt@mozilla.com|jmaher,rwood|2019-04-04 01:09:40|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=50495a5da9f6)|[Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  - [ci] Use 'mach python' to run mozharness scripts when we have a srcdir r=catlee This makes sure that the mozharness scripts have access to all the packages in the build system virtualenv (namely mozbase). Differential Revision: https://phabricator.services.mozilla.com/D22184|apavel@mozilla.com|catlee|2019-04-06 14:10:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=c28c538fca0a)|[Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  - [mozharness] Remove copies of mozbase from testing/mozharness r=catlee Differential Revision: https://phabricator.services.mozilla.com/D22185|apavel@mozilla.com|catlee|2019-04-06 14:10:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=50447a9c4347)|[Bug 1529774](https://bugzilla.mozilla.org/show_bug.cgi?id=1529774)  - Upgrade builders to rust 1.33. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D24830|apavel@mozilla.com|froydnj|2019-04-06 14:10:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ac130652ae81)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|apavel@mozilla.com|bastien|2019-04-06 14:10:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a765634b9ec2)|Backed out changeset ac130652ae81 [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  for Gecko Decision Task bustages. CLOSED TREE|apavel@mozilla.com||2019-04-06 14:10:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b5167ef1c9ea)|Merge mozilla-central to mozilla-inbound on a CLOSED TREE|apavel@mozilla.com||2019-04-06 14:10:01|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2e359f02ea62)|[Bug 1538703](https://bugzilla.mozilla.org/show_bug.cgi?id=1538703)  - roll-out declarative artifacts in Firefox. r=sfraser a=release|mtabara@mozilla.com|sfraser|2019-04-05 19:30:36|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=93075ec49df3)|Backed out 2 changesets [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  for l10n bustages a=backout Backed out changeset 9645ac1a9851 [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  Backed out changeset 4de7f94119fd [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299) |btara@mozilla.com|backout|2019-04-05 14:14:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=20750a2dc85b)|[Bug 1541943](https://bugzilla.mozilla.org/show_bug.cgi?id=1541943)  - Temporarily switch libFuzzer builds back to clang-7. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D26194|btara@mozilla.com|froydnj|2019-04-05 12:57:50|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=50495a5da9f6)|[Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  - [ci] Use 'mach python' to run mozharness scripts when we have a srcdir r=catlee This makes sure that the mozharness scripts have access to all the packages in the build system virtualenv (namely mozbase). Differential Revision: https://phabricator.services.mozilla.com/D22184|apavel@mozilla.com|catlee|2019-04-06 13:57:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c28c538fca0a)|[Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  - [mozharness] Remove copies of mozbase from testing/mozharness r=catlee Differential Revision: https://phabricator.services.mozilla.com/D22185|apavel@mozilla.com|catlee|2019-04-06 13:57:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=50447a9c4347)|[Bug 1529774](https://bugzilla.mozilla.org/show_bug.cgi?id=1529774)  - Upgrade builders to rust 1.33. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D24830|apavel@mozilla.com|froydnj|2019-04-06 13:57:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ac130652ae81)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|apavel@mozilla.com|bastien|2019-04-06 13:57:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a765634b9ec2)|Backed out changeset ac130652ae81 [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  for Gecko Decision Task bustages. CLOSED TREE|apavel@mozilla.com||2019-04-06 13:57:50|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b948a38f204a)|[Bug 1541957](https://bugzilla.mozilla.org/show_bug.cgi?id=1541957)  - [ci] Fix regression causing geckoview tests to run without e10s, r=gbrown Differential Revision: https://phabricator.services.mozilla.com/D26240|shindli@mozilla.com|gbrown|2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3779175a4d7f)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|shindli@mozilla.com|bastien|2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7b3fc26d7fbb)|Backed out changeset 3779175a4d7f [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  for gecko decision bustage. CLOSED TREE|shindli@mozilla.com||2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e2a6e9aafcf6)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|shindli@mozilla.com|bastien|2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0913f775a771)|Backed out changeset e2a6e9aafcf6 [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  for gecko decision task failure. CLOSED TREE|shindli@mozilla.com||2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4de00f3a05ad)|[Bug 1531032](https://bugzilla.mozilla.org/show_bug.cgi?id=1531032)  disable tier2 jobs from running with try syntax unless specifically enabled. r=tomprince Enable WPT-reftests as tier1 Differential Revision: https://phabricator.services.mozilla.com/D21786|shindli@mozilla.com|tomprince|2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=648001848ed2)|[Bug 1539905](https://bugzilla.mozilla.org/show_bug.cgi?id=1539905)  Ensure a copy is taken of memoized values r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D26306|shindli@mozilla.com|mtabara|2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e5ebda0bbbf1)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Specify bouncer-prefix in cron bouncer check as well; r=mtabara The previous changes only changed the check in the release process. This also updates the periodic check. Differential Revision: https://phabricator.services.mozilla.com/D26199|shindli@mozilla.com|mtabara|2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=26eb65cf9325)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Don't restrict the branch that cron-bouncer-check runs on; r=mtabara We only run the cron job on release branches, so it will only get scheduled there. By not otherwise restricting the job, it makes it easier to test the cron job on other branches (like try). Differential Revision: https://phabricator.services.mozilla.com/D26200|shindli@mozilla.com|mtabara|2019-04-06 00:47:45|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=93075ec49df3)|Backed out 2 changesets [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  for l10n bustages a=backout Backed out changeset 9645ac1a9851 [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  Backed out changeset 4de7f94119fd [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299) |btara@mozilla.com|backout|2019-04-05 14:12:21|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=230bb363f2f3)|Merge mozilla-central to inbound|btara@mozilla.com||2019-04-05 12:50:28|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=83c38c0e430b)|Merge mozilla-central to inbound a=merge|btara@mozilla.com|merge|2019-04-05 12:50:28|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=20750a2dc85b)|[Bug 1541943](https://bugzilla.mozilla.org/show_bug.cgi?id=1541943)  - Temporarily switch libFuzzer builds back to clang-7. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D26194|btara@mozilla.com|froydnj|2019-04-05 12:48:43|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6dc5bafd6649)|[Bug 1536555](https://bugzilla.mozilla.org/show_bug.cgi?id=1536555)  - run tc win builds on gcp at tier 3 r=coop,pmoore this change adds support for parallel gcp builds for the following windows build configurations: - win32 - opt - debug - pgo - win64 - opt - debug - pgo gcp builds are triggered with a treeherder tier 3 flag so that they are only displayed in the treeherder ui when the user has a tier 3 flag set. gcp builds use a th build symbol of "Bg" to make them easy to differentiate from ec2 builds in the treeherder ui. gcp builds use a perfherder "gcp" flag to make them easier to differentiate from ec2 builds in the perfherder ui. Differential Revision: https://phabricator.services.mozilla.com/D24865|aiakab@mozilla.com|coop,pmoore|2019-04-04 19:07:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2e66bbe04f08)|[Bug 1541189](https://bugzilla.mozilla.org/show_bug.cgi?id=1541189)  - Moved test to tier 3 - r=whimboo We'll promote it to tier 2 once we have fixed the intermittents Differential Revision: https://phabricator.services.mozilla.com/D26081|aiakab@mozilla.com|whimboo|2019-04-04 19:07:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b2f3367509f9)|[Bug 1541835](https://bugzilla.mozilla.org/show_bug.cgi?id=1541835)  - only run windows/aarch64 tests on m-c/try, not autoland/inbound. r=aryx only run windows/aarch64 tests on m-c/try, not autoland/inbound Differential Revision: https://phabricator.services.mozilla.com/D26093|aiakab@mozilla.com|aryx|2019-04-04 19:07:30|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=16bfbf0db8ac)|No bug: [try-staging] Allow staging builds to access staging github ssh key; r=nthomas The secret with the ssh key already exists in taskcluster, this tells mozharness to try to access it. Differential Revision: https://phabricator.services.mozilla.com/D25700|aciure@mozilla.com|nthomas|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0ab4cffb2675)|No bug: [mozharness] Remove unused esr52 partner repack configuration; r=nthomas Differential Revision: https://phabricator.services.mozilla.com/D25701|aciure@mozilla.com|nthomas|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=362eb37eb09f)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D25584|aciure@mozilla.com|sfraser|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e3809f2c3cb2)|[Bug 1533010](https://bugzilla.mozilla.org/show_bug.cgi?id=1533010)  - Update Windows Rust to 1.34 beta r=glandium This is needed for cross-language LTO [Bug 1512723](https://bugzilla.mozilla.org/show_bug.cgi?id=1512723)  We don't want to block on waiting for 1.34's release, so we'll get a head start now, but we'll update to the final 1.34 release when available. Rust Forge estimates the release at 11 April. Differential Revision: https://phabricator.services.mozilla.com/D25851|aciure@mozilla.com|glandium|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=486395fabe66)|[Bug 1532747](https://bugzilla.mozilla.org/show_bug.cgi?id=1532747)  - [ci] Create try-only raptor reference-browser tasks, r=jmaher,rwood These will run on android-hw against the latest reference browser nightly. Since they are try-only, they can only be scheduled with |mach try fuzzy --full|. Differential Revision: https://phabricator.services.mozilla.com/D25801|aciure@mozilla.com|jmaher,rwood|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=60420822a632)|[Bug 1540213](https://bugzilla.mozilla.org/show_bug.cgi?id=1540213)  - turn on green suites of windows10-aarch64 on taskgraph r=jmaher,gbrown Enables the list of suites as defined in [Bug 1540213](https://bugzilla.mozilla.org/show_bug.cgi?id=1540213)  - added new item in `test-sets.yml` for windows10-aarch64. - reference the new test-set in `test-platforms.yml`. Differential Revision: https://phabricator.services.mozilla.com/D25979|aciure@mozilla.com|jmaher,gbrown|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=29ca2ad7266b)|[Bug 1541121](https://bugzilla.mozilla.org/show_bug.cgi?id=1541121)  [try-staging] Simplify the logic for getting partial update configration; r=aki The original code was converting to json, then comparing against `{}`. This switches things around so that json is only generated where it is directly used a json. Differential Revision: https://phabricator.services.mozilla.com/D24833|aciure@mozilla.com|aki|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=948b7b1003af)|[Bug 1541121](https://bugzilla.mozilla.org/show_bug.cgi?id=1541121)  [try-staging] Allow staging release to not have partials; r=aki We check that partials as a safety check. But we don't need that for staging builds, and it is often useful to be able to test things that don't depend on partials. The shipit UI currently still requires partials, but that can be worked around using the react dev tools. Differential Revision: https://phabricator.services.mozilla.com/D24834|aciure@mozilla.com|aki|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0ff766eb6349)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  Support generating update-verify-config for new configuration; r=aki When adding a new platform, the first release will be at the watershed, and there will be no update paths. Rather than failing in this case (requiring the update-verify setup happen after the first release), generate an empty config which will allow the later tasks to turn green. Differential Revision: https://phabricator.services.mozilla.com/D25833|aciure@mozilla.com|aki|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0c4e9114a199)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  Add win64-aarch64 update verify configuration; r=aki Differential Revision: https://phabricator.services.mozilla.com/D25834|aciure@mozilla.com|aki|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1339cb993b08)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Support bouncer-check in staging; r=aki Differential Revision: https://phabricator.services.mozilla.com/D25835|aciure@mozilla.com|aki|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0e5ad75bf07d)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [mozharness] Remove unused bouncer_check config entries; r=mtabara I beleive these entries date from when bouncer config was handled by mozharness rather than bounerscript and are now obsolete. Differential Revision: https://phabricator.services.mozilla.com/D25836|aciure@mozilla.com|mtabara|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=111aa230d41e)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [mozharness] Remove unused bouncer configuration for fennect; r=mtabara Fennec doesn't have a bouncer check task, and bouncer is update via bouncerscript. Differential Revision: https://phabricator.services.mozilla.com/D25837|aciure@mozilla.com|mtabara|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4daa02d1aa20)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [mozharness] Simplify bouncer-check configuration to not include paths; r=mtabara These existed for when bouncer was updated via mozharness, and they are unused in bouncer-check. By removing the paths, we make the configuration easier to read and update. Differential Revision: https://phabricator.services.mozilla.com/D25838|aciure@mozilla.com|mtabara|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=310d07e69df5)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  Don't create fresh virtualenv for bouncer-check; r=mtabara In automation, the script is run with `mach python`, and all the dependencies are vendored, so just use them directly. Differential Revision: https://phabricator.services.mozilla.com/D25839|aciure@mozilla.com|mtabara|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=e847d4ed0e22)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  [win64-aarch64] Add win64 aarch64 bouner-check configuration; r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D25840|aciure@mozilla.com|mtabara|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=f9d9fb959d89)|[Bug 1533589](https://bugzilla.mozilla.org/show_bug.cgi?id=1533589)  [win64-aarch64] Point win64-aarch64 stub bounce entries at the correct path; r=mtabara There was special case logic to map the win64 platform to win32, for stub entries. When win64-aarch64 was added no special case was added for that plaform, so they stub entries pointed at the incorrect place. This changes the configuration so that all stub entries point at the win32 paths, without needing special case code. Differential Revision: https://phabricator.services.mozilla.com/D25841|aciure@mozilla.com|mtabara|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8c0a7e7ccb50)|[Bug 1533939](https://bugzilla.mozilla.org/show_bug.cgi?id=1533939)  [release] Move beta-channel RC tasks to release platform in treeherder; r=Callek Differential Revision: https://phabricator.services.mozilla.com/D25985|aciure@mozilla.com|Callek|2019-04-04 07:33:36|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b72c02e34261)|Merge autoland to mozilla-central. a=merge|aciure@mozilla.com|merge|2019-04-04 07:33:36|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=1c729b2f5e3e)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Don't restrict the branch that cron-bouncer-check runs on; r=mtabara a=tomprince We only run the cron job on release branches, so it will only get scheduled there. By not otherwise restricting the job, it makes it easier to test the cron job on other branches (like try). Differential Revision: https://phabricator.services.mozilla.com/D26200|dvarga@mozilla.com|mtabara|2019-04-05 22:51:52|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=8d526e3036bf)|[Bug 1541122](https://bugzilla.mozilla.org/show_bug.cgi?id=1541122)  [try-staging] Specify bouncer-prefix in cron bouncer check as well; r=mtabara a=tomprince The previous changes only changed the check in the release process. This also updates the periodic check. Differential Revision: https://phabricator.services.mozilla.com/D26199|dvarga@mozilla.com|mtabara|2019-04-05 22:51:52|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=864e16abd2f7)|[Bug 1539905](https://bugzilla.mozilla.org/show_bug.cgi?id=1539905)  Cache yaml loading with copy of memoized values r=mtabara a=release|mtabara@mozilla.com|mtabara|2019-04-05 20:44:22|
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=df05571b936f)|[Bug 1538703](https://bugzilla.mozilla.org/show_bug.cgi?id=1538703)  - remove try config from declarative artifacts world. r=sfraser a=release|mtabara@mozilla.com|sfraser|2019-04-05 19:36:58|

|	mozilla-release	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-release.md)|FIC - BOT|Self Generated| - |

|	build-puppet	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-puppet.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/build-puppet/commit/e81c82301c93f84a2ffdf6bdb7ad7ba44e802bdb)|Merge pull request #444 from MihaiTabara/bump  Bug 1539067 - bump beetmoverscript in beetmoverworkers.|MihaiTabara|N/A|2019-04-05 16:42:18|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/a82deadea0ac0f01332241185a2957db5038ede5)|Bug 1539067 - bump beetmoverscript in beetmoverworkers.|MihaiTabara|N/A|2019-04-05 16:20:13|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/91afa14c2ae9e0357fc08c9db8f64fd9bc09b959)|balrogscript: remove basic auth support (#443)|rail|N/A|2019-04-04 17:26:11|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/753e2e703bdce697d924e3883b4912170d1f7e71)|Scheduled weekly dependency update for week 13 (#441)    Update boto3 from 1.9.122 to 1.9.127      Update botocore from 1.12.122 to 1.12.127      Update pushapkscript from 0.14.0 to 1.0.0      Update datadog from 0.27.0 to 0.28.0|pyup-bot|N/A|2019-04-03 17:44:58|

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/taskcluster/taskcluster/commit/8aeb54ba72ec3f1f2ded99d4c6a8760f8fc20710)|Merge pull request #526 from djmitche/bug1534713  Bug 1534713 - better debugging for pulse issues|imbstack|N/A|2019-04-04 17:00:09|
|[Link](https://github.com/taskcluster/taskcluster/commit/649df9d35712fd76e5893f55e95c5c82a1bf70c6)|Merge pull request #537 from djmitche/tdd-for-tc-web-server  use tdd for tc-web-server tests|imbstack|N/A|2019-04-04 16:45:36|
|[Link](https://github.com/taskcluster/taskcluster/commit/9833a1c47a4faafa44b8fe0f86204f38eb560a5e)|Merge pull request #524 from djmitche/bug1540697  Bug 1540697 - improve idempotency of task creation, especially in hooks|imbstack|N/A|2019-04-04 16:37:19|
|[Link](https://github.com/taskcluster/taskcluster/commit/239e6d2c6ff8f856e1932f7c315d6fcf53b4abe0)|Merge branch 'master' into bug1534713|imbstack|N/A|2019-04-04 16:34:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/26b2e7839874d0c75b9631d17c9528d65e56b511)|Merge branch 'master' into tdd-for-tc-web-server|imbstack|N/A|2019-04-04 16:31:57|
|[Link](https://github.com/taskcluster/taskcluster/commit/66c2510f7275d0853ccc42690b5968b68df9fa56)|Merge pull request #527 from djmitche/bug1535316  Bug 1535316 - remove use of http-proxy for testing auth|imbstack|N/A|2019-04-04 16:29:44|
|[Link](https://github.com/taskcluster/taskcluster/commit/683d22d624c4111872f66e42e4ad74c364365b47)|Merge branch 'master' into bug1535316|imbstack|N/A|2019-04-04 15:59:59|
|[Link](https://github.com/taskcluster/taskcluster/commit/7d1141a6a0efca5823d74945f28f94e500a8e919)|Merge pull request #544 from djmitche/bug1540160  Bug 1540160 - add bash to the built image|imbstack|N/A|2019-04-04 15:50:58|
|[Link](https://github.com/taskcluster/taskcluster/commit/10ca598510a09e9c7e3f62bb49edb5b58ab00c6a)|Merge pull request #542 from djmitche/remove-PulseListener-leftovers  Remove leftovers of tc-client.PulseListener|imbstack|N/A|2019-04-04 15:49:31|
|[Link](https://github.com/taskcluster/taskcluster/commit/2a78a93ec45350916abdfd6561ebca50d4ee99f1)|Merge pull request #539 from djmitche/bug1517863  Bug 1517863 - use filename as top-level suite name|imbstack|N/A|2019-04-04 15:32:31|
|[Link](https://github.com/taskcluster/taskcluster/commit/55796d2aae61d5b5827dbf46a08299a52774a7c3)|Merge pull request #536 from djmitche/cleanup-builder  remove unused tc-builder file|imbstack|N/A|2019-04-03 18:26:57|
|[Link](https://github.com/taskcluster/taskcluster/commit/ceef9bf43f8d2e4094efe5d28da36c168aa9b8a9)|Merge pull request #538 from djmitche/doc-all-client-options  document all options to client constructor|imbstack|N/A|2019-04-03 18:26:37|

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
|[Link](https://github.com/mozilla-releng/beetmoverscript/commit/1c1373595fa27fb83cdad6babaf4503c432a5f60)|8.4.3|MihaiTabara|N/A|2019-04-05 16:14:17|

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
|[Link](https://github.com/mozilla/release-services/commit/b5e79a12e11ad2c625bd7cce2330c0c9c37f09f4)|setup: update nixpkgs (#2016)|garbas|N/A|2019-04-04 10:58:36|

|	build-cloud-tools	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/build-cloud-tools.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=c0f013451af1)|No bug - amend fenix master role to encompass dep signing. r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D26294|mhentges@mozilla.com|jlorenzo|2019-04-05 18:09:05|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=97aa12ede0b8)|No bug: Run black; rs=me|mozilla@hocat.ca||2019-04-04 02:43:58|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=b5cd4084dd59)|No bug: [ci] Update taskgraph to use worker aliases; r=me|mozilla@hocat.ca|me|2019-04-04 02:43:58|
