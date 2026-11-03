---
id: TC-FA-GRP-E2E-225-tab-assets-setup-column-geser-drag-kolom-name-asset-id-status-dan-last-updated
title: "Tab Assets Setup Column: Geser (Drag) Kolom Name, Asset ID, Status, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-710
  - TC-FA-GRP-711
  - TC-FA-GRP-712
  - TC-FA-GRP-713
coverage:
  web: automated
---

# Tab Assets Setup Column: Geser (Drag) Kolom Name, Asset ID, Status, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi status, ditambah 2 Disposed) pada pohon group Tabel A. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal (urutan Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated).
- Setup Column: spec menyimpan konfigurasi kolom Tab Assets (`[Save]` pada langkah 8). Pemulihan tiap iterasi (langkah 14 dan 17) dan hook `after` menghapus preferensi kolom Tab Assets di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Tabel iterasi "Kolom uji" (posisi tujuan dan urutan kolom tabel yang diharapkan; posisi tujuan dipilih spec karena TC hanya menyebut "posisi lain"):

| Kolom | Posisi tujuan | Urutan kolom sesudah drag |
|---|---|---|
| Name | tepat sesudah Asset ID | Asset ID, Name, TAG, Brand, Model/Type, Status, Last Updated |
| Asset ID | paling atas | Asset ID, Name, TAG, Brand, Model/Type, Status, Last Updated |
| Status | paling atas | Status, Name, Asset ID, TAG, Brand, Model/Type, Last Updated |
| Last Updated | paling atas | Last Updated, Name, Asset ID, TAG, Brand, Model/Type, Status |

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Untuk setiap baris tabel "Kolom uji" (langkah 4 sampai 17) dengan `<Kolom>`, `<Posisi tujuan>`, dan `<Urutan>` sebagai nilai baris:
4. Klik icon (⋯) pada header kolom terakhir
5. Klik [Setup Column]
6. Drag `<Kolom>` ke `<Posisi tujuan>`
7. Verifikasi urutan Live Preview mengikuti posisi baru (`<Urutan>`)
8. Klik [Save]
9. Verifikasi urutan kolom tabel berubah menjadi `<Urutan>`
10. Refresh F5
11. Ketik Search `Warehouse A`, tekan Enter
12. Klik angka Total Asset Warehouse A
13. Verifikasi urutan kolom tabel tetap `<Urutan>` setelah F5
14. Hapus preferensi kolom Tab Assets di browser
15. Refresh F5
16. Ketik Search `Warehouse A`, tekan Enter
17. Klik angka Total Asset Warehouse A

## Notes

- Langkah 4 sampai 17 diulang untuk 4 kolom pada tabel "Kolom uji"; pemetaan baris ke TC: Name (TC-FA-GRP-710), Asset ID (TC-FA-GRP-711), Status (TC-FA-GRP-712), Last Updated (TC-FA-GRP-713).
- Langkah penghubung (S-03): langkah 12 dan 17 membuka ulang Detail Warehouse A sesudah F5; langkah 14 memulihkan preferensi kolom sebelum iterasi berikutnya.
- Langkah 8 `[Save]` Setup Column adalah aksi sisi klien tanpa Tunggu aksi selesai (8b butir 8).
- Alasan di atas 35 langkah (ekspansi 4 iterasi x 14 langkah + 3): empat iterasi satu kelas (Setup Column Tab Assets), parameter tiap iterasi hanya kolom dan posisi tujuan, dan tiap iterasi berdiri sendiri karena preferensi dipulihkan di langkah 14 (8b butir 7).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-710 sampai 713 Langkah 4 "Drag ... ke posisi lain" tidak menyebut posisi tujuan; spec memilih posisi pada tabel iterasi.
  - TC-FA-GRP-710 sampai 713 Expected b tidak menyebut apakah Popup Detail Group tetap terbuka setelah F5; spec membuka ulang Detail Warehouse A (langkah 12).
