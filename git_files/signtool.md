## REPOSITORY NAME: SIGNTOOL
 CURRENT VERSION: 3.2.1 RELEASED ON MON, 27 AUG 2018 17:17:03 GMT

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|90|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|89|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|88|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|87|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|86|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|85|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|84|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|83|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|82|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|81|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
|80|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|79|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|78|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|77|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|76|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|75|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|74|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|73|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|72|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|71|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
|70|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|69|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|68|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|67|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|66|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|65|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|64|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|63|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|62|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|61|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
|60|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|59|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|58|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|57|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|56|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|55|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|54|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|53|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|52|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|51|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
|50|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|49|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|48|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|47|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|46|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|45|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|44|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|43|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|42|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|41|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
|40|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|39|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|38|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|37|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|36|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|35|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|34|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|33|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|32|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|31|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
|30|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|29|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|28|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|27|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|26|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|25|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|24|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|23|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|22|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|21|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
|20|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|19|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|18|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23
|17|escapewindow|Merge pull request #11 from escapewindow/py36  py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/8d9f095fbba19d11a22447c84cf99edd1f26f2fa)|2018-05-10 22:50:07
|16|escapewindow|py36 support|[URL](https://github.com/mozilla-releng/signtool/commit/d8db4153968d052a39793b302f85f9f02f3322a4)|2018-05-10 22:37:21
|15|JohanLorenzo|Use .gitignore file from other releng repos  This allows to ignore .pytest_cache/|[URL](https://github.com/mozilla-releng/signtool/commit/6960bc8bfa92ff7af467888591fd6fd7347716ff)|2018-04-27 16:22:15
|14|JohanLorenzo|Add tox tests against python 3.6 + split travis jobs per python version|[URL](https://github.com/mozilla-releng/signtool/commit/ad068f50e547931fd74f7149d184aafd41653d25)|2018-04-27 16:20:34
|13|JohanLorenzo|Fix errors reported by flake8 new rules|[URL](https://github.com/mozilla-releng/signtool/commit/6479506341029c2cdd9ba0f374d1d8ad7fffcbc1)|2018-04-27 16:17:27
|12|JohanLorenzo|3.2.0|[URL](https://github.com/mozilla-releng/signtool/commit/ab5cb83446d8eb3e5ccad7d69d336f0f238a78dc)|2018-04-24 12:31:29
|11|JohanLorenzo|Bug 1409091 - Add focus-jar support|[URL](https://github.com/mozilla-releng/signtool/commit/6398634cdb432e0cc1d43106aeb7d74a366409f1)|2018-04-24 10:24:14
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


