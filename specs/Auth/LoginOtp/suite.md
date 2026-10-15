---
name: Auth Login with OTP
id: suite-auth-login-otp
description: Spec e2e turunan tc-login-otp.md untuk Auth > Login with OTP
executionOrder: 2.0
parallel: false
---

# Suite: Auth Login with OTP

Suite ini mencakup halaman Request OTP dan Verify OTP (web dan mobile), validasi email dan reCAPTCHA, pengiriman email OTP, kotak 6 digit dengan auto-submit, siklus Resend (countdown 60 detik, kuota 5 kali, cooldown 10 menit), sesi email-request, Edit email, layar Confirm to Continue, handoff MFA, pencatatan log, sinkron status user Global Settings, plan gating, serta ketahanan terhadap kegagalan server, rate limit, dan konkurensi.

`parallel: false` karena spec rate limit IP, kuota Resend, geser jam server, dan perubahan status user di Global Settings memakai state global (counter per IP atau per email, jam server, status user). Setiap spec tetap menyiapkan datanya sendiri lewat hook dan tidak bergantung pada spec lain.
