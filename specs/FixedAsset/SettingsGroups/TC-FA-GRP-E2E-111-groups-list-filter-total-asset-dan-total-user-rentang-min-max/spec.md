---
id: TC-FA-GRP-E2E-111-groups-list-filter-total-asset-dan-total-user-rentang-min-max
title: "Groups List Filter Total Asset dan Total User: Rentang Min-Max dan Hanya Min atau Hanya Max"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-352
  - TC-FA-GRP-353
  - TC-FA-GRP-354
  - TC-FA-GRP-355
coverage:
  web: automated
---

# Groups List Filter Total Asset dan Total User: Rentang Min-Max dan Hanya Min atau Hanya Max

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-111`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-111` | `V111L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-111` | `V111K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-111` | `V111J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-111` | `V111I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-111` | `V111H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-111` | `V111G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-111` | `V111F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-111` | `V111E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-111` | `V111D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-111` | `V111C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-111` | `V111B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-111` | `V111A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-111`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).

## Test Steps

1. Ketik Search `{runId}-111`, tekan Enter

### TC-FA-GRP-352: Total Asset rentang Min-Max

2. Klik icon Filter
3. Isi Total Asset Min `1` dan Max `10`
4. Klik [Apply]
5. Verifikasi sedikitnya satu baris tampil pada tabel
6. Verifikasi baris `Golf {runId}-111` (Total Asset 1) dan `Charlie {runId}-111` (Total Asset 10) tampil (batas inklusif)
7. Verifikasi baris `Echo {runId}-111` (Total Asset 25) dan `bravo {runId}-111` (Total Asset 0) tidak tampil
8. Klik icon Filter
9. Ubah Total Asset Min dan Max menjadi `13`
10. Klik [Apply]
11. Verifikasi baris `India {runId}-111` (Total Asset 13) tampil
12. Verifikasi baris `Charlie {runId}-111` tidak tampil

### TC-FA-GRP-353: Total Asset hanya Min atau hanya Max

13. Klik icon Filter
14. Isi hanya Total Asset Min `5` (Max dikosongkan)
15. Klik [Apply]
16. Verifikasi baris `Charlie {runId}-111` (Total Asset 10) dan `Echo {runId}-111` (Total Asset 25) tampil
17. Verifikasi baris `Alpha {runId}-111` (Total Asset 2) tidak tampil
18. Klik icon Filter
19. Kosongkan Total Asset Min dan isi hanya Max `0`
20. Klik [Apply]
21. Verifikasi baris `bravo {runId}-111` (Total Asset 0) tampil
22. Verifikasi seluruh baris yang tampil bernilai Total Asset 0 (baris `Alpha {runId}-111` tidak tampil)

### TC-FA-GRP-354: Total User rentang Min-Max

23. Klik icon Filter
24. Klik [Clear Field]
25. Isi Total User Min `1` dan Max `10`
26. Klik [Apply]
27. Verifikasi sedikitnya satu baris tampil pada tabel
28. Verifikasi baris `Alpha {runId}-111` (Total User 4) dan `juliet {runId}-111` (Total User 7) tampil
29. Verifikasi baris `Echo {runId}-111` (Total User 12) tidak tampil
30. Klik icon Filter
31. Ubah Total User Min dan Max menjadi `12`
32. Klik [Apply]
33. Verifikasi baris `Echo {runId}-111` (Total User 12) tampil
34. Verifikasi baris `Alpha {runId}-111` tidak tampil

### TC-FA-GRP-355: Total User hanya Min atau hanya Max

35. Klik icon Filter
36. Isi hanya Total User Min `5` (Max dikosongkan)
37. Klik [Apply]
38. Verifikasi baris `Charlie {runId}-111` (Total User 5) dan `Echo {runId}-111` (Total User 12) tampil
39. Verifikasi baris `bravo {runId}-111` (Total User 3) tidak tampil
40. Klik icon Filter
41. Kosongkan Total User Min dan isi hanya Max `0`
42. Klik [Apply]
43. Verifikasi empty state tampil dengan Illustration, title `No results found`, dan body `Try adjusting your search or filter.`
44. Klik icon Filter
45. Klik [Clear Field]
46. Klik [Apply]
47. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec di awal, membuka Filter Panel dan dropdown, menutup dropdown, serta [Clear Field] + [Apply] dan `(←)` pada kotak Search sebagai pemulihan state antar TC (S-03, S-09, R-16).
- Nilai Min `5` dan nilai tepat Min = Max (`13`, `12`) dipilih spec dari dataset sesuai kebutuhan TC ("nilai tepat salah satu baris"); Min `1` Max `10` mengikuti Data Uji TC-FA-GRP-352 dan 354.
- Asersi "Total User tidak pernah 0" diamati dari empty state pada Max `0` (TC-FA-GRP-355).
- Spec 47 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
