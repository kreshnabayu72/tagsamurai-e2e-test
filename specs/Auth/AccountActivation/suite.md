---
name: Auth Account Activation
id: suite-auth-account-activation
description: Spec e2e turunan tc-account-activation.md untuk Auth > Account Activation
executionOrder: 1.0
parallel: false
---

# Suite: Auth Account Activation

Suite ini mencakup validasi link aktivasi, form Set Password, aktivasi akun, halaman Activation Success dan Invalid Link, Resend Activation Email, masa berlaku token, zero logging, dan ketahanan terhadap kegagalan server.

`parallel: false` karena token aktivasi sekali pakai, dan spec Resend, time-travel, rate limit, serta zero logging mengubah atau membaca state global. Setiap spec tetap menyiapkan datanya sendiri lewat hook dan tidak bergantung pada spec lain.
