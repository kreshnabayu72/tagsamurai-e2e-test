---
id: TC-FA-COA-E2E-073-multi-konteks-edit-serentak-kunci-berubah-dan-last-write-wins
title: "Multi-Konteks: Edit Akun saat Kunci Berubah oleh Sesi Lain dan Edit Serentak Dua Sesi (Last-Write-Wins)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-43
  - TC-FA-COA-44
  - TC-FA-COA-45
coverage:
  web: automated
---

# Multi-Konteks: Edit Akun saat Kunci Berubah oleh Sesi Lain dan Edit Serentak Dua Sesi (Last-Write-Wins)

## Prerequisites

- Mode: FE+BE (backend nyata; tanpa intercept).
- Akun aktor sesi A: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun sesi B (hanya TC-FA-COA-45, konteks browser kedua yang hasilnya diasersi): Default User `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_DU_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Default User adalah Total Control permanen (asumsi Pre-setup TC, lihat Temuan untuk QA). Login sesi B ditulis sebagai langkah eksplisit (S-07).
- Sesi API aktor: pelaku kedua pada TC-FA-COA-43 dan TC-FA-COA-44 memakai sesi API sesuai butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan lewat API: mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; jalur ekspor Journal J-06 (pemicu Last Used in Journal) disediakan tim FE/BE tanpa endpoint karangan.
- Flag Guided Tooltip halaman Chart of Accounts: di-set true oleh hook `before` suite (lihat `suite.md`).
- Data Pre-setup (akun Pre-setup sekali pakai, identitas di `Fixture.settingsChartOfAccounts.<kunci>` yang disediakan tim FE; nama kunci ditetapkan tim FE):

  | Akun | Code dan Name | State awal | TC |
  |---|---|---|---|
  | P69 (`Fixture.settingsChartOfAccounts.p69`) | `5-6201` · `Depreciation Expense – Lock Race` · Function Depreciation Expense | Active, Used By 0, Last Used in Journal kosong | TC-FA-COA-43 |
  | P70 (`Fixture.settingsChartOfAccounts.p70`) | `5-6202` · `Depreciation Expense – Lock Race Same Value` · Function Depreciation Expense | Active, Used By 0, Last Used in Journal kosong | TC-FA-COA-44 |
  | P111 (`Fixture.settingsChartOfAccounts.p111`) | `5-6117` · `Depreciation Expense – Concurrent Edit` · Function Depreciation Expense | Active, Used By 0, Last Used in Journal kosong, belum pernah diekspor, bukan nilai default company | TC-FA-COA-45 |

- Efek pada Pre-setup (S-06): P70 berganti Name menjadi `Depreciation Expense – Lock Race HQ` dan Last Used in Journal terisi; P111 berganti Name dua kali dan dipulihkan ke Name awal oleh langkah 30; P69 terisi Last Used in Journal (Code tidak tersimpan berubah; `5-6010` pada langkah 4 adalah nilai input yang ditolak server). Last Updated ketiganya berubah.
- Pengecualian A-18 (lihat butir "Pengecualian A-18" di `suite.md`): P69, P70, dan P111 adalah akun Pre-setup sekali pakai yang menjadi target Edit. Seed idempotent dan pemulihan ketiga akun ke state awal (Code, Name, Last Used in Journal kosong, belum pernah diekspor) dijalankan di hook `before` dan `after` spec ini (disediakan tim FE/BE); satu akun dan satu Account Code literal (`5-6201`, `5-6202`, `5-6117`) hanya dipakai spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): ekspor akun lewat jalur API J-06; membaca jumlah entri log L-02 atas satu akun dan isinya; membaca Account Name tersimpan dari BE; memulihkan Account Name akun lewat sesi API. Jam server dan jam browser sinkron untuk nilai bulan-tahun ekspor.
- Nilai literal `A` dan `B` pada TC-FA-COA-45 adalah nama satu karakter (S-12): P111 adalah akun Pre-setup sehingga tidak dibuat atau dihapus spec, dan Name-nya dipulihkan oleh langkah 30 serta hook `before` dan `after` (A-18).
- Suite berjalan serial (`parallel: false`): spec mengubah akun Pre-setup bersama dan memakai dua sesi pada akun yang sama.
- Env var yang dipakai: `FA_TC_PASSWORD` dan `FA_DU_PASSWORD` (keduanya terdaftar di `spectra.config.ts` dan `.env.example`).

## Test Steps

### TC-FA-COA-43: Save ditolak D-16 bila kunci berubah sejak form dibuka dan submit mengubah field terkunci

1. Ketik Search `Fixture.settingsChartOfAccounts.p69.code`, tekan Enter
2. Sesi A: klik row action `Edit` pada akun P69 (`Fixture.settingsChartOfAccounts.p69.code`)
3. Ekspor P69 melalui jalur API J-06 lewat sesi API hingga Last Used in Journal P69 tersimpan
4. Sesi A: ubah Account Code P69 menjadi `5-6010`
5. Sesi A: klik `[Save]`
6. Verifikasi dialog blok `Cannot Save Account` dengan bullet `• Fixture.settingsChartOfAccounts.p69.code – Fixture.settingsChartOfAccounts.p69.name` dan teks "This account has been locked for editing by another action. The form has been reloaded with the latest lock status."
7. Verifikasi tombol `[OK]` tampil pada dialog
8. Klik `[OK]`
9. Verifikasi form memuat ulang: Account Code kembali `Fixture.settingsChartOfAccounts.p69.code`
10. Arahkan kursor ke field Account Code
11. Verifikasi Account Code Disabled dengan tooltip "Account Code can't be changed because this account was used in a journal in [Month Year]. Create a new account if needed." dengan [Month Year] = bulan dan tahun ekspor pada langkah 3 (format `Mon YYYY`)
12. Klik `✕` pada modal Edit Account

### TC-FA-COA-44: Kunci berubah sejak form dibuka tetapi nilai field terkunci sama dengan nilai tersimpan: Save berhasil

13. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p70.code`, tekan Enter
14. Sesi A: klik row action `Edit` pada akun P70 (`Fixture.settingsChartOfAccounts.p70.code`)
15. Ekspor P70 melalui jalur API J-06 lewat sesi API hingga Last Used in Journal P70 tersimpan
16. Sesi A: ubah Account Name P70 menjadi `Depreciation Expense – Lock Race HQ`
17. Sesi A: klik `[Save]`
18. Verifikasi toast "Success, account has been updated." tampil
19. Verifikasi modal Edit Account tertutup
20. Verifikasi kolom Last Used in Journal pada baris P70 tampil bulan dan tahun ekspor pada langkah 15 (format `Mon YYYY`, TC menulis `Oct 2026`)

### TC-FA-COA-45: Dua admin menyimpan Edit akun yang sama hampir bersamaan: last-write-wins, keduanya dicatat

21. Ganti akun: buka konteks browser kedua (sesi B), login sebagai Default User `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_DU_PASSWORD`, lalu buka Fixed Asset > Settings > Accounting > Chart of Accounts
22. Sesi A: ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p111.code`, tekan Enter; sesi B: ketik Search `Fixture.settingsChartOfAccounts.p111.code`, tekan Enter
23. Sesi A dan sesi B masing-masing klik row action `Edit` pada akun P111 (`Fixture.settingsChartOfAccounts.p111.code`)
24. Catat baseline jumlah entri log L-02 atas P111 (kemampuan baca disediakan tim FE/BE)
25. Sesi A: ubah Account Name P111 menjadi `A`; sesi B: ubah Account Name P111 menjadi `B`
26. Klik `[Save]` di sesi A lalu segera di sesi B (hampir bersamaan)
27. Tunggu aksi selesai
28. Verifikasi Account Name P111 yang tersimpan (dibaca dari BE) sama dengan Account Name pada Save yang tercatat paling akhir di log L-02 P111 (`A` atau `B`)
29. Verifikasi jumlah entri log L-02 atas P111 bertambah 2 dibanding baseline langkah 24 (satu entri per Save yang berhasil)
30. Pulihkan Account Name P111 ke `Fixture.settingsChartOfAccounts.p111.name` lewat sesi API hingga tersimpan
31. Tutup konteks browser sesi B dan hapus sesi login browser sesi B

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Tiga blok berdiri sendiri, satu kelas harness (konflik dua sesi atas akun yang sama); jumlah langkah 31, di bawah sekitar 35.
- Pelaku kedua pada TC-FA-COA-43 dan 44 adalah sesi API yang hanya memicu perubahan state (ekspor J-06), bukan konteks kedua; sesi UI kedua dipakai hanya pada TC-FA-COA-45 karena hasil Save sesi B ikut diasersi.
- Langkah penghubung (S-03, S-09): langkah 1, 13, dan 22 (Search untuk menemukan akun target, R-16, butir 8b.13); langkah 12 (menutup modal Edit setelah form dimuat ulang, form tidak dirty); langkah 27 (tunggu aksi selesai sebelum membaca log, butir 8b.8); langkah 30 (memulihkan Name P111, S-09); langkah 31 (menutup konteks kedua, S-09); langkah 21 (ganti akun eksplisit untuk sesi B, S-07). Search tidak dikosongkan di akhir karena hook `beforeEach` suite membuka layar awal ulang.
- `A-18`: TC-FA-COA-43, 44, dan 45 memakai akun Pre-setup sekali pakai P69, P70, dan P111 sebagai target Edit dengan Account Code literal `5-6201`, `5-6202`, dan `5-6117`; pemulihan di hook `before` dan `after`. Code tujuan `5-6010` pada TC-FA-COA-43 adalah input yang ditolak server dan tidak tersimpan; spec 064 memakai kode yang sama sebagai tujuan Edit atas akunnya sendiri dan memulihkannya sendiri.
- Asersi absence: tidak ada pada spec ini. Post Condition "tidak ada field tersimpan dan tidak ada log" TC-FA-COA-43 tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
- Temuan untuk QA:
  - TC-FA-COA-43 tidak punya langkah `[OK]` sebelum Expected c (form memuat ulang); spec menambah langkah 8 sebagai penghubung. TC tidak memberi teks tooltip ("tooltip terkunci"); spec memakai teks tooltip Account Code dari TC-FA-COA-35 (R-14).
  - TC-FA-COA-43 Post Condition "tidak ada field tersimpan dan tidak ada log" tidak punya langkah observasi, tidak diasersi.
  - TC-FA-COA-44 Expected c menulis "Tabel disegarkan" tanpa metode observasi; spec hanya mengasersi nilai kolom Last Used in Journal. Nilai `Oct 2026` pada TC bergantung bulan eksekusi; spec mengasersi bulan-tahun ekspor (format `Mon YYYY`). Kolom Last Used in Journal tampil secara default (TC-FA-COA-1 butir d), sehingga spec tidak menambah langkah Setup Column.
  - TC-FA-COA-45 Expected a ("nilai yang tersimpan terakhir") tidak mendefinisikan cara menentukan Save terakhir; spec memakai entri log L-02 terakhir lewat kemampuan baca yang disediakan tim FE/BE sebagai asumsi. Expected b ("tercatat sendiri di log") tidak menyebut surface log dan jumlahnya; spec mengasumsikan satu entri L-02 per Save (hanya Name yang berubah) sehingga selisih 2.
  - TC-FA-COA-45 tidak menyatakan keadaan modal Edit di kedua sesi sesudah Save; spec tidak mengasersinya dan mengandalkan penutupan modal pada Save sukses (pola TC-FA-COA-44).
  - TC-FA-COA-45 memakai Default User untuk sesi B sebagai asumsi: dua sesi web dengan akun Total Control yang sama dapat terkena batas satu sesi web dan TC tidak menyatakan perilakunya. Email dan password Default User bukan data PRD (Pre-setup TC menyebutnya asumsi).
  - TC-FA-COA-43, 44, 45 tidak menyebut kolom yang dicari Search; spec mencari berdasarkan Account Code.
