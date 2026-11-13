---
id: TC-FA-GRP-E2E-118-groups-list-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4
title: "Groups List Setup Column: Screening Overlay Column Visibility dan Popup 3 Zona, Guard Kolom Terakhir, dan Pin ke-4 Diblok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-380
  - TC-FA-GRP-381
  - TC-FA-GRP-403
  - TC-FA-GRP-1087
coverage:
  web: automated
---

# Groups List Setup Column: Screening Overlay Column Visibility dan Popup 3 Zona, Guard Kolom Terakhir, dan Pin ke-4 Diblok

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-118`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-118` | `V118L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-118` | `V118K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-118` | `V118J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-118` | `V118I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-118` | `V118H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-118` | `V118G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-118` | `V118F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-118` | `V118E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-118` | `V118D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-118` | `V118C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-118` | `V118B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-118` | `V118A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-118`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): viewport browser disesuaikan sehingga tabel dapat di-scroll horizontal, dan penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).

## Test Steps

1. Ketik Search `{runId}-118`, tekan Enter

### TC-FA-GRP-380: Screening Overlay Column Visibility

2. Hover icon `⋯` di header kolom terakhir
3. Verifikasi tooltip `Column Visibility` tampil
4. Klik icon `⋯` di header kolom terakhir
5. Verifikasi item `Setup Column...` tampil di bagian bawah panel overlay
6. Verifikasi daftar kolom berurutan Group, Code, Function, Total Asset, Total User, Modified By, Last Updated, masing-masing Hideable dengan checkbox tercentang dan aktif
7. Verifikasi tiap baris kolom punya drag handle

### TC-FA-GRP-381: Screening Popup Setup Column

8. Klik `Setup Column...`
9. Verifikasi Header popup: title `Setup Column`, teks panduan drag/check/pin, dan icon close (X)
10. Verifikasi Body: daftar kolom Group, Code, Function, Total Asset, Total User, Modified By, Last Updated, masing-masing tercentang dan aktif, dengan drag handle dan icon Pin
11. Verifikasi Live Preview menampilkan header kolom dan sel data sesuai tabel asli
12. Verifikasi Footer: [Reset to Default] (text, primary) dan [Save] (filled, success)
13. Verifikasi tidak ada tombol [Cancel] pada footer

### TC-FA-GRP-403: Guard kolom terakhir yang visible

14. Hilangkan centang kolom Group
15. Hilangkan centang kolom Code
16. Hilangkan centang kolom Function
17. Hilangkan centang kolom Total Asset
18. Hilangkan centang kolom Total User
19. Hilangkan centang kolom Modified By
20. Hover checkbox kolom `Last Updated` yang tersisa
21. Verifikasi checkbox kolom `Last Updated` disabled (tetap tampil)
22. Verifikasi tooltip `At least one column must remain visible.` tampil
23. Klik [Reset to Default]

### TC-FA-GRP-1087: Pin ke-4 diblok setelah tiga kolom terpin

24. Klik icon Pin kolom Group
25. Klik icon Pin kolom Code
26. Klik icon Pin kolom Function
27. Verifikasi kolom Group, Code, dan Function berstatus terpin
28. Hover icon Pin kolom Total Asset
29. Verifikasi icon Pin kolom Total Asset disabled (tidak dapat diklik, kolom tidak beku)
30. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
31. Klik icon Pin kolom Function untuk unpin
32. Hover icon Pin kolom Total Asset
33. Verifikasi icon Pin kolom Total Asset kembali aktif
34. Klik icon close (X) pada header popup
35. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec, menghilangkan centang kolom sampai tersisa satu, [Reset to Default] untuk memulihkan susunan antar TC, dan menutup popup lewat icon close (X) tanpa [Save] sehingga tidak ada konfigurasi tersimpan (S-03, S-09).
- Kolom yang tersisa pada TC-FA-GRP-403 adalah `Last Updated` (kolom terakhir pada daftar), ditentukan spec; TC menyebut "satu kolom".
- Keadaan awal "belum ada kolom yang terpin" pada TC-FA-GRP-1087 dipenuhi oleh [Reset to Default] pada akhir TC-FA-GRP-403 dan hook `after` yang menghapus preferensi kolom.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel dapat di-scroll horizontal, sehingga viewport disesuaikan (Prerequisites).
