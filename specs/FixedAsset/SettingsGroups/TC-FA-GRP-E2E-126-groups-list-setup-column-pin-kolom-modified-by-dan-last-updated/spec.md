---
id: TC-FA-GRP-E2E-126-groups-list-setup-column-pin-kolom-modified-by-dan-last-updated
title: "Groups List Setup Column: Pin Kolom Modified By dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-401
  - TC-FA-GRP-402
coverage:
  web: automated
---

# Groups List Setup Column: Pin Kolom Modified By dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-126`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-126` | `V126L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-126` | `V126K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-126` | `V126J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-126` | `V126I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-126` | `V126H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-126` | `V126G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-126` | `V126F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-126` | `V126E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-126` | `V126D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-126` | `V126C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-126` | `V126B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-126` | `V126A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-126`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).
- Parameter iterasi TC-FA-GRP-401, 402, urutan baris = urutan iterasi:

| Kolom |
|---|
| Modified By |
| Last Updated |

## Test Steps

1. Ketik Search `{runId}-126`, tekan Enter

### TC-FA-GRP-401 dan 402: Pin kolom Modified By dan Last Updated (iterasi per kolom)

2. Untuk setiap baris tabel parameter iterasi (langkah 3 sampai 17): jalankan langkah berikut dengan kolom pada baris itu
3. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
4. Klik icon Pin kolom pada baris tabel
5. Klik [Save]
6. Setel lebar viewport 900px
7. Scroll tabel secara horizontal
8. Verifikasi kolom pada baris tabel membeku (sticky) saat tabel di-scroll horizontal
9. Muat ulang halaman (F5)
10. Scroll tabel secara horizontal
11. Verifikasi kolom pada baris tabel masih membeku (pin bertahan setelah F5)
12. Buka Popup Setup Column: klik icon `⋯` di header kolom terakhir, lalu klik `Setup Column...`
13. Klik icon Pin kolom pada baris tabel untuk unpin
14. Klik [Save]
15. Scroll tabel secara horizontal
16. Verifikasi kolom pada baris tabel kembali ikut ter-scroll
17. Pulihkan lebar viewport

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 3 sampai 17 diulang untuk tiap baris tabel parameter iterasi (Modified By/Last Updated): 15 langkah per iterasi.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Popup Setup Column lewat icon `⋯` > `Setup Column...`, [Reset to Default] + [Save] untuk memulihkan susunan default antar iterasi, serta F5 setelah [Save] (S-03, S-09). Pemulihan akhir preferensi kolom: hook `after` menghapus preferensi kolom di browser (bagian 4).
- Muat ulang halaman (F5) membuang kotak Search, sehingga spec tidak menutup Search dengan `(←)` di akhir (A-9, S-14).
- Lebar viewport 900px disetel agar tabel dapat di-scroll horizontal dan dipulihkan di akhir tiap iterasi (mengikuti spec 100).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel dapat di-scroll horizontal, sehingga spec menyetel lebar viewport 900px lewat langkah penghubung.
