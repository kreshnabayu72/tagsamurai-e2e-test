---
id: TC-FA-CAT-E2E-075-bulk-delete-homogen-bulk-bar-dialog-d11-hitungan-descendant
title: "Bulk Delete Homogen: Bulk Action Bar, Dialog D-11, Hitungan Descendant, dan Toast T-07"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-241
  - TC-FA-CAT-247
  - TC-FA-CAT-248
  - TC-FA-CAT-249
coverage:
  web: automated
---

# Bulk Delete Homogen: Bulk Action Bar, Dialog D-11, Hitungan Descendant, dan Toast T-07

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after` bila tersisa), semua L1, nama berakhiran `{runId}-075`:
  - `Vehicle {runId}-075` (Code `V75`) leaf dan `Tools {runId}-075` (Code `T75`) leaf.
  - `Accessory {runId}-075` (Code `A75`) berisi `Cable {runId}-075`.
  - `Spare Part {runId}-075` (Code `S75`) > `Bolt {runId}-075` > `Bolt M8 {runId}-075`.
  - `Peripheral {runId}-075` (Code `P75`) berisi `Keyboard {runId}-075` dan `Mouse {runId}-075`.
- Data Pre-setup #20 hanya dibaca (tidak diubah).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `{runId}-075`, tekan Enter

### TC-FA-CAT-241: Screening Bulk Action Bar dan siklus counter singular/plural

2. Centang checkbox baris `Vehicle {runId}-075`
3. Verifikasi Bulk Action Bar muncul di atas tabel rata kiri sejajar Table Tools dengan urutan Button `Bulk Action`, teks counter, Button `Select All (N records)`, icon (×)
4. Verifikasi counter `1 category selected`
5. Verifikasi aksi `Delete` pada bar berseverity danger dengan icon `DeleteBin6Line`
6. Centang checkbox baris `Tools {runId}-075`
7. Verifikasi counter `2 categories selected`
8. Hapus centang `Tools {runId}-075`
9. Verifikasi counter `1 category selected`
10. Klik icon (×) pada bar
11. Verifikasi seluruh seleksi dibatalkan
12. Verifikasi bar hilang

### TC-FA-CAT-248: Dialog D-11 menghitung distinct descendant yang tidak ikut seleksi (bentuk jamak)

13. Centang checkbox baris `Spare Part {runId}-075` dan `Peripheral {runId}-075`
14. Klik `[Delete]` pada Bulk Action Bar
15. Verifikasi kalimat `The selected categories have 4 subcategories in total — deleting them will also delete all of them.` (Bolt, Bolt M8, Keyboard, Mouse)
16. Klik `[Cancel]`
17. Klik icon (×) pada bar

### TC-FA-CAT-249: Dialog D-11 tidak menghitung descendant yang sudah ada di seleksi

18. Centang checkbox baris `Peripheral {runId}-075` pada node `All Categories`
19. Klik node `Peripheral {runId}-075` di Sidebar Category Tree
20. Centang checkbox baris `Keyboard {runId}-075`
21. Verifikasi counter `2 categories selected` (`Peripheral {runId}-075` tetap terpilih setelah berganti node)
22. Klik `[Delete]` pada Bulk Action Bar
23. Verifikasi kalimat `The selected categories have 1 subcategory — deleting them will also delete it.` karena hanya `Mouse {runId}-075` yang tidak ikut dipilih
24. Klik `[Cancel]`
25. Klik icon (×) pada bar

### TC-FA-CAT-247: Bulk Delete homogen, dialog D-11 dan toast T-07

26. Klik node `All Categories` di Sidebar Category Tree
27. Ketik Search `{runId}-075`, tekan Enter
28. Centang checkbox baris `Vehicle {runId}-075` dan `Accessory {runId}-075`
29. Klik `[Delete]` pada Bulk Action Bar
30. Verifikasi dialog `Delete Categories` memuat bullet `Vehicle {runId}-075` dan `Accessory {runId}-075`, kalimat `The selected categories have 1 subcategory — deleting them will also delete it.`, dan `Are you sure you want to delete them? This action cannot be undone.`
31. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil
32. Klik `[Delete]`
33. Verifikasi toast `Success, category has been deleted.`
34. Verifikasi `Vehicle {runId}-075`, `Accessory {runId}-075`, dan `Cable {runId}-075` terhapus
35. Verifikasi bar hilang
36. Verifikasi seleksi menjadi 0

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Bulk Delete homogen), satu dataset milik spec, dan berdiri sendiri; delapan langkah di antaranya hanya langkah penghubung (Search, `[Cancel]`, pembatalan seleksi).
- Urutan TC: TC-FA-CAT-241, TC-FA-CAT-248, TC-FA-CAT-249, lalu TC-FA-CAT-247 (aksi yang menghapus data di akhir, S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03/R-16): Search `{runId}-075` untuk menemukan baris milik spec; `[Cancel]` dan icon (×) membersihkan dialog dan seleksi (S-09); klik node All Categories.
- Data milik spec menggantikan `Vehicle`, `Tools`, `Accessory`, `Spare Part`, `Peripheral` Pre-setup #20 agar Pre-setup tidak berubah (S-06).
- Temuan untuk QA:
  - TC-FA-CAT-247 Post Condition (Changelog menulis tiga baris Delete dengan Date sama) tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-FA-CAT-241 menyebut `Select All (N records)` tanpa nilai N; N adalah jumlah record tabel terfilter Search.
