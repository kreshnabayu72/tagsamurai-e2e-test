---
id: TC-FA-TDC-E2E-191-log-l-03-old-value-strip-penggantian-versi-dan-record-scheduled
title: "Pencatatan Log L-03 dan L-11: Old Value Effective From Strip, Penggantian Versi dengan Effective From Sama, dan Record Scheduled"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-685
  - TC-FA-TDC-686
  - TC-FA-TDC-687
sourceRules: ["L-03", "FATDC-LOGIC-04b.1", "FATDC-LOGIC-04ac", "§4.1.1#r31", "E-FATDC-19", "F-FATDC-02.k8", "FATDC-LOGIC-04u.2", "FATDC-LOGIC-04f.3", "L-11", "§4.1.1#r27", "§8.2#p1", "§8.2#r1", "§8.3#p1"]
smoke: []
dependsOn: []
trace:
  "L-03": [8, 9, 19, 20, 34, 39, 43]
  "FATDC-LOGIC-04b.1": 8
  "FATDC-LOGIC-04ac": [9, 33]
  "§4.1.1#r31": [9, 20, 33]
  "E-FATDC-19": [19, 20, 21]
  "F-FATDC-02.k8": [21, 22]
  "FATDC-LOGIC-04u.2": 22
  "FATDC-LOGIC-04f.3": 22
  "L-11": [32, 33, 34, 37, 38, 39, 41, 42, 43]
  "§4.1.1#r27": 33
  "§8.2#p1": 37
  "§8.2#r1": 38
  "§8.3#p1": [41, 42]
coverage:
  web: automated
---

# Pencatatan Log L-03 dan L-11: Old Value Effective From Strip, Penggantian Versi dengan Effective From Sama, dan Record Scheduled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before` dan dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`; nilai dari TC): Kode class milik spec berpola `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol.

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-685 | `KHS-191A` | Class Name `Kelompok log uji`; satu versi tanpa Effective From, Useful Life 8; Used By 0 |
| TC-FA-TDC-686 | `KHS-191B` | Class Name `Kelompok log uji`; Non-building; versi Current Effective From Jan 2026 dengan Useful Life 10; Used By 0 |
| TC-FA-TDC-687 | `KHS-191C` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`; satu versi tanpa Effective From; Used By 0 |

- Tabel memuat tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah class milik spec; baris `KHS-*` tampil di halaman pertama (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga baris dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` menghapus `KHS-191A`, `KHS-191B`, dan `KHS-191C` lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan jam serta sesi.

## Test Steps

### TC-FA-TDC-685: Log L-03: Old Value Effective From bernilai — bila versi Current sebelumnya adalah versi pertama

1. Catat baseline jumlah entri Changelog
2. Klik link Class Code `KHS-191A` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Pilih Effective From `Jan 2026`
6. Klik `[Apply]` hingga versi berhasil tersimpan
7. Klik ikon Changelog di toolbar
8. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
9. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-191A" | Field "Effective From" | Old Value "—" | New Value "Jan 2026" | Modified By "Rina P"
10. Tutup Popup Changelog
11. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-686: Log L-03: penggantian versi Current dengan Effective From sama tidak menulis baris Effective From

12. Catat baseline jumlah entri Changelog
13. Klik link Class Code `KHS-191B` pada tabel
14. Ganti Useful Life menjadi `12`
15. Klik `[Save]`
16. Pilih Effective From `Jan 2026`
17. Klik `[Apply]` hingga versi berhasil tersimpan
18. Klik ikon Changelog di toolbar
19. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline (tepat satu baris)
20. Verifikasi Changelog, Dicatat: Action "Edit" | Field "Useful Life" | Old Value "10" | New Value "12"
21. Verifikasi tidak ada baris Field "Effective From" di Changelog (nilainya tidak berubah, Jan 2026 tetap Jan 2026)
22. Verifikasi tidak ada baris L-09 maupun L-11 di Changelog (versi yang digantikan berstatus Current)
23. Tutup Popup Changelog
24. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-687: Log L-11: versi Scheduled dicatat sebagai record baru dengan Class Code memuat Effective From di Changelog

25. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
26. Klik link Class Code `KHS-191C` pada tabel
27. Ganti Useful Life menjadi `10`
28. Klik `[Save]`
29. Pilih Effective From `Jan 2027`
30. Klik `[Apply]` hingga versi berhasil tersimpan
31. Klik ikon Changelog di toolbar
32. Verifikasi jumlah entri Changelog bertambah tepat 4 dari baseline
33. Verifikasi Changelog, Dicatat: empat baris Action "Create" | Class Code "KHS-191C (Jan 2027)" | Old Value "—" | Modified By "Rina P" untuk Field "Regulation Reference" (New Value "UU HPP 7/2021; PMK 72/2023"), "Useful Life" (New Value "10"), "Allowed Methods" (New Value "Straight Line · Declining Balance"), dan "Effective From" (New Value "Jan 2027")
34. Verifikasi tidak ada baris L-03 (Action "Edit") untuk Apply ini di Changelog
35. Tutup Popup Changelog
36. Buka Detail User Rina Puspita > Tab System Log
37. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 4 dari baseline
38. Verifikasi System Log Rina Puspita, Dicatat: empat baris Action "Create" | Object "Tax Depreciation Class" | Name "KHS-191C" (tanpa "(Jan 2027)") untuk keempat Field yang sama
39. Verifikasi tidak ada baris L-03 (Action "Edit") untuk Apply ini di System Log Rina Puspita
40. Buka Reports & Logs > Activity Log, tab `User Action`
41. Verifikasi jumlah entri Activity Log bertambah tepat 4 dari baseline
42. Verifikasi Activity Log FAMS, Dicatat: empat baris Action "Create" | Object "Tax Depreciation Class" | Name "KHS-191C" | Modified By "Rina P" untuk keempat Field yang sama
43. Verifikasi tidak ada baris L-03 (Action "Edit") untuk Apply ini di Activity Log
44. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (44 langkah, 21 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 7 sampai 10, 18 sampai 23, 31 sampai 43 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Langkah penghubung (S-03): mencatat baseline, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- TC-FA-TDC-685 dan 686 hanya menyebut Changelog; System Log dan Activity Log tidak dibaca. Selisih jumlah entri (2 pada TC-685, 1 pada TC-686) adalah dasar membaca baris baru (S-12); TC-685 tidak menyebut jumlah, spec memakai pola L-03 (Useful Life dan Effective From).
- Klausa "tidak ada baris" (TC-FA-TDC-686 b, TC-FA-TDC-687 d) ditulis sesudah baris yang dicatat pada surface yang sama sebagai anchor (8b.2); selisih jumlah entri tepat sama dengan jumlah baris yang diasersi.
- Temuan untuk QA:
  - TC-FA-TDC-685 sampai 687 memakai satu Class Code `KHS-LG` untuk tiga keadaan; spec memakai satu class per TC (S-06, S-12).
  - TC-FA-TDC-685 dan 686 tidak menyebut Date pada Expected; tidak diasersi. TC-FA-TDC-686 tidak menyebut Modified By.
  - TC-FA-TDC-687 menyebut keempat baris L-11 untuk Field "Regulation Reference" tanpa Old Value dan New Value pada baris lain; spec mengikuti precondition TC.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
