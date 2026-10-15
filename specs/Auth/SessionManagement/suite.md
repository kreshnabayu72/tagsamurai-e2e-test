---
name: Auth Session Management
id: suite-auth-session-management
description: Spec e2e turunan tc-session-management.md untuk Auth > Session Management
executionOrder: 4.0
parallel: false
---

# Suite: Auth Session Management

Suite ini mencakup dialog dan popup lifecycle sesi (Duplicate Login Attempt, Logged Out, Session Expired, Password Changed, Account no longer Active, Account Deactivated, Log Out, Access Restricted, Concurrent session limit reached, Subscription Not Active), limit login satu sesi aktif per platform, heartbeat dan idle timeout web dan mobile, App Access revoke, Delete Client, Client Suspended, delete dan deactivate akun, concurrent per produk berlisensi (seat dan sesi-produk), status subscription, admin force-logout, manual logout, Biometric Re-login di mobile, Change dan Reset Password yang meng-invalidate sesi lain, pencatatan log multi-surface, sinkron lintas modul, defense-in-depth, dan konkurensi.

`parallel: false` karena spec memakai state global (jam server, kuota seat per Client, status Client dan subscription, batas idle di General Settings, status user di Global Settings, sesi aktif per user). Setiap spec tetap menyiapkan datanya sendiri lewat hook dan tidak bergantung pada spec lain.

Kebijakan reCAPTCHA: login web lewat halaman Login with Password dilindungi reCAPTCHA (PRD Login with Password), sehingga setiap spec yang login lewat Browser menuliskan "reCAPTCHA mode uji di environment" di kemampuan teknis `## Prerequisites`. Login di aplikasi mobile tidak memakainya.
