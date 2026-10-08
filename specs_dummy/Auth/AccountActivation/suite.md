---
name: Auth Account Activation
id: suite-auth-account-activation
description: Test cases derived from tc-account-activation.md for Auth > Account Activation
executionOrder: 1.0
parallel: false
---

# Suite: Auth Account Activation

Suite ini mencakup alur Account Activation (aktivasi akun oleh user baru via link email) secara penuh: trigger pengiriman Activation Email saat pembuatan user, validasi link aktivasi di berbagai state token (valid/expired/consumed/superseded/malformed), halaman Set Password dengan Password Policy dan real-time checklist, konsumsi token dan aktivasi akun (termasuk concurrency/race condition), halaman Activation Success, halaman 404 untuk link invalid, invalidasi token oleh Resend Activation Email, non-logging verification lintas aksi, responsive & accessibility, serta plan gating.

`parallel: false` karena beberapa alasan berikut:

- Spec sensitif terhadap state token dan user (status Pending Activation/Activated). Aktivasi/consume token bersifat one-time dan perubahan status user bisa mempengaruhi spec lain yang memakai user yang sama.
- Spec yang melibatkan Resend Activation Email (E2E-008) membuat token baru dan meng-invalidasi token lama; timing resend dan konsumsi token bisa saling mempengaruhi jika dijalankan paralel.
- Concurrency/race condition diuji di E2E-005 (double-submit, retry timeout, race antar tab, resend mid-fill); menjalankannya paralel dengan spec lain berisiko membuat state tidak terprediksi.
- Verifikasi non-logging (E2E-009) memerlukan pembacaan surface log (Activity Log, User Log, System Log, Changelog) dan perbandingan count entri sebelum/sesudah; untuk menjaga isolasi dan konsistensi penghitungan, dijalankan tidak paralel.
- Beberapa skenario butuh setup data terisolasi per spec melalui hook; meski tiap spec membuat datanya sendiri, state global (token, user status) tetap lebih aman dijalankan berurutan dalam suite ini.

Setiap spec menjalankan seed data sendiri lewat hook, jadi tidak saling menumpang hasil. Spec yang melibatkan concurrency, resend, dan perubahan status user bersifat sensitif urutan dan sebaiknya dijalankan sendirian jika diperlukan debugging terpisah.
