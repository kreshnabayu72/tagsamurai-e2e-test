---
id: TC-FA-COA-E2E-028-bulk-activate-seleksi-campuran-dan-collapse-single
title: "Bulk Activate: Seleksi, Campuran, dan Collapse Single"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-53
  - TC-FA-COA-54
  - TC-FA-COA-298
  - TC-FA-COA-350
coverage:
  web: automated
---

# Bulk Activate: Seleksi, Campuran, dan Collapse Single

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin` | Active, Used By 0; hanya dibaca | TC-54 |
  | P3 | `4-7001 – Gain on Disposal` | Inactive, Used By 0; hanya dibaca | TC-54, TC-298 |
  | P49 | `4-7102 – Gain on Disposal – Bulk Activate A` | Inactive, Used By 0; sekali pakai, diaktifkan | TC-53 |
  | P50 | `1-1102 – Equipment – Bulk Activate B` | Inactive, Used By 0; sekali pakai, diaktifkan | TC-53 |
  | P97 | `5-6110 – Depreciation Expense – Mixed Activate Skip` | Active, Used By 0; tidak berubah | TC-350 |
  | P98 | `4-7110 – Gain on Disposal – Mixed Activate` | Inactive, Used By 0; sekali pakai, diaktifkan | TC-350 |

- Pengecualian A-18 (butir "Data bersama" di `suite.md`): akun sekali pakai P49, P50, dan P98 diaktifkan spec ini. Seed idempotent dan pemulihan ke kondisi awal (termasuk status dan Last Updated) dijalankan fixture backend (disediakan tim FE/BE) di hook `before` dan `after` spec ini; suite berjalan serial. P1, P3, dan P97 hanya dibaca atau tidak berubah.
- P97 dan P98 hanya dipakai spec ini; kondisi awal: P97 Active dan P98 Inactive, Used By 0. Fixture memulihkan keduanya ke kondisi awal itu di hook `before` dan `after` spec ini.
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-54: Seleksi campuran menampilkan Activate dan Deactivate; seleksi semua Active hanya Deactivate

1. Ketik Search `5-6001`, tekan Enter
2. Centang akun P1 (`5-6001`)
3. Verifikasi Bulk Action Bar memuat `Deactivate` dan `Delete`, tanpa `Activate`
4. Ganti isi kotak search dengan `4-7001`, tekan Enter
5. Centang akun P3 (`4-7001`)
6. Verifikasi Bulk Action Bar memuat `Activate`, `Deactivate`, dan `Delete`

### TC-FA-COA-298: Bulk Activate tepat satu akun collapse ke dialog single D-14

7. Muat ulang halaman (F5)
8. Ganti isi kotak search dengan `4-7001`, tekan Enter
9. Centang akun P3
10. Klik Bulk `Activate`
11. Verifikasi dialog "Activate Account" (single, D-14), bukan "Activate Accounts"
12. Verifikasi bullet `• 4-7001 – Gain on Disposal`
13. Klik `[Cancel]`

### TC-FA-COA-53: Bulk Activate pada seleksi semua Inactive memproses seluruh akun terpilih

14. Muat ulang halaman (F5)
15. Ganti isi kotak search dengan `4-7102`, tekan Enter
16. Centang akun P49 (`4-7102`)
17. Ganti isi kotak search dengan `1-1102`, tekan Enter
18. Centang akun P50 (`1-1102`)
19. Verifikasi Bulk Action Bar memuat `Activate` dan `Delete`
20. Verifikasi `Deactivate` Hidden pada Bulk Action Bar
21. Klik Bulk `Activate`
22. Verifikasi dialog "Activate Accounts" dengan bullet `• 4-7102 – Gain on Disposal – Bulk Activate A` dan `• 1-1102 – Equipment – Bulk Activate B` serta teks "Are you sure you want to activate them?"
23. Klik `[Activate]` pada dialog D-15
24. Verifikasi toast "Success, account has been activated."
25. Verifikasi akun P50 Active
26. Ganti isi kotak search dengan `4-7102`, tekan Enter
27. Verifikasi akun P49 Active
28. Verifikasi seleksi di-reset
29. Verifikasi Bulk Action Bar tidak tampil

### TC-FA-COA-350: Bulk Activate pada seleksi campuran hanya memproses akun Inactive

30. Ganti isi kotak search dengan `5-6110`, tekan Enter
31. Centang akun P97 (`5-6110`)
32. Ganti isi kotak search dengan `4-7110`, tekan Enter
33. Centang akun P98 (`4-7110`)
34. Verifikasi Bulk Action Bar memuat `Activate`, `Deactivate`, dan `Delete`
35. Klik Bulk `Activate`
36. Verifikasi dialog berisi hanya `• 4-7110 – Gain on Disposal – Mixed Activate` (akun Active tidak tampil)
37. Verifikasi dialog berjudul "Activate Account" (versi single D-14)
38. Tunggu toast lama hilang otomatis
39. Klik `[Activate]`
40. Verifikasi toast "Success, account has been activated."
41. Verifikasi akun P98 menjadi Active
42. Ganti isi kotak search dengan `5-6110`, tekan Enter
43. Verifikasi akun P97 tetap Active

## Notes

- Spec 43 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik aksi (Bulk Activate) dengan akun sekali pakai milik blok masing-masing; langkah Search dan Centang berulang per akun karena tabel berhalaman banyak; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; "Muat ulang halaman (F5)" (langkah 7, 14) membersihkan seleksi sebelum blok berikutnya (S-09), sedangkan Search tetap terisi sehingga langkah 8 dan 15 mengganti isi kotak search (bagian 8b butir 9); `[Cancel]` pada langkah 13 menutup dialog TC-298; "Tunggu toast lama hilang otomatis" (langkah 38) karena teks toast sama dengan TC-53.
- Urutan Expected TC-53 diubah menurut state sementara (8b.5): isi Bulk Action Bar (langkah 19, 20) diasersi sebelum Bulk `Activate` dibuka karena bar tertutup dialog sesudahnya.
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- `A-18`: P49 dan P50 (TC-53) dan P98 (TC-350) menjadi target ubah status sekali pakai; syarat A-18 dinyatakan di `## Prerequisites`. P97 dan P98 hanya dipakai spec ini.
- Pembagian TC lintas spec (S-05): TC-350 ada di spec ini dan di spec 103 (absence log). Spec ini mengasersi isi Bulk Action Bar, dialog, toast, status P98, dan status P97 (langkah 34 sampai 43); klausa "Changelog, Activity Log, dan System Log tidak memuat baris untuk P97" beserta Langkah 4 TC (membuka ketiga surface log) diasersi di spec 103 dengan akun milik spec 103 dan baseline sendiri.
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan (langkah 4 sampai 6, 17 sampai 20, 30 sampai 34).
  - Post Condition TC-53 (log L-03 per akun per surface) dan TC-298 (data tidak berubah) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `4-7102` dan `5-6110` sudah memakai sebagian dari 15 karakter Account Code dan data Pre-setup di-seed tim FE/BE.
