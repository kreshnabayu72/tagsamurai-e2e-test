---
id: TC-FA-FAAL-E2E-097-paginasi-search-dan-apply-filter-mereset-ke-halaman-1
title: "Paginasi: Search dan Apply Filter Mereset ke Halaman 1"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-160
coverage:
  web: automated
---
# Paginasi: Search dan Apply Filter Mereset ke Halaman 1

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Admin Alpha; General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11; Activity `Session`, Status `—`; waktu Asia/Jakarta), urutan default Date terbaru dahulu. Format: Date; User (Employee ID, Position, Division); Activity; IP; Device.
  - SS-01: 14/07/26 08:05; John Doe (EMP001, Staff, Marketing); Session started; 192.168.1.10; Chrome on Windows
  - SS-02: 14/07/26 09:30; John Doe (EMP001, Staff, Marketing); Session ended; Chrome on Windows
  - SS-03: 14/07/26 10:00; Siti Nurbaya (EMP002, Manager, Finance); Concurrent limit reached; 10.0.0.5; Safari on iOS
  - SS-04: 14/07/26 14:00; Mike Tan (EMP003, Staff, Operations); Logged out by admin; 172.16.0.8; Chrome on Android
  - SS-05: 15/07/26 08:00; Jane Smith (tanpa Employee ID dan Position, Finance); Session started; IP kosong; TAG Samurai App on Android
  - SS-06: 15/07/26 09:00; Budi Santoso (EMP004, Supervisor, Operations); Session started; 9.0.0.1; Device tidak terparse sebagian
  - SS-07: 15/07/26 10:00; Dewi Lestari (EMP005, Staff, Marketing); Session started; 10.0.0.2; Device tidak terparse
  - SS-08: 15/07/26 11:00; Hendra Pratama #1 (EMP006, Staff, Marketing); Session started; 192.168.1.20; Firefox on Linux
  - SS-09: 15/07/26 12:00; Hendra Pratama #2 (EMP007, Manager, Finance); Session started; 192.168.1.21; Edge on Windows
  - SS-10: 16/07/26 08:00; John Dalton (EMP008, Staff, Operations); Session started; 192.168.2.10; Chrome on Windows
  - SS-11: 16/07/26 09:00; John Davis (EMP009, Supervisor, Finance); Session ended; 192.168.2.11; Safari on macOS
- Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), seluruhnya bertanggal 18/06/26 (Asia/Jakarta), urutan default Date terbaru dahulu. Format: Date; Action; Object; Name; Field; Old Value; New Value; Modified By.
  - UA-01: 14:30; Assign; Total Control; Budi Santoso; Access Level; `—`; Total Control; Admin Alpha
  - UA-02: 14:25; Edit; Groups; Gedung A > Lantai 3 - Renovasi; Group Name; Lantai 3; Lantai 3 - Renovasi; Admin Alpha
  - UA-03: 13:00; Delete; Categories; Electronic Devices; Category Name; Electronic Devices; `—`; Admin Beta
  - UA-04: 12:45; Report Disposal; Disposal; Kendaraan Operasional (AST-2024-0088); Status; In Use; In Disposal Process; Admin Alpha
  - UA-05: 12:30; Report Damaged; Damaged; Kamera DSLR (AST-2024-0141); Status; Borrowed; Damaged; Ahmad Dahlan
  - UA-06: 12:00; Finish Audit; Audit; Task Audit Q3-Gedung A; Status; In Audit; Waiting for Approval; Admin Beta
  - UA-07: 11:30; Assign; Group Role; Citra Lestari; Manage asset & TAG — Gedung A; `—`; Assigned; Admin Alpha
  - UA-08: 11:00; Edit; Transactions; `—`; Default Loan Duration; 7 days; 14 days; Admin Beta (seed BE)
  - UA-09: 10:30; Auto-Revert; Total Control; Dewi Lestari; Access Level; Total Control; `—`; Admin Alpha
  - UA-10: 10:00; Activate; User; Citra Lestari; Status; Inactive; Active; Admin Alpha
  - UA-11: 09:30; Create; Groups; Default Group; Group Name; `—`; Default Group; System (seed BE)
  - UA-12: 09:00; Remove; Group Role; Citra Lestari; Manage asset & TAG — Gedung A; Assigned; `—`; Admin Alpha
  - UA-13: 08:30; Edit; Groups; Gedung B; Group Name; Gedung B1; Gedung B; Hendra Pratama #1
  - UA-14: 08:00; Edit; Groups; Gedung C; Group Name; Gedung C1; Gedung C; Hendra Pratama #2
  - UA-15: 07:30; Create; Groups; `Gedung Serbaguna` + nama 120 karakter; Group Name; `—`; nama sama; Admin Alpha
- Seed dan pemulihan data log lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Identitas data dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Spec hanya membaca baris log seed dan tidak membuat, mengubah, atau menghapus baris log maupun data Pre-setup.
- Jendela Seed Tab Session (precondition TC-FA-FAAL-160): Filter Date `14/07/26` sampai `16/07/26` (memuat SS-01 sampai SS-11), diterapkan di langkah 1 dan tetap terpasang saat Search dan Filter Division diterapkan; langkah `[Clear Field]` lalu `[Apply]` di akhir ikut mengosongkan Filter Date. Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAL-160: Search dan Apply Filter mereset ke halaman 1

1. Di Tab Session klik icon Filter, pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date, klik `[Apply]`
2. Klik `Next` untuk pindah ke halaman 2
3. Ketik Search `Chrome`, tekan Enter
4. Verifikasi Tab Session tampil di halaman 1 dengan `Showing 1–4 of 4 entries`
5. Klik `(←)` pada kotak Search
6. Klik `Next` untuk pindah ke halaman 2
7. Pilih Division `Finance` pada panel Filter, klik `[Apply]`
8. Verifikasi Tab Session tampil di halaman 1 dengan `Showing 1–4 of 4 entries`
9. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): `(←)` pada kotak Search dan `[Clear Field]` lalu `[Apply]` memulihkan state akhir TC; layar awal berada di Tab Session (hook `beforeEach` suite).
- Langkah 1 (S-03): menerapkan Filter Date Jendela Seed Tab Session sesuai precondition e TC-FA-FAAL-160. Langkah 7 memakai panel Filter yang diasumsikan tetap terbuka sesudah `[Apply]` pada langkah 1.
- Ukuran spec 9 langkah. TC-FA-FAAL-155 dan 156 ada di spec 043 dan TC-FA-FAAL-157 sampai 159 di spec 096.
- Temuan untuk QA:
  - TC-FA-FAAL-160 memberi precondition Filter Date Jendela Seed Tab Session (14/07/26 sampai 16/07/26) agar angka `4 entries` hasil Search dan Filter tidak bergantung pada baris log lain; spec menerapkannya di langkah 1 dan mengikuti angka TC.
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]`; spec mengasumsikan panel tetap terbuka beserta nilai ter-Apply-nya.
