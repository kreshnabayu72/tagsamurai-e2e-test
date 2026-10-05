---
name: Auth Login with Password
id: suite-auth-login-password
description: Test cases derived from tc-login-password.md for Auth > Login with Password
executionOrder: 1.0
parallel: false
---

# Suite: Auth Login with Password

Suite ini mencakup halaman Login with Password (pra-autentikasi) beserta layar kondisional
"Confirm to Continue" (Agreement Gate), CAPTCHA gate, lock progression, dan pencatatan dua surface.

`parallel: false` karena tiga hal:

- Spec 016 menguji rate limit per IP; request dari spec lain pada IP yang sama bisa ikut terpengaruh.
- Spec 011 mengubah status user di Global Settings > User, dan user yang dipakai spec lain bisa ikut berubah.
- Runner belum terbukti mengikuti nomor folder, sehingga spec yang mengubah data bersama tidak bisa diandalkan berjalan berurutan.

Setiap spec menjalankan seed data sendiri lewat hook, jadi tidak saling menumpang hasil. Spec 016, 017,
dan 020 adalah spec yang paling sensitif urutan dan sebaiknya dijalankan sendirian.