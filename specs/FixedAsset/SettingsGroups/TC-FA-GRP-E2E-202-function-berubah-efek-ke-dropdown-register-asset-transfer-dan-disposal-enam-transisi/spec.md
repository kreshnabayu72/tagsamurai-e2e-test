---
id: TC-FA-GRP-E2E-202-function-berubah-efek-ke-dropdown-register-asset-transfer-dan-disposal-enam-transisi
title: "Perubahan Function (Enam Transisi) dan Efeknya ke Dropdown Register Asset, Transfer, dan Disposal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-896
  - TC-FA-GRP-897
  - TC-FA-GRP-898
  - TC-FA-GRP-899
  - TC-FA-GRP-900
  - TC-FA-GRP-901
coverage:
  web: automated
---

# Perubahan Function (Enam Transisi) dan Efeknya ke Dropdown Register Asset, Transfer, dan Disposal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan No 3, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix): node level 1 `Node XF {runId}-202` yang punya satu aset aktif (Available) dan satu riwayat disposal (aset Disposed) sehingga kedua klausa "aset/histori tidak berpindah" dapat diamati pada Function mana pun. Function awal diatur lewat sesi API aktor pada langkah awal tiap iterasi (R-20).
- Dialog Change Function muncul pada empat transisi yang melepas Assignable atau Disposal Group (tabel kedua); dua transisi dari None langsung tersimpan tanpa dialog (tabel pertama). Karena itu kedua kelompok ditulis sebagai dua perulangan terpisah tanpa langkah bersyarat.
- Transisi tanpa Dialog Change Function:

  | Dari | Ke | Register Asset dan Transfer | Tujuan Disposal |
  |---|---|---|---|
  | None | Assignable | muncul sebagai pilihan baru | tetap tidak muncul |
  | None | Disposal Group | tetap tidak muncul | muncul sebagai pilihan baru |

- Transisi dengan Dialog Change Function:

  | Dari | Ke | Register Asset dan Transfer | Tujuan Disposal |
  |---|---|---|---|
  | Assignable | None | hilang dari pilihan | tetap tidak muncul |
  | Assignable | Disposal Group | hilang dari pilihan | muncul sebagai pilihan baru |
  | Disposal Group | None | tetap tidak muncul | hilang dari pilihan |
  | Disposal Group | Assignable | muncul sebagai pilihan baru | hilang dari pilihan |

## Test Steps

1. Untuk setiap baris tabel Transisi tanpa Dialog Change Function (langkah 1 sampai 23): Buka Fixed Asset > Settings > Groups
2. Atur Function Node XF ke nilai kolom Dari lewat sesi API hingga tersimpan
3. Ketik Search `Node XF {runId}-202`, tekan Enter
4. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
5. Catat Group, status, dan jumlah aset node XF (termasuk aset Disposed) sebagai pembanding sebelum perubahan Function
6. Tutup Popup Detail Group
7. Buka elipsis Node XF, pilih Edit, pilih Function kolom Ke, klik [Save]
8. Tunggu aksi selesai
9. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
10. Verifikasi aset dan histori disposal yang menunjuk node XF tidak berpindah, terkunci, atau terhapus dibanding catatan sebelum perubahan Function
11. Tutup Popup Detail Group
12. Buka Fixed Asset > Register Asset
13. Buka field Group Register Asset
14. Verifikasi sedikitnya satu opsi group lain tampil di field Group Register Asset
15. Verifikasi node XF sesuai kolom Register Asset dan Transfer pada field Group Register Asset
16. Buka Fixed Asset > Transfer
17. Buka field tujuan Transfer
18. Verifikasi sedikitnya satu opsi group lain tampil di field tujuan Transfer
19. Verifikasi node XF sesuai kolom Register Asset dan Transfer pada field tujuan Transfer
20. Buka Fixed Asset > Disposal
21. Buka dropdown tujuan Disposal
22. Verifikasi sedikitnya satu opsi group lain tampil di dropdown tujuan Disposal
23. Verifikasi node XF sesuai kolom Tujuan Disposal
24. Untuk setiap baris tabel Transisi dengan Dialog Change Function (langkah 24 sampai 47): Buka Fixed Asset > Settings > Groups
25. Atur Function Node XF ke nilai kolom Dari lewat sesi API hingga tersimpan
26. Ketik Search `Node XF {runId}-202`, tekan Enter
27. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
28. Catat Group, status, dan jumlah aset node XF (termasuk aset Disposed) sebagai pembanding sebelum perubahan Function
29. Tutup Popup Detail Group
30. Buka elipsis Node XF, pilih Edit, pilih Function kolom Ke, klik [Save]
31. Klik [Save] pada Dialog Change Function
32. Tunggu aksi selesai
33. Klik angka Total Asset Node XF untuk membuka Popup Detail Group, Tab Assets
34. Verifikasi aset dan histori disposal yang menunjuk node XF tidak berpindah, terkunci, atau terhapus dibanding catatan sebelum perubahan Function
35. Tutup Popup Detail Group
36. Buka Fixed Asset > Register Asset
37. Buka field Group Register Asset
38. Verifikasi sedikitnya satu opsi group lain tampil di field Group Register Asset
39. Verifikasi node XF sesuai kolom Register Asset dan Transfer pada field Group Register Asset
40. Buka Fixed Asset > Transfer
41. Buka field tujuan Transfer
42. Verifikasi sedikitnya satu opsi group lain tampil di field tujuan Transfer
43. Verifikasi node XF sesuai kolom Register Asset dan Transfer pada field tujuan Transfer
44. Buka Fixed Asset > Disposal
45. Buka dropdown tujuan Disposal
46. Verifikasi sedikitnya satu opsi group lain tampil di dropdown tujuan Disposal
47. Verifikasi node XF sesuai kolom Tujuan Disposal

## Notes

- Langkah 1 sampai 23 berulang untuk dua baris tabel pertama; langkah 24 sampai 47 berulang untuk empat baris tabel kedua (8b butir 7). Langkah penghubung (S-03): membuka Fixed Asset > Settings > Groups di awal tiap iterasi (S-14; iterasi sebelumnya berakhir di form modul konsumen), mengatur Function awal lewat sesi API, dan Tunggu aksi selesai (8b butir 8). Navigasi ke modul konsumen (S-14): Buka Fixed Asset > Register Asset, > Transfer, dan > Disposal sebelum membuka field atau dropdown, karena field itu milik form modul masing-masing. Pembanding "tidak berpindah, terkunci, atau terhapus" (S-12): Group, status, dan jumlah aset node XF (termasuk aset Disposed) dicatat dari Popup Detail Group Tab Assets sebelum perubahan Function, lalu dibaca ulang dari Popup yang sama sesudahnya dan ditutup sebelum pindah modul. Baris target dicari lewat Search nama bersuffix (client memiliki lebih dari 10 node level 1 dan page size 10; S-03, R-16). Asersi tambahan (S-03): sebelum asersi absence atau "tetap tidak muncul" ada Verifikasi sedikitnya satu opsi group lain tampil di dropdown yang sama sebagai anchor positif (8b butir 2); TC tidak memintanya.
- Spec memiliki 47 langkah nominal dan 142 langkah setelah ekspansi, di atas smell 35 langkah. Alasan: seluruh blok satu topik (efek perubahan Function ke dropdown konsumen) pada node yang sama; langkah tiap transisi identik sehingga ekspansi berasal dari perulangan per transisi tanpa langkah bersyarat (8b butir 7).
- Temuan untuk QA:
  - TC-896 sampai 901 menulis "(konfirmasi dialog bila muncul)" dan "aset existing di node (bila Assignable) atau histori disposal (bila Disposal Group)"; spec memisahkan transisi tanpa dan dengan dialog, dan memakai node dengan aset aktif serta histori disposal sekaligus.
  - TC tidak menyebut cara mengamati histori disposal pada node; spec membaca aset Disposed lewat Tab Assets Popup Detail Group.
  - Field "Group Register Asset" dan "tujuan Transfer" serta "tujuan Disposal" diverifikasi pada pilihan dropdown; TC tidak menyebut langkah rinci membuka form Register Asset, Transfer, dan Disposal.
