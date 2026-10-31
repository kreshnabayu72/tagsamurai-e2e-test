---
id: TC-GS-IMPORT-E2E-148-fault-injection-create-missing-divisions-positions-dan-options-tanpa
title: "Fault injection Create Missing Divisions, Positions, dan Options: tanpa respons dan gagal 500, toast sesuai dan baris tetap error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-721
  - TC-GS-IMPORT-722
  - TC-GS-IMPORT-723
  - TC-GS-IMPORT-724
  - TC-GS-IMPORT-927
  - TC-GS-IMPORT-928
coverage:
  web: automated
---

# Fault injection Create Missing Divisions, Positions, dan Options: tanpa respons dan gagal 500, toast sesuai dan baris tetap error

## Prerequisites

- Mode: FE+BE (backend nyata) dengan `Spectra.intercept` parsial di atas backend nyata; asersi memakai state draft dan master data di backend, jadi bukan `Mode: mock`.
- Suite serial (`parallel: false`): draft Client C dibagikan ke seluruh admin dan spec berbagi Client C dengan spec Create Missing lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client C dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE):
  - `Spectra.intercept` di browser: membalas status 500 dan menahan respons tanpa jawaban sampai timeout FE untuk permintaan Create Missing (Divisions, Positions, Options). Intercept dilepas segera setelah pemicu (S-09).
  - Skrip fixture reset Client C ke tanpa draft (Kontrak Fixture R1).
- Data Pre-setup Client C (hanya dibaca, tidak diubah spec ini): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 item; `Logistik` belum ada); Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor` (5 item; `Store Supervisor` belum ada); Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam` (`Lembur` dan `Piket` belum menjadi opsi).
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal sesuai Data Uji TC):
  - `user-login-logistik-4.csv` (D-45): 4 baris Siti Rahmawati, Budi Santoso, Andi Pratama, Rina Wijaya; Division `Logistik`; Position kosong; Access `Global Settings`.
  - `user-login-store-supervisor-1.csv` (D-45): 1 baris Siti Rahmawati; Division `Engineering`; Position `Store Supervisor`.
  - D-79 `user-login-shift-lembur.csv`: baris #1 Siti Rahmawati Shift `Lembur`, baris #2 Budi Santoso Shift `lembur ` (huruf kecil dengan spasi di akhir), baris #3 Andi Pratama Shift `Siang`; Division `Engineering`, Position kosong, Access `Global Settings`. Hasil staging: baris #1 dan #2 `error`, baris #3 `pending`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lepas semua intercept, hapus draft User Login Client C, pastikan Division `Logistik`, Position `Store Supervisor`, dan opsi `Lembur` serta `Piket` tidak ada di Client C (dihapus bila ada), dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-721 dan TC-GS-IMPORT-722: Create Missing Divisions

#### TC-GS-IMPORT-721: tanpa respons

1. Reset Client C ke tanpa draft pada Sub-Tab User Login (aksi fixture)
2. Buka Global Settings > Import, pilih Sub-Tab User Login
3. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-logistik-4.csv`
4. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
5. Pasang intercept yang menahan permintaan Create Missing tanpa jawaban sampai batas waktu
6. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
7. Lepas intercept permintaan Create Missing
8. Verifikasi toast error persisten tanpa tombol aksi: "Connection problem. Please try again."
9. Verifikasi baris tetap `error`
10. Verifikasi Error Summary Callout tetap memuat "Division not found" dengan badge "4 rows"
11. Verifikasi Error Summary Callout tetap memuat `[Create Missing Divisions]`
12. Tutup toast error
13. Buka Global Settings > User > Division
14. Verifikasi tabel Division menampilkan 5 baris
15. Verifikasi daftar Division tidak memuat `Logistik`

#### TC-GS-IMPORT-722: gagal server 500

16. Kembali ke Global Settings > Import, pilih Sub-Tab User Login (draft TC-721 masih berisi 4 baris `error`)
17. Pasang intercept yang membalas permintaan Create Missing dengan status 500
18. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
19. Lepas intercept permintaan Create Missing
20. Verifikasi toast error: "Error, failed to create division."
21. Verifikasi baris tetap `error`
22. Verifikasi Error Summary Callout tetap memuat "Division not found" dengan badge "4 rows"
23. Verifikasi Error Summary Callout tetap memuat `[Create Missing Divisions]`
24. Tutup toast error
25. Buka Global Settings > User > Division
26. Verifikasi tabel Division menampilkan 5 baris
27. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-723 dan TC-GS-IMPORT-724: Create Missing Positions

#### TC-GS-IMPORT-723: tanpa respons

28. Reset Client C ke tanpa draft pada Sub-Tab User Login (aksi fixture)
29. Buka Global Settings > Import, pilih Sub-Tab User Login
30. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-store-supervisor-1.csv`
31. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
32. Pasang intercept yang menahan permintaan Create Missing tanpa jawaban sampai batas waktu
33. Klik `⋯` pada baris #1
34. Pilih `[Create Missing Positions]`
35. Lepas intercept permintaan Create Missing
36. Verifikasi toast error persisten tanpa tombol aksi: "Connection problem. Please try again."
37. Verifikasi baris #1 tetap `error`
38. Verifikasi Error Summary Callout tetap memuat "Position not found" dengan badge "1 row"
39. Verifikasi Error Summary Callout tetap memuat `[Create Missing Positions]`
40. Tutup toast error
41. Buka Global Settings > User > Position
42. Verifikasi tabel Position menampilkan 5 baris
43. Verifikasi daftar Position tidak memuat `Store Supervisor`

#### TC-GS-IMPORT-724: gagal server 500

44. Kembali ke Global Settings > Import, pilih Sub-Tab User Login (draft TC-723 masih berisi 1 baris `error`)
45. Pasang intercept yang membalas permintaan Create Missing dengan status 500
46. Klik `⋯` pada baris #1
47. Pilih `[Create Missing Positions]`
48. Lepas intercept permintaan Create Missing
49. Verifikasi toast error: "Error, failed to create position."
50. Verifikasi baris #1 tetap `error`
51. Verifikasi Error Summary Callout tetap memuat "Position not found" dengan badge "1 row"
52. Verifikasi Error Summary Callout tetap memuat `[Create Missing Positions]`
53. Tutup toast error
54. Buka Global Settings > User > Position
55. Verifikasi tabel Position menampilkan 5 baris
56. Verifikasi daftar Position tidak memuat `Store Supervisor`

### TC-GS-IMPORT-927 dan TC-GS-IMPORT-928: Create Missing Options

#### TC-GS-IMPORT-927: tanpa respons

57. Reset Client C ke tanpa draft pada Sub-Tab User Login (aksi fixture)
58. Buka Global Settings > Import, pilih Sub-Tab User Login
59. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-shift-lembur.csv`
60. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
61. Pasang intercept yang menahan permintaan Create Missing tanpa jawaban sampai batas waktu
62. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
63. Lepas intercept permintaan Create Missing
64. Verifikasi toast error persisten tanpa tombol aksi: "Connection problem. Please try again."
65. Verifikasi baris tetap `error`
66. Verifikasi Error Summary Callout tetap memuat "Shift: Invalid option" dengan badge "2 rows"
67. Verifikasi Error Summary Callout tetap memuat `[Create Missing Options]`
68. Tutup toast error
69. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
70. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam`

#### TC-GS-IMPORT-928: gagal server 500

71. Kembali ke Global Settings > Import, pilih Sub-Tab User Login (draft TC-927 masih berisi 3 baris: 2 `error`, 1 `pending`)
72. Pasang intercept yang membalas permintaan Create Missing dengan status 500
73. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
74. Lepas intercept permintaan Create Missing
75. Verifikasi toast error: "Error, failed to create option."
76. Verifikasi baris tetap `error`
77. Verifikasi Error Summary Callout tetap memuat "Shift: Invalid option" dengan badge "2 rows"
78. Verifikasi Error Summary Callout tetap memuat `[Create Missing Options]`
79. Tutup toast error
80. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
81. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam`

## Notes

- Mode: FE+BE dengan intercept parsial. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fault injection (b); seeding draft lewat UI upload adalah pemicu state (P-2), bukan objek uji.
- Alasan melewati sekitar 35 langkah (81 langkah nominal, tiap pasangan TC sekitar 27 langkah): enam blok homogen (tiga jenis Create Missing, masing-masing dengan varian tanpa respons dan 500), semua satu kelas dan berdiri sendiri dengan reset Client C di awal tiap pasangan, sehingga kegagalan satu pasangan tidak membuat pasangan lain kehilangan makna. Pasangan TC-721 dan TC-722 memakai draft yang sama karena permintaan yang gagal tidak mengubah draft; hal yang sama berlaku untuk pasangan Positions dan Options.
- Subjudul `###` dan `####` memetakan langkah ke id TC granular. Langkah ulang (langkah 16 sampai 27 mengikuti pola langkah 1 sampai 15) ditulis eksplisit sebagai teks biasa.
- Langkah penghubung (tanpa `Verifikasi`): reset (langkah 1, 28, 57), pembukaan halaman dan Sub-Tab, melepas intercept (S-09), menutup toast error sebelum asersi toast berikutnya (S-09), dan langkah kembali ke Import (langkah 16, 44, 71).
- Asersi absence `Logistik`, `Store Supervisor` didahului Verifikasi jumlah baris tabel (5 baris) sebagai anchor positif pada surface yang sama (butir 2 bagian 8b); Value Setting Shift diasersi sebagai nilai utuh `Pagi, Siang, Malam`.
- Temuan untuk QA:
  - TC-GS-IMPORT-721 sampai 724, 927, 928 menyebut "Setelah langkah 5/6 ... baris tetap `error`" tanpa menyebut baris mana pada draft 4 baris; spec mengasersi bahwa baris tetap `error` tanpa memilih nomor baris tertentu.
  - TC-GS-IMPORT-722 dan 724 menulis toast "Error, failed to create division." dan "Error, failed to create position."; teks mengikuti Expected TC dan tidak diverifikasi ke PRD §7 di spec ini.
  - TC-GS-IMPORT-927 dan 928 memakai berkas D-79 yang menghasilkan 2 baris `error` (`Lembur` dan `lembur `); "Shift: Invalid option" dengan badge "2 rows" bergantung pada normalisasi nilai sesuai PRD, bukan aturan spec.
  - Post Condition TC-GS-IMPORT-721 sampai 724 dan 927, 928 ("draft User Login Client C berisi N baris") tidak punya langkah observasi tersendiri dan tidak diasersi (S-01).
  - Nama endpoint Create Missing untuk intercept tidak didefinisikan di TC; diambil dari kontrak API modul (`import-create-missing`) oleh tim FE.
