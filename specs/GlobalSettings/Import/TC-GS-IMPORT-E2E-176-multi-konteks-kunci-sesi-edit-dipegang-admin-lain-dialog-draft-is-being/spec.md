---
id: TC-GS-IMPORT-E2E-176-multi-konteks-kunci-sesi-edit-dipegang-admin-lain-dialog-draft-is-being
title: "Multi-konteks: kunci sesi edit dipegang admin lain (dialog Draft Is Being Edited, tulis-balik evaluasi ditekan) dan tidak ada push real-time"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-516
  - TC-GS-IMPORT-552
  - TC-GS-IMPORT-574
  - TC-GS-IMPORT-946
coverage:
  web: automated
---

# Multi-konteks: kunci sesi edit dipegang admin lain (dialog Draft Is Being Edited, tulis-balik evaluasi ditekan) dan tidak ada push real-time

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah Custom Field Client A (hapus opsi `Shift` `Siang`, jadikan `Shift Notes` Required) dan Client C yang dibaca lintas spec, serta mengubah jam browser; draft Import dibagikan ke seluruh admin; lihat `suite.md`.
- Konteks browser (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk Sesi A:
  - Sesi A (aktor): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`.
  - Sesi B (administrator lain, sesi UI kedua yang hasilnya diasersi pada TC-574 dan TC-946): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC2_PASSWORD`. Login di hook `before` pada konteks browser terpisah. Pada TC-516 dan TC-552 Admin kedua hanya memicu perubahan state lewat sesi API (P-2).
  - Blok Client C (TC-552): ganti akun eksplisit ke Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`; Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC2_PASSWORD`, memakai sesi API untuk memulai sesi edit dan memegang kunci.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk setiap akun UI spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Dua konteks browser paralel dan sesi API Admin kedua (hapus opsi Custom Field, jadikan Custom Field Required, mulai sesi edit dan memegang kunci, batalkan sesi edit).
  - Skrip fixture inspeksi data: membaca status tersimpan baris draft dan counter Errors tersimpan (TC-574, 946).
  - Jam browser: dimajukan 60 detik pada TC-516 (jeda 60 detik pada TC melebihi batas jeda nyata ±30 detik) dan dipulihkan sesudahnya; jam server tidak diubah.
  - Jendela amat SSE 5 detik (langkah 5) adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya.
  - Skrip fixture pemulihan Custom Field Client A (opsi `Siang` dan flag Required `Shift Notes`) dan draft dasar (D-05 Client A, D-14 Client C, Kontrak Fixture R2).
- Data Dinamis (milik spec ini): D-05 draft User Login 8 baris `pending` Client A dari `user-login-8.csv` (Population; seeding idempotent dan dipulihkan sebelum tiap TC; Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4); D-14 draft User Login 4 baris Client C (`user-login-cm.csv`): Row # 1 Ahmad Fauzi dan Row # 2 Citra Lestari `pending`, Row # 3 Dedi Prakoso Division `Logistik` `error`, Row # 4 Eka Putri Position `Store Supervisor` `error`; `user-login-1.csv` (header First Name; Last Name; Email; Division; Access; 1 baris dengan Email unik, Division `Engineering`, Access `Global Settings`).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): batalkan sesi edit yang masih aktif, pulihkan opsi `Siang` pada Custom Field `Shift` dan flag Required `Shift Notes` ke opsional (Kontrak Fixture R2), pulihkan jam browser, hapus draft Client C, pulihkan draft dasar Client A, tutup konteks Sesi B, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-516: Tidak ada push real-time

1. Pulihkan Custom Field `Shift` (opsi Pagi, Siang, Malam) dan draft dasar Client A D-05 (User Login 8 baris `pending`) lewat skrip fixture
2. [Sesi A] Muat ulang halaman Import > User Login (halaman dibiarkan terbuka tanpa aksi)
3. Hapus opsi `Siang` dari Custom Field `Shift` Client A atas nama Admin kedua Client A lewat sesi API
4. Majukan jam browser Sesi A 60 detik tanpa aksi apa pun pada halaman Import
5. [Sesi A] Tunggu 5 detik tanpa memuat ulang halaman
6. [Sesi A] Verifikasi Staging Metric Cards Ready to Import 8
7. [Sesi A] Verifikasi Staging Metric Cards Errors 0
8. [Sesi A] Verifikasi Row # 1 dan 2 tetap `pending` (tidak ada push)
9. [Sesi A] Klik kartu Ready to Import
10. [Sesi A] Verifikasi Staging Metric Cards Ready to Import 6
11. [Sesi A] Verifikasi Staging Metric Cards Errors 2
12. [Sesi A] Verifikasi tabel menampilkan 6 baris `pending`
13. Pulihkan jam browser Sesi A dan opsi `Siang` pada Custom Field `Shift` Client A

### TC-GS-IMPORT-574: Tulis-balik evaluasi ulang ditekan saat kunci dipegang

14. Pulihkan Custom Field `Shift` dan draft dasar Client A D-05 lewat skrip fixture
15. [Sesi A] Muat ulang halaman Import > User Login
16. [Sesi A] Klik row action `⋯` pada Row # 1 lalu Edit (sesi edit dimulai dan kunci dipegang)
17. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
18. Hapus opsi `Siang` dari Custom Field `Shift` di Custom Field User atas nama Admin kedua Client A lewat sesi API
19. [Sesi B] Buka Global Settings > Import, pilih Sub-Tab User Login
20. [Sesi B] Verifikasi Row # 1 berstatus `error`
21. [Sesi B] Verifikasi Row # 2 berstatus `error`
22. Baca status tersimpan Row # 1 dan 2 lewat skrip fixture inspeksi data
23. Verifikasi status tersimpan Row # 1 dan 2 masih `pending`
24. [Sesi A] Klik `[Cancel]` tanpa mengubah nilai
25. [Sesi A] Muat ulang halaman Import > User Login
26. [Sesi A] Verifikasi kartu Errors menampilkan 2
27. Baca status tersimpan Row # 1 dan 2 serta counter Errors tersimpan lewat skrip fixture inspeksi data
28. Verifikasi status tersimpan Row # 1 dan 2 `error`
29. Verifikasi counter Errors tersimpan 2
30. Pulihkan opsi `Siang` pada Custom Field `Shift` Client A

### TC-GS-IMPORT-946: Tulis-balik evaluasi Required ditekan saat kunci dipegang

31. Pulihkan Custom Field `Shift Notes` (Text Area, opsional) dan draft dasar Client A D-05 lewat skrip fixture
32. [Sesi A] Muat ulang halaman Import > User Login
33. [Sesi A] Klik row action `⋯` pada Row # 1 lalu Edit (sesi edit dimulai dan kunci dipegang)
34. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
35. Jadikan Custom Field `Shift Notes` Required di Custom Field User atas nama Admin kedua Client A lewat sesi API
36. [Sesi B] Muat ulang halaman Import > User Login
37. [Sesi B] Verifikasi seluruh 8 baris berstatus `error`
38. Baca status tersimpan Row # 1 sampai 8 lewat skrip fixture inspeksi data
39. Verifikasi status tersimpan seluruh baris masih `pending`
40. [Sesi A] Klik `[Cancel]` tanpa mengubah nilai
41. [Sesi A] Muat ulang halaman Import > User Login
42. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
43. Baca status tersimpan Row # 1 sampai 8 serta counter Errors tersimpan lewat skrip fixture inspeksi data
44. Verifikasi status tersimpan seluruh baris `error`
45. Verifikasi counter Errors tersimpan 8
46. Pulihkan Custom Field `Shift Notes` ke opsional

### TC-GS-IMPORT-552: Mutasi draft saat kunci dipegang admin lain tidak diproses

47. [Sesi A] Ganti akun: logout, lalu login sebagai Total Control Client C (Rudi Hartanto)
48. Seed draft User Login D-14 (4 baris) Client C lewat skrip fixture
49. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab User Login
50. [Sesi A] Klik `[Upload File]`
51. [Sesi A] Pilih berkas `user-login-1.csv`
52. [Sesi A] Klik `[Append Records]` pada Dialog Append to Draft
53. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
54. Mulai sesi edit pada Row # 1 atas nama Admin kedua Client C lewat sesi API (sesi edit dimulai dan kunci dipegang)
55. Tunggu aksi selesai (permintaan mendapat respons)
56. [Sesi A] Klik `[Confirm Mapping]`
57. [Sesi A] Verifikasi dialog Draft Is Being Edited dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
58. [Sesi A] Klik `[Cancel]` pada dialog
59. [Sesi A] Klik `[Cancel]` pada Modal Column Mapping
60. [Sesi A] Klik `[Import (2)]`
61. [Sesi A] Verifikasi dialog Draft Is Being Edited dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
62. [Sesi A] Klik `[Cancel]` pada dialog
63. [Sesi A] Klik row action `⋯` pada Row # 3 lalu Create Missing Divisions
64. [Sesi A] Verifikasi dialog Draft Is Being Edited dengan Title "Draft Is Being Edited", Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved.", dan tombol `[Cancel]` dan `[Take Over Session]`
65. [Sesi A] Klik `[Cancel]` pada dialog
66. [Sesi A] Muat ulang halaman Import > User Login
67. [Sesi A] Verifikasi Staging Metric Cards Total Rows 4
68. [Sesi A] Verifikasi Staging Metric Cards Ready to Import 2
69. [Sesi A] Verifikasi Staging Metric Cards Errors 2
70. [Sesi A] Verifikasi Row # 3 masih berstatus `error` dengan `Division not found`
71. Batalkan sesi edit Admin kedua Client C lewat sesi API (pemulihan)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (c); objek uji adalah tidak adanya push real-time (TC-516), tulis-balik evaluasi yang ditekan saat kunci dipegang administrator lain (TC-574, 946), dan penolakan mutasi saat kunci dipegang (TC-552). Admin kedua hanya memicu state lewat sesi API pada TC-516 dan TC-552 (P-2); Sesi B adalah sesi UI kedua yang diasersi pada TC-574 dan TC-946.
- Alasan melewati sekitar 35 langkah (71 langkah nominal): empat blok satu kelas multi-konteks yang berdiri sendiri dengan pemulihan Custom Field dan draft di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok Client C (TC-552) memakai ganti akun eksplisit (langkah 47), sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok: TC-516, TC-574, TC-946 (Client A, mengubah Custom Field lalu memulihkannya), lalu TC-552 (Client C).
- Langkah penghubung (tanpa `Verifikasi`): pemulihan dan seeding (langkah 1, 14, 31, 48), muat ulang halaman Import > User Login (langkah 2, 36), pembukaan halaman dan Sub-Tab, memajukan dan memulihkan jam browser (langkah 4 dan 13), perubahan Custom Field oleh Admin kedua (langkah 3, 18, 35), pembacaan status tersimpan (langkah 22, 27, 38, 43), sesi edit Admin kedua Client C (langkah 54), menutup dialog (langkah 58, 62, 65), menunggu 5 detik tanpa memuat ulang halaman (langkah 5; jendela amat SSE, pilihan spec), dan Tunggu aksi selesai (langkah 17, 34, 42, 53, 55). Langkah 17 dan 34 mengikuti Edit Sesi A lalu pemicu sesi API; langkah 42 mengikuti muat ulang Sesi A sebelum pembacaan fixture; langkah 55 mengikuti pemicu sesi edit sesi API sebelum `[Confirm Mapping]` (bagian 8b butir 8). Langkah 6 sampai 8 adalah asersi tidak berubah yang diasersi sebelum klik kartu Ready to Import (langkah 9) yang mengubah state (butir 5 bagian 8b).
- Langkah 8 (Row # 1 dan 2 tetap `pending`, tidak ada push) adalah asersi absence atas propagasi SSE; didahului langkah 5 (tunggu 5 detik tanpa memuat ulang halaman) supaya absence bukan karena push belum tiba.
- Pembagian TC lintas spec: kunci sesi edit dengan dialog Take Over Session ada di spec 068 sampai 073; spec ini memuat kasus tulis-balik evaluasi yang ditekan dan tidak ada push.
- Temuan untuk QA:
  - TC-GS-IMPORT-552 Expected a, b, c menyebut dialog Draft Is Being Edited dengan tombol `[OK]`, sedangkan PRD §4.1 Dialog Konflik Kunci Sesi menetapkan tombol `[Cancel]` dan `[Take Over Session]`; Langkah TC menutup dialog dengan `[Cancel]`. Spec mengasersi tombol sesuai PRD.
  - TC-GS-IMPORT-516 menunggu 60 detik tanpa aksi; jeda nyata di atas ±30 detik tidak diizinkan konvensi (bagian 6), sehingga spec memajukan jam browser 60 detik (langkah 4). Bila push real-time dipicu timer polling server, memajukan jam browser tidak menggantikan menunggu 60 detik nyata; kebutuhan jam yang dipakai harus dikonfirmasi tim FE.
  - TC-GS-IMPORT-516 dan 574 menghapus opsi `Siang` dari Custom Field `Shift` tanpa menyebut urutan opsi saat dipulihkan; Post Condition menyebut pemulihan ke kondisi Pre-setup (Pagi, Siang, Malam).
  - Status `error` yang dilihat Sesi B pada TC-GS-IMPORT-574 dan 946 (langkah 20, 21, 37) adalah hasil hitung read-only untuk tampilan, bukan nilai tersimpan; nilai tersimpan tetap `pending` sampai tulis-balik (langkah 23 dan 39) dan hanya diasersi lewat skrip fixture inspeksi data.
  - TC-GS-IMPORT-574 dan 946 memakai skrip fixture inspeksi data untuk status tersimpan dan counter Errors tersimpan yang tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-GS-IMPORT-552 mengunggah `user-login-1.csv` pada draft yang kuncinya dipegang; Langkah TC 6 dan 7 menutup dialog dan Modal Column Mapping tanpa mengubah dropdown (modal langsung tertutup, PRD §4.1).
  - Post Condition TC-GS-IMPORT-516, 574, 946 (pemulihan Custom Field) dikerjakan langkah 13, 30, 46 dan hook `after`; Post Condition TC-GS-IMPORT-552 (sesi edit dibatalkan) dikerjakan langkah 71.
  - Penanda selesai untuk langkah 52 (`[Append Records]` Sesi A sebelum Admin kedua Client C memulai sesi edit) tidak disebut di TC, PRD, atau spec ini; langkah "Tunggu aksi selesai" (langkah 53) memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface Sesi A.
  - Penanda selesai untuk pemicu sesi API atau fixture tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface aktor UI.
