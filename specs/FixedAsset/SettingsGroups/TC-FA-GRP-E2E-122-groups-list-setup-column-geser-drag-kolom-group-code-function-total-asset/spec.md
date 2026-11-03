---
id: TC-FA-GRP-E2E-122-groups-list-setup-column-geser-drag-kolom-group-code-function-total-asset
title: "Groups List Setup Column: Geser (Drag) Kolom Group, Code, Function, dan Total Asset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-389
  - TC-FA-GRP-390
  - TC-FA-GRP-391
  - TC-FA-GRP-392
coverage:
  web: automated
---

# Groups List Setup Column: Geser (Drag) Kolom Group, Code, Function, dan Total Asset

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-122`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-122` | `V122L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-122` | `V122K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-122` | `V122J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-122` | `V122I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-122` | `V122H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-122` | `V122G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-122` | `V122F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-122` | `V122E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-122` | `V122D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-122` | `V122C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-122` | `V122B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-122` | `V122A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-122`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): viewport browser disesuaikan sehingga tabel dapat di-scroll horizontal, dan penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).
- Parameter iterasi TC-FA-GRP-389, 390, 391, 392, urutan baris = urutan iterasi (urutan header default: Group, Code, Function, Total Asset, Total User, Modified By, Last Updated):

| Kolom yang digeser | Posisi tujuan | Urutan header setelah Save |
|---|---|---|
| Group | paling akhir | Code, Function, Total Asset, Total User, Modified By, Last Updated, Group |
| Code | paling akhir | Group, Function, Total Asset, Total User, Modified By, Last Updated, Code |
| Function | paling awal | Function, Group, Code, Total Asset, Total User, Modified By, Last Updated |
| Total Asset | paling awal | Total Asset, Group, Code, Function, Total User, Modified By, Last Updated |

## Test Steps

1. Ketik Search `{runId}-122`, tekan Enter

### TC-FA-GRP-389 sampai 392: Geser (drag) kolom Group, Code, Function, dan Total Asset (iterasi per kolom)

2. Untuk setiap baris tabel parameter iterasi (langkah 3 sampai 12): jalankan langkah berikut dengan kolom dan posisi pada baris itu
3. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
4. Drag kolom pada baris tabel ke posisi tujuan pada baris tabel
5. Verifikasi urutan Live Preview mengikuti posisi baru
6. Klik [Save]
7. Verifikasi urutan header tabel sesuai kolom "Urutan header setelah Save" baris tabel
8. Muat ulang halaman (F5)
9. Verifikasi urutan header tabel masih sesuai kolom "Urutan header setelah Save" (konfigurasi bertahan setelah F5)
10. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
11. Klik [Reset to Default]
12. Klik [Save]

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 3 sampai 12 diulang untuk tiap baris tabel parameter iterasi (Group/Code/Function/Total Asset): 10 langkah per iterasi.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Popup Setup Column lewat icon `⋯` > `Setup Column...`, [Reset to Default] + [Save] untuk memulihkan susunan default antar iterasi, serta F5 setelah [Save] (S-03, S-09). Pemulihan akhir preferensi kolom: hook `after` menghapus preferensi kolom di browser (bagian 4).
- Posisi tujuan drag ditentukan spec (TC menyebut "posisi lain").
- Spec 12 langkah (ekspansi iterasi ± 42 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di Prerequisites (bagian 8b butir 7).
- Muat ulang halaman (F5) membuang kotak Search, sehingga spec tidak menutup Search dengan `(←)` di akhir (A-9, S-14).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel dapat di-scroll horizontal, sehingga viewport disesuaikan (Prerequisites).
