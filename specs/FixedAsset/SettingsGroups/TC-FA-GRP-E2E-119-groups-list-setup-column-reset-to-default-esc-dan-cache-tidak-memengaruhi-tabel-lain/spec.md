---
id: TC-FA-GRP-E2E-119-groups-list-setup-column-reset-to-default-esc-dan-cache-tidak-memengaruhi-tabel-lain
title: "Groups List Setup Column: [Reset to Default], (X) dan Esc Membatalkan, dan Cache Tidak Memengaruhi Tabel Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-404
  - TC-FA-GRP-405
  - TC-FA-GRP-406
coverage:
  web: automated
---

# Groups List Setup Column: [Reset to Default], (X) dan Esc Membatalkan, dan Cache Tidak Memengaruhi Tabel Lain

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-119`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-119` | `V119L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-119` | `V119K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-119` | `V119J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-119` | `V119I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-119` | `V119H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-119` | `V119G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-119` | `V119F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-119` | `V119E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-119` | `V119D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-119` | `V119C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-119` | `V119B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-119` | `V119A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-119`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): viewport browser disesuaikan sehingga tabel dapat di-scroll horizontal, dan penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).

## Test Steps

1. Ketik Search `{runId}-119`, tekan Enter

### TC-FA-GRP-404: [Reset to Default]

2. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
3. Drag kolom Last Updated ke posisi paling awal
4. Hilangkan centang kolom Code
5. Klik icon Pin kolom Group
6. Klik [Save]
7. Verifikasi tabel menampilkan urutan header Last Updated, Group, Function, Total Asset, Total User, Modified By tanpa kolom Code
8. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
9. Klik [Reset to Default]
10. Verifikasi Live Preview kembali ke susunan default: urutan Group, Code, Function, Total Asset, Total User, Modified By, Last Updated, semua tampil dan tanpa pin
11. Klik [Save]
12. Muat ulang halaman (F5)
13. Verifikasi tabel kembali ke susunan default dan bertahan setelah F5: urutan header Group, Code, Function, Total Asset, Total User, Modified By, Last Updated

### TC-FA-GRP-405: (X) dan Esc membatalkan perubahan

14. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
15. Hilangkan centang kolom Code
16. Klik icon close (X) pada header popup
17. Verifikasi popup tertutup
18. Verifikasi kolom Code masih tampil pada header tabel (perubahan tidak diterapkan)
19. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
20. Drag kolom Last Updated ke posisi paling awal
21. Tekan Esc
22. Verifikasi popup tertutup
23. Verifikasi urutan header tabel tetap Group, Code, Function, Total Asset, Total User, Modified By, Last Updated (konfigurasi tersimpan terakhir)

### TC-FA-GRP-406: Cache tidak memengaruhi tabel lain

24. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
25. Hilangkan centang kolom Total User
26. Klik [Save]
27. Verifikasi kolom Total User hilang dari tabel Groups List
28. Klik icon Changelog
29. Verifikasi tabel Modal Changelog: Group tetap memuat kolom Date, Action, Group Name, Field, Old Value, New Value, dan Modified By (konfigurasi kolomnya sendiri)
30. Klik icon close (X) pada header Modal Changelog
31. Verifikasi kolom Total User masih hilang dari tabel Groups List (konfigurasi tersimpan)
32. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
33. Klik [Reset to Default]
34. Klik [Save]
35. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec, membuka Modal Changelog dan menutupnya lewat (X), serta [Reset to Default] + [Save] sebagai pemulihan antar TC (S-03, S-09, R-16). Posisi tujuan drag (paling awal), kolom yang di-hide (`Code`, `Total User`), dan kolom yang dipin (`Group`) pada TC-FA-GRP-404/405/406 ditentukan spec karena TC menyebut "beberapa kolom" tanpa nama.
- Footer popup tanpa tombol [Cancel]: penutupan lewat icon close (X) dan Esc (TC-FA-GRP-405, Expected a).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel dapat di-scroll horizontal, sehingga viewport disesuaikan (Prerequisites).
