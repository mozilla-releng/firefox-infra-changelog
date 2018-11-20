## COMM-ESR60 COMMIT MARKDOWN TABLE SINCE 2018-11-13 18:17:15.415335

| Commit Number | Commiter | Commit Message | Node | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|19|Jorg K <jorgk@jorgk.com>|No bug - Pin mozilla-esr60 version for release. a=jorgk|afa9e6f5d698d35b4c2e5da7bb711bfbccd6dd54|2018-08-16 00:36:04
|18|Jorg K <jorgk@jorgk.com>|Backed out changeset c597411fe241 for accidentally landing with DONTBUILD. a=jorgk|9a121656853775e6af93e34d9a476c7a84bf22da|2018-11-20 14:47:36
|17|Jorg K <jorgk@jorgk.com>|No bug - Empty commit. a=jorgk|39a6b979d966f7b98ac908e3b2d4eebffc550f24|2018-07-31 20:38:08
|16|Jorg K <jorgk@jorgk.com>|No bug - Pin mozilla-esr60 version for release. a=jorgk DONTBUILD|c597411fe2411e2bd76b21a64b1142fa0335e1e6|2018-08-16 00:36:04
|15|aceman <acelists@atlas.sk>|Bug 1481915 - Do not allow converting Local Folders to maildir if the needed pref isn't set. r=mkmelin a=jorgk|4f5354ecf23fd73446760ff46f58dec8e01fe7f8|2018-11-18 16:52:00
|14|Neil Rashbrook <neil@parkwaycc.co.uk>|Bug 1493143 - Allow copy service to find request by dstFolder for folder copy/move; change IMAP notify accordingly. r+a=jorgk|43b80ff56fa2d0cae801b8e14fed0980219f2605|2018-09-21 06:50:00
|13|Magnus Melin <mkmelin+mozilla@iki.fi>|Bug 1507718 - crash in nsImapProtocol::GetMessageSize(). Make m_hostSessionList an nsCOMPtr. r+a=jorgk|55f5634ac8652274f32a38ac4e4fabe6ac451895|2018-11-16 15:41:13
|12|Magnus Melin <mkmelin+mozilla@iki.fi>|Bug 1072748 - Switch Thunderbird from xpinstall.whitelist.add to using a default permissions file. r+a=jorgk  - port bug 506446 (use default_permissions file)  - port bug 1050080 (remove xpinstall.whitelist.add)  - port bug 1224000 - browser/omni.ja doesn't contain startup cache anymore and resource://app/ doesn't point where it's supposed to|d3b45f75c1dbec8907242485f4c0f42f166a1b28|2018-11-07 12:34:21
|11|MakeMyDay <makemyday@gmx-topmail.de>|Bug 1504753 - Change call cal.userCanRespondToInvitation to cal.acl.userCanRespondToInvitation. r+a=philipp|dc6b5da0d19e640c5f267fba283414c924951eff|2018-11-05 19:27:39
|10|Jorg K <jorgk@jorgk.com>|Bug 1333038 - Use 'modern' pointers to fix crash due to nsMsgLineStreamBuffer object being deleted while still in use. r=mkmelin a=jorgk Suspected "use after free" in nsMsgLineStreamBuffer::ReadNextLine() leading to crash since object may be destroyed while still in use on another thread.|53892f6ffc3a37e0f0c9a4290950f079a68f9425|2018-10-29 10:28:55
|9|Geoff Lankow <geoff@darktrojan.net>|Bug 1490626 - Add new notifications we need for WebExt address book API; r=mkmelin a=jorgk|73ed0515afc2a98dd34890ada1a80324c42daf0a|2018-09-27 03:01:04
|8|Geoff Lankow <geoff@darktrojan.net>|Bug 1482040 - Add UID property to address book interfaces; r=mkmelin a=jorgk|7fe1827e6b395377f9c72160e9d191104fc313ed|2018-09-26 02:56:46
|7|aceman <acelists@atlas.sk>|Bug 1508046 - return cleanly in LDAP autocomplete search if we are offline. r=mkmelin a=jorgk|75c22f453c771322ee486a7b20c1948b682c89cb|2018-11-17 06:41:00
|6|Jorg K <jorgk@jorgk.com>|Bug 1230815 - remove unused SetStripHtml() and accumulate HTML part to correct tag stripping, test. r=aceman a=jorgk|134d931f570884992722fc42f07e55da020f9c73|2018-10-23 11:10:49
|5|Jorg K <jorgk@jorgk.com>|Bug 1230815 - remove unused SetStripHtml() and accumulate HTML part to correct tag stripping. r=aceman a=jorgk|75d43dc40224380d1c07ffa4f3db3408c1a7ba75|2018-10-23 10:59:56
|4|Alfred Peters <infofrommozilla@gmail.com>|Bug 32216 - If the 'Date' header is invalid, use date from 'Received' header instead. r+a=jorgk|b02fba3200f5c14b88dcb672fc9fd4aa8c3b8083|2018-10-20 12:50:00
|3|Richard Marti <richard.marti@gmail.com>|Bug 1504088 - Stop overflowing the toolbars in main window. r+a=jorgk|35f977f9404bf89931e548d707f83ae0ed95bcfc|2018-11-04 13:50:40
|2|Jorg K <jorgk@jorgk.com>|Bug 1506800 - Don't sent AppleDouble for files with extension unless whitelisted. r=mkmelin a=jorgk|5ce5e6f8fc5132ee53f0c2bbe24e6eeb8f832590|2018-11-15 05:58:00
|1|Jorg K <jorgk@jorgk.com>|Bug 1506422 - Replace use of nsMsgI18NFileSystemCharset() with NS_CopyUnicodeToNative/NS_CopyNativeToUnicode(). r=emk a=jorgk|2a4a4a1fad3064ca32eb9343d2e278092d9d86a7|2018-11-10 19:35:00
|0|Mozilla Releng Treescript <release+treescript@mozilla.org>|Automatic version bump CLOSED TREE NO BUG a=release|5b876cd01e092325f0f51f0f7d9ff942be32ee2d|2018-11-15 04:44:57


