## MOZILLA-CENTRAL COMMIT MARKDOWN TABLE SINCE 2018-12-14 07:07:48.898232

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|20|arthur.iakab |Merge inbound to mozilla-central a=merge|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=a77e8f3efc4c)|2018-12-27 21:56:49
|19|Cosmin Sabou |Bug 1433892 - Disable browser_ext_menus_events.js on Linux for frequent failures. r=jmaher|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=96499feeb5bf)|2018-12-26 15:39:00
|18|Lee Salzman |Bug 1516334 - don't draw emoji as paths when they are too big. r=rhunt|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ee0e1df960c4)|2018-12-27 18:30:27
|17|Nicolas B. Pierron |Bug 1515963 - Add vixl::GdbDisassembleInstruction. r=sstangl  This add a simple function made to be called from gdb, which uses the vixl decoder to output in a static buffer the string corresponding to a single instruction.  This is useful when breaking at vixl::Simulator::ExecuteInstruction function, as follow:  (gdb) b vixl::Simulator::ExecuteInstruction Breakpoint 1 at 0x...: file ../jit/arm64/vixl/MozSimulator-vixl.cpp. (gdb) command 1 > call vixl::GdbDisassembleInstruction(this->pc_) > end |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3487b5f2f426)|2018-12-21 16:50:47
|16|Nicolas B. Pierron |Bug 1515704 - ARM64: Generate code for LPowHalfD. r=sstangl |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=89834b056ca0)|2018-12-20 17:53:41
|15|longsonr |Bug 1516076 - Part 4 - make include order more sensible for some files r=dholbert|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=21ce5e3998e3)|2018-12-27 17:30:38
|14|Jason Laster |Bug 1515951 - Update Debugger Frontend v112. r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=49233ec55bff)|2018-12-27 04:44:52
|13|Jason Laster |Bug 1515951 - [release 112] Breakpoint svg changed (#7586). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=8ded394acd81)|2018-12-23 19:46:54
|12|Jason Laster |Bug 1515951 - [release 112] Enable Syntax Highlighting for ClojureScript (#7584). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ea2807921cc3)|2018-12-23 19:46:40
|11|Jason Laster |Bug 1515951 - [release 112] Blackbox original sources (#7370). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=10dc48aa3b1e)|2018-12-23 19:46:23
|10|Jason Laster |Bug 1515951 - [release 112] Fixes flow typing support for reselect (#7573). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=5bfef0866541)|2018-12-23 19:46:07
|9|Jason Laster |Bug 1515951 - [release 112] 7190: Save generated file and source map (#7482). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=796402f4fa52)|2018-12-23 19:45:49
|8|Jason Laster |Bug 1515951 - [release 112] Use CSS animation for the SearchInput loader. (#7565). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=4ca33ee89eb8)|2018-12-23 19:45:03
|7|Jason Laster |Bug 1515951 - [release 112] [search] fix file img icon background on focus (#7558) (#7564). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=05ce3a72db78)|2018-12-23 19:44:50
|6|Jason Laster |Bug 1515951 - [release 112] Option to not auto expand a node if it has a lot of children (#7510). r=bhackett |[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=48aa3ee2c926)|2018-12-23 19:44:35
|5|longsonr |Bug 1516194 - fix identation in SMILNullType.cpp r=dholbert|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=006f69326ccc)|2018-12-27 17:12:48
|4|longsonr |Bug 1516521 - rename nsSMILCSSValueType as SMILCSSValueType and move it to the mozilla namespace r=dholbert|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=ca4a5a7852d6)|2018-12-27 17:02:38
|3|Paolo Amadini |Bug 1516442 - Move "listheader" outside of "richlistbox". r=bgrins  The only uses of "listheader" are part of in-content preferences, and they are updated to use adjacent elements. This is in preparation for the removal of the inner scrollbox in the "richlistbox" binding.  Differential Revision: https://phabricator.services.mozilla.com/D15387|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=7e0448a4aa48)|2018-12-26 17:00:31
|2|longsonr |Bug 1516194 - rename nsSMILNullType to SMILNullType and move it to the mozilla namespace r=dholbert|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=3a5eb424e655)|2018-12-27 10:21:40
|1|sotaro |Bug 1493497 - Clear EGLSurfaceOverride correctly in SharedSurface_ANGLEShareHandle r=jgilbert|[URL](https://hg.mozilla.org/mozilla-central/pushloghtml?changeset=41d9d168940d)|2018-12-27 08:00:59


