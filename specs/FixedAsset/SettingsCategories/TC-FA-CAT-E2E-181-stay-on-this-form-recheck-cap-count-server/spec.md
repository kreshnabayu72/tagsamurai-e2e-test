---
id: TC-FA-CAT-E2E-181-stay-on-this-form-recheck-cap-count-server
title: "Stay on This Form: Server Me-re-check Cap Category Count pada Submit Berikutnya"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-116
  - TC-FA-CAT-517
coverage:
  web: automated
---

# Stay on This Form: Server Me-re-check Cap Category Count pada Submit Berikutnya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatStarter (Pre-setup #27, plan Starter, cap Category count 5), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain). Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- State awal (hook `before`, seed lewat API disediakan tim FE/BE): CatStarter dengan 4 kategori L1 (`Starter A` sampai `Starter D`, count 4, cap 5). Langkah 16 memulihkan CatStarter ke 4 kategori lewat seed API; hook `after` memulihkan ke 4 kategori dan menghapus `Stay Fill 1 {runId}-181` serta `Cap One {runId}-181`.
- Data Dinamis (dibuat spec): `Stay Fill 1 {runId}-181`, `Cap One {runId}-181`. Nama `Stay Fill 2 {runId}-181` dan `Cap Two {runId}-181` ditolak server dan tidak tersimpan.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-116: Re-check cap pada Submit berikutnya

1. Klik `[+] Category` pada sidebar
2. Centang `Stay on this form after submitting`
3. Isi Category Name `Stay Fill 1 {runId}-181`
4. Klik `[Submit]` (count menjadi 5)
5. Verifikasi toast `Success, category has been created.` tampil
6. Verifikasi form tetap terbuka
7. Isi Category Name `Stay Fill 2 {runId}-181`
8. Klik `[Submit]`
9. Verifikasi dialog kontekstual `Cannot Add Category` · `You've reached the category limit for your plan. Upgrade to add more.` · `[OK]` tampil (ditolak server 409)
10. Klik `[OK]`
11. Klik `✕` pada popup
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`
14. Verifikasi baris `Stay Fill 1 {runId}-181` tampil di tabel
15. Verifikasi tidak ada baris `Stay Fill 2 {runId}-181` di tabel

### TC-FA-CAT-517: Stay berulang hingga kuota plan

16. Pulihkan CatStarter ke 4 kategori lewat seed API
17. Muat ulang halaman Categories
18. Klik `[+] Category` pada sidebar
19. Centang `Stay on this form after submitting`
20. Isi Category Name `Cap One {runId}-181`
21. Klik `[Submit]` (count menjadi 5)
22. Verifikasi Submit pertama berhasil (baris `Cap One {runId}-181` tampil di tabel)
23. Verifikasi form tetap terbuka
24. Verifikasi form ter-reset
25. Isi Category Name `Cap Two {runId}-181`
26. Klik `[Submit]`
27. Verifikasi dialog D-01 `Cannot Add Category` · `You've reached the category limit for your plan. Upgrade to add more.` · `[OK]` tampil
28. Klik `[OK]`
29. Klik `✕` pada popup
30. Verifikasi dialog `Unsaved Changes` tampil
31. Klik `[Leave]`
32. Verifikasi tidak ada baris `Cap Two {runId}-181` di tabel

## Notes

- Langkah penghubung (S-03): langkah 10, 28 (menutup dialog), 11 sampai 13 dan 29 sampai 31 (menutup form dirty, S-08), 16 sampai 17 (pemulihan state).
- Asersi "tidak tersimpan" (langkah 15 dan 32) berpijak pada baris pembanding yang tampil di langkah 14 dan 22.
- Alasan di atas sekitar 35 langkah: dua blok TC memakai state CatStarter yang dipulihkan dari seed di antara keduanya; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-116 dan TC-517 tidak menyebut cara menutup popup berisi input yang ditolak; spec menutup lewat `✕` dan dialog `Unsaved Changes`.
  - TC-517 tidak menyebut pemulihan count antar-TC; spec memulihkan lewat seed API.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
