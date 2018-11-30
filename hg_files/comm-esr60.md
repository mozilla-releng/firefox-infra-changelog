## COMM-ESR60 COMMIT MARKDOWN TABLE SINCE 2018-11-22 01:43:30.355108

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|20|Jorg K |Bug 1510472 - Add null check to avoid crash due to nsDependentCString(null). r=mkmelin a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=0ba73c30a3d9)|2018-11-28 09:14:26
|19|Jorg K |Bug 1510028 - Add null check to avoid crash due to nsDependentCString(null). r=mkmelin a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=4f5ec4473e22)|2018-11-27 22:10:19
|18|Jorg K |Bug 1509685 - Add more bounds checking in nsMsgDBView::UpdateDisplayMessage() to avoid crashes. r=alta88 a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=189364307b2e)|2018-11-27 20:11:03
|17|Jorg K |Bug 1470049 - Partially revert rev 40f5ba35583 (bug 1385573) to fix insertion into threaded unified/search view. a=backout|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=9c373f4cbef7)|2018-11-28 09:06:46
|16|aceman |Bug 1509586 - Look for requireEncryptMessage in params.smFields in msgCompSecurityInfo.js. r=mkmelin a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=cc3a5040f78d)|2018-11-25 10:55:00
|15|Jorg K |Bug 1510035 - Set orient="vertical" on splitter on search and AB search. r=Paenglab a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=6f6c836a215c)|2018-11-26 22:47:22
|14|Jorg K |Bug 409458 - fix backport error: mailServices.js vs. MailServices.jsm. rs=bustage-fix a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=ef701c1534bf)|2018-11-27 10:10:14
|13|Jorg K |No bug - Pin mozilla-esr60 version for release. a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=607e71389128)|2018-08-15 21:36:04
|12|Richard Marti |Bug 1508611 - Set orient="vertical" on splitter in filter editor to show it immediately. r+a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=f2bea6614d22)|2018-11-25 12:15:02
|11|Magnus Melin |Bug 1271353 - check own email addresses case-insensitively in correspondents column and ignore plus addressing part. r+a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=949fc4394c9f)|2018-11-21 08:40:25
|10|Jorg K |Bug 1401858 - add null check to avoid crash in EncodedHeader()/DecodedHeader(). r=mkmelin a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=879f355b920c)|2018-11-25 22:28:26
|9|Hiroyuki Ikezoe |Bug 409458 - nsIMsgFolder.AddFolderListener should hold a reference to the listener. r=standard8,neil,darktrojan,jorgk a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=e3a599bf7d54)|2018-08-30 03:42:58
|8|Neil Rashbrook |Bug 1482040 - Fix failure in test_uid.js by iterating MailServices.ab.directories 'manually'. r=darktrojan a=jorgk DONTBUILD|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=a6e340fe4c07)|2018-11-20 06:29:00
|7|Jorg K |No bug - Pin mozilla-esr60 version for release. a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=afa9e6f5d698)|2018-08-15 21:36:04
|6|Jorg K |Backed out changeset c597411fe241 for accidentally landing with DONTBUILD. a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=9a1216568537)|2018-11-20 12:47:36
|5|Jorg K |No bug - Empty commit. a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=39a6b979d966)|2018-07-31 17:38:08
|4|Jorg K |No bug - Pin mozilla-esr60 version for release. a=jorgk DONTBUILD|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=c597411fe241)|2018-08-15 21:36:04
|3|aceman |Bug 1481915 - Do not allow converting Local Folders to maildir if the needed pref isn't set. r=mkmelin a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=4f5354ecf23f)|2018-11-18 14:52:00
|2|Neil Rashbrook |Bug 1493143 - Allow copy service to find request by dstFolder for folder copy/move; change IMAP notify accordingly. r+a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=43b80ff56fa2)|2018-09-21 03:50:00
|1|Magnus Melin |Bug 1507718 - crash in nsImapProtocol::GetMessageSize(). Make m_hostSessionList an nsCOMPtr. r+a=jorgk|[URL](https://hg.mozilla.org/releases/comm-esr60/pushloghtml?changeset=55f5634ac865)|2018-11-16 13:41:13


