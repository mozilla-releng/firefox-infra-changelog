## SIGNTOOL COMMIT MARKDOWN TABLE SINCE 2018-11-12 18:10:25.778321

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|30|Aki Sasaki|Merge pull request #12 from escapewindow/retry-connectionerror  Retry for ConnectionError during upload.|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/5710c473fc04ff0a7b7b850ba237b9c5df3d1e83)|2018-08-27 17:31:58 
|29|Aki Sasaki|3.2.1|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03 
|28|Aki Sasaki|switch to python 3.7 release; try to fix coveralls|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10 
|27|Aki Sasaki|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23 
|26|Aki Sasaki|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07 
|25|Aki Sasaki|py36 support|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21 
|24|Johan Lorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15 
|23|Johan Lorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34 
|22|Johan Lorenzo|Fix errors reported by flake8 new rules|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27 
|21|Johan Lorenzo|3.2.0|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29 
|20|Johan Lorenzo|Bug 1409091 - Add focus-jar support|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14 
|19|Aki Sasaki|Merge pull request #9 from escapewindow/fix-sig  stop munging dest now that `output_file` is working|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/530ee27052e6459c93004de3bcdfbd844bf49bf0)|2017-08-16 03:27:35 
|18|Aki Sasaki|3.1.6|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/73788cf63acb877b42f69e27af6929e663c1b4a9)|2017-08-16 03:15:19 
|17|Aki Sasaki|moar coverage|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/e64dde73e76983536859bea273d0424d1df84112)|2017-08-16 03:25:34 
|16|Aki Sasaki|stop munging path since we have output_file working|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/1611142bce2f38e780e65f099a412903855651e4)|2017-08-16 03:14:30 
|15|Aki Sasaki|Merge pull request #8 from escapewindow/fix-output-file  actually use options.output_file|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/93c000fd34f7d96a46b9cda01e4a86ab9e531794)|2017-08-16 01:05:31 
|14|Aki Sasaki|3.1.5|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/83d33550f9fa373b0bd0cc1ec68632ec0bd43543)|2017-08-16 00:53:09 
|13|Aki Sasaki|actually use options.output_file|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/b99660a8b65a123d14af53bb8392f8689d3d23db)|2017-08-16 00:40:05 
|12|Aki Sasaki|Merge pull request #7 from escapewindow/cdm  bug 1383769 - support widevine in signtool py3|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/a9d12fed1809343c507761631cbce11539d0021a)|2017-08-04 21:47:12 
|11|Aki Sasaki|3.1.4|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/b8fdcc3da82eaaa432214f0dee56a693ea232432)|2017-08-04 18:56:24 
|10|Aki Sasaki|kill py33 support|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/32da51fa7a07a813fd68731185548dac79ace2d9)|2017-08-03 00:26:18 
|9|Aki Sasaki|get an initial noop test of remote_signfile, for coverage|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/9d026978da6be8137d58b9de0f661ba41ab14bbd)|2017-08-03 00:23:11 
|8|Aki Sasaki|support widevine|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/ed07ee82153e65021f9d5ac1259ce09651f45ceb)|2017-07-31 21:01:00 
|7|Aki Sasaki|update changelog for 3.1.3|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/b59a62f7ceae4f6216405302ef38a9a79994966d)|2017-07-13 20:48:29 
|6|Aki Sasaki|Merge pull request #4 from catlee/master  Reimplement signature check without pefile|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/44c59472964752eecae73f50aaf2201458989bc5)|2017-07-13 20:07:34 
|5|Chris AtLee|Merge branch 'master' of https://github.com/mozilla-releng/signtool|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/bd4bd50c765b385fb637a3b29581e6e7568ea7e7)|2017-07-13 19:35:22 
|4|Johan Lorenzo|3.1.2|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/99c8f406ed2f3c930495da6194102b827fdec024)|2017-07-13 16:19:49 
|3|Aki Sasaki|Merge pull request #5 from JohanLorenzo/add-more-formats  Bug 1380536 - update py3 signtool with sha384 mar + sha2signcodestub|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/e822a17c677ffcb6ff302ff0d18b0a29ab41045d)|2017-07-13 16:13:29 
|2|Johan Lorenzo|3.1.1|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/c3fd69f690484080389bcdf8880a175f9db66a2c)|2017-07-13 16:01:30 
|1|Johan Lorenzo|Bug 1380536 - update py3 signtool with sha384 mar + sha2signcodestub|[URL](https://api.github.com/repos/mozilla-releng/signtool/commits/4a98b04ffec0aa597111b2967e33f277be18569c)|2017-07-13 13:13:21 


