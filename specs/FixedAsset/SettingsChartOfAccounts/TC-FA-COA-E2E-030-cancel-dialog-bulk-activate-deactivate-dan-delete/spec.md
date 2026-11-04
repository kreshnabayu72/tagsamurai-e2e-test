---
id: TC-FA-COA-E2E-030-cancel-dialog-bulk-activate-deactivate-dan-delete
title: "Cancel Dialog Bulk Activate, Deactivate, dan Delete"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-293
  - TC-FA-COA-294
  - TC-FA-COA-296
coverage:
  web: automated
---

# Cancel Dialog Bulk Activate, Deactivate, dan Delete

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, seluruhnya hanya dibaca (Cancel tidak mengubah data; identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P3 | `4-7001 – Gain on Disposal` | Inactive, Used By 0 | TC-293 |
  | P4 | `1-1002 – Equipment – Legacy Code` | Inactive, Used By 0 | TC-293 |
  | P1 | `5-6001 – Depreciation Expense – Admin` | Active, Used By 0, belum pernah diekspor | TC-294, TC-296 |
  | P5 | `CAP-6100 – Capitalization Clearing – Repairs` | Active, Used By 0, belum pernah diekspor | TC-294, TC-296 |

- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-293: Cancel pada dialog Bulk Activate (D-15) mempertahankan seleksi dan data

1. Ketik Search `4-7001`, tekan Enter
2. Centang akun P3 (`4-7001`)
3. Ganti isi kotak search dengan `1-1002`, tekan Enter
4. Centang akun P4 (`1-1002`)
5. Klik Bulk `Activate`
6. Klik `[Cancel]` pada dialog D-15
7. Verifikasi dialog "Activate Accounts" tertutup
8. Verifikasi tidak ada toast
9. Verifikasi akun P4 tetap Inactive
10. Ganti isi kotak search dengan `4-7001`, tekan Enter
11. Verifikasi akun P3 tetap Inactive
12. Verifikasi seleksi tetap dipertahankan
13. Verifikasi Bulk Action Bar tetap tampil

### TC-FA-COA-294: Cancel pada dialog Bulk Deactivate semua lolos (D-02) mempertahankan seleksi dan data

14. Muat ulang halaman (F5)
15. Ganti isi kotak search dengan `5-6001`, tekan Enter
16. Centang akun P1 (`5-6001`)
17. Ganti isi kotak search dengan `CAP-6100`, tekan Enter
18. Centang akun P5 (`CAP-6100`)
19. Klik Bulk `Deactivate`
20. Klik `[Cancel]` pada dialog D-02
21. Verifikasi dialog "Deactivate Accounts" tertutup
22. Verifikasi tidak ada toast
23. Verifikasi akun P5 tetap Active
24. Ganti isi kotak search dengan `5-6001`, tekan Enter
25. Verifikasi akun P1 tetap Active
26. Verifikasi seleksi tetap dipertahankan
27. Verifikasi Bulk Action Bar tetap tampil

### TC-FA-COA-296: Cancel pada dialog Bulk Delete semua lolos (D-08) mempertahankan seleksi dan data

28. Klik Bulk `Delete`
29. Klik `[Cancel]` pada dialog D-08
30. Verifikasi dialog "Delete Accounts" tertutup
31. Verifikasi tidak ada toast
32. Verifikasi akun P1 tetap ada di tabel
33. Ganti isi kotak search dengan `CAP-6100`, tekan Enter
34. Verifikasi akun P5 tetap ada di tabel
35. Verifikasi seleksi tetap dipertahankan
36. Verifikasi Bulk Action Bar tetap tampil

## Notes
- Spec 36 langkah, di atas ambang 35 langkah. Alasan: tiga TC Cancel dialog bulk (Activate, Deactivate, Delete) satu topik aksi tanpa perubahan data; TC-296 memakai ulang seleksi TC-294 sehingga tidak mengulang Search dan Centang; tiap klausa seleksi dan Bulk Action Bar diasersi dalam langkah sendiri (S-01).

- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; "Muat ulang halaman (F5)" (langkah 14) membersihkan seleksi sebelum TC berikutnya (S-09), sedangkan Search tetap terisi sehingga langkah 15 mengganti isi kotak search (bagian 8b butir 9).
- Langkah "Centang P1 dan P5" TC-296 sudah terpenuhi oleh seleksi TC-294 yang dipertahankan setelah `[Cancel]` (Expected TC-294 butir c); karena itu TC-296 dimulai dari Bulk `Delete`. Keduanya memakai akun P1 dan P5 yang sama.
- Asersi tidak ada toast ditaruh segera setelah dialog tertutup, sebelum asersi data (8b.11); urutan Expected TC berubah untuk itu.
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition "tidak ada log" ketiga TC tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-6100` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
