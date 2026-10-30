---
id: TC-GS-IMPORT-E2E-001-screening-halaman-import-dengan-draft-brand-sub-tab-default-skeleton
title: "Screening Halaman Import dengan Draft Brand, Sub-Tab Default, Skeleton Loading, dan Unsaved Banner Dibaca Admin Kedua"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-7
  - TC-GS-IMPORT-8
  - TC-GS-IMPORT-17
  - TC-GS-IMPORT-20
coverage:
  web: automated
---

# Screening Halaman Import dengan Draft Brand, Sub-Tab Default, Skeleton Loading, dan Unsaved Banner Dibaca Admin Kedua

## Prerequisites

- Mode: FE+BE (backend nyata). Intercept hanya menahan respons pembacaan Staging Table selama 3 detik untuk mengamati skeleton (bukan kelas fault injection) dan dilepas segera setelah respons tiba.
- Suite serial (`parallel: false`) karena spec memakai hook umur draft dan state draft bersama Client A; lihat `suite.md`.
- Akun aktor:
  - Total Control (Client A, Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-7, 8, dan 17. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-20: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_TC2_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk Total Control Client A. TC-GS-IMPORT-17 dan TC-GS-IMPORT-20 membuka menu Import lewat langkah sendiri karena objek ujinya pemuatan halaman atau akun berbeda.
- Data Dinamis (disiapkan lewat skrip fixture di hook `before`, tanpa menjalankan Upload lewat UI):
  - D-01: draft Brand 12 baris `pending` dari `brand-12.csv` pada Client A (nama literal Population D-01 bernama literal karena asersi jumlah dan isi, di-seed idempotent).
  - D-04: draft Division 6 baris `pending` dari `division-6.csv` pada Client A, dibuat oleh akun Total Control (dipakai TC-GS-IMPORT-20).
  - D-76 varian 1: `created_at` job draft Brand (D-01) dan draft Division (D-04) dimundurkan ke tanggal tiga hari sebelum hari uji (hanya seed backdate, bukan batas waktu yang diuji) sehingga Unsaved Banner tampil.
  - Format tanggal General Settings Client A: `dd/MM/yy`.
- Reset: hook `beforeEach` mereset draft dasar Client A ke kondisi Population (Kontrak Fixture R2); hook `after` memulihkan draft dasar dan tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor, lihat `suite.md`.
- Kemampuan teknis: intercept network untuk menunda respons pembacaan Staging Table 3 detik; hook umur draft D-76 (disediakan tim FE/BE); skrip reset/seed draft (disediakan tim FE/BE); ganti akun (logout lalu login); pembacaan gaya terhitung (outline/filled) dan keberadaan icon.
- State global: tidak ada yang diubah selain draft Client A (dipulihkan hook) dan flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### TC-GS-IMPORT-7: Screening halaman Import dengan draft Brand oleh Total Control

1. Amati halaman dari atas ke bawah, kiri ke kanan
2. Verifikasi Header: Breadcrumb `Import > Brand`
3. Verifikasi Header: tombol `[?]` tepat di kanan Breadcrumb
4. Verifikasi Header: tombol icon-only `[Changelog]` paling kanan
5. Verifikasi Header: tidak ada Page Title terpisah di bawah Breadcrumb
6. Verifikasi Sub-Tab: `Brand (aktif) | Measurement | Position | Division | User Login | User Non Login`
7. Verifikasi Unsaved Banner tampil dengan teks `You have an unsaved import from [Date]. [Discard]`
8. Verifikasi [Date] pada Unsaved Banner berisi tanggal tiga hari sebelum hari uji menurut format tanggal General Settings
9. Verifikasi Staging Metric Cards: Total Rows 12 (Active)
10. Verifikasi Staging Metric Cards: Ready to Import 12
11. Verifikasi Staging Metric Cards: Errors 0 (Disabled)
12. Verifikasi Staging Metric Cards: Duplicates 0 (Disabled)
13. Verifikasi Toolbar: sisi kiri kosong (0 baris terpilih)
14. Verifikasi Toolbar: sisi kanan memuat Switch `Edit this page`
15. Verifikasi Toolbar: Button `[Download Template]` bergaya outline
16. Verifikasi Toolbar: Button `[Upload File]` bergaya filled, aksi utama, paling kanan
17. Verifikasi Toolbar: tidak ada Search
18. Verifikasi Toolbar: tidak ada Filter
19. Verifikasi Toolbar: tidak ada dropdown filter status
20. Verifikasi Staging DataTable: kolom `Checkbox | # | Brand Name | Status | Actions`
21. Verifikasi Staging DataTable: 10 baris pertama tampil
22. Verifikasi Pagination: `Showing 1 - 10 of 12 items`
23. Verifikasi Pagination: Rows per page 10
24. Verifikasi Footer: `[Import (12)]`
25. Perhatikan Button `[Download Template]` di toolbar
26. Verifikasi Button `[Download Template]` bertulisan "Download Template" tanpa icon
27. Perhatikan Button `[Upload File]` di toolbar
28. Verifikasi Button `[Upload File]` bertulisan "Upload File" tanpa icon
29. Verifikasi Button `[Upload File]` berada paling kanan di toolbar

### TC-GS-IMPORT-8: Sub-Tab aktif default dan perpindahan ke Division

30. Perhatikan Sub-Tab aktif dan Breadcrumb
31. Verifikasi Sub-Tab `Brand` aktif
32. Verifikasi Breadcrumb `Import > Brand`
33. Klik Sub-Tab Division
34. Verifikasi Sub-Tab `Division` aktif
35. Verifikasi Sub-Tab `Brand` tidak aktif
36. Verifikasi Breadcrumb `Import > Division`
37. Verifikasi segmen terakhir Breadcrumb `Division` berupa label (bukan link)
38. Verifikasi URL berubah ke route tab Division

### TC-GS-IMPORT-17: Skeleton tampil saat Staging Table dimuat

39. Aktifkan intercept network yang menunda respons pembacaan Staging Table selama 3 detik
40. Buka menu Import dari sidebar
41. Perhatikan halaman selama respons tertunda
42. Verifikasi skeleton tampil pada Staging Metric Cards
43. Verifikasi skeleton tampil pada Staging DataTable
44. Verifikasi Header tetap tampil
45. Verifikasi Sub-Tab tetap tampil
46. Verifikasi toolbar tetap tampil
47. Tunggu respons tiba
48. Lepas intercept
49. Verifikasi skeleton diganti Staging Metric Cards
50. Verifikasi Staging DataTable berisi 12 baris draft Brand

### TC-GS-IMPORT-20: Unsaved Banner dibaca admin kedua pada draft bersama

51. Ganti akun: logout dari Total Control Client A
52. Login sebagai Admin kedua Client A dengan `Spectra.env.GS_TC2_PASSWORD`
53. Buka menu Import dari sidebar
54. Klik Sub-Tab Division
55. Perhatikan Unsaved Banner
56. Verifikasi Unsaved Banner tampil untuk akun Admin kedua Client A pada draft yang dibuat akun Total Control
57. Verifikasi tanggal pada banner adalah tanggal tiga hari sebelum hari uji menurut format tanggal General Settings

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: 7, 8, 17, 20. TC-GS-IMPORT-8 klik Sub-Tab Division sehingga TC-GS-IMPORT-17 membuka menu Import ulang (halaman kembali ke Sub-Tab Brand); TC-GS-IMPORT-20 ditaruh terakhir karena ganti akun ke Admin kedua.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 25, 27 (mengamati/memperhatikan elemen sesuai Langkah Uji TC), langkah 41, 48 (lepas intercept, S-09), dan langkah 51 sampai 54 (ganti akun dan navigasi).
- Spec melewati sekitar 35 langkah (57 langkah). Seluruhnya screening baca halaman Import tanpa aksi yang mengubah data; tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain. Pemecahan hanya menambah login dan pembukaan halaman tanpa menambah kelas harness; satu-satunya blok pada akun lain (TC-GS-IMPORT-20) berada di akhir dengan langkah ganti akun eksplisit.
- Penahanan respons 3 detik pada TC-GS-IMPORT-17 hanya untuk mengamati skeleton (bukan kelas fault injection, konvensi bagian 3 prinsip 13 butir b).
- Temuan untuk QA:
  - TC-GS-IMPORT-7, 17, dan 20 menyebut draft dan hook umur (D-76) tanpa mendefinisikan skrip seed/reset dan hook backdate; mekanismenya disediakan tim FE/BE dan tidak dikarang di spec (S-13).
  - Data berkas dan draft memakai nama literal Population (mis. `brand-12.csv`) tanpa suffix `{runId}`; keunikan dijaga lewat reset draft di hook, bukan suffix.
  - TC-GS-IMPORT-7 mensyaratkan Unsaved Banner tampil karena `created_at` dimundurkan; TC-GS-IMPORT-8 dan 17 tidak menyebut apakah banner memengaruhi asersinya (spec tidak mengasersi banner pada kedua TC itu).
