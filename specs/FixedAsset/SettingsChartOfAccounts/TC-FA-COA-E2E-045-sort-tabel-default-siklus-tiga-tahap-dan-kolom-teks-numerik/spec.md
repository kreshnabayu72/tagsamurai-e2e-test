---
id: TC-FA-COA-E2E-045-sort-tabel-default-siklus-tiga-tahap-dan-kolom-teks-numerik
title: "Sort Tabel: Default, Siklus Tiga Tahap pada Account Name, Account Code, Active, dan Used By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-80
  - TC-FA-COA-182
  - TC-FA-COA-174
  - TC-FA-COA-175
coverage:
  web: automated
---

# Sort Tabel: Default, Siklus Tiga Tahap pada Account Name, Account Code, Active, dan Used By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed dan hapus, termasuk Asset Class pemakai akun untuk Used By, disediakan tim FE/BE, butir "Seed dan pemulihan lewat API" di `suite.md`). Tujuh akun padanan P1 sampai P7 pada precondition TC-FA-COA-80, 174, 175, dan 182. Account Code maksimal 15 karakter sehingga bernilai literal dan memuat nomor spec; Account Name bersuffix `{runId}-045`. Asset Class pemakai akun (nama bersuffix `{runId}-045`) dihapus lebih dulu, lalu akun:

  | Padanan | Account Code | Account Name | Function | Status | Used By |
  |---|---|---|---|---|---|
  | P4 | `DID045A` | `Sort Equipment {runId}-045` | Asset Cost | Inactive | 0 |
  | P3 | `DID045B` | `Sort Gain {runId}-045` | Gain on Disposal | Inactive | 0 |
  | P1 | `DID045C` | `Sort Depresiasi {runId}-045` | Depreciation Expense | Active | 0 |
  | P2 | `DID045D` | `Sort Repairs {runId}-045` | Capitalization Offset | Active | 0 |
  | P5 | `DID045E` | `Sort Clearing {runId}-045` | Capitalization Offset | Active | 0 |
  | P6 | `DID045F` | `Sort Warehouse {runId}-045` | Depreciation Expense | Active | 1 |
  | P7 | `DID045G` | `Sort Loss {runId}-045` | Loss on Disposal | Active | 2 |

- Pengecualian A-18 (butir "Pengecualian A-18" di `suite.md`): Account Code literal `DID045A` sampai `DID045G` hanya dipakai spec ini; seed idempotent dan penghapusan sisa akun dijalankan di hook `before` dan `after`.
- Search `{runId}-045` (langkah 1) membatasi tabel pada tujuh akun milik spec sehingga semuanya tampil di halaman 1 (10 baris per halaman) dan urutan relatif tidak bergantung pada jumlah akun Pre-setup (S-14, R-23). Tiap kolom yang di-sort punya sedikitnya dua nilai distinct pada akun yang diasersi (S-11). Label P1 sampai P7 pada langkah menunjuk akun padanan di atas.
- Urutan relatif yang diasersi: Account Code A-Z P4, P3, P1, P2, P5; Account Name A-Z P5, P1, P4, P3, P2; Used By naik P1, P6, P7.
- State yang diubah spec: isi kotak Search (dikosongkan langkah 39) dan sort kolom (tiap siklus berakhir netral). Ukuran halaman tidak diubah. Hook `after` menghapus preferensi tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan data tampilan

1. Ketik Search `{runId}-045`, tekan Enter

### TC-FA-COA-80: Sort default Account Code A-Z dan siklus sort tiga tahap pada kolom

2. Verifikasi urutan default Account Code A-Z: baris akun P4 `DID045A`, P3 `DID045B`, P1 `DID045C`, P2 `DID045D`, P5 `DID045E` tampil berurutan
3. Klik header Account Name satu kali
4. Verifikasi baris berurut naik menurut Account Name: P5, P1, P4, P3, P2
5. Klik header Account Name kedua kali
6. Verifikasi baris berurut turun menurut Account Name: P2, P3, P4, P1, P5
7. Klik header Account Name ketiga kali
8. Verifikasi header Account Name kembali netral (tanpa indikator sort aktif)

### TC-FA-COA-182: Sort siklus tiga tahap pada kolom Account Code

9. Verifikasi urutan baris mengikuti default Account Code A-Z: urutan relatif P4, P3, P1, P2, P5
10. Verifikasi header Account Code netral (tanpa indikator sort aktif)
11. Klik header Account Code satu kali
12. Verifikasi indikator naik (↑) aktif pada header Account Code
13. Verifikasi urutan A-Z tanpa membedakan huruf besar-kecil: urutan relatif P4, P3, P1, P2, P5
14. Klik header Account Code kedua kali
15. Verifikasi indikator turun (↓) aktif pada header Account Code
16. Verifikasi urutan Z-A: urutan relatif P5, P2, P1, P3, P4
17. Klik header Account Code ketiga kali
18. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif P4, P3, P1, P2, P5
19. Verifikasi header Account Code netral (tanpa indikator sort aktif)
20. Verifikasi tidak ada indikator sort aktif pada kolom lain

### TC-FA-COA-174: Sort siklus tiga tahap pada kolom Active

21. Klik header Active satu kali
22. Verifikasi indikator naik (↑) aktif pada header Active
23. Verifikasi Active First: baris akun P1 (Active) berada di atas baris akun P3 (Inactive)
24. Klik header Active kedua kali
25. Verifikasi indikator turun (↓) aktif pada header Active
26. Verifikasi Inactive First: baris akun P3 (Inactive) berada di atas baris akun P1 (Active)
27. Klik header Active ketiga kali
28. Verifikasi indikator header Active netral
29. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif P4, P3, P1, P2, P5

### TC-FA-COA-175: Sort siklus tiga tahap pada kolom Used By

30. Klik header Used By satu kali
31. Verifikasi indikator naik (↑) aktif pada header Used By
32. Verifikasi urutan numerik dari terkecil: baris akun P1 (0), lalu P6 (1), lalu P7 (2)
33. Klik header Used By kedua kali
34. Verifikasi indikator turun (↓) aktif pada header Used By
35. Verifikasi urutan dari terbesar: baris akun P7 (2), lalu P6 (1), lalu P1 (0)
36. Klik header Used By ketiga kali
37. Verifikasi indikator header Used By netral
38. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif P4, P3, P1, P2, P5

### Pemulihan

39. Klik `(←)` pada kotak Search

## Notes

- Alasan spec di atas sekitar 35 langkah (39 langkah): empat blok sort satu kelas (Sort), satu dataset, tiap blok berupa siklus tiga klik yang berdiri sendiri dan berakhir netral, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected indikator dan urutan dipecah satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (S-03, S-09): langkah 1 (Search `{runId}-045` supaya hanya tujuh akun milik spec tampil; R-16, R-23, 8b.13) dan langkah 39 (mengosongkan Search). Kotak Search tetap berisi `{runId}-045` selama keempat siklus sort; klik header sort tidak mengubah isinya. Tiap siklus sort berakhir netral sehingga tidak ada langkah reset tambahan.
- `A-18`: TC-FA-COA-182 memakai Account Code `DID045A` sampai `DID045E` sebagai objek asersi urutan (akun milik spec, Name bersuffix `{runId}-045`); seed idempotent dan penghapusan sisa di hook `before` dan `after`.
- Asersi urutan memakai urutan relatif akun yang diturunkan dari data seed spec (nama, kode, status, Used By); TC-FA-COA-80 hanya menulis "urut naik/turun/netral".
- Tidak ada asersi pencatatan/log di spec ini (aksi sort tidak menghasilkan log).
- Temuan untuk QA:
  - TC-FA-COA-80, 174, 175, 182 menyebut P1 sampai P7 di antara lebih dari seratus akun Pre-setup (P1 sampai P117), sedangkan ukuran halaman default 10 dan tabel tidak menjamin akun P berada di satu halaman pada sort Name, Code Z-A, Active, atau Used By; spec memakai tujuh akun padanan milik spec dan Search awalan nama bersama tanpa mengubah Expected TC. Used By 1 dan 2 membutuhkan Asset Class pemakai akun yang di-seed hook (kemampuan disediakan tim FE/BE).
  - TC-FA-COA-80 butir b tidak menyebut data uji urutan Account Name; urutan relatif P5, P1, P4, P3, P2 diturunkan dari nama seed spec.
  - TC-FA-COA-182 butir b menyebut "tanpa membedakan huruf besar-kecil" tetapi data tidak memuat kode huruf kecil; asersi hanya mengonfirmasi urutan relatif.
