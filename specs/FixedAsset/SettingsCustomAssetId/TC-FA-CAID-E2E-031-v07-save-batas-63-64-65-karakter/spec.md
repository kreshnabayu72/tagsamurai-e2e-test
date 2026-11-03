---
id: TC-FA-CAID-E2E-031-v07-save-batas-63-64-65-karakter
title: "V-07 pada Save: Batas 63, 64, dan 65 Karakter serta Rollback Transaksi"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-86
  - TC-FA-CAID-87
  - TC-FA-CAID-88
  - TC-FA-CAID-89
coverage:
  web: automated
---

# V-07 pada Save: Batas 63, 64, dan 65 Karakter serta Rollback Transaksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada tiga Company khusus (Pre-setup No 19): `Company V07 63`, `Company V07 64`, `Company V07 65`. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun dan password disediakan tim FE dengan env var usulan `Spectra.env.FA_V0763_TC_PASSWORD`, `Spectra.env.FA_V0764_TC_PASSWORD`, `Spectra.env.FA_V0765_TC_PASSWORD`. Login akun `Company V07 63` di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke `Company V07 64` dan `Company V07 65` ditulis sebagai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (No 19): tiap Company V07 memiliki satu aset Draft dengan Group Code `GRP-LONG-000001`, Category Code `CAT-LONG-000001`, Asset Name Code `AST-LONG-000001`, Separator `- (Dash)`, formula tanpa Purchase Date, dan Division yang di-assign ke aset Draft itu: `Company V07 63` memakai Division Code `DIVISION-A-13`, `Company V07 64` memakai `DIVISION-AB-14`, `Company V07 65` memakai `DIVISION-ABC-15`. `Company V07 65` juga memiliki aset kedua berkode pendek (Group Code `JKT`, Category Code `LAP`, Asset Name Code `T490`) ber-Asset ID `JKT-LAP-T490-2`.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID untuk akun `Company V07 63`; langkah ganti akun diikuti langkah membuka tab itu.
- Kemampuan teknis: seed ketiga Company V07 dan pengembalian ke keadaan awal sebelum run disediakan tim FE/BE; sesi API aktor tiap Company untuk seed dan pemulihan (suite.md); konfirmasi otomatis dialog `beforeunload` browser oleh harness untuk langkah muat ulang pada form berisi perubahan belum tersimpan (prasyarat tahap script yang disediakan tim FE/BE).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: konfigurasi dan Asset ID aset di `Company V07 63` dan `Company V07 64` berubah (Division Code tercentang). Hook `after` memulihkan ketiga Company V07 ke seed awal lewat seed API. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-86: Save dengan Asset ID 63 karakter diterima

1. Centang `Division Code`
2. Klik `[Save]`
3. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
4. Buka Fixed Asset > Assets > All Assets
5. Verifikasi Asset ID aset menjadi `GRP-LONG-000001-CAT-LONG-000001-AST-LONG-000001-DIVISION-A-13-1` (63 karakter)

### TC-FA-CAID-87: Save dengan Asset ID tepat 64 karakter diterima

6. Ganti akun: logout, lalu login sebagai Total Control `Company V07 64`
7. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
8. Centang `Division Code`
9. Klik `[Save]`
10. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
11. Buka Fixed Asset > Assets > All Assets
12. Verifikasi Asset ID aset menjadi `GRP-LONG-000001-CAT-LONG-000001-AST-LONG-000001-DIVISION-AB-14-1` (64 karakter) tanpa pemotongan

### TC-FA-CAID-88: Save dengan Asset ID 65 karakter ditolak dengan alert inline

13. Ganti akun: logout, lalu login sebagai Total Control `Company V07 65`
14. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
15. Centang `Division Code`
16. Klik `[Save]`
17. Verifikasi alert inline severity danger tampil tepat di atas `[Save]` berbunyi `Asset ID would exceed 64 characters. Remove a segment or choose a shorter separator.`
18. Verifikasi tidak ada toast sukses maupun toast error
19. Muat ulang halaman
20. Verifikasi checkbox `Division Code` tidak tercentang (konfigurasi tersimpan tidak berubah)
21. Buka Fixed Asset > Assets > All Assets
22. Verifikasi Asset ID aset tetap `GRP-LONG-000001-CAT-LONG-000001-AST-LONG-000001-1` tanpa pemotongan otomatis

### TC-FA-CAID-89: Penolakan V-07 membatalkan seluruh transaksi

23. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
24. Pilih Separator `. (Dot)`
25. Centang `Division Code`
26. Klik `[Save]`
27. Verifikasi alert inline V-07 `Asset ID would exceed 64 characters. Remove a segment or choose a shorter separator.` tampil di atas `[Save]`
28. Klik menu `Assets` pada sidebar navigasi
29. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
30. Klik `[Leave]`
31. Buka Fixed Asset > Assets > All Assets
32. Verifikasi aset kedua tetap `JKT-LAP-T490-2` (Separator Dash lama)
33. Verifikasi aset pertama tetap `GRP-LONG-000001-CAT-LONG-000001-AST-LONG-000001-1`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: membuka Fixed Asset > Assets > All Assets dan tab Custom Asset ID, ganti akun antar Company V07, muat ulang halaman (dialog `beforeunload` dikonfirmasi otomatis, kemampuan di Prerequisites), serta menutup form dirty lewat sidebar, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]` (S-08) sebelum membuka All Assets pada TC-FA-CAID-89.
- Langkah ke All Assets pada TC-FA-CAID-86 dan TC-FA-CAID-87 tidak memicu dialog karena form pristine setelah Save sukses.
- Urutan TC mengikuti nomor TC; validasi yang ditolak (TC-FA-CAID-88 dan TC-FA-CAID-89) tidak mendahului aksi sukses karena tiap TC memakai Company V07 berbeda.
- Pembagian TC lintas spec: TC-FA-CAID-90, TC-FA-CAID-91, dan TC-FA-CAID-334 ada di spec 032; TC-FA-CAID-92 dan TC-FA-CAID-93 ada di spec 047.
- Temuan untuk QA:
  - TC-FA-CAID-86 sampai 88 menulis akun "Total Control (Pre-setup #1) pada Company V07 63/64/65", sedangkan Pre-setup No 1 hanya mendefinisikan akun Company Alpha; email akun per Company V07 tidak tertulis di Pre-setup TC dan ditulis "disediakan tim FE".
  - Pre-setup No 19 tidak menyebut aset kedua berkode pendek untuk varian `Company V07 63` dan `Company V07 64`; hanya TC-FA-CAID-89 memakainya. Nilai `JKT-LAP-T490-2` pada TC-FA-CAID-89 mengasumsikan aset kedua ber-Increment 2.
  - TC-FA-CAID-88 langkah 3 memuat ulang halaman saat form masih berisi perubahan belum tersimpan sehingga dialog `beforeunload` browser muncul; TC tidak menyebutnya dan spec menanganinya sebagai kemampuan harness.
  - Post Condition TC-FA-CAID-86 sampai 89 tidak diasersi karena TC tidak memberi langkah observasinya.
