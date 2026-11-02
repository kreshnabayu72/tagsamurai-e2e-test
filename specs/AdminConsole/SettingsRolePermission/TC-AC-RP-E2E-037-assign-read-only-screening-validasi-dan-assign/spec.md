---
id: TC-AC-RP-E2E-037-assign-read-only-screening-validasi-dan-assign
title: "Assign Read Only: Screening Popup, Total Control Tidak Dapat Dijadikan Read Only, dan Assign User Standard"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-138
  - TC-AC-RP-139
  - TC-AC-RP-141
coverage:
  web: automated
---

# Assign Read Only: Screening Popup, Total Control Tidak Dapat Dijadikan Read Only, dan Assign User Standard

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses dan penugasan Group Manager) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-138: Screening popup Assign Read Only dan pool kandidat

1. Klik tab `Read Only`
2. Klik tombol "+ Assign"
3. Amati header dan baris kandidat popup
4. Verifikasi header popup "Assign Read Only"
5. Verifikasi struktur popup sama dengan popup Assign Total Control: toolbar Search dan Filter; kolom Checkbox, Name, Email, Position, Division, Status; footer `[Cancel]` dan `[Assign]`
6. Telusuri seluruh halaman Pagination popup dan amati seluruh baris kandidat
7. Verifikasi kandidat memuat `Fajar Nugroho` (Group Manager) dan user Standard berstatus apa pun, termasuk `Teguh Santoso` dan `Jane Smith` (Inactive)
8. Verifikasi kandidat tidak memuat pemegang Total Control, Default User, pemegang Read Only (`Dewi Anggraini`, `Lisa Wong`), maupun aktor

### TC-AC-RP-141: Total Control tidak dapat langsung dijadikan Read Only

9. Ketik Search `John Doe`, tekan Enter
10. Verifikasi picker menampilkan "No results found"

### TC-AC-RP-139: Assign Read Only ke user Standard

11. Ganti isi kotak search dengan `Alex Tan`, tekan Enter
12. Centang `Alex Tan`
13. Klik `[Assign]`
14. Verifikasi toast "Success, Read Only has been assigned."
15. Verifikasi `Alex Tan` muncul di Tab Read Only
16. Klik tab `System`
17. Klik `⋯` pada baris `Manage device master data` di section Global Role lalu klik `Detail`
18. Ketik Search `Alex Tan`, tekan Enter
19. Verifikasi pada baris `Alex Tan` kolom R tercentang
20. Verifikasi pada baris `Alex Tan` kolom C, U, dan D tidak tercentang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 6, 16 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 11, 18.
- Penyimpangan urutan (S-05, S-10): TC-AC-RP-141 (blokir) diletakkan sebelum TC-AC-RP-139 (assign sukses). Popup yang dibuka di langkah 2 dipakai bersama TC-AC-RP-138, 141, dan 139 (jumlah buka tidak melebihi jumlah tutup, prinsip 6) dan ditutup oleh `[Assign]` di langkah 13.
- Search `John Doe` (langkah 9) adalah aksi TC-AC-RP-141, bukan langkah penghubung.
- Temuan untuk QA:
  - Picker memuat lebih dari 10 kandidat (Pagination default 10) dan TC tidak menyatakan cara menelusuri halaman; spec menelusuri seluruh halaman Pagination untuk asersi daftar kandidat dan memakai Search untuk menemukan baris target (S-14, S-15).
  - TC-AC-RP-141 Expected kalimat kedua ("Total Control harus di-Remove lebih dahulu sebelum dapat di-Assign Read Only") adalah alasan aturan tanpa elemen UI; spec hanya mengasersi "No results found".
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
