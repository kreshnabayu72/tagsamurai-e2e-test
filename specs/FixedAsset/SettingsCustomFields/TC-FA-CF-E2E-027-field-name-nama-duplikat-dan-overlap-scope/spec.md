---
id: TC-FA-CF-E2E-027-field-name-nama-duplikat-dan-overlap-scope
title: "Field Name: Nama Duplikat, Beda Huruf, dan Scope Overlap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-68
  - TC-FA-CF-69
  - TC-FA-CF-70
coverage:
  web: automated
---

# Field Name: Nama Duplikat, Beda Huruf, dan Scope Overlap

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data dinamis. Seed lewat API di hook `before` (milik spec, S-06):
  - S-1: `Asset Serial Tag {runId}-027`, Data Type Text, Scope General, Value Type Specific, Required No (padanan baris Pre-setup #12 `Asset Serial Tag`).
  - S-2: `Storage Capacity {runId}-027`, Data Type Numeric 0 Decimal Places, Scope {Generator, Pump}, Value Type Specific, Required No (padanan baris Pre-setup #12 `Storage Capacity`).
- Data dinamis dibuat lewat UI oleh spec ini:
  - D-1: `Asset Serial Tag {runId}-027`, Data Type Text, Scope General (nama sama persis dengan S-1).
  - D-2: `ASSET SERIAL TAG {runId}-027`, Data Type Text (nama sama dengan S-1 berbeda huruf besar-kecil).
  - D-3: `Storage Capacity {runId}-027`, Data Type Text, Scope Specific Asset Name `Pump` (nama dan Scope overlap dengan S-2).
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-027`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-68: Field Name sama persis dengan field lain dalam grup yang sama diizinkan

1. Klik `[+ Custom Field]`
2. Isi Field Name `Asset Serial Tag {runId}-027`, Data Type `Text`, Scope `General`
3. Klik `[Submit]`
4. Verifikasi tidak ada pesan duplikat
5. Verifikasi toast sukses: "Success, custom field has been created."
6. Ketik Search `Asset Serial Tag {runId}-027`, tekan Enter
7. Verifikasi tabel memuat dua baris `Asset Serial Tag {runId}-027` yang independen

#### TC-FA-CF-69: Field Name sama dengan field lain berbeda huruf besar-kecil diizinkan

8. Klik `[+ Custom Field]`
9. Isi Field Name `ASSET SERIAL TAG {runId}-027`, Data Type `Text`
10. Tunggu toast lama hilang otomatis
11. Klik `[Submit]`
12. Verifikasi toast sukses: "Success, custom field has been created."
13. Ganti isi kotak search dengan `ASSET SERIAL TAG {runId}-027`, tekan Enter
14. Verifikasi baris `ASSET SERIAL TAG {runId}-027` tampil sebagai baris baru

#### TC-FA-CF-70: Dua field bernama sama dengan Scope overlap tersimpan sebagai rekaman independen

15. Klik `[+ Custom Field]`
16. Isi Field Name `Storage Capacity {runId}-027`, Data Type `Text`, pilih Scope `Specific Asset Name` dengan Asset Name `Pump`
17. Klik `[Submit]`
18. Ganti isi kotak search dengan `Storage Capacity {runId}-027`, tekan Enter
19. Verifikasi tabel memuat dua baris `Storage Capacity {runId}-027` dengan Data Type `Numeric` dan `Text`
20. Verifikasi baris Data Type `Numeric` menampilkan Scope badge `Generator` dan `Pump`, Required `No`
21. Verifikasi baris Data Type `Text` menampilkan Scope badge `Pump`, Required `No`
22. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16) dan `Klik (←)` untuk mereset Search di akhir.
- Field Dinamis bernama bersuffix `{runId}-027` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca. Field Pre-setup #12 `Asset Serial Tag` dan `Storage Capacity` tidak dipakai sebagai target; spec membuat padanannya bersuffix milik sendiri lewat seeding supaya nama duplikat yang diuji tetap sama persis dan baseline Pre-setup tidak berubah (S-06).
- Expected TC-FA-CF-70 butir a ('Data Type, Required, Values, dan Scope masing-masing sendiri') diasersi pada kolom Data Type, Scope, dan Required; kolom Value Setting tidak diasersi karena Text tanpa Values dan Numeric tanpa nilai disebut TC.
- Asersi 'tidak ada pesan duplikat' (TC-FA-CF-68 butir a) ditulis segera setelah `[Submit]` dan sebelum toast.
- Langkah penghubung toast (S-03, R-22): langkah 10 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-69 butir b 'Field tersimpan sebagai baris baru' tidak menyebut jumlah baris; Search `ASSET SERIAL TAG {runId}-027` bisa mengembalikan tiga baris bila Search tidak membedakan huruf besar-kecil, sehingga spec hanya mengasersi baris bernama huruf besar tampil.
  - TC-FA-CF-68 dan TC-FA-CF-69 menyebut Pre-setup `Asset Serial Tag` yang ada di baseline; spec memakai padanan bersuffix milik spec (lihat Notes di atas).
