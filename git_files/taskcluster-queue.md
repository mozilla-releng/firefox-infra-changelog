## TASKCLUSTER-QUEUE COMMIT MARKDOWN TABLE SINCE 2018-11-20 05:15:08.721118

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|10|djmitche|Merge pull request #303 from djmitche/bug1456909  Bug 1456909 - use monitor.oneShot()|[URL](https://github.com/taskcluster/taskcluster-queue/commit/9595f61cd17ad72c315e52d7d950026527ded5c6)|2018-11-26 22:05:11
|9|djmitche|Bug 1456909 - use monitor.oneShot()|[URL](https://github.com/taskcluster/taskcluster-queue/commit/0e7810781f5e64b1ef06a01f97abf85830e024c9)|2018-11-26 19:30:30
|8|djmitche|Bug 1508846 - upgrade tc-lib-api|[URL](https://github.com/taskcluster/taskcluster-queue/commit/5f259488c4ea8bd43a15fa4c5f1b660c2ce887da)|2018-11-21 21:35:58
|7|djmitche|Merge pull request #299 from djmitche/bug1508395  Bug 1508395 - upgrade tc-lib-validate|[URL](https://github.com/taskcluster/taskcluster-queue/commit/ee3bef79dc9bb2726dd8cea644ad3290da60d3d4)|2018-11-21 21:34:10
|6|djmitche|Merge branch 'master' into bug1508395|[URL](https://github.com/taskcluster/taskcluster-queue/commit/087cca55ada7a151518f018819b1a21f59df769d)|2018-11-21 21:34:04
|5|djmitche|Merge pull request #300 from djmitche/bug1505405  Bug 1505405 - upgrade tc-lib-pulse|[URL](https://github.com/taskcluster/taskcluster-queue/commit/6340fc2bafc194872799e59b55a37a7c54dd63b6)|2018-11-21 21:33:36
|4|djmitche|Bug 1505405 - upgrade tc-lib-pulse|[URL](https://github.com/taskcluster/taskcluster-queue/commit/17bf8649dabb96c849f2b875c82ad02fdf0d14ff)|2018-11-20 20:24:55
|3|djmitche|Merge pull request #301 from djmitche/bug1508849  Bug 1508849 - implement   -scope protection differently|[URL](https://github.com/taskcluster/taskcluster-queue/commit/bed26fb8855ee4c96174be3f9200cf4965f75a1d)|2018-11-21 21:32:11
|2|djmitche|Bug 1508849 - implement   -scope protection differently  The old solution used a negative lookbehind, which per https://json-schema.org/understanding-json-schema/reference/regular_expressions.html#regular-expressions is not supported in json-schema. In fact, it's not supported in even fairly recent versions of Node. This causes problems when validating schemas using those old versions of node (or using json-schema validators that do not support this form).  So, the new solution is to explicitly forbid those forms where used in creating clients and roles. The result is much the same, as evidenced by the minimal changes to the tests.|[URL](https://github.com/taskcluster/taskcluster-queue/commit/936be6b0b42002fbae57b69a6b4f7acabf82d8ac)|2018-11-21 00:55:08
|1|djmitche|Bug 1508395 - upgrade tc-lib-validate  This should only affect writeDocs|[URL](https://github.com/taskcluster/taskcluster-queue/commit/54344d0e797e7338f88dadca4627846648200c36)|2018-11-20 20:22:31


