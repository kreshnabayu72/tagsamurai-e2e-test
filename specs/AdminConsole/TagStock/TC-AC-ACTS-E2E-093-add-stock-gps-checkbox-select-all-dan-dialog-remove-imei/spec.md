---
id: TC-AC-ACTS-E2E-093-add-stock-gps-checkbox-select-all-dan-dialog-remove-imei
title: "Add Stock GPS: Kolom Checkbox, Select All dan Unselect All, Bulk Action Bar Remove, serta Dialog Remove IMEI dan IMEIs"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-880
  - TC-AC-ACTS-881
  - TC-AC-ACTS-882
coverage:
  web: automated
---

# Add Stock GPS: Kolom Checkbox, Select All dan Unselect All, Bulk Action Bar Remove, serta Dialog Remove IMEI dan IMEIs

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC, tidak diasersi). Spec ini tidak menekan `[Submit]`, sehingga tidak ada unit yang perlu dihapus.
- Kemampuan teknis disediakan tim FE (kelas f): pembuat dan pengunggah berkas CSV berheader `IMEI` berisi 12 IMEI valid baru (TC-AC-ACTS-882).
- Env var password akun aktor: `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-880: Preview GPS memiliki kolom Checkbox, Select All, Unselect All, dan Bulk Action Bar Remove tanpa [Remove by Scan]

1. Tambahkan IMEI baru `356938035643809` (OK), IMEI existing `356938035643810` (Waiting for Approval), `356938035643809` sekali lagi (Duplicate in File/List), dan `12345` (Invalid Format) lewat Manual Entry (Preview berisi 4 baris)
2. Amati kolom paling kiri Preview dan area aksi
3. Verifikasi kolom Checkbox ada di paling kiri (pinned)
4. Verifikasi semua baris, apa pun statusnya, punya checkbox
5. Centang satu baris
6. Verifikasi bar tampil dengan `1 IMEI selected`
7. Verifikasi `Bulk Action` berisi satu aksi `Remove`
8. Verifikasi tombol `Select All (4 records)` tampil
9. Klik `Select All (4 records)`
10. Verifikasi tombol menjadi `Unselect All`
11. Klik `Unselect All`
12. Verifikasi seleksi dibatalkan
13. Verifikasi tidak ada tombol `[Remove by Scan]` pada halaman ini
14. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-881: Remove satu baris Preview membuka dialog Remove IMEI tanpa petunjuk scan; Cancel tidak mengeluarkan baris

15. Tambahkan tiga IMEI OK IMEI A `356938035643809`, IMEI B `356938035643811`, dan IMEI C `356938035643812` lewat Manual Entry
16. Centang IMEI A
17. Pilih Bulk Action > `Remove`
18. Verifikasi dialog `Remove IMEI` memuat `• 356938035643809` dan `Are you sure you want to remove it?` dengan tombol `[Cancel]` dan `[Remove]`
19. Verifikasi tidak ada baris `For more accurate results, use Remove by Scan.`
20. Klik `[Cancel]`
21. Verifikasi Preview tetap 3 baris
22. Verifikasi seleksi tetap ada
23. Klik `Unselect All`
24. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-882: Remove beberapa baris Preview membuka dialog Remove IMEIs dengan semua IMEI terpilih

25. Unggah file CSV berheader `IMEI` berisi 12 IMEI valid baru (Preview berisi 12 baris)
26. Klik `Select All (12 records)`
27. Pilih Bulk Action > `Remove`
28. Gulir daftar bullet di dialog
29. Verifikasi dialog `Remove IMEIs` memuat 12 bullet IMEI lengkap dalam container scrollable tanpa ringkasan jumlah
30. Verifikasi teks `Are you sure you want to remove them?`
31. Verifikasi tombol `[Cancel]` dan `[Remove]`
32. Verifikasi tidak ada baris petunjuk scan
33. Klik `[Cancel]`
34. Klik `Unselect All`
35. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

## Notes

- Mode: FE+BE.
- Akun: Distributor Toggle ON untuk seluruh TC, karena baris Waiting for Approval hanya terbentuk untuk Distributor (bypass E2a Total Control membuat IMEI existing berstatus OK, TC-AC-ACTS-734) dan precondition TC-AC-ACTS-880 memakai akun yang sama.
- Langkah penghubung tanpa Verifikasi (S-03): pengisian Preview lewat Manual Entry atau unggah berkas, `Unselect All` dan "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" (S-09).
- Temuan untuk QA:
  - TC-AC-ACTS-882 menyebut 12 baris Preview tanpa nilai IMEI; spec memakai 12 IMEI valid baru dari berkas (disediakan tim FE).
