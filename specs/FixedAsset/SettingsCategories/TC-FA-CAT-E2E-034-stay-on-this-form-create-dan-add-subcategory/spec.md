---
id: TC-FA-CAT-E2E-034-stay-on-this-form-create-dan-add-subcategory
title: "Stay on This Form: Create Kategori Root dan Add Subcategory Mempertahankan Popup, Banner, dan Parent"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-114
  - TC-FA-CAT-115
coverage:
  web: automated
---

# Stay on This Form: Create Kategori Root dan Add Subcategory Mempertahankan Popup, Banner, dan Parent

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), dibaca: parent `Peripheral` (Internal).
- Data Dinamis (dibuat spec): `Stay One {runId}-034` (Code `STAY1`, Description `Stay desc`), `Stay Two {runId}-034`, `Stay Sub One {runId}-034` (Code `SSUB1`), `Stay Sub Two {runId}-034` (Code `SSUB2`). Hook `before` menghapus sisa kategori ber-Code `STAY1`, `SSUB1`, `SSUB2`; hook `after` menghapus keempat kategori. Seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-114: Stay on this form pada Create

1. Klik `[+] Category` pada sidebar
2. Centang `Stay on this form after submitting`
3. Isi Category Name `Stay One {runId}-034`, Code `STAY1`, Description `Stay desc`
4. Klik `[Submit]`
5. Verifikasi toast `Success, category has been created.` tampil
6. Verifikasi popup tetap terbuka
7. Verifikasi field Category Name kosong
8. Verifikasi field Code kosong
9. Verifikasi field Description kosong
10. Verifikasi error validasi terhapus
11. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
12. Verifikasi tabel dan sidebar di-refresh (baris dan node `Stay One {runId}-034` tampil)
13. Isi Category Name `Stay Two {runId}-034`
14. Klik `[Submit]`
15. Verifikasi Submit kedua membuat `Stay Two {runId}-034`
16. Verifikasi dialog guard preemptif tidak ditampilkan ulang
17. Klik `✕` pada popup

### TC-FA-CAT-115: Stay on this form pada Add Subcategory

18. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
19. Centang `Stay on this form after submitting`
20. Isi Category Name `Stay Sub One {runId}-034` dan Code `SSUB1`
21. Klik `[Submit]`
22. Verifikasi banner `Adding subcategory under parent: Peripheral` tetap tampil
23. Isi Category Name `Stay Sub Two {runId}-034` dan Code `SSUB2`
24. Klik `[Submit]`
25. Verifikasi field Category Name dan Code dikosongkan
26. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
27. Klik `✕` pada popup
28. Klik node `Peripheral` di Sidebar Category Tree
29. Verifikasi `Stay Sub One {runId}-034` dan `Stay Sub Two {runId}-034` tampil sebagai sibling di bawah `Peripheral`

## Notes

- Urutan (8b butir 5): toast sukses TC-FA-CAT-114 butir b diasersi tepat sesudah `[Submit]` (langkah 5), sebelum asersi state popup, tabel, dan sidebar; TC menuliskannya sesudah asersi tabel.
- Langkah penghubung (S-03): langkah 17 dan 27 (menutup popup dengan form kosong setelah Submit; tidak ada dialog `Unsaved Changes` karena form kosong), langkah 28 (membaca hasil di node `Peripheral`).
- Temuan untuk QA:
  - TC-114 dan TC-115 tidak menyebut cara menutup popup setelah Stay on form; spec menutup dengan `✕` pada form yang sudah kosong dan mengasumsikan tidak ada dialog `Unsaved Changes`.
  - Keadaan awal checkbox Stay tidak disebut TC; spec mencentangnya eksplisit.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
