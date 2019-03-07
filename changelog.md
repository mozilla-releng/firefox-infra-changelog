##  Commits in production - for one day, generated on: 2019-03-07 14:51:14 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=281171d69172)|[Bug 1532710 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532710) [taskgraph] Provide a function version of `resolve_keyed_by` that doesn't mutate; r=dustin I'd like to use the same format for config values, that get evaluated in different contexts, so don't to mutate the config for that. Differential Revision: https://phabricator.services.mozilla.com/D22126|mozilla@hocat.ca|dustin|2019-03-07 06:23:27|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0db48ebeac07)|[Bug 1532710 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532710) [taskgraph] Move default branch priorities to graph config; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22127|mozilla@hocat.ca|dustin|2019-03-07 06:23:27|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6b25ace491c3)|[Bug 1530908 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530908) - Use a transform for try --artifact instead of a morph. r=tomprince While the morph was changing the treeherder symbol to `Ba` for all jobs, doing so with a transform fails because of the conflicting symbol check (as multiple jobs in the same category would end up with `Ba`). So instead, we append `a` to the existing symbol. We also change the documentation wrt templates for try pushes, as the artifact template is now essentially gone (although technically, mach try will still set params['templates']['artifacts']['enabled'] for now, and the template still exists, albeit empty). Differential Revision: https://phabricator.services.mozilla.com/D22054|mh@glandium.org|tomprince|2019-03-07 00:50:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=61dd01ed9002)|[Bug 1530908 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530908) - Unify artifact builds setup between try config and try syntax. r=dustin While try syntax is approaching its EOL, the fact that using it to do artifact builds does some things subtly differently from using try config is not helpful. Depends on D22055 Differential Revision: https://phabricator.services.mozilla.com/D21312|mh@glandium.org|dustin|2019-03-07 00:50:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ad8315f51807)|[Bug 1530908 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530908) - Only enable artifacts on try builds that support them. r=dustin Currently, all tasks of kind builds are indiscriminately altered to use artifacts, but only few of them actually support that, and the others won't actually have the expected result when that happens. E.g. ASAN builds with artifacts enabled end up being non-ASAN builds. Effectively, this makes the artifact flag ignored for builds that don't support artifacts. One could argue that those builds shouldn't happen at all, but it feels a better use time of developer's time to just do the full build they asked for. E.g. if they asked for ASAN with artifacts, they still get an ASAN build, rather than an error or silently having the task not happen after the decision task. This also allows to mix artifact and non-artifact builds. Further changes down the road are also modifying the artifact builds configuration, which would actively turn those builds that don't support artifact builds red (e.g. ASAN), so something has to be done anyways. The alternative would be filter those builds out. Depends on D21312 Differential Revision: https://phabricator.services.mozilla.com/D22056|mh@glandium.org|dustin|2019-03-07 00:50:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=c21559af66d6)|[Bug 1530908 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530908) - Always set USE_ARTIFACT from taskcluster for artifact builds. r=chmanchester The artifact builds that are automatically derived using the artifact template set the USE_ARTIFACT environment variable from taskcluster. After the previous change, --artifact builds from try syntax do that too. That leaves us with only the artifact-build build not doing it, so for consistency, do it there. That makes it not necessary to set USE_ARTIFACT from mozconfig.artifact.automation anymore. Depends on D22056 Differential Revision: https://phabricator.services.mozilla.com/D21313|mh@glandium.org|chmanchester|2019-03-07 00:50:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=0d70e7e33020)|[Bug 1530908 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530908) - Don't use different mozconfigs for artifact builds. r=chmanchester Artifact mozconfigs are not necessarily up-to-date wrt changes to the nightly mozconfigs, and all in all, shouldn't be much different from them. It's just better to use the nightly mozconfigs (or beta on beta, etc.) and make the mozconfigs themselves handle the few things that need to be different when the USE_ARTIFACT environment is set (which is now consistently set by taskcluster) This does have the side effect of turning builds that actually don't support artifact builds red when using --artifact on try, instead of having them silently not be artifact builds as currently happens. Depends on D21314 Differential Revision: https://phabricator.services.mozilla.com/D21315|mh@glandium.org|chmanchester|2019-03-07 00:50:00|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b8e5c1d19e24)|[Bug 1459222 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1459222) - Firefox RC: push snaps onto the beta channel at ship_rc phase r=mtabara Firefox RC: push snaps onto the beta channel at ship_rc phase Differential Revision: https://phabricator.services.mozilla.com/D21380|jlorenzo@mozilla.com|mtabara|2019-03-06 15:53:12|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=7a89e05b3e0c)|No bug: fix black errors in check tests. r=me|mtabara@mozilla.com|me|2019-03-07 01:51:58|
|[Link](https://hg.mozilla.org/ci/ci-admin/pushloghtml?changeset=c72e4cbea39c)|[Bug 1519493 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519493) - fix checker in ci-admin r=tomprince Fix checker which broke with D19246 Differential Revision: https://phabricator.services.mozilla.com/D22415|mtabara@mozilla.com|tomprince|2019-03-07 01:43:08|

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=0dedd6b601b8)|[Bug 1533393 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533393) - Give reference-browser and fenix the rights to publish results to Treeherder r=mtabara Give reference-browser and fenix the rights to publish results to Treeherder Differential Revision: https://phabricator.services.mozilla.com/D22504|jlorenzo@mozilla.com|mtabara|2019-03-07 16:51:01|
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=eb561312b56f)|[Bug 1519493 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519493) - step 1 in automating permissions in mobile world. r=tomprince This is a preliminary ask-for-feedback. * not to be merged until we perform the cleanup in [Bug 1526017 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526017) * this is experimental to understand if the mapping logic can be optimized Differential Revision: https://phabricator.services.mozilla.com/D19240|mtabara@mozilla.com|tomprince|2019-03-07 00:06:27|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7b3b1bc4586f)|[Bug 1533142 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533142) - Update min cbindgen version. r=jrmuizel,kats Differential Revision: https://phabricator.services.mozilla.com/D22381|apavel@mozilla.com|jrmuizel,kats|2019-03-07 11:47:53|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=281171d69172)|[Bug 1532710 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532710) [taskgraph] Provide a function version of `resolve_keyed_by` that doesn't mutate; r=dustin I'd like to use the same format for config values, that get evaluated in different contexts, so don't to mutate the config for that. Differential Revision: https://phabricator.services.mozilla.com/D22126|apavel@mozilla.com|dustin|2019-03-07 11:47:53|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=0db48ebeac07)|[Bug 1532710 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532710) [taskgraph] Move default branch priorities to graph config; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22127|apavel@mozilla.com|dustin|2019-03-07 11:47:53|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7b3b1bc4586f)|[Bug 1533142 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533142) - Update min cbindgen version. r=jrmuizel,kats Differential Revision: https://phabricator.services.mozilla.com/D22381|apavel@mozilla.com|jrmuizel,kats|2019-03-07 12:01:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=281171d69172)|[Bug 1532710 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532710) [taskgraph] Provide a function version of `resolve_keyed_by` that doesn't mutate; r=dustin I'd like to use the same format for config values, that get evaluated in different contexts, so don't to mutate the config for that. Differential Revision: https://phabricator.services.mozilla.com/D22126|apavel@mozilla.com|dustin|2019-03-07 12:01:39|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=0db48ebeac07)|[Bug 1532710 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532710) [taskgraph] Move default branch priorities to graph config; r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22127|apavel@mozilla.com|dustin|2019-03-07 12:01:39|

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
|[Link](https://github.com/mozilla-releng/build-puppet/commit/001add8f7f47ff4cfc357b36da82e468d81bec39)|Scheduled weekly dependency update for week 09 (#417)    Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update attrs from 18.2.0 to 19.1.0      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update jsonschema from 2.6.0 to 3.0.1      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update virtualenv from 16.4.1 to 16.4.3      Update boto3 from 1.9.103 to 1.9.108      Update botocore from 1.12.103 to 1.12.108      Update lxml from 4.3.1 to 4.3.2      Update matplotlib from 3.0.2 to 3.0.3      Update ipy from 0.83 to 1.00      Update ipy from 0.83 to 1.00      Update cryptography from 2.5 to 2.6.1      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update slugid from 2.0.0 to 1.0.7      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0      revert update jsonschema from 3.0.1 to 2.6.0|pyup-bot|N/A|2019-03-06 21:33:16|

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
|[Link](https://github.com/mozilla/release-services/commit/688dd403d87226a42ac26b9fbec5e7111e198c00)|backend_common/auth: we shouldn't touch permissions in decorator (#1929)|garbas|N/A|2019-03-07 11:36:09|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/60d08da601b6d4ad1f7ee59f00b63da638bc8244)|Merge pull request #199 from arshadkazmi42/tc-v1-yml-quick  Bug 1515673 - YML changed for v1 in QuickStart|owlishDeveloper|N/A|2019-03-07 03:38:04|
|[Link](https://github.com/taskcluster/taskcluster/commit/c6f305c2eb5594a398282d1cf0f9371aa646844f)|Merge pull request #355 from taskcluster/fix-oneshot-exit-in-test  Fix oneshot exit in test|imbstack|N/A|2019-03-06 21:36:11|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
