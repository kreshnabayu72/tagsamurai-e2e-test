---
id: TC-FA-FAAL-E2E-043-paginasi-rows-per-page-dan-showing-kedua-tab
title: "Paginasi: Rows per Page Default dan Navigasi Halaman di Kedua Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-155
  - TC-FA-FAAL-156
coverage:
  web: automated
---
# Paginasi: Rows per Page Default dan Navigasi Halaman di Kedua Tab

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
  - UA-04: 12:45; Report Disposal; Disposal; Kendaraan Operasional (AST-2024-0088); Status; In Use; Reported Disposal; Admin Alpha
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
- Jendela Seed (precondition TC-FA-FAAL-156): Tab Session Filter Date `14/07/26` sampai `16/07/26` (memuat SS-01 sampai SS-11), diterapkan di langkah 11; Tab User Action Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15), diterapkan di langkah 21. Total `11 entries` dan `15 entries` dihitung hanya atas baris seed. TC-FA-FAAL-155 tidak memuat Filter Date. State yang diubah: Filter Date kedua tab, di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAL-155: Rows per page default dan opsi di kedua tab

1. Verifikasi Rows per page Tab Session bernilai awal `10`
2. Buka overlay Rows per page
3. Verifikasi overlay memuat tepat opsi 10, 25, 50, 100 tanpa opsi All
4. Tutup overlay Rows per page
5. Klik tab User Action
6. Verifikasi Rows per page Tab User Action bernilai awal `10`
7. Buka overlay Rows per page
8. Verifikasi overlay memuat tepat opsi 10, 25, 50, 100 tanpa opsi All
9. Tutup overlay Rows per page

### TC-FA-FAAL-156: Navigasi halaman dan teks Showing di kedua tab

10. Klik tab Session
11. Di Tab Session klik icon Filter, pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date, klik `[Apply]`
12. Verifikasi teks pagination Tab Session halaman 1 `Showing 1–10 of 11 entries`
13. Klik `Next`
14. Verifikasi teks pagination halaman 2 `Showing 11–11 of 11 entries`
15. Verifikasi halaman 2 berisi satu baris
16. Klik `Prev`
17. Verifikasi tabel kembali ke halaman 1
18. Ketik `2` pada input halaman, tekan Enter
19. Verifikasi halaman 2 terbuka langsung
20. Klik tab User Action
21. Di Tab User Action klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`
22. Verifikasi teks pagination Tab User Action halaman 1 `Showing 1–10 of 15 entries`
23. Klik `Next`
24. Verifikasi teks pagination halaman 2 `Showing 11–15 of 15 entries`
25. Klik `Prev`
26. Verifikasi tabel kembali ke halaman 1
27. Ketik `2` pada input halaman, tekan Enter
28. Verifikasi halaman 2 terbuka langsung
29. Klik `Prev`
30. Klik tab Session
31. Klik `Prev`

## Notes

- Langkah penghubung (S-03): klik tab Session dan tab User Action untuk berpindah tab; `Prev` memulihkan state sebelum TC berikutnya mengandalkannya (S-09); layar awal berada di Tab Session (hook `beforeEach` suite).
- Langkah 11 dan 21 (S-03): menerapkan Filter Date Jendela Seed tiap tab sesuai precondition e TC-FA-FAAL-156.
- TC-FA-FAAL-156 butir `Pada halaman 1` dipenuhi dengan menekan `Prev` di akhir TC pada kedua tab.
- Ukuran spec 31 langkah. TC-FA-FAAL-157 sampai 159 ada di spec 096 dan TC-FA-FAAL-160 di spec 097.
- Temuan untuk QA:
  - TC-FA-FAAL-156 butir c ("Prev kembali ke halaman 1 dan input halaman 2 langsung membuka halaman 2") tidak menyebut tab; spec memverifikasinya di kedua tab.
  - TC-FA-FAAL-156 memberi precondition Filter Date Jendela Seed pada kedua tab (Tab Session 14/07/26 sampai 16/07/26; Tab User Action 18/06/26 sampai 18/06/26) agar angka `11 entries` dan `15 entries` tidak bergantung pada baris log lain; spec menerapkannya di langkah 11 dan 21 dan mengikuti angka TC.
