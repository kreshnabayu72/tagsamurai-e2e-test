---
id: TC-FA-PREF-E2E-164-save-fiscal-year-start-ditolak-d03-saat-soft-closed-muncul-di-d01
title: "Save Fiscal Year Start Ditolak D-03 Saat Periode Soft Closed Muncul Setelah D-01 Terbuka"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-559
coverage:
  web: automated
---

# Save Fiscal Year Start Ditolak D-03 Saat Periode Soft Closed Muncul Setelah D-01 Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PC-1 (Preferences nilai awal; belum ada posting penyusutan, semua periode Open; bulan berjalan Oktober 2026) dan PC-8 (akun pengguna).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Sesi API aktor untuk pemicu perubahan state (fixture BE): kemampuan disediakan tim BE/FE (butir "Sesi API aktor" di `suite.md`).
- Pelaku sesi B diganti fixture BE lewat sesi API aktor (bukan sesi UI kedua); TC sumber menandai TC ini Manual Only karena dua sesi paralel.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-559: Periode Soft Closed saat dialog Save Changes terbuka membuat Save Fiscal Year Start menampilkan dialog blok

1. Klik ikon View history lalu catat jumlah baris pada modal Changelog dan tutup modal
2. Sesi A: pilih "April" pada Select Fiscal Year Start
3. Sesi A: klik [Save changes]
4. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
5. Verifikasi body dialog memuat daftar bullet: "13 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start."
6. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
7. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
8. Sesi B: lewat sesi API (fixture BE), ubah status periode Mar 2026 menjadi Soft Closed hingga status tersimpan
9. Sesi A: klik [Save] pada dialog Save Changes
10. Verifikasi dialog "Cannot Save Preferences" tampil
11. Verifikasi body dialog D-03: "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status."
12. Verifikasi dialog hanya memuat tombol [OK]
13. Verifikasi tidak ada toast tambahan
14. Sesi A: klik [OK]
15. Verifikasi halaman dimuat ulang dari nilai tersimpan dan Select Fiscal Year Start menampilkan "January" (perubahan yang belum disimpan dibuang)
16. Verifikasi Select Fiscal Year Start dan First Accounting Period tampil Disabled dengan ikon gembok
17. Arahkan kursor ke Select Fiscal Year Start
18. Verifikasi tooltip "Fiscal year start is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page." tampil
19. Arahkan kursor ke Select bulan First Accounting Period
20. Verifikasi tooltip "First accounting period is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page." tampil
21. Verifikasi Select bulan dan tahun First Accounting Period menampilkan "March" dan "2026" (tidak ada yang tersimpan)
22. Klik ikon View history
23. Verifikasi jumlah baris pada modal Changelog sama dengan jumlah yang dicatat sebelum aksi (tidak ada baris log baru)
24. Tutup modal Changelog
25. Pulihkan periode dan Preferences ke PC-1 lewat seed API

## Notes

- Langkah penghubung (S-03): catat baseline Changelog, tutup modal, dan pemulihan seed. Sesi B diganti pemicu fixture BE lewat sesi API; sesi UI A satu-satunya yang diasersi.
- P-1: asersi "tidak ada baris log baru" (Expected e) ditulis di spec ini dengan baseline Changelog karena bergantung pada state kunci yang dibangun langkah sebelumnya dan tidak ada spec absence yang memuat aksi nyata TC ini (S-05).
- Tooltip kunci memakai teks ST-05 dari TC-FA-PREF-238 karena TC-559 hanya menyebut "tooltip kunci".
- Temuan untuk QA:
  - TC-559 ditandai Manual Only (butuh dua sesi pengguna paralel); spec memakai fixture BE sebagai pemicu setelah dialog Save Changes terbuka. Perlu konfirmasi kemampuan itu ke tim FE/BE.
  - TC-559 Expected e "tidak ada baris log baru" tidak menyebut surface log; spec memakai Changelog Preferences (satu-satunya dengan langkah observasi pada TC sejenis, TC-244). System Log dan Activity Log tidak diasersi.
  - TC-559 Expected d menyebut "tooltip kunci" tanpa teks; teks diambil dari TC-238.
