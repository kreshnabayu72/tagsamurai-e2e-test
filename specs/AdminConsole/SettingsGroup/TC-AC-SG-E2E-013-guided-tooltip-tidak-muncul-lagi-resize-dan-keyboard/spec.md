---
id: TC-AC-SG-E2E-013-guided-tooltip-tidak-muncul-lagi-resize-dan-keyboard
title: "Guided Tooltip Settings > Group: Tidak Muncul Lagi Setelah Selesai, Resize Menutup Tanpa Seen, dan Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-49
  - TC-AC-SG-50
  - TC-AC-SG-51
coverage:
  web: automated
---

# Guided Tooltip Settings > Group: Tidak Muncul Lagi Setelah Selesai, Resize Menutup Tanpa Seen, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Pengecualian atas hook suite: spec ini menguji Guided Tooltip sehingga mengatur flag `guided_tooltip_seen_ac-settings-group` sendiri sesudah hook (flag disetel belum `seen` sebelum tiap blok TC dan dipulihkan oleh hook `after` suite).
- Kemampuan teknis: Fixture BE untuk membaca dan menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` pada akun aktor; disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: lebar jendela browser (TC-AC-SG-50, 1100px); dipulihkan ke 1440px pada langkah 15 dan di hook `after`.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-013`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global selain flag Guided Tooltip akun aktor yang dipulihkan hook suite.

## Test Steps

### TC-AC-SG-49: Walkthrough tidak muncul lagi setelah selesai pada kunjungan berikutnya

1. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
2. Muat ulang halaman Settings > Group dengan F5
3. Klik `[Next]` tiga kali sampai Step 4
4. Klik `[Done]`
5. Buka ulang halaman `Settings > Group` dengan F5
6. Verifikasi Breadcrumb "Settings > Group" tampil
7. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya
8. Verifikasi flag Guided Tooltip `seen` tersimpan pada akun

### TC-AC-SG-50: Resize atau navigasi menutup walkthrough tanpa menandai seen

9. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
10. Muat ulang halaman Settings > Group dengan F5
11. Verifikasi walkthrough tampil pada Step 1
12. Ubah lebar jendela browser menjadi 1100px saat walkthrough berjalan
13. Verifikasi walkthrough tertutup saat resize
14. Verifikasi flag Guided Tooltip belum `seen` untuk akun aktor
15. Pulihkan lebar jendela browser menjadi 1440px
16. Buka ulang halaman `Settings > Group` dengan F5
17. Verifikasi walkthrough muncul lagi dari awal (Step 1)
18. Klik `[Skip]` untuk menutup walkthrough

### TC-AC-SG-51: Keyboard pada Guided Tooltip: Enter, panah kiri, dan Esc

19. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
20. Muat ulang halaman Settings > Group dengan F5
21. Tekan Enter
22. Verifikasi Enter memajukan walkthrough ke Step 2
23. Tekan panah kiri
24. Verifikasi panah kiri mengembalikan walkthrough ke Step 1
25. Tekan Esc
26. Verifikasi Esc menutup walkthrough (setara Skip)

## Notes

- Langkah penghubung (S-03, S-09): langkah 1, 9, dan 19 (menyetel flag sebelum tiap blok), langkah 3 dan 4 (menyelesaikan walkthrough sebagai aksi TC), langkah 15 (memulihkan viewport), langkah 18 (menutup walkthrough sebelum blok berikutnya).
- Langkah 11 memverifikasi walkthrough berjalan sebagai anchor positif sebelum absence "tertutup saat resize" (langkah 13, bagian 8b butir 2); TC-AC-SG-50 tidak menyebutnya sebagai Expected.
- Temuan untuk QA:
  - TC-AC-SG-50 langkah 2 tidak menyebut ukuran jendela baru; spec memakai 1100px (di bawah 1280px). Judul TC juga menyebut "navigasi", sedangkan langkah dan Expected hanya memuat resize; navigasi tidak diasersi.
  - TC-AC-SG-49 menyebut "(flag seen tersimpan pada akun)" tanpa langkah observasi; spec membacanya lewat Fixture BE (kemampuan disediakan tim FE/BE, langkah 8 dan 14).
