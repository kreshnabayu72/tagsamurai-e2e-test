---
id: TC-FA-FAAL-E2E-038-filter-tab-user-action-logika-dan-interaksi
title: "Filter Tab User Action: Logika AND dan OR serta Interaksi Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-134
  - TC-FA-FAAL-135
  - TC-FA-FAAL-136
  - TC-FA-FAAL-137
coverage:
  web: automated
---

# Filter Tab User Action: Logika AND dan OR serta Interaksi Search dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Admin Alpha; General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
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
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action
2. Klik icon Filter

### TC-FA-FAAL-134: Dua field filter berbeda memakai logika AND

3. Pilih Action `Assign`
4. Pilih Object `Group Role`
5. Klik `[Apply]`
6. Verifikasi hanya baris UA-07 yang tampil

### TC-FA-FAAL-135: Dua opsi dalam satu field filter memakai logika OR

7. Klik `[Clear Field]`, klik `[Apply]`
8. Pilih Action `Delete` dan `Remove`
9. Klik `[Apply]`
10. Verifikasi baris UA-03 dan UA-12 tampil

### TC-FA-FAAL-136: Search lalu Filter

11. Klik `[Clear Field]`, klik `[Apply]`
12. Ketik Search `Citra`, tekan Enter
13. Verifikasi baris UA-07, UA-10, dan UA-12 tampil
14. Pilih Action `Assign`, klik `[Apply]`
15. Verifikasi hanya baris UA-07 yang tampil
16. Verifikasi keyword `Citra` tetap terisi pada kotak Search

### TC-FA-FAAL-137: Filter lalu Search

17. Klik `[Clear Field]`, klik `[Apply]`
18. Klik `(←)` pada kotak Search
19. Pilih Action `Assign`, klik `[Apply]`
20. Verifikasi baris UA-01 dan UA-07 tampil
21. Ketik Search `Citra`, tekan Enter
22. Verifikasi hanya baris UA-07 yang tampil
23. Verifikasi filter Action `Assign` tetap aktif

## Notes

- Langkah penghubung (S-03): klik tab User Action dan icon Filter di awal; `[Clear Field]` lalu `[Apply]` dan `(←)` pada kotak Search di antara blok (langkah 7, 11, 17, 18).
- Panel Filter dibuka satu kali dan tetap terbuka; langkah "Klik icon Filter" TC-FA-FAAL-135, 136, dan 137 tidak diulang karena akan menutup panel.
- Temuan untuk QA:
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]` dan saat berpindah tab; spec mengasumsikan panel tetap terbuka (TC-FA-FAAL-135 mengulang `[Clear Field]` dan `[Apply]` tanpa membuka panel lagi).
