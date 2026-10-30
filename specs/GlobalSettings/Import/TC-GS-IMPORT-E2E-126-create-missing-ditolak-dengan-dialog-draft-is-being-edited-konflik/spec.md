---
id: TC-GS-IMPORT-E2E-126-create-missing-ditolak-dengan-dialog-draft-is-being-edited-konflik
title: "Create Missing ditolak dengan dialog Draft Is Being Edited (konflik kunci sesi) saat admin lain memegang kunci edit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-338
  - TC-GS-IMPORT-725
  - TC-GS-IMPORT-726
  - TC-GS-IMPORT-727
  - TC-GS-IMPORT-919
coverage:
  web: automated
---

# Create Missing ditolak dengan dialog Draft Is Being Edited (konflik kunci sesi) saat admin lain memegang kunci edit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Pelaku kedua: Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` (Pre-setup), hanya memegang kunci edit lewat sesi API (P-2) dengan `Spectra.env.GS_CLIENTC_TC2_PASSWORD`; tidak ada sesi UI kedua. Kemampuan memulai sesi edit baris atas nama Admin kedua (setara `Edit` pada menu `⋯`) disediakan tim FE/BE; mekanisme tidak disebut TC (lihat Temuan untuk QA).
- Layar awal: hook `beforeEach` suite membuka Import > User Login (Client C).
- Data Pre-setup Client C (tidak diubah): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 baris); Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor` (5 baris); Custom Field Shift (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`. Client C tanpa draft Tab User Login pada awal spec (Kontrak Fixture R1).
- Data Dinamis (fixture baru `Fixture.import.berkas`, disediakan tim QA; berkas User Login standar D-45): `user-login-logistik-4.csv` (4 baris, Division `Logistik`, Position kosong), `user-login-store-supervisor-3.csv` (3 baris, Division `Engineering`, Position `Store Supervisor`), `user-login-shift-lembur.csv` (Data Dinamis D-79; baris #1 Shift `Lembur`, #2 `lembur `, #3 `Siang`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepas kunci edit Admin kedua, Discard Draft Tab User Login Client C lewat reset fixture, dan pastikan Division `Logistik`, Position `Store Supervisor`, serta opsi `Lembur` dan `Piket` tidak ada (kondisi Pre-setup, Kontrak Fixture R2).
- Layanan AI mock mode normal (D-40): disetel di hook `before`, dikembalikan di hook `after`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- State global: kunci edit draft dan master data Client C; suite berjalan serial (`parallel: false`).
- Env var: `GS_CLIENTC_TC_PASSWORD`, `GS_CLIENTC_TC2_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-338: Create Missing Divisions bulk ditolak (konflik kunci sesi)

1. Klik [Upload File] di toolbar dan pilih berkas `user-login-logistik-4.csv`
2. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
3. Tunggu aksi selesai (Modal Column Mapping tertutup)
4. Admin kedua Client C (sesi API): mulai sesi edit baris #4 hingga kunci edit tersimpan
5. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
6. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
7. Klik `[Cancel]` pada dialog
8. Verifikasi dialog tertutup
9. Verifikasi Staging Table tetap menampilkan 4 baris `error`
10. Verifikasi Error Summary Callout tetap memuat "Division not found" dengan badge "4 rows"
11. Verifikasi Error Summary Callout tidak memuat baris pesan baru
12. Buka Global Settings > User > Division
13. Verifikasi daftar Division tidak memuat `Logistik` (5 baris pada tabel)

### TC-GS-IMPORT-725: Create Missing Divisions per-baris ditolak (konflik kunci sesi)

14. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
15. Klik [Upload File] di toolbar dan pilih berkas `user-login-logistik-4.csv`
16. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
17. Tunggu aksi selesai (Modal Column Mapping tertutup)
18. Admin kedua Client C (sesi API): mulai sesi edit baris #4 hingga kunci edit tersimpan
19. Total Control Client C (halaman Import belum dimuat ulang): klik `⋯` pada baris #1
20. Pilih `[Create Missing Divisions]`
21. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
22. Klik `[Cancel]` pada dialog
23. Verifikasi dialog tertutup
24. Verifikasi Staging Table tetap menampilkan 4 baris `error`
25. Verifikasi Error Summary Callout tetap memuat "Division not found" dengan badge "4 rows"
26. Verifikasi Error Summary Callout tidak memuat baris pesan baru
27. Buka Global Settings > User > Division
28. Verifikasi daftar Division tidak memuat `Logistik` (5 baris pada tabel)

### TC-GS-IMPORT-726: Create Missing Positions per-baris ditolak (konflik kunci sesi)

29. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
30. Klik [Upload File] di toolbar dan pilih berkas `user-login-store-supervisor-3.csv`
31. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
32. Tunggu aksi selesai (Modal Column Mapping tertutup)
33. Admin kedua Client C (sesi API): mulai sesi edit baris #3 hingga kunci edit tersimpan
34. Total Control Client C (halaman Import belum dimuat ulang): klik `⋯` pada baris #1
35. Pilih `[Create Missing Positions]`
36. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
37. Klik `[Cancel]` pada dialog
38. Verifikasi dialog tertutup
39. Verifikasi Staging Table tetap menampilkan 3 baris `error`
40. Verifikasi Error Summary Callout tetap memuat "Position not found" dengan badge "3 rows"
41. Verifikasi Error Summary Callout tidak memuat baris pesan baru
42. Buka Global Settings > User > Position
43. Verifikasi daftar Position tidak memuat `Store Supervisor` (5 baris pada tabel)

### TC-GS-IMPORT-727: Create Missing Positions bulk ditolak (konflik kunci sesi)

44. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
45. Klik [Upload File] di toolbar dan pilih berkas `user-login-store-supervisor-3.csv`
46. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
47. Tunggu aksi selesai (Modal Column Mapping tertutup)
48. Admin kedua Client C (sesi API): mulai sesi edit baris #3 hingga kunci edit tersimpan
49. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
50. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
51. Klik `[Cancel]` pada dialog
52. Verifikasi dialog tertutup
53. Verifikasi Staging Table tetap menampilkan 3 baris `error`
54. Verifikasi Error Summary Callout tetap memuat "Position not found" dengan badge "3 rows"
55. Verifikasi Error Summary Callout tidak memuat baris pesan baru
56. Buka Global Settings > User > Position
57. Verifikasi daftar Position tidak memuat `Store Supervisor` (5 baris pada tabel)

### TC-GS-IMPORT-919: Create Missing Options bulk dan per-baris ditolak (konflik kunci sesi)

58. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
59. Klik [Upload File] di toolbar dan pilih berkas `user-login-shift-lembur.csv`
60. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
61. Tunggu aksi selesai (Modal Column Mapping tertutup)
62. Admin kedua Client C (sesi API): mulai sesi edit baris #3 hingga kunci edit tersimpan
63. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
64. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
65. Klik `[Cancel]` pada dialog
66. Verifikasi dialog tertutup
67. Verifikasi Staging Table tetap menampilkan baris #1 dan #2 berstatus `error`
68. Verifikasi Error Summary Callout "Shift: Invalid option" dengan badge "2 rows"
69. Klik `⋯` pada baris #1 lalu pilih `[Create Missing Options]`
70. Verifikasi dialog blok yang sama tampil (Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", tombol `[Cancel]` dan `[Take Over Session]`)
71. Klik `[Cancel]` pada dialog
72. Verifikasi dialog tertutup tanpa perubahan pada Staging Table
73. Buka Global Settings > User > Custom Field
74. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-338, 725, 726, 727, 919).
- P-2: Admin kedua Client C hanya memicu state (memegang kunci edit) lewat sesi API dan tidak menjadi objek asersi; asersi seluruhnya di sesi Total Control Client C. Lima TC konflik kunci tetap di spec ini bersama pola Create Missing (bukan kelas c) karena objek ujinya penolakan aksi Create Missing; bila slice lain memakai spec kelas c untuk dialog Draft Is Being Edited, kelimanya dipindah serentak.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (338, 725, 726, 727, 919) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14, 29, 44, dan 58 (lepas kunci edit Admin kedua dan reset draft supaya precondition tiap TC terpenuhi, Kontrak Fixture R1); langkah 7, 22, 37, 51, 65, dan 71 menutup dialog dengan `[Cancel]` (kunci tetap pada Admin kedua, tidak ada ambil alih); langkah 12, 27, 42, 56, dan 73 berpindah surface untuk verifikasi master data. Langkah 3, 17, 32, 47, 61 (Tunggu aksi selesai: menunggu aksi tanpa `Verifikasi` selesai sebelum Admin kedua memulai sesi edit baris lewat sesi API; penanda Modal Column Mapping tertutup).
- Spec berisi 74 langkah, di atas sekitar 35 langkah. Alasan: lima blok berbentuk sama (unggah, Admin kedua memegang kunci, aksi Create Missing, verifikasi dialog dan draft tidak berubah), tiap blok berdiri sendiri dengan draft dan kunci yang di-reset di langkah pembuka, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Expected TC-GS-IMPORT-338, 725, 726, 727, dan 919 menyatakan dialog "Draft Is Being Edited" hanya memuat satu tombol `[OK]`, sedangkan PRD `import.md` §4.1 butir 6 (Dialog Konflik Kunci Sesi), EC-31, dan IMP-LOGIC-04 menetapkan tombol `[Cancel]` dan `[Take Over Session]` untuk `[Create Missing ...]` yang ditolak karena kunci sesi (`[OK]` saja hanya untuk `[Save]` yang memuat baris terhapus, bukan aksi ini). Spec mengikuti PRD: dialog diasersi dengan kedua tombol itu dan ditutup dengan `[Cancel]`, sesuai Langkah Uji TC-338, 725, 726, 727 (klik `[Cancel]`); Expected kelima TC perlu diselaraskan oleh QA.
  - Mekanisme Admin kedua memegang kunci edit lewat sesi API tidak didefinisikan TC, PRD, atau Kontrak Fixture; TC menulisnya sebagai langkah UI (`⋯` baris lalu `Edit`). Spec memakai sesi API sesuai P-2 dan menyebutnya kemampuan disediakan tim FE/BE tanpa mengarang endpoint.
  - Post Condition "Sesi edit Admin kedua Client C tetap berjalan" pada TC-GS-IMPORT-338, 725, 726, 727, dan 919 tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Post Condition "Draft User Login Client C berisi N baris `error`" diamati lewat Staging Table pada langkah verifikasi, bukan lewat pembacaan data BE.
