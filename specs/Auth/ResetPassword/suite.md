---
name: Auth Reset Password
id: suite-auth-reset-password
description: Test cases derived from tc-reset-password.md for Auth > Reset Password
executionOrder: 1.0
parallel: false
---

# Suite: Auth Reset Password

Suite ini mencakup alur Reset Password (Forgot Password) secara penuh: halaman permintaan reset,
gate reCAPTCHA dan status akun, pengiriman email beserta resend dan cooldown, rate limit serta
anti-enumeration, validasi link reset, halaman Setup New Password dengan Password Policy,
konsumsi token dan reset lock progression, halaman 404 untuk link invalid, halaman sukses,
pencatatan dua surface, concurrency, aksesibilitas, dan gating plan.

`parallel: false` karena lima hal:

- Spec 012 dan 013 memakai rate limit per email dan per IP; request dari spec lain pada email atau
  IP yang sama bisa ikut terpengaruh.
- Spec 004, 020, dan 021 mengubah status user, tahap lock, dan counter akun di Global Settings > User,
  sehingga user yang dipakai spec lain bisa ikut berubah.
- Spec 011 dan 013 bergantung pada cooldown 60 detik yang bersifat server-side dan tidak bisa
  dipercepat dari sisi runner.
- Spec 006, 011, 012, dan 014 memakai mailbox uji yang sama; isi kotak masuk tidak bisa diantar
  antar spec secara paralel.
- Runner belum terbukti mengikuti nomor folder, sehingga spec yang mengubah data bersama tidak bisa
  diandalkan berjalan berurutan.

Setiap spec menjalankan seed data sendiri lewat hook, jadi tidak saling menumpang hasil. Spec 012,
013, dan 020 adalah spec yang paling sensitif urutan dan sebaiknya dijalankan sendirian.