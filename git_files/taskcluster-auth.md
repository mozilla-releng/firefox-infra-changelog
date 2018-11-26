## TASKCLUSTER-AUTH COMMIT MARKDOWN TABLE SINCE 2018-11-19 05:15:53.601441

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|7|djmitche|Bug 1508846 - upgrade tc-lib-api|[URL](https://github.com/taskcluster/taskcluster-auth/commit/ee8964bac335b073f41210c3968e7f12a5ec5341)|2018-11-21 20:12:20
|6|djmitche|Merge pull request #181 from djmitche/bug1505405  Bug 1505405 - upgrade tc-lib-pulse|[URL](https://github.com/taskcluster/taskcluster-auth/commit/d0bc2154649c75406ff56757d126127289ee4e01)|2018-11-21 20:32:22
|5|djmitche|Bug 1505405 - upgrade tc-lib-pulse  This only affects the output references format (for RFC 128)|[URL](https://github.com/taskcluster/taskcluster-auth/commit/33052858d025cf67f128dff7fd55231c323c95b1)|2018-11-20 19:13:43
|4|djmitche|Merge pull request #180 from djmitche/bug1508395  Bug 1508395 - upgrade tc-lib-validate|[URL](https://github.com/taskcluster/taskcluster-auth/commit/9ed089f62916fa2a54967379cfb5bc35156b8cea)|2018-11-21 19:48:44
|3|djmitche|Merge pull request #182 from djmitche/bug1508849  Bug 1508849 - implement   -scope protection differently|[URL](https://github.com/taskcluster/taskcluster-auth/commit/052d624ea730559489f6984b8fb47b819e2ffe94)|2018-11-21 19:48:33
|2|djmitche|Bug 1508849 - implement   -scope protection differently  The old solution used a negative lookbehind, which per https://json-schema.org/understanding-json-schema/reference/regular_expressions.html#regular-expressions is not supported in json-schema.  In fact, it's not supported in even fairly recent versions of Node.  This causes problems when validating schemas using those old versions of node (or using json-schema validators that do not support this form).  So, the new solution is to explicitly forbid those forms where used in creating clients and roles.  The result is much the same, as evidenced by the minimal changes to the tests.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/b19103d6d2ac47d16e2086a283e04320651ff383)|2018-11-21 00:46:14
|1|djmitche|Bug 1508395 - upgrade tc-lib-validate  The change ony affects the output of writeDocs.|[URL](https://github.com/taskcluster/taskcluster-auth/commit/e52d89a68dc312b5ca045558ff7d4011663312db)|2018-11-20 19:10:53


