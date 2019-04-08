##  Commits in production - for 3 days, generated on: 2019-04-08 10:49:06 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=674a4d255565)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|bpostelnicu@mozilla.com|bastien|2019-04-08 13:44:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=248454418988)|Backed out changeset 7e2aef09165a [Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  on request by Andy|ccoroiu@mozilla.com||2019-04-08 13:25:05|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7e2aef09165a)|[Bug 1541147](https://bugzilla.mozilla.org/show_bug.cgi?id=1541147)  - [Coverity] Create a try job that performs coverity static-analysis for patches. r=bastien Differential Revision: https://phabricator.services.mozilla.com/D26145|bpostelnicu@mozilla.com|bastien|2019-04-08 13:16:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c9d95a544902)|[Bug 1503453](https://bugzilla.mozilla.org/show_bug.cgi?id=1503453)  - Temporarily disable permafailing Windows static analysis builds: Add one more whitespace because the linting gods demand this. a=permafail CLOSED TREE|archaeopteryx@coole-files.de|permafail|2019-04-08 11:14:28|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=13b40bbdb45c)|[Bug 1503453](https://bugzilla.mozilla.org/show_bug.cgi?id=1503453)  - Temporarily disable permafailing Windows static analysis builds. a=permafail|archaeopteryx@coole-files.de|permafail|2019-04-08 10:55:34|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b5167ef1c9ea)|Merge mozilla-central to mozilla-inbound on a CLOSED TREE|nerli@mozilla.com||2019-04-07 00:51:25|
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

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=97fa367562a0)|[Bug 1541821](https://bugzilla.mozilla.org/show_bug.cgi?id=1541821)  - Ensure docker images using setup_packages.sh are up-to-date wrt the packages provided there. r=tomprince When docker images use setup_packages.sh, they add apt sources. While we currently do run apt-get update to pick those new sources, if a package provided by them is already installed and not explicitly listed in subsequent apt-get install, they're not going to be upgraded. Differential Revision: https://phabricator.services.mozilla.com/D26100|cbrindusan@mozilla.com|tomprince|2019-04-07 12:40:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7d60a7fd2fac)|[Bug 1541821](https://bugzilla.mozilla.org/show_bug.cgi?id=1541821)  - Update debian7 docker images for CVE-2019-3462. r=tomprince This imports the changes from wheezy-lts (http://deb.freexian.com/extended-lts/) and creates a package we install in the debian7-based images (with a modified version number to work around [Bug 1419577](https://bugzilla.mozilla.org/show_bug.cgi?id=1419577)  This leaves out debian7-raw and debian7-packages as unpatched, because of the chicken-and-egg problem. Depends on D26100 Differential Revision: https://phabricator.services.mozilla.com/D26102|cbrindusan@mozilla.com|tomprince|2019-04-07 12:40:07|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2e359f02ea62)|[Bug 1538703](https://bugzilla.mozilla.org/show_bug.cgi?id=1538703)  - roll-out declarative artifacts in Firefox. r=sfraser a=release|mtabara@mozilla.com|sfraser|2019-04-05 19:30:36|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=93075ec49df3)|Backed out 2 changesets [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  for l10n bustages a=backout Backed out changeset 9645ac1a9851 [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299)  Backed out changeset 4de7f94119fd [Bug 1195299](https://bugzilla.mozilla.org/show_bug.cgi?id=1195299) |btara@mozilla.com|backout|2019-04-05 14:14:44|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=20750a2dc85b)|[Bug 1541943](https://bugzilla.mozilla.org/show_bug.cgi?id=1541943)  - Temporarily switch libFuzzer builds back to clang-7. r=froydnj Differential Revision: https://phabricator.services.mozilla.com/D26194|btara@mozilla.com|froydnj|2019-04-05 12:57:50|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=13b40bbdb45c)|[Bug 1503453](https://bugzilla.mozilla.org/show_bug.cgi?id=1503453)  - Temporarily disable permafailing Windows static analysis builds. a=permafail|dluca@mozilla.com|permafail|2019-04-08 13:33:51|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=c9d95a544902)|[Bug 1503453](https://bugzilla.mozilla.org/show_bug.cgi?id=1503453)  - Temporarily disable permafailing Windows static analysis builds: Add one more whitespace because the linting gods demand this. a=permafail CLOSED TREE|dluca@mozilla.com|permafail|2019-04-08 13:33:51|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b5167ef1c9ea)|Merge mozilla-central to mozilla-inbound on a CLOSED TREE|nerli@mozilla.com||2019-04-07 00:48:55|
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

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=c261ac70fabc)|No bug: Turn off staged rollout for Fennec 67.0b. a=release DONTBUILD|jcristau@mozilla.com|release|2019-04-08 11:19:31|
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

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)|FIC - BOT|Self Generated| - |

|	taskcluster	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.json)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/taskcluster.md)|FIC - BOT|Self Generated| - |

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
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=e0e131534dc9)|No bug - Move fenix master scopes to their own grant section r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D26480|jlorenzo@mozilla.com|jlorenzo|2019-04-08 12:49:22|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=99bb5249719c)|[Bug 1542697](https://bugzilla.mozilla.org/show_bug.cgi?id=1542697)  - Add secret project/relman/coverity to L1, L2 and L3 access. r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D26478|jlorenzo@mozilla.com|jlorenzo|2019-04-08 12:18:53|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last 3 days.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |
