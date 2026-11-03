---
id: TC-FA-CAT-E2E-027-new-category-uppercase-code-helper-text-dan-batas-description
title: "New Category: Helper Text Code, Uppercase Otomatis Code, dan Batas Description 360 Karakter"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-106
  - TC-FA-CAT-105
  - TC-FA-CAT-100
coverage:
  web: automated
---

# New Category: Helper Text Code, Uppercase Otomatis Code, dan Batas Description 360 Karakter

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); hanya dibaca.
- Data milik spec: kategori level 1 `Desc Max new {runId}-027` dengan Description 360 karakter `D` dibuat oleh TC-FA-CAT-100 lewat UI. Hook `after` menghapusnya lewat API.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-106: Helper text Code tampil sejak awal dan dipulihkan setelah error diperbaiki

1. Klik `[+] Category` pada sidebar
2. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tampil di bawah field Code sejak popup dibuka
3. Ketik Code `A!`
4. Verifikasi helper text digantikan `Code contains invalid characters`
5. Hapus karakter `!` sehingga Code berisi `A`
6. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tampil kembali

### TC-FA-CAT-105: Code di-uppercase otomatis saat diketik

7. Ganti Code dengan `ab-1_c.d` (ketik)
8. Verifikasi field menampilkan `AB-1_C.D` (auto-uppercase)
9. Verifikasi tidak ada error karena karakter lolos whitelist
10. Klik icon close (✕)
11. Verifikasi dialog Unsaved Changes tampil
12. Pada dialog klik `[Leave]`

### TC-FA-CAT-100: Description tepat 360 karakter diterima dan 361 karakter menampilkan error (New Category)

13. Klik `[+] Category` pada sidebar
14. Isi Category Name `Desc Max new {runId}-027`
15. Isi Description dengan 361 karakter `D`
16. Verifikasi pesan `Max. 360 characters` tampil langsung saat melebihi batas
17. Klik `[Submit]`
18. Verifikasi Submit diblok dan tidak ada kategori tersimpan (popup tetap terbuka, toast sukses tidak tampil)
19. Hapus satu karakter sehingga Description berisi 360 karakter `D`
20. Klik `[Submit]`
21. Verifikasi toast `Success, category has been created.` tampil
22. Ketik Search `Desc Max new {runId}-027`, tekan Enter
23. Verifikasi Description 360 karakter diterima dan kategori `Desc Max new {runId}-027` tersimpan

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): TC-FA-CAT-105 membuka popup baru pada langkah pertamanya; spec memakai satu sesi popup dari TC-FA-CAT-106 dan mengganti Code (langkah 7). TC-FA-CAT-100 menguji 360 karakter dulu lalu popup baru untuk 361; spec membalik urutan (361 lalu 360) dalam satu popup agar validasi diblokir lebih dulu dan popup tidak dibuka dua kali. Jumlah buka form (langkah 1 dan 13) sama dengan jumlah kejadian menutup (Leave langkah 12 dan Submit sukses langkah 20).
- Langkah penghubung (S-03, R-16): langkah 10 sampai 12 (menutup form dirty secara deterministik, S-08), langkah 19 (mengurangi satu karakter), langkah 22 (Search untuk menemukan baris target).
- Temuan untuk QA:
  - TC-FA-CAT-100 memberi Category Name `Desc Max new` tanpa suffix; spec menambah suffix `{runId}-027` (S-12).
  - TC-FA-CAT-100 langkah 5 tidak mengisi Category Name pada pembukaan popup kedua sehingga penolakan Submit dapat berasal dari Category Name kosong; spec mengisi Category Name agar penolakan hanya dari Description.
