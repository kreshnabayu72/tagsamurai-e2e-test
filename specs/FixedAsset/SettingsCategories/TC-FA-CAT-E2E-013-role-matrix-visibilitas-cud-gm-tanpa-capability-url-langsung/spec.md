---
id: TC-FA-CAT-E2E-013-role-matrix-visibilitas-cud-gm-tanpa-capability-url-langsung
title: "Role Matrix: Visibilitas Elemen Categories List (CUD, Group Manager CRUD), Tanpa Capability, dan URL Langsung"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-38
  - TC-FA-CAT-39
  - TC-FA-CAT-40
  - TC-FA-CAT-41
  - TC-FA-CAT-42
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Categories List (CUD, Group Manager CRUD), Tanpa Capability, dan URL Langsung

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-CAT-38 | Create-Update-Delete (Manage Asset Master Data: C, U, D) | #7 | `createUpdateDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CUD_PASSWORD` |
  | TC-FA-CAT-39 | Group Manager Capability CRUD (Manage Asset Master Data: C, R, U, D) | #9 | `gmCapability_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GMCRUD_PASSWORD` |
  | TC-FA-CAT-40 | Group Manager Tanpa Capability | #8 | `gmNoCapability_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GMNOCAP_PASSWORD` |
  | TC-FA-CAT-41 | Tanpa Role Ini (tanpa capability, bukan Total Control atau Read Only) | #10 | `noCategoryRole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_NOROLE_PASSWORD` |
  | TC-FA-CAT-42 | Capability Read (Global Role Manage Asset Master Data: R saja) | #3 | `capabilityRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CAPREAD_PASSWORD` |
- Login akun aktor pertama (Create-Update-Delete) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pengecualian atas `suite.md`: precondition TC adalah halaman utama FAMS, sehingga hook `beforeEach` membuka halaman utama FAMS (bukan Categories) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Env var `FA_CUD_PASSWORD`, `FA_GMCRUD_PASSWORD`, `FA_GMNOCAP_PASSWORD`, `FA_NOROLE_PASSWORD`, `FA_CAPREAD_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise); baris `Furniture` dan `Tools` dibaca; spec tidak mengubah data.
- URL halaman Settings > Categories untuk langkah akses langsung dibaca dari fixture (kunci ditetapkan tim FE; URL tidak tertulis di TC).
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun aktor yang membuka halaman Categories (Create-Update-Delete dan Group Manager Capability CRUD).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-38: Visibilitas elemen Categories List untuk aktor Create-Update-Delete

1. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
2. Verifikasi Create-Update-Delete: menu `Settings > Categories` Show
3. Verifikasi Create-Update-Delete: halaman Categories terbuka (aktor memiliki Read)
4. Verifikasi Create-Update-Delete: sidebar `[+] Category` Show
5. Klik elipsis (⋯) pada baris `Furniture`
6. Verifikasi Create-Update-Delete: row action Detail, + Add Subcategory, Edit, Delete Show pada baris `Furniture`
7. Tutup menu row action
8. Verifikasi Create-Update-Delete: checkbox baris Show
9. Centang checkbox baris `Tools`
10. Verifikasi Create-Update-Delete: Bulk Action Bar `[Delete]` Show
11. Hapus centang checkbox baris `Tools`
12. Verifikasi Create-Update-Delete: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

### TC-FA-CAT-39: Visibilitas elemen Categories List untuk aktor Group Manager Capability CRUD

13. Logout dari akun Create-Update-Delete
14. Login sebagai Group Manager Capability CRUD (`gmCapability_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_GMCRUD_PASSWORD`)
15. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
16. Verifikasi Group Manager Capability CRUD: menu `Settings > Categories` Show
17. Verifikasi Group Manager Capability CRUD: halaman Categories terbuka (aktor memiliki Read)
18. Verifikasi Group Manager Capability CRUD: sidebar `[+] Category` Show
19. Klik elipsis (⋯) pada baris `Furniture`
20. Verifikasi Group Manager Capability CRUD: row action Detail, + Add Subcategory, Edit, Delete Show pada baris `Furniture`
21. Tutup menu row action
22. Verifikasi Group Manager Capability CRUD: checkbox baris Show
23. Centang checkbox baris `Tools`
24. Verifikasi Group Manager Capability CRUD: Bulk Action Bar `[Delete]` Show
25. Hapus centang checkbox baris `Tools`
26. Verifikasi Group Manager Capability CRUD: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

### TC-FA-CAT-40: Group Manager tanpa capability Manage Asset Master Data tidak memiliki akses menu

27. Logout dari akun Group Manager Capability CRUD
28. Login sebagai Group Manager Tanpa Capability (`gmNoCapability_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_GMNOCAP_PASSWORD`)
29. Perhatikan sidebar navigasi FAMS
30. Verifikasi Group Manager Tanpa Capability: item menu lain pada sidebar navigasi FAMS tampil
31. Verifikasi Group Manager Tanpa Capability: item menu `Settings > Categories` Hidden total (tier Group Manager saja tidak memberi akses)
32. Buka URL halaman Settings > Categories langsung di address bar
33. Verifikasi Group Manager Tanpa Capability: toast error `You don't have permission to do this.` tampil
34. Verifikasi Group Manager Tanpa Capability: UI di-refresh agar elemen tak berhak tersembunyi, tanpa redirect ke halaman unauthorized

### TC-FA-CAT-41: Aktor tanpa capability: item sidebar Hidden dan akses URL langsung ditolak

35. Logout dari akun Group Manager Tanpa Capability
36. Login sebagai Tanpa Role Ini (`noCategoryRole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_NOROLE_PASSWORD`)
37. Perhatikan sidebar navigasi FAMS
38. Verifikasi Tanpa Role Ini: item menu lain pada sidebar navigasi FAMS tampil
39. Verifikasi Tanpa Role Ini: item menu `Settings > Categories` Hidden total (tidak muncul di daftar menu sama sekali)
40. Buka URL halaman Settings > Categories langsung di address bar
41. Verifikasi Tanpa Role Ini: toast error `You don't have permission to do this.` tampil
42. Verifikasi Tanpa Role Ini: UI di-refresh agar elemen tak berhak tersembunyi, tanpa redirect ke halaman unauthorized

### TC-FA-CAT-42: Item sidebar Settings > Categories Show untuk aktor dengan satu capability saja (Read)

43. Logout dari akun Tanpa Role Ini
44. Login sebagai Capability Read (`capabilityRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_CAPREAD_PASSWORD`)
45. Perhatikan sidebar navigasi FAMS
46. Verifikasi Capability Read: item `Settings > Categories` Show karena aktor memiliki minimal satu capability (Read)

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Spec Role Matrix visibilitas (bagian 3a): satu daftar elemen, banyak role, hasil berbeda per role; polaritas Show dan Hidden dicampur.
- Langkah penghubung (S-03): tiap langkah "Tutup menu row action" dan "Hapus centang checkbox baris `Tools`", serta pasangan logout dan login di awal tiap blok sesudah blok pertama (ganti akun eksplisit; akun pertama login di hook `before`, S-07).
- Pada blok TC-FA-CAT-38 dan TC-FA-CAT-39, langkah "Centang checkbox baris `Tools` bila checkbox tampil" ditulis deterministik: Expected menyatakan checkbox Show sehingga checkbox dicentang.
- Urutan (S-10): TC-FA-CAT-42 diletakkan terakhir (ganti akun ke Capability Read) agar akun tanpa akses (TC-FA-CAT-40 dan TC-FA-CAT-41) berurutan.
- Anchor absence (bagian 8b butir 2): `Verifikasi` item menu lain pada sidebar yang sama tampil mendahului asersi item `Settings > Categories` Hidden.
- Temuan untuk QA:
  - TC-FA-CAT-40 dan TC-FA-CAT-41 menyebut URL halaman Settings > Categories tanpa nilai; URL dibaca dari fixture (disediakan tim FE).
  - TC-FA-CAT-42 memakai Capability Read (Pre-setup #3) yang tidak disebut Precondition (hanya Login sbg Role); spec memakai Pre-setup #3 sesuai nama role.
  - Nama env var password per role tidak tertulis di TC; diusulkan spec dan perlu keputusan tim.
- Ukuran spec (46 langkah, melewati sekitar 35): Role Matrix mengulang urutan langkah untuk tiap role (bagian 3a) dan tiap klausa Expected menjadi satu `Verifikasi` (S-01). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, keputusan 2026-10-30) dan hasil tiap role berbeda; tiap blok berdiri sendiri (login ulang eksplisit di awal blok) sehingga bagian sesudahnya tetap bermakna walau blok sebelumnya gagal; spec tidak dipecah.
- Spec melewati 35 langkah (46 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
