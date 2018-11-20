## TRY COMMIT MARKDOWN TABLE SINCE 2018-11-14 01:20:27.639344

| Commit Number | Commiter | Commit Message | Node | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|19|Brian Grinstead <bgrinstead@mozilla.com>|try: -b do -p win64,linux64,macosx64 -u mochitests,xpcshell -t none --artifact  Pushed via `mach try syntax`|f140c7785f5fc8575a613f5de3d142b7fac92a46|2018-11-21 01:15:37
|18|Brian Grinstead <bgrinstead@mozilla.com>|Bug 1508446 - Require that [accesskey] gets set on <xul:label> to enable formatting;r=paolo  Previously, if the accesskey attribute was missing then the label would reach up to binding parent to find it's accesskey. In practice, bindings already do [xbl:inherits=accesskey] to send it down to the label anyway.  The problem with this is that for controls without accesskeys, the attribute doesn't get set, so the label will access the control from JS. This is fine for XBL, since typically the label XBL will construct at the same time as the control, but when migrating to Custom Elements, the label gets connected even when the control is hidden.  Differential Revision: https://phabricator.services.mozilla.com/D12355|78b17ebbd4b223c57c549b34fa1ff22fea26d8bc|2018-11-20 01:13:38
|17|Wes Kocher <wkocher@mozilla.com>|Fuzzy query=web-platform-tests  Pushed via `mach try fuzzy`|5ecf21069d41386935c48272b061e1fae92939ad|2018-11-21 01:14:35
|16|Wes Kocher <wkocher@mozilla.com>|Update all jobs from try push|7dc70d45d1e9277611592827b45610e614b87251|2018-11-21 01:00:11
|15|Blake Kaplan <mrbkap@gmail.com>|Fuzzy query='linux 'debug '-sw | 'mochitest  Pushed via `mach try fuzzy`|7311a3bd1a42b313f38e5d1f27e601bdc9a69c26|2018-11-21 01:13:50
|14|Blake Kaplan <mrbkap@gmail.com>|Fuzzy query='linux64 'debug '-sw | 'mochitest  Pushed via `mach try fuzzy`|c07174a9142377d52a0b1abf832081b0c0f666cf|2018-11-21 01:12:53
|13|Blake Kaplan <mrbkap@gmail.com>|Bug 1508595 - Only set an intercept controller when needed. r=asuth  We only need to expose an intercept controller in SharedWorkers if we're on the non-parent-intercept version of ServiceWorkers or if e10s is off. nsDocShell already does this dance and we have to mirror it.|59dcebc7bdc2ff6118fc0a23fdc1a46cfc944c65|2018-11-21 01:10:40
|12|Logan Smyth <loganfsmyth@gmail.com>|try: -b o -p win64 -u mochitest-e10s-dt -t none --artifact  Pushed via `mach try syntax`|2ae283bf44185fa1e611c7d6a0f65e263f177af8|2018-11-21 01:10:23
|11|Logan Smyth <loganfsmyth@gmail.com>|remove all logs|998fe7ec61f2f92b7f027bf37183f9766e316869|2018-11-21 01:09:56
|10|Logan Smyth <loganfsmyth@gmail.com>|remove all logs|89b91d0424976ce0649c74da0a9804e3d369b470|2018-11-21 00:51:09
|9|Logan Smyth <loganfsmyth@gmail.com>|WIP: Add logging for expected failure mode|bd14a62eafefff90e27e0e14f91ec2ee0cea8bc9|2018-11-20 02:42:28
|8|Steve Fink <sfink@mozilla.com>|try: -b do -p linux64-shell-haz --upload-xdbs  Pushed via `mach try syntax`|8f65796b1ce1c952cfca06a8d5d831bb5f3f94c8|2018-11-21 01:07:37
|7|Tom Prince <mozilla@hocat.ca>|Fuzzy query=linux64/debug  Pushed via `mach try fuzzy`|e21728ba93a0a8ca08fef341a167faafbed2d893|2018-11-21 01:07:54
|6|Tom Prince <mozilla@hocat.ca>|Bug 1508836: Don't try to guess MOZ_UPDATE_CHANNEL in automation;  Differential Revision: https://phabricator.services.mozilla.com/D12487|16491e62124228fa1d1597f578a090043f2730aa|2018-11-21 01:05:55
|5|Jeff Muizelaar <jrmuizel@gmail.com>|try: -b do -p macosx64,win64,linux64,linux64-base-toolchains,linux -u all[linux64-qr,windows10-64-qr,macosx64-qr] -t none  Pushed via `mach try syntax` |1d4bb870ef5631e50bd0c229766be68bb27c0b7b|2018-11-21 01:03:30
|4|Jeff Muizelaar <jrmuizel@gmail.com>|remove mEventRegions |a9f5eb8439305a92740e73d0c63161a7ffdfd7e5|2018-11-21 01:01:22
|3|Kartikaya Gupta <kgupta@mozilla.com>|try: -b do -p android-api-16,win64,macosx64,linux64,linux64-base-toolchains,linux -u all[linux64-qr,windows10-64-qr,macosx64-qr] -t all[linux64-qr,windows10-64-qr,macosx64-qr]  Pushed via `mach try syntax`|d4394b7d135c7d0189f098fef245455a35c4f009|2018-11-21 01:01:03
|2|Kartikaya Gupta <kgupta@mozilla.com>|placeholder for try push  MozReview-Commit-ID: LKDk2deY2x7|d33ce8ce9a459bd270403fd251a4ec9a31fc745c|2018-11-21 01:00:58
|1|Kartikaya Gupta <kgupta@mozilla.com>|Placeholder  MozReview-Commit-ID: LhRD1MOzjK|dbf905ce85711be64a145b22fefa4e995464298a|2018-11-21 01:00:29
|0|WR Updater Bot <graphics-team@mozilla.staktrace.com>|Bug 1508766 - Update webrender to commit 229436b578701fc74a009d6cedc6b2a3ae313f77 (WR PR #3331). r?kats|887b23bb872f9058bf5a669eed0b043d22b38709|2018-11-21 01:00:27


