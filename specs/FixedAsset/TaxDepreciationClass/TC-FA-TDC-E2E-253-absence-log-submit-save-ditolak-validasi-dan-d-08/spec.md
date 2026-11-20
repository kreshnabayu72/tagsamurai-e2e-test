---
id: TC-FA-TDC-E2E-253-absence-log-submit-save-ditolak-validasi-dan-d-08
title: "Absence Log: Submit dan Save yang Ditolak (Validasi Create dan Edit, Dialog D-08) Tidak Menulis Entri"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-695
  - TC-FA-TDC-696
  - TC-FA-TDC-962
sourceRules: ["V-04", "F-FATDC-01.k1", "§4.2c#b1", "V-05", "L-01", "§8.2#p1", "§8.3#p1", "D-08", "FATDC-LOGIC-10b.1", "F-FATDC-02.k6c", "FATDC-LOGIC-10c", "F-FATDC-02.k6d"]
smoke: []
dependsOn: []
trace:
  "V-04": 10
  "F-FATDC-01.k1": [10, 22]
  "§4.2c#b1": [12, 19, 36]
  "V-05": 17
  "L-01": 22
  "§8.2#p1": 25
  "§8.3#p1": 27
  "D-08": [33, 46]
  "FATDC-LOGIC-10b.1": 33
  "FATDC-LOGIC-10c": 46
  "F-FATDC-02.k6d": 46
  "F-FATDC-02.k6c": 39
coverage:
  web: automated
---

# Absence Log: Submit dan Save yang Ditolak (Validasi Create dan Edit, Dialog D-08) Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser tidak digeser dan tidak dipulihkan: precondition c TC-695, 696, dan 962 ("Tanggal sistem uji 15 Okt 2026") tidak berpengaruh pada validasi dan dialog yang ditolak, sehingga spec tidak memakainya (lihat Temuan untuk QA). Baseline dan entri log dibaca pada waktu nyata.
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Spec absence (kelas g): pemicu validasi Create dan Edit serta dialog D-08 hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5). Tiap TC punya baseline sendiri yang dicatat tepat sebelum pemicu (S-12).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`; nilai dari TC): Kode class milik spec berpola `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol.

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-695 | `KHS-253A` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Active, Used By 0, satu versi tanpa Effective From, Last Posted Tax Year kosong |
| TC-FA-TDC-696 | `KHS-253B` | Straight Line dan Declining Balance; Used By 2 (dua Asset Class memakai Declining Balance) |
| TC-FA-TDC-962 | `KHS-253C` | Straight Line dan Declining Balance; Used By 1 (Asset Class memakai Straight Line pada versi Current dan Declining Balance pada versi Scheduled Jan 2027 Asset Class) |

- Tabel memuat tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah tiga class milik spec (10 baris); baris `KHS-253*` tampil di halaman pertama (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga baris dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` menghapus `KHS-253A`, `KHS-253B`, dan `KHS-253C` lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan sesi.

## Test Steps

### TC-FA-TDC-695: Submit atau Save yang ditolak tidak menulis entri log

1. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
2. Klik `+ Class` di toolbar
3. Isi Class Code `KHS-253A` (duplikat)
4. Isi Class Name `Kelompok log duplikat`
5. Pilih Asset Type `Non-building`
6. Isi Useful Life `8`
7. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
8. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
9. Klik `[Submit]`
10. Verifikasi caption "Class code already exists" muncul di bawah Class Code
11. Klik `[×]` pada Drawer Create
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`
14. Klik link Class Code `KHS-253A` pada tabel
15. Hapus seluruh isi Class Name
16. Klik `[Save]`
17. Verifikasi caption "Class name must not be empty" muncul di bawah Class Name
18. Klik `[×]` pada Drawer Edit
19. Verifikasi dialog `Unsaved Changes` tampil
20. Klik `[Leave]`
21. Klik ikon Changelog di toolbar
22. Verifikasi jumlah entri Changelog sama dengan baseline
23. Tutup Popup Changelog
24. Buka Detail User Rina Puspita > Tab System Log
25. Verifikasi jumlah entri System Log Rina Puspita sama dengan baseline
26. Buka Reports & Logs > Activity Log, tab `User Action`
27. Verifikasi jumlah entri Activity Log sama dengan baseline
28. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-696: Save yang ditolak D-08 tidak menulis entri log

29. Catat baseline jumlah entri Changelog
30. Klik link Class Code `KHS-253B` pada tabel
31. Lepas `Declining Balance` dari Allowed Methods
32. Klik `[Save]`
33. Verifikasi dialog D-08 tampil
34. Klik `[OK]` pada D-08
35. Klik `[×]` pada Drawer Edit
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`
38. Klik ikon Changelog di toolbar
39. Verifikasi jumlah entri Changelog sama dengan baseline
40. Tutup Popup Changelog
41. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-962: Save yang ditolak D-08 karena versi Scheduled Asset Class tidak menulis entri log

42. Catat baseline jumlah entri Changelog
43. Klik link Class Code `KHS-253C` pada tabel
44. Lepas `Declining Balance` dari Allowed Methods
45. Klik `[Save]`
46. Verifikasi dialog D-08 tampil
47. Klik `[OK]` pada D-08
48. Klik `[×]` pada Drawer Edit
49. Verifikasi dialog `Unsaved Changes` tampil
50. Klik `[Leave]`
51. Klik ikon Changelog di toolbar
52. Verifikasi jumlah entri Changelog sama dengan baseline
53. Tutup Popup Changelog
54. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (54 langkah, 41 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 21 sampai 27, 38 sampai 40, 51 sampai 53 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- P-5 (butir a): pemicu validasi Create dan Edit serta dialog D-08 hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya user dan baseline sendiri.
- S-05 dan prinsip 13g: ketiga TC adalah asersi absence atas log dengan aksi nyata dan baseline sendiri (S-12). Anchor positif (8b.2): caption validasi (langkah 10 dan 17) dan dialog D-08 (langkah 33 dan 46). Penutupan form dirty ditulis `[×]`, dialog `Unsaved Changes`, `[Leave]` (S-08).
- Langkah penghubung (S-03): mencatat baseline (langkah 1, 29, 42), menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14).
- Temuan untuk QA:
  - TC-FA-TDC-695 dan 696 mensyaratkan "Tanggal sistem uji 15 Okt 2026" (precondition c) tanpa Expected atau langkah yang bergantung pada tanggal; precondition itu tidak berpengaruh pada validasi atau dialog D-08 dan tidak dipakai spec (jam tidak digeser). Perlu konfirmasi QA apakah precondition c dihapus dari TC.
  - TC-FA-TDC-695 tidak menyebut nilai field valid selain Class Code; spec memakai nilai TC lain (Class Name `Kelompok log duplikat`, Non-building, Useful Life 8, Straight Line dan Declining Balance). Keadaan form sesudah penolakan (Drawer tetap terbuka dengan input dipertahankan) tidak disebut; spec menganggapnya terbuka dan menutupnya lewat `[×]` dan `[Leave]`.
  - TC-FA-TDC-696 memakai kode `KHS-V8`; spec memakai `KHS-253B`. Keadaan Drawer sesudah `[OK]` pada D-08 tidak disebut; spec menganggap Drawer tetap terbuka dengan perubahan dipertahankan.
  - TC-FA-TDC-695, 696, dan 962 memakai kode class literal (`KHS-LG`, `KHS-V8`, `KHS-V15`); spec memakai satu class per TC (S-06, S-12).
  - TC-FA-TDC-962 Expected a dan b (teks dialog D-08, bullet, tombol `[OK]`) diasersi di spec 275 dengan aksi nyata sendiri; spec ini hanya memuat klausa "tidak ada entri log" (Expected c). Precondition c TC-FA-TDC-962 (tanggal sistem uji 15 Okt 2026) tidak dipakai di spec ini, sama dengan TC-FA-TDC-695 dan 696.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
