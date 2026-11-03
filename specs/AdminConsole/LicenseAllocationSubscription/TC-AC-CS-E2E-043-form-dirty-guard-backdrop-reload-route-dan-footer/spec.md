---
id: TC-AC-CS-E2E-043-form-dirty-guard-backdrop-reload-route-dan-footer
title: "Form: Dirty Guard Backdrop, Reload, Route, dan Footer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-168
  - TC-AC-CS-169
  - TC-AC-CS-170
  - TC-AC-CS-635
coverage:
  web: automated
---

# Form: Dirty Guard Backdrop, Reload, Route, dan Footer

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite). Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman.
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): menangani dialog `beforeunload` bawaan browser (menerima atau membatalkan reload, S-08).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-043` (padanan Pre-setup #48: tanpa term dan tanpa trial) dan Client `Warung Kopi Senja+{runId}-043` dengan satu term Active FAMS plan Professional, Start Date 01/09/25, End Date 31/08/26, Plan Owner PT Maju Bersama, tanpa successor dan tanpa trial aktif (padanan Pre-setup #69) untuk form Renew; Client `Klinik Harapan Bunda+{runId}-043` dengan trial SAMS Growth Active 10/08/26 sampai 08/09/26, Plan Owner CV Karya Mandiri, tanpa term paid SAMS (padanan Pre-setup #71) untuk form Convert. State yang dirugikan oleh Submit Renew pada TC-AC-CS-635 (term successor Pending) dihapus di hook `after`.

## Test Steps

### TC-AC-CS-168: Klik backdrop tidak menutup form walau dirty

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription+{runId}-043`
3. Klik area gelap di luar modal
4. Verifikasi modal tetap terbuka dengan input dipertahankan
5. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-CS-169: Reload saat form dirty memunculkan konfirmasi bawaan browser

6. Tekan `F5`
7. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul saat form dirty
8. Batalkan reload pada konfirmasi bawaan browser
9. Klik `[Clear Field]`, lalu klik `[✕]` pada header modal
10. Klik `[+ Subscription]` tanpa mengisi apa pun, lalu tekan `F5`
11. Verifikasi reload langsung berjalan tanpa konfirmasi pada form bersih

### TC-AC-CS-170: Pindah route di dalam aplikasi saat form dirty memunculkan dialog Unsaved Changes

12. Klik `[+ Subscription]`, lalu pilih Client `Client Tanpa Subscription+{runId}-043`
13. Klik menu `Device Allocation` di sidebar
14. Verifikasi dialog Unsaved Changes muncul dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
15. Klik `[Cancel]`
16. Verifikasi navigasi dibatalkan dan tetap di form
17. Klik menu `Device Allocation` di sidebar, lalu klik `[Leave]`
18. Verifikasi navigasi dilanjutkan dan form ditutup

### TC-AC-CS-635: Footer varian Renew dan Convert tanpa checkbox Stay on this form dan Submit sukses menutup modal

19. Buka Allocation > Client Subscription dari sidebar, ketik Search `Warung Kopi Senja+{runId}-043`, tekan Enter
20. Klik ikon `⋯` pada baris term Active, lalu pilih `Renew`
21. Verifikasi footer modal Renew hanya memuat `[Clear Field]` dan `[Submit]` rata kanan, dan checkbox "Stay on this form after submitting" tidak dirender
22. Pilih Renewal Option `Keep current plan`, isi Duration `1`, lalu klik `[Submit]`
23. Verifikasi modal Renew tertutup setelah Submit
24. Verifikasi toast sukses "Success, your renewal has been scheduled and will take effect on 01/09/26." muncul
25. Klik `(←)` pada kotak Search, lalu ketik Search `Klinik Harapan Bunda+{runId}-043`, tekan Enter
26. Klik ikon `⋯` pada baris trial, lalu pilih `Convert`
27. Verifikasi footer modal Convert hanya memuat `[Clear Field]` dan `[Submit]` rata kanan, dan checkbox "Stay on this form after submitting" tidak dirender
28. Klik `[✕]` pada header modal, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): `[Clear Field]` dan `[✕]` pada langkah 9 (S-08 untuk form dirty di langkah 6 sampai 8 dilakukan lewat pembatalan reload lalu Clear Field sehingga `[✕]` tanpa dialog), pindah halaman lewat sidebar (langkah 19), Search untuk menemukan baris target (R-16; langkah 19, 25), `(←)` pada kotak Search (langkah 25, 28), dan `[✕]` pada form Convert bersih (langkah 28).
- Reload pada langkah 6 dan 10 memakai kemampuan penanganan `beforeunload` yang tertulis di Prerequisites (S-08).
- Temuan untuk QA:
  - TC-AC-CS-169 Langkah 4 ("Ulangi pada form bersih") tidak menyebut cara menutup form dirty sebelum mengulang; spec memakai Clear Field lalu `[✕]` (form kembali clean).
  - TC-AC-CS-635 Langkah 4 menyebut menutup modal Convert lewat `[✕]` tanpa Expected tambahan; tidak ada Verifikasi selain footer.
