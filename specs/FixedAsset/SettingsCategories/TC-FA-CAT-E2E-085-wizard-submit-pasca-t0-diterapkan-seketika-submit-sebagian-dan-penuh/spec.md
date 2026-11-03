---
id: TC-FA-CAT-E2E-085-wizard-submit-pasca-t0-diterapkan-seketika-submit-sebagian-dan-penuh
title: "Wizard Consolidation Pasca-T-0: Save Selection Diterapkan Seketika, Submit Satu Centang, dan Submit Sebanyak Cap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-292
  - TC-FA-CAT-294
  - TC-FA-CAT-295
coverage:
  web: automated
---

# Wizard Consolidation Pasca-T-0: Save Selection Diterapkan Seketika, Submit Satu Centang, dan Submit Sebanyak Cap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #33 (CatPostT0, plan Starter cap 5, T-0 sudah lewat, belum pernah submit selection): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`. Spec menyimpan seleksi tiga kali sehingga mengubah state client; langkah penghubung memulihkan Pre-setup #33 lewat fixture backend yang disediakan tim FE/BE sebelum TC-FA-CAT-294 dan TC-FA-CAT-295, dan hook `after` memulihkannya bila spec berhenti di tengah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog dengan Action tertentu sebelum aksi (baseline N1, S-12); membaca waktu klik `[Save Selection]` dari jam yang sama dengan jam server (jam browser dan jam server sinkron) sebagai penanda waktu untuk asersi Last Updated (S-12).
- Parameter iterasi langkah 8 sampai 11:

  | Baris |
  |---|
  | `Zeta Vehicle` |
  | `Eta Furniture` |
  | `Theta Heavy` |

- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-292: Save Selection pasca-T-0 diterapkan seketika, Excess untuk yang tidak dicentang, toast T-10

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
3. Catat baseline N1 jumlah baris Changelog `Marked as Excess (Category Consolidation)`
4. Klik `[Save Selection]` dan catat waktu klik (penanda waktu untuk langkah 14)
5. Verifikasi toast sukses `Success, category consolidation has been updated.` tampil
6. Verifikasi popup tertutup
7. Verifikasi baris `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess (redup)
8. Untuk setiap baris di tabel parameter (langkah 8 sampai 11): klik elipsis (⋯) pada baris
9. Verifikasi menu baris memuat Detail dan Delete
10. Verifikasi Edit dan + Add Subcategory Hidden pada menu baris
11. Tutup menu baris
12. Verifikasi Alert Category Consolidation tetap tampil (jumlah kategori 8 masih di atas cap 5)
13. Verifikasi Modified By baris `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berformat `[First Name] [Last Initial]` aktor Total Control
14. Verifikasi Last Updated ketiga baris sama dengan waktu klik `[Save Selection]` yang dicatat pada langkah 4 (toleransi satu menit)
15. Buka Modal Changelog
16. Verifikasi Changelog bertambah tepat tiga baris `Marked as Excess (Category Consolidation)` untuk `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` (N1 + 3)
17. Verifikasi tiap baris baru berisi Field `Excess`, Old Value `Usable`, dan New Value `Excess`
18. Verifikasi Modified By tiap baris baru adalah aktor Total Control
19. Tutup Modal Changelog

### TC-FA-CAT-294: Submit dengan satu centang diterima dan kuota tersisa tidak diisi otomatis

20. Pulihkan Pre-setup #33 lewat fixture dan muat ulang halaman Categories
21. Klik `[Choose Categories]` pada Alert Category Consolidation
22. Centang `Keep usable` pada `Alpha Tech`
23. Klik `[Save Selection]`
24. Verifikasi toast `Success, category consolidation has been updated.` tampil
25. Verifikasi hanya `Alpha Tech` yang berstatus usable
26. Verifikasi `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess (kuota tersisa tidak diisi otomatis)

### TC-FA-CAT-295: Submit tepat sebanyak cap diterima

27. Pulihkan Pre-setup #33 lewat fixture dan muat ulang halaman Categories
28. Klik `[Choose Categories]` pada Alert Category Consolidation
29. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
30. Klik `[Save Selection]`
31. Verifikasi toast `Success, category consolidation has been updated.` tampil (Submit diterima)
32. Verifikasi `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear` berstatus usable
33. Verifikasi `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (33 langkah nominal, sekitar 41 dengan ekspansi langkah 8 sampai 11 untuk tiga baris). Alasan: seluruh blok satu kelas (fungsional Wizard Consolidation pasca-T-0 pada satu client, CatPostT0) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CAT-293 dan TC-FA-CAT-296 (client CatExcess) ada di spec 189.
- Urutan TC: TC-FA-CAT-292 (aksi utama dengan verifikasi menu dan Changelog), lalu TC-FA-CAT-294 dan TC-FA-CAT-295; tiap blok mengubah state client sehingga didahului pemulihan fixture (S-09, S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3 (baseline), 4 (pencatatan waktu klik), 11 (menutup menu), 19 (menutup Modal Changelog), 20 dan 27 (pemulihan fixture dan muat ulang).
- Temuan untuk QA:
  - TC-FA-CAT-292 Expected a dan b di kolom Post Condition ditulis sebagai satu klausa per baris Changelog; spec memecahnya menjadi jumlah baris, isi Field/Old/New, dan Modified By (S-01).
  - TC-FA-CAT-292 menyebut "satu baris per node yang berubah" tanpa baseline; spec memakai selisih +3 terhadap N1 (S-12).
