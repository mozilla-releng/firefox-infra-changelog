## SIGNTOOL COMMIT MARKDOWN TABLE SINCE 2018-11-25 06:59:30.452334

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|4|escapewindow|Merge pull request #12 from escapewindow/retry-connectionerror  Retry for ConnectionError during upload.|[URL](https://github.com/mozilla-releng/signtool/commit/5710c473fc04ff0a7b7b850ba237b9c5df3d1e83)|2018-08-27 17:31:58
|3|escapewindow|3.2.1|[URL](https://github.com/mozilla-releng/signtool/commit/62debcab19529af096cb7298c9557e8914cae589)|2018-08-27 17:17:03
|2|escapewindow|switch to python 3.7 release; try to fix coveralls|[URL](https://github.com/mozilla-releng/signtool/commit/85d4d8ff6c2ec91a4b3f7a00d754d30228b12ece)|2018-08-25 01:41:10
|1|escapewindow|Retry for ConnectionError during upload.  The remote_signfile function is pretty ugly and should be rewritten. However, I believe we were failing to retry because we're in the except block of the outer try/except, and the inner try/except didn't catch ConnectionError. RequestException should catch both HTTPError and ConnecitonError.  Fixes https://github.com/mozilla-releng/signingscript/issues/66 .|[URL](https://github.com/mozilla-releng/signtool/commit/18c2cf87aaea71208ece3fe575bd466b674b3981)|2018-08-25 00:50:23


