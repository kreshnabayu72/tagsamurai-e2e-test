---
id: TC-FA-CF-E2E-055-perilaku-form-create-submit-tidak-valid-dan-clear-field
title: "Perilaku Form Create: Submit dengan Beberapa Field Tidak Valid dan Clear Field"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-174
  - TC-FA-CF-175
coverage:
  web: automated
---

# Perilaku Form Create: Submit dengan Beberapa Field Tidak Valid dan Clear Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); Asset Name `Pump` sudah ada di baseline.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-055`): `To Clear {runId}-055` (Dropdown dengan opsi `A`, Scope `Pump`, Required Yes; tidak pernah tersimpan). Tidak ada field yang tersimpan oleh spec ini.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-055`.
- Kemampuan teknis: pembacaan state checkbox, isi input, dan pesan error inline pada modal Create; pengamatan toast.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-174: Submit dengan beberapa field tidak valid menampilkan semua pesan inline tanpa toast

1. Klik [+ Custom Field]
2. Biarkan Field Name dan Data Type kosong
3. Pilih Scope `Specific Asset Name` tanpa memilih Asset Name
4. Klik [Submit]
5. Verifikasi tidak ada toast
6. Verifikasi pesan inline "Field name must not be empty" tampil
7. Verifikasi pesan inline "Data type must not be empty" tampil
8. Verifikasi pesan inline "Please select at least one asset name" tampil
9. Verifikasi modal tetap terbuka
10. Verifikasi input dipertahankan: Scope tetap `Specific Asset Name`
11. Klik `[✕]`
12. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
13. Klik `[Leave]`

### TC-FA-CF-175: Klik Clear Field pada Create mengosongkan input, menghapus pesan error, dan modal tetap terbuka

14. Klik [+ Custom Field]
15. Isi Field Name `To Clear {runId}-055`, pilih Data Type `Dropdown` dengan opsi `A`, Scope `Specific Asset Name` dengan `Pump`, Required Yes
16. Kosongkan Field Name, lalu klik [Submit]
17. Verifikasi pesan error inline tampil pada Field Name
18. Isi Field Name `To Clear {runId}-055`
19. Centang `Stay on this form after submitting`
20. Klik [Clear Field]
21. Verifikasi Field Name kosong
22. Verifikasi Data Type belum dipilih
23. Verifikasi Scope `General`
24. Verifikasi Value Type `Specific`
25. Verifikasi Required No
26. Verifikasi pesan error inline hilang
27. Verifikasi modal tetap terbuka
28. Verifikasi tidak ada dialog konfirmasi
29. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
30. Hapus centang `Stay on this form after submitting`
31. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (174, 175). TC-FA-CF-174 berakhir dengan form dirty sehingga ditutup lewat `[✕]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08) sebelum TC-FA-CF-175 membuka modal baru.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3, 11, 13, 14, 18, 19, 30, 31, serta pengisian form dan klik tombol sebagai bagian langkah TC. Langkah 30 (hapus centang `Stay on this form after submitting`) mengembalikan form ke kondisi awal sebelum `[✕]` pada langkah 31; form identik dengan kondisi awal dianggap bersih (TC-FA-CF-181) sehingga dialog `Unsaved Changes` tidak diharapkan.
- Langkah 5 diletakkan segera setelah pemicu [Submit] dan sebelum asersi pesan inline (bagian 8b butir 11); pesan inline pada langkah 6 sampai 8 menjadi anchor positif bahwa Submit sudah diproses. Langkah 17 adalah anchor positif bagi Expected b TC-FA-CF-175 ("pesan error inline hilang"), bukan Expected TC.
- Langkah 6 sampai 8 memecah Expected a TC-FA-CF-174 per pesan (S-01).
- Temuan untuk QA:
  - TC-FA-CF-175: Langkah Uji menulis "Value Type tidak berlaku" untuk Data Type Dropdown, sedangkan Expected a mengasersi Value Type `Specific` setelah [Clear Field]; spec mengikuti Expected.
  - TC-FA-CF-175: Langkah 3 TC mengisi Field Name kembali sesudah Submit gagal tanpa menyebut nilai pemicu pesan error selain Field Name kosong; spec memicu pesan lewat Field Name kosong (langkah 16).
  - Nama field memakai suffix `{runId}-055` (S-12) sehingga tidak sama dengan `To Clear` pada Data Uji TC.
  - TC-FA-CF-175 menutup form dengan `[✕]` sesudah [Clear Field] dengan checkbox Stay tercentang tanpa menyebut apakah centang itu membuat form dirty; spec menghapus centang lebih dulu (langkah 30) agar penutupan deterministik. Bila PRD menetapkan checkbox Stay bukan bagian kondisi dirty, langkah itu tidak diperlukan.
