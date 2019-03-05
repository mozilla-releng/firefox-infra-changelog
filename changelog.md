##  Commits in production - for one day, generated on: 2019-03-05 19:18:43 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4e5d97c93515)|[Bug 1508976 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1508976) - Produce a multi-architecture GeckoView "fat AAR". r=snorp,agi,froydnj Differential Revision: https://phabricator.services.mozilla.com/D15771|nalexander@mozilla.com|snorp,agi,froydnj|2019-03-05 20:40:48|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c47b37ac1775)|[Bug 1522581 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1522581) - Publish GeckoView multi-architecture fat AAR Nightly. r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D15774|nalexander@mozilla.com|jlorenzo|2019-03-05 20:40:48|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7a6be593b0be)|[Bug 1522581 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1522581) - Post: Clean up Android TC artifacts. r=jlorenzo Differential Revision: https://phabricator.services.mozilla.com/D21479|nalexander@mozilla.com|jlorenzo|2019-03-05 20:40:48|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=9fca85ee3084)|Backed out changeset ce3dfcdb5861 (bug 1532236) for linting opt failure in partials.py CLOSED TREE|nerli@mozilla.com||2019-03-05 18:54:35|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ce3dfcdb5861)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) Convert level into integer in partials transform r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D22108|sfraser@mozilla.com|mtabara|2019-03-05 18:36:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=bc4e03f4ea20)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) Remove extra newlines from partials logging r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D22072|sfraser@mozilla.com|mtabara|2019-03-05 12:59:42|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=1cc8b60d8a6b)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) - longer timeout for asan partial generation, r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D22038|nthomas@mozilla.com|tomprince|2019-03-05 02:52:06|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b58080db50e6)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add code-review-issues task in CI, r=dustin,marco,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21348|babadie@mozilla.com|dustin,marco,tomprince|2019-03-04 23:26:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5cfbf5c1dbe7)|Backed out changeset 7fdcccd878ad (bug 1527895) for Gecko Decision Task failure. CLOSED TREE|dluca@mozilla.com||2019-03-04 19:41:57|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=7fdcccd878ad)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add code-review-issues task in CI, r=dustin,marco,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21348|babadie@mozilla.com|dustin,marco,tomprince|2019-03-04 19:34:02|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=f201447a5f65)|No bug: Fix black errors in tests; r=me|mozilla@hocat.ca|me|2019-03-04 23:36:59|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=0368a98315e9)|[Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) Allow parameterizing based on priorties determined by level; r=dustin For the moment, we hard-code the priorities by level based on those used in firefox. Differential Revision: https://phabricator.services.mozilla.com/D21813|mozilla@hocat.ca|dustin|2019-03-04 23:27:16|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=60bc15b47919)|[Bug 1526979 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526979) allow ignored payload.data.source, too, in triggering hook r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D21969|dmitchell@mozilla.com|tomprince|2019-03-04 20:38:07|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=e72a3935e409)|No bug: fix use of bindings in 'ci-admin apply' r=tomprince I missed this when refactoring the `bindings` property to use an object instead of a tuple. Differential Revision: https://phabricator.services.mozilla.com/D21963|dmitchell@mozilla.com|tomprince|2019-03-04 20:37:38|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=6a3895820e75)|No bug: capture absolute path for --ci-configuration-directory r=tomprince The `ci-admin check` command changes working directory, so it broke use of `--ci-configuration-directory`. Differential Revision: https://phabricator.services.mozilla.com/D21959|dmitchell@mozilla.com|tomprince|2019-03-04 19:42:19|

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=9c33e3407330)|[Bug 1532453 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532453) Add user repositories for experimenting with taskgraph and mobile; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22031|mozilla@hocat.ca|dustin|2019-03-05 02:04:42|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=c1f008b66b74)|[Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) Remove some redundant and cross-level/trust-domain scope grants; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D21805|mozilla@hocat.ca|dustin|2019-03-04 23:44:32|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=9593b1fcbf4e)|[Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) Remove obsolete worker types; r=dustin Most of these have not been used for some time, or no longer exist. gecko-decision (not level constrained) is still used in some non-mozilla-central nigthly hooks. I think they are unused, and otherwise they can be updated as needed. Differential Revision: https://phabricator.services.mozilla.com/D21806|mozilla@hocat.ca|dustin|2019-03-04 23:44:32|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=0475eb0a0339)|[Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) Remove unused docker.images and project.releng.funsize routes; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D21807|mozilla@hocat.ca|dustin|2019-03-04 23:44:32|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=1eea5e725cf6)|[Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) Remove obsolete `scheduler:*` scopes; r=dustin These are for an decommisioned service. Differential Revision: https://phabricator.services.mozilla.com/D21808|mozilla@hocat.ca|dustin|2019-03-04 23:44:32|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=42c8b3e56a48)|[Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) Parameterize gecko workers using priorities; r=dustin This consolidates the scopes for the main worker-types used by firefox CI, by parametrizing them by priority based on the level. Differential Revision: https://phabricator.services.mozilla.com/D21812|mozilla@hocat.ca|dustin|2019-03-04 23:44:32|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=c4e950fe3fe6)|[Bug 1531178 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531178) - provide gls and safe browsing separate keys. r=tomprince a=test-only Provide gls and safe browsine separate keys at build time. Differential Revision: https://phabricator.services.mozilla.com/D21536|nerli@mozilla.com|tomprince|2019-03-05 17:14:43|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b58080db50e6)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add code-review-issues task in CI, r=dustin,marco,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21348|aciure@mozilla.com|dustin,marco,tomprince|2019-03-05 06:19:19|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=1cc8b60d8a6b)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) - longer timeout for asan partial generation, r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D22038|aciure@mozilla.com|tomprince|2019-03-05 06:19:19|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ee0735447f25)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D21903|aciure@mozilla.com|sfraser|2019-03-04 23:48:23|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=817014bcd372)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) Improve logging and timeouts in partials generation r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D21909|aciure@mozilla.com|mtabara|2019-03-04 23:48:23|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0ece01da444e)|[Bug 1532251 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532251) Add new xpcshell dependency to periodic updates r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D21912|aciure@mozilla.com|mtabara|2019-03-04 23:48:23|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=aeee5b2fac0f)|[Bug 1531178 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531178) - provide gls and safe browsing separate keys. r=tomprince Provide gls and safe browsine separate keys at build time. Differential Revision: https://phabricator.services.mozilla.com/D21536|aciure@mozilla.com|tomprince|2019-03-04 23:48:23|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5caf48a420eb)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add soft-dependencies to taskgraph, r=ahal,marco,tomprince,dustin Differential Revision: https://phabricator.services.mozilla.com/D19791|aciure@mozilla.com|ahal,marco,tomprince,dustin|2019-03-04 23:48:23|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7fdcccd878ad)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add code-review-issues task in CI, r=dustin,marco,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21348|aciure@mozilla.com|dustin,marco,tomprince|2019-03-04 23:48:23|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5cfbf5c1dbe7)|Backed out changeset 7fdcccd878ad (bug 1527895) for Gecko Decision Task failure. CLOSED TREE|aciure@mozilla.com||2019-03-04 23:48:23|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8df68de51796)|[Bug 1532336 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532336) - Turn off optimizations for searchfox jobs. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D21964|aciure@mozilla.com|tomprince|2019-03-04 23:48:23|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b58080db50e6)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add code-review-issues task in CI, r=dustin,marco,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21348|aciure@mozilla.com|dustin,marco,tomprince|2019-03-05 06:24:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=1cc8b60d8a6b)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) - longer timeout for asan partial generation, r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D22038|aciure@mozilla.com|tomprince|2019-03-05 06:24:51|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ee0735447f25)|No Bug, taskcluster/docker/funsize-update-generator pipfile-update. r=sfraser Differential Revision: https://phabricator.services.mozilla.com/D21903|aciure@mozilla.com|sfraser|2019-03-04 23:54:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=817014bcd372)|[Bug 1532236 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532236) Improve logging and timeouts in partials generation r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D21909|aciure@mozilla.com|mtabara|2019-03-04 23:54:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=0ece01da444e)|[Bug 1532251 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532251) Add new xpcshell dependency to periodic updates r=mtabara Differential Revision: https://phabricator.services.mozilla.com/D21912|aciure@mozilla.com|mtabara|2019-03-04 23:54:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=aeee5b2fac0f)|[Bug 1531178 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531178) - provide gls and safe browsing separate keys. r=tomprince Provide gls and safe browsine separate keys at build time. Differential Revision: https://phabricator.services.mozilla.com/D21536|aciure@mozilla.com|tomprince|2019-03-04 23:54:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5caf48a420eb)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add soft-dependencies to taskgraph, r=ahal,marco,tomprince,dustin Differential Revision: https://phabricator.services.mozilla.com/D19791|aciure@mozilla.com|ahal,marco,tomprince,dustin|2019-03-04 23:54:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7fdcccd878ad)|[Bug 1527895 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1527895) - Add code-review-issues task in CI, r=dustin,marco,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21348|aciure@mozilla.com|dustin,marco,tomprince|2019-03-04 23:54:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=5cfbf5c1dbe7)|Backed out changeset 7fdcccd878ad (bug 1527895) for Gecko Decision Task failure. CLOSED TREE|aciure@mozilla.com||2019-03-04 23:54:47|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=8df68de51796)|[Bug 1532336 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532336) - Turn off optimizations for searchfox jobs. r=tomprince Differential Revision: https://phabricator.services.mozilla.com/D21964|aciure@mozilla.com|tomprince|2019-03-04 23:54:47|

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
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/19d4f80e2fbb590c78628866fcf99be55ae2d0ed)|update to gw 13.0.2, tc-proxy 5.1.0 on l1 & l2 builders  deploy: gecko-1-b-win2012 gecko-2-b-win2012|grenade|N/A|2019-03-05 09:42:40|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/818d2412b9a0f1cdf90234b7724fb9ad2073c98e)|update to gw 13.0.2, tc-proxy 5.1.0 on win 10  deploy: gecko-t-win10-64 gecko-t-win10-64-gpu|grenade|N/A|2019-03-05 07:25:59|

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/pushsnapscript/commit/48ded4332ef5acda5ab62db74ca926695175fff2)|0.2.5|JohanLorenzo|N/A|2019-03-05 16:43:28|

|	scriptworker	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/scriptworker.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/scriptworker/commit/58768476d7b5eeef969e67eb42cb01ac0d9ee117)|21.0.0|JohanLorenzo|N/A|2019-03-05 14:17:09|
|[Link](https://github.com/mozilla-releng/scriptworker/commit/58768476d7b5eeef969e67eb42cb01ac0d9ee117)|21.0.0|JohanLorenzo|N/A|2019-03-05 14:17:09|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/0c297baed0af93923572691f54f6868cb313cbbf)|Revert "bug fix 1519969"  This reverts commit 0a79f4efcc937620b849b83faae440b1e2334317.|djmitche|N/A|2019-03-05 16:04:35|
|[Link](https://github.com/taskcluster/taskcluster/commit/6e5c4fda9eb46c9182c9d3921497b17f47e45c5e)|import Iterate for claim resolver|djmitche|N/A|2019-03-05 15:29:01|
|[Link](https://github.com/taskcluster/taskcluster/commit/5487ee62b54e07425c6da8b56b2c82c3436141b7)|Merge pull request #229 from taskcluster/bug1527583  Bug 1527583 - Queue doesn't take jobs from "unscheduled" to "pending"|djmitche|N/A|2019-03-05 15:21:35|
|[Link](https://github.com/taskcluster/taskcluster/commit/d206d0c1389276e8e59d477d08b5fbe92b676ce9)|Merge pull request #358 from djmitche/new-images  update to new monoimage, with fixes|djmitche|N/A|2019-03-05 14:48:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/bc7ebe63875b03d134db99e0d1ebed9bfc148f45)|update to new image|djmitche|N/A|2019-03-04 23:59:03|
|[Link](https://github.com/taskcluster/taskcluster/commit/5e63ce8ebae938f8c8dae40cd6c9f9e896acc0d9)|write the contents of references.json, not the filename|djmitche|N/A|2019-03-05 03:21:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/f3c0741a6510d9719d880339b177aaa74228f448)|set proc_name so that tc-ui runs properly|djmitche|N/A|2019-03-05 03:20:22|
|[Link](https://github.com/taskcluster/taskcluster/commit/cca34f6bcefa14eada8d4cadbbce7d40de6b8727)|set FORCE_SSL for secrets service|djmitche|N/A|2019-03-05 03:19:51|
|[Link](https://github.com/taskcluster/taskcluster/commit/9298ad24a9ee5bd7c44fb212b9288f6a4148ca45)|Merge pull request #356 from owlishDeveloper/scopes-fix  Add Check-related Azure scopes to the terraform for Kube deployments|owlishDeveloper|N/A|2019-03-05 01:32:00|
|[Link](https://github.com/taskcluster/taskcluster/commit/784f1a1a02c83b900762dea099973e3e8b6b6e4a)|Add Check-related Azure scopes to the terraform for Kube deployments|owlishDeveloper|N/A|2019-03-05 00:48:44|
|[Link](https://github.com/taskcluster/taskcluster/commit/4a7e4531ba6ca57ad974171830237db5ab89a19a)|Merge pull request #352 from djmitche/bug1523805  Bug 1523805 - rename typed-env-config to taskcluster-lib-config|djmitche|N/A|2019-03-04 23:43:57|
|[Link](https://github.com/taskcluster/taskcluster/commit/c2c774f6adcc5cd072c2731dbb45eb85928f6fc9)|Merge pull request #341 from sudipt1999/bug1519969  Bug 1519969 - Sending an email to an invalid address fails|djmitche|N/A|2019-03-04 23:41:07|
|[Link](https://github.com/taskcluster/taskcluster/commit/a070042c7f274ab7c27ba6211ed25e6c9801db52)|Merge pull request #283 from sudipt1999/crashOnError  Bug 1527969  Add function to lib-loader that is for using when file is executed|djmitche|N/A|2019-03-04 23:34:37|
|[Link](https://github.com/taskcluster/taskcluster/commit/e2b407b508422bab5837a90e438b1cbd8c11aad6)|Merge pull request #342 from djmitche/eslint-for-test  Run eslint over the meta-test directory, too|djmitche|N/A|2019-03-04 23:31:40|
|[Link](https://github.com/taskcluster/taskcluster/commit/72d42d787c401b2f16774f1a24516e9102e141c0)|Merge pull request #343 from djmitche/no-more-check-staging  No more check staging|djmitche|N/A|2019-03-04 23:31:29|
|[Link](https://github.com/taskcluster/taskcluster/commit/94df6451339c83399db6a332156039c57ee57ebd)|Merge pull request #350 from djmitche/codeowners-jhford  Remove use of single users in CODEOWNERS|djmitche|N/A|2019-03-04 23:29:26|
|[Link](https://github.com/taskcluster/taskcluster/commit/9d00159370c900cc0ddfe107c7c6d75e17862050)|Merge pull request #351 from djmitche/remove-unused-schemas  Validate that schemas are used, and remove unused schemas|djmitche|N/A|2019-03-04 23:27:40|
|[Link](https://github.com/taskcluster/taskcluster/commit/aee25c65bad123bc82a441c05b28c90c04a6d983)|Merge pull request #353 from djmitche/bug1525130  Bug 1525130 - write out 'references.json' for use by client builders|djmitche|N/A|2019-03-04 23:26:21|
|[Link](https://github.com/taskcluster/taskcluster/commit/410424da6e6a4ace93e537cfa65d33c546c0cc26)|Bug 1527583 - terminate polling services after each test, just to be safe|djmitche|N/A|2019-03-04 22:56:30|
|[Link](https://github.com/taskcluster/taskcluster/commit/0b4ef8ba4013967499e92617376e3151b1a73133)|Bug 1527583 - use tc-lib-iterate for claim resolver|djmitche|N/A|2019-03-04 22:50:18|
|[Link](https://github.com/taskcluster/taskcluster/commit/2140d4fd3509bcebf8e7a641b13076ab5bca3391)|Bug 1527583 - use tc-lib-iterate for deadline resolver|djmitche|N/A|2019-03-04 22:48:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/ae58c44cd01f0c2b2c9179cc09f642dbeb3fc02c)|Bug 1527583 - fix logging of elapsed fake time|djmitche|N/A|2019-03-04 22:42:30|
|[Link](https://github.com/taskcluster/taskcluster/commit/ff274809b70232585e2aea2ad6a7692026f8b649)|Bug 1527583 - fix up times for dependency resolver|djmitche|N/A|2019-03-04 21:35:32|
|[Link](https://github.com/taskcluster/taskcluster/commit/9095dbcf7c3df2bb41582db5e2bb6718220c4c60)|Merge pull request #354 from taskcluster/fix-force-ssl  Fix forceSSL for secrets|imbstack|N/A|2019-03-04 22:38:42|
|[Link](https://github.com/taskcluster/taskcluster/commit/fd5400d20208239e07176153f502b1d41194c419)|Fix forceSSL for secrets|imbstack|N/A|2019-03-04 22:15:30|
|[Link](https://github.com/taskcluster/taskcluster/commit/9dae677b5232a551eea3caeae8e8119150cb0529)|Merge pull request #349 from taskcluster/renovate/eslint-5.x  Update dependency eslint to v5.15.0|djmitche|N/A|2019-03-04 20:40:39|
|[Link](https://github.com/taskcluster/taskcluster/commit/84a5d4efe47a8940fb80a8086c16a43695ebb9d1)|Merge pull request #348 from taskcluster/renovate/ajv-6.x  Update dependency ajv to v6.10.0|djmitche|N/A|2019-03-04 19:40:37|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
