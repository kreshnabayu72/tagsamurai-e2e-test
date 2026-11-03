---
id: TC-FA-CAT-E2E-011-role-matrix-visibilitas-total-control-read-only-capability-read
title: "Role Matrix: Visibilitas Elemen Categories List (Total Control, Read Only, Capability Read)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-32
  - TC-FA-CAT-33
  - TC-FA-CAT-34
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Categories List (Total Control, Read Only, Capability Read)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-CAT-32 | Total Control | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | TC-FA-CAT-33 | Read Only | #2 | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
  | TC-FA-CAT-34 | Capability Read (Global Role Manage Asset Master Data: R saja) | #3 | `capabilityRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CAPREAD_PASSWORD` |
- Login akun aktor pertama (Total Control) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pengecualian atas `suite.md`: precondition TC adalah halaman utama FAMS, sehingga hook `beforeEach` membuka halaman utama FAMS (bukan Categories) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Env var `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CAPREAD_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise); baris `Furniture` dan `Tools` dibaca; spec tidak mengubah data.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk ketiga akun aktor.
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-32: Visibilitas elemen Categories List untuk aktor Total Control

1. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
2. Verifikasi Total Control: menu `Settings > Categories` Show
3. Verifikasi Total Control: halaman Categories terbuka (aktor memiliki Read)
4. Verifikasi Total Control: sidebar `[+] Category` Show
5. Klik elipsis (⋯) pada baris `Furniture`
6. Verifikasi Total Control: row action Detail, + Add Subcategory, Edit, Delete Show pada baris `Furniture`
7. Tutup menu row action
8. Verifikasi Total Control: checkbox baris Show
9. Centang checkbox baris `Tools`
10. Verifikasi Total Control: Bulk Action Bar `[Delete]` Show
11. Hapus centang checkbox baris `Tools`
12. Verifikasi Total Control: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

### TC-FA-CAT-33: Visibilitas elemen Categories List untuk aktor Read Only

13. Logout dari akun Total Control
14. Login sebagai Read Only (`readOnly_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_RO_PASSWORD`)
15. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
16. Verifikasi Read Only: menu `Settings > Categories` Show
17. Verifikasi Read Only: halaman Categories terbuka (aktor memiliki Read)
18. Verifikasi Read Only: sidebar `[+] Category` Hidden
19. Klik elipsis (⋯) pada baris `Furniture`
20. Verifikasi Read Only: row action Detail Show pada baris `Furniture`
21. Verifikasi Read Only: row action + Add Subcategory, Edit, Delete Hidden pada baris `Furniture`
22. Tutup menu row action
23. Verifikasi Read Only: checkbox baris dan Bulk Action Bar `[Delete]` Hidden
24. Verifikasi Read Only: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

### TC-FA-CAT-34: Visibilitas elemen Categories List untuk aktor Capability Read

25. Logout dari akun Read Only
26. Login sebagai Capability Read (`capabilityRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_CAPREAD_PASSWORD`)
27. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
28. Verifikasi Capability Read: menu `Settings > Categories` Show
29. Verifikasi Capability Read: halaman Categories terbuka (aktor memiliki Read)
30. Verifikasi Capability Read: sidebar `[+] Category` Hidden
31. Klik elipsis (⋯) pada baris `Furniture`
32. Verifikasi Capability Read: row action Detail Show pada baris `Furniture`
33. Verifikasi Capability Read: row action + Add Subcategory, Edit, Delete Hidden pada baris `Furniture`
34. Tutup menu row action
35. Verifikasi Capability Read: checkbox baris dan Bulk Action Bar `[Delete]` Hidden
36. Verifikasi Capability Read: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Spec Role Matrix visibilitas (bagian 3a): satu daftar elemen, banyak role, hasil berbeda per role; polaritas Show dan Hidden dicampur.
- Langkah penghubung (S-03): tiap langkah "Tutup menu row action" dan "Hapus centang checkbox baris `Tools`", serta pasangan logout dan login di awal blok TC-FA-CAT-33 dan TC-FA-CAT-34 (ganti akun eksplisit; akun pertama login di hook `before`, S-07).
- Langkah "Centang checkbox baris `Tools` bila checkbox tampil" pada LK TC ditulis deterministik per role: role yang Expected-nya menyatakan checkbox Show mencentang checkbox, role yang Expected-nya menyatakan Hidden memverifikasi checkbox dan Bulk Action Bar Hidden (tanpa langkah bersyarat).
- Expected TC-FA-CAT-33 butir d dan TC-FA-CAT-34 butir d "Bulk Action Bar Hidden" dikerjakan sebagai satu `Verifikasi` bersama checkbox karena tanpa checkbox tidak ada seleksi yang memunculkan bar (S-03).
- Temuan untuk QA:
  - TC-FA-CAT-32 sampai TC-FA-CAT-39 menyebut env var password tidak sama sekali; nama env var diusulkan spec (`FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CAPREAD_PASSWORD`, dan seterusnya) dan perlu keputusan tim.
- Ukuran spec (36 langkah, melewati sekitar 35): Role Matrix mengulang urutan langkah untuk tiap role (bagian 3a) dan tiap klausa Expected menjadi satu `Verifikasi` (S-01). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, keputusan 2026-10-30) dan hasil tiap role berbeda; tiap blok berdiri sendiri (login ulang eksplisit di awal blok) sehingga bagian sesudahnya tetap bermakna walau blok sebelumnya gagal; spec tidak dipecah.
- Spec melewati 35 langkah (36 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
