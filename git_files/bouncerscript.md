## BOUNCER SCRIPT MARKDOWN TABLE

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|30|Justin Wood (Callek)|Merge pull request #46 from Callek/3.3.0  Bump to 3.3.0 for MSI installer|[URL](https://github.com/mozilla-releng/bouncerscript/commit/c3be67b9b8886f78514503b97ff055553fbe77f2)|2018-11-12 16:20:14 
|29|Justin Wood|Bump to 3.3.0 for MSI installer|[URL](https://github.com/mozilla-releng/bouncerscript/commit/14820782bf1f83eabfa396b036b60e78df596399)|2018-11-12 16:01:24 
|28|Justin Wood (Callek)|Merge pull request #43 from Callek/msi  Support .msi in bouncerscript|[URL](https://github.com/mozilla-releng/bouncerscript/commit/3792c3106c05c09875cdf9634e6da305188a9b95)|2018-11-12 15:09:06 
|27|Mihai Tabara|Merge branch 'master' into msi|[URL](https://github.com/mozilla-releng/bouncerscript/commit/3409785ede3fa3a0377b8cee3e5bca3ab49757ed)|2018-11-10 09:49:19 
|26|Mihai Tabara|Fix logging (#45)|[URL](https://github.com/mozilla-releng/bouncerscript/commit/a88e5f643bd2671cc47c6240a2794d8d11a5d792)|2018-11-10 09:49:02 
|25|Justin Wood|Support msi for aliases and product submission|[URL](https://github.com/mozilla-releng/bouncerscript/commit/ce515b8a8bd853c39f3f87d848017b0c3e8b63e7)|2018-11-08 20:53:47 
|24|Justin Wood|Add msi support for nightly locations|[URL](https://github.com/mozilla-releng/bouncerscript/commit/a4f4426a5935e5c1267f7ba752df44ffda14dc12)|2018-11-02 20:00:05 
|23|Mihai Tabara|Add documentation for bouncerscript logic. (#44)|[URL](https://github.com/mozilla-releng/bouncerscript/commit/7c86c5cf2340ad691a43993dbc8e05e31f31e4ce)|2018-11-08 13:33:35 
|22|Justin Wood (Callek)|Merge pull request #42 from Callek/flake8_update  Fix flake8 issues with newest package|[URL](https://github.com/mozilla-releng/bouncerscript/commit/bb85d6ac0677760b6f28082f13b4e9c065d8fbc1)|2018-11-02 20:33:51 
|21|Justin Wood|Fix flake8 issues with newest package|[URL](https://github.com/mozilla-releng/bouncerscript/commit/cffb0e05872cbfb3dd657a512e3fa4efa2429db9)|2018-11-02 18:27:30 
|20|Tom Prince|Merge pull request #41 from tp-tc/stub-path-platforms   Check that paths exist per-platform.|[URL](https://github.com/mozilla-releng/bouncerscript/commit/89da29e5bd9ea8c5063f526b2c73e45159f2bdb8)|2018-09-04 22:05:15 
|19|Tom Prince|3.2.1|[URL](https://github.com/mozilla-releng/bouncerscript/commit/3e8b26caf9477d8c56cdbd8fa9a886c079597695)|2018-09-04 21:39:08 
|18|Tom Prince|Check that paths exist per-platform.|[URL](https://github.com/mozilla-releng/bouncerscript/commit/5562ee3ae80469bc06bf4e2df1cf48aa027de7f6)|2018-09-04 21:36:45 
|17|Mihai Tabara|3.2.0|[URL](https://github.com/mozilla-releng/bouncerscript/commit/e2fd6912146ff0dbbb9abe59b9e9abb0a04d95c5)|2018-09-03 22:22:31 
|16|Lisa Guo|automate nightly latest bouncer products; bump to 3.2.0(#32)    Added main bouncer_locations function, and helper functions. Untested.      Added locations regexes. Need to confirm for firefox-nightly-ssl, firefox-nightly-latest-l10n, firefox-nightly-latest-l10n-ssl      WIP. fix existing tests. finish high-level logic      100% code coverage on utils.py      100% code coverage on task.py      100% code coverage on script.py      Add SCOPES.md      Add missing test in test_check_aliases_match.      s,LOCATION_TO_DESTINATIONS_REGEXES,BOUNCER_PATH_REGEXES_PER_PRODUCT      s,locations_entries,bouncer_products + amend corresponding contexts.      Terminology fix and logging improvement      Amend CHANGELOG.      Use mozilla-version over hacks. Terminology cleanup      Refactor get_locations_info to split in more granular methods      Refactoring & renaming functions.      Add yet another test for completition.      Remove blank line      Fix tests to use get_locations_info instead of get_locations_paths      Remove duplicate false_async in testing      Remove useless import      Fix tests coverage.      Update bouncerscript to 3.2.0|[URL](https://github.com/mozilla-releng/bouncerscript/commit/7ec11e05e7a8bbf688e664a3cbfdb1c1c863591c)|2018-09-03 22:20:20 
|15|Johan Lorenzo|Bug 1486747 - Bouncer submission: Locations aren't added/checked if t… (#40)|[URL](https://github.com/mozilla-releng/bouncerscript/commit/91bb469a46cc6244b7eb4034f719f8886d87f9e8)|2018-08-31 14:07:31 
|14|Johan Lorenzo|Add comment about PRODUCT_TO_PRODUCT_ENTRY|[URL](https://github.com/mozilla-releng/bouncerscript/commit/77b0c2c251a5e13fc5638be8f854653e9e6b3ac6)|2018-08-28 07:16:13 
|13|Tom Prince|Bump version.|[URL](https://github.com/mozilla-releng/bouncerscript/commit/09427a51259517cad1abdc4ee8c1c7120249fc7f)|2018-08-27 22:58:38 
|12|Tom Prince|Require firefox rc build entries to point to candidates.|[URL](https://github.com/mozilla-releng/bouncerscript/commit/d9d94a6eccc0bae1a99ee25605e8ec61f138c54e)|2018-08-27 22:54:18 
|11|Aki Sasaki|Merge pull request #33 from escapewindow/py37  require py37 tests to be green|[URL](https://github.com/mozilla-releng/bouncerscript/commit/54f34fdd452bedb4ad9b314eba152ae497362be9)|2018-07-27 21:45:21 
|10|Aki Sasaki|use the pytest-asyncio event_loop fixture|[URL](https://github.com/mozilla-releng/bouncerscript/commit/61f118af68d0c1376abfbf82581ea33646c3aec1)|2018-07-27 21:41:18 
|9|Aki Sasaki|require py37 tests to be green|[URL](https://github.com/mozilla-releng/bouncerscript/commit/559c5196f4c6e62cfbde5f421b665c7ba3e57beb)|2018-07-27 21:36:37 
|8|Mihai Tabara|Merge pull request #24 from Callek/SCOPES.md  Add SCOPES.md|[URL](https://github.com/mozilla-releng/bouncerscript/commit/591466df69d922e9e2dff11b1ae3f771d3cd6a03)|2018-07-12 14:51:04 
|7|Mihai Tabara|Merge branch 'master' into SCOPES.md|[URL](https://github.com/mozilla-releng/bouncerscript/commit/d0ab56713fbf3aae739be740878409760c1f0450)|2018-07-12 14:11:41 
|6|Mihai Tabara|3.0.0|[URL](https://github.com/mozilla-releng/bouncerscript/commit/3faab785a53183af0282f1b4e94109b53dacffaa)|2018-07-11 21:29:40 
|5|Mihai Tabara|Merge pull request #31 from MihaiTabara/leaf-alias  Add checks to validate the bouncer aliases values after API calls.|[URL](https://github.com/mozilla-releng/bouncerscript/commit/205665d0a0ee8a496233c451c8ce6734fb29914a)|2018-07-10 17:14:21 
|4|Mihai Tabara|More accurate exceptions handling.|[URL](https://github.com/mozilla-releng/bouncerscript/commit/ed51b97e8c933218929b8c16a5afe3f5c2282059)|2018-07-10 13:49:28 
|3|Mihai Tabara|More verbose variable names.|[URL](https://github.com/mozilla-releng/bouncerscript/commit/46dde165452a51e07d7e2344aa43d0cd7a66c7af)|2018-07-10 13:19:43 
|2|Mihai Tabara|Amend test to reuse provided/expected|[URL](https://github.com/mozilla-releng/bouncerscript/commit/47ddc9867cda202e4b0fe6410b8d52b69b1671ac)|2018-07-10 12:24:15 
|1|Mihai Tabara|Add docstrings|[URL](https://github.com/mozilla-releng/bouncerscript/commit/e6ced33109eba9cfa2afa1284fdab175a1157fad)|2018-07-10 09:46:31 


