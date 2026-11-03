---
id: TC-FA-CF-E2E-142-sinkron-general-settings-format-tanggal-dan-currency
title: "Sinkron General Settings dan Identitas Aktor: Format Tanggal, Time Zone, Currency, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-548
  - TC-FA-CF-549
  - TC-FA-CF-550
  - TC-FA-CF-554
coverage:
  web: automated
---

# Sinkron General Settings dan Identitas Aktor: Format Tanggal, Time Zone, Currency, dan Modified By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (ganti akun eksplisit pada langkah 12): Total Control Company Changelog (Pre-setup #19) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Changelog; login UI dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD` (email tidak tertulis di Pre-setup TC; disediakan tim FE). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Company Changelog (Pre-setup #19): riwayat Changelog seed L1 sampai L12 pada tab General; baris seed L1 (`17/10/26, 10:45` Create `Asset Serial Tag`, tercatat 03:45 UTC) dicari lewat Filter Date pada tanggal seed, bukan lewat posisi teratas (S-14).
- State global: General Settings Company Alpha dan Company Changelog diubah ke varian (Pre-setup #27): Date Format `dd MMM yy`, Time Format 12 jam, Time Zone `(UTC+08:00) Kuala Lumpur, Singapore, Makassar`, Currency Code `USD`, disiapkan lewat seed di hook `before` spec ini; hook `after` memulihkan General Settings kedua Company ke baseline (Date Format `dd/MM/yy`, 24 jam, `(UTC+07:00) Bangkok, Hanoi, Jakarta`, `IDR`) (R-08). Suite berjalan serial.
- Data Dinamis: field `MB Check {runId}-142` (Text, Scope General) dibersihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): seed varian General Settings dan pemulihannya.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-548: Kolom Last Updated mengikuti Date Format, Time Format, dan Time Zone General Settings varian

1. Verifikasi Last Updated baris `Asset Serial Tag` (tersimpan 17/10/26 03:45 UTC) menampilkan `17 Oct 26, 11:45 AM`

### TC-FA-CF-550: Simbol mata uang input Global Value Currency mengikuti Currency Code tenant

2. Klik `[+ Custom Field]`, pilih Data Type `Currency`, lalu pilih Value Type `Global`
3. Verifikasi input Value menampilkan prefix simbol `$` (bukan `Rp`)
4. Verifikasi field hanya menampung nilai numerik tanpa pilihan mata uang
5. Klik `✕` pada modal Create
6. Verifikasi dialog `Unsaved Changes` tampil
7. Klik `[Leave]` pada dialog `Unsaved Changes`

### TC-FA-CF-554: Identitas aktor pada kolom Modified By berasal dari Global Settings > User

8. Klik `[+ Custom Field]`, isi Field Name `MB Check {runId}-142`, pilih Data Type `Text` dan Scope `General`, lalu klik `[Submit]` oleh pengguna `Sarah Johnson`
9. Ketik Search `MB Check {runId}-142`, tekan Enter
10. Verifikasi kolom Modified By baris `MB Check {runId}-142` menampilkan `Sarah J`
11. Klik `(←)` pada kotak Search

### TC-FA-CF-549: Kolom Date dan input Date Filter Modal Changelog mengikuti General Settings varian

12. Ganti akun: logout, lalu login sebagai Total Control Company Changelog (Pre-setup #19)
13. Buka Modal Changelog
14. Verifikasi kolom Date baris seed L1 (Create `Asset Serial Tag`, tercatat 17/10/26 03:45 UTC) menampilkan `17 Oct 26, 11:45 AM`
15. Buka Filter dan pilih Date 17 Oct 26
16. Verifikasi input Date Filter menampilkan teks tanggal terpilih dalam format `dd MMM yy` (`17 Oct 26`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 548, 550, 554 (Company Alpha), lalu 549 (Company Changelog, ganti akun eksplisit pada langkah 12).
- P-5 (b): perubahan General Settings (format tanggal dan Currency) adalah objek uji ringan kelas h dalam spec pencatatan dengan permukaan sama (tabel Custom Fields); state global dipulihkan di hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, pencarian baris target lewat Search (R-16), dan `(←)` pada kotak Search.
- Temuan untuk QA:
  - TC-FA-CF-549 Expected a menyebut "baris pertama" untuk Date `17 Oct 26, 11:45 AM`; karena Changelog adalah audit trail yang tumbuh (S-14), spec mengacu pada baris seed L1 (Create `Asset Serial Tag`).
  - TC-FA-CF-549 Precondition menyebut Company Changelog dengan General Settings varian (Pre-setup #19 dan #27) sedangkan Pre-setup #27 hanya mendefinisikan varian untuk Company Alpha; spec menerapkan varian yang sama pada Company Changelog.
  - TC-FA-CF-554 tidak menyebut Scope dan Data Type field yang dibuat; spec memakai Text dan Scope `General`.
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; env var `FA_TC_CHANGELOG_PASSWORD` disediakan tim FE.
