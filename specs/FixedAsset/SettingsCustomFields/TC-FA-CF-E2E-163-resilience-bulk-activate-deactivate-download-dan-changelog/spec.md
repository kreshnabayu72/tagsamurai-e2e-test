---
id: TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog
title: "Resilience: Bulk Activate dan Deactivate, Download, dan Download Changelog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-338
  - TC-FA-CF-339
  - TC-FA-CF-340
  - TC-FA-CF-424
  - TC-FA-CF-477
  - TC-FA-CF-629
coverage:
  web: automated
---

# Resilience: Bulk Activate dan Deactivate, Download, dan Download Changelog

## Prerequisites

- Mode: FE+BE (backend nyata). Respons 500 dan timeout dipaksa lewat intercept parsial di atas backend nyata (Pre-setup #26); state backend (status keaktifan) tetap diasersi.
- Akun aktor blok pertama: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite.
- Akun aktor blok kedua (ganti akun eksplisit di langkah 48 dan 49): Total Control Company Changelog (Pre-setup #19). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12): `Asset Serial Tag` dan `Storage Capacity` (Active), `Depreciated Ratio` (Inactive), dan `Compliance File` yang dinonaktifkan lewat seed API di hook `before` (disediakan tim FE/BE; dipakai TC-FA-CF-339 dan 629). Company Changelog (Pre-setup #19): dua belas entri log tab General dan dua entri tab Purchasing. Semua aksi gagal sehingga data tidak berubah (S-06). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Kemampuan teknis: intercept dan penundaan respons (`Spectra.intercept`) untuk request Bulk Activate, Bulk Deactivate, dan Download; Bulk Action Bar dengan `Unselect All`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain `Compliance File` yang dinonaktifkan di hook `before`; hook `after` memulihkannya lewat seed reset Company Alpha. Intercept dilepas segera setelah pemicu (S-09). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-338: Bulk Deactivate gagal 5xx

1. Centang dua baris (`Asset Serial Tag` dan `Storage Capacity`)
2. Intersep respons Bulk Deactivate dengan 500
3. Klik `[Deactivate]` pada Bulk Action Bar
4. Klik `[Deactivate]` pada dialog
5. Verifikasi dialog tertutup
6. Verifikasi toast error `Error, failed to deactivate custom field.` tampil
7. Verifikasi tabel di-refresh
8. Verifikasi Bulk Action Bar dan seleksi dipertahankan
9. Verifikasi tidak ada perubahan sebagian (kedua field tetap Active)
10. Lepas intersepsi
11. Tutup toast error
12. Klik `Unselect All`

### TC-FA-CF-339: Bulk Activate gagal 5xx

13. Centang dua field Inactive (`Depreciated Ratio` dan `Compliance File`)
14. Intersep respons Bulk Activate dengan 500
15. Klik `[Activate]` pada Bulk Action Bar
16. Klik `[Activate]` pada dialog
17. Verifikasi toast error `Error, failed to activate custom field.` tampil
18. Verifikasi seleksi dan Bulk Action Bar dipertahankan
19. Lepas intersepsi
20. Tutup toast error
21. Klik `Unselect All`

### TC-FA-CF-340: Bulk Deactivate timeout

22. Centang dua baris (`Asset Serial Tag` dan `Storage Capacity`)
23. Tunda respons Bulk Deactivate melewati batas waktu
24. Klik `[Deactivate]` pada Bulk Action Bar
25. Klik `[Deactivate]` pada dialog
26. Verifikasi toast `Connection problem. Please try again.` tampil
27. Verifikasi tabel di-refresh
28. Verifikasi seleksi dan Bulk Action Bar dipertahankan
29. Lepas tahanan respons
30. Tutup toast
31. Klik `Unselect All`

### TC-FA-CF-629: Bulk Activate timeout

32. Centang `Depreciated Ratio` dan `Compliance File`
33. Tunda respons Bulk Activate melewati batas waktu
34. Klik `[Activate]` pada Bulk Action Bar
35. Klik `[Activate]` pada dialog
36. Verifikasi toast `Connection problem. Please try again.` tampil
37. Verifikasi tabel di-refresh
38. Verifikasi seleksi dan Bulk Action Bar dipertahankan
39. Verifikasi status kedua field tidak berubah (tetap Inactive)
40. Lepas tahanan respons
41. Tutup toast
42. Klik `Unselect All`

### TC-FA-CF-424: Download gagal

43. Intersep request Download dengan 500
44. Klik icon Download > `Download as CSV`
45. Verifikasi toast error `Error, failed to download Custom-Fields.` tampil
46. Lepas intersepsi
47. Tutup toast error

### TC-FA-CF-477: Download Changelog gagal (Company Changelog)

48. Ganti akun: `Logout` dari Total Control Company Alpha
49. Login sebagai Total Control Company Changelog dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`
50. Klik icon Changelog di toolbar
51. Intersep request Download dengan 500
52. Klik icon Download > `Download as CSV`
53. Verifikasi toast error `Error, failed to download Changelog-Custom-Field.` tampil
54. Lepas intersepsi
55. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 55 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kelas b, fault injection pada bulk dan download), berdiri sendiri, dan tiap blok pendek (5 sampai 12 langkah) dengan Verifikasi per klausa (S-01); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Intercept dipakai sebagai pemicu dan dilepas segera setelah pemicu (S-09); toast error berulang ditutup sebelum asersi berikutnya (R-12).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 19, 29, 40, 46, dan 54 (melepas intersepsi atau tahanan), langkah 11, 20, 30, 41, dan 47 (menutup toast), langkah 12, 21, 31, dan 42 (`Unselect All`, S-09), langkah 48 dan 49 (ganti akun eksplisit ke Company Changelog), langkah 55 (menutup Modal Changelog).
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Changelog (Pre-setup #19 hanya mendeskripsikan Company); akun disediakan tim FE.
  - TC-FA-CF-338 dan 340 menyebut "Centang dua baris" tanpa nama; TC-FA-CF-339 menyebut "dua field Inactive" padahal baseline Pre-setup #12 hanya memiliki satu field Inactive (`Depreciated Ratio`); spec memakai `Compliance File` yang dinonaktifkan lewat seed API (seperti Precondition TC-FA-CF-629).
  - TC-FA-CF-424 dan 477 menyebut [File Name] tanpa extension; spec memakai `Custom-Fields` dan `Changelog-Custom-Field` sesuai Expected.
