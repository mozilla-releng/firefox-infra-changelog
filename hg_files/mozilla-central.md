## MOZILLA-CENTRAL COMMIT MARKDOWN TABLE SINCE 2018-11-12 18:10:25.778321

| Commit Number | Commiter | Commit Message | Node | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|19|Margareta Eliza Balazs <ebalazs@mozilla.com>|Merge inbound to mozilla-central.  a=merge|e44bb5b4bc79be613d29b3f95d7b508e68e3d128|2018-11-19 11:28:37
|18|sotaro <sotaro.ikeda.g@gmail.com>|Bug 1508117 - Fix mAsyncImageManager->AddPipeline() calls in WebRenderBridgeParent::UpdateWebRender() r=mattwoodrow|20c99b0e8e4ecd54197b7d785f94eb60cfbc42e0|2018-11-19 05:15:55
|17|Jan de Mooij <jdemooij@mozilla.com>|Bug 1507721 - Simplify AutoEnterOOMUnsafeRegion by adding an explicit inUnsafeRegion_ flag to the OOM simulator. r=jonco  Differential Revision: https://phabricator.services.mozilla.com/D12103|7987651658f0c2cdf836eef25ba91ee52e965ec1|2018-11-16 12:23:11
|16|Mike Hommey <mh+mozilla@glandium.org>|Bug 1502457 - Derive the default update channel from the application display version. r=nalexander  Depends on D11986  Differential Revision: https://phabricator.services.mozilla.com/D11987|88ba9f723934257d34fde00d87b5ed4f54e258ca|2018-11-16 03:16:59
|15|Mike Hommey <mh+mozilla@glandium.org>|Bug 1502457 - Move MOZILLA_OFFICIAL to init.configure. r=nalexander  Depends on D11985  Differential Revision: https://phabricator.services.mozilla.com/D11986|83e6f0d47a8050ab1dc796dc0c795eac2f8cda4c|2018-11-16 03:16:31
|14|Mike Hommey <mh+mozilla@glandium.org>|Bug 1502457 - Move js_option around to make it available earlier. r=nalexander  Depends on D11984  Differential Revision: https://phabricator.services.mozilla.com/D11985|fd205107b0f4beac469995f809b7c77d6bddde0a|2018-11-16 03:15:58
|13|Mike Hommey <mh+mozilla@glandium.org>|Bug 1502457 - Move MOZ_APP_VERSION{,_DISPLAY} to python configure. r=nalexander  Depends on D11983  Differential Revision: https://phabricator.services.mozilla.com/D11984|f28ea3184e5ca7be89bfa62802af63c5dfe8f7e8|2018-11-16 03:15:35
|12|Mike Hommey <mh+mozilla@glandium.org>|Bug 1502457 - Move FIREFOX_VERSION to python configure. r=nalexander  Depends on D11982  Differential Revision: https://phabricator.services.mozilla.com/D11983|c62948fc14e698a9a987b8d8ec229d3f464bedb1|2018-11-16 03:14:46
|11|Mike Hommey <mh+mozilla@glandium.org>|Bug 1502457 - Use MOZ_APP_VERSION instead of FIREFOX_VERSION. r=nalexander  Differential Revision: https://phabricator.services.mozilla.com/D11982|70e906a17ad36aaa3aee981daf0a4a6654ab7789|2018-11-16 03:14:07
|10|WR Updater Bot <graphics-team@mozilla.staktrace.com>|Bug 1507938 - Update webrender to commit 199ace786ef5d80982a8c811dabfab13593e6ae6 (WR PR #3321). r=kats  Differential Revision: https://phabricator.services.mozilla.com/D12227|9ca8941c235755271b4510909931b28f807b804f|2018-11-19 00:37:30
|9|Ted Campbell <tcampbell@mozilla.com>|Bug 1508160 - Add JS_BEGIN_MACRO to .clang-format r=sylvestre  Differential Revision: https://phabricator.services.mozilla.com/D12226|eb04ab1f698a06f6f9eb58b212dab59d5e1828cd|2018-11-18 21:54:59
|8|Jared Wein <jwein@mozilla.com>|Bug 1504277 - Open new tabs at the end of a multiselection of tabs if the New Tab button is ctrl-clicked. r=dao  Differential Revision: https://phabricator.services.mozilla.com/D11376|b42ccd72214c31ff454a56436321cecc6cc8416a|2018-11-19 00:26:52
|7|Tim Nguyen <ntim.bugs@gmail.com>|Bug 1468517 - Make toolbar_bottom_separator color apply to findbar top border. r=dao  Differential Revision: https://phabricator.services.mozilla.com/D11577|7e9cac76980a2a4a10898c721c4a054db831ab4a|2018-11-18 20:16:52
|6|Brindusan Cristian <cbrindusan@mozilla.com>|Merge inbound to mozilla-central. a=merge|b3ceae83e290925f754544cff4d30ef4de9ab399|2018-11-18 13:06:19
|5|Neil Deakin <neil@mozilla.com>|Bug 1502704, overlay scrollbars don't fade out properly as no QI to nsStyledElement is available r=peterv|2b13a09333e79d452555cff461b645e214639b4b|2018-10-29 07:00:00
|4|Cristina Coroiu <ccoroiu@mozilla.com>|Bug 1383454 - Disable box-sizing-replaced-003.xht on mac for frequent failures. r=jmaher|d32110a492f5eece3697fd039d53dba247f9f202|2018-11-17 14:25:00
|3|Coroiu Cristina <ccoroiu@mozilla.com>|Merge mozilla-central to inbound a=merge|572f525f1afe920d092830673f843066425d4494|2018-11-17 23:43:13
|2|Brian Hackett <bhackett1024@gmail.com>|Bug 1507359 Part 3 - Control pausing and resuming in ReplayDebugger, r=lsmyth.|3a3c453432c15dfcedcb294f2da580506d6de5e7|2018-11-17 19:59:33
|1|Brian Hackett <bhackett1024@gmail.com>|Bug 1507359 Part 2 - Bindings and internal changes to allow ReplayDebugger to control child pausing/resuming, r=mccr8.|1c7fc8389e012c987347efefca6b35f3948b742a|2018-11-15 04:09:58
|0|Brian Hackett <bhackett1024@gmail.com>|Bug 1507359 Part 1 - Change breakpoint state to be a set of positions, r=mccr8.|70a8eb10c67f46134779b3106f74f4353ea37f7a|2018-11-15 03:56:49


