---
id: TC-FA-GRP-E2E-114-groups-list-kombinasi-search-lalu-filter-dan-filter-lalu-search-irisan
title: "Groups List Kombinasi: Search lalu Filter dan Filter lalu Search (Irisan)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-365
  - TC-FA-GRP-366
coverage:
  web: automated
---

# Groups List Kombinasi: Search lalu Filter dan Filter lalu Search (Irisan)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-114`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-114` | `V114L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-114` | `V114K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-114` | `V114J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-114` | `V114I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-114` | `V114H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-114` | `V114G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-114` | `V114F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-114` | `V114E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-114` | `V114D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-114` | `V114C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-114` | `V114B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-114` | `V114A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-114`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kombinasi filter lengkap (dipakai TC-FA-GRP-365, 366, 375, 377, 378): Function `Assignable`; Total Asset Min `1` Max `20`; Total User Min `4` Max `8`; Modified By `ModA`; Last Updated tanggal hari ini s.d. tanggal hari ini. Irisan dengan Search suffix spec: `Alpha`, `Charlie`, dan `Golf`; di luar irisan (alasan): `Echo` (Total Asset 25), `India` (Modified By `ModB`), `bravo` (Function None). Keyword Search K = suffix spec.

## Test Steps

### TC-FA-GRP-365: Search lalu Filter (irisan)

1. Ketik Search `{runId}-114`, tekan Enter
2. Klik icon Filter
3. Pilih `Assignable` pada dropdown Function
4. Isi Total Asset Min `1` dan Max `20`
5. Isi Total User Min `4` dan Max `8`
6. Pilih `ModA` pada dropdown Modified By
7. Pilih rentang Last Updated tanggal hari ini sampai tanggal hari ini
8. Klik [Apply]
9. Verifikasi baris `Alpha {runId}-114`, `Charlie {runId}-114`, dan `Golf {runId}-114` tampil
10. Verifikasi baris `Echo {runId}-114` tidak tampil (Total Asset di luar rentang)
11. Verifikasi baris `India {runId}-114` tidak tampil (Modified By `ModB`)
12. Verifikasi baris `bravo {runId}-114` tidak tampil (Function `None`)
13. Verifikasi keyword Search `{runId}-114` tetap terpasang pada kotak Search

### TC-FA-GRP-366: Filter lalu Search (irisan)

14. Klik `(←)` pada kotak Search
15. Klik icon Filter
16. Klik [Clear Field]
17. Klik [Apply]
18. Klik icon Filter
19. Pilih `Assignable` pada dropdown Function
20. Isi Total Asset Min `1` dan Max `20`
21. Isi Total User Min `4` dan Max `8`
22. Pilih `ModA` pada dropdown Modified By
23. Pilih rentang Last Updated tanggal hari ini sampai tanggal hari ini
24. Klik [Apply]
25. Ketik Search `{runId}-114`, tekan Enter
26. Verifikasi baris `Alpha {runId}-114`, `Charlie {runId}-114`, dan `Golf {runId}-114` tampil
27. Verifikasi baris `Echo {runId}-114` tidak tampil (Total Asset di luar rentang)
28. Verifikasi baris `India {runId}-114` tidak tampil (Modified By `ModB`)
29. Verifikasi baris `bravo {runId}-114` tidak tampil (Function `None`)
30. Verifikasi kriteria filter tetap aktif: indikator filter aktif tampil pada icon Filter
31. Klik `(←)` pada kotak Search
32. Klik icon Filter
33. Klik [Clear Field]
34. Klik [Apply]

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mengisi kombinasi filter pada Prerequisites, membersihkan Search dan filter antar TC (S-03, S-09, R-16).
- Keyword Search K memakai suffix spec; kombinasi filter ditentukan spec karena TC menyebut "nilai yang beririsan" tanpa nilai.
- TC-FA-GRP-375 dan 376 berada di spec 284.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
