---
id: TC-FA-PREF-E2E-010-guided-tooltip-back-done-skip-dan-replay
title: "Guided Tooltip Preferences: [Back], [Done], [Skip], dan Replay Lewat [?]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-56
  - TC-FA-PREF-57
  - TC-FA-PREF-58
  - TC-FA-PREF-59
coverage:
  web: automated
---

# Guided Tooltip Preferences: [Back], [Done], [Skip], dan Replay Lewat [?]

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1, keadaan PA-20 tanpa flag `guided_tooltip_seen_fa-accounting-preferences` pada awal tiap kunjungan pertama) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Pengecualian hook suite untuk Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-accounting-preferences` true; spec ini mengatur flag itu sendiri menjadi belum tersimpan pada langkah 1, 10, dan 21 (kemampuan menyetel dan membaca flag disediakan tim FE/BE). Hook `after` memulihkan flag ke nilai awal hook suite.
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Data Uji TC: page_key `fa-accounting-preferences`.
- Suite berjalan serial (`parallel: false`); spec ini mengubah flag Guided Tooltip akun aktor dan memulihkannya di hook `after`.

## Test Steps

### TC-FA-PREF-56: [Back] pada Step 2 kembali ke Step 1

1. Setel flag `guided_tooltip_seen_fa-accounting-preferences` akun aktor menjadi belum tersimpan
2. Pindah ke halaman aplikasi lain di luar Settings > Accounting
3. Buka Settings > Accounting > Preferences untuk pertama kali
4. Klik `[Next]` pada Step 1
5. Klik `[Back]` pada Step 2
6. Verifikasi tooltip kembali menampilkan indikator "Step 1 of 4"
7. Verifikasi tooltip menampilkan judul "Accounting Year"
8. Verifikasi `[Back]` tidak tampil pada Step 1
9. Klik `[Skip]` untuk menutup walkthrough

### TC-FA-PREF-57: [Done] pada Step 4 menutup walkthrough

10. Setel flag `guided_tooltip_seen_fa-accounting-preferences` akun aktor menjadi belum tersimpan
11. Pindah ke halaman aplikasi lain di luar Settings > Accounting
12. Buka Settings > Accounting > Preferences untuk pertama kali
13. Klik `[Next]` pada Step 1
14. Klik `[Next]` pada Step 2
15. Klik `[Next]` pada Step 3
16. Klik `[Done]` pada Step 4
17. Verifikasi overlay dan tooltip box tertutup
18. Muat ulang halaman dengan F5
19. Verifikasi Breadcrumb "Settings > Accounting > Preferences" tampil
20. Verifikasi Guided Tooltip tidak muncul otomatis

### TC-FA-PREF-58: [Skip] menutup walkthrough

21. Setel flag `guided_tooltip_seen_fa-accounting-preferences` akun aktor menjadi belum tersimpan
22. Pindah ke halaman aplikasi lain di luar Settings > Accounting
23. Buka Settings > Accounting > Preferences untuk pertama kali
24. Klik `[Skip]` pada Step 1
25. Verifikasi overlay dan tooltip box tertutup
26. Muat ulang halaman dengan F5
27. Verifikasi Breadcrumb "Settings > Accounting > Preferences" tampil
28. Verifikasi Guided Tooltip tidak muncul otomatis

### TC-FA-PREF-59: Replay lewat [?]

29. Klik tombol `[?]` di sebelah kanan Breadcrumb
30. Verifikasi walkthrough mulai dari Step 1 dengan judul "Accounting Year"
31. Verifikasi flag seen tetap tersimpan (tidak di-reset)
32. Klik `[Skip]` untuk menutup walkthrough

## Notes

- Langkah penghubung (S-03): langkah 1 sampai 3, 10 sampai 12, dan 21 sampai 23 (membentuk kunjungan pertama; hook `beforeEach` suite sudah membuka halaman Preferences sehingga spec pindah ke halaman lain lalu membukanya kembali), serta langkah 9 dan 32 (menutup walkthrough). Langkah 19 dan 27 (Breadcrumb tampil) menjadi anchor positif untuk asersi absence sesudah muat ulang (8b butir 2, R-21).
- Urutan TC dalam spec: TC-FA-PREF-56, 57, 58, 59. TC-FA-PREF-59 berprecondition flag seen sudah tersimpan; keadaan itu dibentuk oleh `[Skip]` pada langkah 24 (TC-FA-PREF-58). Spec tidak bergantung pada spec lain.
- Langkah 31 membaca flag lewat kemampuan baca flag yang disediakan tim FE/BE untuk Expected TC-FA-PREF-59 butir b ("Flag seen tidak di-reset"), tanpa endpoint karangan (S-13).
- Temuan untuk QA:
  - TC-FA-PREF-57 dan 58 menulis Post Condition "flag seen tersimpan untuk akun ini" tanpa langkah observasi flag; Post Condition itu tidak diasersi terpisah dan diamati secara tidak langsung lewat Guided Tooltip tidak muncul sesudah muat ulang (langkah 20 dan 28).
  - TC-FA-PREF-59 Expected b ("Flag seen tidak di-reset") tidak memiliki langkah observasi di TC; spec membacanya lewat kemampuan baca flag (langkah 31).
