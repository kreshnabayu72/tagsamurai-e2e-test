---
id: TC-FA-PREF-E2E-039-caption-v-02-v-03-v-04-tanpa-titik-peringatan-sectioncard
title: "Caption V-02, V-03, V-04 tidak menampilkan titik peringatan SectionCard; V-09 dan V-10 tidak menyalakan titik General"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-615
  - TC-FA-PREF-616
  - TC-FA-PREF-617
  - TC-FA-PREF-619
coverage:
  web: automated
---

# Caption V-02, V-03, V-04 tidak menampilkan titik peringatan SectionCard; V-09 dan V-10 tidak menyalakan titik General

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PC (TC-FA-PREF-362-621), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), periode Mar 2026 sampai Dec 2026 Open, belum ada posting penyusutan.
- Data: akun Chart of Accounts PC-5 (`1-1001 – Kas Utama`, Active, function Asset Cost). Untuk TC-FA-PREF-619 seed memuat versi kedua Tax Depreciation Class ber-Effective From (PC-3) dan transaksi bertanggal paling awal 15 Mei 2026 (PC-4); Fiscal Year Start dan First Accounting Period tidak terkunci.
- Kemampuan teknis: sesi API Total Control (butir "Sesi API aktor" di `suite.md`): pelaku kedua yang hanya memicu perubahan state; token tidak dihitung sebagai sesi web. Dipakai untuk mengubah status akun `1-1001 – Kas Utama` menjadi Inactive pada TC-FA-PREF-617.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-615: Caption V-02 tidak menampilkan titik peringatan pada SectionCard Capitalization

1. Ketik "-1" pada CurrencyInput Default Capitalization Threshold
2. Verifikasi caption "Capitalization threshold must be 0 or more" tampil langsung pada field
3. Verifikasi judul SectionCard Capitalization tidak menampilkan titik peringatan (Badge Standalone Dot) karena seluruh setting wajib di section itu terisi
4. Klik `[Cancel]`

### TC-FA-PREF-616: Caption V-03 tidak menampilkan titik peringatan pada SectionCard Capitalization

5. Ketik "10000000000000000" (17 digit) pada CurrencyInput Default Capitalization Threshold
6. Verifikasi input menampilkan "10.000.000.000.000.000"
7. Verifikasi caption "Capitalization threshold is too large" tampil langsung pada field
8. Verifikasi judul SectionCard Capitalization tidak menampilkan titik peringatan (Badge Standalone Dot)
9. Klik `[Cancel]`

### TC-FA-PREF-617: Caption V-04 pada Found Asset Credit Account tidak menampilkan titik peringatan pada SectionCard Chart of Accounts

10. Pilih "1-1001 – Kas Utama" pada Select Found Asset Credit Account
11. Lewat sesi API Total Control, ubah status akun 1-1001 menjadi Inactive hingga tersimpan
12. Klik `[Save changes]`
13. Verifikasi caption "This found asset credit account no longer exists. Please select another." tampil pada Select Found Asset Credit Account
14. Verifikasi judul SectionCard Chart of Accounts tidak menampilkan titik peringatan (Badge Standalone Dot) karena tidak ada setting wajib yang kosong
15. Verifikasi tidak ada toast sukses

### TC-FA-PREF-619: Save yang ditolak V-09 dan V-10 tidak menampilkan titik peringatan pada judul SectionCard General

16. Pulihkan akun `1-1001 – Kas Utama` ke Active dan siapkan seed PC-3 dan PC-4 (versi kedua Tax Depreciation Class ber-Effective From; transaksi bertanggal paling awal 15 Mei 2026) lewat seed API hingga tersimpan
17. Buka ulang Fixed Asset > Settings > Accounting > Preferences
18. Ubah Select Fiscal Year Start dari "January" menjadi "April"
19. Ubah Select bulan First Accounting Period dari "March" menjadi "June"
20. Klik `[Save changes]` sampai dialog D-01 tampil
21. Klik `[Save]` pada dialog D-01
22. Verifikasi dialog D-01 ditutup
23. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
24. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada Select Fiscal Year Start
25. Verifikasi caption "First accounting period cannot be later than existing dated transactions." tampil pada First Accounting Period
26. Verifikasi judul SectionCard General tidak menampilkan titik peringatan (Badge Standalone Dot) karena tidak ada setting wajib di section itu yang kosong
27. Verifikasi tidak ada toast dan tidak ada dialog D-03
28. Klik `[Cancel]`

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 4, 9, 28; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 16; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 17.
- Urutan: TC-FA-PREF-615 sampai 617 memakai seed PC-1; TC-FA-PREF-619 terakhir karena membutuhkan varian PC-3 dan PC-4 dalam satu seed (S-10).
- Temuan untuk QA:
  - TC-FA-PREF-617 tidak menyatakan apakah form kembali pristine setelah Select Found Asset Credit Account dikosongkan otomatis; spec tidak menambah `[Cancel]` setelahnya dan memulihkan akun lewat seed pembuka blok TC-FA-PREF-619.
  - TC-FA-PREF-619 Precondition d menyatakan PC-3 dan PC-4 ada pada seed yang sama, sedangkan Data Pre-setup mendefinisikannya sebagai varian company terpisah; spec memakai satu seed gabungan.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
