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
- Data Pre-setup (hanya dibaca, tidak diubah; disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):

  | Akun | Account Code | Account Name | Function | Status | Used By |
  |---|---|---|---|---|---|
  | P1 | `5-6001` | Depreciation Expense – Admin | Depreciation Expense | Active | 0 |
  | P2 | `6-2001` | Repairs & Maintenance Expense | Capitalization Offset | Active | 0 |
  | P3 | `4-7001` | Gain on Disposal | Gain on Disposal | Inactive | 0 |
  | P4 | `1-1002` | Equipment – Legacy Code | Asset Cost | Inactive | 0 |
  | P5 | `CAP-6100` | Capitalization Clearing – Repairs | Capitalization Offset | Active | 0 |
  | P6 | `5-6002` | Depreciation Expense – Warehouse | Depreciation Expense | Active | 1 |
  | P7 | `4-7002` | Gain and Loss on Disposal | Loss on Disposal | Active | 2 |

- Tabel client default berisi akun P1 sampai P7 dan akun hasil seed lainnya (lebih dari 10 akun). Tiap kolom yang di-sort punya sedikitnya dua nilai distinct pada akun P yang diasersi (S-11). Asersi urutan memakai urutan relatif akun P yang disebut di langkah, bukan posisi baris di halaman; ukuran halaman diubah ke 100 pada langkah 1 agar akun P terlihat di satu halaman, dan dipulihkan ke 10 pada langkah 39.
- Urutan relatif yang diasersi (diturunkan dari data di atas): Account Code A-Z P4, P3, P1, P2, P5; Account Name A-Z P5, P1, P4, P3, P2; Used By naik P1, P6, P7.
- State yang diubah spec: ukuran halaman (langkah 1, dipulihkan langkah 39) dan sort kolom (tiap siklus berakhir netral). Tidak ada data yang ditulis. Hook `after` menghapus preferensi tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan tampilan

1. Ubah jumlah baris per halaman menjadi 100

### TC-FA-COA-80: Sort default Account Code A-Z dan siklus sort tiga tahap pada kolom

2. Verifikasi urutan default Account Code A-Z: baris akun P4 `1-1002`, P3 `4-7001`, P1 `5-6001`, P2 `6-2001`, P5 `CAP-6100` tampil berurutan
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

39. Ubah jumlah baris per halaman kembali menjadi 10

## Notes

- Alasan spec di atas sekitar 35 langkah (39 langkah): empat blok sort satu kelas (Sort), satu dataset, tiap blok berupa siklus tiga klik yang berdiri sendiri dan berakhir netral, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected indikator dan urutan dipecah satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (S-03, S-09): langkah 1 (ukuran halaman 100 agar akun P terlihat bersama) dan langkah 39 (memulihkan ukuran halaman). Tiap siklus sort berakhir netral sehingga tidak ada langkah reset tambahan.
- Asersi urutan memakai urutan relatif akun P yang diturunkan dari data Pre-setup (nama, kode, status, Used By); TC-FA-COA-80 hanya menulis "urut naik/turun/netral".
- Tidak ada asersi pencatatan/log di spec ini (aksi sort tidak menghasilkan log).
- Temuan untuk QA:
  - TC-FA-COA-80, 174, 175, 182 tidak menyebut ukuran halaman. Dengan total akun Pre-setup P1 sampai P115 (lebih dari 100 baris) akun P mungkin tidak seluruhnya berada di halaman 1 pada sort Active atau Used By; spec memakai ukuran halaman 100 dan mengasumsikan akun P terlihat bersama; perlu konfirmasi tim FE tentang urutan baris seed.
  - TC-FA-COA-80 butir b tidak menyebut data uji urutan Account Name; urutan relatif P5, P1, P4, P3, P2 diturunkan dari nama Pre-setup.
  - TC-FA-COA-182 butir b menyebut "tanpa membedakan huruf besar-kecil" tetapi data P1 sampai P5 tidak memuat kode huruf kecil; asersi hanya mengonfirmasi urutan relatif.
