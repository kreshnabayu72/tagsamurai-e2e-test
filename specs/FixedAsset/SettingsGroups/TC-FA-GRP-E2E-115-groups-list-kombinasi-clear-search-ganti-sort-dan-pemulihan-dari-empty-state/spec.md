---
id: TC-FA-GRP-E2E-115-groups-list-kombinasi-clear-search-ganti-sort-dan-pemulihan-dari-empty-state
title: "Groups List Kombinasi: Clear Search Saat Filter/Sort Aktif, Ganti Target Sort Saat Search/Filter Aktif, dan Pemulihan dari Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-377
  - TC-FA-GRP-378
  - TC-FA-GRP-379
coverage:
  web: automated
---

# Groups List Kombinasi: Clear Search Saat Filter/Sort Aktif, Ganti Target Sort Saat Search/Filter Aktif, dan Pemulihan dari Empty State

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-115`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-115` | `V115L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-115` | `V115K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-115` | `V115J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-115` | `V115I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-115` | `V115H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-115` | `V115G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-115` | `V115F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-115` | `V115E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-115` | `V115D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-115` | `V115C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-115` | `V115B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-115` | `V115A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-115`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kombinasi filter lengkap (dipakai TC-FA-GRP-365, 366, 375, 377, 378): Function `Assignable`; Total Asset Min `1` Max `20`; Total User Min `4` Max `8`; Modified By `ModA`; Last Updated tanggal hari ini s.d. tanggal hari ini. Irisan dengan Search suffix spec: `Alpha`, `Charlie`, dan `Golf`; di luar irisan (alasan): `Echo` (Total Asset 25), `India` (Modified By `ModB`), `bravo` (Function None). Keyword Search K = suffix spec.

## Test Steps

### TC-FA-GRP-377: Clear Search saat Filter dan Sort aktif

1. Ketik Search `{runId}-115`, tekan Enter
2. Klik icon Filter
3. Pilih `Assignable` pada dropdown Function
4. Isi Total Asset Min `1` dan Max `20`
5. Isi Total User Min `4` dan Max `8`
6. Pilih `ModA` pada dropdown Modified By
7. Pilih rentang Last Updated tanggal hari ini sampai tanggal hari ini
8. Klik [Apply]
9. Klik header Group dua kali sampai sort Descending
10. Klik `✕` pada kotak Search
11. Tekan Enter
12. Verifikasi kotak Search kosong
13. Verifikasi indikator filter aktif tetap tampil pada icon Filter
14. Verifikasi sedikitnya satu baris tampil pada tabel
15. Verifikasi urutan Descending tetap berlaku: baris `Golf {runId}-115` berada di atas baris `Charlie {runId}-115`, dan baris `Charlie {runId}-115` berada di atas baris `Alpha {runId}-115`

### TC-FA-GRP-378: Ganti target sort saat Search dan Filter aktif

16. Klik `(←)` pada kotak Search
17. Klik header Group satu kali sampai sort netral
18. Klik icon Filter
19. Klik [Clear Field]
20. Klik [Apply]
21. Ketik Search `{runId}-115`, tekan Enter
22. Klik icon Filter
23. Pilih `Assignable` pada dropdown Function
24. Isi Total Asset Min `1` dan Max `20`
25. Isi Total User Min `4` dan Max `8`
26. Pilih `ModA` pada dropdown Modified By
27. Pilih rentang Last Updated tanggal hari ini sampai tanggal hari ini
28. Klik [Apply]
29. Klik header Group satu kali sampai sort Ascending
30. Klik header Total Asset
31. Verifikasi sort berpindah ke kolom Total Asset Ascending: urutan baris `Golf {runId}-115`, `Alpha {runId}-115`, lalu `Charlie {runId}-115`
32. Verifikasi sort kolom Group kembali netral
33. Verifikasi baris `Echo {runId}-115` tidak tampil (Search dan filter tetap menyaring)

### TC-FA-GRP-379: Pemulihan dari empty state hasil Search + Filter

34. Klik header Total Asset dua kali sampai sort netral
35. Klik icon Filter
36. Klik [Clear Field]
37. Klik [Apply]
38. Klik `(←)` pada kotak Search
39. Ketik Search `delta {runId}-115`, tekan Enter
40. Klik icon Filter
41. Pilih `Disposal Group` pada dropdown Function
42. Klik [Apply]
43. Verifikasi empty state tampil dengan Illustration, title `No results found`, dan body `Try adjusting your search or filter.`
44. Klik icon Filter
45. Klik [Clear Field]
46. Klik [Apply]
47. Verifikasi baris `delta {runId}-115` tampil (tabel pulih)
48. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mengisi kombinasi filter pada Prerequisites, mengembalikan sort ke netral, serta membersihkan Search dan filter antar TC (S-03, S-09, R-16).
- Pada TC-FA-GRP-378 kolom A = Group (Ascending) dan kolom B = Total Asset; pada TC-FA-GRP-379 kombinasi tanpa irisan = Search `delta` (Function None) dengan filter Function `Disposal Group`. Keduanya ditentukan spec karena TC memakai "K", "A", "B" tanpa nilai.
- Siklus sort netral memakai 3 klik per kolom (Ascending, Descending, netral) menurut TC-FA-GRP-367.
- Spec 48 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
