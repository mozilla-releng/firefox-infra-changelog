## SCRIPT WORKER MARKDOWN TABLE

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|30|Mihai Tabara|Merge pull request #270 from MihaiTabara/docs  Bug 1503549 - improve docs for ramping up scriptworkers after aws-man…|[URL](https://github.com/mozilla-releng/scriptworker/commit/7ecf1958e98b1822e596651a62c1581bde8b7436)|2018-11-02 23:16:33 
|29|Mihai Tabara|Fix markdown syntax.|[URL](https://github.com/mozilla-releng/scriptworker/commit/b722dc37d9187e791e13dd4c190880f74034250d)|2018-11-02 23:03:24 
|28|Mihai Tabara|Fix flake8 issues.|[URL](https://github.com/mozilla-releng/scriptworker/commit/c63ffda1e5131ea82c157f117f01098e53b9ebf4)|2018-11-02 22:05:21 
|27|Mihai Tabara|Bug 1503549 - improve docs for ramping up scriptworkers after aws-manager2 retirement.|[URL](https://github.com/mozilla-releng/scriptworker/commit/34f792dc72185b3ea99c1c81a7d3337674779b84)|2018-11-02 21:52:28 
|26|Justin Wood (Callek)|Merge pull request #253 from Callek/1486970   Bug 1486970 - Need to pass push info to cron decision task validation|[URL](https://github.com/mozilla-releng/scriptworker/commit/2f38da7282620af08f08a1f63cd2cdcd4e72a4b9)|2018-10-19 19:51:57 
|25|Justin Wood|Bug 1486970 - Support actual push values for cron tasks, rather than stubs. r=aki|[URL](https://github.com/mozilla-releng/scriptworker/commit/5646e094d8f0b932f2f53709f2b387981f0b661b)|2018-09-06 19:45:53 
|24|Aki Sasaki|use ARG to allow for a 3.6 and 3.7 docker image from the same Dockerfile (#266)    use ARG to allow for a 3.6 and 3.7 docker image from the same Dockerfile      address review comments|[URL](https://github.com/mozilla-releng/scriptworker/commit/8dc1015249cb00b010a97633c194f5999102b434)|2018-10-19 19:13:55 
|23|Aki Sasaki|Merge pull request #267 from JohanLorenzo/bug-1486089-2  Bug 1486089 - part 2: Whitelist android-components and reference-browser repos|[URL](https://github.com/mozilla-releng/scriptworker/commit/e6257cd7db50c2c308221846f5eac7cc205a4ce1)|2018-10-15 16:06:45 
|22|Johan Lorenzo|16.2.1|[URL](https://github.com/mozilla-releng/scriptworker/commit/ffbf8c3d29d14ba1efc62ec53c81bd6adf3a963a)|2018-10-15 14:20:41 
|21|Johan Lorenzo|Bug 1486089 - part 2: Whitelist android-components and reference-browser repos|[URL](https://github.com/mozilla-releng/scriptworker/commit/f45ea14a383b55987f3bfa6562ecfa038f1ee728)|2018-10-15 14:17:26 
|20|Johan Lorenzo|16.2.0|[URL](https://github.com/mozilla-releng/scriptworker/commit/da3bfba2420bb2f523d78612319df097a16c0c2f)|2018-10-15 08:21:03 
|19|Johan Lorenzo|Bug 1486089 - Support "github-release" tasks_for and cron of mobile|[URL](https://github.com/mozilla-releng/scriptworker/commit/4834c85b4a614c8bc92794468b1708b58d21a480)|2018-10-12 16:24:27 
|18|Aki Sasaki|Merge pull request #265 from escapewindow/fix-verify-cot  fix verify_cot for taskcluster>=5.0.0|[URL](https://github.com/mozilla-releng/scriptworker/commit/d94ce80deabcc331378a7780fda20240f3ae2976)|2018-10-12 21:23:55 
|17|Aki Sasaki|fix verify_cot for taskcluster>=5.0.0  By populating `context.config` before `context.credentials`, we have a `taskcluster_root_url` defined for `context.queue`.|[URL](https://github.com/mozilla-releng/scriptworker/commit/ea1589ad36d4da5be424e43f4ec6652320e3abf2)|2018-10-12 18:10:30 
|16|Aki Sasaki|Merge pull request #263 from escapewindow/docker-fix  fix and refactor dockerfiles|[URL](https://github.com/mozilla-releng/scriptworker/commit/f682fe067b7f0fff8d00ba0a4150eab4ade3691e)|2018-10-12 17:54:14 
|15|Aki Sasaki|fix readme|[URL](https://github.com/mozilla-releng/scriptworker/commit/77d9261c64bc4bb876d131a68a648e9979714cbd)|2018-10-12 16:43:59 
|14|Aki Sasaki|fix and refactor dockerfiles  - update .dockerignore to avoid copying __pycache__ and  .pyc files - update README.rst - downgrade gnupg on the python docker images to 2.0.26-6+deb8u2 - rename /data to /builds - move scriptworker from /builds/. to /builds/scriptworker to keep   things cleaner and avoid lint/pytest warnings+errors for   non-scriptworker code (e.g. puppet) - consolidate the .test and .gnupg dockerfiles, get all tests passing in   the docker container - add a py37 version. This only differs from the py36 version in the   FROM line; we may want to either templatize these for less duplication   or allow for multiple versions of python on a single image.|[URL](https://github.com/mozilla-releng/scriptworker/commit/f45ea983b3a0ea77fd24edafbc9cfc8120faa14e)|2018-10-09 18:21:32 
|13|Aki Sasaki|Merge pull request #262 from escapewindow/rootUrl  add rootUrl support for taskcluster>=5.0.0|[URL](https://github.com/mozilla-releng/scriptworker/commit/b09074dcd114254505b8c77e767b6c850c9fce3b)|2018-10-10 19:18:38 
|12|Aki Sasaki|16.1.0|[URL](https://github.com/mozilla-releng/scriptworker/commit/e5931430922b72f3071abe40925a7dd21a34c0bf)|2018-10-10 17:21:21 
|11|Aki Sasaki|raw strings to cut down on pytest warnings|[URL](https://github.com/mozilla-releng/scriptworker/commit/88175945b11839ee1c0f7dc2a2ad92a05cfa23b2)|2018-10-09 22:25:42 
|10|Aki Sasaki|log.warn -> log.warning|[URL](https://github.com/mozilla-releng/scriptworker/commit/0a22fa95cab915b27040bde9378a34c19ad29669)|2018-10-09 22:13:17 
|9|Aki Sasaki|pass rootUrl to taskcluster-client|[URL](https://github.com/mozilla-releng/scriptworker/commit/52b0c50469b1dfec4bf14c7d0589fee59540d545)|2018-10-09 22:11:04 
|8|Tom Prince|Merge pull request #259 from tp-tc/rel-pro-action-cb  Handle hook and task actions via callback name.|[URL](https://github.com/mozilla-releng/scriptworker/commit/d7ac2ee55e7fb537b939090358692ebd2131b725)|2018-09-14 22:21:24 
|7|Tom Prince|16.0.1|[URL](https://github.com/mozilla-releng/scriptworker/commit/9fb7424475b481e91196080f497d2c2421e38d58)|2018-09-14 21:52:11 
|6|Tom Prince|Handle hook and task actions via callback name.|[URL](https://github.com/mozilla-releng/scriptworker/commit/5b7ef69265f95639582e737af6d138ed1e8e9029)|2018-09-13 17:16:58 
|5|Aki Sasaki|Merge pull request #258 from escapewindow/multiple-retrigger  use `cb_name` instead of `name` to identify actions in actions.json|[URL](https://github.com/mozilla-releng/scriptworker/commit/4089b88d763f75850ad4b9039de048c4e4c5a7c2)|2018-09-12 19:20:39 
|4|Aki Sasaki|16.0.0|[URL](https://github.com/mozilla-releng/scriptworker/commit/5329e3110e723096675a7317faabbef9f9a54d58)|2018-09-12 18:54:54 
|3|Aki Sasaki|100 % coverage|[URL](https://github.com/mozilla-releng/scriptworker/commit/e97e358fc4fa50be47fbd9ce6a09911c7c5534d9)|2018-09-12 18:49:15 
|2|Aki Sasaki|address review comment: get_action_name -> get_action_callback_name  This is a breaking change.|[URL](https://github.com/mozilla-releng/scriptworker/commit/9fff06dcb4ccbb1d9d29396a62c7888d5cc17345)|2018-09-12 18:38:49 
|1|Aki Sasaki|fix unit tests|[URL](https://github.com/mozilla-releng/scriptworker/commit/d9edb100449871c6bc451c4288580730e9d60b45)|2018-09-12 18:37:00 


