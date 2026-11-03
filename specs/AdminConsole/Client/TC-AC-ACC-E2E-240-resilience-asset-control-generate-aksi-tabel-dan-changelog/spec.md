---
id: TC-AC-ACC-E2E-240-resilience-asset-control-generate-aksi-tabel-dan-changelog
title: "Resilience Tab Asset Control: Generate Gagal, Deactivate dan Revoke Gagal, Error State Tabel, dan Error State Modal Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-319
  - TC-AC-ACC-333
  - TC-AC-ACC-855
  - TC-AC-ACC-856
coverage:
  web: automated
---

# Resilience Tab Asset Control: Generate Gagal, Deactivate dan Revoke Gagal, Error State Tabel, dan Error State Modal Changelog

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk 5xx; kegagalan Global Settings di TC-AC-ACC-333 dipicu di sisi server, bagian 6 konvensi).
- Akun aktor pertama: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (TC-AC-ACC-319 dan 333). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite. Akun kedua (langkah ganti akun): Total Control A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-AC-ACC-855 dan 856). Nama env `AC_CLIENT_ACTIVE_FULL_PASSWORD` baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca; semua aksi gagal sehingga data tidak berubah): C-01 "PT Sejahtera Abadi" (Asset Control Total 3 / Used 2 / Available 1; Station "Gerbang Gudang A" Active dengan Tablet "Tablet Lobi 1" Active; Tab Storage dengan tabel Quota dan Purchase History Storage; Tab Subscription untuk Changelog: Subscription).
- Kemampuan teknis: (1) pemaksaan respons 5xx per jenis permintaan lewat intercept di browser, dilepas segera setelah dipakai (S-09): permintaan data Station List, Quota Storage, Purchase History Storage, Changelog: Client, Changelog: Subscription, dan Changelog: Asset Control, serta permintaan Generate Enrollment QR (respons 500); endpoint mengikuti kontrak modul, dipetakan tim FE; (2) membuat Global Settings tidak terjangkau dari backend Client (kegagalan sisi server, disediakan tim FE/BE) dan memulihkannya di langkah penutup serta di hook `after`.
- State global: Global Settings tidak terjangkau lalu dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-319: Generate gagal: toast error dan tombol aktif kembali

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control
2. Paksa respons permintaan Generate Enrollment QR gagal dengan status 500
3. Klik [Generate Enrollment QR]
4. Verifikasi toast error: "Error, failed to generate enrollment QR."
5. Verifikasi tombol [Generate Enrollment QR] aktif kembali
6. Verifikasi tidak ada QR yang tampil
7. Lepas pemaksaan respons 500

### TC-AC-ACC-333: Deactivate dan Revoke gagal karena Global Settings tidak terjangkau

8. Buat Global Settings tidak terjangkau dari backend Client
9. Buka ⋯ pada Station "Gerbang Gudang A" lalu klik Deactivate, lalu klik [Deactivate] pada dialog
10. Verifikasi toast error: "Error, failed to deactivate station."
11. Verifikasi Status "Gerbang Gudang A" tetap `Active`
12. Klik row "Gerbang Gudang A" untuk expand Tablet List
13. Buka ⋯ pada Tablet "Tablet Lobi 1" lalu klik Revoke, lalu klik [Revoke] pada dialog
14. Verifikasi toast error: "Error, failed to revoke tablet."
15. Verifikasi Status "Tablet Lobi 1" tetap `Active`
16. Pulihkan Global Settings agar terjangkau

### Ganti akun

17. Logout, lalu login sebagai Total Control A-01 (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`)

### TC-AC-ACC-855: Error state tabel Tab Asset Control dan Tab Storage

18. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, dan klik Company Name "PT Sejahtera Abadi"
19. Paksa respons data Station List gagal (5xx), lalu klik Tab Asset Control
20. Verifikasi Station List menampilkan "Unable to load this data." dengan tombol [Try Again]
21. Pulihkan respons, lalu klik [Try Again] pada Station List
22. Verifikasi data Station List tampil normal (baris "Gerbang Gudang A" tampil)
23. Verifikasi state error Station List hilang
24. Paksa respons data tabel Quota Storage gagal (5xx), lalu klik Tab Storage
25. Verifikasi tabel Quota menampilkan "Unable to load this data." dengan tombol [Try Again]
26. Pulihkan respons, lalu klik [Try Again] pada tabel Quota
27. Verifikasi data tabel Quota tampil normal
28. Verifikasi state error tabel Quota hilang
29. Paksa respons data tabel Purchase History Storage gagal (5xx), lalu muat ulang Tab Storage
30. Verifikasi tabel Purchase History Storage menampilkan "Unable to load this data." dengan tombol [Try Again]
31. Pulihkan respons, lalu klik [Try Again] pada tabel Purchase History Storage
32. Verifikasi data tabel Purchase History Storage tampil normal
33. Verifikasi state error tabel Purchase History Storage hilang

### TC-AC-ACC-856: Error state modal Changelog: Client, Subscription, dan Asset Control

34. Klik breadcrumb "Client"
35. Paksa respons data Changelog: Client gagal (5xx), lalu klik [Changelog] di toolbar List
36. Verifikasi modal Changelog: Client menampilkan "Unable to load this data." dengan tombol [Try Again]
37. Pulihkan respons, lalu klik [Try Again] di dalam modal
38. Verifikasi tabel Changelog: Client tampil normal
39. Verifikasi state error Changelog: Client hilang
40. Tutup modal, ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Subscription
41. Paksa respons data Changelog: Subscription gagal (5xx), lalu klik [Changelog]
42. Verifikasi modal Changelog: Subscription menampilkan "Unable to load this data." dengan tombol [Try Again]
43. Pulihkan respons, lalu klik [Try Again] di dalam modal
44. Verifikasi tabel Changelog: Subscription tampil normal
45. Verifikasi state error Changelog: Subscription hilang
46. Tutup modal, lalu klik Tab Asset Control
47. Paksa respons data Changelog: Asset Control gagal (5xx), lalu klik ikon Changelog
48. Verifikasi modal Changelog: Asset Control menampilkan "Unable to load this data." dengan tombol [Try Again]
49. Pulihkan respons, lalu klik [Try Again] di dalam modal
50. Verifikasi tabel Changelog: Asset Control tampil normal
51. Verifikasi state error Changelog: Asset Control hilang
52. Tutup modal

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 18, 40 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 7 dan 16 (melepas pemaksaan respons dan memulihkan Global Settings), langkah 12 (expand row agar Tablet List teramati), langkah 34, 46, 52 (navigasi dan menutup modal).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (b, fault injection), pola identik "paksa gagal, verifikasi error, pulihkan, Try Again"; ganti akun (langkah 17) memakai Step eksplisit dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal keras.
- Pembagian TC lintas spec: Changelog: Loading state (TC-AC-ACC-858) ada di spec 256; pencatatan Changelog saat aksi berhasil di spec 267.
- Temuan untuk QA:
  - TC-AC-ACC-319 menyebut "Mock 500" tanpa menyebut permintaan yang dipaksa; spec memaksa permintaan Generate Enrollment QR. TC-AC-ACC-333 menyebut "Mock GS down" dan tidak menyebut Station atau Tablet target; spec memakai "Gerbang Gudang A" dan "Tablet Lobi 1".
  - TC-AC-ACC-855 langkah 5 memuat ulang Tab Storage tanpa menyebut apakah tabel Quota sudah dipulihkan; spec memulihkannya lebih dulu (langkah 26).
