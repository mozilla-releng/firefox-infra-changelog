## COMM-ESR60 COMMIT MARKDOWN TABLE SINCE 2018-11-20 05:12:27.198934

| Commit Number | Commiter | Commit Message | Node | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|19|Jorg K <jorgk@jorgk.com>|No bug - Pin mozilla-esr60 version for release. a=jorgk|607e7138912852c182fd42d9e0f3c87ea3b8eeb3|2018-08-16 00:36:04
|18|Richard Marti <richard.marti@gmail.com>|Bug 1508611 - Set orient="vertical" on splitter in filter editor to show it immediately. r+a=jorgk|f2bea6614d22d3efdd2274ab7d63d62c18c2590f|2018-11-25 14:15:02
|17|Magnus Melin <mkmelin+mozilla@iki.fi>|Bug 1271353 - check own email addresses case-insensitively in correspondents column and ignore plus addressing part. r+a=jorgk|949fc4394c9f2a940139ed16aa214c9d5337e6b6|2018-11-21 10:40:25
|16|Jorg K <jorgk@jorgk.com>|Bug 1401858 - add null check to avoid crash in EncodedHeader()/DecodedHeader(). r=mkmelin a=jorgk|879f355b920c29492bf3867c7406df174d26f08b|2018-11-26 00:28:26
|15|Hiroyuki Ikezoe <hiikezoe@mozilla-japan.org>|Bug 409458 - nsIMsgFolder.AddFolderListener should hold a reference to the listener. r=standard8,neil,darktrojan,jorgk a=jorgk|e3a599bf7d540a475f30b807ed6711bce1f16cfb|2018-08-30 06:42:58
|14|Neil Rashbrook <neil@parkwaycc.co.uk>|Bug 1482040 - Fix failure in test_uid.js by iterating MailServices.ab.directories 'manually'. r=darktrojan a=jorgk DONTBUILD|a6e340fe4c07d16d962abab48404aad0d07848b8|2018-11-20 08:29:00
|13|Jorg K <jorgk@jorgk.com>|No bug - Pin mozilla-esr60 version for release. a=jorgk|afa9e6f5d698d35b4c2e5da7bb711bfbccd6dd54|2018-08-16 00:36:04
|12|Jorg K <jorgk@jorgk.com>|Backed out changeset c597411fe241 for accidentally landing with DONTBUILD. a=jorgk|9a121656853775e6af93e34d9a476c7a84bf22da|2018-11-20 14:47:36
|11|Jorg K <jorgk@jorgk.com>|No bug - Empty commit. a=jorgk|39a6b979d966f7b98ac908e3b2d4eebffc550f24|2018-07-31 20:38:08
|10|Jorg K <jorgk@jorgk.com>|No bug - Pin mozilla-esr60 version for release. a=jorgk DONTBUILD|c597411fe2411e2bd76b21a64b1142fa0335e1e6|2018-08-16 00:36:04
|9|aceman <acelists@atlas.sk>|Bug 1481915 - Do not allow converting Local Folders to maildir if the needed pref isn't set. r=mkmelin a=jorgk|4f5354ecf23fd73446760ff46f58dec8e01fe7f8|2018-11-18 16:52:00
|8|Neil Rashbrook <neil@parkwaycc.co.uk>|Bug 1493143 - Allow copy service to find request by dstFolder for folder copy/move; change IMAP notify accordingly. r+a=jorgk|43b80ff56fa2d0cae801b8e14fed0980219f2605|2018-09-21 06:50:00
|7|Magnus Melin <mkmelin+mozilla@iki.fi>|Bug 1507718 - crash in nsImapProtocol::GetMessageSize(). Make m_hostSessionList an nsCOMPtr. r+a=jorgk|55f5634ac8652274f32a38ac4e4fabe6ac451895|2018-11-16 15:41:13
|6|Magnus Melin <mkmelin+mozilla@iki.fi>|Bug 1072748 - Switch Thunderbird from xpinstall.whitelist.add to using a default permissions file. r+a=jorgk  - port bug 506446 (use default_permissions file)  - port bug 1050080 (remove xpinstall.whitelist.add)  - port bug 1224000 - browser/omni.ja doesn't contain startup cache anymore and resource://app/ doesn't point where it's supposed to|d3b45f75c1dbec8907242485f4c0f42f166a1b28|2018-11-07 12:34:21
|5|MakeMyDay <makemyday@gmx-topmail.de>|Bug 1504753 - Change call cal.userCanRespondToInvitation to cal.acl.userCanRespondToInvitation. r+a=philipp|dc6b5da0d19e640c5f267fba283414c924951eff|2018-11-05 19:27:39
|4|Jorg K <jorgk@jorgk.com>|Bug 1333038 - Use 'modern' pointers to fix crash due to nsMsgLineStreamBuffer object being deleted while still in use. r=mkmelin a=jorgk Suspected "use after free" in nsMsgLineStreamBuffer::ReadNextLine() leading to crash since object may be destroyed while still in use on another thread.|53892f6ffc3a37e0f0c9a4290950f079a68f9425|2018-10-29 10:28:55
|3|Geoff Lankow <geoff@darktrojan.net>|Bug 1490626 - Add new notifications we need for WebExt address book API; r=mkmelin a=jorgk|73ed0515afc2a98dd34890ada1a80324c42daf0a|2018-09-27 03:01:04
|2|Geoff Lankow <geoff@darktrojan.net>|Bug 1482040 - Add UID property to address book interfaces; r=mkmelin a=jorgk|7fe1827e6b395377f9c72160e9d191104fc313ed|2018-09-26 02:56:46
|1|aceman <acelists@atlas.sk>|Bug 1508046 - return cleanly in LDAP autocomplete search if we are offline. r=mkmelin a=jorgk|75c22f453c771322ee486a7b20c1948b682c89cb|2018-11-17 06:41:00
|0|Jorg K <jorgk@jorgk.com>|Bug 1230815 - remove unused SetStripHtml() and accumulate HTML part to correct tag stripping, test. r=aceman a=jorgk|134d931f570884992722fc42f07e55da020f9c73|2018-10-23 11:10:49


