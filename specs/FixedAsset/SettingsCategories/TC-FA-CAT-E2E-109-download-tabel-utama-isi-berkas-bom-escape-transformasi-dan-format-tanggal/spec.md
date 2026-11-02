---
id: TC-FA-CAT-E2E-109-download-tabel-utama-isi-berkas-bom-escape-transformasi-dan-format-tanggal
title: "Download: Isi Berkas XLSX dan CSV (Tipe Sel, BOM, Escape), Berkas Changelog, dan Format Tanggal General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-371
  - TC-FA-CAT-372
  - TC-FA-CAT-614
  - TC-FA-CAT-496
coverage:
  web: automated
---

# Download: Isi Berkas XLSX dan CSV (Tipe Sel, BOM, Escape), Berkas Changelog, dan Format Tanggal General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Kelas harness: binary buffer (isi berkas CSV dan XLSX: nilai sel, tipe sel, BOM, escape). Kemampuan membaca isi berkas yang terunduh disediakan tim FE.
- Data Pre-setup #20 (CatMain), hanya dibaca: `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12, Alex Brown) dan `Monitor` (Code `ELEC-MN`, Total Asset 0). Data Pre-setup #23 (Changelog CatMain): baris Create `Electronics`, Delete `Kunci Locker`, Marked as Excess `Vehicle`, dan Edit rename `Laptop` ke `Notebook` (Category Name `Electronics › Notebook`). Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dihapus hook `after`): kategori L1 `Q,uote "X" {runId}-109`.
- State global yang diubah spec (langkah 20 sampai 23): General Settings Date Format, Time Format, dan Time Zone. Nilai awal dibaca sebelum diubah lewat kemampuan baca yang disediakan tim FE/BE (dipakai sebagai acuan format pada langkah 4 dan 15); hook `after` memulihkannya ke nilai awal lewat API (disediakan tim FE/BE). Spec berjalan serial.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-371: Transformasi data per tipe kolom di berkas XLSX

1. Klik node `Electronics` di Sidebar Category Tree
2. Klik Download > `Download as XLSX`
3. Verifikasi sel Total Asset `12` (baris `Laptop`) ditulis sebagai sel angka, bukan teks
4. Verifikasi Last Updated mengikuti Date Format dan Time Format General Settings
5. Verifikasi Modified By sesuai nilai tabel
6. Verifikasi Category dan Code ditulis sebagai teks
7. Verifikasi berkas satu sheet bernama `Sheet1`
8. Klik node `All Categories` di Sidebar Category Tree

### TC-FA-CAT-372: CSV memakai UTF-8 dengan BOM dan meng-escape karakter khusus

9. Klik Download > `Download as CSV`
10. Verifikasi berkas CSV berencoding UTF-8 dengan BOM
11. Verifikasi nilai `Q,uote "X" {runId}-109` dibungkus tanda kutip ganda dengan tanda kutip di dalamnya digandakan

### TC-FA-CAT-614: Download Modal Changelog

12. Klik icon Changelog di Table Tools
13. Klik Download > `Download as XLSX`
14. Verifikasi Old Value baris Create `Electronics` dan New Value baris Delete `Kunci Locker` yang tampil `—` ditulis `-` di berkas (bukan blank, `—`, atau `null`)
15. Verifikasi kolom Date mengikuti Date Format dan Time Format General Settings
16. Verifikasi Action, Field, Old Value, dan New Value ditulis teks apa adanya (mis. `Marked as Excess (Category Consolidation)`, Field `Excess`, Old Value `Usable`, New Value `Excess`)
17. Verifikasi Category Name ditulis sama dengan tabel (mis. `Electronics › Notebook` untuk baris hasil rename)
18. Tutup Modal Changelog dengan icon Close (✕)

### TC-FA-CAT-496: Berkas export memuat tanggal sesuai General Settings

19. Buka Global Settings > General Settings
20. Atur Date Format menjadi `dd MMM yy`
21. Atur Time Format menjadi 24 jam
22. Atur Time Zone ke nilai yang ditetapkan fixture (Fixture.settings-categories.timeZone)
23. Simpan perubahan General Settings
24. Buka Fixed Asset > Settings > Categories
25. Klik Download > `Download as XLSX`
26. Verifikasi sel Last Updated pada berkas ditulis dalam format `dd MMM yy` 24 jam sesuai General Settings

## Notes

- Langkah penghubung (S-03): langkah 8 (kembali ke `All Categories` sebelum TC-372), 18 (menutup Modal Changelog), 24 (membuka halaman Categories setelah mengubah General Settings).
- TC-496 diletakkan terakhir karena mengubah state global (General Settings); hook `after` memulihkannya (R-08).
- Temuan untuk QA:
  - TC-496 menyebut Time Zone diatur "menjadi `dd MMM yy` 24 jam" tanpa nilai zona waktu; spec memakai nilai dari fixture (langkah 22) dan nilai itu perlu ditetapkan tim.
  - TC-496 tidak menyebut label tombol penyimpanan General Settings; langkah 23 ditulis generik.
  - TC-372 menyebut kategori `Q,uote "X"` tanpa suffix; spec memakai nama milik spec berakhiran `{runId}-109` (S-06, S-12).
  - TC-371 butir b dan TC-614 butir b mengacu ke General Settings tanpa menyebut nilai default; spec membaca nilai awal sebagai acuan.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
