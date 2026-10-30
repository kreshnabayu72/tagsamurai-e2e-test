---
id: TC-GS-ACTLOG-E2E-001-screening-layout-tab-default-breadcrumb-dan-tanpa-kontrol-tulis
title: "Screening Layout, Tab Default, Breadcrumb, dan Tanpa Kontrol Tulis"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-01
  - TC-GS-ACTLOG-02
  - TC-GS-ACTLOG-03
  - TC-GS-ACTLOG-221
  - TC-GS-ACTLOG-227
coverage:
  web: automated
---

# Screening Layout, Tab Default, Breadcrumb, dan Tanpa Kontrol Tulis

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup: tidak ada data Pre-setup yang dibaca selain akun aktor.
- Data Dinamis (suffix `{runId}-001`):
  - Baris Session milik akun aktor harus tersedia di tab Session. Bila login akun aktor di hook `before` tidak menghasilkan baris Session, seed baris Session disediakan tim FE/BE.
  - Brand `Brand ActLog {runId}-001`, dibuat lewat API oleh akun aktor di hook `before` supaya tab User Action memiliki baris log (aksi `Create` Object `Brand`). Dihapus lewat API di hook `after` (tidak berasumsi seeding berhasil penuh).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Kemampuan teknis: membaca URL (route) halaman aktif; refresh halaman (F5).
- Suite serial: `parallel: false` (lihat `suite.md`). Spec tidak mengubah format tanggal, zona waktu, atau jam.

## Test Steps

### TC-GS-ACTLOG-227: Tab Session aktif saat pertama masuk halaman Activity Log

1. Buka Global Settings
2. Klik menu Activity Log tanpa mengklik tab apa pun
3. Verifikasi tab `Session` aktif
4. Verifikasi tab `User Action` tidak aktif
5. Verifikasi Breadcrumb `Activity Log > Session`
6. Verifikasi tabel log Session tampil

### TC-GS-ACTLOG-01: Screening 3 zona Tab Session

7. Klik tab "Session"
8. Verifikasi Header: Breadcrumb `Activity Log > Session`
9. Verifikasi Header: segmen terakhir Breadcrumb bukan link
10. Verifikasi Header: Tab `Session (aktif) | User Action`
11. Verifikasi Header: Table Tools memuat `Search | Filter | Download`
12. Verifikasi Header: Table Tools rata kanan
13. Verifikasi Header: tidak ada tombol create
14. Verifikasi Body: kolom `Date (sortable) | User (sortable) | Employee ID (sortable) | Position (sortable) | Division (sortable) | Activity (sortable) | Status (sortable) | Note (sortable) | IP Address (sortable) | Device / Browser (sortable) | Column Visibility (⋯) (unsortable)`
15. Klik header kolom Column Visibility (⋯)
16. Verifikasi Overlay Column Visibility terbuka
17. Verifikasi Overlay Column Visibility memuat item `Setup Column...`
18. Klik item `Setup Column...`
19. Verifikasi Popup Setup Column terbuka
20. Tutup Popup Setup Column dengan `✕`
21. Verifikasi Body: baris data log Session tampil
22. Verifikasi Body: sel kolom Column Visibility (⋯) pada tiap baris kosong karena tabel read-only tanpa row action
23. Verifikasi Footer: pagination default 10 baris per halaman
24. Buka pilihan jumlah baris per halaman pada Footer
25. Verifikasi Footer: pilihan 10, 25, 50, 100
26. Tutup pilihan jumlah baris per halaman dengan `Esc`

### TC-GS-ACTLOG-02: Screening 3 zona Tab User Action

27. Klik tab "User Action"
28. Verifikasi Header: Breadcrumb `Activity Log > User Action`
29. Verifikasi Header: segmen terakhir Breadcrumb bukan link
30. Verifikasi Header: Tab `Session | User Action (aktif)`
31. Verifikasi Header: Table Tools memuat `Search | Filter | Download`
32. Verifikasi Header: Table Tools rata kanan
33. Verifikasi Header: tidak ada tombol create
34. Verifikasi Body: kolom `Date (sortable) | Action (sortable) | Object (sortable) | Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
35. Klik header kolom Column Visibility (⋯)
36. Verifikasi Overlay Column Visibility terbuka
37. Verifikasi Overlay Column Visibility memuat item `Setup Column...`
38. Klik item `Setup Column...`
39. Verifikasi Popup Setup Column terbuka
40. Tutup Popup Setup Column dengan `✕`
41. Verifikasi Body: baris data log User Action tampil
42. Verifikasi Body: sel kolom Column Visibility (⋯) pada tiap baris kosong karena tabel read-only tanpa row action
43. Verifikasi Footer: pagination default 10 baris per halaman
44. Buka pilihan jumlah baris per halaman pada Footer
45. Verifikasi Footer: pilihan 10, 25, 50, 100
46. Tutup pilihan jumlah baris per halaman dengan `Esc`

### TC-GS-ACTLOG-03: Breadcrumb per tab, route sendiri, dan refresh tetap di tab aktif

47. Klik menu Activity Log di sidebar
48. Klik tab "Session"
49. Verifikasi Breadcrumb `Activity Log > Session`
50. Catat URL (route) tab Session sebagai pembanding
51. Klik segmen terakhir Breadcrumb
52. Verifikasi klik segmen terakhir Breadcrumb tidak memindahkan halaman
53. Klik tab "User Action"
54. Verifikasi Breadcrumb `Activity Log > User Action`
55. Verifikasi URL (route) tab User Action berbeda dari URL tab Session
56. Refresh halaman (F5) di tab "User Action"
57. Verifikasi halaman tetap tab User Action setelah refresh
58. Klik tab "Session"
59. Refresh halaman (F5) di tab "Session"
60. Verifikasi halaman tetap tab Session setelah refresh

### TC-GS-ACTLOG-221: Tidak ada kontrol tulis pada log, kedua tab

61. Amati toolbar, header, dan baris tabel pada tab "Session"
62. Verifikasi Tab Session: baris data log tampil
63. Verifikasi Tab Session: tidak ada tombol Create, Edit, Delete, kolom checkbox, atau row action pada toolbar maupun baris
64. Klik tab "User Action"
65. Amati toolbar, header, dan baris tabel pada tab "User Action"
66. Verifikasi Tab User Action: baris data log tampil
67. Verifikasi Tab User Action: tidak ada tombol Create, Edit, Delete, kolom checkbox, atau row action pada toolbar maupun baris

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-01, 2, 3, 221, 227). Tidak ada TC hanya-BE di spec ini.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah; urutan TC: TC-227 (halaman pertama dibuka), TC-1, TC-2, TC-3, lalu TC-221 (screening tanpa aksi, tanpa data yang diubah).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (buka Global Settings sebagai precondition TC-227), 20 dan 40 (tutup Popup Setup Column dengan `✕`; Setup Column punya footer `[Reset to Default]` dan `[Save]` tanpa `[Cancel]`), 26 dan 46 (tutup pilihan jumlah baris dengan `Esc`), 50 (mencatat URL sebagai pembanding, kriterianya ada di langkah 55), 61 dan 65 (amati). Langkah 15 sampai 20, 35 sampai 40, 24 sampai 26, dan 44 sampai 46 membuka Overlay Column Visibility, Popup Setup Column, dan pilihan jumlah baris hanya untuk membuktikan butir Expected TC-1 dan TC-2 (isi Overlay, `Setup Column...` membuka Popup, pilihan 10/25/50/100).
- Langkah 62 dan 66 adalah `Verifikasi` data pembanding (baris data log tampil) yang mendahului asersi "tidak ada kontrol tulis" pada surface yang sama (aturan anchor absence); Expected TC-221 tidak memuatnya.
- Pembagian TC lintas spec: Setup Column (fungsional), Search, Filter, Sort, dan Pagination diuji di spec lain; spec ini hanya membuktikan keberadaan dan titik masuknya.
- Spec di atas smell 35 langkah (67 langkah). Alasan: seluruh blok satu kelas (screening read-only tanpa mutasi data), lima TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected TC-1 dan TC-2 bermajemuk dan dipecah per klausa (S-01).
- Temuan untuk QA:
  - TC-1 dan TC-2 menyebut item `Setup Column...` di dalam Overlay Column Visibility, sedangkan modul Division di repo ini memakai CTA `[Setup Column]` pada Overlay yang sama. Spec mengikuti TC (`Setup Column...`); QA perlu memastikan penulisan label yang benar.
  - TC-1 dan TC-2 Expected b.ii hanya menyebut "baris data log tampil" tanpa jumlah; spec memastikan ada data lewat aksi login aktor (Session) dan pembuatan Brand `Brand ActLog {runId}-001` (User Action).
  - TC-3 Expected c hanya menyatakan URL kedua tab berbeda tanpa menyebut path; spec mengasersi perbedaan relatif, bukan nilai path.
  - Login akun aktor di hook `before` belum tentu menghasilkan baris Session (tergantung cara login hook); kebutuhan seed baris Session disediakan tim FE/BE.
