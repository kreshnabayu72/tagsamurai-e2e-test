---
id: TC-FA-COA-E2E-031-blokir-deactivate-akun-dipakai-asset-class
title: "Blokir Deactivate: Akun Dipakai Asset Class"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-125
  - TC-FA-COA-126
  - TC-FA-COA-127
  - TC-FA-COA-128
  - TC-FA-COA-156
coverage:
  web: automated
---

# Blokir Deactivate: Akun Dipakai Asset Class

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1 (Asset Class `Office Equipment`); hanya dibaca, tidak berubah | TC-125, TC-127, TC-128 |
  | P7 | `4-7002 – Gain and Loss on Disposal` | Active, Used By 2 (Asset Class `Delivery Vehicles` dan `Heavy Equipment`); hanya dibaca, tidak berubah | TC-126, TC-127 |
  | P13 | `5-6850 – Depreciation Expense – Legacy` | Active, Used By 1 (Asset Class `Legacy Machinery` berstatus Inactive); hanya dibaca, tidak berubah | TC-156 |
  | P9 | `CAP-6200 – Capitalization Clearing – Overhead` | Active, Used By 0; sekali pakai, dinonaktifkan | TC-128 |

- Pengecualian A-18 (butir "Data bersama" di `suite.md`): akun sekali pakai P9 dinonaktifkan spec ini dan dipakai spec ini saja. Seed idempotent dan pemulihan ke kondisi awal (termasuk status dan Last Updated) dijalankan fixture backend (disediakan tim FE/BE) di hook `before` dan `after` spec ini; suite berjalan serial. P6, P7, dan P13 hanya dibaca dan tidak berubah.
- Asset Class pemakai P6, P7, dan P13 (termasuk `Legacy Machinery` berstatus Inactive) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-125: Deactivate akun yang dipakai satu Asset Class ditolak dengan dialog blok D-04

1. Ketik Search `5-6002`, tekan Enter
2. Klik switch Status pada akun P6 (`5-6002`)
3. Verifikasi dialog "Cannot Deactivate Account" dengan bullet `• 5-6002 – Depreciation Expense – Warehouse` dan teks "This account is used by 1 Asset Class and cannot be deactivated."
4. Verifikasi tombol `[OK]`
5. Klik `[OK]`
6. Verifikasi switch Status P6 tetap Active

### TC-FA-COA-126: Deactivate akun yang dipakai dua Asset Class menampilkan bentuk jamak D-04

7. Ganti isi kotak search dengan `4-7002`, tekan Enter
8. Klik switch Status pada akun P7 (`4-7002`)
9. Verifikasi dialog "Cannot Deactivate Account" dengan bullet `• 4-7002 – Gain and Loss on Disposal` dan teks "This account is used by 2 Asset Classes and cannot be deactivated."
10. Klik `[OK]`
11. Verifikasi switch Status P7 tetap Active

### TC-FA-COA-156: Used By menghitung Asset Class berstatus Inactive sehingga Deactivate ditolak dengan D-04

12. Ganti isi kotak search dengan `5-6850`, tekan Enter
13. Verifikasi nilai Used By P13 adalah `1`
14. Klik angka `1` di kolom Used By P13
15. Verifikasi popup "Used By" memuat teks polos satu baris `5-6850 – Depreciation Expense – Legacy (1)` di bawah judul
16. Verifikasi popup memuat bullet dengan nama Asset Class `Legacy Machinery`
17. Klik `[✕]` pada popup Used By
18. Klik switch Status pada akun P13 (`5-6850`)
19. Verifikasi dialog "Cannot Deactivate Account" dengan bullet `• 5-6850 – Depreciation Expense – Legacy` dan teks "This account is used by 1 Asset Class and cannot be deactivated."
20. Klik `[OK]`
21. Verifikasi switch Status P13 tetap Active

### TC-FA-COA-127: Bulk Deactivate seluruh akun terpilih terblokir menampilkan D-04 bentuk jamak tanpa perubahan

22. Ganti isi kotak search dengan `5-6002`, tekan Enter
23. Centang akun P6 (`5-6002`)
24. Ganti isi kotak search dengan `4-7002`, tekan Enter
25. Centang akun P7 (`4-7002`)
26. Klik Bulk `Deactivate`
27. Verifikasi dialog "Cannot Deactivate Accounts" dengan bullet beranotasi `• 5-6002 – Depreciation Expense – Warehouse (still in use)` dan `• 4-7002 – Gain and Loss on Disposal (still in use)`
28. Verifikasi teks "These accounts are in use and cannot be deactivated."
29. Verifikasi tombol `[OK]`
30. Klik `[OK]`
31. Verifikasi seleksi P6 dan P7 dipertahankan
32. Verifikasi Bulk Action Bar tetap tampil

### TC-FA-COA-128: Bulk Deactivate campuran: akun eligible dinonaktifkan dan akun yang dipakai Asset Class dilewati dengan D-03

33. Hapus centang akun P7
34. Ganti isi kotak search dengan `CAP-6200`, tekan Enter
35. Centang akun P9 (`CAP-6200`)
36. Klik Bulk `Deactivate`
37. Verifikasi dialog "Deactivate Accounts" dengan "The following will be deactivated:" memuat `• CAP-6200 – Capitalization Clearing – Overhead`
38. Verifikasi "The following are still in use and will be skipped:" memuat `• 5-6002 – Depreciation Expense – Warehouse (still in use)`
39. Verifikasi teks "Are you sure you want to continue?" dengan tombol `[Cancel]` dan `[Continue]`
40. Klik `[Continue]`
41. Verifikasi toast "Success, account has been deactivated. Some items were skipped (still in use)."
42. Verifikasi seleksi di-reset
43. Verifikasi Bulk Action Bar tidak tampil

## Notes

- Spec 43 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik (blokir Deactivate karena Used By) dengan fixture berbeda per blok; langkah Search dan Centang berulang per akun karena tabel berhalaman banyak; aksi yang mengubah data (TC-128) di akhir spec.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; `[OK]` (langkah 5, 10, 20) menutup dialog blok sebelum asersi switch; `[✕]` popup (langkah 17); hapus centang P7 (langkah 33) agar seleksi TC-128 berisi P9 dan P6.
- Urutan blok: TC-156 sebelum TC-127 dan TC-128 (berbeda dari urutan `sourceTc`). Alasan: TC-156 menguji satu akun (P13) dengan dialog blok single seperti TC-125 dan TC-126 sehingga variasi topik yang sama berurutan (prinsip 4), sedangkan TC-127 dan TC-128 memakai seleksi bulk dan TC-128 mengubah data sehingga diletakkan di akhir spec (S-10).
- `A-18`: P9 (TC-128) menjadi target ubah status sekali pakai; syarat A-18 dinyatakan di `## Prerequisites`.
- Langkah "Centang P9 dan P6" TC-128: P6 sudah tercentang dari TC-127 (seleksi dipertahankan setelah `[OK]`, Expected TC-127 butir d), sehingga hanya P9 yang dicentang.
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - TC-125 dan TC-126 tidak memberi langkah menutup dialog blok; spec menambah `[OK]` sebagai langkah penghubung agar switch dapat diasersi.
  - Post Condition TC-125, TC-127, TC-128, TC-156 (status akun, tidak ada log, log L-03 P9) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-6200` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
