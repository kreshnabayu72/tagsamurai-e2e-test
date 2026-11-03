---
id: TC-FA-CAT-E2E-023-keyboard-form-esc-enter-dan-default-checkbox-stay
title: "Keyboard Form (Esc dan Enter) dan Default Checkbox Stay on This Form"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-74
  - TC-FA-CAT-75
  - TC-FA-CAT-76
  - TC-FA-CAT-113
coverage:
  web: automated
---

# Keyboard Form (Esc dan Enter) dan Default Checkbox Stay on This Form

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); baris `Furniture` dan `Peripheral` (level 1) hanya dibaca. Popup Edit pada `Furniture` hanya dibuka dan ditutup tanpa perubahan.
- Data milik spec: kategori `Enter Cat {runId}-023` dibuat oleh TC-FA-CAT-75 lewat UI. Hook `after` menghapusnya lewat API. TC-FA-CAT-76 tidak menyimpan kategori.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-113: Checkbox Stay on this form default Unchecked dan hanya ada pada form Create

1. Klik `[+] Category` pada sidebar
2. Verifikasi checkbox `Stay on this form after submitting` pada popup New Category Unchecked
3. Klik icon close (✕)
4. Klik elipsis (⋯) pada baris `Peripheral`
5. Klik `+ Add Subcategory`
6. Verifikasi checkbox `Stay on this form after submitting` pada popup New Subcategory Unchecked
7. Klik icon close (✕)
8. Klik elipsis (⋯) pada baris `Furniture`
9. Klik `Edit`
10. Verifikasi footer popup Edit Category tidak memuat checkbox `Stay on this form after submitting`
11. Klik icon close (✕)

### TC-FA-CAT-74: Esc menutup menu row action tanpa dialog atau perubahan data

12. Klik elipsis (⋯) pada baris `Furniture`
13. Tekan `Esc`
14. Verifikasi menu row action tertutup
15. Verifikasi tidak ada dialog dan baris `Furniture` tetap ada

### TC-FA-CAT-76: Enter di textarea Description menyisipkan baris baru dan tidak men-submit

16. Klik `[+] Category` pada sidebar
17. Isi Category Name `Enter Area Cat`
18. Klik Description lalu ketik `Baris 1`, tekan `Enter`, ketik `Baris 2`
19. Verifikasi textarea berisi dua baris `Baris 1` dan `Baris 2`
20. Verifikasi form tidak ter-submit dan popup tetap terbuka tanpa toast
21. Klik icon close (✕)
22. Verifikasi dialog Unsaved Changes tampil
23. Pada dialog klik `[Leave]`

### TC-FA-CAT-75: Enter pada field satu baris men-submit form yang valid

24. Klik `[+] Category` pada sidebar
25. Isi Category Name `Enter Cat {runId}-023`
26. Tekan `Enter` saat fokus di Category Name
27. Verifikasi toast `Success, category has been created.` tampil
28. Ketik Search `Enter Cat {runId}-023`, tekan Enter
29. Verifikasi kategori `Enter Cat {runId}-023` tersimpan (baris tampil di tabel)

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan (S-10): TC-FA-CAT-113 (screening default checkbox) di awal, TC-FA-CAT-74 dan TC-FA-CAT-76 (tanpa menyimpan) sebelum TC-FA-CAT-75 (aksi sukses menyimpan data) di akhir.
- Langkah penghubung (S-03, R-16): langkah 3, 7, dan 11 (menutup popup bersih), langkah 28 (Search untuk menemukan baris target).
- Nama `Enter Area Cat` tidak disimpan dan ditulis literal; `Enter Cat` diberi suffix karena tersimpan (S-12).
- Temuan untuk QA:
  - TC-FA-CAT-113 Expected a menyebut checkbox pada popup New Category dan New Subcategory, tetapi Langkah hanya membuka popup New Category; spec menambah langkah membuka popup New Subcategory (langkah 4 sampai 7) agar setiap butir Expected punya langkah Verifikasi (S-01).
  - TC-FA-CAT-74 diberi HINT `g` tetapi Expected menegasi dialog dan perubahan data hanya lewat anchor baris `Furniture`; diperlakukan fungsional (lihat Temuan untuk QA).
  - TC-FA-CAT-75 Post Condition tidak punya langkah observasi selain toast; spec mengasersi tersimpan lewat Search.
