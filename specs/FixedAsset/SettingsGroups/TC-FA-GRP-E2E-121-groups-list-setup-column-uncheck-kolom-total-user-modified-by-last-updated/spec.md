---
id: TC-FA-GRP-E2E-121-groups-list-setup-column-uncheck-kolom-total-user-modified-by-last-updated
title: "Groups List Setup Column: Uncheck Kolom Total User, Modified By, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-386
  - TC-FA-GRP-387
  - TC-FA-GRP-388
coverage:
  web: automated
---

# Groups List Setup Column: Uncheck Kolom Total User, Modified By, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-121`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-121` | `V121L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-121` | `V121K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-121` | `V121J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-121` | `V121I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-121` | `V121H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-121` | `V121G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-121` | `V121F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-121` | `V121E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-121` | `V121D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-121` | `V121C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-121` | `V121B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-121` | `V121A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-121`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): viewport browser disesuaikan sehingga tabel dapat di-scroll horizontal, dan penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).
- Parameter iterasi TC-FA-GRP-386, 387, 388, urutan baris = urutan iterasi:

| Kolom |
|---|
| Total User |
| Modified By |
| Last Updated |

## Test Steps

1. Ketik Search `{runId}-121`, tekan Enter

### TC-FA-GRP-386 sampai 388: Uncheck kolom Total User, Modified By, dan Last Updated (iterasi per kolom)

2. Untuk setiap baris tabel parameter iterasi (langkah 3 sampai 13): jalankan langkah berikut dengan kolom pada baris itu
3. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
4. Hilangkan centang kolom pada baris tabel pada daftar Popup Setup Column
5. Verifikasi Live Preview langsung menyembunyikan kolom pada baris tabel
6. Klik [Save]
7. Verifikasi kolom pada baris tabel hilang dari tabel
8. Muat ulang halaman (F5)
9. Verifikasi kolom selain kolom pada baris tabel tampil di tabel
10. Verifikasi kolom pada baris tabel masih hilang dari tabel (konfigurasi bertahan setelah F5)
11. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
12. Klik [Reset to Default]
13. Klik [Save]
14. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 3 sampai 13 diulang untuk tiap baris tabel parameter iterasi (Total User/Modified By/Last Updated): 11 langkah per iterasi.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Popup Setup Column lewat icon `⋯` > `Setup Column...`, [Reset to Default] + [Save] untuk memulihkan susunan default antar iterasi, serta F5 setelah [Save] (S-03, S-09). Verifikasi kolom lain pada tabel tampil (langkah 9) ditambahkan sebagai anchor positif sebelum asersi kolom hilang sesudah F5 (8b butir 2, R-21; S-03). Pemulihan akhir preferensi kolom: hook `after` menghapus preferensi kolom di browser (bagian 4).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel dapat di-scroll horizontal, sehingga viewport disesuaikan (Prerequisites).
