---
id: TC-FA-FAAL-E2E-040-sort-tab-user-action
title: "Sort Tab User Action: Date, Teks, Modified By, Old/New Value"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-143
  - TC-FA-FAAL-144
  - TC-FA-FAAL-145
  - TC-FA-FAAL-146
coverage:
  web: automated
---
# Sort Tab User Action: Date, Teks, Modified By, Old/New Value

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
- Jendela Seed Tab User Action: Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15), diterapkan di langkah 2 (precondition TC-FA-FAAL-143, 144, 145, 146) sehingga baris yang diasersi hanya baris seed #12 (halaman terakhir = halaman 2 dari 15 baris). State yang diubah: Filter Date Tab User Action, di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Parameter iterasi TC-FA-FAAL-144 (kolom teks; baris diidentifikasi lewat UA-xx):

  | Kolom | Klik 1 (Ascending) | Klik 2 (Descending) |
  |---|---|---|
  | Action | baris pertama sampai keempat: UA-10, UA-01, UA-07, UA-09 | dua baris pertama: UA-04 lalu UA-05 |
  | Object | empat baris pertama: UA-06, UA-03, UA-05, UA-04 | baris pertama: UA-10 |
  | Name | tiga baris pertama: UA-01, UA-07, UA-10 | baris pertama: UA-08 (`—`) |
  | Field | empat baris pertama: UA-01, UA-09, UA-03, UA-08 | baris pertama: UA-04 |
- Parameter iterasi TC-FA-FAAL-146 (kolom nilai):

  | Kolom | Klik 1: baris pertama | Klik 1: nilai `—` di akhir | Klik 2: baris pertama |
  |---|---|---|---|
  | Old Value | UA-08 (`7 days`) | UA-01, UA-07, UA-11, UA-15 | UA-01 (`—`) |
  | New Value | UA-08 (`14 days`) | UA-03, UA-09, UA-12 | UA-03 (`—`) |
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action
2. Klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-143: Sort kolom Date, siklus tiga tahap

3. Klik ikon sort header kolom Date sekali (Ascending)
4. Verifikasi Klik 1 (Oldest First): baris UA-15 di baris pertama
5. Klik ikon sort header kolom Date kedua kali (Descending)
6. Verifikasi Klik 2 (Newest First): baris UA-01 di baris pertama
7. Klik ikon sort header kolom Date ketiga kali
8. Verifikasi indikator sort kolom Date hilang
9. Verifikasi urutan kembali default: UA-01 lalu UA-02

### TC-FA-FAAL-144: Sort kolom Action, Object, Name, dan Field

Untuk setiap kolom pada tabel parameter TC-FA-FAAL-144 (langkah 10 sampai 15):

10. Klik ikon sort header kolom sekali
11. Verifikasi baris Klik 1 sesuai tabel parameter
12. Klik ikon sort header kolom kedua kali
13. Verifikasi baris Klik 2 sesuai tabel parameter
14. Klik ikon sort header kolom ketiga kali
15. Verifikasi urutan kembali default

### TC-FA-FAAL-145: Sort kolom Modified By berdasarkan nama lengkap

16. Klik ikon sort header kolom Modified By sekali (Ascending)
17. Verifikasi Klik 1 (A-Z menurut nama lengkap): baris UA-01 (`Admin A`) di baris pertama
18. Klik `Next` untuk pindah ke halaman terakhir
19. Verifikasi baris UA-11 (`System`) di baris terakhir
20. Klik `Prev` untuk kembali ke halaman 1
21. Klik ikon sort header kolom Modified By kedua kali (Descending)
22. Verifikasi Klik 2: baris UA-11 (`System`) di baris pertama
23. Verifikasi baris UA-13 dan UA-14 (`Hendra P`) menyusul sesudah baris UA-11
24. Klik ikon sort header kolom Modified By ketiga kali
25. Verifikasi urutan kembali default

### TC-FA-FAAL-146: Sort kolom Old Value dan New Value

Untuk setiap kolom pada tabel parameter TC-FA-FAAL-146 (langkah 26 sampai 34):

26. Klik ikon sort header kolom sekali (Ascending)
27. Verifikasi baris pertama Klik 1 sesuai tabel parameter
28. Klik `Next` untuk pindah ke halaman terakhir
29. Verifikasi nilai `—` di akhir sesuai tabel parameter
30. Klik `Prev` untuk kembali ke halaman 1
31. Klik ikon sort header kolom kedua kali (Descending)
32. Verifikasi baris pertama Klik 2 sesuai tabel parameter
33. Klik ikon sort header kolom ketiga kali
34. Verifikasi urutan kembali default

## Notes

- Langkah penghubung (S-03): klik tab User Action di awal; langkah 2 menerapkan Filter Date Jendela Seed Tab User Action sesuai precondition d TC-FA-FAAL-143 sampai 146; pada TC-FA-FAAL-145 dan 146 klik `Next` ke halaman terakhir dan `Prev` kembali ke halaman 1 supaya asersi "baris terakhir" dan "di akhir" diamati pada halaman terakhir (S-14) dan klik sort berikutnya dilakukan di halaman 1 (sort mempertahankan nomor halaman). Halaman terakhir = halaman 2 (15 baris, 10 per halaman).
- Langkah 10 sampai 15 (TC-FA-FAAL-144) dan langkah 26 sampai 34 (TC-FA-FAAL-146) diulang per kolom; parameter tiap iterasi ada di Prerequisites. Tiap kolom diasersi dengan `Verifikasi` per klausa Expected (S-01).
- Ukuran spec 34 langkah nominal (61 langkah setelah ekspansi iterasi), melewati sekitar 35 karena TC-FA-FAAL-144 dan 146 berupa iterasi per kolom dengan Expected per klausa. Seluruh blok satu kelas harness (fungsional, baca saja), satu dataset (Pre-setup #12), tanpa aksi tulis, dan tiap blok berdiri sendiri; spec tidak dipecah (konvensi bagian 3, batas ukuran).
- Temuan untuk QA:
  - TC-FA-FAAL-143 langkah 1 sampai 3 meminta mengamati indikator sort, tetapi Expected hanya menyebut urutan (klik 1 dan 2) dan indikator hilang (klik 3); spec tidak menambah asersi indikator pada klik 1 dan 2.
  - TC-FA-FAAL-145 butir a ("UA-11 di baris terakhir") dan TC-FA-FAAL-146 butir a dan b (nilai `—` "di akhir") tidak menyebut halaman; dengan 15 baris dan 10 per halaman, baris tersebut ada di halaman 2.
  - TC-FA-FAAL-144 butir c menulis baris pertama Klik 2 kolom Name sebagai UA-08 (`—`); spec membaca `—` sebagai nilai sel Name UA-08.
  - TC-FA-FAAL-143 sampai 146 memberi precondition Filter Date Jendela Seed Tab User Action (18/06/26 sampai 18/06/26) agar posisi baris dan halaman terakhir tidak bergantung pada baris log lain; spec menerapkannya di langkah 2 dan mengikuti TC.

