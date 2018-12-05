## REPOSITORY NAME: SERVICES
 CURRENT VERSION: V51 RELEASED ON WED, 21 NOV 2018 18:05:34 GMT

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|17|La0|staticanalysis/bot: Filter clang-format publishable issues by their path. (#1689)|[URL](https://github.com/mozilla/release-services/commit/ae0004b50d4d2252d5b8ed3d3d3aa232a1412d14)|2018-11-20 15:36:16
|16|kevinluvian|codecoverage/backend: Add test for codecoverage backend with mocked rq and Redis (#1673)|[URL](https://github.com/mozilla/release-services/commit/f5434b1aff3d78db8bfceae7cfa872382c4b1d9f)|2018-11-20 11:57:13
|15|jankeromnes|uplift/bot: Add a BUGZILLA_COMMENT_ONLY setting in order to report failed uplifts without cancelling requests. (#1680)|[URL](https://github.com/mozilla/release-services/commit/88b939c265b26fe9e960d7a3361648d9ea522af6)|2018-11-20 09:34:34
|14|rail|shipit/frontent: add testing config (#1687)  At this point it is the same as staging.js|[URL](https://github.com/mozilla/release-services/commit/3399eed333cb502e46c5a7b83f3673d0fb4faafb)|2018-11-20 01:39:45
|13|rail|shipit/api: update release status (#1688)  In the future we will need to update the release status explicitly from  a in-tree scheduled task, so we mark a release as completed only after  all required tasks are done (bouncer, tests, etc).|[URL](https://github.com/mozilla/release-services/commit/37bc7cafe221c5cea7d33041125d95312fe7757f)|2018-11-19 20:45:16
|12|rail|shipit/api: Fix release sync, add dates (#1684)  Initially I didn't add the started/completed datetimes to the sync  functionality, probably because they are not exposed in the constructor.    Additionally I added an API endpoint to sync the datetimes only.|[URL](https://github.com/mozilla/release-services/commit/4117cbaa527bd0a7d70edd0e9ad15cc1a0f6ee6f)|2018-11-19 15:19:47
|11|rail|backend_common: add swagger_ui (#1685)  connexion 2.0 doesn't bundle swagger UI anymore by default, so the  projects that enable the API extension don't get it installed. I also  regenerated the dependencies of the projects that switched to connexion  2.0.|[URL](https://github.com/mozilla/release-services/commit/a508a60b9049302aae8c8128467d2646a345b38a)|2018-11-19 15:01:56
|10|La0|staticanalysis/bot: Bump rust to 1.30.0 (#1686)|[URL](https://github.com/mozilla/release-services/commit/75d8a9229cf31db102d7cc69c58fe4bfd26fc724)|2018-11-19 11:15:41
|9|garbas|tooltool/api: use app.cli.add_command instead of decorator for flask subcommands (#1683)|[URL](https://github.com/mozilla/release-services/commit/bf1f4e93bd3f54c23a4cebaf844dfa977339c0a4)|2018-11-15 18:28:53
|8|marco-c|codecoverage/bot: Use a placeholder chunk for build tasks to avoid having empty chunks (#1682)|[URL](https://github.com/mozilla/release-services/commit/ce6a87eb0c462e98e353c8c6b5a06ad9caf7e5a3)|2018-11-14 17:38:32
|7|kevinluvian|please-cli: refactor mkProject to only pass project_name (#1678)|[URL](https://github.com/mozilla/release-services/commit/0efec3094069275c8c9155bfc4d70ffd9cace3bb)|2018-11-13 00:48:39
|6|kevinluvian|please-cli: display in which project shell you are (#1676)|[URL](https://github.com/mozilla/release-services/commit/55795964c7b8af1f658ae4cf0437f90ac284f86f)|2018-11-13 00:16:42
|5|garbas|setup: update dependencies (#1670)|[URL](https://github.com/mozilla/release-services/commit/591e05867afb6a7dd5fb3917aac0511d323f9110)|2018-11-12 23:36:45
|4|marco-c|staticanalysis/bot: Update parsepatch to latest version and add a regression test for checking if an issue is in a revision (#1679)    staticanalysis/bot: Add tests for Revision.analyze_patch      staticanalysis/bot: Update parsepatch to 0.1.3|[URL](https://github.com/mozilla/release-services/commit/77b4e9d1b463b01ab4fdc56cbef1a71176e5ddf8)|2018-11-12 16:40:20
|3|jankeromnes|staticanalysis/bot: Use the right diffs for the improvement patch. (#1671)|[URL](https://github.com/mozilla/release-services/commit/e505e8e2aad9ff34e5dc2f9e8cbe100684ca9200)|2018-11-08 13:47:00
|2|garbas|setup: bumping to v51 (#1672)|[URL](https://github.com/mozilla/release-services/commit/8650a55cb9e33bcbe429ad9e3a8b5759e530129b)|2018-11-07 22:14:32
|1|La0|docs: Remove IRC notification (#1646)|[URL](https://github.com/mozilla/release-services/commit/b9843defb782381398b0c486d6cc87e9fbc33599)|2018-11-02 15:15:35


