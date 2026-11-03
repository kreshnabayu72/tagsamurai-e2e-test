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
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 8). Pemulihan tiap iterasi (langkah 15) dan hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom uji":

| Kolom |
|---|
| Name |
| Asset ID |
| Status |
| Last Updated |

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Untuk setiap baris tabel "Kolom uji" (langkah 4 sampai 18) dengan `<Kolom>` sebagai nilai baris:
4. Klik icon (⋯) pada header kolom terakhir
5. Klik [Setup Column]
6. Uncheck `<Kolom>`
7. Verifikasi Live Preview langsung menyembunyikan `<Kolom>`
8. Klik [Save]
9. Verifikasi kolom `<Kolom>` hilang dari tabel
10. Refresh F5
11. Ketik Search `Warehouse A`, tekan Enter
12. Klik angka Total Asset Warehouse A
13. Verifikasi tabel menampilkan sedikitnya satu kolom lain
14. Verifikasi kolom `<Kolom>` tetap tidak ada pada tabel setelah F5
15. Hapus preferensi kolom Tab Assets di browser
16. Refresh F5
17. Ketik Search `Warehouse A`, tekan Enter
18. Klik angka Total Asset Warehouse A

## Notes

- Langkah 4 sampai 18 diulang untuk 4 kolom pada tabel "Kolom uji"; pemetaan baris ke TC: Name (TC-FA-GRP-706), Asset ID (TC-FA-GRP-707), Status (TC-FA-GRP-708), Last Updated (TC-FA-GRP-709).
- Langkah penghubung (S-03): langkah 12 membuka ulang Detail Warehouse A sesudah F5; langkah 15 memulihkan preferensi kolom sebelum iterasi berikutnya.
- Langkah 8 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Alasan di atas 35 langkah (ekspansi 4 iterasi x 15 langkah + 3): empat iterasi satu kelas (Setup Column Tab Assets), parameter tiap iterasi hanya nama kolom, dan tiap iterasi berdiri sendiri karena preferensi dipulihkan di langkah 15 (8b butir 7).
- Langkah 13 menjadi anchor positif untuk absence pada langkah 14.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-706 sampai 709 Expected c "Konfigurasi bertahan setelah F5" tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A (langkah 12).
