---
id: TC-FA-COA-E2E-103-absence-log-bulk-activate-dan-deactivate-seleksi-campuran
title: "Absence Log: Bulk Deactivate dan Bulk Activate Seleksi Campuran Tidak Menulis Log untuk Akun yang Dilewati"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-56
  - TC-FA-COA-350
coverage:
  web: automated
---

# Absence Log: Bulk Deactivate dan Bulk Activate Seleksi Campuran Tidak Menulis Log untuk Akun yang Dilewati

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence log). Pemicu adalah Bulk Deactivate dan Bulk Activate atas seleksi campuran yang berhasil diproses sebagian; pemicu hanya membentuk kondisi yang diasersi tidak tercatat untuk akun yang dilewati, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: empat akun milik spec ini, dibuat di hook `before` dan dihapus di hook `after` (kemampuan seed disediakan tim FE/BE; tidak memakai kunci fixture Pre-setup). Used By 0, belum pernah diekspor, Last Used in Journal kosong. Account Code literal `DID103A` sampai `DID103D` (batas 15 karakter sehingga tidak bersuffix `{runId}`; memuat nomor spec supaya unik per spec); Account Name bersuffix `{runId}-103`:

  | Code | Account Name | Function | Kondisi awal | Padanan Pre-setup TC | Peran | Dipakai |
  |---|---|---|---|---|---|---|
  | `DID103A` | `Mixed Deactivate {runId}-103` | Depreciation Expense | Active | P53 | Dinonaktifkan | TC-56 |
  | `DID103B` | `Mixed Skip {runId}-103` | Gain on Disposal | Inactive | P54 | Dilewati, tidak berubah | TC-56 |
  | `DID103C` | `Mixed Activate Skip {runId}-103` | Depreciation Expense | Active | P97 | Dilewati, tidak berubah | TC-350 |
  | `DID103D` | `Mixed Activate {runId}-103` | Gain on Disposal | Inactive | P98 | Diaktifkan | TC-350 |

- Pengecualian A-18 (S-06 dan S-12; butir "Pengecualian A-18" di `suite.md`): Account Code literal `DID103A` sampai `DID103D` tanpa suffix `{runId}` dan dipakai spec ini saja. `DID103A` dinonaktifkan dan `DID103D` diaktifkan; `DID103B` dan `DID103C` tidak berubah. Keempat akun dibuat di hook `before` dan dihapus di hook `after` spec ini (seed idempotent dan pembersihan disediakan tim FE/BE); suite berjalan serial. Akun Pre-setup P53, P54, P97, dan P98 tidak dipakai spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code. Baseline dicatat sebelum aksi pemicu tiap TC dan jumlah sesudah pemicu dibaca lewat kemampuan yang sama (S-12, bagian 8b butir 10).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pembersihan akun milik spec lewat API mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-56: Bulk Deactivate seleksi campuran tidak menulis log untuk akun Inactive yang dilewati

1. Ketik Search `DID103A`, tekan Enter
2. Centang akun `DID103A`
3. Ganti isi kotak search dengan `DID103B`, tekan Enter
4. Centang akun `DID103B`
5. Klik Bulk `Deactivate`
6. Verifikasi dialog berisi hanya `• DID103A – Depreciation Expense – Mixed Deactivate {runId}-103` (akun Inactive tidak tampil)
7. Catat baseline jumlah entri Account Code `DID103A` dan `DID103B` pada Changelog, System Log aktor, dan Activity Log dari server
8. Klik `[Deactivate]`
9. Verifikasi toast "Success, account has been deactivated."
10. Klik icon Changelog
11. Verifikasi jumlah entri `DID103A` pada Changelog bertambah satu dari baseline langkah 7
12. Verifikasi jumlah entri `DID103B` pada Changelog sama dengan baseline langkah 7
13. Tutup Modal Changelog
14. Buka System Log pada Detail User aktor
15. Verifikasi jumlah entri `DID103A` pada System Log aktor bertambah satu dari baseline langkah 7
16. Verifikasi jumlah entri `DID103B` pada System Log aktor sama dengan baseline langkah 7
17. Buka Activity Log FAMS
18. Verifikasi jumlah entri `DID103A` pada Activity Log bertambah satu dari baseline langkah 7
19. Verifikasi jumlah entri `DID103B` pada Activity Log sama dengan baseline langkah 7

### TC-FA-COA-350: Bulk Activate seleksi campuran tidak menulis log untuk akun Active yang dilewati

20. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
21. Ketik Search `DID103C`, tekan Enter
22. Centang akun `DID103C`
23. Ganti isi kotak search dengan `DID103D`, tekan Enter
24. Centang akun `DID103D`
25. Klik Bulk `Activate`
26. Verifikasi dialog berisi hanya `• DID103D – Gain on Disposal – Mixed Activate {runId}-103` (akun Active tidak tampil)
27. Catat baseline jumlah entri Account Code `DID103C` dan `DID103D` pada Changelog, System Log aktor, dan Activity Log dari server
28. Klik `[Activate]`
29. Verifikasi toast "Success, account has been activated."
30. Klik icon Changelog
31. Verifikasi jumlah entri `DID103D` pada Changelog bertambah satu dari baseline langkah 27
32. Verifikasi jumlah entri `DID103C` pada Changelog sama dengan baseline langkah 27
33. Tutup Modal Changelog
34. Buka System Log pada Detail User aktor
35. Verifikasi jumlah entri `DID103D` pada System Log aktor bertambah satu dari baseline langkah 27
36. Verifikasi jumlah entri `DID103C` pada System Log aktor sama dengan baseline langkah 27
37. Buka Activity Log FAMS
38. Verifikasi jumlah entri `DID103D` pada Activity Log bertambah satu dari baseline langkah 27
39. Verifikasi jumlah entri `DID103C` pada Activity Log sama dengan baseline langkah 27

## Notes

- `P-5`: spec absence (kelas g) memuat pemicu Bulk Deactivate dan Bulk Activate atas seleksi campuran (langkah 8 dan 28) yang hanya membentuk kondisi yang diasersi tidak tercatat untuk `DID103B` dan `DID103C`; tiap TC punya baseline sendiri (langkah 7 dan 27).
- Pembagian TC lintas spec (S-05): TC-FA-COA-56 ada di spec 029 (isi dialog, toast, dan status akun Inactive yang dilewati) dan di spec ini (klausa "Changelog, Activity Log, dan System Log tidak memuat baris untuk P54" beserta Langkah 4 TC; spec ini membacanya atas `DID103B`); TC-FA-COA-350 ada di spec 028 (Bulk Action Bar, dialog, toast, dan status P97 dan P98) dan di spec ini (klausa "Changelog, Activity Log, dan System Log tidak memuat baris untuk P97" beserta Langkah 4 TC; spec ini membacanya atas `DID103C`). Spec ini memuat aksi nyata yang sama dengan baseline sendiri per TC; spec 028 dan 029 tidak mengasersi log.
- `A-18`: akun milik spec `DID103A` (TC-FA-COA-56) dan `DID103D` (TC-FA-COA-350) menjadi target ubah status; `DID103B` dan `DID103C` dilewati dan tidak berubah. Syarat A-18 (Code literal satu spec saja, seed dan pembersihan di hook `before` dan `after`, suite serial) dinyatakan di `## Prerequisites`. Akun Pre-setup P53, P54, P97, dan P98 hanya dipakai spec 028 dan 029.
- Anchor absence (bagian 8b butir 2): toast sukses (langkah 9 dan 29) membuktikan respons server sudah diproses; pada tiap surface log, entri akun yang diproses bertambah satu dari baseline (langkah 11, 15, 18 untuk `DID103A`; langkah 31, 35, 38 untuk `DID103D`) menjadi anchor positif sebelum asersi jumlah entri akun yang dilewati sama dengan baseline (langkah 12, 16, 19 untuk `DID103B`; langkah 32, 36, 39 untuk `DID103C`). Ketiga surface disebut satu per satu. Post Condition TC-FA-COA-56 dan TC-FA-COA-350 ("log L-03 hanya untuk P53" dan "hanya untuk P98", dibaca atas `DID103A` dan `DID103D`) punya langkah observasi di Langkah 4 TC sehingga diasersi.
- Langkah penghubung (S-03, S-09, R-16, R-23): langkah 1, 3, 21, dan 23 (Search Account Code untuk menemukan baris target); langkah 13 dan 33 (menutup Modal Changelog); langkah 20 (kembali ke halaman Chart of Accounts sesudah membuka System Log dan Activity Log, S-14); langkah 7 dan 27 mencatat baseline sebelum aksi pemicu tiap TC dan bukan asersi. Pemilihan akun pada langkah 2, 4, 22, dan 24 adalah precondition TC.
- Asersi tambahan di luar Expected TC (S-03): langkah 6 dan 26 (isi dialog; Expected a TC-FA-COA-56 dan Expected b TC-FA-COA-350) menjadi anchor bahwa akun yang dilewati tidak ikut diproses; langkah 9 dan 29 (toast; Expected b TC-FA-COA-56 dan Expected d TC-FA-COA-350).
- Cara baca (S-14): spec mengasersi selisih jumlah entri per Account Code terhadap baseline, bukan isi baris teratas.
- Spec 39 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu kelas harness (absence log) dan berdiri sendiri; blok baca-log berpola (buka surface, Verifikasi jumlah entri akun yang diproses, Verifikasi jumlah entri akun yang dilewati; langkah 10 sampai 19 dan 30 sampai 39) tidak dihitung menurut bagian 3 prinsip 13, sisanya di bawah ambang.
- Temuan untuk QA:
  - TC-FA-COA-56 dan TC-FA-COA-350 menamai akun lewat Pre-setup bersama (P53, P54, P97, P98 dengan Code `5-6103`, `4-7103`, `5-6110`, `4-7110`), sedangkan spec ini memakai akun milik spec `DID103A` sampai `DID103D` dengan Account Name bersuffix `{runId}-103` (padanan, seperti spec 096, 097, dan 102) agar satu akun hanya dipakai satu spec (A-18). Akibatnya Expected a TC-FA-COA-56 (`• 5-6103 – Depreciation Expense – Mixed Deactivate`) dan Expected b TC-FA-COA-350 (`• 4-7110 – Gain on Disposal – Mixed Activate`) diverifikasi dengan Account Code dan Account Name akun milik spec; nilai literal TC berbeda.
  - TC-FA-COA-56 dan TC-FA-COA-350 Langkah 4 menyebut ketiga surface "di Detail User aktor" tanpa jalur menu; spec membuka Changelog lewat icon Changelog dan System Log serta Activity Log lewat penamaan TC-FA-COA-93 sampai 95 (System Log pada Detail User aktor dan Activity Log FAMS).
  - TC-FA-COA-56 dan TC-FA-COA-350 tidak menyebut cara membaca "tidak memuat baris"; spec membandingkan jumlah entri per Account Code terhadap baseline (S-12).
