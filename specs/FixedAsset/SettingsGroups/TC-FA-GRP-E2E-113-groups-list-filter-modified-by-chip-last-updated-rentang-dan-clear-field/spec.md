---
id: TC-FA-GRP-E2E-113-groups-list-filter-modified-by-chip-last-updated-rentang-dan-clear-field
title: "Groups List Filter: Chip Opsi Modified By, Rentang Last Updated, dan [Clear Field]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-360
  - TC-FA-GRP-361
  - TC-FA-GRP-362
  - TC-FA-GRP-364
coverage:
  web: automated
---

# Groups List Filter: Chip Opsi Modified By, Rentang Last Updated, dan [Clear Field]

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-113`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-113` | `V113L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-113` | `V113K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-113` | `V113J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-113` | `V113I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-113` | `V113H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-113` | `V113G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-113` | `V113F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-113` | `V113E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-113` | `V113D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-113` | `V113C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-113` | `V113B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-113` | `V113A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-113`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Spec ini tidak membatasi tabel dengan Search suffix, kecuali Search nama baris sebelum asersi baris pada TC-FA-GRP-362. Format tanggal input Last Updated mengikuti Date Format General Settings akun aktor (dibaca sebelum uji; spec tidak mengubahnya). `Default Group` (Pre-setup Tabel A) punya Last Updated waktu onboarding client, di luar rentang hari ini.

## Test Steps

### TC-FA-GRP-364: [Clear Field] mengosongkan seluruh field

1. Catat nama baris halaman 1 tabel sebelum filter
2. Klik icon Filter
3. Pilih `Assignable` pada dropdown Function
4. Isi Total Asset Min `5` dan Max `20`
5. Klik [Apply]
6. Klik icon Filter
7. Klik [Clear Field]
8. Verifikasi field Function kosong dengan placeholder `All functions`
9. Verifikasi field Total Asset kosong dengan placeholder `Min` dan `Max`
10. Verifikasi field Total User kosong dengan placeholder `Min` dan `Max`
11. Verifikasi field Modified By kosong dengan placeholder `All users`
12. Verifikasi field Last Updated kosong dengan placeholder `Select date`
13. Klik [Apply]
14. Verifikasi tabel kembali menampilkan seluruh data: nama baris halaman 1 sama dengan yang dicatat pada langkah 1

### TC-FA-GRP-360: Chip opsi Modified By dihapus via (X)

15. Klik icon Filter
16. Centang opsi `ModA` lalu opsi `ModB` pada dropdown Modified By
17. Tutup dropdown Modified By
18. Verifikasi chip `ModA` dan chip `ModB` tampil di dalam field Modified By (chip `ModB` tidak menggantikan chip `ModA`)
19. Klik (X) pada chip `ModA`
20. Verifikasi chip `ModA` hilang dari field Modified By
21. Buka dropdown Modified By
22. Verifikasi checkbox opsi `ModA` ter-uncheck
23. Verifikasi chip `ModB` tetap ada
24. Tutup dropdown Modified By
25. Klik [Apply]
26. Verifikasi sedikitnya satu baris tampil pada tabel
27. Verifikasi baris `Kilo {runId}-113` tampil dan baris `Alpha {runId}-113` tidak tampil (Modified By = `ModB`)

### TC-FA-GRP-361: Chip opsi Modified By dihapus via uncheck di dropdown

28. Klik icon Filter
29. Klik [Clear Field]
30. Centang opsi `ModA` lalu opsi `ModB` pada dropdown Modified By
31. Buka lagi dropdown Modified By dan hilangkan centang opsi `ModA`
32. Verifikasi chip `ModA` hilang dari field Modified By
33. Verifikasi chip `ModB` tetap ada
34. Klik [Apply]
35. Verifikasi baris `Kilo {runId}-113` tampil dan baris `Alpha {runId}-113` tidak tampil (Modified By = `ModB`)

### TC-FA-GRP-362: Filter Last Updated rentang tanggal

36. Klik icon Filter
37. Klik [Clear Field]
38. Buka date range picker Last Updated, pilih tanggal awal = hari ini - 1 dan tanggal akhir = hari ini
39. Klik [Apply]
40. Verifikasi sedikitnya satu baris tampil pada tabel
41. Ketik Search `Alpha {runId}-113`, tekan Enter
42. Verifikasi baris `Alpha {runId}-113` tampil (Last Updated hari ini, batas akhir inklusif)
43. Ganti isi kotak Search dengan `Default Group`, tekan Enter
44. Verifikasi baris `Default Group` tidak tampil (Last Updated di luar rentang)
45. Klik icon Filter
46. Ubah rentang Last Updated: tanggal awal = tanggal akhir = hari ini
47. Verifikasi teks tanggal pada input Last Updated mengikuti Date Format General Settings
48. Klik [Apply]
49. Ganti isi kotak Search dengan `Alpha {runId}-113`, tekan Enter
50. Verifikasi baris `Alpha {runId}-113` tampil (hari itu saja)
51. Ganti isi kotak Search dengan `Default Group`, tekan Enter
52. Verifikasi baris `Default Group` tidak tampil (hari itu saja)
53. Klik `(←)` pada kotak Search
54. Klik icon Filter
55. Klik [Clear Field]
56. Klik [Apply]

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mencatat nama baris halaman 1 (langkah 1), membuka Filter Panel dan dropdown, menutup dropdown, dan [Clear Field] + [Apply] antar TC (S-03, S-09), serta Search nama bersuffix atau `Default Group` sebelum asersi baris pada TC-FA-GRP-362 karena client punya lebih dari 10 node level 1 dan page size 10, sehingga baris target tidak diandalkan berada di halaman 1 (S-03, R-16).
- Opsi A = `ModA` dan opsi B = `ModB` ditentukan spec. Nilai kombinasi Function/Total Asset pada TC-FA-GRP-364 ditentukan spec karena TC hanya menyebut "isi Function dan Total Asset".
- Rentang tanggal TC-FA-GRP-362 memakai tanggal relatif hari uji (hari ini - 1 s.d. hari ini); TC tidak menyebut tanggal.
- Spec 56 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
