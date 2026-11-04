---
id: TC-FA-TDC-E2E-091-seed-gagal-dan-job-j-01-harian-time-zone-entitas
title: "Job J-01 Harian: Seed Tidak Dibuat Ulang Setelah Dihapus, Dicoba Ulang Setelah Gagal, pada 00:00 Menurut Time Zone Entitas"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-340
  - TC-FA-TDC-341
  - TC-FA-TDC-342
coverage:
  web: automated
---

# Job J-01 Harian: Seed Tidak Dibuat Ulang Setelah Dihapus, Dicoba Ulang Setelah Gagal, pada 00:00 Menurut Time Zone Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada company uji khusus automation yang dapat dikembalikan ke keadaan belum aktivasi modul akuntansi (plan Growth atau lebih tinggi). Akun, email, dan company disediakan tim FE (tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TCNEWACC_PASSWORD` (nama env belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu arti dengan spec 089). Login di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Time Zone entitas Asia/Jakarta (UTC+07:00); Fiscal Year Start Januari.
- Kendali jam sistem dan penahanan/penjalanan job (`suite.md`): jam server dan jam browser diatur bersama pada waktu absolut yang tertulis di langkah; tick scheduler J-01 dijalankan eksplisit di langkah; jam dipulihkan di hook `after`. Batas 00:00 WIB adalah 17:00 UTC hari sebelumnya: langkah 8 dan 17 memakai 17:05 UTC (margin 5 menit setelah batas, dihitung dari batas itu); langkah 21 dan 24 memakai 16:59 UTC dan 17:00 UTC (batas eksak).
- Kemampuan teknis: fault injection sisi server pada pembuatan seed class ketiga (disediakan tim FE/BE; TC menyebutnya tanpa mekanisme, S-13); membuat/mengembalikan company ke keadaan belum aktivasi modul akuntansi dan mengaktifkan modul akuntansi pertama kali; mengembalikan keadaan "seed gagal sebelumnya" (tabel kosong, seed belum ada); menghapus seluruh class lewat UI (langkah 1 sampai 3).
- Data: pada awal spec company memiliki tujuh class seed bawaan tanpa Used By dan tanpa Last Posted Tax Year (precondition TC-340). Hook `after` memulihkan tujuh class seed bawaan dan menghapus fault injection lewat seeding API (`suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-340: Seed tidak dibuat ulang otomatis setelah seluruh class dihapus

1. Atur jam server dan jam browser ke 15 Okt 2026 03:00 UTC (15 Okt 2026 10:00 WIB)
2. Centang checkbox header sehingga ketujuh baris terpilih
3. Klik `Delete` pada Bulk Action Bar
4. Klik `[Delete]` pada dialog
5. Verifikasi tabel kosong dengan Empty State "No tax depreciation class"
6. Muat ulang halaman
7. Verifikasi Empty State tetap tampil
8. Atur jam server ke 15 Okt 2026 17:05 UTC (16 Okt 2026 00:05 WIB) dan jalankan tick scheduler harian J-01
9. Muat ulang halaman
10. Verifikasi Empty State tetap tampil
11. Verifikasi tidak ada seed baru: tabel tanpa baris class

### TC-FA-TDC-341: Pembuatan seed gagal di tengah jalan, dicoba ulang oleh J-01

12. Kembalikan company ke keadaan belum pernah mengaktifkan modul akuntansi, atur jam server dan jam browser ke 15 Okt 2026 03:00 UTC, dan aktifkan fault injection pembuatan seed pada class ketiga (pembentuk precondition, tidak diasersi)
13. Aktifkan modul akuntansi untuk pertama kali
14. Buka Settings > Accounting > Tax Depreciation Class
15. Verifikasi tabel kosong dengan Empty State "No tax depreciation class" (tidak ada seed sebagian)
16. Hapus fault injection
17. Atur jam server ke 15 Okt 2026 17:05 UTC (16 Okt 2026 00:05 WIB) dan jalankan tick scheduler J-01
18. Muat ulang halaman
19. Verifikasi tabel memuat tujuh class seed, semuanya Active

### TC-FA-TDC-342: J-01 mencoba ulang seed pada 00:00 menurut Time Zone entitas, bukan UTC

20. Kembalikan company ke keadaan pembuatan seed sebelumnya gagal (tabel kosong, seed belum ada; pembentuk precondition, tidak diasersi)
21. Atur jam server ke 14 Okt 2026 16:59 UTC (14 Okt 2026 23:59 WIB) dan jalankan tick scheduler J-01
22. Muat ulang halaman
23. Verifikasi tabel masih kosong (Empty State)
24. Atur jam server ke 14 Okt 2026 17:00 UTC (15 Okt 2026 00:00 WIB) dan jalankan tick scheduler J-01
25. Muat ulang halaman
26. Verifikasi tabel memuat tujuh class seed, semuanya Active

## Notes

- Pengecualian P-2: kegagalan pembuatan seed yang dipaksa lewat fault injection sisi server (TC-341, TC-342 precondition) hanya berfungsi sebagai pemicu state; objek uji adalah perilaku J-01 dan hasil di tabel, sehingga TC-341 dan 342 tidak dipindah ke spec kelas b. TC-341 dan TC-342 bertanda Manual Only (b) di TC karena kegagalan transaksi seed dan jam scheduler tidak dapat dipicu dari klien; spec menuliskan kebutuhan itu di Prerequisites.
- Langkah penghubung (S-03): langkah 1, 12, dan 20 (pembentuk state: jam awal, reset company, injeksi), langkah 6, 9, 18, 22, 25 (muat ulang), dan langkah 14 (membuka layar; halaman tidak tersedia sebelum modul akuntansi aktif).
- Langkah 2 menulis checkbox header menyeleksi ketujuh baris yang tampil pada satu halaman; klausa "klik `Select All` bila perlu" pada TC-340 langkah 1 tidak ditulis karena tidak diperlukan untuk tujuh baris pada satu halaman (page size default 10).
- Waktu "melewati 00:00 WIB berikutnya" pada TC-340 dan TC-341 ditulis sebagai nilai absolut 15 Okt 2026 17:05 UTC (16 Okt 2026 00:05 WIB); TC tidak menyebut nilai persisnya.
- Langkah 11 menjalankan klausa "tidak ada seed baru" dengan anchor positif Empty State pada langkah 10.
- Post Condition TC-340 ("tidak ada entri L-01 baru"), TC-341 (tujuh entri L-01 Modified By System; tidak ada entri dari percobaan gagal), dan TC-342 (tujuh entri L-01 System setelah langkah 3 TC) tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan L-01 ada di spec pencatatan log.
- Temuan untuk QA:
  - TC-340 precondition d tidak menyebut company mana; TC-341 dan TC-342 membutuhkan company yang dapat dikembalikan ke keadaan belum aktivasi; mekanisme reset company dan fault injection tidak disebut TC, PRD, atau LLD.
  - TC-342 precondition c menyebut "pembuatan seed sebelumnya gagal" tanpa cara membentuknya; TC-342 tidak menyebut apakah J-01 mengenali seed yang pernah gagal berbeda dari seed yang dihapus manual (TC-340).
  - TC-340 langkah 1 memuat "klik `Select All` bila perlu" (langkah bersyarat).
  - Post Condition TC-340, TC-341, TC-342 tanpa langkah observasi di TC.
  - Email akun Total Control tidak tertulis di TC.
