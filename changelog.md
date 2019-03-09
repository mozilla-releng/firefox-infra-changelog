##  Commits in production - for one day, generated on: 2019-03-08 21:02:09 UTC.
|	autoland	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=5d5db39b0497)|[Bug 1533391 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533391) - Lint Debugger on try. r=davidwalsh Differential Revision: https://phabricator.services.mozilla.com/D22503|jlaster@mozilla.com|davidwalsh|2019-03-08 22:06:17|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ef2b461b0a90)|[Bug 1529211 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1529211) Add new Raptor tests in tp6m-6 r=davehunt Differential Revision: https://phabricator.services.mozilla.com/D20820|fstrugariu@mozilla.com|davehunt|2019-03-08 11:40:59|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6b1f78426763)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Set worker `os` and `implementation` earlier in job transform; r=dustin This slightly decreases the amount of code that needs to know how to determine this. Differential Revision: https://phabricator.services.mozilla.com/D22446|mozilla@hocat.ca|dustin|2019-03-08 09:01:52|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=29168c60c4e6)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Move handling of windows scopes to taskgraph.transfroms.task; r=dustin Currently the scopes are handled in some test-specific code. However, there is logic not to be in generic code. Differential Revision: https://phabricator.services.mozilla.com/D22447|mozilla@hocat.ca|dustin|2019-03-08 09:01:52|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=54ed5eac2abc)|Backed out 2 changesets (bug 1532783) for causing Gecko Decision Task bustage. CLOSED TREE Backed out changeset 722b3915da31 (bug 1532783) Backed out changeset 421bdcc103d3 (bug 1532783)|nbeleuzu@mozilla.com||2019-03-08 08:46:36|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=421bdcc103d3)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Set worker `os` and `implementation` earlier in job transform; r=dustin This slightly decreases the amount of code that needs to know how to determine this. Differential Revision: https://phabricator.services.mozilla.com/D22446|mozilla@hocat.ca|dustin|2019-03-08 05:44:03|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=722b3915da31)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Move handling of windows scopes to taskgraph.transfroms.task; r=dustin Currently the scopes are handled in some test-specific code. However, there is logic not to be in generic code. Differential Revision: https://phabricator.services.mozilla.com/D22447|mozilla@hocat.ca|dustin|2019-03-08 05:44:03|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ea4a69b40a66)|[Bug 1533565 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533565) - Increase max-run-time for osx ccov builds; r=marco Differential Revision: https://phabricator.services.mozilla.com/D22615|gbrown@mozilla.com|marco|2019-03-08 04:03:43|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=3dc5de51e631)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Move Raptor chrome task definitions to separate file. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D21371|gmierz2@outlook.com|glandium|2019-03-08 04:02:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=225dab563b6d)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Add fetch tasks for raptor chromium builds. r=rwood,glandium,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21372|gmierz2@outlook.com|rwood,glandium,tomprince|2019-03-08 04:02:16|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=d91c333553e4)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Add missing configuration for nasm on hazard and plain builds. r=dmajor Differential Revision: https://phabricator.services.mozilla.com/D22451|mh@glandium.org|dmajor|2019-03-08 00:31:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=707ec85ae54c)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Remove nasm Debian packages. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22257|mh@glandium.org|dustin|2019-03-08 00:31:54|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=6c77b4a7cbd3)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Derive the diffoscope docker image from debian9-base. r=dustin Because the debian9-base apt configuration doesn't install recommended packages, we end up needing to install more packages than before. We could pass --install-recommended to apt-get, but that would make the image larger than it already was after the upcoming changes, because new versions of diffoscope come with more recommended dependencies. The side effect is that this makes the image much smaller than it used to be, while preserving all the useful recommended packages (we don't actually need all of them). Differential Revision: https://phabricator.services.mozilla.com/D22262|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=b1e1e1bba900)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Unbreak mach-o diffs after [Bug 1513798 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1513798) r=dustin Depends on D22262 Differential Revision: https://phabricator.services.mozilla.com/D22455|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=88e8b3f52329)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Ensure the base Debian docker image is up-to-date wrt the snapshot used. r=dustin When the apt snapshot is more recent than the docker image on the docker hub, some packages may not be up-to-date. Depends on D22455 Differential Revision: https://phabricator.services.mozilla.com/D22263|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ed46ddfa23b7)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Update to a more recent snapshot for Debian stretch-based docker images. r=dustin This has the side effect of addressing [Bug 1524723 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1524723) for those images. Depends on D22263 Differential Revision: https://phabricator.services.mozilla.com/D22264|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=4a6cb39329d1)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Install diffoscope from stretch-backports. r=dustin As of the update snapshot, stretch-backports contains version 112. Depends on D22264 Differential Revision: https://phabricator.services.mozilla.com/D22265|mh@glandium.org|dustin|2019-03-08 00:30:25|
|[Link](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=8e48fdd65475)|No bug - build cbindgen for macos using rust 1.32. r=froydnj 1.32 includes https://github.com/rust-lang/rust/pull/49219, which means new cbindgen no longer depends on compiler internals, which fixes some reported build issues on IRC.|aiakab@mozilla.com|froydnj|2019-03-08 00:14:58|

|	ci-admin	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)|FIC - BOT|Self Generated| - |

|	ci-configuration	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/ci/ci-configuration/pushloghtml?changeset=1f02faf115f2)|No bug: Cleanup in old fenix sentry secrets. r=jlorenzo|mtabara@mozilla.com|jlorenzo|2019-03-08 21:26:21|

|	mozilla-beta	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-beta.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=858a6e5a240a)|[Bug 1459222 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1459222) - Firefox RC: push snaps onto the beta channel at ship_rc phase r=mtabara a=release Firefox RC: push snaps onto the beta channel at ship_rc phase Differential Revision: https://phabricator.services.mozilla.com/D21380|jlorenzo@mozilla.com|mtabara|2019-03-08 15:21:37|

|	mozilla-central	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-central.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6b1f78426763)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Set worker `os` and `implementation` earlier in job transform; r=dustin This slightly decreases the amount of code that needs to know how to determine this. Differential Revision: https://phabricator.services.mozilla.com/D22446|shindli@mozilla.com|dustin|2019-03-08 15:49:21|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=29168c60c4e6)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Move handling of windows scopes to taskgraph.transfroms.task; r=dustin Currently the scopes are handled in some test-specific code. However, there is logic not to be in generic code. Differential Revision: https://phabricator.services.mozilla.com/D22447|shindli@mozilla.com|dustin|2019-03-08 15:49:21|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=615a12a92768)|[Bug 1532893 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532893) - Retry packages tasks when snapshot.debian.org doesn't respond. r=dustin [Bug 1486071 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1486071) intended to fix this, but while the tasks are setup to restart on exit status 100, there are multiple failure cases where snapshot.debian.org doesn't respond and the exit status is not 100. One is dget, when downloading package sources from snapshot.debian.org. Eventually, those should move to fetch tasks, but in the meantime, we bubble up get errors with an exit code 100. mk-build-deps wraps a call to apt-get install, but doesn't return the exit code that apt-get returns when apt-get returns one. It makes it hard to distinguish the error modes, but mk-build-deps is unlikely to fail on anything else than apt-get. Not all apt-get failures would be due to snapshot.debian.org availability, but that's a tradeoff we decided was okay in [Bug 1486071 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1486071) Differential Revision: https://phabricator.services.mozilla.com/D22269|shindli@mozilla.com|dustin|2019-03-08 15:49:21|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=6c77b4a7cbd3)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Derive the diffoscope docker image from debian9-base. r=dustin Because the debian9-base apt configuration doesn't install recommended packages, we end up needing to install more packages than before. We could pass --install-recommended to apt-get, but that would make the image larger than it already was after the upcoming changes, because new versions of diffoscope come with more recommended dependencies. The side effect is that this makes the image much smaller than it used to be, while preserving all the useful recommended packages (we don't actually need all of them). Differential Revision: https://phabricator.services.mozilla.com/D22262|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=b1e1e1bba900)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Unbreak mach-o diffs after [Bug 1513798 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1513798) r=dustin Depends on D22262 Differential Revision: https://phabricator.services.mozilla.com/D22455|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=88e8b3f52329)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Ensure the base Debian docker image is up-to-date wrt the snapshot used. r=dustin When the apt snapshot is more recent than the docker image on the docker hub, some packages may not be up-to-date. Depends on D22455 Differential Revision: https://phabricator.services.mozilla.com/D22263|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ed46ddfa23b7)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Update to a more recent snapshot for Debian stretch-based docker images. r=dustin This has the side effect of addressing [Bug 1524723 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1524723) for those images. Depends on D22263 Differential Revision: https://phabricator.services.mozilla.com/D22264|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4a6cb39329d1)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Install diffoscope from stretch-backports. r=dustin As of the update snapshot, stretch-backports contains version 112. Depends on D22264 Differential Revision: https://phabricator.services.mozilla.com/D22265|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=d91c333553e4)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Add missing configuration for nasm on hazard and plain builds. r=dmajor Differential Revision: https://phabricator.services.mozilla.com/D22451|shindli@mozilla.com|dmajor|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=707ec85ae54c)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Remove nasm Debian packages. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22257|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3dc5de51e631)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Move Raptor chrome task definitions to separate file. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D21371|shindli@mozilla.com|glandium|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=225dab563b6d)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Add fetch tasks for raptor chromium builds. r=rwood,glandium,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21372|shindli@mozilla.com|rwood,glandium,tomprince|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ea4a69b40a66)|[Bug 1533565 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533565) - Increase max-run-time for osx ccov builds; r=marco Differential Revision: https://phabricator.services.mozilla.com/D22615|shindli@mozilla.com|marco|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3fd4a7b0872e)|[Bug 1533445 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533445) - Make android tests shutdown faster when device unresponsive; r=bc Differential Revision: https://phabricator.services.mozilla.com/D22610|shindli@mozilla.com|bc|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=421bdcc103d3)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Set worker `os` and `implementation` earlier in job transform; r=dustin This slightly decreases the amount of code that needs to know how to determine this. Differential Revision: https://phabricator.services.mozilla.com/D22446|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=722b3915da31)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Move handling of windows scopes to taskgraph.transfroms.task; r=dustin Currently the scopes are handled in some test-specific code. However, there is logic not to be in generic code. Differential Revision: https://phabricator.services.mozilla.com/D22447|shindli@mozilla.com|dustin|2019-03-08 11:39:15|
|[Link](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=54ed5eac2abc)|Backed out 2 changesets (bug 1532783) for causing Gecko Decision Task bustage. CLOSED TREE Backed out changeset 722b3915da31 (bug 1532783) Backed out changeset 421bdcc103d3 (bug 1532783)|shindli@mozilla.com||2019-03-08 11:39:15|

|	mozilla-inbound	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/hg_files/mozilla-inbound.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6b1f78426763)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Set worker `os` and `implementation` earlier in job transform; r=dustin This slightly decreases the amount of code that needs to know how to determine this. Differential Revision: https://phabricator.services.mozilla.com/D22446|shindli@mozilla.com|dustin|2019-03-08 15:56:37|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=29168c60c4e6)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Move handling of windows scopes to taskgraph.transfroms.task; r=dustin Currently the scopes are handled in some test-specific code. However, there is logic not to be in generic code. Differential Revision: https://phabricator.services.mozilla.com/D22447|shindli@mozilla.com|dustin|2019-03-08 15:56:37|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=615a12a92768)|[Bug 1532893 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532893) - Retry packages tasks when snapshot.debian.org doesn't respond. r=dustin [Bug 1486071 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1486071) intended to fix this, but while the tasks are setup to restart on exit status 100, there are multiple failure cases where snapshot.debian.org doesn't respond and the exit status is not 100. One is dget, when downloading package sources from snapshot.debian.org. Eventually, those should move to fetch tasks, but in the meantime, we bubble up get errors with an exit code 100. mk-build-deps wraps a call to apt-get install, but doesn't return the exit code that apt-get returns when apt-get returns one. It makes it hard to distinguish the error modes, but mk-build-deps is unlikely to fail on anything else than apt-get. Not all apt-get failures would be due to snapshot.debian.org availability, but that's a tradeoff we decided was okay in [Bug 1486071 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1486071) Differential Revision: https://phabricator.services.mozilla.com/D22269|shindli@mozilla.com|dustin|2019-03-08 15:56:37|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=6c77b4a7cbd3)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Derive the diffoscope docker image from debian9-base. r=dustin Because the debian9-base apt configuration doesn't install recommended packages, we end up needing to install more packages than before. We could pass --install-recommended to apt-get, but that would make the image larger than it already was after the upcoming changes, because new versions of diffoscope come with more recommended dependencies. The side effect is that this makes the image much smaller than it used to be, while preserving all the useful recommended packages (we don't actually need all of them). Differential Revision: https://phabricator.services.mozilla.com/D22262|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=b1e1e1bba900)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Unbreak mach-o diffs after [Bug 1513798 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1513798) r=dustin Depends on D22262 Differential Revision: https://phabricator.services.mozilla.com/D22455|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=88e8b3f52329)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Ensure the base Debian docker image is up-to-date wrt the snapshot used. r=dustin When the apt snapshot is more recent than the docker image on the docker hub, some packages may not be up-to-date. Depends on D22455 Differential Revision: https://phabricator.services.mozilla.com/D22263|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ed46ddfa23b7)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Update to a more recent snapshot for Debian stretch-based docker images. r=dustin This has the side effect of addressing [Bug 1524723 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1524723) for those images. Depends on D22263 Differential Revision: https://phabricator.services.mozilla.com/D22264|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=4a6cb39329d1)|[Bug 1532878 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532878) - Install diffoscope from stretch-backports. r=dustin As of the update snapshot, stretch-backports contains version 112. Depends on D22264 Differential Revision: https://phabricator.services.mozilla.com/D22265|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=d91c333553e4)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Add missing configuration for nasm on hazard and plain builds. r=dmajor Differential Revision: https://phabricator.services.mozilla.com/D22451|shindli@mozilla.com|dmajor|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=707ec85ae54c)|[Bug 1532883 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532883) - Remove nasm Debian packages. r=dustin Differential Revision: https://phabricator.services.mozilla.com/D22257|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3dc5de51e631)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Move Raptor chrome task definitions to separate file. r=glandium Differential Revision: https://phabricator.services.mozilla.com/D21371|shindli@mozilla.com|glandium|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=225dab563b6d)|[Bug 1476372 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1476372) - Add fetch tasks for raptor chromium builds. r=rwood,glandium,tomprince Differential Revision: https://phabricator.services.mozilla.com/D21372|shindli@mozilla.com|rwood,glandium,tomprince|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=ea4a69b40a66)|[Bug 1533565 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533565) - Increase max-run-time for osx ccov builds; r=marco Differential Revision: https://phabricator.services.mozilla.com/D22615|shindli@mozilla.com|marco|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=3fd4a7b0872e)|[Bug 1533445 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1533445) - Make android tests shutdown faster when device unresponsive; r=bc Differential Revision: https://phabricator.services.mozilla.com/D22610|shindli@mozilla.com|bc|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=421bdcc103d3)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Set worker `os` and `implementation` earlier in job transform; r=dustin This slightly decreases the amount of code that needs to know how to determine this. Differential Revision: https://phabricator.services.mozilla.com/D22446|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=722b3915da31)|[Bug 1532783 ](https://bugzilla.mozilla.org/show_bug.cgi?id=1532783) [taskgraph] Move handling of windows scopes to taskgraph.transfroms.task; r=dustin Currently the scopes are handled in some test-specific code. However, there is logic not to be in generic code. Differential Revision: https://phabricator.services.mozilla.com/D22447|shindli@mozilla.com|dustin|2019-03-08 11:43:34|
|[Link](https://hg.mozilla.org/integration/mozilla-inbound/pushloghtml?changeset=54ed5eac2abc)|Backed out 2 changesets (bug 1532783) for causing Gecko Decision Task bustage. CLOSED TREE Backed out changeset 722b3915da31 (bug 1532783) Backed out changeset 421bdcc103d3 (bug 1532783)|shindli@mozilla.com||2019-03-08 11:43:34|

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
|[Link](https://github.com/mozilla-releng/build-puppet/commit/0d549acc0dcfd9358470c0612c5cf3b9feb6848c)|Merge pull request #420 from escapewindow/ed25519  roll out scriptworker 22 with ed25519|escapewindow|N/A|2019-03-08 18:00:53|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/9b5adc5583df288c5c9b2ce949c0ff8b9dc78765)|pin click to 6.7|escapewindow|N/A|2019-03-08 17:43:26|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/770357b36991409cdf3c5799e70d913b236a0d2b)|Merge branch 'master' into ed25519|escapewindow|N/A|2019-03-08 17:27:17|
|[Link](https://github.com/mozilla-releng/build-puppet/commit/c0cb221f878a7c26ffa02f35dd51f60fa8f85203)|Bug 1533563 - Bump pushsnapscript to 0.2.6 (#422)|JohanLorenzo|N/A|2019-03-08 14:29:45|

|	mozapkpublisher	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/mozapkpublisher.md)|FIC - BOT|Self Generated| - |

|	OpenCloudConfig	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/OpenCloudConfig.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/9e723b573a91a60b1f5fb74154d1df7562d51886)|Testing generic-worker 13.0.4 / taskcluster-proxy 5.1.0 on  STAGING   This change does _not_ affect any production workers. Commit made with:      ./gecko-try.sh 13.0.4 5.1.0  See https://github.com/taskcluster/generic-worker/blob/08e68a24b3fa73f2dc43af3d19ac6b28f44c477c/mozilla-try-scripts/gecko-try.sh  deploy: gecko-1-b-win2012-beta gecko-t-win10-64-beta gecko-t-win10-64-cu gecko-t-win10-64-gpu-b gecko-t-win10-64-hw-b gecko-t-win10-64-ux-b gecko-t-win10-a64-beta gecko-t-win7-32-beta gecko-t-win7-32-cu gecko-t-win7-32-gpu-b|petemoore|N/A|2019-03-08 19:06:58|
|[Link](https://github.com/mozilla-releng/OpenCloudConfig/commit/66f22171a3a1f2d0dab9aae1b86de350bf235e81)|Testing generic-worker 13.0.4 / taskcluster-proxy 5.1.0 on  STAGING   This change does _not_ affect any production workers. Commit made with:      ./gecko-try.sh 13.0.4 5.1.0  See https://github.com/taskcluster/generic-worker/blob/461c2fb847ecd28a59f7c8bf56d51e57d9fa5e90/mozilla-try-scripts/gecko-try.sh  deploy: gecko-1-b-win2012-beta gecko-t-win10-64-beta gecko-t-win10-64-cu gecko-t-win10-64-gpu-b gecko-t-win10-64-hw-b gecko-t-win10-64-ux-b gecko-t-win10-a64-beta gecko-t-win7-32-beta gecko-t-win7-32-cu gecko-t-win7-32-gpu-b|petemoore|N/A|2019-03-08 16:48:50|

|	pushapkscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushapkscript.md)|FIC - BOT|Self Generated| - |

|	pushsnapscript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/pushsnapscript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
|[Link](https://github.com/mozilla-releng/pushsnapscript/commit/8ce4053fb2d1c25fe749a402056086755c0367c2)|0.2.6|JohanLorenzo|N/A|2019-03-08 11:14:25|
|[Link](https://github.com/mozilla-releng/pushsnapscript/commit/efadd779e6dd63d4b58f14d373dbe6743c921d11)|Bug 1533563 - Unpin requests (#18)    Restrict it to >=2,<3|escapewindow|N/A|2019-03-08 11:12:24|

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
|[Link](https://github.com/taskcluster/taskcluster/commit/ab22724a50f60c87c06abd99783597a7ecb78340)|Merge pull request #369 from taskcluster/speed-back-up-q-test  Speed back up queue tests|imbstack|N/A|2019-03-08 19:42:15|
|[Link](https://github.com/taskcluster/taskcluster/commit/aa6695a81fc121f4b4f75eb39dec735fa6afa312)|Add comment as to why teardown needs to happen manually|imbstack|N/A|2019-03-08 16:59:45|
|[Link](https://github.com/taskcluster/taskcluster/commit/8ab2ab3703d4f506bc61493e1a2544a6181b74c2)|Merge pull request #370 from taskcluster/bug-1533493  [Bug 1533493] Remove old auditlogs terraform|imbstack|N/A|2019-03-08 16:57:33|
|[Link](https://github.com/taskcluster/taskcluster/commit/0f81a6e4345ec7e13667dc15cc138b580ae0400a)|Merge pull request #364 from ydidwania/bug-1523801  [Bug 1523801] Blacklist listening to some specific exchanges|djmitche|N/A|2019-03-07 23:00:34|
|[Link](https://github.com/taskcluster/taskcluster/commit/dcd2e2c8c46dfe1934a69496629b4314b5d5d6cf)|refactor: rename denyList to denylist. simplify format of denylsit in config.yml|ydidwania|N/A|2019-03-07 21:06:56|

|	treescript	|	[MarkDown](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)	|	[Json](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.json)	| 
|:----------:|:-----------------------:|:--------:| 
 
| Link | Last commit | Author | Reviewer | Deploy time | 
|:----------:|:-----------:|:------:|:--------:|:-----------:| 
| |No push in the last day.. [see the history of MD commits](https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/git_files/treescript.md)|FIC - BOT|Self Generated| - |
