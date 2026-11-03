---
id: TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi
title: "Resilience Download: Toast Error Tanpa Ekstensi dan Nol Baris Tetap Mengunduh Header"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-185
  - TC-FA-LIC-224
  - TC-FA-LIC-228
  - TC-FA-LIC-361
  - TC-FA-LIC-561
  - TC-FA-LIC-583
coverage:
  web: automated
---

# Resilience Download: Toast Error Tanpa Ekstensi dan Nol Baris Tetap Mengunduh Header

## Prerequisites

- Mode: FE+BE. Kegagalan dipaksa dengan `Spectra.intercept()` di atas backend nyata (bagian 6): request unduh dijawab 500 hanya pada langkah yang menyebutnya, dan intercept dilepas segera setelah asersi toast (S-09). Endpoint request unduh tiap permukaan tidak tercantum di TC; pencocokan request disediakan tim FE (S-13).
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup (hanya dibaca): #12 (kuota dan hierarki PT Sejahtera), #13 (4 term Subscription dan 6 alokasi), #27 (riwayat Changelog Allocation Quota, 6 entri), dan #31 (riwayat Changelog Concurrent User, 4 entri), lewat `Fixture.fixedAssetLicense.kuotaHierarki`, `.riwayat`, `.changelogAllocationQuota`, dan `.changelogConcurrentUser` (fixture belum ada; disediakan tim FE/BE).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV (nama berkas, baris header, jumlah baris); berkas tiap unduhan ditangkap ke direktori bersih sehingga "tidak ada berkas terunduh" dapat diamati.
- Jeda toast: "tidak hilang otomatis" diamati dengan menunggu 10 detik nyata (pilihan spec; TC dan PRD tidak menyebut durasi toast otomatis, di bawah batas 30 detik bagian 6).
- State yang diubah dan dipulihkan: intercept (dilepas pada langkah 7, 12, 26, 43, 48, dan 54) dan Search tiap tabel riwayat (dibersihkan pada langkah 21 dan 35).

## Test Steps

### TC-FA-LIC-185: Kegagalan Download License Summary

1. Pasang intercept: request unduh License Summary dijawab 500
2. Klik ikon Download pada header SectionCard `License Summary`, lalu pilih `Download as CSV`
3. Verifikasi toast error `Error, failed to download License-Summary.` tampil
4. Tunggu 10 detik tanpa menutup toast
5. Verifikasi toast error tetap tampil (tidak hilang otomatis)
6. Verifikasi tidak ada berkas terunduh
7. Lepas intercept, lalu tutup toast error

### TC-FA-LIC-224: Kegagalan Download Subscription History dan nol baris

8. Klik sub-tab `Subscription History`
9. Pasang intercept: request unduh Subscription History dijawab 500
10. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV`
11. Verifikasi toast error `Error, failed to download License-Subscription-History.` tampil
12. Lepas intercept, lalu tutup toast error
13. Ketik Search `zzzz`, tekan Enter
14. Verifikasi tabel menampilkan empty state `No results found`
15. Verifikasi tombol Download tetap aktif
16. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV`
17. Verifikasi tidak ada toast
18. Buka isi berkas yang terunduh
19. Verifikasi berkas memuat header kolom visible `Subscription ID`, `Plan`, `Type`, `Status`, `Start Date`, `End Date`, dan `Plan Owner`
20. Verifikasi berkas tidak memuat baris data
21. Klik `(←)` pada kotak Search

### TC-FA-LIC-228: Kegagalan Download Allocation History dan nol baris

22. Klik sub-tab `Allocation History`
23. Pasang intercept: request unduh Allocation History dijawab 500
24. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV`
25. Verifikasi toast error `Error, failed to download License-Allocation-History.` tampil
26. Lepas intercept, lalu tutup toast error
27. Ketik Search `zzzz`, tekan Enter
28. Verifikasi tabel menampilkan empty state `No results found`
29. Verifikasi tombol Download tetap aktif
30. Klik ikon Download pada toolbar tabel, lalu pilih `Download as CSV`
31. Verifikasi tidak ada toast
32. Buka isi berkas yang terunduh
33. Verifikasi berkas memuat header kolom visible `Allocation ID`, `Subscription ID`, `License Type`, `Quantity`, `Status`, `Date`, `End Date`, `Plan Owner`, dan `Last Updated`
34. Verifikasi berkas tidak memuat baris data
35. Klik `(←)` pada kotak Search

### TC-FA-LIC-561: Kegagalan Download Allocation Quota

36. Klik Tab `Allocation Quota`
37. Pasang intercept: request unduh Allocation Quota dijawab 500
38. Klik ikon Download pada toolbar Section 2, lalu pilih `Download as CSV`
39. Verifikasi toast error `Error, failed to download License-Allocation-Quota.` tampil
40. Tunggu 10 detik tanpa menutup toast
41. Verifikasi toast error tetap tampil (tidak hilang otomatis)
42. Verifikasi tidak ada berkas terunduh
43. Lepas intercept, lalu tutup toast error

### TC-FA-LIC-361: Kegagalan Download modal Changelog: Allocation Quota

44. Klik ikon Changelog pada toolbar Section 2 untuk membuka modal `Changelog: Allocation Quota`
45. Pasang intercept: request unduh Changelog Allocation Quota dijawab 500
46. Klik Download pada modal, lalu pilih `Download as CSV`
47. Verifikasi toast error `Error, failed to download Changelog-Allocation-Quota.` tampil
48. Lepas intercept, tutup toast error, lalu tutup modal Changelog

### TC-FA-LIC-583: Kegagalan Download modal Changelog: Concurrent User

49. Klik Tab `Concurrent User`
50. Klik ikon Changelog pada toolbar tab untuk membuka modal `Changelog: Concurrent User`
51. Pasang intercept: request unduh Changelog Concurrent User dijawab 500
52. Klik Download pada modal, lalu pilih `Download as CSV`
53. Verifikasi toast error `Error, failed to download Changelog-Concurrent-User.` tampil
54. Lepas intercept, tutup toast error, lalu tutup modal Changelog

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (54 langkah). Alasan: seluruh blok satu kelas harness (b, kegagalan unduh yang dipaksa) dengan pola identik per permukaan Download (enam permukaan), memakai data Pre-setup yang hanya dibaca, dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4 dan 40 (jeda 10 detik), langkah 7, 12, 26, 43, 48, dan 54 (melepas intercept; S-09, serta menutup toast dan modal; R-12), langkah 8, 22, 36, dan 49 (membuka sub-tab atau tab sebagai aksi deterministik), langkah 18 dan 32 (membuka isi berkas), langkah 21 dan 35 (pemulihan Search; S-09), langkah 44 dan 50 (membuka modal Changelog dari toolbar; TC-FA-LIC-583 menulis "Popup Changelog: Concurrent User").
- Asersi di luar Expected TC (S-03): langkah 14 dan 28 (empty state `No results found`) adalah anchor positif bahwa Search sudah diproses sebelum asersi berkas nol baris; langkah 6 dan 42 (tidak ada berkas terunduh) didahului langkah 3 dan 39 (toast error tampil) sebagai anchor bahwa respons gagal sudah diproses (bagian 8b butir 2).
- Absence state sementara (bagian 8b butir 11 dan 5): "tanpa toast" pada nol baris diasersi segera setelah pemicu dan sebelum asersi berkas (langkah 17 dan 31).
- Temuan untuk QA:
  - TC-FA-LIC-185 dan 561 menulis "toast error tidak hilang otomatis" tanpa menyebut durasi pengamatan atau cara menutup toast persisten; spec menunggu 10 detik dan menutup toast sebagai langkah penghubung.
  - TC-FA-LIC-224 dan 228 menulis "Pulihkan jaringan" tanpa menyebut mekanisme; spec melepas intercept (langkah 12 dan 26).
  - TC-FA-LIC-583 menyebut "Popup Changelog: Concurrent User" tanpa menyebut pemicunya; spec membukanya dari ikon Changelog pada toolbar tab Concurrent User (TC-FA-LIC-11 memuat toolbar Changelog tab itu).
  - TC-FA-LIC-185, 224, 228, 361, 561, dan 583 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
