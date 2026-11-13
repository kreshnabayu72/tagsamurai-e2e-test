---
id: TC-FA-GRP-E2E-116-groups-list-sort-kolom-group-code-function-dan-total-asset-siklus-asc-desc-netral
title: "Groups List Sort Kolom Group, Code, Function, dan Total Asset (Asc, Desc, Netral)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-367
  - TC-FA-GRP-368
  - TC-FA-GRP-369
  - TC-FA-GRP-370
coverage:
  web: automated
---

# Groups List Sort Kolom Group, Code, Function, dan Total Asset (Asc, Desc, Netral)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-116`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-116` | `V116L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-116` | `V116K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-116` | `V116J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-116` | `V116I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-116` | `V116H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-116` | `V116G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-116` | `V116F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-116` | `V116E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-116` | `V116D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-116` | `V116C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-116` | `V116B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-116` | `V116A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-116`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Parameter iterasi TC-FA-GRP-367, 368, 369, 370 (kolom Group, Code, Function, Total Asset), urutan baris = urutan iterasi. Tabel dibatasi Search suffix spec (12 baris; 10 baris di halaman 1). Default tabel = Group A-Z tanpa membedakan huruf besar/kecil. Code dataset berurutan terbalik terhadap nama (`V116A` milik `lima`, `V116L` milik `Alpha`); Function: Assignable 6 baris, None 6 baris; Total Asset terurut: 0, 0, 0, 1, 2, 3, 4, 5, 7, 10, 13, 25.

| Kolom | Setelah klik #1 (Ascending) | Setelah klik #2 (Descending) |
|---|---|---|
| Group | baris 1 sampai 3 = `Alpha {runId}-116`, `bravo {runId}-116`, `Charlie {runId}-116` | baris 1 sampai 3 = `lima {runId}-116`, `Kilo {runId}-116`, `juliet {runId}-116` |
| Code | baris 1 sampai 3 = `lima {runId}-116`, `Kilo {runId}-116`, `juliet {runId}-116` | baris 1 sampai 3 = `Alpha {runId}-116`, `bravo {runId}-116`, `Charlie {runId}-116` |
| Function | baris 1 sampai 6 ber-Function Assignable, baris 7 sampai 10 None | baris 1 sampai 6 None, baris 7 sampai 10 Assignable |
| Total Asset | baris 4 = `Golf {runId}-116`, baris 5 = `Alpha {runId}-116`, baris 10 = `Charlie {runId}-116` | baris 1 sampai 3 = `Echo {runId}-116`, `India {runId}-116`, `Charlie {runId}-116` |

## Test Steps

1. Ketik Search `{runId}-116`, tekan Enter

### TC-FA-GRP-367, 368, 369, 370: Sort per kolom Group, Code, Function, dan Total Asset (iterasi per kolom)

2. Untuk setiap baris tabel parameter iterasi (langkah 3 sampai 9): jalankan langkah berikut dengan kolom pada baris itu
3. Verifikasi header kolom pada baris tabel tampil di tabel
4. Klik header kolom pada baris tabel satu kali
5. Verifikasi urutan tabel sesuai sel "Setelah klik #1 (Ascending)" baris tabel
6. Klik header kolom yang sama satu kali lagi
7. Verifikasi urutan tabel sesuai sel "Setelah klik #2 (Descending)" baris tabel
8. Klik header kolom yang sama satu kali lagi
9. Verifikasi urutan tabel kembali ke default: baris 1 sampai 3 = `Alpha {runId}-116`, `bravo {runId}-116`, `Charlie {runId}-116` (Group A-Z)
10. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 3 sampai 9 diulang untuk tiap baris tabel parameter iterasi (Group, Code, Function, Total Asset): 4 iterasi x 7 langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec di awal dan menutupnya di akhir (S-03, R-16).
- Pada iterasi kolom Group, urutan netral (default Group A-Z) sama dengan Ascending; asersi klik #3 tetap ditulis sesuai TC. Data Uji TC "nilai variasi (huruf besar/kecil, angka, kosong)" dipenuhi oleh nama dataset berhuruf besar dan kecil.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-367 menyebut data variasi "kosong" untuk kolom Group yang tidak pernah kosong; spec memakai variasi huruf besar/kecil.
  - TC-FA-GRP-368 memakai Data Uji Code `BO, HO, R301, WH-A, WH-B`; spec memakai Code dataset bersuffix nomor spec (bagian 5) dengan urutan berbeda dari nama agar Ascending dan netral dapat dibedakan.
