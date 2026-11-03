---
id: TC-AC-DC-E2E-035-add-unsaved-reload-dan-navigasi
title: "Add Subcategory: Reload Halaman dan Navigasi Internal dengan Input Berisi Perubahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-74
  - TC-AC-DC-75
  - TC-AC-DC-76
  - TC-AC-DC-77
coverage:
  web: automated
---

# Add Subcategory: Reload Halaman dan Navigasi Internal dengan Input Berisi Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-035`): `Induk {runId}-035` (leaf di bawah `Handheld Reader`). Node hasil Add spec (`Pemindai Meja {runId}-035`) ikut terhapus saat hook `after` menghapus `Induk {runId}-035` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Draft Name` (tidak pernah disimpan sehingga tidak bersuffix).
- Kemampuan teknis: dialog `beforeunload` bawaan browser dapat ditangani oleh skrip (diterima untuk melanjutkan reload atau dibatalkan untuk tetap di halaman) dan kemampuan itu disediakan tim FE. Item menu navigasi lain pada sidebar aplikasi (TC-76 dan TC-77) tidak disebut TC; tujuannya dipilih tim FE (lihat Temuan untuk QA). Jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `Draft Name`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline
5. Klik `[×]` pada modal Changelog

### Reload saat input berisi perubahan (TC-74)

6. Hover node `Induk {runId}-035`, klik aksi `+ Subcategory`
7. Ketik `Draft Name`, tekan F5
8. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul sebelum halaman dimuat ulang
9. Pilih tetap di halaman pada konfirmasi browser
10. Verifikasi input inline Add tetap terbuka dengan nilai `Draft Name`
11. Klik `[Clear Field]`, tekan Esc

### Reload saat input bersih atau setelah submit sukses (TC-75)

12. Hover node `Induk {runId}-035`, klik aksi `+ Subcategory`
13. Tekan F5 tanpa mengetik apa pun
14. Verifikasi konfirmasi bawaan browser tidak muncul
15. Expand `Hardware` lalu `Handheld Reader`
16. Hover node `Induk {runId}-035`, klik aksi `+ Subcategory`
17. Ketik `Pemindai Meja {runId}-035`, klik `[Submit]`
18. Verifikasi toast sukses "Success, category has been created."
19. Tekan F5
20. Verifikasi konfirmasi bawaan browser tidak muncul

### Navigasi internal: Cancel membatalkan navigasi (TC-76)

21. Expand `Hardware` lalu `Handheld Reader`
22. Hover node `Induk {runId}-035`, klik aksi `+ Subcategory`
23. Ketik `Draft Name`, klik item menu navigasi lain di sidebar aplikasi
24. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
25. Klik `[Cancel]`
26. Verifikasi pengguna tetap di Settings > Device > Device Name
27. Verifikasi input inline Add terbuka dengan nilai `Draft Name`

### Navigasi internal: Leave melanjutkan navigasi (TC-77)

28. Klik item menu navigasi lain di sidebar aplikasi yang sama
29. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
30. Klik `[Leave]`
31. Verifikasi navigasi berlanjut ke halaman tujuan

### Pemeriksaan akhir tidak ada node dan tidak ada entri baru

32. Buka Settings > Device > Device Name, lalu expand `Hardware` dan `Handheld Reader`
33. Verifikasi node `Draft Name` tidak ada di bawah `Induk {runId}-035` (anchor: node `Pemindai Meja {runId}-035` tampil)
34. Klik ikon Changelog pada header Sidebar Category
35. Ketik Search `Draft Name`, tekan Enter
36. Verifikasi jumlah baris hasil Search sama dengan baseline
37. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1, 15, 21 (membuka cabang tree; langkah 15 dan 21 setelah halaman dimuat ulang), langkah 5 dan 37 (menutup modal Changelog), langkah 11 (memulihkan input yang dirty ke keadaan bersih lalu menutupnya tanpa dialog), langkah 32 (kembali ke halaman Device Name setelah navigasi).
- Spec ini melewati sekitar 35 langkah (37) karena TC-75 dan pemeriksaan akhir. Seluruh blok satu topik (Unsaved Changes pada input Add, reload dan navigasi) memakai satu halaman dan satu induk, dan pemeriksaan akhir mengonsolidasikan tiga asersi "tidak ada node dan tidak ada entri log" menjadi satu pembacaan sehingga tidak diulang per TC.
- S-05: klausa "node `Draft Name` tidak dibuat dan tidak ada entri log" pada TC-77 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 33, 36), bukan asersi absence kelas g. Nilai `Draft Name` tidak pernah disimpan sehingga Search `Draft Name` ber-baseline sama sebelum dan sesudah.
- Temuan untuk QA:
  - TC-76 dan TC-77 menyebut "item menu navigasi lain di sidebar aplikasi" tanpa nama item; tujuan dipilih tim FE.
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai induk Add. Spec memakai `Induk {runId}-035` milik spec.
  - TC-75 menyebut dua kali F5 tanpa konfirmasi tetapi tidak menyebut hasil muat ulang pada tree; spec hanya mengasersi tidak munculnya konfirmasi.
