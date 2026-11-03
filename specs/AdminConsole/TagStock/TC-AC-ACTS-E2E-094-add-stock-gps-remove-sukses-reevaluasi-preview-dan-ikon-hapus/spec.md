---
id: TC-AC-ACTS-E2E-094-add-stock-gps-remove-sukses-reevaluasi-preview-dan-ikon-hapus
title: "Add Stock GPS: Remove Sukses (T-37) dengan Ringkasan Dihitung Ulang, Re-evaluasi IMEI Kembar, dan Ikon Hapus per Baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-883
  - TC-AC-ACTS-884
  - TC-AC-ACTS-886
coverage:
  web: automated
---

# Add Stock GPS: Remove Sukses (T-37) dengan Ringkasan Dihitung Ulang, Re-evaluasi IMEI Kembar, dan Ikon Hapus per Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC, tidak diasersi). Unit `356938035643816` yang didaftarkan langkah 20 dihapus lewat fixture BE di hook `after`.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca jumlah unit Available SKU dan jumlah Subject pending (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-883: Remove dari Preview sukses dengan toast T-37, Ringkasan dihitung ulang, bar hilang

1. Catat baseline jumlah unit Available SKU dan jumlah Subject pending
2. Tambahkan IMEI baru `356938035643809`, `356938035643811`, dan `356938035643812` (tiga baris OK) serta `12345` (satu baris Invalid Format) lewat Manual Entry
3. Centang dua baris OK (`356938035643809` dan `356938035643811`)
4. Pilih Bulk Action > `Remove`
5. Klik `[Remove]` pada dialog
6. Verifikasi toast "Success, IMEI has been removed."
7. Verifikasi Preview menyisakan satu baris OK dan satu baris Invalid Format
8. Verifikasi Ringkasan `1 valid, 0 waiting approval, 0 duplicate, 1 invalid of 2 entries`
9. Verifikasi bar hilang dan seleksi 0
10. Verifikasi tidak ada data tersimpan (jumlah unit dan Subject tidak berubah terhadap baseline)
11. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-884: Remove kemunculan pertama IMEI kembar dan baris Waiting mengevaluasi ulang Preview

12. Tambahkan IMEI X `356938035643816` dua kali (satu OK dan satu Duplicate in File/List) serta IMEI W existing `356938035643810` (Waiting for Approval) lewat Manual Entry
13. Centang baris IMEI X yang OK
14. Pilih Bulk Action > `Remove`, klik `[Remove]` pada dialog
15. Verifikasi baris IMEI X yang tersisa menjadi OK (bukan Duplicate in File/List)
16. Verifikasi Ringkasan dihitung ulang `1 valid, 1 waiting approval, 0 duplicate, 0 invalid of 2 entries`
17. Centang baris IMEI W
18. Pilih Bulk Action > `Remove`, klik `[Remove]` pada dialog
19. Verifikasi tidak ada baris Waiting for Approval di Preview
20. Klik `[Submit]`
21. Verifikasi toast "Success, TAG has been registered."
22. Verifikasi tidak ada dialog `Partial Register`

### TC-AC-ACTS-886: Ikon hapus per baris tetap menghapus tanpa dialog; Select All lalu Remove mengosongkan Preview dan seleksi

23. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
24. Tambahkan tiga IMEI OK `356938035643809`, `356938035643811`, dan `356938035643812` lewat Manual Entry
25. Centang baris 1
26. Klik ikon hapus pada baris 2
27. Verifikasi baris 2 terhapus langsung tanpa dialog
28. Verifikasi seleksi baris 1 tetap
29. Klik Select All pada header
30. Pilih Bulk Action > `Remove`, klik `[Remove]` pada dialog `Remove IMEIs`
31. Verifikasi Preview kosong
32. Verifikasi seleksi kosong dan bar hilang

## Notes

- Mode: FE+BE.
- Akun: TC-AC-ACTS-883, TC-AC-ACTS-884, dan TC-AC-ACTS-886 seluruhnya memakai Distributor Toggle ON sesuai TC (baris Waiting for Approval hanya terbentuk untuk Distributor; bypass E2a Total Control, TC-AC-ACTS-734), sehingga satu akun cukup (S-07).
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12), "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" (S-09), dan buka kembali halaman Add Stock sesudah Submit (langkah 20).
- Temuan untuk QA:
  - TC-AC-ACTS-886 menyebut `D-12` untuk Select All lalu Remove tanpa jumlah baris; spec memakai dialog `Remove IMEIs` untuk dua baris tersisa.
