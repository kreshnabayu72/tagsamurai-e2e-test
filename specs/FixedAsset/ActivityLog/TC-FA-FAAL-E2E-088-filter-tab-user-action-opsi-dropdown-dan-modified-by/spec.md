---
id: TC-FA-FAAL-E2E-088-filter-tab-user-action-opsi-dropdown-dan-modified-by
title: "Filter Tab User Action: Opsi Dropdown dan Filter Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-130
  - TC-FA-FAAL-132
  - TC-FA-FAAL-133
coverage:
  web: automated
---

# Filter Tab User Action: Opsi Dropdown dan Filter Modified By

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

### TC-FA-FAAL-130: Opsi dropdown Action, Object, dan Field berasal dari data tabel

1. Klik tab User Action
2. Klik icon Filter
3. Buka dropdown Action
4. Verifikasi dropdown Action berisi tepat: `Activate`, `Assign`, `Auto-Revert`, `Create`, `Delete`, `Edit`, `Finish Audit`, `Remove`, `Report Damaged`, `Report Disposal`
5. Tutup dropdown Action
6. Buka dropdown Object
7. Verifikasi dropdown Object berisi tepat: `Audit`, `Categories`, `Damaged`, `Disposal`, `Group Role`, `Groups`, `Total Control`, `Transactions`, `User`
8. Tutup dropdown Object
9. Buka dropdown Field
10. Verifikasi dropdown Field berisi tepat: `Access Level`, `Category Name`, `Default Loan Duration`, `Group Name`, `Manage asset & TAG — Gedung A`, `Status`
11. Tutup dropdown Field

### TC-FA-FAAL-132: Opsi filter Modified By: satu opsi per nama lengkap dan opsi System

12. Buka dropdown Modified By
13. Verifikasi opsi berlabel nama lengkap: `Admin Alpha`, `Admin Beta`, `Ahmad Dahlan`, `Hendra Pratama`, `System`
14. Verifikasi opsi `Hendra Pratama` muncul satu kali walau UA-13 dan UA-14 berasal dari dua pengguna berbeda
15. Verifikasi opsi `System` ada satu kali
16. Tutup dropdown Modified By

### TC-FA-FAAL-133: Filter Modified By menyaring baris termasuk nama sama dan System

17. Pilih Modified By `Hendra Pratama`, klik `[Apply]`
18. Verifikasi baris UA-13 dan UA-14 tampil
19. Klik `[Clear Field]`, pilih Modified By `Admin Beta`, klik `[Apply]`
20. Verifikasi baris UA-03, UA-06, dan UA-08 tampil
21. Klik `[Clear Field]`, pilih Modified By `System`, klik `[Apply]`
22. Verifikasi hanya baris UA-11 yang tampil
23. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): klik tab User Action dan icon Filter di awal; menutup dropdown; `[Clear Field]` lalu `[Apply]` di antara filter Modified By.
- TC-FA-FAAL-132 dan 133 ditulis fungsional karena seluruh alurnya satu sesi: `Hendra Pratama` ganda berasal dari dua baris seed (UA-13 pengguna `Hendra Pratama #1`, UA-14 pengguna `Hendra Pratama #2`).
- Tidak ada Post Condition TC pada blok ini.
- Temuan untuk QA:
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]` dan saat berpindah tab; spec mengasumsikan panel tetap terbuka dan membukanya sekali di awal.
