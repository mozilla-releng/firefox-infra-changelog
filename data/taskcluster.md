## taskcluster MD table
Generated on: 2019-06-15T12:13:14

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:-----:|:-----:|:----------------------------------:|:------:|:----:| 
|1|Dustin J. Mitchell|Merge pull request #871 from [Bug 1551607](https://bugzilla.mozilla.org/show_bug.cgi?id=1551607)  - use docker volumes for building|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/954996979a16766c72d4bc9aee90071afbb213dd)|2019-06-14 20:38:40
|2|Dustin J. Mitchell|Merge pull request #870 from djmitche/azure-encrenable encryption on azure resources|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/d96338e314bf941b25e4d4f1409fa3e9fd54c49c)|2019-06-14 20:37:11
|3|Dustin J. Mitchell|[Bug 1551607](https://bugzilla.mozilla.org/show_bug.cgi?id=1551607)  - remove debugging bits|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/97dfcb2155d87c169df86097415ca12d358c2c91)|2019-06-14 20:04:13
|4|Dustin J. Mitchell|[Bug 1551607](https://bugzilla.mozilla.org/show_bug.cgi?id=1551607)  - use docker volumes for buildingThis requires a good deal more manual copying back and forth, but meansthat the `yarn install` operations run entirely on a docker volume,rather than over a bind mount. Bind mounts don't work reliably onDocker for Mac, so this change allows `yarn build` to operate correcltyon such systems.|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/0b0fa21c22a2f5a76bf01f97dbcc816bd9e2f19a)|2019-06-14 18:50:45
|5|Dustin J. Mitchell|enable encryption on azure resources|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/8dd71c9000d355d16754c0d2690e1b828815b052)|2019-06-14 18:40:37
|6|Dustin J. Mitchell|Merge pull request #868 from djmitche/nocacheUse cmdOptions.cache|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/215cee37eb2dc7f27017937159dc6c68d4c101f1)|2019-06-13 20:30:32
|7|Dustin J. Mitchell|Use cmdOptions.cacheEither this never worked, or it worked once and `program` changed how itinterprets `--no-foo` options.|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/147238c4a7db02ba71b500f5e5c5026ebb276c6e)|2019-06-13 19:57:06
|8|Dustin J. Mitchell|Merge tag 'v14.1.0'|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/3a7969b72fed3274bbd844fa2cd0161691301bf3)|2019-06-13 19:35:12
|9|Dustin J. Mitchell|Merge pull request #857 from [Bug 1557487](https://bugzilla.mozilla.org/show_bug.cgi?id=1557487)  - fix /references/references.json, add docs|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/7c73b2502e6f6a0836cea8dd27584face8d3494c)|2019-06-13 15:13:43
|10|Brian Stack|More worker-manager coverage and fixes ( #866 )More worker-manager coverage and fixes|[URL](https://api.github.com/repos/taskcluster/taskcluster/commits/27575452a5dac2b71f066c658dd83f85a7834429)|2019-06-12 19:32:03
