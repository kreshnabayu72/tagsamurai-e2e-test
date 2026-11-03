---
id: TC-AC-ACTS-E2E-084-add-stock-gps-screening-upload-csv-xlsx-manual-entry-dan-preview-bersama
title: "Add Stock GPS: Screening, Upload CSV dan XLSX Valid dengan Empat Status, Manual Entry, dan Satu Preview Bersama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-241
  - TC-AC-ACTS-242
  - TC-AC-ACTS-243
  - TC-AC-ACTS-244
  - TC-AC-ACTS-245
coverage:
  web: automated
---

# Add Stock GPS: Screening, Upload CSV dan XLSX Valid dengan Empat Status, Manual Entry, dan Satu Preview Bersama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15; Device Name `GPS Tracker Core`, Brand `Core`, Model/Type `G3`). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC, tidak diasersi). Spec ini tidak menekan `[Submit]`, sehingga tidak ada unit yang perlu dihapus.
- Kemampuan teknis disediakan tim FE (kelas f): pembuat dan pengunggah berkas CSV dan XLSX berheader `IMEI` dengan isi sesuai langkah.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-241: Screening halaman Add Stock GPS

1. Amati halaman Add Stock SKU GPS dari atas ke bawah
2. Verifikasi Breadcrumb `TAG > Stock > Detail > Add Stock`
3. Verifikasi judul `Add Stock` tanpa kode SKU
4. Verifikasi SKU info card baris 1 `GPS Tracker Core (GPS-TRACK-CORE-G3)` setelah foto
5. Verifikasi SKU info card memuat `TAG Type:` icon GPS, `Brand:` badge `Core`, dan `Model/Type:` badge `G3`
6. Verifikasi Body memuat `Download template`
7. Verifikasi dropzone `Drag & drop file here, or [Browse]` dengan `Accepted: .csv, .xlsx · Column: IMEI`
8. Verifikasi pemisah `— or —`
9. Verifikasi Manual Entry dengan input IMEI dan `[+ Add]`
10. Verifikasi Preview kosong
11. Verifikasi Footer memuat `[Cancel]` (text, contrast) dan `[Submit]` (Success) yang selalu enabled

### TC-AC-ACTS-244: Manual Entry menambahkan IMEI ke Preview

12. Ketik `356938035643813` di input IMEI
13. Klik `[+ Add]`
14. Verifikasi satu baris berstatus OK ditambahkan ke Preview
15. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-243: Upload XLSX valid menampilkan Preview

16. Unggah file XLSX berheader `IMEI` berisi IMEI `356938035643811` dan `356938035643812`
17. Verifikasi dua baris berstatus OK di Preview
18. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-245: Upload file dan Manual Entry berbagi satu Preview; upload kedua menambah baris

19. Unggah file berisi IMEI A `356938035643811`
20. Tambahkan IMEI B `356938035643813` lewat Manual Entry (ketik di input IMEI, klik `[+ Add]`)
21. Unggah file kedua berisi IMEI C `356938035643812`
22. Verifikasi Preview memuat A, B, dan C dalam satu tabel
23. Verifikasi upload kedua tidak mengganti baris yang ada (baris A dan B tetap)
24. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-242: Upload CSV valid menampilkan Preview dengan empat status dan ringkasan

25. Ganti akun: klik Logout
26. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
27. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
28. Unggah file CSV berheader `IMEI` berisi 4 baris: `356938035643809`, `356938035643810`, `356938035643809`, `12345`
29. Verifikasi baris 1 berstatus OK (success)
30. Verifikasi baris 2 berstatus Waiting for Approval (warning)
31. Verifikasi baris 3 berstatus Duplicate in File/List (warning)
32. Verifikasi baris 4 berstatus Invalid Format (danger)
33. Verifikasi Ringkasan `1 valid, 1 waiting approval, 1 duplicate, 1 invalid of 4 entries`
34. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

## Notes

- Mode: FE+BE. Satu kelas harness (kelas f, berkas CSV/XLSX) dan satu dataset; kegagalan satu blok TC tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-244 sebelum TC-AC-ACTS-243 dan TC-AC-ACTS-242 terakhir supaya penggantian akun (langkah 25) hanya satu kali (S-07, S-10).
- Langkah penghubung tanpa Verifikasi (S-03): langkah "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" sesudah tiap TC (S-09: Preview dibersihkan sebelum TC berikutnya mengandalkannya), serta langkah ganti akun dan buka halaman Add Stock untuk TC-AC-ACTS-242.
- Temuan untuk QA:
  - TC-AC-ACTS-245 menyebut "IMEI A, B, C" tanpa nilai; spec memakai `356938035643811`, `356938035643813`, dan `356938035643812` dari rentang Data Dinamis #2.
  - TC-AC-ACTS-241 meminta SKU info card "setelah foto" tanpa mendefinisikan foto SKU uji; spec mengasersi teks baris 1 saja.
