---
id: TC-AC-PF-E2E-121-isi-entri-changelog-create-edit-dan-rename
title: "Isi Entri Changelog: Create Custom dan Default Plan, Edit Satu atau Beberapa Field, serta Rename"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-520
  - TC-AC-PF-521
  - TC-AC-PF-522
  - TC-AC-PF-523
  - TC-AC-PF-524
coverage:
  web: automated
---

# Isi Entri Changelog: Create Custom dan Default Plan, Edit Satu atau Beberapa Field, serta Rename

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup (target aksi tulis): Dataset Plan A / Dataset Plan C (Pre-setup #21 dan #23): custom plan `Growth Tier` v20 (Group count `25`, Borrowing `Full`) dan default plan `Growth` v5 (Group count `3`, Borrowing `Basic`). Dataset Plan S (Pre-setup #31): default SAMS `Supply Starter` dan `Supply Pro` (Paid sisa slot tersedia). General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Aksi menghapus atau mengubah data Pre-setup. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Data Dinamis (bersuffix per run): custom plan `Paket Log Create {runId}-121` (Product FAMS, Template `Growth`) dan default plan `Supply Log Create {runId}-121` (Product SAMS, Pricing Type Paid). Nama hasil rename `Growth Tier Log` ditulis literal sesuai TC (target `Growth Tier` Pre-setup, pengecualian A-6).
- State global: suite serial (`parallel: false`). Pemulihan `Growth Tier` v20 dan `Growth` v5 ke keadaan awal dijamin Fixture BE (idempoten, disediakan tim FE/BE): dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 34, 48, dan 60). `Paket Log Create {runId}-121` dan `Supply Log Create {runId}-121` dihapus di hook `after` lewat Fixture BE. Efek yang tersisa: Last Modified plan Pre-setup, serta entri Changelog (permanen) yang bertambah dan dikembalikan lewat Fixture BE (Pre-setup Dinamis #4).
- Baseline: jumlah entri Changelog tab Custom dan tab Default dicatat sebelum aksi tiap TC lewat kemampuan baca (audit trail permanen; S-12, bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog tab Default dan tab Custom; Fixture BE untuk pemulihan Dataset dan penghapusan plan buatan spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-520: Create custom plan menulis satu entri Create

1. Klik tab `Custom` sub-tab `Active`
2. Catat jumlah entri Changelog tab Custom sebagai baseline
3. Klik `+ Custom Plan` pada toolbar
4. Pilih Product `FAMS`, pilih Template `Growth`, isi Plan Name `Paket Log Create {runId}-121`
5. Klik `[Submit]`
6. Tunggu aksi selesai (Plan Detail `Paket Log Create {runId}-121` terbuka)
7. Kembali ke Plans List tab Custom sub-tab Active
8. Klik ikon Changelog pada toolbar tab Custom
9. Verifikasi Entri teratas: Action `Create`, Plan Name `Paket Log Create {runId}-121`, Field `Plan Name`, Old Value `—`, New Value `Paket Log Create {runId}-121`, Modified By `Andi W`
10. Verifikasi Jumlah entri Changelog tab Custom bertambah tepat satu dari baseline langkah 2
11. Tutup modal Changelog

### TC-AC-PF-521: Create default plan menulis entri Create pada modal Default

12. Klik tab `Default` sub-tab `Active`
13. Catat jumlah entri Changelog tab Default sebagai baseline
14. Klik `+ Default Plan` pada toolbar
15. Pilih Product `SAMS`, pilih Pricing Type `Paid`, isi Plan Name `Supply Log Create {runId}-121`
16. Klik `[Submit]`
17. Tunggu aksi selesai (Plan Detail `Supply Log Create {runId}-121` terbuka)
18. Kembali ke Plans List tab Default sub-tab Active
19. Klik ikon Changelog pada toolbar tab Default
20. Verifikasi Entri teratas modal `Changelog: Plans & Features > Default`: Action `Create`, Plan Name `Supply Log Create {runId}-121`, Field `Plan Name`, Old Value `—`, New Value `Supply Log Create {runId}-121`
21. Verifikasi Jumlah entri Changelog tab Default bertambah tepat satu dari baseline langkah 13
22. Tutup modal Changelog

### TC-AC-PF-522: Edit satu field menulis tepat satu entri Edit

23. Klik tab `Custom` sub-tab `Active`
24. Catat jumlah entri Changelog tab Custom sebagai baseline
25. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
26. Ubah Group count `25` menjadi `3`
27. Klik `[Save]`
28. Tunggu aksi selesai (Plan Detail `Growth Tier` terbuka)
29. Kembali ke Plans List tab Custom sub-tab Active
30. Klik ikon Changelog pada toolbar tab Custom
31. Verifikasi Entri baru: Action `Edit`, Plan Name `Growth Tier`, Field `Group count`, Old Value `25`, New Value `3`
32. Verifikasi Jumlah entri Changelog tab Custom bertambah tepat satu dari baseline langkah 24 (tidak ada entri duplikat)
33. Tutup modal Changelog
34. Pulihkan Dataset Pre-setup (`Growth Tier` v20) lewat Fixture BE

### TC-AC-PF-523: Edit beberapa field default plan menulis satu entri per field

35. Klik tab `Default` sub-tab `Active`
36. Catat jumlah entri Changelog tab Default sebagai baseline
37. Buka Overlay Row Action `Growth`, lalu klik `Edit`
38. Ubah Group count `3` menjadi `25`
39. Ubah Borrowing `Basic` menjadi `Full`
40. Klik `[Save]`
41. Tunggu aksi selesai (Plan Detail `Growth` terbuka)
42. Kembali ke Plans List tab Default sub-tab Active
43. Klik ikon Changelog pada toolbar tab Default
44. Verifikasi Entri baru Action `Edit`, Plan Name `Growth`, Field `Group count`, Old Value `3`, New Value `25`
45. Verifikasi Entri baru Action `Edit`, Plan Name `Growth`, Field `Borrowing`, Old Value `Basic`, New Value `Full`
46. Verifikasi Jumlah entri Changelog tab Default bertambah tepat dua dari baseline langkah 36 (tidak ada entri untuk field yang tidak berubah)
47. Tutup modal Changelog
48. Pulihkan Dataset Pre-setup (`Growth` v5) lewat Fixture BE

### TC-AC-PF-524: Edit yang hanya mengganti Plan Name tanpa kenaikan versi

49. Klik tab `Custom` sub-tab `Active`
50. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
51. Ganti Plan Name menjadi `Growth Tier Log`
52. Klik `[Save]`
53. Tunggu aksi selesai (Plan Detail `Growth Tier Log` terbuka)
54. Kembali ke Plans List tab Custom sub-tab Active
55. Klik ikon Changelog pada toolbar tab Custom
56. Verifikasi Entri baru: Action `Edit`, Plan Name `Growth Tier Log`, Field `Plan Name`, Old Value `Growth Tier`, New Value `Growth Tier Log`
57. Tutup modal Changelog
58. Buka Plan Detail `Growth Tier Log`
59. Verifikasi Judul Plan Detail tetap `v20`
60. Pulihkan Dataset Pre-setup (`Growth Tier` v20) lewat Fixture BE

## Notes

- Langkah penghubung (S-03): buka tab dan sub-tab sebagai precondition TC, "Tunggu aksi selesai" sebelum pindah surface (bagian 8b butir 8), kembali ke Plans List, tutup modal Changelog, dan pemulihan Dataset Pre-setup lewat Fixture BE (langkah 34, 48, 60). Pembuatan data Dinamis (langkah 3 sampai 5 dan 14 sampai 16) mengikuti Langkah TC; jumlah entri dicatat pada langkah 2, 13, 24, dan 36 sebagai baseline (S-12).
- Pembagian TC lintas spec: TC-AC-PF-531 ada di spec 128; TC-AC-PF-525 sampai TC-AC-PF-528 dan TC-AC-PF-530 ada di spec 122.
- Alasan melewati sekitar 35 langkah (60 langkah): kelima TC memakai satu pola (aksi pada plan, lalu baca Changelog), satu dataset, dan satu kelas harness (fungsional). Langkah baca-log tiap TC (kembali ke Plans List, buka Changelog, `Verifikasi` kolom log, tutup modal: langkah 7 sampai 11, 18 sampai 22, 29 sampai 33, 42 sampai 47, dan 54 sampai 57) mengikuti pola buka surface lalu Verifikasi yang tidak dihitung pada ambang menurut bagian 3 prinsip 13; tanpa blok itu spec ini 35 langkah. Sisanya adalah langkah aksi dan pemulihan yang tidak dapat digabung.
- Temuan untuk QA:
  - TC-AC-PF-520 dan TC-AC-PF-521 memakai nama literal `Paket Log Create` dan `Supply Log Create`; spec memberi suffix `{runId}-121` karena plan dibuat spec (S-12) sehingga asersi memakai nama bersuffix.
  - TC-AC-PF-522, TC-AC-PF-523, dan TC-AC-PF-524 mengubah plan Pre-setup (`Growth Tier`, `Growth`) yang slotnya tidak dapat dimiliki spec; dipulihkan lewat Fixture BE (A-6).
  - TC-AC-PF-520 Expected butir a menyebut "Modified By nama singkat aktor" tanpa format; spec memakai `Andi W` (format `[First Name] [Last Initial]`, R-14).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01): TC-AC-PF-523 ("satu versi baru").
  - TC-AC-PF-524 Expected butir b menyebut "Judul Plan Detail tetap v20" tanpa langkah pembuka Plan Detail; spec menambah langkah 58 sebagai langkah penghubung.
