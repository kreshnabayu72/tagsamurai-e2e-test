---
name: Auth Login with Password
id: suite-auth-login-password
description: Spec e2e turunan tc-login-password.md untuk Auth > Login with Password
executionOrder: 3.0
parallel: false
---

# Suite: Auth Login with Password

Suite ini mencakup halaman Login with Password (web dan mobile), validasi field Email dan Password, reCAPTCHA, evaluasi status akun, lock progression (15 menit, 1 jam, Requires Reset, Permanent) termasuk pergantian hari dan pemulihan lewat Reset Password, layar Confirm to Continue (Agreement), handoff MFA, navigasi ke Login with OTP dan Reset Password, pencatatan Activity Log Session dan User Log, sinkron dengan Global Settings > User, serta ketahanan terhadap kegagalan server, rate limit IP, dan konkurensi.

`parallel: false` karena spec lock progression, geser jam server, rate limit IP, dan perubahan General Settings atau status user di Global Settings memakai state global (counter per user, jam server, counter per IP, format tanggal). Setiap spec tetap menyiapkan datanya sendiri lewat hook dan tidak bergantung pada spec lain.
