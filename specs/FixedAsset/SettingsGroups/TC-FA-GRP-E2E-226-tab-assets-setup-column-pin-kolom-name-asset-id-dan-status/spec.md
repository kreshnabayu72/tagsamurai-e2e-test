---
id: TC-FA-GRP-E2E-226-tab-assets-setup-column-pin-kolom-name-asset-id-dan-status
title: "Tab Assets Setup Column: Pin Kolom Name, Asset ID, dan Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-714
  - TC-FA-GRP-715
  - TC-FA-GRP-716
coverage:
  web: automated
---

# Tab Assets Setup Column: Pin Kolom Name, Asset ID, dan Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal.
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 8, 12, dan 18); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 6 dan 16). Tiap iterasi mengakhiri dengan unpin sehingga konfigurasi kembali tanpa pin; hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom uji":

| Kolom |
|---|
| Name |
| Asset ID |
| Status |

## Test Steps

1. Klik angka Total Asset Warehouse A
2. Untuk setiap baris tabel "Kolom uji" (langkah 3 sampai 19) dengan `<Kolom>` sebagai nilai baris:
3. Klik icon (⋯) pada header kolom terakhir
4. Klik [Setup Column]
5. Klik icon Pin `<Kolom>`
6. Klik [Save]
7. Scroll tabel horizontal ke kanan
8. Verifikasi kolom `<Kolom>` membeku (sticky) saat scroll horizontal
9. Refresh F5
10. Klik angka Total Asset Warehouse A
11. Scroll tabel horizontal ke kanan
12. Verifikasi pin kolom `<Kolom>` bertahan setelah F5 (kolom tetap membeku)
13. Klik icon (⋯) pada header kolom terakhir
14. Klik [Setup Column]
15. Klik icon Pin `<Kolom>` untuk unpin
16. Klik [Save]
17. Scroll tabel horizontal ke kanan
18. Verifikasi kolom `<Kolom>` ikut scroll (tidak membeku) setelah unpin
19. Scroll tabel horizontal kembali ke kiri

## Notes

- Langkah 3 sampai 19 diulang untuk 3 kolom pada tabel "Kolom uji"; pemetaan baris ke TC: Name (TC-FA-GRP-714), Asset ID (TC-FA-GRP-715), Status (TC-FA-GRP-716).
- Langkah penghubung (S-03): langkah 10 membuka ulang Detail Warehouse A sesudah F5; langkah 11, 17, dan 19 mengatur posisi scroll (scroll kembali ke kiri sebelum iterasi berikutnya); langkah 13 sampai 16 adalah Langkah 8 TC ("Unpin lagi lalu [Save]").
- Langkah 6 dan 16 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Alasan di atas 35 langkah (ekspansi 3 iterasi x 17 langkah + 1 = 52): tiga iterasi satu kelas (Setup Column Tab Assets), parameter tiap iterasi hanya nama kolom, dan tiap iterasi berdiri sendiri karena berakhir dengan unpin (8b butir 7).
- Temuan untuk QA:
  - TC-FA-GRP-714 sampai 716 Expected b tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A (langkah 10).
  - TC-FA-GRP-714 sampai 716 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport atau jumlah kolom; spec menyatakannya sebagai kemampuan tim FE di Prerequisites.
