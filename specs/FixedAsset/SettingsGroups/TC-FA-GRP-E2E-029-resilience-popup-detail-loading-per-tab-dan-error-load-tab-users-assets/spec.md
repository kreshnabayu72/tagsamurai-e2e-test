---
id: TC-FA-GRP-E2E-029-resilience-popup-detail-loading-per-tab-dan-error-load-tab-users-assets
title: "Resilience Popup Detail: Loading per Tab dan Error Load Tab Users/Tab Assets Tidak Memengaruhi Tab Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-282
  - TC-FA-GRP-283
  - TC-FA-GRP-291
  - TC-FA-GRP-298
coverage:
  web: automated
---

# Resilience Popup Detail: Loading per Tab dan Error Load Tab Users/Tab Assets Tidak Memengaruhi Tab Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9) dengan Warehouse A (24 aset aktif, sedikitnya satu user). Spec ini tidak menjalankan aksi tulis.
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk (a) menahan respons request data Tab Users (TC-FA-GRP-282, menahan respons hanya untuk mengamati Loading) dan (b) memaksa respons 5xx pada request data Tab Users atau Tab Assets (TC-FA-GRP-283, 291, 298). Tiap intercept dilepas segera setelah pemicunya selesai dan dilepas di hook `after` bila spec gagal di tengah. Fixture BE dan sesi API aktor disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-282: Loading per tab

1. Ketik Search `Warehouse A`, tekan Enter
2. Tahan respons request data Tab Users dengan intercept
3. Klik nama Warehouse A
4. Klik Tab Users
5. Verifikasi Loading component tampil hanya di area tabel Tab Users
6. Verifikasi header popup, toolbar, dan Tab Assets tetap tampil
7. Lepas tahanan respons
8. Tutup popup dengan [X]

### TC-FA-GRP-283: Error load Tab Users tidak memengaruhi tab lain

9. Paksa respons 5xx pada request data Tab Users dengan intercept
10. Klik nama Warehouse A
11. Klik Tab Users
12. Verifikasi Tab Users menampilkan `Unable to load this data.` beserta tombol [Try Again]
13. Klik Tab Assets
14. Verifikasi Tab Assets tampil normal dengan baris data
15. Lepas intercept 5xx
16. Klik Tab Users
17. Klik [Try Again]
18. Verifikasi Tab Users memuat ulang dan menampilkan baris data
19. Tutup popup dengan [X]

### TC-FA-GRP-291: Error load Tab Assets

20. Paksa respons 5xx pada request data Tab Assets dengan intercept
21. Klik angka Total Asset Warehouse A
22. Verifikasi area tabel Tab Assets menampilkan `Unable to load this data.` beserta tombol [Try Again]
23. Verifikasi header popup dan Tab Users tetap tampil
24. Lepas intercept 5xx
25. Klik [Try Again]
26. Verifikasi Tab Assets memuat data dan menampilkan baris data
27. Tutup popup dengan [X]

### TC-FA-GRP-298: Tab Users read-only, error load

28. Paksa respons 5xx pada request data Tab Users dengan intercept
29. Klik angka Total User Warehouse A
30. Verifikasi area tabel Tab Users menampilkan `Unable to load this data.` beserta tombol [Try Again]
31. Verifikasi Tab Users tidak memiliki aksi tulis
32. Lepas intercept 5xx
33. Klik [Try Again]
34. Verifikasi Tab Users memuat data dan menampilkan baris data
35. Tutup popup dengan [X]

## Notes

- Spec 35 langkah, pada batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 7, 15, 24, 32 (melepas intercept segera setelah pemicu selesai, S-09), langkah 8, 19, 27, 35 (menutup popup). Langkah 1 (Ketik Search `Warehouse A`, tekan Enter, sebelum intercept dipasang) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; Search tetap aktif selama popup dibuka dan ditutup (R-16).
- Kelas b: kegagalan 5xx dipaksa lewat intercept parsial di atas backend nyata sehingga spec ditandai `FE+BE`, bukan `Mode: mock` (bagian 6 konvensi). TC-FA-GRP-282 menahan respons hanya untuk mengamati Loading (bukan kelas b) dan berada di spec ini bersama TC-FA-GRP-283 pada permukaan yang sama.
- Urutan TC dalam spec: 282, 283, 291, 298.
- Temuan untuk QA:
  - TC-FA-GRP-282, 283, 291, 298 menyebut "endpoint Tab Users/data tab 5xx" tanpa nama endpoint; spec mengintercept request data tab tanpa menyebut endpoint (S-13).
  - TC-FA-GRP-298 butir a ("tidak ada aksi tulis") tidak menyebut aksi yang dicek; spec mengasersi tidak adanya aksi tulis pada tab.
