---
id: TC-FA-FAAL-E2E-042-setup-column-tab-user-action-urutan-reset-tutup
title: "Setup Column Tab User Action: Reset to Default dan Tutup tanpa Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-152
  - TC-FA-FAAL-153
coverage:
  web: automated
---
# Setup Column Tab User Action: Reset to Default dan Tutup tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Admin Alpha; General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
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
- Pemulihan Setup Column: hook `after` spec ini menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`; kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action

### TC-FA-FAAL-152: Reset to Default pada Popup Setup Column

2. Klik header kolom Actions (⋯)
3. Klik `Setup Column...`
4. Sembunyikan kolom Field
5. Drag kolom Modified By ke posisi pertama
6. Pin kolom Date
7. Klik `[Save]`
8. Klik header kolom Actions (⋯)
9. Klik `Setup Column...`
10. Klik `[Reset to Default]`
11. Klik `[Save]`
12. Verifikasi 8 kolom default dengan urutan awal tampil di tabel
13. Verifikasi tidak ada kolom beku
14. Muat ulang halaman (F5)
15. Verifikasi 8 kolom default dengan urutan awal tetap setelah muat ulang
16. Verifikasi tidak ada kolom beku setelah muat ulang

### TC-FA-FAAL-153: Tutup Popup Setup Column tanpa Save

17. Klik header kolom Actions (⋯)
18. Klik `Setup Column...`
19. Sembunyikan kolom Field
20. Klik `(X)`
21. Verifikasi kolom Field tetap tampil di tabel
22. Klik header kolom Actions (⋯)
23. Klik `Setup Column...`
24. Sembunyikan kolom Field
25. Tekan Esc
26. Verifikasi kolom Field tetap tampil di tabel

## Notes

- Langkah penghubung (S-03): klik tab User Action di awal agar spec mulai di tab yang benar (layar awal hook `beforeEach` suite berada di Tab Session); kolom Field disembunyikan dengan menghilangkan centang checkbox-nya.
- Ukuran spec 26 langkah. TC-FA-FAAL-150 (iterasi per kolom) ada di spec 095 (konvensi bagian 3, batas ukuran).
- Pembagian TC lintas spec: TC-FA-FAAL-149 ada di spec 071 dan TC-FA-FAAL-151 di spec 072, masing-masing berupa iterasi per kolom yang berdiri sendiri; TC-FA-FAAL-147, 148, dan 154 di spec 041; TC-FA-FAAL-150 di spec 095.
- Temuan untuk QA:
  - TC-FA-FAAL-152 langkah 4 menyebut "amati" sesudah `[Reset to Default]` tanpa Expected sendiri; spec tidak menambah `Verifikasi` sebelum `[Save]`.
  - TC-FA-FAAL-153 mengasumsikan tutup lewat `(X)` atau Esc pada popup yang berubah tidak memunculkan dialog konfirmasi; TC tidak menyebut dialog `Unsaved Changes` untuk popup ini.
