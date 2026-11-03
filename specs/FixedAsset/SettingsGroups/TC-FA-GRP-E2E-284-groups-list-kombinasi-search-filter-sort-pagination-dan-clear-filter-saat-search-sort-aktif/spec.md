---
id: TC-FA-GRP-E2E-284-groups-list-kombinasi-search-filter-sort-pagination-dan-clear-filter-saat-search-sort-aktif
title: "Groups List Kombinasi: Search + Filter + Sort + Pagination dan Clear Filter Saat Search/Sort Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-375
  - TC-FA-GRP-376
coverage:
  web: automated
---

# Groups List Kombinasi: Search + Filter + Sort + Pagination dan Clear Filter Saat Search/Sort Aktif

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-284`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-284` | `V284L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-284` | `V284K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-284` | `V284J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-284` | `V284I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-284` | `V284H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-284` | `V284G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-284` | `V284F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-284` | `V284E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-284` | `V284D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-284` | `V284C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-284` | `V284B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-284` | `V284A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-284`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kombinasi filter lengkap (dipakai TC-FA-GRP-365, 366, 375, 377, 378): Function `Assignable`; Total Asset Min `1` Max `20`; Total User Min `4` Max `8`; Modified By `ModA`; Last Updated tanggal hari ini s.d. tanggal hari ini. Irisan dengan Search suffix spec: `Alpha`, `Charlie`, dan `Golf`; di luar irisan (alasan): `Echo` (Total Asset 25), `India` (Modified By `ModB`), `bravo` (Function None). Keyword Search K = suffix spec.

## Test Steps

### TC-FA-GRP-375: Kombinasi Search + Filter + Sort + Pagination

1. Ketik Search `{runId}-284`, tekan Enter
2. Klik icon Filter
3. Pilih `Assignable` pada dropdown Function
4. Isi Total Asset Min `1` dan Max `20`
5. Isi Total User Min `4` dan Max `8`
6. Pilih `ModA` pada dropdown Modified By
7. Pilih rentang Last Updated tanggal hari ini sampai tanggal hari ini
8. Klik [Apply]
9. Klik header Group dua kali sampai sort Descending
10. Ubah page size ke 25
11. Verifikasi keyword Search `{runId}-284` tetap terpasang pada kotak Search
12. Verifikasi indikator filter aktif tampil pada icon Filter
13. Verifikasi page size 25 tetap terpilih
14. Verifikasi urutan baris Descending pada himpunan irisan: `Golf {runId}-284`, lalu `Charlie {runId}-284`, lalu `Alpha {runId}-284`

### TC-FA-GRP-376: Clear Filter saat Search dan Sort aktif

15. Klik icon Filter
16. Klik [Clear Field]
17. Klik [Apply]
18. Verifikasi keyword Search `{runId}-284` tetap terpasang pada kotak Search
19. Verifikasi kolom Group tetap Descending: baris `lima {runId}-284` berada di atas baris `Kilo {runId}-284`
20. Verifikasi baris `bravo {runId}-284` tampil (kriteria filter terlepas)
21. Verifikasi indikator filter aktif tidak tampil pada icon Filter
22. Klik header Group satu kali sampai sort netral
23. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mengisi kombinasi filter pada Prerequisites, mengembalikan sort ke netral, dan menutup Search (S-03, S-09, R-16). TC-FA-GRP-376 memakai state akhir TC-FA-GRP-375 (Search, filter, dan sort aktif) sebagai precondition, sesuai langkah TC.
- Keyword Search K memakai suffix spec; kombinasi filter ditentukan spec karena TC menyebut "nilai yang beririsan" tanpa nilai. Sort Descending diperoleh dengan 2 klik header Group (siklus Asc, Desc, netral menurut TC-FA-GRP-367).
- TC-FA-GRP-365 dan 366 berada di spec 114.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
