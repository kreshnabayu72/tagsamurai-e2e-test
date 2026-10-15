---
name: Auth MFA
id: suite-auth-mfa
description: Spec e2e turunan tc-mfa.md untuk Auth > MFA (Multi-Factor Authentication)
executionOrder: 3.5
parallel: false
---

# Suite: Auth MFA

Suite ini mencakup evaluasi kapan MFA wajib (login pertama, idle 30 hari, device baru, lokasi lebih dari 100 km, negara berbeda dan pasangan negara trusted), halaman Choose Verification Method, OTP Verification, Authenticator Verification dan Enrollment Authenticator, batas percobaan salah dan TTL sesi pre-auth, trust device, email alert login tak biasa, pencatatan log, sinkronisasi lintas modul, plan gating, defense-in-depth, konkurensi, ketahanan terhadap kegagalan server, rate limit, serta MFA di aplikasi mobile.

`parallel: false` karena spec memakai state global (jam server, jam browser dan jam authenticator uji, IP uji dan lokasi koneksi, geo-IP, email service alert, counter rate limit IP, versi Privacy Policy terbitan, status user dan Client di Global Settings). Setiap spec tetap menyiapkan datanya sendiri lewat hook dan tidak bergantung pada spec lain.
