---
id: TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup
title: "Defense-in-Depth: Request Langsung Wizard, Download, Node Excess, Function Ganda, Delete Guard, Isolasi Client, Nilai Bergerbang, serta Markup dan SQL sebagai Teks"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-926
  - TC-FA-GRP-927
  - TC-FA-GRP-928
  - TC-FA-GRP-929
  - TC-FA-GRP-930
  - TC-FA-GRP-931
  - TC-FA-GRP-932
  - TC-FA-GRP-933
  - TC-FA-GRP-963
  - TC-FA-GRP-934
  - TC-FA-GRP-935
  - TC-FA-GRP-1249
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Wizard, Download, Node Excess, Function Ganda, Delete Guard, Isolasi Client, Nilai Bergerbang, serta Markup dan SQL sebagai Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Password user subjek yang di-seed: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru).
- Request langsung (tabel di bawah dan TC-1249) memakai klien HTTP dengan token sesi API aktor (tidak dihitung sebagai sesi web); env password aktor adalah nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`. TC-934 dan 935 memakai UI sebagai Total Control.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dan fixture BE (membaca state data sebelum dan sesudah request); downgrade terjadwal plan Professional ke Growth (cap 3) dengan seleksi Wizard tersimpan berisi 2 group untuk dua baris Wizard (kelas h sebagai pemicu); ID group milik client lain.
- State global yang diubah spec (TC-931 dan 963): downgrade terjadwal plan Professional ke Growth (cap 3) dengan seleksi Wizard tersimpan berisi 2 group, dibentuk fixture BE di hook `before`. Pemulihan di hook `after` oleh fixture BE yang disediakan tim FE/BE: jadwal downgrade dibatalkan, seleksi Wizard tersimpan dihapus, plan kembali Professional. Suite berjalan serial.
- Data (dibaca atau milik spec): Warehouse A dan Warehouse B (Excess) Pre-setup No 9 (ditolak, tidak berubah); `Edit Target {runId}-209` (Function Assignable, di-seed lewat API di hook `before`, dihapus di hook `after`); node uji XSS/SQL dibuat TC-934 dan 935 dan dihapus di hook `after`; untuk TC-1249 fixture `Value Gate Node A {runId}-209` (Pre-setup tambahan No 10: aset G1 sampai G6 dengan Asset Value, Warranty Expiry, dan custom field Purchasing; dibaca saja, dihapus di hook `after`). Aktor TC-1249: `noValueAccess_automated_{namaCompany}@qwertysystem.net` (No 16, env `FA_GRP_NOVALUEACCESS_PASSWORD`) dan `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net` (No 14, env `FA_GRP_MANAGEPURCHASE_PASSWORD`).

  | Aktor | Env password | Request langsung ke API | Hasil yang diharapkan |
  |---|---|---|---|
  | Group Manager scope Region West (No 4) | `FA_GM_PASSWORD` | simpan seleksi Wizard Group Consolidation | ditolak server (403), hanya Total Control atau Default User |
  | Read Only (No 3) | `FA_RO_PASSWORD` | simpan seleksi Wizard Group Consolidation | ditolak server (403) |
  | Role Lain tanpa Manage Group (No 7) `otherRole_automated_{namaCompany}@qwertysystem.net` | `FA_OTHER_PASSWORD` | Download Groups dan Download Changelog | ditolak server |
  | Total Control (No 1) | `FA_TC_PASSWORD` | Edit Warehouse B lalu Add Subgroup di bawahnya (dua request) | keduanya ditolak (422, group excess terkunci) |
  | Total Control (No 1) | `FA_TC_PASSWORD` | Edit `Edit Target {runId}-209` dengan penanda Assignable=true dan Disposal Group=true | ditolak (422); kombinasi tidak tersimpan; Function tetap nilai lama |
  | Total Control (No 1) | `FA_TC_PASSWORD` | simpan seleksi Wizard berisi 4 group (cap 3 berjalan) | ditolak (422, seleksi melebihi cap); seleksi tersimpan lama tetap |
  | Total Control (No 1) | `FA_TC_PASSWORD` | simpan seleksi Wizard berisi 0 group (cap 3 berjalan, seleksi tersimpan berisi 2 group) | ditolak (422, seleksi kosong); seleksi tersimpan lama tetap berlaku |
  | Total Control (No 1) | `FA_TC_PASSWORD` | Delete Warehouse A (beraset) | ditolak; Warehouse A tidak terhapus |
  | Total Control (No 1) | `FA_TC_PASSWORD` | baca, edit, dan delete group dengan ID milik client lain | ditolak server (tidak dilayani); tidak ada data client lain yang dikembalikan atau diubah |

## Test Steps

1. Untuk setiap baris tabel Prerequisites (langkah 1 sampai 4): Catat state data target request lewat fixture BE
2. Kirim request pada kolom Request langsung ke API dengan token sesi API aktor pada baris tabel
3. Verifikasi respons ditolak server sesuai kolom Hasil yang diharapkan
4. Verifikasi state data target (termasuk Function dan seleksi tersimpan) tidak berubah dibanding yang dicatat lewat fixture BE

### TC-934: Payload HTML/script dirender sebagai teks

5. Klik [+] Group
6. Isi Group Name `<script>alert(1)</script> {runId}-209` dan Description `<img src=x onerror=alert(1)>`, klik [Submit]
7. Verifikasi toast sukses "Success, group has been created."
8. Ketik Search `{runId}-209`, tekan Enter
9. Buka tabel Groups List, sidebar, Detail, dan Changelog
10. Verifikasi Group Name dan Description tampil sebagai teks literal di tabel, sidebar, Detail, dan Changelog
11. Verifikasi tidak ada script yang dieksekusi (tidak ada dialog alert)

### TC-935: String SQL disimpan literal

12. Klik [+] Group
13. Isi Group Name `Lab'; DROP TABLE groups; -- {runId}-209`, klik [Submit]
14. Verifikasi toast sukses "Success, group has been created."
15. Kosongkan Search dengan klik `✕`, lalu ketik Search `{runId}-209`, tekan Enter
16. Verifikasi group tersimpan dengan nama literal `Lab'; DROP TABLE groups; -- {runId}-209`
17. Kosongkan Search dengan klik `✕`, lalu ketik Search `Head Office`, tekan Enter
18. Verifikasi Head Office tetap tampil di Groups List
19. Kosongkan Search dengan klik `✕`, lalu ketik Search `Warehouse A`, tekan Enter
20. Verifikasi Warehouse A tetap tampil di Groups List

### TC-1249: Server tidak mengirim nilai sel bergerbang

21. Catat state data Tab Assets `Value Gate Node A {runId}-209` lewat fixture BE
22. Kirim request baca data Tab Assets `Value Gate Node A {runId}-209` sebagai noValueAccess
23. Verifikasi respons memuat sedikitnya satu baris dengan kolom lain yang tidak bergerbang terisi (anchor)
24. Verifikasi payload baris tidak memuat nilai Asset Value, Warranty Expiry, maupun custom field Purchasing; hanya penanda keadaan `No access`
25. Kirim request baca yang sama dengan parameter filter Asset Value Min 0 Max 99999 sebagai noValueAccess
26. Verifikasi data Tab Assets `Value Gate Node A {runId}-209` tanpa filter berisi sedikitnya satu baris (anchor, dari respons request tanpa filter)
27. Verifikasi respons filter Asset Value mengembalikan 0 baris
28. Kirim request baca yang sama sebagai managePurchaseGroups untuk kolom Asset Value
29. Verifikasi respons memuat sedikitnya satu baris dengan kolom lain yang tidak bergerbang terisi (anchor)
30. Verifikasi nilai Warranty Expiry terkirim
31. Verifikasi nilai Asset Value tidak ikut terkirim
32. Verifikasi state data tidak berubah dibanding yang dicatat lewat fixture BE sebelum request

## Notes

- K-1: seluruh TC API di spec ini kelas a dengan Expected respons API; tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec. Asersi hanya status respons dan state data lewat fixture BE (8b butir 1). TC-934 dan 935 memakai UI untuk melihat payload dirender sebagai teks.
- Langkah 1 sampai 4 berulang untuk setiap baris tabel Prerequisites (9 baris: TC-926 sampai 933 dan TC-963); satu `Verifikasi` per klausa tetap dipertahankan (8b butir 7). TC-931 dan 963 mengasersi hanya respons API; dialog blok FE "Cannot Save Selection" diasersi di spec jalur form, bukan di sini (8b butir 1).
- Spec memiliki 32 langkah nominal dan 64 langkah setelah ekspansi, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (defense-in-depth tanpa harness eksternal) dan tiap blok berdiri sendiri; ekspansi berasal dari perulangan tabel tanpa langkah bersyarat (8b butir 7).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Asersi absence payload TC-1249 (8b butir 2): `Verifikasi` respons memuat sedikitnya satu baris dengan kolom lain terisi mendahului asersi tiap nilai bergerbang tidak terkirim; Warranty Expiry terkirim dipindah mendahului asersi Asset Value tidak terkirim untuk managePurchaseGroups. Filter Asset Value mengembalikan 0 baris dianchor oleh data tanpa filter yang berisi sedikitnya satu baris. Baseline state dicatat sebelum request TC-1249 (S-12).
- Temuan untuk QA:
  - TC-931 dan 963 Expected b (dialog blok D-23 "Cannot Save Selection") adalah perilaku FE pada request langsung; tidak disalin ke spec (8b butir 1).
  - Kode status respons TC-928, 932, dan 933 tidak ditulis TC ("ditolak"); spec tidak mengarang kode. TC-933 memuat ID group client lain tanpa menyebut sumbernya; disediakan tim FE/BE.
  - TC-1249 membutuhkan Value Gate Node A dengan nilai asli tersimpan (Dinamis No 10); fixture milik spec diberi suffix per run. TC-934 menulis Group Name `<script>alert(1)</script>` literal; spec menambah suffix `{runId}-209` setelah payload (S-12). TC-935 menulis `Lab'; DROP TABLE groups;--`; spec menambah spasi dan suffix.
  - Penolakan TC-926 (hanya Total Control atau Default User) dan TC-927 tidak mendefinisikan akun Default User sebagai kontrol positif; tidak ditambahkan.
