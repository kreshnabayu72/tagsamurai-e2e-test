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
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
4. Klik `[Upload File]` di toolbar dan pilih berkas `brand-ai-commit.csv`
5. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
6. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API; setara klik `[Import (2)]`)
7. Pada halaman langkah 5 (tanpa muat ulang) klik `[Accept]` pada badge saran sel Brand Name baris #3
8. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan satu tombol `[OK]`
9. Klik `[OK]` pada dialog
10. Verifikasi dialog tertutup
11. Verifikasi sel Brand Name baris #3 tetap bernilai 121 karakter semula
12. Verifikasi baris #3 tetap `error`

### TC-GS-IMPORT-747: AI Accept dari halaman basi saat committing

13. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) lewat skrip fixture
14. Buka Global Settings > Import, pilih Sub-Tab Brand
15. Verifikasi footer `[Import (248)]` Enabled
16. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
17. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
18. Pada halaman langkah 14 (tanpa muat ulang) klik `[Accept]` pada badge saran sel Brand Name baris #5
19. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
20. Klik `[OK]`
21. Muat ulang halaman Import > Brand
22. Verifikasi Brand Name baris #5 tetap bernilai `PT Samsung Electronics Indonesia Manufacturing and Distribution Company for Consumer Electronics and Home Appliances Prod` (121 karakter)
23. Verifikasi baris #5 tetap berstatus `error`

### TC-GS-IMPORT-860: Accept saran AI basi saat committing ditolak, bukan no-op diam

24. Reset Client E (D-47) dan seed draft Brand D-57 lewat skrip fixture; pastikan mock AI mode normal
25. Buka Global Settings > Import, pilih Sub-Tab Brand
26. Verifikasi badge saran tampil pada baris #5 (halaman tidak dimuat ulang setelahnya)
27. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
28. Hapus baris #5 atas nama Admin kedua Client E lewat fixture permintaan (sesi API)
29. Mulai Import atas nama Admin kedua Client E lewat fixture permintaan (sesi API) sehingga job berstatus `committing`
30. Klik `[Accept]` pada badge saran baris #5 yang masih tampil
31. Verifikasi dialog blok Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol `[OK]` saja
32. Klik `[OK]`
33. Verifikasi dialog tertutup
34. Verifikasi Staging Table menampilkan baris lain selain baris #5
35. Verifikasi baris #5 tidak lagi tampil pada Staging Table
36. Verifikasi kartu Total Rows tetap 249

### TC-GS-IMPORT-731: Create Missing Divisions bulk dari halaman basi saat committing

37. Reset Client E (D-47) ke tanpa draft dan pulihkan worker commit
38. Pilih Sub-Tab User Login
39. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
40. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-commit-logistik.csv`
41. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
42. Mulai commit draft User Login Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API; setara klik `[Import (1)]`)
43. Pada halaman langkah 41 (tanpa muat ulang) klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
44. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan satu tombol `[OK]`
45. Klik `[OK]` pada dialog
46. Verifikasi dialog tertutup
47. Verifikasi baris #2 berstatus `error` dengan Division `Logistik` pada Staging Table
48. Verifikasi baris #3 berstatus `error` dengan Division `Logistik` pada Staging Table
49. Buka Global Settings > User > Division
50. Verifikasi tabel Division menampilkan 5 baris
51. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-732: Create Missing Positions per-baris dari halaman basi saat committing

52. Reset Client E (D-47) ke tanpa draft dan pulihkan worker commit
53. Buka Global Settings > Import, pilih Sub-Tab User Login
54. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
55. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-commit-store-supervisor.csv`
56. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
57. Mulai commit draft User Login Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API; setara klik `[Import (1)]`)
58. Pada halaman langkah 56 (tanpa muat ulang) klik `⋯` pada baris #2
59. Pilih `[Create Missing Positions]`
60. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan satu tombol `[OK]`
61. Klik `[OK]` pada dialog
62. Verifikasi dialog tertutup
63. Verifikasi baris #2 berstatus `error` dengan Position `Store Supervisor` pada Staging Table
64. Verifikasi baris #3 berstatus `error` dengan Position `Store Supervisor` pada Staging Table
65. Buka Global Settings > User > Position
66. Verifikasi tabel Position menampilkan 5 baris
67. Verifikasi daftar Position tidak memuat `Store Supervisor`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah penolakan aksi dari halaman basi saat job `committing` yang dibentuk kontrol worker D-47. Pelaku kedua hanya memicu perubahan state lewat sesi API (P-2); langkah TC "Admin kedua Client E: buka Import > Brand" dan "klik `[Import (N)]`" digantikan pemicu sesi API tanpa pembukaan halaman karena hasil di sesi itu tidak diasersi.
- Alasan melewati sekitar 35 langkah (67 langkah nominal): lima blok homogen (aksi dari halaman basi saat `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok Brand (TC-705, 747, 860) mendahului blok User Login; TC-860 menghapus baris dan diletakkan terakhir di antara blok Brand.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 13, 24, 37, 52), aktivasi kontrol worker, pembukaan halaman dan Sub-Tab, dan pemicu sesi API (langkah 6, 17, 28, 29, 42, 57). Langkah 34 adalah `Verifikasi` anchor (Staging Table masih menampilkan baris lain) bagi langkah 35. Langkah 15 dan 26 adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan prasyarat halaman basi (footer `[Import (248)]` Enabled; badge saran tampil sebelum pemicu).
- Asersi `Logistik` dan `Store Supervisor` tidak ada di daftar didahului Verifikasi jumlah baris tabel (5 baris) sebagai anchor positif (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-705, 747, dan 860 hampir duplikat (Accept AI dari halaman basi saat `committing` ditolak dengan dialog Import In Progress); perbedaan hanya sumber data (brand-ai-commit.csv vs D-57) dan, pada TC-860, penegasan "bukan no-op diam" serta baris #5 yang dihapus pemicu.
  - TC-GS-IMPORT-860 menghapus baris #5 oleh Admin kedua sebelum Import sehingga Accept menargetkan baris yang sudah terhapus; TC menyatakan hasilnya 409 dengan dialog Import In Progress (gerbang `committing` mendahului pemeriksaan keberadaan baris).
  - TC-GS-IMPORT-705, 731, 732 tidak menyebut apakah draft Brand/User Login dengan 2 atau 3 baris `pending` cukup agar `[Import (N)]` tampil Enabled sebelum job dimulai; angka `[Import (2)]` dan `[Import (1)]` mengikuti Langkah TC.
  - Post Condition TC-GS-IMPORT-705, 731, 732 ("worker dilanjutkan dan Client E dipulihkan") tidak punya langkah observasi dan tidak diasersi (S-01); Post Condition TC-GS-IMPORT-747 ("job committing; draft tetap 250 baris") dan TC-GS-IMPORT-860 ("job `committing`; kontrol worker dan hasil commit direset") juga tidak diasersi.
