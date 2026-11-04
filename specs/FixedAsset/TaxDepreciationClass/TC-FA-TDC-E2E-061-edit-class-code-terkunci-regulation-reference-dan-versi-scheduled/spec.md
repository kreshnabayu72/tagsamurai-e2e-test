---
id: TC-FA-TDC-E2E-061-edit-class-code-terkunci-regulation-reference-dan-versi-scheduled
title: "Edit: Class Code Terkunci, Regulation Reference, dan Edit pada Class dengan Versi Scheduled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-184
  - TC-FA-TDC-215
  - TC-FA-TDC-216
  - TC-FA-TDC-217
coverage:
  web: automated
---

# Edit: Class Code Terkunci, Regulation Reference, dan Edit pada Class dengan Versi Scheduled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk class berkunci dan versi Scheduled), kendali jam sistem, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- State global yang diubah: jam server dan jam browser diatur bersama ke `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta) di awal spec (langkah 1) dan dipulihkan dengan langkah eksplisit (langkah 42) serta di hook `after` sebagai cadangan.
- Kolom Regulation Reference tidak ditampilkan di tabel (keadaan bawaan); Search tetap mencari nilai Regulation Reference walau kolom tersembunyi.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `khsV2` | `KHS-V2` | Versi Current tanpa Effective From (Useful Life `8`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`) dan versi Scheduled Jan 2027 (Useful Life `10`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`), Used By 0 |
| `khsLck` | `KHS-LCK` | Non-building, Useful Life `10`, Straight Line dan Declining Balance, Active, Used By 0, Last Posted Tax Year `2026` (Class Code terkunci) |

- Nilai awal Class Name `KHS-LCK`, `KHS-E1`, dan `KHS-V2` diatur seed; TC tidak menyebutnya dan tidak diasersi.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal dan jam sistem diubah (lihat Temuan untuk QA).

## Test Steps

1. Atur jam server dan jam browser ke `15 Okt 2026 10:00 WIB`

### TC-FA-TDC-217: Edit No-Op dinilai terhadap nilai versi terakhir

2. Ketik Search `KHS-V2`, tekan Enter
3. Klik link Class Code `KHS-V2`
4. Klik `[Save]` tanpa mengubah field (form berisi nilai versi Scheduled)
5. Verifikasi muncul toast info: `No changes to save.`
6. Verifikasi dialog Save Changes (D-09) tidak muncul
7. Klik link Class Code `KHS-V2`
8. Klik tautan `View versions`
9. Verifikasi modal Versions memuat tepat dua versi: Current dan Scheduled `Jan 2027` (tidak ada versi baru)
10. Tutup modal Versions
11. Klik ikon ✕

### TC-FA-TDC-216: Edit Regulation Reference saat versi terakhir adalah versi Scheduled

12. Klik link Class Code `KHS-V2`
13. Ganti Regulation Reference menjadi `PMK 99/2099`
14. Klik `[Save]`
15. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
16. Ganti isi kotak search dengan `PMK 99/2099`, tekan Enter
17. Verifikasi hasil Search tidak menampilkan baris `KHS-V2`
18. Ganti isi kotak search dengan `KHS-V2`, tekan Enter
19. Klik link Class Code `KHS-V2`
20. Klik tautan `View versions`
21. Verifikasi modal Versions: baris `Jan 2027` (Scheduled) memiliki Regulation Reference `PMK 99/2099`
22. Verifikasi modal Versions: baris `—` (Current) tetap memiliki Regulation Reference `UU HPP 7/2021; PMK 72/2023`
23. Tutup modal Versions
24. Klik ikon ✕

### TC-FA-TDC-215: Edit Regulation Reference pada class dengan versi terakhir Current tercermin di Search

25. Ganti isi kotak search dengan `KHS-E1`, tekan Enter
26. Klik link Class Code `KHS-E1`
27. Ganti Regulation Reference menjadi `PMK 99/2099`
28. Klik `[Save]`
29. Tunggu aksi selesai
30. Ganti isi kotak search dengan `PMK 99/2099`, tekan Enter
31. Verifikasi hasil Search menampilkan baris `KHS-E1`
32. Ganti isi kotak search dengan `UU HPP 7/2021; PMK 72/2023`, tekan Enter
33. Verifikasi hasil Search tidak menampilkan baris `KHS-E1`

### TC-FA-TDC-184: Class Name dan Regulation Reference tetap dapat disimpan pada class berkunci

34. Ganti isi kotak search dengan `KHS-LCK`, tekan Enter
35. Klik link Class Code `KHS-LCK`
36. Ganti Class Name menjadi `Kelompok terkunci uji`
37. Ganti Regulation Reference menjadi `PMK 72/2023`
38. Klik `[Save]`
39. Verifikasi muncul toast sukses: `Success, tax depreciation class has been updated.`
40. Verifikasi baris `KHS-LCK` menampilkan Class Name `Kelompok terkunci uji`
41. Verifikasi Class Code baris tetap `KHS-LCK`
42. Pulihkan jam server dan jam browser ke waktu semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 42 mengatur dan memulihkan jam; langkah 2, 18, 25, dan 34 Search kode class agar baris target ada di halaman teramati (R-16, 8b.13); langkah 16, 30, dan 32 adalah Search yang menjadi objek TC-FA-TDC-215 dan TC-FA-TDC-216; langkah 10, 11, 23, dan 24 menutup modal Versions dan Drawer yang bersih; langkah 29 menunggu aksi selesai (8b.8).
- Urutan TC: TC-FA-TDC-217 (No-Op), TC-FA-TDC-216, TC-FA-TDC-215, TC-FA-TDC-184 (S-10). Jam sistem diatur di awal spec karena precondition TC-FA-TDC-216 mensyaratkannya; jam dipulihkan di langkah 42 sebelum selesai.
- Langkah 9 dan 22 (versi dan nilai Regulation Reference): langkah 5 dan 15 (toast) menjadi anchor positif bahwa respons server sudah diproses. Langkah 17 (baris tidak tampil): toast sukses langkah 15 menjadi anchor untuk absence baris sesudah Edit (8b.2). Langkah 33: hasil Search langkah 31 membuktikan Search berfungsi pada surface yang sama (anchor).
- Langkah 7 sampai 9 adalah observasi tambahan untuk Expected b TC-FA-TDC-217 ("tidak ada versi baru"); TC tidak memberi langkahnya (S-03, S-15).
- Alasan spec melewati sekitar 35 langkah: seluruh blok adalah Edit Regulation Reference atau Save pada class milik spec dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah langkah dibentuk `Verifikasi` per klausa (S-01) dan Search pembuka berulang per blok.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-*` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-215 Expected b ("pencarian `UU HPP 7/2021; PMK 72/2023`: baris `KHS-E1` tidak tampil") tidak menyebut baris pembanding lain pada surface yang sama; anchor memakai hasil Search langkah 31 (8b.2). Usul QA: sebut baris seed yang dijamin memuat nilai itu.
  - TC-FA-TDC-216 Expected c: "nilai kolom versi Current tidak berubah" mengasumsikan Search hanya membaca versi Current; spec mengikuti TC.
  - TC-FA-TDC-184 Post Condition (entri log L-02) dan TC-FA-TDC-216 Post Condition ("tidak ada versi baru", sudah teramati lewat Expected b) tidak punya langkah observasi tambahan di TC; entri log tidak diasersi (S-01).
  - TC-FA-TDC-218 pada spec 060 memakai `KHS-LCK` yang sama; tiap spec men-seed ulang class itu.
