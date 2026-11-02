---
id: TC-FA-GRP-E2E-224-tab-assets-setup-column-uncheck-kolom-name-asset-id-status-dan-last-updated
title: "Tab Assets Setup Column: Uncheck Kolom Name, Asset ID, Status, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-706
  - TC-FA-GRP-707
  - TC-FA-GRP-708
  - TC-FA-GRP-709
coverage:
  web: automated
---

# Tab Assets Setup Column: Uncheck Kolom Name, Asset ID, Status, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated tampil).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 7). Pemulihan tiap iterasi (langkah 13) dan hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom uji":

| Kolom |
|---|
| Name |
| Asset ID |
| Status |
| Last Updated |

## Test Steps

1. Klik angka Total Asset Warehouse A
2. Untuk setiap baris tabel "Kolom uji" (langkah 3 sampai 13) dengan `<Kolom>` sebagai nilai baris:
3. Klik icon (⋯) pada header kolom terakhir
4. Klik [Setup Column]
5. Uncheck `<Kolom>`
6. Verifikasi Live Preview langsung menyembunyikan `<Kolom>`
7. Klik [Save]
8. Verifikasi kolom `<Kolom>` hilang dari tabel
9. Refresh F5
10. Klik angka Total Asset Warehouse A
11. Verifikasi tabel menampilkan sedikitnya satu kolom lain
12. Verifikasi kolom `<Kolom>` tetap tidak ada pada tabel setelah F5
13. Hapus preferensi kolom Tab Assets di browser, Refresh F5, lalu klik angka Total Asset Warehouse A

## Notes

- Langkah 3 sampai 13 diulang untuk 4 kolom pada tabel "Kolom uji"; pemetaan baris ke TC: Name (TC-FA-GRP-706), Asset ID (TC-FA-GRP-707), Status (TC-FA-GRP-708), Last Updated (TC-FA-GRP-709).
- Langkah penghubung (S-03): langkah 10 membuka ulang Detail Warehouse A sesudah F5; langkah 13 memulihkan preferensi kolom sebelum iterasi berikutnya.
- Langkah 7 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Alasan di atas 35 langkah (ekspansi 4 iterasi x 11 langkah + 2): empat iterasi satu kelas (Setup Column Tab Assets), parameter tiap iterasi hanya nama kolom, dan tiap iterasi berdiri sendiri karena preferensi dipulihkan di langkah 13 (8b butir 7).
- Langkah 11 menjadi anchor positif untuk absence pada langkah 12.
- Temuan untuk QA:
  - TC-FA-GRP-706 sampai 709 Expected c "Konfigurasi bertahan setelah F5" tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A (langkah 10).
