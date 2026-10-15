---
name: Auth Account Activation
id: suite-auth-account-activation
description: Test cases derived from tc-account-activation.md for Auth > Account Activation
executionOrder: 1.0
parallel: false
---

# Suite: Auth Account Activation

Suite ini mencakup alur Account Activation (aktivasi akun oleh user baru lewat link Activation Email) secara penuh, diturunkan dari `tc-account-activation.md` canonical 2026-10-07 dengan 134 TC (`TC-AUTH-ACT-01` sampai `TC-AUTH-ACT-134`):

1. Screening halaman Set Password dan akses berbasis token (link dibuka tanpa sesi, dengan sesi login aktif milik user lain, dibuka dua kali) — E2E-001.
2. Validasi link saat memuat: full-page loading, server error 5xx, timeout, rate limit 429, dan pemulihan lewat [Try Again] — E2E-002 (mock).
3. Trigger Activation Email dari Global Settings > User beserta template email, snapshot nama, dan klik link/button email — E2E-003.
4. Trigger Activation Email dari Admin Console lewat pembuatan Client + Default User — E2E-004.
5. Kegagalan pengiriman email yang tidak membatalkan user dan pemulihan lewat Resend — E2E-005.
6. Password Policy dan checklist real-time, toggle show/hide, boundary panjang 72 karakter, serta karakter khusus — E2E-006 s.d. E2E-008.
7. Validasi saat submit yang diblokir di client (field kosong, mismatch, policy belum terpenuhi) beserta ketiadaan CAPTCHA — E2E-009 dan E2E-010.
8. Guard halaman (tanpa dialog Unsaved Changes) dan accessibility halaman Set Password — E2E-011.
9. Alur sukses submit: loading, double-click guard, password boundary, lalu halaman Activation Success dan Go to Login — E2E-012 dan E2E-014.
10. Kegagalan server saat Set Password (5xx, timeout, 429) beserta retry — E2E-013 (mock).
11. Halaman Invalid Link (404) beserta seluruh variannya dan masa berlaku token — E2E-015 dan E2E-016.
12. Blokir berbasis kondisi data target: user dihapus, toggle Active OFF, kondisi entity Client, dan plan — E2E-017, E2E-018, E2E-023.
13. Zero-logging pada seluruh aksi Auth dan refleksi lintas modul (gate Login, status Activated di Global Settings) — E2E-019 dan E2E-020.
14. Resend Activation Email: invalidasi token lama dari Global Settings > User, dari Admin Console, dan Bulk Resend — E2E-021 dan E2E-022.
15. Security & defense-in-depth: token milik user lain, payload injeksi, penegakan server terhadap password/confirm, serta tampilan respons 422/400 — E2E-024 s.d. E2E-026.
16. Concurrency dan perubahan state saat form terbuka: race dua tab, Resend/expired saat form terbuka, status user berubah, serta token tidak dikenal — E2E-027 dan E2E-028.

`parallel: false` karena alasan berikut:

- Konsumsi token bersifat one-time dan status user berpindah dari Pending Activation ke Activated; spec yang mengaktifkan akun (E2E-012, E2E-014, E2E-019, E2E-020) memakai user seeding sendiri tetapi state global token tetap lebih aman dijalankan berurutan.
- Resend Activation Email (E2E-005, E2E-021, E2E-022) membuat token baru dan meng-invalidasi token lama; timing resend terhadap spec lain yang memakai user sama saling mempengaruhi.
- E2E-017 dan E2E-028 menghapus/mengubah user di tengah alur, sehingga harus berjalan sendirian agar kegagalannya tidak menutupi spec lain.
- E2E-019 membandingkan jumlah entri pada empat surface log (Activity Log, User Log, System Log, Changelog) sebelum dan sesudah aksi; eksekusi paralel mencemari penghitungan.
- E2E-027 dan E2E-028 menguji race multi-tab dan perubahan state saat form terbuka; isolasi sesi dan token diperlukan agar hasilnya deterministik.

Setiap spec menyiapkan data ujinya sendiri lewat hook dan fixture, sehingga dapat dieksekusi secara independen tanpa menumpang hasil spec lain.
