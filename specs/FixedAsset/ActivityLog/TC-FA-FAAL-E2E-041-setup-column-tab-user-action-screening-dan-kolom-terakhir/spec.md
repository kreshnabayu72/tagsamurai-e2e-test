---
id: TC-FA-FAAL-E2E-041-setup-column-tab-user-action-screening-dan-kolom-terakhir
title: "Setup Column Tab User Action: Screening Overlay dan Popup, serta Kolom Visible Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-147
  - TC-FA-FAAL-148
  - TC-FA-FAAL-154
coverage:
  web: automated
---
# Setup Column Tab User Action: Screening Overlay dan Popup, serta Kolom Visible Terakhir

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
- Pemulihan Setup Column: hook `after` spec ini menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`; kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action

### TC-FA-FAAL-147: Screening Overlay Column Visibility

2. Klik header kolom Actions (⋯)
3. Verifikasi overlay memuat 8 kolom berurutan: Date, Action, Object, Name, Field, Old Value, New Value, Modified By
4. Verifikasi semua checkbox tercentang dan enabled
5. Verifikasi setiap baris punya drag handle
6. Verifikasi item `Setup Column...` ada di bagian bawah overlay

### TC-FA-FAAL-148: Screening Popup Setup Column

7. Klik `Setup Column...`
8. Verifikasi header popup: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol close `(X)`
9. Verifikasi kedelapan kolom pada body popup tercentang
10. Verifikasi setiap kolom pada body popup punya drag handle
11. Verifikasi setiap kolom pada body popup punya icon Pin
12. Verifikasi Live Preview tampil pada body popup
13. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan
14. Verifikasi tidak ada `[Cancel]` pada footer
15. Klik `(X)` untuk menutup popup

### TC-FA-FAAL-154: Kolom visible terakhir tidak dapat disembunyikan

16. Klik header kolom Actions (⋯)
17. Klik `Setup Column...`
18. Hilangkan centang kolom Date, Action, Object, Name, Field, Old Value, dan New Value satu per satu hingga hanya Modified By tercentang
19. Arahkan kursor ke checkbox Modified By
20. Verifikasi checkbox Modified By disabled dengan tooltip `At least one column must remain visible.`
21. Coba hilangkan centang Modified By
22. Verifikasi Modified By tetap tercentang
23. Verifikasi Live Preview tetap memiliki satu kolom data
24. Klik `(X)` untuk menutup popup tanpa `[Save]`

## Notes

- Langkah penghubung (S-03): klik tab User Action di awal; overlay Column Visibility pada TC-FA-FAAL-147 tetap terbuka sehingga TC-FA-FAAL-148 langsung mengklik `Setup Column...` tanpa klik header lagi; `(X)` menutup popup di akhir TC-FA-FAAL-148 dan TC-FA-FAAL-154.
- Spec ini hanya membuka popup dan tidak menyimpan konfigurasi kolom; hook `after` tetap memulihkan preferensi kolom sebagai jaring pengaman.
- Pembagian TC lintas spec: TC-FA-FAAL-149 ada di spec 071; TC-FA-FAAL-150, 152, dan 153 di spec 042; TC-FA-FAAL-151 di spec 072.
- Temuan untuk QA:
  - TC-FA-FAAL-154 butir b menyebut "tabel tetap memiliki satu kolom data", sedangkan langkah TC tidak menekan `[Save]` sehingga tabel di belakang popup belum berubah; spec memverifikasi Live Preview pada popup (konfigurasi belum disimpan). Bila yang dimaksud tabel, TC perlu menambah langkah `[Save]`.
  - TC-FA-FAAL-148 butir b menyebut drag handle dan icon Pin tanpa menyebut per kolom; spec membaca keduanya berlaku untuk tiap kolom.

