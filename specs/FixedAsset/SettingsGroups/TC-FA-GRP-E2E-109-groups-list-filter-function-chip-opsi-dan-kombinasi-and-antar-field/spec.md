---
id: TC-FA-GRP-E2E-109-groups-list-filter-function-chip-opsi-dan-kombinasi-and-antar-field
title: "Groups List Filter: Chip Opsi Function (Hapus via X dan Uncheck) dan Kombinasi Function + Total Asset (AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-350
  - TC-FA-GRP-351
  - TC-FA-GRP-363
coverage:
  web: automated
---

# Groups List Filter: Chip Opsi Function (Hapus via X dan Uncheck) dan Kombinasi Function + Total Asset (AND)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-109`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-109` | `V109L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-109` | `V109K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-109` | `V109J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-109` | `V109I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-109` | `V109H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-109` | `V109G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-109` | `V109F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-109` | `V109E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-109` | `V109D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-109` | `V109C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-109` | `V109B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-109` | `V109A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-109`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).

## Test Steps

1. Ketik Search `{runId}-109`, tekan Enter

### TC-FA-GRP-350: Chip opsi Function dihapus via (X)

2. Klik icon Filter
3. Centang opsi `None` lalu opsi `Assignable` pada dropdown Function
4. Tutup dropdown Function
5. Verifikasi chip `None` dan chip `Assignable` tampil di dalam field Function (chip `Assignable` tidak menggantikan chip `None`)
6. Klik (X) pada chip `None`
7. Verifikasi chip `None` hilang dari field Function
8. Buka dropdown Function
9. Verifikasi checkbox opsi `None` ter-uncheck
10. Verifikasi chip `Assignable` tetap ada
11. Tutup dropdown Function
12. Klik [Apply]
13. Verifikasi sedikitnya satu baris tampil pada tabel
14. Verifikasi baris `Alpha {runId}-109` tampil dan baris `bravo {runId}-109` tidak tampil (Function = `Assignable`)

### TC-FA-GRP-351: Chip opsi Function dihapus via uncheck di dropdown

15. Klik icon Filter
16. Klik [Clear Field]
17. Centang opsi `None` lalu opsi `Assignable` pada dropdown Function
18. Buka lagi dropdown Function dan hilangkan centang opsi `None`
19. Verifikasi chip `None` hilang dari field Function
20. Verifikasi chip `Assignable` tetap ada
21. Klik [Apply]
22. Verifikasi baris `Alpha {runId}-109` tampil dan baris `bravo {runId}-109` tidak tampil (Function = `Assignable`)

### TC-FA-GRP-363: Kombinasi Function + Total Asset (AND)

23. Klik icon Filter
24. Klik [Clear Field]
25. Pilih `Assignable` pada dropdown Function
26. Isi Total Asset Min `5` dan Max `20`
27. Klik [Apply]
28. Verifikasi baris `Charlie {runId}-109` dan `India {runId}-109` tampil (memenuhi kedua kriteria)
29. Verifikasi baris `Echo {runId}-109` tidak tampil (Total Asset 25 di luar rentang)
30. Verifikasi baris `bravo {runId}-109` tidak tampil (Function `None`)
31. Verifikasi baris `Alpha {runId}-109` tidak tampil (Total Asset 2 di luar rentang)
32. Klik icon Filter
33. Klik [Clear Field]
34. Klik [Apply]
35. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec di awal, membuka Filter Panel dan dropdown, menutup dropdown, serta [Clear Field] + [Apply] dan `(←)` pada kotak Search sebagai pemulihan state antar TC (S-03, S-09, R-16).
- Opsi A = `None` dan opsi B = `Assignable` ditentukan spec (TC menyebut "opsi A lalu opsi B"). Rentang Total Asset Min `5` Max `20` pada TC-FA-GRP-363 ditentukan spec karena TC tidak menyebut nilainya.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
