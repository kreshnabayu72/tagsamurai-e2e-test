---
id: TC-FA-FAAL-E2E-039-filter-tab-user-action-pemulihan-dan-tanpa-hasil
title: "Filter Tab User Action: Kosongkan Search, Pemulihan Empty State, dan Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-140
  - TC-FA-FAAL-141
  - TC-FA-FAAL-142
coverage:
  web: automated
---
# Filter Tab User Action: Kosongkan Search, Pemulihan Empty State, dan Tanpa Hasil

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
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action
2. Klik icon Filter

### Precondition TC-FA-FAAL-140 (langkah TC-FA-FAAL-138 butir 1 sampai 3, dipakai sebagai precondition, tidak diasersi)

3. Pilih Object `Groups`, klik `[Apply]`
4. Ketik Search `Gedung`, tekan Enter
5. Klik header Name sekali (Ascending)

### TC-FA-FAAL-140: Kosongkan Search mempertahankan Filter dan Sort

6. Klik `✕` pada kotak Search, tekan Enter
7. Verifikasi Filter Object `Groups` tetap aktif
8. Verifikasi Sort Name Ascending tetap aktif
9. Verifikasi urutan baris UA-11, UA-02, UA-13, UA-14, UA-15

### TC-FA-FAAL-141: Pemulihan dari empty state

10. Klik `[Clear Field]`, klik `[Apply]`
11. Klik header Name dua kali (kembali ke urutan default)
12. Pilih Object `Audit`, klik `[Apply]`
13. Ketik Search `zzz`, tekan Enter
14. Verifikasi state `No results found`
15. Kosongkan isi kotak Search, tekan Enter
16. Verifikasi baris UA-06 tampil kembali

### TC-FA-FAAL-142: Filter tanpa hasil menampilkan state kosong terfilter

17. Klik `[Clear Field]`, klik `[Apply]`
18. Pilih Action `Delete` dan Object `Audit`
19. Klik `[Apply]`
20. Verifikasi tampil Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
21. Verifikasi tidak ada baris tabel dan tidak ada pesan error

## Notes

- Langkah penghubung (S-03): klik tab User Action dan icon Filter di awal; tiga langkah precondition TC-FA-FAAL-140 disalin dari TC-FA-FAAL-138 butir 1 sampai 3 (S-04) dan tidak diasersi (Rows per page 25 pada butir 4 TC-FA-FAAL-138 tidak termasuk state precondition TC-FA-FAAL-140); `[Clear Field]` lalu `[Apply]` dan klik header Name dua kali sebagai pemulihan di antara blok. Panel Filter tetap terbuka sesudah dibuka (langkah "Klik icon Filter" TC tidak diulang).
- Pada TC-FA-FAAL-141, "Kosongkan Search lalu Enter" ditulis "kosongkan isi kotak Search, tekan Enter" (bagian 8b butir 9).
- TC-FA-FAAL-142 butir b ("tidak ada baris tabel dan tidak ada pesan error") didahului empty state `No results found` pada butir a sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-FAAL-140 mencantumkan state precondition tanpa langkah pembentuknya dan hanya menyebut dependensi TC-FA-FAAL-138; spec menyalin tiga langkah pertama TC-FA-FAAL-138.
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]` dan saat berpindah tab; spec mengasumsikan panel tetap terbuka (TC-FA-FAAL-129 mengulang `[Clear Field]` dan `[Apply]` tanpa membuka panel lagi).

