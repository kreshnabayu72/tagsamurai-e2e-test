---
id: TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped
title: "Groups List Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, Kolom Hide/Unhide, Node Leaf Header Saja, dan Node Terpilih + Scope Aktor Server-Side"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-407
  - TC-FA-GRP-408
  - TC-FA-GRP-409
  - TC-FA-GRP-410
  - TC-FA-GRP-421
  - TC-FA-GRP-1127
coverage:
  web: automated
---

# Groups List Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, Kolom Hide/Unhide, Node Leaf Header Saja, dan Node Terpilih + Scope Aktor Server-Side

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-127`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-127` | `V127L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-127` | `V127K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-127` | `V127J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-127` | `V127I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-127` | `V127H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-127` | `V127G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-127` | `V127F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-127` | `V127E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-127` | `V127D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-127` | `V127C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-127` | `V127B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-127` | `V127A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-127`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): penangkapan berkas unduhan browser dan pembacaan isi berkas CSV/XLSX (nama berkas, baris header, jumlah baris data).
- N = jumlah seluruh group level 1 client pada Groups List tanpa Search dan filter, dibaca lewat kemampuan baca jumlah (disediakan tim FE/BE) sebelum uji, dipakai untuk asersi jumlah baris berkas pada TC-FA-GRP-407.
- Data Pre-setup (hanya dibaca): Head Office > Floor 2 > Server Room (leaf, tanpa subgroup); Global HQ > Region West > Branch West 1 (Tabel A).
- Akun kedua untuk TC-FA-GRP-421 (ganti akun eksplisit): Group Manager scope Region West (`groupManagerGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 4, `Spectra.env.FA_GM_PASSWORD`; env baru yang didaftarkan tim FE). Hook `after` mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-GRP-407: Download tanpa Search/filter, seluruh data

1. Klik icon Download
2. Klik `Download as CSV`
3. Verifikasi tidak ada toast sukses tampil
4. Verifikasi berkas `Groups.csv` terunduh
5. Verifikasi jumlah baris data berkas `Groups.csv` sama dengan N (seluruh halaman, bukan hanya halaman aktif)

### TC-FA-GRP-408: Download dengan Search dan filter aktif

6. Ketik Search `{runId}-127`, tekan Enter
7. Klik icon Filter
8. Pilih `Assignable` pada dropdown Function
9. Klik [Apply]
10. Klik icon Download
11. Klik `Download as XLSX`
12. Verifikasi tidak ada toast sukses tampil
13. Verifikasi berkas `Groups.xlsx` terunduh
14. Verifikasi berkas `Groups.xlsx` hanya berisi 6 baris data: `Alpha {runId}-127`, `Charlie {runId}-127`, `Echo {runId}-127`, `Golf {runId}-127`, `India {runId}-127`, `Kilo {runId}-127`
15. Verifikasi berkas `Groups.xlsx` tidak memuat baris `bravo {runId}-127`

### TC-FA-GRP-409: Kolom yang di-hide tidak ikut ter-export

16. Klik icon Filter
17. Klik [Clear Field]
18. Klik [Apply]
19. Hide kolom Code lewat Column Visibility (icon `⋯` di header kolom terakhir)
20. Verifikasi kolom Code tidak tampil pada header tabel
21. Klik icon Download
22. Klik `Download as CSV`
23. Verifikasi tidak ada toast atau peringatan tambahan tampil
24. Verifikasi berkas `Groups.csv` terunduh
25. Verifikasi header berkas `Groups.csv` tidak memuat kolom Code dan berurutan Group, Function, Total Asset, Total User, Modified By, Last Updated

### TC-FA-GRP-410: Kolom yang di-unhide kembali ikut ter-export

26. Tampilkan kembali kolom Code lewat Column Visibility
27. Verifikasi kolom Code tampil pada header tabel
28. Klik icon Download
29. Klik `Download as CSV`
30. Verifikasi berkas `Groups.csv` terunduh
31. Verifikasi header berkas `Groups.csv` memuat kolom Code

### TC-FA-GRP-1127: Node leaf kosong, Download berisi header saja

32. Klik `(←)` pada kotak Search
33. Klik expand `Head Office` di sidebar Group Tree
34. Klik expand `Floor 2` di sidebar Group Tree
35. Klik `Server Room` di sidebar Group Tree
36. Verifikasi tabel menampilkan Illustration, title `No subgroup yet`, dan body `This group does not have any subgroups.`
37. Verifikasi Search, Filter, dan Download tetap tampil pada toolbar
38. Klik icon Download
39. Klik `Download as CSV`
40. Verifikasi tidak ada toast sukses tampil
41. Verifikasi berkas `Groups.csv` terunduh
42. Verifikasi berkas `Groups.csv` hanya berisi baris header kolom yang visible, tanpa baris data
43. Klik icon Filter
44. Buka dropdown Function
45. Verifikasi dropdown Function menampilkan teks `No options available`
46. Klik icon Filter untuk menutup panel

### TC-FA-GRP-421: Node terpilih dan scope aktor server-side

47. Ganti akun: logout, lalu login sebagai Group Manager scope Region West dengan `Spectra.env.FA_GM_PASSWORD`
48. Buka Fixed Asset > Settings > Groups
49. Klik `Region West` di sidebar Group Tree
50. Verifikasi group `Branch West 1` tampil pada tabel
51. Klik icon Download
52. Klik `Download as CSV`
53. Verifikasi berkas `Groups.csv` terunduh
54. Verifikasi berkas `Groups.csv` hanya berisi direct children Region West: baris data `Branch West 1`
55. Verifikasi berkas `Groups.csv` tidak memuat baris di luar scope aktor (`Region East`, `Region North`, `Global HQ`)
56. Verifikasi nilai Total Asset dan Total User baris `Branch West 1` pada berkas sama dengan nilai pada tabel

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec, [Clear Field] + [Apply], membuka node di sidebar Group Tree, dan menutup Filter Panel; ganti akun pada TC-FA-GRP-421 ditempatkan paling akhir agar akun aktor tidak berganti di tengah spec, disusul langkah Buka Fixed Asset > Settings > Groups karena hook `beforeEach` tidak jalan sesudah login ulang (S-03, S-07, S-14, R-16).
- Asersi "tidak ada toast sukses" (bagian 8b butir 11) ditulis segera setelah memilih format dan sebelum `Verifikasi` berkas terunduh, termasuk pada TC-FA-GRP-409; pemilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- Isi sel berkas (tipe sel, BOM, escaping) diasersi pada spec kelas f terpisah (spec 128); spec ini hanya mengasersi nama berkas, header, dan jumlah baris (bagian 3 prinsip 13 kelas f).
- TC-FA-GRP-408 memakai filter Function `Assignable` pada dataset; hasil berkas dicocokkan terhadap 6 baris Assignable milik spec.
- Spec 56 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-407: jumlah baris seluruh halaman tidak dapat diturunkan dari seeding karena Pre-setup dan data tambahan lain ikut tampil; N dibaca lewat kemampuan baca jumlah (bagian 8b butir 10).
  - TC-FA-GRP-421 menyebut Group Manager scope Region West tanpa nilai Total Asset/Total User baris `Branch West 1`; spec membandingkan berkas terhadap tabel.
