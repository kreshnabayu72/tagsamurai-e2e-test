---
id: TC-FA-GRP-E2E-108-groups-list-filter-panel-screening-dan-filter-function-opsi-search-dropdown
title: "Groups List Filter Panel: Screening, Isi Opsi Function, Filter Function Satu/Dua Opsi (OR), dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-345
  - TC-FA-GRP-346
  - TC-FA-GRP-347
  - TC-FA-GRP-348
  - TC-FA-GRP-349
coverage:
  web: automated
---

# Groups List Filter Panel: Screening, Isi Opsi Function, Filter Function Satu/Dua Opsi (OR), dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-108`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-108` | `V108L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-108` | `V108K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-108` | `V108J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-108` | `V108I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-108` | `V108H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-108` | `V108G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-108` | `V108F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-108` | `V108E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-108` | `V108D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-108` | `V108C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-108` | `V108B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-108` | `V108A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-108`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).

## Test Steps

1. Ketik Search `{runId}-108`, tekan Enter

### TC-FA-GRP-345: Screening Filter Panel

2. Klik icon Filter
3. Verifikasi Filter Panel terbuka berisi field berurutan: Function (dropdown multi-select searchable, placeholder `All functions`), Total Asset (Range Min-Max, placeholder `Min` dan `Max`), Total User (Range Min-Max, placeholder `Min` dan `Max`), Modified By (dropdown multi-select searchable, placeholder `All users`), dan Last Updated (date range picker, placeholder `Select date`)
4. Verifikasi tombol footer [Clear Field] dan [Apply] tampil
5. Verifikasi tidak ada field filter lain di luar daftar field tersebut

### TC-FA-GRP-346: Isi opsi dropdown Filter Function

6. Buka dropdown Function
7. Verifikasi opsi `None`, `Assignable`, dan `Disposal Group` tampil sebagai nilai Function distinct yang ada pada baris tabel
8. Verifikasi opsi ditampilkan sebagai nilai penuh (bukan label badge)
9. Verifikasi kotak search internal tampil di dalam dropdown
10. Centang opsi `None`
11. Centang opsi `Assignable`
12. Verifikasi opsi `None` dan `Assignable` keduanya tercentang (multi-select)
13. Hilangkan centang opsi `None` dan `Assignable`

### TC-FA-GRP-347: Filter Function satu opsi

14. Pilih opsi `Disposal Group` pada dropdown Function
15. Klik [Apply]
16. Verifikasi sedikitnya satu baris tampil pada tabel
17. Verifikasi baris `hotel {runId}-108` tampil
18. Verifikasi seluruh baris yang tampil ber-Function `Disposal Group`
19. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-348: Filter Function dua opsi (OR)

20. Klik icon Filter
21. Klik [Clear Field]
22. Centang opsi `None` dan `Assignable` pada dropdown Function
23. Klik [Apply]
24. Verifikasi baris `bravo {runId}-108` dan `Alpha {runId}-108` tampil (opsi 1 atau opsi 2)
25. Verifikasi baris `hotel {runId}-108` tidak tampil

### TC-FA-GRP-349: Search internal dropdown Filter Function

26. Klik icon Filter
27. Klik [Clear Field]
28. Buka dropdown Function
29. Ketik `ssign` di kotak search dropdown
30. Verifikasi daftar opsi menyempit: opsi `Assignable` tampil
31. Verifikasi opsi `None` tidak tampil
32. Ganti isi kotak search dropdown dengan `zzz-tidak-ada`
33. Verifikasi daftar opsi kosong dengan teks `No results found` (teks saja, tanpa ilustrasi)
34. Klik [Apply]
35. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec di awal, membuka Filter Panel dan dropdown, menutup dropdown, serta [Clear Field] + [Apply] dan `(←)` pada kotak Search sebagai pemulihan state antar TC (S-03, S-09, R-16).
- Dataset memuat ketiga nilai Function (`None`, `Assignable`, `Disposal Group`), sehingga opsi dropdown pada TC-FA-GRP-346 dapat diasersi dari baris yang tampil; opsi dari baris Pre-setup tidak diasersi.
- Keyword `ssign` (potongan `Assignable`) dipilih spec; TC menyebut "potongan nama opsi huruf kecil" tanpa nilai.
- Verifikasi "seluruh baris yang tampil ber-Function `Disposal Group`" didahului pembanding sedikitnya satu baris (bagian 8b butir 2).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
