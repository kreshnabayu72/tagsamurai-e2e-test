---
id: TC-FA-FAAL-E2E-089-filter-tab-user-action-kombinasi-filter-search-sort-dan-clear-field
title: "Filter Tab User Action: Kombinasi Filter, Search, Sort, Ukuran Halaman, dan Clear Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-138
  - TC-FA-FAAL-139
coverage:
  web: automated
---

# Filter Tab User Action: Kombinasi Filter, Search, Sort, Ukuran Halaman, dan Clear Field

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

### TC-FA-FAAL-138: Kombinasi Filter, Search, Sort, dan ukuran halaman

3. Pilih Object `Groups`, klik `[Apply]`
4. Ketik Search `Gedung`, tekan Enter
5. Klik header Name sekali (Ascending)
6. Ubah Rows per page menjadi 25
7. Verifikasi urutan baris UA-02, UA-13, UA-14, UA-15
8. Verifikasi Filter Object `Groups` tetap aktif
9. Verifikasi Search `Gedung` tetap aktif
10. Verifikasi Sort Name Ascending tetap aktif
11. Verifikasi teks pagination `Showing 1–4 of 4 entries`

### TC-FA-FAAL-139: Clear Field filter mempertahankan Search dan Sort

12. Klik `[Clear Field]`, klik `[Apply]`
13. Verifikasi Search `Gedung` tetap aktif
14. Verifikasi Sort Name Ascending tetap aktif
15. Verifikasi urutan baris UA-07, UA-12, UA-02, UA-13, UA-14, UA-15, UA-06
16. Klik `(←)` pada kotak Search
17. Klik header Name dua kali (kembali ke urutan default)
18. Ubah Rows per page menjadi 10

## Notes

- Langkah penghubung (S-03): klik tab User Action dan icon Filter di awal; pada TC-FA-FAAL-139 state precondition (Object `Groups`, Search `Gedung`, Sort Name Ascending) dibentuk oleh langkah TC-FA-FAAL-138 yang dijalankan lebih dulu (S-04); tiga langkah terakhir mengembalikan Search, Sort, dan Rows per page (S-09).
- Spec dimulai dari Filter, Search, dan Sort bersih (data seed baca saja), sehingga TC-FA-FAAL-138 tidak memerlukan langkah pembersih di awal.
- Temuan untuk QA:
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]` dan saat berpindah tab; spec mengasumsikan panel tetap terbuka dan membukanya sekali di awal.
