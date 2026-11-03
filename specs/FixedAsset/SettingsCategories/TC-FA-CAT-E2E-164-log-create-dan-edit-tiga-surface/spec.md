---
id: TC-FA-CAT-E2E-164-log-create-dan-edit-tiga-surface
title: "Log Create dan Edit Category pada Tiga Surface (Changelog, System Log, Activity Log): Create Root, Add Subcategory, Edit Name, Edit Code, dan Edit Description"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-458
  - TC-FA-CAT-459
  - TC-FA-CAT-460
  - TC-FA-CAT-461
  - TC-FA-CAT-462
coverage:
  web: automated
---

# Log Create dan Edit Category pada Tiga Surface (Changelog, System Log, Activity Log): Create Root, Add Subcategory, Edit Name, Edit Code, dan Edit Description

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain) hanya sebagai konteks client; target Create dan Edit memakai data milik spec (S-06).
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; semua dibersihkan hook `after`, termasuk kategori yang dibuat spec):
  - `Log Parent {runId}-164` (Code `LP164`, leaf): parent Add Subcategory (langkah 12).
  - `Vehicle Log Awal {runId}-164` (Code `VL164`, leaf, Total Asset 0): target Edit Category Name (langkah 23).
  - `Code Edit {runId}-164` (Code `VEH164`, leaf, Total Asset 0): target Edit Code (langkah 31).
  - `Desc Edit {runId}-164` (Description kosong, leaf, Total Asset 0): target Edit Description (langkah 39).
  - Data Dinamis yang dibuat spec: `Log Create {runId}-164` (Code `LGC164`, Description `Deskripsi Log Create`) pada langkah 1 sampai 3 dan `Log Child {runId}-164` pada langkah 12 sampai 14.
- Nama kategori bersuffix unik sehingga baseline jumlah baris Changelog, System Log, dan Activity Log untuk tiap nama adalah nol (S-12). Pengecualian: jumlah baris dengan Category Name tepat `Log Parent {runId}-164` pada System Log dan Activity Log dicatat sebagai baseline pada langkah 11 karena seed parent dapat menulis baris sendiri.
- Kemampuan teknis: membuka Modal Changelog (filter Category Name), Detail User aktor > Tab System Log, dan Activity Log serta mencari baris berdasarkan nama kategori; mekanisme pencarian di tiga surface tidak diuraikan TC dan disediakan tim FE/BE tanpa endpoint karangan. Kolom Modified By diasersi berformat `[First Name] [Last Initial]` aktor Total Control.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-458: Log Create, tiga surface menulis satu baris Category Name

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Log Create {runId}-164`, Code `LGC164`, dan Description `Deskripsi Log Create`
3. Klik `[Submit]`
4. Buka Modal Changelog dan filter Category Name `Log Create {runId}-164`
5. Verifikasi Changelog menulis tepat satu baris: Action `Create`, Field `Category Name`, Old Value `—`, New Value `Log Create {runId}-164`, Category Name `Log Create {runId}-164`, Modified By aktor
6. Verifikasi Changelog tidak memuat baris Field `Code` atau `Description` untuk `Log Create {runId}-164`
7. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Log Create {runId}-164`
8. Verifikasi System Log aktor memuat baris yang sama dengan Object `Categories` dan Name `Log Create {runId}-164`
9. Buka Activity Log dan cari baris `Log Create {runId}-164`
10. Verifikasi Activity Log memuat baris yang sama dengan Modified By aktor

### TC-FA-CAT-459: Log Create untuk Add Subcategory memuat path lengkap parent

11. Catat baseline jumlah baris dengan Category Name tepat `Log Parent {runId}-164` pada System Log aktor dan Activity Log
12. Klik elipsis (⋯) pada baris `Log Parent {runId}-164` > `+ Add Subcategory`
13. Isi Category Name `Log Child {runId}-164`
14. Klik `[Submit]`
15. Buka Modal Changelog dan filter Category Name `Log Child {runId}-164`
16. Verifikasi Changelog memuat baris Create Field `Category Name` Old Value `—` New Value `Log Child {runId}-164` dengan kolom Category Name `Log Parent {runId}-164 › Log Child {runId}-164`
17. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Log Child {runId}-164`
18. Verifikasi System Log aktor memuat baris yang sama
19. Verifikasi jumlah baris dengan Category Name tepat `Log Parent {runId}-164` pada System Log aktor sama dengan baseline langkah 11
20. Buka Activity Log dan cari baris `Log Child {runId}-164`
21. Verifikasi Activity Log memuat baris yang sama
22. Verifikasi jumlah baris dengan Category Name tepat `Log Parent {runId}-164` pada Activity Log sama dengan baseline langkah 11

### TC-FA-CAT-460: Log Edit Category Name pada tiga surface

23. Klik elipsis (⋯) pada baris `Vehicle Log Awal {runId}-164` > `Edit`
24. Ubah Category Name menjadi `Vehicle Log {runId}-164`, lalu klik `[Save]`
25. Buka Modal Changelog dan filter Category Name `Vehicle Log {runId}-164`
26. Verifikasi Changelog menulis tepat satu baris: Action `Edit`, Field `Category Name`, Old Value `Vehicle Log Awal {runId}-164`, New Value `Vehicle Log {runId}-164`, Category Name `Vehicle Log {runId}-164`, Modified By aktor
27. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Vehicle Log {runId}-164`
28. Verifikasi System Log aktor memuat baris yang sama dengan Object `Categories` dan Name `Vehicle Log {runId}-164`
29. Buka Activity Log dan cari baris `Vehicle Log {runId}-164`
30. Verifikasi Activity Log memuat baris yang sama dengan Modified By aktor

### TC-FA-CAT-461: Log Edit Code pada tiga surface

31. Klik elipsis (⋯) pada baris `Code Edit {runId}-164` > `Edit`
32. Ubah Code `VEH164` menjadi `VEH164-2`, lalu klik `[Save]`
33. Buka Modal Changelog dan filter Category Name `Code Edit {runId}-164`
34. Verifikasi Changelog menulis tepat satu baris: Action `Edit`, Field `Code`, Old Value `VEH164`, New Value `VEH164-2`, Category Name `Code Edit {runId}-164`, Modified By aktor
35. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Code Edit {runId}-164`
36. Verifikasi System Log aktor memuat baris yang sama dengan Object `Categories` dan Name `Code Edit {runId}-164`
37. Buka Activity Log dan cari baris `Code Edit {runId}-164`
38. Verifikasi Activity Log memuat baris yang sama dengan Modified By aktor

### TC-FA-CAT-462: Log Edit Description pada tiga surface

39. Klik elipsis (⋯) pada baris `Desc Edit {runId}-164` > `Edit`
40. Ubah Description dari kosong menjadi `Log desc {runId}-164`, lalu klik `[Save]`
41. Buka Modal Changelog dan filter Category Name `Desc Edit {runId}-164`
42. Verifikasi Changelog menulis tepat satu baris: Action `Edit`, Field `Description`, Old Value `—`, New Value `Log desc {runId}-164`, Category Name `Desc Edit {runId}-164`, Modified By aktor
43. Tutup Modal Changelog, buka Detail User aktor > Tab System Log, dan cari baris Name `Desc Edit {runId}-164`
44. Verifikasi System Log aktor memuat baris yang sama dengan Object `Categories` dan Name `Desc Edit {runId}-164`
45. Buka Activity Log dan cari baris `Desc Edit {runId}-164`
46. Verifikasi Activity Log memuat baris yang sama dengan Modified By aktor

## Notes

- Spec melewati sekitar 35 langkah (46). Alasan: lima blok TC satu kelas (pencatatan log tiga surface) yang berdiri sendiri; 30 langkah di antaranya adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung terhadap ambang (prinsip 13 bagian 3), sehingga langkah di luar blok itu sekitar 16.
- Langkah penghubung (S-03, S-09, R-16): langkah 4, 7, 9, 15, 17, 20, 25, 27, 29, 33, 35, 37, 41, 43, 45 (membuka surface dan mencari entri berdasarkan nama kategori), langkah 11 (baseline).
- Langkah 6 (tidak ada baris Field `Code` atau `Description`) diasersi sebagai jumlah pada nama bersuffix unik dengan anchor baris Create langkah 5 (bukan asersi absence kelas g; S-05). Langkah 19 dan 22 adalah asersi jumlah dengan baseline langkah 11.
- Langkah 2 mengisi Description sehingga Expected d TC-FA-CAT-458 ("Code dan Description yang diisi saat Create tidak menulis baris tersendiri") teramati; TC hanya menyebut Code pada langkah 1.
- Data milik spec menggantikan `Vehicle`, `Furniture`, dan `Peripheral` Pre-setup yang disebut TC (S-06).
- TC log lain: Edit Code kosong, Delete, cascade, dan Wizard ada di spec 165; hasil Import dan Fallback T-0 di spec 166; asersi tanpa pencatatan di spec 167.
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-458 sampai 462 menyebut "Buka ... Detail User aktor > Tab System Log, dan Activity Log" tanpa menjelaskan navigasi dan pencarian baris di tiga surface; spec mencari baris berdasarkan nama kategori sebagai kemampuan yang disediakan tim FE/BE.
  - TC-FA-CAT-459 Expected b ("tidak ada baris untuk parent `Peripheral`") tidak menyebut baseline; spec memakai parent milik spec dan baseline jumlah baris (langkah 11).
  - TC-FA-CAT-459 hanya menyebut Modal Changelog dengan kolom Category Name `Peripheral › Log Child`; spec memakai path `Log Parent {runId}-164 › Log Child {runId}-164`.
