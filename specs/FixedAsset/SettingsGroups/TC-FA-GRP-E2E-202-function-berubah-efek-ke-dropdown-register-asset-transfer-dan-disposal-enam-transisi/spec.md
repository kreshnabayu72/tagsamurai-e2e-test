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

1. Untuk setiap baris tabel Transisi tanpa Dialog Change Function (langkah 1 sampai 11): Buka Fixed Asset > Settings > Groups
2. Atur Function Node XF ke nilai kolom Dari lewat sesi API hingga tersimpan
3. Buka elipsis Node XF, pilih Edit, pilih Function kolom Ke, klik [Save]
4. Tunggu aksi selesai
5. Buka field Group Register Asset dan field tujuan Transfer
6. Verifikasi sedikitnya satu opsi group lain tampil di field Group Register Asset dan field tujuan Transfer
7. Verifikasi node XF sesuai kolom Register Asset dan Transfer
8. Buka dropdown tujuan Disposal
9. Verifikasi sedikitnya satu opsi group lain tampil di dropdown tujuan Disposal
10. Verifikasi node XF sesuai kolom Tujuan Disposal
11. Verifikasi aset dan histori disposal yang menunjuk node XF tidak berpindah, terkunci, atau terhapus
12. Untuk setiap baris tabel Transisi dengan Dialog Change Function (langkah 12 sampai 23): Buka Fixed Asset > Settings > Groups
13. Atur Function Node XF ke nilai kolom Dari lewat sesi API hingga tersimpan
14. Buka elipsis Node XF, pilih Edit, pilih Function kolom Ke, klik [Save]
15. Klik [Save] pada Dialog Change Function
16. Tunggu aksi selesai
17. Buka field Group Register Asset dan field tujuan Transfer
18. Verifikasi sedikitnya satu opsi group lain tampil di field Group Register Asset dan field tujuan Transfer
19. Verifikasi node XF sesuai kolom Register Asset dan Transfer
20. Buka dropdown tujuan Disposal
21. Verifikasi sedikitnya satu opsi group lain tampil di dropdown tujuan Disposal
22. Verifikasi node XF sesuai kolom Tujuan Disposal
23. Verifikasi aset dan histori disposal yang menunjuk node XF tidak berpindah, terkunci, atau terhapus

## Notes

- Langkah 1 sampai 11 berulang untuk dua baris tabel pertama; langkah 12 sampai 23 berulang untuk empat baris tabel kedua (8b butir 7). Langkah penghubung (S-03): membuka Fixed Asset > Settings > Groups di awal tiap iterasi (S-14; iterasi sebelumnya berakhir di form modul konsumen), mengatur Function awal lewat sesi API, dan Tunggu aksi selesai (8b butir 8). Asersi tambahan (S-03): sebelum asersi absence atau "tetap tidak muncul" ada Verifikasi sedikitnya satu opsi group lain tampil di dropdown yang sama sebagai anchor positif (8b butir 2); TC tidak memintanya.
- Spec memiliki 23 langkah nominal dan 70 langkah setelah ekspansi, di atas smell 35 langkah. Alasan: seluruh blok satu topik (efek perubahan Function ke dropdown konsumen) pada node yang sama; langkah tiap transisi identik sehingga ekspansi berasal dari perulangan per transisi tanpa langkah bersyarat (8b butir 7).
- Temuan untuk QA:
  - TC-896 sampai 901 menulis "(konfirmasi dialog bila muncul)" dan "aset existing di node (bila Assignable) atau histori disposal (bila Disposal Group)"; spec memisahkan transisi tanpa dan dengan dialog, dan memakai node dengan aset aktif serta histori disposal sekaligus.
  - Field "Group Register Asset" dan "tujuan Transfer" serta "tujuan Disposal" diverifikasi pada pilihan dropdown; TC tidak menyebut langkah rinci membuka form Register Asset, Transfer, dan Disposal.
