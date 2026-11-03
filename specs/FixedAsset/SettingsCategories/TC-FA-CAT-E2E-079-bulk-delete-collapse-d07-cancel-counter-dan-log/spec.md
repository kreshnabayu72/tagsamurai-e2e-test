---
id: TC-FA-CAT-E2E-079-bulk-delete-collapse-d07-cancel-counter-dan-log
title: "Bulk Delete: Collapse ke Dialog D-07, Cancel Tidak Mereset Seleksi, Seleksi 0 Setelah Commit, dan Log per Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-258
  - TC-FA-CAT-634
  - TC-FA-CAT-266
  - TC-FA-CAT-267
  - TC-FA-CAT-269
coverage:
  web: automated
---

# Bulk Delete: Collapse ke Dialog D-07, Cancel Tidak Mereset Seleksi, Seleksi 0 Setelah Commit, dan Log per Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup in-use yang hanya dibaca dan menjadi target aksi yang diblokir atau dilewati (tidak diubah; S-06): `Furniture` (ditunjuk Asset Name `Office Chair`) dan `Tools` (ditunjuk `Drill Set`). Asset Name Pre-setup #21.
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after` bila tersisa): `Vehicle {runId}-079` (Code `V79`, leaf), `Heavy Tools {runId}-079` (Code `HT79`, leaf, Total Asset 0, pengganti `Heavy Tools` Pre-setup #39), `Accessory {runId}-079` (Code `A79`) berisi `Cable {runId}-079`, `Peripheral {runId}-079` (Code `P79`) berisi `Keyboard {runId}-079` dan `Mouse {runId}-079`.
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline); disediakan tim FE/BE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Atur jumlah baris per halaman menjadi 25

### TC-FA-CAT-258: Seleksi satu kategori yang dipakai Asset Name collapse ke dialog D-07

2. Centang checkbox baris `Furniture`
3. Klik `[Delete]` pada Bulk Action Bar
4. Verifikasi dialog `Cannot Delete Category` D-07 bentuk tunggal tampil (bukan D-13)
5. Tutup dialog D-07
6. Klik icon (×) pada Bulk Action Bar

### TC-FA-CAT-634: Cancel pada dialog Bulk Delete campuran D-12 tidak mereset seleksi

7. Centang checkbox baris `Vehicle {runId}-079` dan `Tools`
8. Catat baseline jumlah entri Changelog kategori (N1)
9. Klik `[Delete]` pada Bulk Action Bar sampai dialog D-12 tampil
10. Verifikasi dialog `Delete Categories` dengan dua kelompok bullet tampil
11. Verifikasi tombol `[Cancel]` dan `[Continue]` tampil
12. Klik `[Cancel]`
13. Verifikasi dialog tertutup
14. Verifikasi kedua baris tetap tercentang dengan counter `2 categories selected`
15. Verifikasi baris `Vehicle {runId}-079` dan `Tools` masih tampil (tidak ada perubahan data)
16. Verifikasi tidak ada toast
17. Verifikasi jumlah entri Changelog kategori masih N1 (tidak ada log)
18. Klik icon (×) pada Bulk Action Bar

### TC-FA-CAT-266: Cancel pada dialog Bulk Delete tidak mereset seleksi

19. Centang checkbox baris `Vehicle {runId}-079` dan `Heavy Tools {runId}-079`
20. Klik `[Delete]` pada Bulk Action Bar
21. Klik `[Cancel]`
22. Verifikasi dialog tertutup
23. Verifikasi kedua baris tetap tercentang dengan counter `2 categories selected`
24. Verifikasi baris `Vehicle {runId}-079` dan `Heavy Tools {runId}-079` masih tampil (tidak ada perubahan data)
25. Klik icon (×) pada Bulk Action Bar

### TC-FA-CAT-267: Setelah Bulk Delete ter-commit bar hilang dan seleksi menjadi 0 termasuk baris yang di-skip

26. Centang checkbox baris `Vehicle {runId}-079` dan `Tools`
27. Klik `[Delete]` pada Bulk Action Bar
28. Klik `[Continue]`
29. Verifikasi Bulk Action Bar hilang
30. Verifikasi semua checkbox kosong, termasuk `Tools` yang di-skip dan tetap tampil di tabel

### TC-FA-CAT-269: Log Bulk Delete, satu baris per node terhapus dengan Date sama, skip tidak menulis entri

31. Centang checkbox baris `Peripheral {runId}-079`, `Accessory {runId}-079`, dan `Tools`
32. Klik `[Delete]` pada Bulk Action Bar
33. Klik `[Continue]`
34. Buka Modal Changelog
35. Verifikasi Changelog memuat lima baris Delete (`Peripheral {runId}-079`, `Peripheral {runId}-079 › Keyboard {runId}-079`, `Peripheral {runId}-079 › Mouse {runId}-079`, `Accessory {runId}-079`, `Accessory {runId}-079 › Cable {runId}-079`) dengan Date yang sama (satu batch)
36. Verifikasi tidak ada baris Delete untuk `Tools` yang di-skip
37. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-FA-CAT-260 ada di spec 187.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Bulk Delete), satu client, dan berdiri sendiri; delapan langkah di antaranya hanya langkah penghubung.
- Urutan: dialog tanpa eksekusi (TC-FA-CAT-258, TC-FA-CAT-634, TC-FA-CAT-266) mendahului eksekusi (TC-FA-CAT-267, TC-FA-CAT-269) sesuai S-10.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): pengaturan jumlah baris per halaman, penutupan dialog D-07, icon (×), pencatatan baseline, membuka dan menutup Modal Changelog.
- P-1: asersi "tidak ada log" pada TC-FA-CAT-634 berada di spec ini dengan baseline (S-12) karena konteksnya (seleksi dan dialog D-12 yang baru dibangun) tidak dapat dibentuk ulang di spec absence tanpa biaya.
- Data milik spec menggantikan `Vehicle`, `Heavy Tools`, `Peripheral`, `Accessory` Pre-setup (S-06).
- Temuan untuk QA:
  - TC-FA-CAT-634 menyebut "tidak ada log" tanpa surface; spec hanya memeriksa Changelog.
  - TC-FA-CAT-258 tidak menulis tombol dan teks dialog D-07; spec hanya meng-assert dialog tampil dan menutupnya.
  - TC-FA-CAT-266 Precondition menyebut Pre-setup #39 (`Heavy Tools`); diganti kategori milik spec.
