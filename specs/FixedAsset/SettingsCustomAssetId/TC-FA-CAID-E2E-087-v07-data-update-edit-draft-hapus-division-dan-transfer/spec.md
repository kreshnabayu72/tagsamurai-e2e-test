---
id: TC-FA-CAID-E2E-087-v07-data-update-edit-draft-hapus-division-dan-transfer
title: "V-07 pada Data Update, Edit Draft, Hapus Division, dan Transfer"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-284
  - TC-FA-CAID-291
  - TC-FA-CAID-336
  - TC-FA-CAID-276
coverage:
  web: automated
---

# V-07 pada Data Update, Edit Draft, Hapus Division, dan Transfer

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Company V07D (Pre-setup No 33; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE), password `Spectra.env.FA_V07D_TC_PASSWORD` (nama env dari kolom `Akun dan Env Var` Pre-setup No 33; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit untuk TC-FA-CAID-276): Total Control Company V07T (Pre-setup No 32; email disediakan tim FE), password `Spectra.env.FA_V07T_TC_PASSWORD` (nama env dari kolom `Akun dan Env Var` Pre-setup No 32; didaftarkan tim FE).
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup Company V07D (No 33): formula Initial Company `ABCDE`, Group, Category, Asset Name, Division, Purchase Date, Increment; Group Code `GRP-LONG-000001`, Category Code `CAT-LONG-000001`, Asset Name Code `AST-LONG-000001`; Division `Procurement` (Code `PRC`, tanpa pengguna terkait) dan Division `Procurement X` (Code `PRCX`, menghasilkan 65 karakter). Hook `before` men-seed aset Draft AS1 (Asset ID 64 karakter, segmen Purchase Date `0000`, Division `Procurement`; TC-FA-CAID-284) dan aset Draft DD1 (Asset ID 64 karakter, Division `Procurement`; TC-FA-CAID-336 dan 291).
- Data Pre-setup Company V07T (No 32): aset Active Asset ID `GRP-LONG-00001-CAT-LONG-000001-AST-LONG-000001-DIVISION-ABC-15-1` (64 karakter, Group Code asal `GRP-LONG-00001`), Group tujuan berkode `GRP-LONG-000002`, tiket Transfer XFR-1 In Transit (hasil seed hook `before`).
- Fixture: nilai data Pre-setup di atas (akun Company, master data, Code Division, Asset ID seed) dibaca dari `Fixture.customAssetId.<kunci>`; berkas `fixtures/customAssetId.json` belum ada (prasyarat tahap script yang disediakan tim FE/BE).
- Data Dinamis: tidak ada data baru; Purchase Date AS1 diubah (`15/09/26`) dan dikembalikan oleh seed reset Company.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: Purchase Date AS1 berubah; hook `after` memulihkan Company V07D dan Company V07T ke seed awal dan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-284: Pengisian Purchase Date pada Asset ID 64 karakter tetap sah

1. Buka Fixed Asset > Assets > Registration
2. Klik `[Complete Detail]` pada aset AS1
3. Isi Purchase Date `15/09/26` lalu klik `[Save Details]`
4. Verifikasi toast sukses `Success, asset details completed.` tampil
5. Buka Fixed Asset > Assets > All Assets > Detail AS1
6. Verifikasi segmen Purchase Date pada Asset ID AS1 menjadi `0926` (menggantikan `0000`)
7. Verifikasi Asset ID AS1 tetap 64 karakter

### TC-FA-CAID-336: Mutasi Division lewat Edit Draft yang membuat Asset ID melebihi 64 karakter membatalkan Edit Draft

8. Buka Fixed Asset > Assets > Registration
9. Edit Draft aset DD1: ganti Division menjadi `Procurement X` lalu simpan
10. Verifikasi toast error `Error, failed to update asset.` tampil dan bertahan sampai di-dismiss
11. Dismiss toast error
12. Klik `✕` pada form Edit Draft
13. Verifikasi dialog `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
14. Klik `[Leave]`
15. Verifikasi form Edit Draft tertutup
16. Buka Fixed Asset > Assets > All Assets > Detail DD1 > tab `Histori Aset`
17. Verifikasi Division DD1 tetap `Procurement`
18. Verifikasi Asset ID DD1 tetap 64 karakter semula
19. Verifikasi tidak ada entri riwayat maupun banner

### TC-FA-CAID-291: Hapus Division yang membuat Asset ID melebihi 64 karakter membatalkan penghapusan

20. Buka Global Settings > User > Division
21. Klik `⋯` pada baris `Procurement` lalu `Delete`
22. Klik `[Delete]` pada dialog `Delete Division`
23. Verifikasi toast error `Error, failed to delete division.` tampil dan bertahan sampai di-dismiss
24. Dismiss toast error
25. Verifikasi Division `Procurement` masih ada pada daftar Division
26. Buka Fixed Asset > Assets > All Assets > Detail DD1 > tab `Histori Aset`
27. Verifikasi Asset ID DD1 tetap 64 karakter semula
28. Verifikasi tidak ada entri riwayat

### TC-FA-CAID-276: Pembaruan Asset ID akibat Transfer yang melebihi 64 karakter membatalkan Transfer

29. Logout dari akun Total Control Company V07D
30. Login sebagai Total Control Company V07T (password dari `Spectra.env.FA_V07T_TC_PASSWORD`)
31. Buka Fixed Asset > Transactions > Transfer
32. Buka tab Incoming lalu klik `[Arrival Scan]` pada XFR-1
33. Lakukan verifikasi unit aset pada arrival scan lalu klik `[Confirm Receipt]`
34. Verifikasi toast error `Error, failed to transfer asset.` tampil dan bertahan sampai di-dismiss
35. Verifikasi tiket XFR-1 tetap In Transit
36. Dismiss toast error
37. Buka Fixed Asset > Assets > All Assets > Detail aset > tab `Histori Aset`
38. Verifikasi Group aset tetap Group asal
39. Verifikasi Asset ID aset tetap 64 karakter semula
40. Verifikasi tidak ada entri riwayat maupun banner

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 40 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik (V-07 memblokir mutasi Asset ID pada Data Update, Edit Draft, hapus Division, dan Transfer), semua kelas fungsional blokir kondisi data, tiap blok memakai data seed sendiri (AS1, DD1, aset V07T) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Penyimpangan urutan: TC-FA-CAID-336 ditulis sebelum TC-FA-CAID-291 agar dua TC yang berjalan di Registration berurutan sebelum pindah ke Global Settings > User > Division; kedua TC memakai DD1 yang tidak berubah karena mutasinya ditolak.
- Langkah penghubung: langkah 1, 8 (buka halaman), 11, 24, 36 (dismiss toast error sebelum asersi berikutnya), 12 dan 14 (menutup form Edit Draft dengan `✕` dan `[Leave]`; `Verifikasi` dialog `Unsaved Changes` pada langkah 13 mengikuti S-08), 29 dan 30 (ganti akun eksplisit, S-07).
- Temuan untuk QA:
  - Langkah TC-FA-CAID-284 hanya mengisi Purchase Date, sedangkan TC-FA-CAID-277 mensyaratkan Purchase Price dan faktur pada `[Save Details]`; spec mengikuti TC-FA-CAID-284 apa adanya.
  - Pre-setup No 33 kini memisahkan Company V07R (spec 086) dan Company V07D (TC-FA-CAID-284, 291, 336). Nilai separator formula dan Asset ID literal aset seed tidak tertulis, sehingga hanya panjang 64 karakter dan segmen Purchase Date yang diasersi.
  - Email akun Total Control Company V07D dan Company V07T tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}` dan "email disediakan tim FE/BE").
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
