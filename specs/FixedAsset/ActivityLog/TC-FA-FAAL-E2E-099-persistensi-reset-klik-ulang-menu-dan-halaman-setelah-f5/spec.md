---
id: TC-FA-FAAL-E2E-099-persistensi-reset-klik-ulang-menu-dan-halaman-setelah-f5
title: "Persistensi Reset Klik Ulang Menu dan Halaman Aktif Setelah F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-196
  - TC-FA-FAAL-287
coverage:
  web: automated
---
# Persistensi Reset Klik Ulang Menu dan Halaman Aktif Setelah F5

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
- Jendela Seed Tab User Action (precondition TC-FA-FAAL-287): Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15), diterapkan di langkah 15, sesudah langkah 8 yang mengosongkan seluruh state tab. TC-FA-FAAL-196 tidak memuat Filter Date. Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAL-196: Klik ulang menu Activity Log di sidebar mereset state

1. Klik menu Activity Log di sidebar Reports & Logs
2. Klik `Next` untuk pindah ke halaman 2 Tab Session
3. Ketik Search `Chrome`, tekan Enter
4. Klik tab User Action
5. Ketik Search `Citra`, tekan Enter
6. Klik icon Filter, pilih Action `Assign`, klik `[Apply]`
7. Klik header Name sekali (Ascending)
8. Klik menu Activity Log di sidebar Reports & Logs
9. Verifikasi halaman terbuka di Tab Session (tab default)
10. Verifikasi Tab Session tanpa Search, Filter, maupun Sort
11. Verifikasi Tab Session di halaman 1
12. Verifikasi Tab Session memakai Rows per page 10
13. Klik tab User Action
14. Verifikasi Tab User Action kembali ke default: tanpa Search, Filter, maupun Sort
15. Di Tab User Action klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-287: Refresh F5 mempertahankan halaman aktif

16. Klik header Name sekali (Ascending)
17. Klik `Next` untuk pindah ke halaman 2
18. Tekan F5
19. Verifikasi Tab User Action tetap aktif
20. Verifikasi Sort Name Ascending tetap aktif
21. Verifikasi teks pagination tetap `Showing 11–15 of 15 entries`

## Notes

- Langkah penghubung (S-03): klik tab Session dan tab User Action untuk berpindah tab; langkah pertama TC-FA-FAAL-196 (klik menu Activity Log di sidebar Reports & Logs) memastikan awal di Tab Session. TC-FA-FAAL-287 berlanjut di Tab User Action dari akhir TC-FA-FAAL-196 (tab itu sudah terbuka setelah verifikasi default), sehingga langkah "Klik tab User Action" TC tidak diulang.
- Langkah 15 (S-03): menerapkan Filter Date Jendela Seed Tab User Action sesuai precondition d TC-FA-FAAL-287, setelah state tab dikosongkan oleh langkah 8 (TC-FA-FAAL-196).
- Panel Filter tiap tab dibuka satu kali dan diasumsikan tetap terbuka beserta nilai ter-Apply-nya.
- Ukuran spec 21 langkah. TC-FA-FAAL-194 dan 195 ada di spec 045.
- Temuan untuk QA:
  - TC-FA-FAAL-196 butir b ("Tab User Action juga kembali ke default saat dibuka") mensyaratkan membuka Tab User Action; spec menambah langkah klik tab itu sebagai langkah menuju keadaannya (S-14).
  - TC-FA-FAAL-196 langkah 1 meminta "pindah ke halaman 2 dan Search `Chrome`" tanpa menyebut urutan; Search mereset ke halaman 1 (TC-FA-FAAL-160), sehingga spec mengikuti urutan penulisan TC (halaman 2 lalu Search).
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]` dan saat berpindah tab; spec mengasumsikan panel tetap terbuka beserta nilai ter-Apply-nya.
  - TC-FA-FAAL-287 memberi precondition Filter Date Jendela Seed Tab User Action (18/06/26 sampai 18/06/26) agar angka `15 entries` tidak bergantung pada baris log lain; spec menerapkannya di langkah 15 dan mengikuti angka TC.
