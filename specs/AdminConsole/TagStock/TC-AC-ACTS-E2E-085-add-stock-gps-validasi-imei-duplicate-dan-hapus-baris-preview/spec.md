---
id: TC-AC-ACTS-E2E-085-add-stock-gps-validasi-imei-duplicate-dan-hapus-baris-preview
title: "Add Stock GPS: Validasi IMEI 15 Digit, Duplicate in File/List, Hapus Baris Preview, dan Re-evaluasi Kemunculan Pertama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-246
  - TC-AC-ACTS-247
  - TC-AC-ACTS-248
  - TC-AC-ACTS-249
  - TC-AC-ACTS-763
coverage:
  web: automated
---

# Add Stock GPS: Validasi IMEI 15 Digit, Duplicate in File/List, Hapus Baris Preview, dan Re-evaluasi Kemunculan Pertama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC, tidak diasersi). Unit `356938035643815` yang didaftarkan langkah 15 dihapus lewat fixture BE di hook `after`.
- Kemampuan teknis disediakan tim FE: pembuat dan pengunggah berkas CSV berheader `IMEI` (kelas f); kemampuan baca jumlah unit SKU dan jumlah Subject Tab Active (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-246: Hapus satu baris Preview lewat ikon hapus

1. Tambahkan IMEI `356938035643809`, `356938035643811`, dan `356938035643812` lewat Manual Entry (ketik di input IMEI, klik `[+ Add]` untuk tiap IMEI; dipakai sebagai precondition TC, tidak diasersi)
2. Klik ikon hapus pada baris kedua (`356938035643811`)
3. Verifikasi baris kedua hilang
4. Verifikasi dua baris lain (`356938035643809` dan `356938035643812`) tetap ada
5. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-247: Validasi IMEI tepat 15 digit angka, selain itu Invalid Format

6. Tambahkan lewat Manual Entry berturut-turut: `35693803564380` (14 digit), `3569380356438090` (16 digit), `35693803564380A`, `3569 3803 5643 809`, dan input kosong
7. Verifikasi lima nilai pertama berstatus Invalid Format
8. Tambahkan IMEI ` 356938035643814 ` (dengan spasi di tepi)
9. Verifikasi IMEI dengan spasi di tepi di-trim lalu dinilai valid (OK)
10. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-248: Duplicate in File/List, kemunculan pertama dievaluasi normal dan berikutnya Duplicate

11. Catat baseline jumlah unit SKU dan jumlah Subject di Approvals > TAG Stock > Tab Active
12. Unggah file CSV berheader `IMEI` berisi `356938035643815` dua kali (IMEI belum terdaftar)
13. Verifikasi kemunculan pertama berstatus OK
14. Verifikasi kemunculan kedua berstatus Duplicate in File/List
15. Klik `[Submit]`
16. Verifikasi halaman menavigasi ke Detail SKU > Tab Available
17. Verifikasi tidak ada dialog `Partial Register`
18. Verifikasi jumlah unit SKU bertambah tepat 1 terhadap baseline (baris Duplicate tidak ikut Submit)
19. Verifikasi jumlah Subject di Approvals > TAG Stock > Tab Active tidak berubah terhadap baseline (baris Duplicate bukan approval)
20. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)

### TC-AC-ACTS-249: Duplicate lintas file dan Manual Entry ditandai Duplicate in File/List

21. Unggah file CSV berisi IMEI X `356938035643816`
22. Tambahkan IMEI X `356938035643816` lewat Manual Entry
23. Verifikasi baris Manual Entry berstatus Duplicate in File/List
24. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-763: Hapus baris Preview, kemunculan IMEI kembar berikutnya dievaluasi ulang sebagai kemunculan pertama

25. Ganti akun: klik Logout
26. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
27. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
28. Tambahkan IMEI `356938035643816` dua kali lewat Manual Entry (baris #1 dan #2)
29. Tambahkan IMEI `356938035643810` dua kali lewat Manual Entry (baris #3 dan #4)
30. Verifikasi baris #1 berstatus OK
31. Verifikasi baris #2 berstatus Duplicate in File/List
32. Verifikasi baris #3 berstatus Waiting for Approval
33. Verifikasi baris #4 berstatus Duplicate in File/List
34. Verifikasi Ringkasan `1 valid, 1 waiting approval, 2 duplicate, 0 invalid of 4 entries`
35. Klik ikon hapus pada baris #1 dan baris #3
36. Verifikasi baris #2 (kini kemunculan pertama IMEI `356938035643816`) dievaluasi ulang menjadi OK
37. Verifikasi baris #4 (kini kemunculan pertama IMEI `356938035643810`) menjadi Waiting for Approval
38. Verifikasi Ringkasan dihitung ulang `1 valid, 1 waiting approval, 0 duplicate, 0 invalid of 2 entries`
39. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (39 langkah); alasan: semua blok satu kelas harness (kelas f, berkas CSV/XLSX dan mekanisme impor) dan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-763 (Distributor) terakhir supaya penggantian akun hanya satu kali (S-07, S-10).
- Langkah penghubung tanpa Verifikasi (S-03): "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" sesudah tiap TC (S-09), langkah buka kembali halaman Add Stock sesudah Submit (langkah 15), dan langkah ganti akun serta buka halaman untuk TC-AC-ACTS-763.
- Klausa b TC-AC-ACTS-248 ("tidak ikut Submit dan bukan approval") diamati lewat selisih terhadap baseline setelah `[Submit]` (unit +1, Subject tidak berubah); ini asersi jumlah, bukan kelas g (prinsip 13g).
- Temuan untuk QA:
  - TC-AC-ACTS-248 tidak menyebut cara mengamati "tidak ikut Submit dan bukan approval"; spec memakai selisih jumlah unit dan Subject terhadap baseline.
  - TC-AC-ACTS-247 menyebut kolom "kosong" sebagai nilai IMEI tanpa menyebut aksinya; spec memakai `[+ Add]` pada input kosong (selaras TC-AC-ACTS-272).
