---
id: TC-FA-FAAL-E2E-037-filter-tab-user-action-date-dan-opsi
title: "Filter Tab User Action: Screening Panel, Date, serta Action, Object, dan Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-126
  - TC-FA-FAAL-127
  - TC-FA-FAAL-129
coverage:
  web: automated
---

# Filter Tab User Action: Screening Panel, Date, serta Action, Object, dan Field

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
- Sebelum TC-FA-FAAL-127 kolom Date diisi tanggal `18/06/26` dan `19/06/26`-`20/06/26` mengikuti format General Settings staf `dd/MM/yy`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAL-126: Screening Filter Panel Tab User Action

1. Klik tab User Action
2. Klik icon Filter
3. Verifikasi panel Filter tampil di bawah Toolbar
4. Verifikasi icon Filter berubah gelap
5. Verifikasi field berurutan dari kiri ke kanan sesuai urutan kolom tabel: `Date` (date range picker, `Select date`), `Action` (multi-select searchable, `All actions`), `Object` (multi-select searchable, `All objects`), `Field` (multi-select searchable, `All fields`), `Modified By` (multi-select searchable, `All users`)
6. Verifikasi kelima field tanpa nilai ter-pilih
7. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan
8. Verifikasi tidak ada field Name, Old Value, maupun New Value pada panel

### TC-FA-FAAL-127: Filter Date Tab User Action

9. Pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`
10. Verifikasi teks pagination `Showing 1–10 of 15 entries`
11. Klik `[Clear Field]`
12. Pilih tanggal mulai `19/06/26` dan tanggal akhir `20/06/26` pada field Date, klik `[Apply]`
13. Verifikasi state `No results found`

### TC-FA-FAAL-129: Filter Action, Object, dan Field menyaring baris

14. Klik `[Clear Field]`, klik `[Apply]`
15. Pilih Action `Assign`, klik `[Apply]`
16. Verifikasi baris UA-01 dan UA-07 tampil
17. Klik `[Clear Field]`, klik `[Apply]`
18. Pilih Object `Groups`, klik `[Apply]`
19. Verifikasi baris UA-02, UA-11, UA-13, UA-14, dan UA-15 tampil
20. Klik `[Clear Field]`, klik `[Apply]`
21. Pilih Field `Status`, klik `[Apply]`
22. Verifikasi baris UA-04, UA-05, UA-06, dan UA-10 tampil
23. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): klik tab User Action; `[Clear Field]` lalu `[Apply]` sebelum dan sesudah tiap blok filter; panel Filter dibuka satu kali pada TC-FA-FAAL-126 dan tetap terbuka untuk TC berikutnya, sehingga langkah "Klik icon Filter" pada TC-FA-FAAL-127 dan 129 tidak diulang; pada TC-FA-FAAL-129 pilihan dibuka dari panel yang sama.
- Tidak ada Post Condition TC pada blok ini.
- Temuan untuk QA:
  - TC-FA-FAAL-127 butir a menulis "seluruh 15 baris tampil" bersama `Showing 1–10 of 15 entries`, padahal Rows per page default 10; spec mengasersi teks pagination `Showing 1–10 of 15 entries`, bukan 15 baris pada satu halaman.
  - Total `15 entries` dan keberadaan hanya 15 baris pada TC bergantung pada log User Action client Pre-setup #12 yang tidak bertambah. Log immutable dan spec lain (Section 7 dan 9) menambah baris pada client yang sama, sehingga total absolut dapat berubah (S-12, S-14); TC tidak menyatakan client khusus atau Filter pembatas. Spec mengikuti angka TC.
  - TC tidak menyatakan apakah panel Filter tetap terbuka setelah `[Apply]` dan saat berpindah tab; spec mengasumsikan panel tetap terbuka (TC-FA-FAAL-129 mengulang `[Clear Field]` dan `[Apply]` tanpa membuka panel lagi).
