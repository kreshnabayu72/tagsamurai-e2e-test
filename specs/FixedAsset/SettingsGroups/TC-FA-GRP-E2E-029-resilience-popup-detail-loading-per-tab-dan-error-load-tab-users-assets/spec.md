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

1. Tahan respons request data Tab Users dengan intercept
2. Klik nama Warehouse A
3. Klik Tab Users
4. Verifikasi Loading component tampil hanya di area tabel Tab Users
5. Verifikasi header popup, toolbar, dan Tab Assets tetap tampil
6. Lepas tahanan respons
7. Tutup popup dengan [X]

### TC-FA-GRP-283: Error load Tab Users tidak memengaruhi tab lain

8. Paksa respons 5xx pada request data Tab Users dengan intercept
9. Klik nama Warehouse A
10. Klik Tab Users
11. Verifikasi Tab Users menampilkan `Unable to load this data.` beserta tombol [Try Again]
12. Klik Tab Assets
13. Verifikasi Tab Assets tampil normal dengan baris data
14. Lepas intercept 5xx
15. Klik Tab Users
16. Klik [Try Again]
17. Verifikasi Tab Users memuat ulang dan menampilkan baris data
18. Tutup popup dengan [X]

### TC-FA-GRP-291: Error load Tab Assets

19. Paksa respons 5xx pada request data Tab Assets dengan intercept
20. Klik angka Total Asset Warehouse A
21. Verifikasi area tabel Tab Assets menampilkan `Unable to load this data.` beserta tombol [Try Again]
22. Verifikasi header popup dan Tab Users tetap tampil
23. Lepas intercept 5xx
24. Klik [Try Again]
25. Verifikasi Tab Assets memuat data dan menampilkan baris data
26. Tutup popup dengan [X]

### TC-FA-GRP-298: Tab Users read-only, error load

27. Paksa respons 5xx pada request data Tab Users dengan intercept
28. Klik angka Total User Warehouse A
29. Verifikasi area tabel Tab Users menampilkan `Unable to load this data.` beserta tombol [Try Again]
30. Verifikasi Tab Users tidak memiliki aksi tulis
31. Lepas intercept 5xx
32. Klik [Try Again]
33. Verifikasi Tab Users memuat data dan menampilkan baris data
34. Tutup popup dengan [X]

## Notes

- Spec 34 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 6, 14, 23, 31 (melepas intercept segera setelah pemicu selesai, S-09), langkah 7, 18, 26, 34 (menutup popup).
- Kelas b: kegagalan 5xx dipaksa lewat intercept parsial di atas backend nyata sehingga spec ditandai `FE+BE`, bukan `Mode: mock` (bagian 6 konvensi). TC-FA-GRP-282 menahan respons hanya untuk mengamati Loading (bukan kelas b) dan berada di spec ini bersama TC-FA-GRP-283 pada permukaan yang sama.
- Urutan TC dalam spec: 282, 283, 291, 298.
- Temuan untuk QA:
  - TC-FA-GRP-282, 283, 291, 298 menyebut "endpoint Tab Users/data tab 5xx" tanpa nama endpoint; spec mengintercept request data tab tanpa menyebut endpoint (S-13).
  - TC-FA-GRP-298 butir a ("tidak ada aksi tulis") tidak menyebut aksi yang dicek; spec mengasersi tidak adanya aksi tulis pada tab.
