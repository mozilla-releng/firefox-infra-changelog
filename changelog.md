##  Commits in production - for one day, generated on: 2019-03-02 20:34:05 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=811caa480654)|[Bug 1526419 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526419) - add mar-signing-autograph-stage task r=Callek We use autograph-prod for our ci, nightly, and release signing. Autograph-stage doesn't have the same guarantees for availability, so pointing, say, dep-signing at autograph-stage would have resulted in occasional tree closures whenever autograph-stage changes configuration or is down. However, we also want a way to verify autograph-stage is still valid, after the autograph team makes changes. This task is meant to be add-task'ed; a green result means autograph-stage has signed the mar file correctly. Differential Revision: https://phabricator.services.mozilla.com/D20749|asasaki@mozilla.com|Callek|2019-03-02 01:55:40|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3b08a133c893)|[Bug 1519472 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1519472) Disable caches on windows repackage builds; r=aki a=tomprince They appear to be causing tasks to take several hours to complete. Differential Revision: https://phabricator.services.mozilla.com/D21775|dluca@mozilla.com|aki|2019-03-02 01:24:21|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=2bd9674d85a1)|Merge mozilla-central to autoland|dluca@mozilla.com||2019-03-02 01:24:21|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=a88b39ffb1f1)|[Bug 1513000 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1513000) [openh264] Adjust `create_tasks` call in openh264 action for [Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) r=Callek Differential Revision: https://phabricator.services.mozilla.com/D21794|mozilla@hocat.ca|Callek|2019-03-02 00:20:58|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ac3747e1e5da)|[Bug 1456855 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1456855) Install a newer freetype from Ubuntu bionic (18.04) r=Callek Differential Revision: https://phabricator.services.mozilla.com/D21360|jmaher@mozilla.com|Callek|2019-03-01 23:07:21|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=02dec1fe0aca)|[Bug 1531592 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531592) [taskgraph] Ensure that treeherder platform has the correct format; r=dustin A recent change caused the treeherder platform for several jobs to have an extra `/` in it. This add a check to ensure that the platform is formatted correctly, and fixes the tasks with the incorrect format. Differential Revision: https://phabricator.services.mozilla.com/D21650|mozilla@hocat.ca|dustin|2019-03-01 21:55:13|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=290bdcdf2b63)|[Bug 1482231 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1482231) - Increase test chunks for geckoview-junit to avoid intermittent timeouts; r=jmaher Increase test chunks for Android 4.3 /opt and /debug and ccov geckoview-junit. Most chunks run in 20 to 30 minutes with this change: https://treeherder.mozilla.org/#/jobs?repo=try&tier=1%2C2%2C3&revision=a952f0dde8b508d8f87867757d98ca2642cbd48c Differential Revision: https://phabricator.services.mozilla.com/D21762|gbrown@mozilla.com|jmaher|2019-03-01 21:25:37|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=bd930453714e)|[Bug 1531499 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531499) - additional workaround for Windows 32bit incorrectly reporting failure for reftest r=jmaher,ahal Changes: - modified the criteria for using 1 as the successful return code by using a combination of factors; is it Windows, is it 32bit, and is it Reftest. Differential Revision: https://phabricator.services.mozilla.com/D21596|egao@mozilla.com|jmaher,ahal|2019-03-01 20:53:04|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=44e7a91589a3)|[Bug 1530732 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530732) Grant access to level-3 pgo testers; r=dustin Additionally, make sure that other levels can't access them. Differential Revision: https://phabricator.services.mozilla.com/D21754|mozilla@hocat.ca|dustin|2019-03-01 20:58:22|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)|FIC - BOT|Self Generated| - |

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=45b6b4f345d5)|[Bug 1530391 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530391) Disable hg extensions incompatible automated tasks r=dustin I've set HGPLAIN in the container entrypoint so that people running the main script interactively still get the nice features. Differential Revision: https://phabricator.services.mozilla.com/D21343|rmaries@mozilla.com|dustin|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7f3e90c4b9c2)|[Bug 1529210 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1529210) Add new Raptor tests in tp6m-5 r=davehunt Differential Revision: https://phabricator.services.mozilla.com/D20815|rmaries@mozilla.com|davehunt|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=dcfebc36f75c)|[Bug 1531441 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531441) - Re-enable Raptor android ugl temporarily as tier 3, pending benchmark upgrade; r=davehunt Differential Revision: https://phabricator.services.mozilla.com/D21713|rmaries@mozilla.com|davehunt|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ccd70bb02d61)|[Bug 1531234 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531234) - Write JS test structured logs to main_raw.log instead of intermixing them in stdout r=ahal Differential Revision: https://phabricator.services.mozilla.com/D21483|rmaries@mozilla.com|ahal|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=bd930453714e)|[Bug 1531499 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531499) - additional workaround for Windows 32bit incorrectly reporting failure for reftest r=jmaher,ahal Changes: - modified the criteria for using 1 as the successful return code by using a combination of factors; is it Windows, is it 32bit, and is it Reftest. Differential Revision: https://phabricator.services.mozilla.com/D21596|rmaries@mozilla.com|jmaher,ahal|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=290bdcdf2b63)|[Bug 1482231 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1482231) - Increase test chunks for geckoview-junit to avoid intermittent timeouts; r=jmaher Increase test chunks for Android 4.3 /opt and /debug and ccov geckoview-junit. Most chunks run in 20 to 30 minutes with this change: https://treeherder.mozilla.org/#/jobs?repo=try&tier=1%2C2%2C3&revision=a952f0dde8b508d8f87867757d98ca2642cbd48c Differential Revision: https://phabricator.services.mozilla.com/D21762|rmaries@mozilla.com|jmaher|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=02dec1fe0aca)|[Bug 1531592 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531592) [taskgraph] Ensure that treeherder platform has the correct format; r=dustin A recent change caused the treeherder platform for several jobs to have an extra `/` in it. This add a check to ensure that the platform is formatted correctly, and fixes the tasks with the incorrect format. Differential Revision: https://phabricator.services.mozilla.com/D21650|rmaries@mozilla.com|dustin|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ac3747e1e5da)|[Bug 1456855 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1456855) Install a newer freetype from Ubuntu bionic (18.04) r=Callek Differential Revision: https://phabricator.services.mozilla.com/D21360|rmaries@mozilla.com|Callek|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a88b39ffb1f1)|[Bug 1513000 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1513000) [openh264] Adjust `create_tasks` call in openh264 action for [Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) r=Callek Differential Revision: https://phabricator.services.mozilla.com/D21794|rmaries@mozilla.com|Callek|2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=2bd9674d85a1)|Merge mozilla-central to autoland|rmaries@mozilla.com||2019-03-02 11:26:10|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=811caa480654)|[Bug 1526419 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526419) - add mar-signing-autograph-stage task r=Callek We use autograph-prod for our ci, nightly, and release signing. Autograph-stage doesn't have the same guarantees for availability, so pointing, say, dep-signing at autograph-stage would have resulted in occasional tree closures whenever autograph-stage changes configuration or is down. However, we also want a way to verify autograph-stage is still valid, after the autograph team makes changes. This task is meant to be add-task'ed; a green result means autograph-stage has signed the mar file correctly. Differential Revision: https://phabricator.services.mozilla.com/D20749|rmaries@mozilla.com|Callek|2019-03-02 11:26:10|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=45b6b4f345d5)|[Bug 1530391 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1530391) Disable hg extensions incompatible automated tasks r=dustin I've set HGPLAIN in the container entrypoint so that people running the main script interactively still get the nice features. Differential Revision: https://phabricator.services.mozilla.com/D21343|rmaries@mozilla.com|dustin|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=7f3e90c4b9c2)|[Bug 1529210 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1529210) Add new Raptor tests in tp6m-5 r=davehunt Differential Revision: https://phabricator.services.mozilla.com/D20815|rmaries@mozilla.com|davehunt|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=dcfebc36f75c)|[Bug 1531441 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531441) - Re-enable Raptor android ugl temporarily as tier 3, pending benchmark upgrade; r=davehunt Differential Revision: https://phabricator.services.mozilla.com/D21713|rmaries@mozilla.com|davehunt|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ccd70bb02d61)|[Bug 1531234 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531234) - Write JS test structured logs to main_raw.log instead of intermixing them in stdout r=ahal Differential Revision: https://phabricator.services.mozilla.com/D21483|rmaries@mozilla.com|ahal|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=bd930453714e)|[Bug 1531499 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531499) - additional workaround for Windows 32bit incorrectly reporting failure for reftest r=jmaher,ahal Changes: - modified the criteria for using 1 as the successful return code by using a combination of factors; is it Windows, is it 32bit, and is it Reftest. Differential Revision: https://phabricator.services.mozilla.com/D21596|rmaries@mozilla.com|jmaher,ahal|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=290bdcdf2b63)|[Bug 1482231 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1482231) - Increase test chunks for geckoview-junit to avoid intermittent timeouts; r=jmaher Increase test chunks for Android 4.3 /opt and /debug and ccov geckoview-junit. Most chunks run in 20 to 30 minutes with this change: https://treeherder.mozilla.org/#/jobs?repo=try&tier=1%2C2%2C3&revision=a952f0dde8b508d8f87867757d98ca2642cbd48c Differential Revision: https://phabricator.services.mozilla.com/D21762|rmaries@mozilla.com|jmaher|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=02dec1fe0aca)|[Bug 1531592 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1531592) [taskgraph] Ensure that treeherder platform has the correct format; r=dustin A recent change caused the treeherder platform for several jobs to have an extra `/` in it. This add a check to ensure that the platform is formatted correctly, and fixes the tasks with the incorrect format. Differential Revision: https://phabricator.services.mozilla.com/D21650|rmaries@mozilla.com|dustin|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ac3747e1e5da)|[Bug 1456855 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1456855) Install a newer freetype from Ubuntu bionic (18.04) r=Callek Differential Revision: https://phabricator.services.mozilla.com/D21360|rmaries@mozilla.com|Callek|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=a88b39ffb1f1)|[Bug 1513000 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1513000) [openh264] Adjust `create_tasks` call in openh264 action for [Bug 1528362 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1528362) r=Callek Differential Revision: https://phabricator.services.mozilla.com/D21794|rmaries@mozilla.com|Callek|2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=2bd9674d85a1)|Merge mozilla-central to autoland|rmaries@mozilla.com||2019-03-02 12:10:00|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=811caa480654)|[Bug 1526419 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1526419) - add mar-signing-autograph-stage task r=Callek We use autograph-prod for our ci, nightly, and release signing. Autograph-stage doesn't have the same guarantees for availability, so pointing, say, dep-signing at autograph-stage would have resulted in occasional tree closures whenever autograph-stage changes configuration or is down. However, we also want a way to verify autograph-stage is still valid, after the autograph team makes changes. This task is meant to be add-task'ed; a green result means autograph-stage has signed the mar file correctly. Differential Revision: https://phabricator.services.mozilla.com/D20749|rmaries@mozilla.com|Callek|2019-03-02 12:10:00|

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
|[Link](https://github.com/mozilla-releng/build-puppet/commit/0cf36813cfdbb1fc5fcf5bc427449c4119eb6c82)|Scheduled weekly dependency update for week 08 (#406)    Update cffi from 1.11.5 to 1.12.2      Update cffi from 1.12.1 to 1.12.2      Update cffi from 1.11.5 to 1.12.2      Update cffi from 1.11.5 to 1.12.2      Update cffi from 1.11.5 to 1.12.2      Update cffi from 1.12.1 to 1.12.2      Update cffi from 1.12.1 to 1.12.2      Update cffi from 1.11.5 to 1.12.2      Update cffi from 1.12.1 to 1.12.2      Update cffi from 1.12.1 to 1.12.2      Update cffi from 1.11.5 to 1.12.2      Update cffi from 1.11.5 to 1.12.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update dictdiffer from 0.7.1 to 0.7.2      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update jsonschema from 2.6.0 to 3.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update slugid from 1.0.7 to 2.0.0      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update virtualenv from 16.4.0 to 16.4.1      Update markupsafe from 1.1.0 to 1.1.1      Update markupsafe from 1.1.0 to 1.1.1      Update markupsafe from 1.1.0 to 1.1.1      Update boto3 from 1.9.98 to 1.9.103      Update botocore from 1.12.98 to 1.12.103      Update jmespath from 0.9.3 to 0.9.4      Update jedi from 0.13.2 to 0.13.3      Update numpy from 1.16.1 to 1.16.2      Update prompt_toolkit from 2.0.8 to 2.0.9      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      reverted slugid from 2.0.0 to 1.0.7      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      revert jsonschema from 3.0.0 to 2.6.0      treescript jsonschema==2.6.0|pyup-bot|N/A|2019-03-02 01:59:46|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/73730cd7bf12b86df82d3dd17a46d2186b4cac9f)|Merge pull request #335 from owlishDeveloper/bug1531606  DB migration: add a table|owlishDeveloper|N/A|2019-03-01 23:42:10|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
