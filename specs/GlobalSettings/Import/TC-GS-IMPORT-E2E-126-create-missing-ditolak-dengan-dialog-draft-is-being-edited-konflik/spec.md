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
3. Admin kedua Client C (sesi API): mulai sesi edit baris #4 hingga kunci edit tersimpan
4. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
5. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan satu tombol `[OK]`
6. Klik `[OK]` pada dialog
7. Verifikasi dialog tertutup
8. Verifikasi Staging Table tetap menampilkan 4 baris `error`
9. Verifikasi Error Summary Callout tetap memuat "Division not found" dengan badge "4 rows"
10. Verifikasi Error Summary Callout tidak memuat baris pesan baru
11. Buka Global Settings > User > Division
12. Verifikasi daftar Division tidak memuat `Logistik` (5 baris pada tabel)

### TC-GS-IMPORT-725: Create Missing Divisions per-baris ditolak (konflik kunci sesi)

13. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
14. Klik [Upload File] di toolbar dan pilih berkas `user-login-logistik-4.csv`
15. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
16. Admin kedua Client C (sesi API): mulai sesi edit baris #4 hingga kunci edit tersimpan
17. Total Control Client C (halaman Import belum dimuat ulang): klik `⋯` pada baris #1
18. Pilih `[Create Missing Divisions]`
19. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan satu tombol `[OK]`
20. Klik `[OK]` pada dialog
21. Verifikasi dialog tertutup
22. Verifikasi Staging Table tetap menampilkan 4 baris `error`
23. Verifikasi Error Summary Callout tetap memuat "Division not found" dengan badge "4 rows"
24. Verifikasi Error Summary Callout tidak memuat baris pesan baru
25. Buka Global Settings > User > Division
26. Verifikasi daftar Division tidak memuat `Logistik` (5 baris pada tabel)

### TC-GS-IMPORT-726: Create Missing Positions per-baris ditolak (konflik kunci sesi)

27. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
28. Klik [Upload File] di toolbar dan pilih berkas `user-login-store-supervisor-3.csv`
29. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
30. Admin kedua Client C (sesi API): mulai sesi edit baris #3 hingga kunci edit tersimpan
31. Total Control Client C (halaman Import belum dimuat ulang): klik `⋯` pada baris #1
32. Pilih `[Create Missing Positions]`
33. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan satu tombol `[OK]`
34. Klik `[OK]` pada dialog
35. Verifikasi dialog tertutup
36. Verifikasi Staging Table tetap menampilkan 3 baris `error`
37. Verifikasi Error Summary Callout tetap memuat "Position not found" dengan badge "3 rows"
38. Verifikasi Error Summary Callout tidak memuat baris pesan baru
39. Buka Global Settings > User > Position
40. Verifikasi daftar Position tidak memuat `Store Supervisor` (5 baris pada tabel)

### TC-GS-IMPORT-727: Create Missing Positions bulk ditolak (konflik kunci sesi)

41. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
42. Klik [Upload File] di toolbar dan pilih berkas `user-login-store-supervisor-3.csv`
43. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
44. Admin kedua Client C (sesi API): mulai sesi edit baris #3 hingga kunci edit tersimpan
45. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
46. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan satu tombol `[OK]`
47. Klik `[OK]` pada dialog
48. Verifikasi dialog tertutup
49. Verifikasi Staging Table tetap menampilkan 3 baris `error`
50. Verifikasi Error Summary Callout tetap memuat "Position not found" dengan badge "3 rows"
51. Verifikasi Error Summary Callout tidak memuat baris pesan baru
52. Buka Global Settings > User > Position
53. Verifikasi daftar Position tidak memuat `Store Supervisor` (5 baris pada tabel)

### TC-GS-IMPORT-919: Create Missing Options bulk dan per-baris ditolak (konflik kunci sesi)

54. Lepas kunci edit Admin kedua, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
55. Klik [Upload File] di toolbar dan pilih berkas `user-login-shift-lembur.csv`
56. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
57. Admin kedua Client C (sesi API): mulai sesi edit baris #3 hingga kunci edit tersimpan
58. Total Control Client C (halaman Import belum dimuat ulang): klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
59. Verifikasi dialog blok dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan satu tombol `[OK]`
60. Klik `[OK]` pada dialog
61. Verifikasi dialog tertutup
62. Verifikasi Staging Table tetap menampilkan baris #1 dan #2 berstatus `error`
63. Verifikasi Error Summary Callout "Shift: Invalid option" dengan badge "2 rows"
64. Klik `⋯` pada baris #1 lalu pilih `[Create Missing Options]`
65. Verifikasi dialog blok yang sama tampil (Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", satu tombol `[OK]`)
66. Klik `[OK]` pada dialog
67. Verifikasi dialog tertutup tanpa perubahan pada Staging Table
68. Buka Global Settings > User > Custom Field
69. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-338, 725, 726, 727, 919).
- P-2: Admin kedua Client C hanya memicu state (memegang kunci edit) lewat sesi API dan tidak menjadi objek asersi; asersi seluruhnya di sesi Total Control Client C. Lima TC konflik kunci tetap di spec ini bersama pola Create Missing (bukan kelas c) karena objek ujinya penolakan aksi Create Missing; bila slice lain memakai spec kelas c untuk dialog Draft Is Being Edited, kelimanya dipindah serentak.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (338, 725, 726, 727, 919) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13, 27, 41, dan 54 (lepas kunci edit Admin kedua dan reset draft supaya precondition tiap TC terpenuhi, Kontrak Fixture R1); langkah 6, 20, 34, 47, 60, dan 66 menutup dialog dengan `[OK]`; langkah 11, 25, 39, 52, dan 68 berpindah surface untuk verifikasi master data.
- Spec berisi 69 langkah, di atas sekitar 35 langkah. Alasan: lima blok berbentuk sama (unggah, Admin kedua memegang kunci, aksi Create Missing, verifikasi dialog dan draft tidak berubah), tiap blok berdiri sendiri dengan draft dan kunci yang di-reset di langkah pembuka, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-IMPORT-338, 725, 726, dan 727 menulis "klik `[Cancel]` pada dialog" di Langkah Uji, sedangkan Expected menyatakan dialog hanya memuat satu tombol `[OK]` (TC-GS-IMPORT-919 memakai `[OK]`). Spec mengikuti Expected dan mengklik `[OK]`.
  - Mekanisme Admin kedua memegang kunci edit lewat sesi API tidak didefinisikan TC, PRD, atau Kontrak Fixture; TC menulisnya sebagai langkah UI (`⋯` baris lalu `Edit`). Spec memakai sesi API sesuai P-2 dan menyebutnya kemampuan disediakan tim FE/BE tanpa mengarang endpoint.
  - Post Condition "Sesi edit Admin kedua Client C tetap berjalan" pada TC-GS-IMPORT-338, 725, 726, 727, dan 919 tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Post Condition "Draft User Login Client C berisi N baris `error`" diamati lewat Staging Table pada langkah verifikasi, bukan lewat pembacaan data BE.
