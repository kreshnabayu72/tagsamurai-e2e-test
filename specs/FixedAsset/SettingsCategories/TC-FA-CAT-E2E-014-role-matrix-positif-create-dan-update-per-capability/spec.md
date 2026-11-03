---
id: TC-FA-CAT-E2E-014-role-matrix-positif-create-dan-update-per-capability
title: "Role Matrix Positif: Create dan Update Kategori per Capability"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-43
  - TC-FA-CAT-44
  - TC-FA-CAT-45
  - TC-FA-CAT-48
coverage:
  web: automated
---

# Role Matrix Positif: Create dan Update Kategori per Capability

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-CAT-43, 44 | Create-Only (Manage Asset Master Data: C) | #4 | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CO_PASSWORD` |
  | TC-FA-CAT-45 | Update-Only (Manage Asset Master Data: U) | #5 | `updateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_UO_PASSWORD` |
  | TC-FA-CAT-48 | Group Manager Capability CRUD (Manage Asset Master Data: C, R, U, D) | #9 | `gmCapability_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GMCRUD_PASSWORD` |
- Login akun aktor pertama (Create-Only) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Env var `FA_CO_PASSWORD`, `FA_UO_PASSWORD`, `FA_GMCRUD_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise); L1 `Accessory`, `Default Category`, `Electronics`, `Furniture`, `Peripheral`, `Spare Part`, `Tools`, `Vehicle` dibaca (TC-FA-CAT-48).
- Data milik spec (S-06), di-seed lewat API di hook `before` dan dihapus di hook `after`: `Role Sub Parent-{runId}-014` (L1, leaf, tanpa Asset Name; pengganti `Vehicle` pada TC-FA-CAT-44), `Role Edit Src-{runId}-014` (L1, leaf; pengganti `Vehicle` pada TC-FA-CAT-45), dan `Role GM Edit-{runId}-014` (L1, leaf, Description kosong; pengganti `Furniture` pada TC-FA-CAT-48).
- Data Dinamis dibuat spec dan dihapus di hook `after`: `Role Create Cat-{runId}-014` (TC-FA-CAT-43), `Role Sub Cat-{runId}-014` (TC-FA-CAT-44), hasil rename `Role Edit Dst-{runId}-014` (TC-FA-CAT-45), dan Description `Office furniture items` (TC-FA-CAT-48). Pembersihan tidak berasumsi seeding berhasil penuh.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk ketiga akun aktor.
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-43: Create-Only membuat kategori root sampai sukses

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Role Create Cat-{runId}-014`
3. Klik `[Submit]`
4. Verifikasi toast sukses `Success, category has been created.`
5. Verifikasi baris `Role Create Cat-{runId}-014` tampil di tabel L1
6. Verifikasi node baru `Role Create Cat-{runId}-014` tampil di sidebar
7. Klik elipsis (⋯) pada baris `Role Create Cat-{runId}-014`
8. Verifikasi row action Edit dan Delete Hidden pada baris `Role Create Cat-{runId}-014`
9. Tutup menu row action

### TC-FA-CAT-44: Create-Only menambah subcategory lewat row action + Add Subcategory

10. Klik elipsis (⋯) baris `Role Sub Parent-{runId}-014` > `+ Add Subcategory`
11. Verifikasi Popup New Subcategory terbuka
12. Verifikasi tidak ada dialog heads-up (kategori leaf tidak ditunjuk Asset Name)
13. Isi Category Name `Role Sub Cat-{runId}-014`
14. Klik `[Submit]`
15. Verifikasi toast sukses `Success, category has been created.`
16. Expand node `Role Sub Parent-{runId}-014` di sidebar
17. Verifikasi `Role Sub Parent-{runId}-014` menjadi Internal (memiliki chevron expand/collapse)
18. Verifikasi `Role Sub Cat-{runId}-014` tampil sebagai anak `Role Sub Parent-{runId}-014`

### TC-FA-CAT-45: Update-Only mengubah Category Name sampai sukses

19. Logout dari akun Create-Only
20. Login sebagai Update-Only (`updateOnly_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_UO_PASSWORD`)
21. Buka Fixed Asset > Settings > Categories
22. Klik elipsis (⋯) baris `Role Edit Src-{runId}-014` > `Edit`
23. Ubah Category Name menjadi `Role Edit Dst-{runId}-014`
24. Klik `[Save]`
25. Verifikasi toast sukses `Success, category has been updated.`
26. Verifikasi baris tampil `Role Edit Dst-{runId}-014`
27. Verifikasi sidebar `[+] Category` Hidden
28. Klik elipsis (⋯) pada baris `Role Edit Dst-{runId}-014`
29. Verifikasi row action + Add Subcategory dan Delete Hidden
30. Tutup menu row action

### TC-FA-CAT-48: Group Manager pemegang capability Update mengubah kategori sampai sukses

31. Logout dari akun Update-Only
32. Login sebagai Group Manager Capability CRUD (`gmCapability_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_GMCRUD_PASSWORD`)
33. Buka Fixed Asset > Settings > Categories
34. Klik elipsis (⋯) baris `Role GM Edit-{runId}-014` > `Edit`
35. Ubah Description menjadi `Office furniture items`
36. Klik `[Save]`
37. Verifikasi toast sukses `Success, category has been updated.`
38. Verifikasi sidebar memuat L1 `Accessory`, `Default Category`, `Electronics`, `Furniture`, `Peripheral`, `Spare Part`, `Tools`, dan `Vehicle` (seluruh pohon client yang sama dengan Total Control, master data client-wide tanpa scoping group)

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Spec Role Matrix positif (bagian 3a): aksi berhasil per capability; ditulis per blok role karena ganti akun menuntut Step eksplisit dan langkah tiap role berbeda.
- Penyimpangan data (S-06): TC-FA-CAT-44, 45, dan 48 menyebut `Vehicle` dan `Furniture` (Pre-setup #20) sebagai target tulis; spec memakai kategori milik spec dengan karakter yang sama (leaf tanpa Asset Name) agar data Pre-setup tidak berubah.
- Langkah penghubung (S-03): langkah 9, 30 (menutup menu), langkah 16 (expand node untuk mengamati anak), pasangan logout dan login di awal TC-FA-CAT-45 dan TC-FA-CAT-48 (ganti akun eksplisit; akun pertama login di hook `before`, S-07), serta langkah 21 dan 33 (membuka halaman Categories setelah login).
- Cleanup: kategori hasil Create, hasil Add Subcategory, dan hasil rename dihapus lewat API di hook `after`; satu record tidak sekaligus di daftar hapus dan daftar kembalikan (R-13).
- Temuan untuk QA:
  - TC-FA-CAT-44 butir c (`Vehicle` menjadi Internal) tidak menyebut cara mengamati status Internal; spec mengamati chevron expand/collapse node sesuai TC-FA-CAT-4.
  - TC-FA-CAT-43 butir c dan TC-FA-CAT-45 butir c menyebut aksi yang tidak terlihat tanpa langkah; spec menambah klik elipsis pada baris terkait.
  - TC-FA-CAT-48 butir b tidak memiliki langkah uji; spec membandingkan daftar L1 sidebar dengan Pre-setup #20 yang sama dengan Total Control.
  - Email akun Create-Only, Update-Only, dan Group Manager Capability CRUD dibentuk dari pola Pre-setup #4, #5, dan #9; nama env var password diusulkan spec.
- Ukuran spec 38 langkah, di bawah ambang sekitar 35 atau mendekatinya; blok per akun berdiri sendiri lewat login ulang eksplisit.
- Spec melewati 35 langkah (38 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
