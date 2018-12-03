## SIGNTOOL COMMIT MARKDOWN TABLE SINCE 2018-11-26 06:26:50.747249

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|10|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|9|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|8|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|7|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|6|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|5|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|4|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|3|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|2|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|1|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14


