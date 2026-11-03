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
- Viewport: hook `before` mengatur lebar viewport sehingga tabel Tab Assets dapat di-scroll horizontal (asersi sticky pada langkah 9, 14, dan 20); hook `after` memulihkan viewport (kemampuan disediakan tim FE).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 7 dan 18). Tiap iterasi mengakhiri dengan unpin sehingga konfigurasi kembali tanpa pin; hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom uji":

| Kolom |
|---|
| Name |
| Asset ID |
| Status |

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Untuk setiap baris tabel "Kolom uji" (langkah 4 sampai 21) dengan `<Kolom>` sebagai nilai baris:
4. Klik icon (⋯) pada header kolom terakhir
5. Klik [Setup Column]
6. Klik icon Pin `<Kolom>`
7. Klik [Save]
8. Scroll tabel horizontal ke kanan
9. Verifikasi kolom `<Kolom>` membeku (sticky) saat scroll horizontal
10. Refresh F5
11. Ketik Search `Warehouse A`, tekan Enter
12. Klik angka Total Asset Warehouse A
13. Scroll tabel horizontal ke kanan
14. Verifikasi pin kolom `<Kolom>` bertahan setelah F5 (kolom tetap membeku)
15. Klik icon (⋯) pada header kolom terakhir
16. Klik [Setup Column]
17. Klik icon Pin `<Kolom>` untuk unpin
18. Klik [Save]
19. Scroll tabel horizontal ke kanan
20. Verifikasi kolom `<Kolom>` ikut scroll (tidak membeku) setelah unpin
21. Scroll tabel horizontal kembali ke kiri

## Notes

- Langkah 4 sampai 21 diulang untuk 3 kolom pada tabel "Kolom uji"; pemetaan baris ke TC: Name (TC-FA-GRP-714), Asset ID (TC-FA-GRP-715), Status (TC-FA-GRP-716).
- Langkah penghubung (S-03): langkah 12 membuka ulang Detail Warehouse A sesudah F5; langkah 13, 19, dan 21 mengatur posisi scroll (scroll kembali ke kiri sebelum iterasi berikutnya); langkah 15 sampai 18 adalah Langkah 8 TC ("Unpin lagi lalu [Save]").
- Langkah 7 dan 18 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Alasan di atas 35 langkah (ekspansi 3 iterasi x 18 langkah + 3 = 57): tiga iterasi satu kelas (Setup Column Tab Assets), parameter tiap iterasi hanya nama kolom, dan tiap iterasi berdiri sendiri karena berakhir dengan unpin (8b butir 7).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-714 sampai 716 Expected b tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A (langkah 12).
  - TC-FA-GRP-714 sampai 716 mensyaratkan tabel dapat di-scroll horizontal tanpa menyebut kebutuhan lebar viewport atau jumlah kolom; spec menyatakannya sebagai kemampuan tim FE di Prerequisites.
