---
id: TC-FA-FAAL-E2E-045-persistensi-refresh-f5-dan-reset-klik-ulang-menu
title: "Persistensi Refresh F5 pada Search, Filter, Sort, Rows per Page, dan Tab Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-194
  - TC-FA-FAAL-195
coverage:
  web: automated
---
# Persistensi Refresh F5 pada Search, Filter, Sort, Rows per Page, dan Tab Aktif

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
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAL-194: Refresh F5 mempertahankan Search, Filter, Sort, dan Rows per page tiap tab

1. Di Tab Session ketik Search `Chrome`, tekan Enter
2. Klik icon Filter, pilih Division `Marketing`, klik `[Apply]`
3. Klik header User sekali (Ascending)
4. Ubah Rows per page menjadi 25
5. Klik tab User Action
6. Klik icon Filter, pilih Object `Groups`, klik `[Apply]`
7. Klik header Name sekali (Ascending)
8. Tekan F5
9. Verifikasi Filter Object `Groups` tetap pada Tab User Action
10. Verifikasi Sort Name Ascending tetap aktif pada Tab User Action
11. Klik tab Session
12. Verifikasi Search `Chrome` tetap pada Tab Session
13. Verifikasi Filter Division `Marketing` tetap pada Tab Session
14. Verifikasi Sort User Ascending tetap aktif pada Tab Session
15. Verifikasi Rows per page 25 tetap pada Tab Session
16. Klik menu Activity Log di sidebar Reports & Logs

### TC-FA-FAAL-195: Refresh F5 mempertahankan tab aktif

17. Klik tab User Action
18. Tekan F5
19. Verifikasi Tab User Action tetap aktif

## Notes

- Langkah penghubung (S-03): klik tab Session dan tab User Action untuk berpindah tab; `Klik menu Activity Log di sidebar Reports & Logs` pada akhir TC-FA-FAAL-194 memulihkan semua state dan membuka Tab Session sebelum TC-FA-FAAL-195.
- Panel Filter tiap tab dibuka satu kali dan diasumsikan tetap terbuka beserta nilai ter-Apply-nya.
- Pada TC-FA-FAAL-194, F5 dilakukan ketika Tab User Action aktif; sesuai TC-FA-FAAL-195, tab aktif tetap sama sesudah muat ulang, sehingga tab Session dibuka lewat klik tab sebelum asersi Tab Session.
- Ukuran spec 19 langkah (konvensi bagian 3, batas ukuran). TC-FA-FAAL-196 dan 287 ada di spec 099.
- Temuan untuk QA:
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]` dan saat berpindah tab; spec mengasumsikan panel tetap terbuka beserta nilai ter-Apply-nya.
  - Total `11 entries` (Tab Session) dan `15 entries` (Tab User Action) pada TC bergantung pada log client Pre-setup #11 dan #12 yang tidak bertambah. Log immutable dan spec lain menambah baris pada client yang sama, sehingga total absolut dapat berubah (S-12, S-14); TC tidak menyatakan client khusus atau Filter pembatas. Spec mengikuti angka TC.
