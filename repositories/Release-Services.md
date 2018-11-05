## RELEASE-SERVICES MARKDOWN TABLE

| Commit Number | Commiter | Commit Message | Date | 
|:---:|:----:|:----------------------------------:|:----:| 
|0|Bastien Abadie|docs: Remove IRC notification (#1646)|2018-11-02T15:15:35Z
|1|Rok Garbas|tooltool/api: upload does not work (#1667)    backend_common: wrong relengapi token serializer used      tooltool/api: wrong flask subcommand used      releng_frontend: sha of node module changed      releng_frontend: pass correct variables to body      releng_frontend: serve static folder when development|2018-11-02T14:23:59Z
|2|Rail Aliiev|shipit/frontend: Add release ETA (#1658)    Add release ETA      Add better validation      Remove margins|2018-11-02T14:23:02Z
|3|Rail Aliiev|shipit/api: add /sync API (#1665)    shipit/api: add /sync API    This is a reland of #1517. It was tested in staging and worked fine  without any issues so far.      Remove temp hack|2018-11-02T14:22:49Z
|4|Tom Prince|shipit/frontend: Generate partial suggestions when selecting a revision manually. (#1666)|2018-11-02T00:31:32Z
|5|ANdi|staticanalysis/bot: Update cbindgen to 0.6.7 (#1663)|2018-10-31T12:03:11Z
|6|Rail Aliiev|Fix IRC env var (#1660)|2018-10-30T16:35:56Z
|7|Rail Aliiev|shipit/api: Use env vars for TC IRC notifications (#1659)    Use env vars for TC IRC notifications      Fallback to secrets|2018-10-30T16:17:39Z
|8|Rail Aliiev|shipit/frontend: Use BACKEND_URL (renamed to SHIPIT_API_URL) from data-shipit-api-url for accessing backend (#1656)|2018-10-30T08:18:30Z
|9|Bastien Abadie|staticanalysis/bot: Update rust-cbindgen to 0.6.6 (#1654)|2018-10-29T09:37:54Z
|10|Bastien Abadie|staticanalysis/frontend: Load all tasks & support http errors (#1651)|2018-10-26T09:44:46Z
|11|Bastien Abadie|uplift/frontend: Display issue level & type for infer issues. (#1652)|2018-10-25T20:06:50Z
|12|Bastien Abadie|setup: bumping to v50 (#1639)|2018-10-25T19:58:05Z
|13|ANdi|Add to logger if we don't have clang nor infer files into the revision. (#1648)|2018-10-25T19:23:32Z
|14|Rail Aliiev|shipit/frontend: Revert "Use BACKEND_URL from data-shipit-api-url for accessing backend." (#1653)|2018-10-25T17:34:31Z
|15|Marco|codecoverage/bot: Update ActiveData query URL (#1644)|2018-10-24T20:11:57Z
|16|ANdi|staticanalysis/bot: Create gradle properties file that prevents gradle from running in daemon mode (#1643)|2018-10-24T18:13:17Z
|17|Marco|codecoverage/bot: Fix detection of Windows platforms (#1642)|2018-10-24T16:21:32Z
|18|Marco| codecoverage/bot: Consider build machines as test platforms as they could contain coverage artifacts (#1637)|2018-10-24T10:50:06Z
|19|Rahul Verma|please_cli: Notify '#ci' and '#moc' IRC channels that deployment to production is about to start.(#1568) (#1634)|2018-10-23T16:47:24Z
|20|Tom Prince|shipit/frontend: Use URL from data-shipit-api-url for accessing backend. (#1636)|2018-10-23T16:19:37Z
|21|Rahul Verma| staticanalysis/bot: Allow justifying clang-tidy checkers with a 'reason' text field #1556, fixes #1481|2018-10-23T14:36:46Z
|22|Bastien Abadie|uplift/frontend: Remove project #1638, fixes #1617|2018-10-23T14:15:54Z
|23|Bastien Abadie|staticanalysis/bot: Add localtime and zoneinfo for infer  (#1632)|2018-10-23T12:52:07Z
|24|Andi-Bogdan Postelnicu|staticanalysis/bot: Pass _JAVA_OPTIONS envrionment variable to set a hard-coded home directory for Java (#1635)|2018-10-18T16:22:09Z
|25|Marco|codecoverage/bot: Don't fail when a file is removed by a commit and then the commit is backed out in the same push (#1619)|2018-10-19T13:57:33Z
|26|Rahul Verma|setup: Notify via IRC when deployment happens (#1623)|2018-10-19T10:56:26Z
|27|Bastien Abadie|staticanalysis/bot: Fix dummy leftover bug (#1631)|2018-10-19T10:15:57Z
|28|Bastien Abadie|staticanalysis/bot: Filter Phabricator analyzers to publish (#1626)|2018-10-18T13:54:58Z
|29|Bastien Abadie|staticanalysis/bot: Use improvement patches built by analyzers #1624 #1271|2018-10-18T12:40:42Z


