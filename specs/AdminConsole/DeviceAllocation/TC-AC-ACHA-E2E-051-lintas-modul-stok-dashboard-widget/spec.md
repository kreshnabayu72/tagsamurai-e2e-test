---
id: TC-AC-ACHA-E2E-051-lintas-modul-stok-dashboard-widget
title: "Konsumen Lintas Modul: Stok Fisik, Client Dashboard, Widget Pending Device Allocation, dan Kuota Client Suspended"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-399
  - TC-AC-ACHA-400
  - TC-AC-ACHA-401
  - TC-AC-ACHA-402
coverage:
  web: automated
---

# Konsumen Lintas Modul: Stok Fisik, Client Dashboard, Widget Pending Device Allocation, dan Kuota Client Suspended

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor `totalControlDistributor_automated_qaTeam1@qwertysystem.net` (Pre-setup #27, Hendra Wibowo), password `Spectra.env.AC_DA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: Group Member Distributor `memberOnDistributor_automated_qaTeam1@qwertysystem.net` (Pre-setup #32, Budi Santoso, MB_ON) hanya memicu perubahan state (Submit dan Cancel) lewat sesi API aktor, password `Spectra.env.AC_DA_MB_ON_PASSWORD`; hasilnya diamati di sesi UI Hendra Wibowo.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #7 Client PT Sejahtera Logistik (Active, binaan langsung PT Global Distribusi), #14 harga produk dan #16 kantong PT Global Distribusi saldo $20,000.00 (saldo dan harga cukup untuk Submit alokasi `TAG - BLE` dan Approve).
- Data seeding milik spec (fixture API disediakan tim FE/BE; salinan milik spec dari Pre-setup #49): satu transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00) untuk TC-AC-ACHA-400. Allocation ID tiap salinan ditangkap dari respons fixture seeding (Dynamic Reference) dan dipakai sebagai penanda Search, asersi, dan cleanup hook `after`. Data lain dibuat spec lewat UI atau sesi API dengan Category `TAG - BLE`.
- Kemampuan teknis: halaman Hardware Stock dan TAG Stock (membaca stok fisik pengirim), Client Dashboard PT Sejahtera Logistik (membaca kuota BLE), Dashboard (widget Pending Device Allocation), dan Approvals > Device Allocation; fixture baca kuota Client PT Sejahtera Logistik bila halaman Client Dashboard tidak menampilkan angka eksak (disediakan tim FE/BE).
- Pemulihan dan efek (R-08, S-06): transaksi yang dibuat spec tidak dapat dihapus lewat UI. Transaksi Waiting for Approval BLE Quantity 30 (langkah 16) tetap Waiting sampai hook `after`; hook `after` membatalkannya, memulihkan saldo dan Reserve kantong PT Global Distribusi, kuota Client PT Sejahtera Logistik, dan seed ke 30 baris lewat fixture yang disediakan tim FE/BE. Pre-setup bersama tidak diubah selain saldo, Reserve, dan kuota itu.
- Suite berjalan serial (`parallel: false`): kuota Client dan jumlah widget adalah state bersama yang dibaca dengan selisih terhadap angka yang dicatat sebelum aksi (S-12).

## Test Steps

### TC-AC-ACHA-399: Alokasi langsung tidak mengurangi stok fisik pengirim

1. Buka halaman TAG Stock dan Hardware Stock, lalu catat stok BLE pengirim PT Global Distribusi pada masing-masing halaman sebagai stok awal
2. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu tunggu toast sukses
3. Buka halaman TAG Stock dan bandingkan stok BLE pengirim dengan stok awal
4. Verifikasi stok fisik BLE pengirim pada TAG Stock tidak berubah (alokasi hanya mendistribusikan kuota hak guna)
5. Buka halaman Hardware Stock dan bandingkan stok pengirim dengan stok awal
6. Verifikasi stok pada Hardware Stock tidak berubah

### TC-AC-ACHA-400: Approve tidak mengurangi stok fisik pengirim

7. Buka halaman TAG Stock, lalu catat stok RFID Object TAG pengirim PT Global Distribusi sebagai stok awal
8. Buka Approvals > Device Allocation, klik `[Approve]` pada transaksi Waiting for Approval milik MB_ON (salinan untuk blok ini), konfirmasi, lalu tunggu toast sukses
9. Buka halaman TAG Stock dan bandingkan stok RFID Object TAG pengirim dengan stok awal
10. Verifikasi stok fisik RFID Object TAG pengirim pada TAG Stock tidak berubah setelah Approve

### TC-AC-ACHA-401: Client Dashboard menampilkan kuota hanya dari transaksi Completed

11. Buka Client Dashboard PT Sejahtera Logistik dan catat kuota BLE sebagai kuota awal
12. Buka Allocation > Device Allocation, klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu tunggu toast sukses
13. Muat ulang Client Dashboard PT Sejahtera Logistik dan baca kuota BLE
14. Verifikasi kuota BLE pada Client Dashboard bertambah tepat 20 dibanding kuota awal setelah alokasi langsung
15. Catat kuota BLE saat ini sebagai kuota sebelum transaksi menunggu persetujuan
16. Kirim Submit alokasi BLE Quantity `30` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan
17. Muat ulang Client Dashboard PT Sejahtera Logistik dan baca kuota BLE
18. Verifikasi kuota BLE tidak bertambah akibat alokasi BLE Quantity 30 yang Waiting for Approval: sama dengan kuota sebelum transaksi menunggu persetujuan

### TC-AC-ACHA-402: Widget Pending Device Allocation mengikuti jumlah Waiting for Approval

19. Buka Dashboard dan catat jumlah pada widget Pending Device Allocation sebagai N
20. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan
21. Muat ulang Dashboard
22. Verifikasi jumlah widget Pending Device Allocation menjadi N + 1 setelah Submit
23. Kirim Cancel (`Cancel Allocation`) untuk transaksi itu lewat sesi API `Budi Santoso` hingga status `Canceled` tersimpan
24. Muat ulang Dashboard
25. Verifikasi jumlah widget kembali menjadi N setelah Cancel
26. Kirim Submit alokasi BLE Quantity `20` yang baru untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan, lalu catat Allocation ID
27. Muat ulang Dashboard
28. Verifikasi jumlah widget menjadi N + 1 setelah Submit kedua
29. Buka Approvals > Device Allocation, klik `[Approve]` pada transaksi baru itu, konfirmasi, lalu tunggu toast sukses
30. Muat ulang Dashboard
31. Verifikasi jumlah widget kembali menjadi N setelah Approve (widget dibaca langsung dari data Device Allocation tanpa penulisan sinkron)

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 7b). TC-AC-ACHA-403 (kuota Completed tidak ditarik saat Client di-Suspend) ada di spec 015 (`state-tenant-client-penerima-suspended-archived`). Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API (R-20): langkah Submit dan Cancel oleh `Budi Santoso` hanya memicu perubahan state; bukan konteks kedua kelas c, tidak memakai `P-2`.
- Langkah penghubung (S-03): langkah mencatat stok awal, kuota awal, dan N sebelum aksi pemicu (baseline S-12); langkah muat ulang Client Dashboard dan Dashboard; langkah "catat kuota BLE saat ini" sebelum transaksi menunggu persetujuan.
- Baris target (R-16): transaksi salinan pada langkah 8 ditemukan lewat Allocation ID yang ditangkap dari respons fixture seeding, dan transaksi baru pada langkah 29 lewat Allocation ID yang dicatat pada langkah 26; baris Approvals dicocokkan dengan Allocation ID itu (Search bila tersedia) sebagai langkah penghubung tanpa `Verifikasi` dan tanpa nomor sendiri.
- TC-AC-ACHA-399 dan 400 mengasersi "stok tidak berubah" sebagai perbandingan dengan stok awal yang dicatat; tanpa angka absolut karena stok fisik dipengaruhi data lain (S-12).
- Temuan untuk QA:
  - TC-AC-ACHA-399 dan 400 menyebut halaman "Hardware Stock dan TAG Stock" tanpa path menu dan tanpa menyebut baris atau kolom stok yang dibaca; Expected TC-AC-ACHA-400 hanya menyebut TAG Stock walau langkah 2 menyebut kedua halaman; spec mengasersi TAG Stock saja.
  - TC-AC-ACHA-401 menyebut kuota BLE Client Dashboard tanpa menyebut surface atau angka eksak yang diamati; spec mengasersi selisih terhadap angka yang dicatat.
  - TC-AC-ACHA-401 dan 402 menyebut Submit "sebagai MB_ON" tanpa menyebut apakah sesi UI atau API; spec memakai sesi API karena MB_ON hanya memicu state.
  - Post Condition TC-AC-ACHA-399, 400, 401, 402 ("Modul terdampak ...") tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.
