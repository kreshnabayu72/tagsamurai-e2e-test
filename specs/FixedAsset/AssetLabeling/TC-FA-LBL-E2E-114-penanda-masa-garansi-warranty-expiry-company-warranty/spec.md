---
id: TC-FA-LBL-E2E-114-penanda-masa-garansi-warranty-expiry-company-warranty
title: "Penanda Masa Garansi Warranty Expiry (Company Warranty)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-582
  - TC-FA-LBL-583
  - TC-FA-LBL-584
  - TC-FA-LBL-585
  - TC-FA-LBL-587
coverage:
  web: automated
---

# Penanda Masa Garansi Warranty Expiry (Company Warranty)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Warranty` (Pre-setup #51, Time Zone General Settings GMT+7), `Fixture.assetLabeling.akun.totalControlWarranty`, `Spectra.env.FA_TC_WARRANTY_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Warranty-NoPurchase (`Company Warranty`; Read Manage Asset Master Data tanpa Manage purchase) (Pre-setup #52), `Fixture.assetLabeling.akun.warrantyNoPurchase`, `Spectra.env.FA_WARRANTYNOPURCHASE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Warranty` (#51), dirujuk lewat `Fixture.assetLabeling.warranty`: label `Warranty Tint` pada aset Active `Warranty Asset - 71` (Warranty Expiry H-1), `Warranty Asset - 72` (H), `Warranty Asset - 73` (H+30), `Warranty Asset - 74` (H+31), `Warranty Asset - 75` (belum ada), `Warranty Asset - 76` (H+1), dan `Warranty Asset - 77` (10 Nov 2026). H adalah hari ini menurut Time Zone client (GMT+7).
- Data Dinamis: tidak ada (nilai Warranty Expiry di-seed lewat API sesuai Data Pre-setup).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlWarranty` (email akun Total Control `Company Warranty`), `Fixture.assetLabeling.akun.warrantyNoPurchase` (email akun Warranty-NoPurchase), dan `Fixture.assetLabeling.warranty` (data Pre-setup #51 dan #52).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4). Seeding nilai Warranty Expiry aset `Warranty Asset - 71` sampai `Warranty Asset - 76` relatif terhadap H lewat API di hook `before` (nilai tidak ditetapkan tetap di Pre-setup; H dibaca dari Time Zone client pada saat seeding) dan pemulihan nilai awal di hook `after` (disediakan tim FE/BE; endpoint tidak ditulis di TC). Spec dijalankan jauh dari pergantian hari pada Time Zone client (batas H) supaya H tidak bergeser di tengah spec.
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat entitas. Data Pre-setup hanya dibaca kecuali nilai Warranty Expiry `Warranty Asset - 71` sampai `Warranty Asset - 76` yang di-seed relatif H di hook `before` (efek: Last Updated aset berubah) dan dipulihkan di hook `after`.
- Env var: `Spectra.env.FA_TC_WARRANTY_PASSWORD`, `Spectra.env.FA_WARRANTYNOPURCHASE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-582: Warranty Expiry lewat (sebelum hari ini): kelas danger dan tooltip Warranty expired

1. Klik chip `Warranty Tint` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Warranty Expiry`, lalu klik `[Save]`
3. Verifikasi tanggal `Warranty Asset - 71` tampil penuh sesuai format General Settings
4. Verifikasi tanggal `Warranty Asset - 71` berkelas danger (kode warna tidak di-assert)
5. Hover tanggal `Warranty Asset - 71`
6. Verifikasi tooltip `Warranty expired`

### TC-FA-LBL-583: Warranty Expiry hari ini dan hari berikutnya: masih berlaku, kelas warning dan tooltip Warranty expires soon

7. Verifikasi tanggal `Warranty Asset - 72` (jatuh hari ini, garansi masih berlaku) berkelas warning, bukan danger
8. Verifikasi tanggal `Warranty Asset - 76` berkelas warning
9. Hover tanggal `Warranty Asset - 72`
10. Verifikasi tooltip `Warranty expires soon`
11. Hover tanggal `Warranty Asset - 76`
12. Verifikasi tooltip `Warranty expires soon`
13. Verifikasi tanggal `Warranty Asset - 72` dan `Warranty Asset - 76` tetap tampil penuh

### TC-FA-LBL-584: Warranty Expiry batas 30 hari: hari ke-30 kelas warning, hari ke-31 normal tanpa penanda

14. Verifikasi tanggal `Warranty Asset - 73` (H+30, inklusif) berkelas warning
15. Hover tanggal `Warranty Asset - 73`
16. Verifikasi tooltip `Warranty expires soon`
17. Verifikasi tanggal `Warranty Asset - 74` (H+31) berkelas normal (bukan danger dan bukan warning)
18. Hover tanggal `Warranty Asset - 74`
19. Verifikasi tidak ada tooltip penanda masa garansi

### TC-FA-LBL-587: Warna Warranty Expiry tidak memengaruhi Sort dan Filter

20. Klik header kolom `Warranty Expiry` satu kali
21. Verifikasi urutan klik 1 (Oldest First): `Warranty Asset - 71`, `72`, `76`, `73`, `74`, lalu `75` (`—`) di akhir
22. Klik header kolom `Warranty Expiry` kedua kali
23. Verifikasi urutan klik 2 (Newest First): `Warranty Asset - 75` di awal, lalu `74`, `73`, `76`, `72`, `71`
24. Klik header kolom `Warranty Expiry` ketiga kali
25. Verifikasi urutan klik 3 kembali ke default Name A-Z
26. Klik icon Filter di toolbar Drawer, pilih rentang `Warranty Expiry` H-1 sampai H, lalu klik `[Apply]`
27. Verifikasi hanya `Warranty Asset - 71` dan `Warranty Asset - 72` tampil
28. Verifikasi `Warranty Asset - 71` tetap berkelas danger dan `Warranty Asset - 72` tetap berkelas warning
29. Buka panel Filter lagi, klik `[Clear Field]`, lalu tutup panel Filter

### TC-FA-LBL-585: Warranty Expiry — dan No access tanpa warna dan tanpa penanda masa garansi

30. Hover sel `Warranty Expiry` pada `Warranty Asset - 75`
31. Verifikasi sel `Warranty Asset - 75` menampilkan `—`
32. Verifikasi sel `Warranty Asset - 75` tanpa warna
33. Verifikasi sel `Warranty Asset - 75` tanpa tooltip masa garansi
34. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry`, lalu klik `[Save]`
35. Tutup Drawer Tagged Asset
36. Ganti akun: Logout, login sebagai Warranty-NoPurchase `Fixture.assetLabeling.akun.warrantyNoPurchase` (`Spectra.env.FA_WARRANTYNOPURCHASE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
37. Klik chip `Warranty Tint` di kolom Label
38. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Warranty Expiry`, lalu klik `[Save]`
39. Verifikasi sel `Warranty Expiry` pada `Warranty Asset - 71` dan `Warranty Asset - 72` menampilkan `No access`
40. Verifikasi sel `No access` pada `Warranty Asset - 71` dan `Warranty Asset - 72` tanpa warna danger maupun warning
41. Hover sel `No access` pada `Warranty Asset - 71`
42. Verifikasi tooltip sel `No access` hanya `Requires Manage purchase access in this group.`
43. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry`, lalu klik `[Save]`
44. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Penyimpangan urutan (bagian 3): TC-FA-LBL-587 ditaruh sebelum TC-FA-LBL-585 supaya Ganti akun ke Warranty-NoPurchase hanya sekali dan berada di akhir spec. Kolom `Warranty Expiry` dicentang sekali pada TC-FA-LBL-582 dan tetap tampil sampai bagian akun Total Control TC-FA-LBL-585 (Drawer tetap terbuka); langkah klik chip dan mencentang kolom di TC-FA-LBL-583, 584, 587, dan 585 tidak ditulis ulang karena keadaan yang dibutuhkannya sudah terpenuhi dan tidak ada Expected yang bergantung pada keadaan Hidden.
- Ganti akun: langkah Ganti akun ke Warranty-NoPurchase ditulis eksplisit; akun pertama (Total Control `Company Warranty`) login di hook `before`.
- Langkah penghubung (S-03): `[Clear Field]` sesudah Filter, Pemulihan kolom, dan tutup Drawer memulihkan keadaan awal (S-09).
- Kelas penanda (danger, warning, normal) diasersi lewat kelas elemen; kode warna tidak diasersi sesuai TC.
- Ukuran spec (44 langkah, di atas smell 35 langkah): kelima TC satu kelas (fungsional, penanda masa garansi `AST-LOGIC-11` pada kolom Warranty Expiry) pada akun dan data Pre-setup #51 yang sama dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Pembagian TC lintas spec: TC-FA-LBL-586 (Warranty Expiry mengikuti Time Zone dengan jam sistem diatur) ada di spec 115.
- Temuan untuk QA:
  - TC-FA-LBL-582 sampai 585 dan 587 menyebut H "hari ini menurut Time Zone client" tanpa menyebut cara seeding; Pre-setup #51 menyatakan nilai dibuat lewat seed API saat TC dijalankan; spec menulisnya sebagai kemampuan "disediakan tim FE/BE".
  - TC-FA-LBL-585 Langkah Uji 3 menyebut "lalu hover" pada sel `—` tanpa menyebut sel yang di-hover; spec men-hover sel `Warranty Asset - 75`.
