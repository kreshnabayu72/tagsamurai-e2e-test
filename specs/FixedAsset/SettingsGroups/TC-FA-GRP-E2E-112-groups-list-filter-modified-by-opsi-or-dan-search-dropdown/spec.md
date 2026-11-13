---
id: TC-FA-GRP-E2E-112-groups-list-filter-modified-by-opsi-or-dan-search-dropdown
title: "Groups List Filter Modified By: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-356
  - TC-FA-GRP-357
  - TC-FA-GRP-358
  - TC-FA-GRP-359
coverage:
  web: automated
---

# Groups List Filter Modified By: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-112`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-112` | `V112L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-112` | `V112K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-112` | `V112J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-112` | `V112I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-112` | `V112H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-112` | `V112G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-112` | `V112F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-112` | `V112E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-112` | `V112D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-112` | `V112C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-112` | `V112B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-112` | `V112A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-112`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Spec ini tidak membatasi tabel dengan Search suffix: filter Modified By diasersi bersama baris Pre-setup `Default Group` (Modified By `System`, Pre-setup Tabel A, NC-01). Hasil filter `ModB` (5 baris seeding batch 2) dan `System` (baris Pre-setup Tabel A yang Modified By-nya `System`, hanya dibaca) tidak dijamin muat satu halaman sebesar 10 baris; page size tabel diatur 25 sebelum asersi hasil filter, dan jumlah total hasil filter dijamin tidak melebihi 25 (jumlah baris Pre-setup `System` dibaca tim FE sebelum uji, disediakan tim FE).

## Test Steps

### TC-FA-GRP-356: Isi opsi dropdown Filter Modified By

1. Klik icon Filter
2. Buka dropdown Modified By
3. Verifikasi opsi `ModA` dan `ModB` tampil sebagai nilai Modified By distinct pada baris tabel
4. Verifikasi opsi `System` tampil (baris `Default Group` terakhir diubah sistem)
5. Verifikasi kotak search internal tampil di dalam dropdown
6. Centang opsi `ModA` dan opsi `ModB`
7. Verifikasi opsi `ModA` dan `ModB` keduanya tercentang (multi-select)
8. Hilangkan centang opsi `ModA` dan `ModB`

### TC-FA-GRP-357: Filter Modified By satu opsi

9. Pilih opsi `ModB` pada dropdown Modified By
10. Klik [Apply]
11. Atur page size tabel menjadi 25
12. Verifikasi sedikitnya satu baris tampil pada tabel
13. Verifikasi baris `Kilo {runId}-112` tampil dan baris `Alpha {runId}-112` tidak tampil
14. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-358: Filter Modified By dua opsi (OR)

15. Klik icon Filter
16. Klik [Clear Field]
17. Centang opsi `ModB` dan opsi `System` pada dropdown Modified By
18. Klik [Apply]
19. Atur page size tabel menjadi 25
20. Verifikasi baris `Kilo {runId}-112` dan baris `Default Group` tampil (opsi 1 atau opsi 2)
21. Verifikasi baris `Alpha {runId}-112` tidak tampil (Modified By `ModA`)

### TC-FA-GRP-359: Search internal dropdown Filter Modified By

22. Klik icon Filter
23. Klik [Clear Field]
24. Buka dropdown Modified By
25. Ketik potongan nama `ModB` huruf kecil di kotak search dropdown
26. Verifikasi daftar opsi menyempit: opsi `ModB` tampil
27. Verifikasi opsi `System` tidak tampil
28. Ganti isi kotak search dropdown dengan `zzz-tidak-ada`
29. Verifikasi daftar opsi kosong dengan teks `No results found` (teks saja, tanpa ilustrasi)
30. Klik [Apply]

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Filter Panel dan dropdown, menghilangkan centang pada TC-FA-GRP-356, serta [Clear Field] + [Apply] sebagai pemulihan state antar TC (S-03, S-09).
- Pilihan opsi `ModB` (TC-FA-GRP-357) dan pasangan `ModB` + `System` (TC-FA-GRP-358) ditentukan spec agar baris hasil tidak melampaui satu halaman dan opsi "lain" dapat diamati lewat `Default Group`.
- Langkah "Atur page size tabel menjadi 25" (langkah 11 dan 19) adalah langkah penghubung supaya seluruh hasil filter berada pada satu halaman (S-14, S-03).
- Opsi `System` pada TC-FA-GRP-356 diasersi dari baris Pre-setup `Default Group` (hanya dibaca).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Hasil filter `System` dan `ModB` diasumsikan tidak lebih dari 25 baris (page size 25), bergantung pada data Pre-setup aktual (menyangkut TC-FA-GRP-356 dan TC-FA-GRP-358). Dikonfirmasi tim FE.
