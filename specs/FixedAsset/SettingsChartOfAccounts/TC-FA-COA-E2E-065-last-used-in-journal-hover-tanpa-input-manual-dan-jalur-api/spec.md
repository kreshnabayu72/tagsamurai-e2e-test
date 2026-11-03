---
id: TC-FA-COA-E2E-065-last-used-in-journal-hover-tanpa-input-manual-dan-jalur-api
title: "Last Used in Journal: Hover, Tanpa Input Manual, dan Jalur API"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-106
  - TC-FA-COA-117
  - TC-FA-COA-119
  - TC-FA-COA-120
coverage:
  web: automated
---

# Last Used in Journal: Hover, Tanpa Input Manual, dan Jalur API

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Akun Pre-setup (kunci fixture `Fixture.settingsChartOfAccounts.<kunci>` ditetapkan tim FE):

  | Akun | Account Code | Kondisi | Dipakai di |
  |---|---|---|---|
  | P1 | `5-6001` | Active, Last Used in Journal kosong | TC-119, TC-106 (hanya dibaca) |
  | P2 | `6-2001` | Active, Last Used in Journal `Aug 2026`; terekspor lewat jalur API J-06 pada 22/10/26, 09:15 oleh Rina Pratama (waktu dan nama pengekspor: asumsi pre-setup P2, bukan data PRD) | TC-106 (hanya dibaca) |
  | P112 | `5-6118` | Active, Last Used in Journal kosong, belum pernah diekspor, bukan nilai default company; Account Name `Depreciation Expense – Last Used Advance` | TC-117 (diubah; Last Used maju ke `Sep 2026`) |
  | P4 | `1-1002` | Inactive, Last Used in Journal `Mar 2025` | TC-120 (hanya dibaca) |

- General Settings: Date Format `dd/MM/yy` dan Time Format 24 jam (TC-106).
- Jalur API J-06 (ekspor Journal) belum ada (NC-04, modul Export Journal belum disusun); TC-106 (bagian ekspor nyata), TC-117, dan TC-120 bertanda `[DEFERRED]`. Kemampuan memicu permintaan langsung J-06 lewat sesi API aktor (suite.md, Sesi API aktor) dan akun P2 yang sudah terekspor disediakan tim FE/BE; tanpa endpoint karangan (S-13).
- Kemampuan teknis: membaca jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS lewat BE sebelum aksi (8b.10, S-12); disediakan tim FE/BE.
- State yang diubah spec: Last Used in Journal akun P112 maju ke `Sep 2026` dan audit trail bertambah permanen; pemulihan nilai P112 dan seed ulang disediakan tim FE/BE (S-06).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-119: Tanpa input manual Last Used in Journal

1. Klik `+ Account`
2. Verifikasi field Account Code tampil pada form Add Account
3. Verifikasi form Add Account tidak memuat field Last Used in Journal
4. Tutup modal Add Account dengan `✕`
5. Ketik Search `5-6001`, tekan Enter
6. Klik row action `Edit` pada baris akun P1
7. Verifikasi field Account Code tampil pada form Edit Account
8. Verifikasi form Edit Account tidak memuat field Last Used in Journal
9. Tutup modal Edit Account dengan `✕`

### TC-FA-COA-106: Hover sel Last Used in Journal

10. Arahkan kursor ke sel Last Used in Journal baris akun P1
11. Verifikasi sel baris P1 tampil `—`
12. Verifikasi sel baris P1 tidak memiliki hover
13. Ganti isi kotak search dengan `6-2001`, tekan Enter
14. Arahkan kursor ke sel Last Used in Journal baris akun P2
15. Verifikasi sel baris P2 tampil `Aug 2026`
16. Verifikasi hover sel baris P2 menampilkan "Last exported 22/10/26, 09:15 by Rina Pratama"
17. Klik `(←)` pada kotak Search

### TC-FA-COA-117: [DEFERRED] Ekspor periode lebih baru memajukan Last Used in Journal

18. Catat jumlah entri Changelog Chart of Accounts, System Log pada Detail User aktor, dan Activity Log FAMS sebagai baseline TC-117
19. Kirim permintaan langsung J-06 untuk periode Sep 2026 dengan akun P112 lewat sesi API aktor hingga ekspor tersimpan
20. Ketik Search `5-6118`, tekan Enter
21. Verifikasi kolom Last Used in Journal baris akun P112 tampil `Sep 2026`
22. Klik ikon Changelog di toolbar
23. Verifikasi jumlah entri Changelog bertambah satu dari baseline
24. Verifikasi entri teratas Changelog: Field Last Used in Journal, Old Value `—`, New Value `Sep 2026`, Modified By = user yang mengekspor
25. Tutup modal Changelog dengan ikon ✕
26. Buka System Log pada Detail User aktor
27. Verifikasi jumlah entri System Log bertambah satu dari baseline
28. Verifikasi entri teratas System Log: Field Last Used in Journal, Old Value `—`, New Value `Sep 2026`
29. Buka Activity Log FAMS
30. Verifikasi jumlah entri Activity Log bertambah satu dari baseline
31. Verifikasi entri teratas Activity Log: Field Last Used in Journal, Old Value `—`, New Value `Sep 2026`, Modified By = user yang mengekspor

### TC-FA-COA-120: [DEFERRED] Export ulang tanpa akun P4 tidak mengosongkan nilai tersimpan

32. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
33. Ketik Search `1-1002`, tekan Enter
34. Verifikasi kolom Last Used in Journal baris akun P4 tampil `Mar 2025`
35. Kirim permintaan langsung J-06 tanpa akun P4 lewat sesi API aktor hingga ekspor tersimpan
36. Muat ulang halaman
37. Ketik Search `1-1002`, tekan Enter
38. Verifikasi kolom Last Used in Journal baris akun P4 tetap `Mar 2025`

## Notes

- Alasan spec di atas sekitar 35 langkah (38 langkah): empat TC berdiri sendiri pada satu kolom (Last Used in Journal) dengan akun milik masing-masing, dan sebagian besar langkah adalah blok baca-log berpola di tiga surface (TC-117) serta Search untuk membuka baris target (8b.12).
- TC-117 dan TC-120 `[DEFERRED]` (NC-04, J-06 belum ada); TC-106 bagian ekspor nyata juga `[DEFERRED]` dan P2 sudah terekspor sebagai precondition. Spec tetap ditulis lengkap dan kebutuhan jalur J-06 ada di Prerequisites.
- Permintaan langsung pada langkah 19 dan 35 adalah pelaku kedua lewat sesi API (suite.md, Sesi API aktor) yang hanya memicu perubahan state; asersi memakai UI dan tiga surface log, bukan respons permintaan (8b.1).
- Cara baca entri baru (S-14): setelah selisih jumlah dari baseline dibuktikan, entri baru dibaca pada baris teratas urutan default Date Newest First.
- Langkah penghubung (S-03): langkah 4 dan 9 (menutup modal), langkah 5, 13, 20, 33, dan 37 (Search untuk menemukan baris target, R-16), langkah 17 (Search dikosongkan), langkah 32 (navigasi kembali ke modul asal setelah membaca log, S-14), langkah 36 (muat ulang halaman).
- Asersi "tidak ada pencatatan/log" tidak ada di spec ini (S-05); TC-120 tidak mengasersi ketiadaan log dan hanya nilai kolom P4.
- Temuan untuk QA:
  - TC-117 butir b mensyaratkan Modified By = user yang mengekspor (NC-06) tanpa menyebut akun pengekspor; spec memakai aktor sesi API (user yang memicu J-06). Atribut Modified By pada System Log tidak diasersi karena TC tidak menyebut kolomnya pada surface itu.
  - TC-106 menyebut Rina Pratama dan waktu ekspor 22/10/26, 09:15 sebagai asumsi pre-setup P2 yang bukan data PRD.
  - TC-120 tidak menyebut daftar akun yang dikirim pada permintaan J-06; spec menulis "tanpa akun P4".
  - TC-119 tidak menyebut cara membuka Edit Account selain "Buka Edit Account P1"; spec memakai row action `Edit` hasil Search.
