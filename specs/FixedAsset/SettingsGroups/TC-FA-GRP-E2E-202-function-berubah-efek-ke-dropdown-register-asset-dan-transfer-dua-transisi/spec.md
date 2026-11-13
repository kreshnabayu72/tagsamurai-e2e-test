---
id: TC-FA-GRP-E2E-202-function-berubah-efek-ke-dropdown-register-asset-dan-transfer-dua-transisi
title: "Perubahan Function (Dua Transisi) dan Efeknya ke Dropdown Register Asset dan Transfer"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-896
  - TC-FA-GRP-898
coverage:
  web: automated
---

# Perubahan Function (Dua Transisi) dan Efeknya ke Dropdown Register Asset dan Transfer

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan No 3, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix): node level 1 `Node XF {runId}-202` yang punya satu aset aktif (Available) dan satu riwayat (aset Disposed) sehingga kedua klausa "aset/histori tidak berpindah" dapat diamati pada Function mana pun. Function awal diatur lewat sesi API aktor pada langkah awal tiap blok (R-20).
- Function hanya `None` dan `Assignable`. Transisi None ke Assignable langsung tersimpan tanpa Dialog Change Function (TC-FA-GRP-896); transisi Assignable ke None memunculkan Dialog Change Function (TC-FA-GRP-898). Kedua transisi ditulis sebagai dua blok terpisah tanpa langkah bersyarat.

## Test Steps

### TC-FA-GRP-896: Function None ke Assignable, efek ke dropdown Register Asset dan Transfer

1. Buka Fixed Asset > Settings > Groups
2. Atur Function Node XF ke `None` lewat sesi API hingga tersimpan
3. Ketik Search `Node XF {runId}-202`, tekan Enter
4. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
5. Catat Group, status, dan jumlah aset node XF (termasuk aset Disposed) sebagai pembanding sebelum perubahan Function
6. Tutup Popup Detail Group
7. Buka elipsis Node XF, pilih Edit, pilih Function `Assignable`, klik [Save]
8. Tunggu aksi selesai
9. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
10. Verifikasi aset dan histori yang menunjuk node XF tidak berpindah, terkunci, atau terhapus dibanding catatan sebelum perubahan Function
11. Tutup Popup Detail Group
12. Buka Fixed Asset > Register Asset
13. Buka field Group Register Asset
14. Verifikasi sedikitnya satu opsi group lain tampil di field Group Register Asset
15. Verifikasi node XF muncul sebagai pilihan baru pada field Group Register Asset
16. Buka Fixed Asset > Transfer
17. Buka field tujuan Transfer
18. Verifikasi sedikitnya satu opsi group lain tampil di field tujuan Transfer
19. Verifikasi node XF muncul sebagai pilihan baru pada field tujuan Transfer

### TC-FA-GRP-898: Function Assignable ke None, efek ke dropdown Register Asset dan Transfer

20. Buka Fixed Asset > Settings > Groups
21. Atur Function Node XF ke `Assignable` lewat sesi API hingga tersimpan
22. Ketik Search `Node XF {runId}-202`, tekan Enter
23. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
24. Catat Group, status, dan jumlah aset node XF (termasuk aset Disposed) sebagai pembanding sebelum perubahan Function
25. Tutup Popup Detail Group
26. Buka elipsis Node XF, pilih Edit, pilih Function `None`, klik [Save]
27. Klik [Save] pada Dialog Change Function
28. Tunggu aksi selesai
29. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
30. Verifikasi aset dan histori yang menunjuk node XF tidak berpindah, terkunci, atau terhapus dibanding catatan sebelum perubahan Function
31. Tutup Popup Detail Group
32. Buka Fixed Asset > Register Asset
33. Buka field Group Register Asset
34. Verifikasi sedikitnya satu opsi group lain tampil di field Group Register Asset
35. Verifikasi node XF hilang dari pilihan pada field Group Register Asset
36. Buka Fixed Asset > Transfer
37. Buka field tujuan Transfer
38. Verifikasi sedikitnya satu opsi group lain tampil di field tujuan Transfer
39. Verifikasi node XF hilang dari pilihan pada field tujuan Transfer

## Notes

- Langkah penghubung (S-03): membuka Fixed Asset > Settings > Groups di awal tiap blok (S-14; blok sebelumnya berakhir di form modul konsumen), mengatur Function awal lewat sesi API, dan Tunggu aksi selesai (8b butir 8). Navigasi ke modul konsumen (S-14): Buka Fixed Asset > Register Asset dan > Transfer sebelum membuka field atau dropdown, karena field itu milik form modul masing-masing. Pembanding "tidak berpindah, terkunci, atau terhapus" (S-12): Group, status, dan jumlah aset node XF (termasuk aset Disposed) dicatat dari Popup Detail Group Tab Assets sebelum perubahan Function, lalu dibaca ulang dari Popup yang sama sesudahnya dan ditutup sebelum pindah modul. Baris target dicari lewat Search nama bersuffix (client memiliki lebih dari 10 node level 1 dan page size 10; S-03, R-16). Asersi tambahan (S-03): sebelum asersi absence ("hilang dari pilihan") ada Verifikasi sedikitnya satu opsi group lain tampil di dropdown yang sama sebagai anchor positif (8b butir 2); TC tidak memintanya.
- Spec memiliki 39 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (efek perubahan Function ke dropdown konsumen) pada node yang sama; kedua transisi dipisah sebagai dua blok yang berdiri sendiri tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC-896 dan 898 menulis "(konfirmasi dialog bila muncul)" dan "aset existing di node (bila Assignable)"; spec memisahkan transisi tanpa dan dengan dialog, dan memakai node dengan aset aktif serta riwayat sekaligus.
  - TC tidak menyebut cara mengamati histori pada node; spec membaca aset Disposed lewat Tab Assets Popup Detail Group.
  - Field "Group Register Asset" dan "tujuan Transfer" diverifikasi pada pilihan dropdown; TC tidak menyebut langkah rinci membuka form Register Asset dan Transfer.
