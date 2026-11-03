---
id: TC-AC-ACAL-E2E-009-pagination-info-page-size-navigasi-dan-reset-halaman
title: "Pagination: Info, Page Size, Navigasi, dan Reset Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-116
  - TC-AC-ACAL-117
coverage:
  web: automated
---

# Pagination: Info, Page Size, Navigasi, dan Reset Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log yang di-seed di hook `before` (volume 35 entri per tab, Pre-setup No 11; kemampuan seeding log dengan stempel tanggal yang dapat ditentukan disediakan tim FE/BE; lihat Temuan untuk QA):
  - Seluruh entri seed spec ini berstempel satu tanggal khusus `{tanggalSeed}`; nilainya ditetapkan tim FE (satu tanggal khusus spec 009 yang tidak dipakai entri lain pada entitas aktor dan tidak sama dengan `22 Jun 2026`, tanggal seed spec 002); Filter Date `{tanggalSeed}`–`{tanggalSeed}` membatasi tabel sehingga total 35 entri dapat diasersi tanpa mengandalkan total tabel hidup (S-12).
  - Tab Session: tepat 35 entri pada `{tanggalSeed}`, dengan 15 entri milik `John Doe` (Division `Marketing`; nama literal menurut Lampiran A-3; seeding idempotent, dilewati bila sudah ada, dan tidak dihapus) dan 20 entri milik user lain (Division `Finance`).
  - Tab User Action: tepat 35 entri pada `{tanggalSeed}` dengan Name bersuffix `{runId}-009`.
  - Seeding idempotent (dilewati bila sudah ada), tidak dihapus (audit trail permanen).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-116: Pagination, info, page size, navigasi, kedua tab

1. Klik icon Filter, pilih Date `{tanggalSeed}`–`{tanggalSeed}`, klik `[Apply]`
2. Verifikasi tab Session: footer `Showing 1–10 of 35 entries`
3. Buka pilihan Rows per page tab Session
4. Verifikasi tab Session: pilihan Rows per page `10`, `25`, `50`, `100` (tanpa All)
5. Tutup pilihan Rows per page dengan `Esc`
6. Klik `[Next →]`
7. Verifikasi tab Session: footer `Showing 11–20 of 35 entries`
8. Ganti Rows per page ke `25`
9. Verifikasi tab Session: kembali ke halaman 1, footer `Showing 1–25 of 35 entries`
10. Ketik `2` di input halaman, tekan Enter
11. Verifikasi tab Session: footer `Showing 26–35 of 35 entries`
12. Klik tab "User Action"
13. Klik icon Filter, pilih Date `{tanggalSeed}`–`{tanggalSeed}`, klik `[Apply]`
14. Verifikasi tab User Action: footer `Showing 1–10 of 35 entries`
15. Buka pilihan Rows per page tab User Action
16. Verifikasi tab User Action: pilihan Rows per page `10`, `25`, `50`, `100` (tanpa All)
17. Tutup pilihan Rows per page dengan `Esc`
18. Klik `[Next →]`
19. Verifikasi tab User Action: footer `Showing 11–20 of 35 entries`
20. Ganti Rows per page ke `25`
21. Verifikasi tab User Action: kembali ke halaman 1, footer `Showing 1–25 of 35 entries`
22. Ketik `2` di input halaman, tekan Enter
23. Verifikasi tab User Action: footer `Showing 26–35 of 35 entries`

### TC-AC-ACAL-117: Pagination reset ke halaman 1 saat Search atau Filter diterapkan

24. Klik tab "Session"
25. Ganti Rows per page ke `10`
26. Ketik `3` di input halaman, tekan Enter
27. Verifikasi tab Session: halaman 3 aktif (`Showing 21–30 of 35 entries`)
28. Ketik Search `John`, tekan Enter
29. Verifikasi kembali ke halaman 1
30. Klik `[Next →]` ke halaman 2
31. Klik icon Filter, pilih Division `Marketing`, klik `[Apply]`
32. Verifikasi kembali ke halaman 1

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-116, 117). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 13 (Filter Date `{tanggalSeed}` membatasi tabel pada seed supaya total 35 dapat diasersi pada audit trail yang tumbuh; S-12), langkah 5 dan 17 (menutup pilihan Rows per page), dan langkah 24 sampai 26 (kembali ke tab Session, mengembalikan Rows per page ke `10` setelah TC-116, dan menuju halaman 3 sebagai precondition TC-117).
- Asersi tambahan di luar Expected TC (S-03): langkah 27 (halaman 3 aktif, `Showing 21–30 of 35 entries`) membuktikan precondition TC-117 "User di halaman 3" tercapai sebelum Search diterapkan.
- Langkah TC-116 nomor 5 ("Ulangi langkah 1-4 di tab User Action") ditulis eksplisit per langkah untuk tab User Action supaya tiap klausa Expected punya `Verifikasi` sendiri (S-01).
- Filter Date tab Session tetap aktif selama TC-117 (Filter tiap tab dipertahankan); Search `John` dan Filter Division `Marketing` bekerja atas seed yang sudah dibatasi tanggal.
- Temuan untuk QA:
  - TC-116 mensyaratkan "35 entri per tab" sebagai total mutlak, sedangkan Activity Log adalah audit trail permanen yang tumbuh; spec membatasi tabel dengan Filter Date atas tanggal seed khusus dan menulis komposisi seed di Prerequisites.
  - TC-117 menyebut "Apply filter Division" tanpa nilai; spec memakai Division `Marketing`.
  - TC-117 precondition ("User di halaman 3") tidak menyebut Rows per page; spec memakai 10 baris per halaman supaya halaman 3 ada pada 35 entri.
  - Mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
