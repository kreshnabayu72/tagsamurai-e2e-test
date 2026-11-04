---
id: TC-FA-COA-E2E-039-delete-single-dan-bulk-delete-berhasil
title: "Delete Single dan Bulk Delete Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-61
  - TC-FA-COA-62
  - TC-FA-COA-63
  - TC-FA-COA-67
  - TC-FA-COA-68
  - TC-FA-COA-284
coverage:
  web: automated
---

# Delete Single dan Bulk Delete Berhasil

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.p<N>`: `.code` Account Code dan `.name` Account Name; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P3 | `4-7001 – Gain on Disposal` | Inactive, Last Used in Journal kosong; hanya dibaca (dialog dibatalkan) | TC-61, TC-63 |
  | P5 | `CAP-6100 – Capitalization Clearing – Repairs` | Active, eligible; hanya dibaca (dialog dibatalkan) | TC-67 |
  | P55 | `CAP-8102 – Capitalization Clearing – Single Delete` | Active, Used By 0, belum pernah diekspor, bukan nilai default company; sekali pakai, dihapus | TC-62 |
  | P83 | `CAP-8213 – Capitalization Clearing – Double Delete` | Active, Used By 0, belum pernah diekspor, bukan nilai default company; sekali pakai, dihapus | TC-284 |
  | P58 | `4-7104 – Gain on Disposal – Bulk Delete A` | Inactive, eligible; sekali pakai, dihapus | TC-68 |
  | P59 | `CAP-8105 – Capitalization Clearing – Bulk Delete B` | Active, eligible; sekali pakai, dihapus | TC-68 |

- Pengecualian A-18 (S-06 dan S-12; butir "Pengecualian A-18" di `suite.md`): akun sekali pakai P55, P83, P58, dan P59 menjadi target hapus dengan Account Code literal tanpa suffix `{runId}`. Seed idempotent dan pemulihan ke keadaan awal dijalankan di hook `before` dan `after` spec ini (kemampuan disediakan tim FE/BE).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-61: Dialog konfirmasi Delete single untuk akun yang lolos guard

1. Ketik Search `Fixture.settingsChartOfAccounts.p3.code`, tekan Enter
2. Klik row action `Delete` pada akun P3 (`Fixture.settingsChartOfAccounts.p3.code`) sehingga dialog D-07 terbuka
3. Verifikasi dialog "Delete Account" dengan bullet `• Fixture.settingsChartOfAccounts.p3.code – Fixture.settingsChartOfAccounts.p3.name`
4. Verifikasi teks "This action cannot be undone. Are you sure you want to delete it?"
5. Verifikasi tombol `[Cancel]` dan `[Delete]` (severity danger)

### TC-FA-COA-63: Cancel pada dialog Delete single mempertahankan akun

6. Klik `[Cancel]`
7. Verifikasi dialog tertutup
8. Verifikasi akun P3 tetap di tabel tanpa perubahan

### TC-FA-COA-67: Bulk Delete satu akun collapse ke dialog single D-07

9. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p5.code`, tekan Enter
10. Centang akun P5 (`Fixture.settingsChartOfAccounts.p5.code`)
11. Klik Bulk `Delete`
12. Verifikasi dialog "Delete Account" (single, D-07), bukan "Delete Accounts"
13. Klik `[Cancel]`
14. Hapus centang akun P5

### TC-FA-COA-62: Konfirmasi Delete single menghapus akun dan menyisakan Account Code di log

15. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p55.code`, tekan Enter
16. Klik row action `Delete` pada akun P55 (`Fixture.settingsChartOfAccounts.p55.code`) sehingga dialog D-07 terbuka
17. Klik `[Delete]`
18. Verifikasi toast "Success, account has been deleted."
19. Verifikasi akun P55 hilang dari tabel

### TC-FA-COA-284: Klik ganda `[Delete]` pada dialog D-07 menghapus akun satu kali

20. Tunggu toast lama hilang otomatis
21. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p83.code`, tekan Enter
22. Klik row action `Delete` pada akun P83 (`Fixture.settingsChartOfAccounts.p83.code`)
23. Klik `[Delete]` pada dialog D-07 dua kali cepat
24. Verifikasi hanya satu toast "Success, account has been deleted."
25. Verifikasi akun P83 hilang dari tabel

### TC-FA-COA-68: Bulk Delete semua akun eligible menghapus seluruh akun terpilih

26. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p58.code`, tekan Enter
27. Centang akun P58 (`Fixture.settingsChartOfAccounts.p58.code`)
28. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p59.code`, tekan Enter
29. Centang akun P59 (`Fixture.settingsChartOfAccounts.p59.code`)
30. Klik Bulk `Delete`
31. Verifikasi dialog "Delete Accounts" dengan bullet `• Fixture.settingsChartOfAccounts.p58.code – Fixture.settingsChartOfAccounts.p58.name`, `• Fixture.settingsChartOfAccounts.p59.code – Fixture.settingsChartOfAccounts.p59.name`, dan teks "This action cannot be undone. Are you sure you want to delete them?"
32. Tunggu toast lama hilang otomatis
33. Klik `[Delete]` pada D-08
34. Verifikasi toast "Success, account has been deleted."
35. Verifikasi akun P59 hilang dari tabel
36. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p58.code`, tekan Enter
37. Verifikasi akun P58 hilang dari tabel
38. Verifikasi seleksi di-reset
39. Verifikasi Bulk Action Bar tidak tampil

## Notes

- Spec 39 langkah, di atas ambang 35 langkah. Alasan: satu topik aksi Delete dengan akun sekali pakai per blok; aksi yang menghapus data (TC-62, TC-284, TC-68) ada di akhir spec (S-10).
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; `[Cancel]` dan hapus centang P5 (langkah 13, 14) membersihkan dialog dan seleksi sebelum TC berikutnya; "Tunggu toast lama hilang otomatis" (langkah 20, 32) karena teks toast sama dengan TC sebelumnya.
- Dialog D-07 TC-63 adalah dialog yang sama dengan yang dibuka TC-61 pada akun P3 (langkah 2); langkah klik row action TC-63 terpenuhi oleh langkah itu, dan TC-63 dilanjutkan dari langkah 6.
- Asersi hilangnya baris (langkah 19, 25, 35, 37) memakai toast sukses sebagai anchor (8b.2).
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- A-18: akun sekali pakai P55 (TC-62), P83 (TC-284), P58 dan P59 (TC-68) dihapus spec ini dengan Account Code literal tanpa suffix `{runId}` (batas 15 karakter); seed idempotent dipulihkan di hook `before` dan `after`.
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan (langkah 26 sampai 31).
  - Post Condition TC-62 (hard delete, log L-04 satu baris di tiga surface, Account Code tetap terbaca di log, dampak modul lain) dan TC-68 dan TC-284 (log L-04 per akun per surface) tidak punya langkah observasi di TC sehingga tidak diasersi.
