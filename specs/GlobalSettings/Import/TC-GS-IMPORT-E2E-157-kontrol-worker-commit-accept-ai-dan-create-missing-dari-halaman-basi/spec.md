---
id: TC-GS-IMPORT-E2E-157-kontrol-worker-commit-accept-ai-dan-create-missing-dari-halaman-basi
title: "Kontrol worker commit: Accept AI dan Create Missing dari halaman basi saat committing memunculkan dialog Import In Progress"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-705
  - TC-GS-IMPORT-731
  - TC-GS-IMPORT-732
  - TC-GS-IMPORT-747
  - TC-GS-IMPORT-860
coverage:
  web: automated
---

# Kontrol worker commit: Accept AI dan Create Missing dari halaman basi saat committing memunculkan dialog Import In Progress

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit, mode mock AI) dan memakai Client E yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Pelaku kedua (pemicu): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, memakai sesi API untuk permintaan Import fixture (memulai commit) dan hapus baris Staging pada TC-860; tidak ada sesi UI kedua karena hasil di sesi itu tidak diasersi (P-2).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-705, 731, 732, 747, 860 tidak merujuk D-47 pada kolom D-ref pada sebagian baris tetapi membutuhkannya):
  - Kontrol worker commit D-47 mode 1 (dijeda sebelum job mulai, job yang dimulai tetap `committing`) untuk TC-705, 731, 732, 860; mode 2 (dijeda di dalam batch pertama) untuk TC-747.
  - Mock layanan AI deterministik mode normal D-40 (tabel D-41 dan D-42).
  - Sesi API Admin kedua Client E: permintaan Import fixture dan hapus baris Staging (TC-860).
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus hasil commit) dan seeding draft.
- Data Pre-setup Client E (hanya dibaca, tidak diubah spec ini): Division 5 item (`Logistik` belum ada), Position 5 item (`Store Supervisor` belum ada).
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal; tidak ada record master data tercipta karena worker dijeda):
  - D-44 `brand-ai-commit.csv`: kolom `Brand Name`; `Lenovo`, `Dell`, nilai sumber Brand D-41 (121 karakter, badge saran `Samsung Electronics Indonesia`) (TC-705).
  - D-45 `user-login-commit-logistik.csv` (baris #1 Bambang Hartono Division `Engineering`; #2 Citra Wulandari dan #3 Doni Kurniawan Division `Logistik`) dan `user-login-commit-store-supervisor.csv` (baris #1 Division `Engineering` Position kosong; #2 dan #3 Division `Engineering` Position `Store Supervisor`).
  - D-57 `brand-250-mixed.csv`: 248 `pending` (`Brand Impor nnn`), baris #5 `error` (Brand Name 121 karakter, badge saran AI `Samsung Electronics Indonesia`), baris #20 `duplicate` (`Samsung`); batch pertama = baris #1-#4, #6-#19, #21-#102 (TC-747, 860).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, kembalikan mock AI ke normal, hapus draft Client E, hapus hasil commit bila ada, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-705: Accept dari halaman basi saat committing

1. Reset Client E (D-47) ke tanpa draft; pastikan mock AI mode normal
2. Muat ulang halaman Import > Brand
3. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
4. Klik `[Upload File]` di toolbar dan pilih berkas `brand-ai-commit.csv`
5. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
6. Tunggu aksi selesai (modal tertutup)
7. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API; setara klik `[Import (2)]`)
8. Tunggu aksi selesai (permintaan mendapat respons)
9. Pada halaman langkah 5 (tanpa muat ulang) klik `[Accept]` pada badge saran sel Brand Name baris #3
10. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan satu tombol `[OK]`
11. Klik `[OK]` pada dialog
12. Verifikasi dialog tertutup
13. Verifikasi sel Brand Name baris #3 tetap bernilai 121 karakter semula
14. Verifikasi baris #3 tetap `error`

### TC-GS-IMPORT-747: AI Accept dari halaman basi saat committing

15. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) lewat skrip fixture
16. Muat ulang halaman Import > Brand
17. Verifikasi footer `[Import (248)]` Enabled
18. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
19. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
20. Tunggu aksi selesai (permintaan mendapat respons)
21. Pada halaman langkah 16 (tanpa muat ulang) klik `[Accept]` pada badge saran sel Brand Name baris #5
22. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
23. Klik `[OK]`
24. Muat ulang halaman Import > Brand
25. Verifikasi Brand Name baris #5 tetap bernilai `PT Samsung Electronics Indonesia Manufacturing and Distribution Company for Consumer Electronics and Home Appliances Prod` (121 karakter)
26. Verifikasi baris #5 tetap berstatus `error`

### TC-GS-IMPORT-860: Accept saran AI basi saat committing ditolak, bukan no-op diam

27. Reset Client E (D-47) dan seed draft Brand D-57 lewat skrip fixture; pastikan mock AI mode normal
28. Muat ulang halaman Import > Brand
29. Verifikasi badge saran tampil pada baris #5
30. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
31. Hapus baris #5 atas nama Admin kedua Client E lewat fixture permintaan (sesi API)
32. Mulai Import atas nama Admin kedua Client E lewat fixture permintaan (sesi API) sehingga job berstatus `committing`
33. Tunggu aksi selesai (permintaan mendapat respons)
34. Klik `[Accept]` pada badge saran baris #5 yang masih tampil
35. Verifikasi dialog blok Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol `[OK]` saja
36. Klik `[OK]`
37. Verifikasi dialog tertutup
38. Verifikasi Staging Table menampilkan baris lain selain baris #5
39. Verifikasi baris #5 tidak lagi tampil pada Staging Table
40. Verifikasi kartu Total Rows tetap 249

### TC-GS-IMPORT-731: Create Missing Divisions bulk dari halaman basi saat committing

41. Reset Client E (D-47) ke tanpa draft dan pulihkan worker commit
42. Pilih Sub-Tab User Login
43. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
44. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-commit-logistik.csv`
45. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
46. Tunggu aksi selesai (modal tertutup)
47. Mulai commit draft User Login Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API; setara klik `[Import (1)]`)
48. Tunggu aksi selesai (permintaan mendapat respons)
49. Pada halaman langkah 45 (tanpa muat ulang) klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
50. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan satu tombol `[OK]`
51. Klik `[OK]` pada dialog
52. Verifikasi dialog tertutup
53. Verifikasi baris #2 berstatus `error` dengan Division `Logistik` pada Staging Table
54. Verifikasi baris #3 berstatus `error` dengan Division `Logistik` pada Staging Table
55. Buka Global Settings > User > Division
56. Verifikasi tabel Division menampilkan 5 baris
57. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-732: Create Missing Positions per-baris dari halaman basi saat committing

58. Reset Client E (D-47) ke tanpa draft dan pulihkan worker commit
59. Buka Global Settings > Import, pilih Sub-Tab User Login
60. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
61. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-commit-store-supervisor.csv`
62. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
63. Tunggu aksi selesai (modal tertutup)
64. Mulai commit draft User Login Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API; setara klik `[Import (1)]`)
65. Tunggu aksi selesai (permintaan mendapat respons)
66. Pada halaman langkah 62 (tanpa muat ulang) klik `⋯` pada baris #2
67. Pilih `[Create Missing Positions]`
68. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan satu tombol `[OK]`
69. Klik `[OK]` pada dialog
70. Verifikasi dialog tertutup
71. Verifikasi baris #2 berstatus `error` dengan Position `Store Supervisor` pada Staging Table
72. Verifikasi baris #3 berstatus `error` dengan Position `Store Supervisor` pada Staging Table
73. Buka Global Settings > User > Position
74. Verifikasi tabel Position menampilkan 5 baris
75. Verifikasi daftar Position tidak memuat `Store Supervisor`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah penolakan aksi dari halaman basi saat job `committing` yang dibentuk kontrol worker D-47. Pelaku kedua hanya memicu perubahan state lewat sesi API (P-2); langkah TC "Admin kedua Client E: buka Import > Brand" dan "klik `[Import (N)]`" digantikan pemicu sesi API tanpa pembukaan halaman karena hasil di sesi itu tidak diasersi.
- Alasan melewati sekitar 35 langkah (75 langkah nominal): lima blok homogen (aksi dari halaman basi saat `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok Brand (TC-705, 747, 860) mendahului blok User Login; TC-860 menghapus baris dan diletakkan terakhir di antara blok Brand.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 15, 27, 41, 58), aktivasi kontrol worker, muat ulang halaman Import > Brand sesudah reset (langkah 2, 16, dan 28), pembukaan halaman dan Sub-Tab lain, dan pemicu sesi API (langkah 7, 19, 31, 32, 47, 64). Langkah 6, 46, dan 63 menunggu modal Column Mapping tertutup sesudah `[Confirm Mapping]` dan sebelum permintaan Import sesi API (bagian 8b butir 8), tanpa `Verifikasi`. Langkah 38 adalah `Verifikasi` anchor (Staging Table masih menampilkan baris lain) bagi langkah 39. Langkah 17 dan 29 adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan prasyarat halaman basi (footer `[Import (248)]` Enabled; badge saran tampil sebelum pemicu). Langkah 8, 20, 33, 48, dan 65 (Tunggu aksi selesai: permintaan mendapat respons) mengikuti pemicu sesi API dan mendahului aksi UI pada halaman basi (bagian 8b butir 8).
- Asersi `Logistik` dan `Store Supervisor` tidak ada di daftar didahului Verifikasi jumlah baris tabel (5 baris) sebagai anchor positif (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-705, 747, dan 860 hampir duplikat (Accept AI dari halaman basi saat `committing` ditolak dengan dialog Import In Progress); perbedaan hanya sumber data (brand-ai-commit.csv vs D-57) dan, pada TC-860, penegasan "bukan no-op diam" serta baris #5 yang dihapus pemicu.
  - TC-GS-IMPORT-860 menghapus baris #5 oleh Admin kedua sebelum Import sehingga Accept menargetkan baris yang sudah terhapus; TC menyatakan hasilnya 409 dengan dialog Import In Progress (gerbang `committing` mendahului pemeriksaan keberadaan baris).
  - TC-GS-IMPORT-705, 731, 732 tidak menyebut apakah draft Brand/User Login dengan 2 atau 3 baris `pending` cukup agar `[Import (N)]` tampil Enabled sebelum job dimulai; angka `[Import (2)]` dan `[Import (1)]` mengikuti Langkah TC.
  - Post Condition TC-GS-IMPORT-705, 731, 732 ("worker dilanjutkan dan Client E dipulihkan") tidak punya langkah observasi dan tidak diasersi (S-01); Post Condition TC-GS-IMPORT-747 ("job committing; draft tetap 250 baris") dan TC-GS-IMPORT-860 ("job `committing`; kontrol worker dan hasil commit direset") juga tidak diasersi.
  - Penanda selesai untuk pemicu sesi API atau fixture tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface aktor UI.
