---
id: TC-AC-LCS-E2E-167-bypass-selection-limit-bulk-delete-ditolak-server
title: "Bypass Guard UI Selection Limit: Bulk Delete 101 Baris Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-585
coverage:
  web: automated
---

# Bypass Guard UI Selection Limit: Bulk Delete 101 Baris Ditolak Server

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: guard UI dilewati lewat injeksi DOM dan penolakan server diamati).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: 150 Group level 1 pada Settings > Group diatur lewat Fixture BE (seeding minimal 101 baris; disediakan tim FE/BE) dan dibuang di hook `after` suite; Selection Limit tersimpan `100` diatur lewat Fixture BE sebagai precondition TC.
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): penguji dapat menyuntikkan status checkbox lewat DOM untuk melewati guard UI; Fixture BE untuk membangun 150 Group, mengisi tab System Limits, membaca jumlah Group, dan memulihkan ketujuh tab ke nilai default.
- State global: konfigurasi tab System Limits dan 150 Group diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

1. Atur lewat Fixture BE: Selection Limit tersimpan `100`; Settings > Group memuat 150 Group level 1 pada tabel dengan Bulk Action Bar; catat jumlah Group level 1 sebelum aksi
2. Buka Settings > Group
3. Suntikkan status tercentang pada 101 baris lewat DOM
4. Pilih Bulk Action > Delete
5. Verifikasi Dialog Blok `[OK]` dengan teks "You have selected 101 rows, which exceeds the maximum of 100 rows per bulk action. Please narrow your filter or select fewer rows."
6. Klik `[OK]` pada Dialog Blok
7. Verifikasi tidak ada Group yang terhapus (jumlah Group level 1 dibaca lewat Fixture BE sama dengan jumlah sebelum aksi)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Penolakan server diamati lewat Dialog Blok pada UI karena TC menyuntikkan status checkbox lewat DOM (bukan request langsung ke server).
- Temuan untuk QA:
  - TC 585 Expected b "Tidak ada Group yang terhapus" tidak menyebut cara pengamatan; spec membaca jumlah Group lewat Fixture BE yang disediakan tim FE/BE dan membandingkannya dengan jumlah sebelum aksi.
  - Post Condition ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 6.
