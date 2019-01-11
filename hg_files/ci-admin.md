## REPOSITORY NAME: CI-ADMIN
 CURRENT PUSH ID: 31

| Changeset | Date | Commiter | Commit Message | Commit URL | 
|:---:|:---:|:----:|:----------------------------------:|:-----:| 
|31|2019-01-02 22:26:29|Aki Sasaki <asasaki@mozilla.com>|Bug 1485680 - if we modify the action hook task logic, we need to update scriptworker. r=dustinDifferential Revision: https://phabricator.services.mozilla.com/D15482|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=b2d0f7af52d2
|30|2018-12-18 21:48:17|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1515137 - pass environment rootUrl to cron context r=tomprinceDifferential Revision: https://phabricator.services.mozilla.com/D14882|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=0f4b1e9e03cd
|29|2018-10-22 20:53:12|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1492665 - add support for environments.yml r=Callek,bstackDifferential Revision: https://phabricator.services.mozilla.com/D6932|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=241f75b5d808
|29|2018-10-22 20:53:12|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1492665 - add modify_resources support r=Callek,bstackDifferential Revision: https://phabricator.services.mozilla.com/D6933|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=99d859a7a655
|28|2018-10-22 20:50:28|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1494320 - remove unnecessary resources.manage r=tomprinceThese were in place in order to delete some old, now-unused roles.  They'regone, so no need to continue to manage those namespaces.Differential Revision: https://phabricator.services.mozilla.com/D9166|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=d1796b61fbd0
|27|2018-09-26 05:49:00|Tom Prince <mozilla@hocat.ca>|Don't generate hooks for actions with cross trust-domain `.taskcluster.yml`s; r=dustinDifferential Revision: https://phabricator.services.mozilla.com/D6858|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=9d35e153d813
|26|2018-09-12 23:04:50|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1489181: handle input_schema in actions.yml r=akiDifferential Revision: https://phabricator.services.mozilla.com/D5683|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=c88ca415a1c6
|25|2018-09-11 21:00:43|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1490066: fix unit tests and add a few r=tomprinceI broke the unit tests in bug 1488766 and also introduced a bug (no longerallowing granting to a single group); this fixes that up and even adds sometests.Differential Revision: https://phabricator.services.mozilla.com/D5464|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=edad9f8f78d4
|24|2018-09-10 17:54:50|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1489983: fix markdown link in descriptions r=janxDifferential Revision: https://phabricator.services.mozilla.com/D5430|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=5b8819a7b072
|23|2018-09-07 22:42:24|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1488766: improve error handling for malformed grants.yml r=tomprinceDifferential Revision: https://phabricator.services.mozilla.com/D5158|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=135f264d65d2
|22|2018-09-07 22:42:11|Dustin J. Mitchell <dustin@mozilla.com>|Bug 1488766: also substitute {hgmo_path} r=tomprinceDifferential Revision: https://phabricator.services.mozilla.com/D5155|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=95397719f02d
|21|2018-09-06 01:14:08|Dustin J. Mitchell <dustin@mozilla.com>|(hotfix) add created and expires to .taskcluster.yml|https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=559c3f6fd329


