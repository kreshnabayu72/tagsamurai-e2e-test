---
id: TC-FA-COA-E2E-046-sort-tabel-last-used-last-updated-kolom-tanpa-sort-pindah-kolom-dan-tie
title: "Sort Tabel: Last Used in Journal, Last Updated, Kolom Tanpa Sort, Pindah Kolom, dan Tie-Breaker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-176
  - TC-FA-COA-177
  - TC-FA-COA-178
  - TC-FA-COA-179
  - TC-FA-COA-220
coverage:
  web: automated
---

# Sort Tabel: Last Used in Journal, Last Updated, Kolom Tanpa Sort, Pindah Kolom, dan Tie-Breaker

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hanya dibaca, tidak diubah; disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):

  | Akun | Account Code | Account Name | Function | Status | Last Used in Journal |
  |---|---|---|---|---|---|
  | P1 | `5-6001` | Depreciation Expense – Admin | Depreciation Expense | Active | kosong (`—`) |
  | P2 | `6-2001` | Repairs & Maintenance Expense | Capitalization Offset | Active | `Aug 2026` |
  | P3 | `4-7001` | Gain on Disposal | Gain on Disposal | Inactive | kosong (`—`) |
  | P4 | `1-1002` | Equipment – Legacy Code | Asset Cost | Inactive | `Mar 2025` |
  | P5 | `CAP-6100` | Capitalization Clearing – Repairs | Capitalization Offset | Active | kosong (`—`) |
  | P6 | `5-6002` | Depreciation Expense – Warehouse | Depreciation Expense | Active | kosong (`—`) |
  | P8 | `1-2001` | Accumulated Depreciation – Equipment | Accumulated Depreciation | Active | `Sep 2026` |

- Waktu Last Updated akun P1 lebih awal daripada akun P5 dengan selisih minimal satu menit (precondition c TC-FA-COA-177). Nilai waktunya tidak punya identitas di Pre-setup TC; disediakan tim FE.
- Tabel client default berisi akun P1 sampai P8 dan akun hasil seed lainnya (lebih dari 100 akun; seed P1 sampai P115 disediakan tim FE). Tiap kolom yang di-sort punya sedikitnya dua nilai distinct pada akun P yang diasersi (S-11). Asersi urutan memakai urutan relatif akun P yang disebut di langkah, bukan posisi baris. Ukuran halaman diubah ke 100 pada langkah 1 agar akun P terlihat di satu halaman, diubah ke 10 pada langkah 62 (sesuai precondition d TC-FA-COA-220) dan tetap 10 sampai akhir spec. Asersi nilai kosong "di akhir" dan "di awal" memakai langkah pindah ke halaman terakhir (S-14); akun bernilai Last Used in Journal diasumsikan sedikit (kurang dari satu halaman) sehingga P2 dan P4 berada pada halaman yang sama.
- Kolom Last Used in Journal tampil secara default (asumsi, TC-FA-COA-176 tidak menyebut Setup Column). Kolom Last Updated tidak tampil secara default dan ditampilkan lewat Setup Column pada langkah 17 sampai 18 (precondition d TC-FA-COA-177); langkah 28 sampai 29 memulihkannya (R-24).
- State yang diubah spec: ukuran halaman, kolom Last Updated (ditampilkan lalu disembunyikan lagi), Search dan filter (dilepas di langkah 51), dan sort (tiap siklus berakhir netral). Tidak ada data yang ditulis. Hook `after` menghapus preferensi kolom dan tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan tampilan

1. Ubah jumlah baris per halaman menjadi 100

### TC-FA-COA-176: Sort kolom Last Used in Journal, nilai kosong di akhir saat naik dan di awal saat turun

2. Klik header Last Used in Journal satu kali
3. Verifikasi indikator naik (↑) aktif pada header Last Used in Journal
4. Verifikasi Oldest First: baris akun P4 (`Mar 2025`) tampil di atas baris akun P2 (`Aug 2026`)
5. Pindah ke halaman terakhir
6. Verifikasi baris terakhir tabel memiliki nilai Last Used in Journal kosong (`—`)
7. Pindah ke halaman pertama
8. Klik header Last Used in Journal kedua kali
9. Verifikasi indikator turun (↓) aktif pada header Last Used in Journal
10. Verifikasi baris pertama tabel memiliki nilai Last Used in Journal kosong (`—`)
11. Pindah ke halaman terakhir
12. Verifikasi Newest First: baris akun P2 (`Aug 2026`) tampil di atas baris akun P4 (`Mar 2025`)
13. Pindah ke halaman pertama
14. Klik header Last Used in Journal ketiga kali
15. Verifikasi indikator header Last Used in Journal netral
16. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif P4, P3, P1, P2

### TC-FA-COA-177: Sort siklus tiga tahap pada kolom Last Updated

17. Klik header Actions ⋯ > `Setup Column...`
18. Centang kolom `Last Updated`, klik `[Save]`
19. Klik header Last Updated satu kali
20. Verifikasi indikator naik (↑) aktif pada header Last Updated
21. Verifikasi Oldest First: baris akun P1 tampil di atas baris akun P5
22. Klik header Last Updated kedua kali
23. Verifikasi indikator turun (↓) aktif pada header Last Updated
24. Verifikasi Newest First: baris akun P5 tampil di atas baris akun P1
25. Klik header Last Updated ketiga kali
26. Verifikasi indikator header Last Updated netral
27. Verifikasi urutan kembali ke default Account Code A-Z: baris akun P1 tampil di atas baris akun P5
28. Klik header Actions ⋯ > `Setup Column...`
29. Hilangkan centang kolom `Last Updated`, klik `[Save]`

### TC-FA-COA-178: Kolom checkbox dan Actions tidak memiliki ikon sort

30. Verifikasi urutan baris default Account Code A-Z: urutan relatif P4, P3, P1, P2, P5
31. Verifikasi header kolom checkbox tidak memiliki ikon sort
32. Verifikasi header kolom Actions ⋯ tidak memiliki ikon sort
33. Klik header kolom checkbox
34. Verifikasi urutan baris tidak berubah: urutan relatif P4, P3, P1, P2, P5
35. Klik header kolom Actions ⋯
36. Verifikasi menu Column Visibility terbuka, bukan sort
37. Verifikasi urutan baris tidak berubah: urutan relatif P4, P3, P1, P2, P5
38. Tutup menu Column Visibility dengan menekan Esc

### TC-FA-COA-179: Pindah kolom sort, kolom lama netral, kolom baru mulai dari naik, Search dan Filter tidak direset

39. Ketik Search `Depreciation`, tekan Enter
40. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
41. Klik header Account Name satu kali
42. Klik header Function satu kali
43. Verifikasi indikator Account Name netral
44. Verifikasi indikator naik (↑) aktif pada header Function
45. Verifikasi baris urut A-Z menurut label Function: baris akun P8 (Accumulated Depreciation) tampil di atas baris akun P1 (Depreciation Expense)
46. Verifikasi Search tetap `Depreciation`
47. Verifikasi chip filter Active tetap aktif
48. Verifikasi sedikitnya satu baris tampil di tabel
49. Verifikasi setiap baris tabel berstatus Active
50. Verifikasi setiap baris tabel memuat `Depreciation`
51. Klik `(←)` pada kotak Search, klik `Clear all`, lalu klik header Function dua kali sampai netral

### TC-FA-COA-220: Sort tie-breaker mengikuti default Account Code A-Z dan urutan deterministik antar halaman

52. Klik header Function satu kali
53. Verifikasi indikator naik (↑) aktif pada header Function
54. Verifikasi kelompok Capitalization Offset (P2, P5) mendahului kelompok Depreciation Expense (P1, P6)
55. Verifikasi baris akun P2 mendahului baris akun P5
56. Verifikasi baris akun P1 mendahului baris akun P6
57. Klik header Function kedua kali
58. Verifikasi indikator turun (↓) aktif pada header Function
59. Verifikasi kelompok Depreciation Expense (P1, P6) mendahului kelompok Capitalization Offset (P2, P5)
60. Verifikasi baris akun P1 tetap mendahului baris akun P6
61. Verifikasi baris akun P2 tetap mendahului baris akun P5
62. Ubah jumlah baris per halaman menjadi 10
63. Telusuri seluruh halaman pada sort Function turun dari halaman pertama sampai halaman terakhir dan catat Account Code tiap baris
64. Verifikasi tidak ada akun muncul dua kali antar halaman
65. Verifikasi tidak ada akun terlewat antar halaman
66. Verifikasi jumlah baris seluruh halaman sama dengan total akun pada info paginasi
67. Pindah ke halaman pertama, lalu klik header Function ketiga kali sampai netral

## Notes

- Alasan spec di atas sekitar 35 langkah (67 langkah): lima TC sort satu kelas (Sort) pada satu layar dan satu dataset Pre-setup; tiap blok berupa siklus klik yang berdiri sendiri dan berakhir netral, dan Expected dipecah satu `Verifikasi` per klausa (S-01) termasuk pindah halaman terakhir untuk asersi nilai kosong dan penelusuran seluruh halaman TC-FA-COA-220. Memecahnya mengulang login, pembukaan halaman, dan pengaturan ukuran halaman yang sama.
- Langkah penghubung (S-03, S-09): langkah 1 (ukuran halaman 100 agar akun P terlihat bersama); langkah 5, 7, 11, 13 (pindah halaman untuk asersi "di akhir" dan "di awal", S-14); langkah 17 sampai 18 dan 28 sampai 29 (menampilkan lalu memulihkan kolom Last Updated, R-24 dan 8b.13); langkah 38 (menutup menu Column Visibility); langkah 51 (melepas Search, filter, dan sort sebelum TC berikutnya); langkah 62 (ukuran halaman 10, precondition d TC-FA-COA-220, sekaligus memulihkan ukuran halaman awal); langkah 67 (kembali ke halaman pertama dan sort netral).
- Search pada langkah 39 diketik lalu Enter (8b.9); dikosongkan lewat `(←)` pada langkah 51.
- Tiap siklus sort berakhir netral sehingga tidak ada langkah reset sort tambahan.
- Tidak ada asersi pencatatan/log di spec ini (aksi sort tidak menghasilkan log).
- Temuan untuk QA:
  - TC-FA-COA-176 tidak menyebut ukuran halaman dan menulis "nilai kosong di akhir/di awal" tanpa menyebut halaman. Dengan akun lebih dari 100 baris, spec menafsirkannya sebagai baris terakhir pada halaman terakhir (naik) dan baris pertama pada halaman pertama (turun), serta mengasumsikan P2 dan P4 berada pada halaman terakhir saat sort turun; perlu konfirmasi tim FE tentang jumlah akun bernilai Last Used in Journal.
  - TC-FA-COA-176 tidak menyebut apakah kolom Last Used in Journal tampil secara default; spec mengasumsikan tampil.
  - TC-FA-COA-177 menyebut selisih waktu minimal satu menit antara P1 dan P5 tanpa nilai; Last Updated P1 dan P5 dapat berubah bila spec lain mengedit akun itu; perlu fixture yang menjamin urutan ini.
  - TC-FA-COA-178 langkah 2 ("klik header kolom checkbox") ambigu: header kolom checkbox bisa berfungsi sebagai Select All, sehingga klik dapat memilih baris halaman; TC tidak menyebut hasil seleksi atau pemulihannya. Spec mengikuti TC dan hanya mengasersi urutan; bila klik memilih baris, perlu langkah pembersih seleksi.
  - TC-FA-COA-179 butir a ("urut A-Z menurut label") tidak menyebut data uji; urutan P8 (Accumulated Depreciation) di atas P1 (Depreciation Expense) diturunkan dari Pre-setup dengan asumsi Search `Depreciation` juga mencocokkan Account Name P8. TC juga tidak menyebut kolom Search yang dipakai.
  - TC-FA-COA-220 langkah 3 tidak menyebut arah sort saat penelusuran halaman; spec menelusuri pada sort turun (setelah klik kedua). TC juga tidak menyebut sumber total akun; spec memakai info paginasi.
