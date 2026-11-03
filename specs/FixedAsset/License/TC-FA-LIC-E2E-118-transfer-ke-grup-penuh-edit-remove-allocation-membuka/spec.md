---
id: TC-FA-LIC-E2E-118-transfer-ke-grup-penuh-edit-remove-allocation-membuka
title: "Transfer ke Grup Penuh Ditolak, Edit dan Remove Allocation Membuka Kembali Penerimaan Aset"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-391
  - TC-FA-LIC-490
  - TC-FA-LIC-534
  - TC-FA-LIC-392
  - TC-FA-LIC-393
coverage:
  web: automated
---

# Transfer ke Grup Penuh Ditolak, Edit dan Remove Allocation Membuka Kembali Penerimaan Aset

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, dan kuota dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (Gudang A beralokasi 100 di bawah Divisi Logistik; Divisi IT beralokasi 100 dengan Used by This Group 60; Kantor Pusat) dan #20 (aset Active di Divisi IT untuk Transfer; draf aset siap Submit di Gudang A dan Divisi IT). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-391 Gudang A Remaining 0; blok TC-FA-LIC-490 Divisi IT Remaining 0; blok TC-FA-LIC-534 Gudang A Used 99 (Remaining 1), transfer satu aset Active dari Divisi IT ke Gudang A sudah di-Request dan berstatus In Transfer Process, lalu satu registrasi aset lain mengisi slot terakhir sebelum Arrival (Used 100, Remaining 0); blok TC-FA-LIC-392 Gudang A beralokasi 100 dengan Remaining 0, Remaining Divisi Logistik 50, approval OFF; blok TC-FA-LIC-393 Divisi IT beralokasi 100 dengan Used 60, Remaining Kantor Pusat 200, approval OFF.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #20 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah, serta Used dan Remaining grup dan status aset berubah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-391: Transfer ke grup yang kuotanya penuh ditolak

1. Jalankan fixture BE pemulih Pre-setup #12 dengan Gudang A Remaining `0` dan aset Active di Divisi IT siap Transfer ke Gudang A hingga tersimpan
2. Buka Fixed Asset > Transfer; ajukan Transfer aset Active di Divisi IT ke group tujuan Gudang A sampai titik arrival
3. Verifikasi Transfer ditolak karena `QUOTA_EXCEEDED` (pesan penolakan dimiliki modul transfer)
4. Buka daftar aset
5. Verifikasi aset tetap di Divisi IT
6. Buka License > Allocation Quota > node `Gudang A`
7. Verifikasi Used by This Group Gudang A tetap `100`
8. Klik node `Divisi IT` di Sidebar
9. Verifikasi Used by This Group Divisi IT tetap `60`

### TC-FA-LIC-490: Transfer ke grup penuh ditolak dengan copy milik modul transfer

10. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Remaining `0` hingga tersimpan
11. Buka Fixed Asset > Transfer; ajukan Transfer satu aset ke Divisi IT
12. Verifikasi pemeriksaan kuota mengembalikan `QUOTA_EXCEEDED` (Transfer ditolak)
13. Verifikasi penolakan ditampilkan dengan copy milik modul transfer (`transactions-transfer/`), bukan teks V-FALIC-06 milik registrasi dan Manage
14. Buka License > All License
15. Verifikasi License Summary tampil
16. Verifikasi halaman License tidak menampilkan toast sendiri

### TC-FA-LIC-534: Kuota grup tujuan terlampaui di titik arrival menggagalkan seluruh Arrival

17. Jalankan fixture BE pemulih Pre-setup #12 dengan Gudang A Used `99`, transfer satu aset Active dari Divisi IT ke Gudang A berstatus In Transfer Process, dan satu registrasi aset lain ke Gudang A hingga Used `100` dan Remaining `0` tersimpan
18. Buka Fixed Asset > Transfer > Incoming
19. Klik Arrival pada transaksi ke Gudang A
20. Verifikasi aset pada transaksi Arrival Gudang A
21. Klik `[Confirm Receipt]`
22. Verifikasi pemeriksaan kuota di titik arrival mengembalikan `QUOTA_EXCEEDED` dan seluruh Arrival gagal
23. Verifikasi transaksi tetap In Transfer Process
24. Verifikasi aset tetap di Divisi IT
25. Buka License > Allocation Quota > node `Gudang A`
26. Verifikasi Used by This Group Gudang A tetap `100` dan Remaining `0`

### TC-FA-LIC-392: Edit Allocation ke atas membuka kembali kemampuan registrasi di grup yang penuh

27. Jalankan fixture BE pemulih Pre-setup #12 dengan Gudang A beralokasi 100 (Remaining `0`), Remaining Divisi Logistik `50`, approval OFF, dan draf aset di Gudang A hingga tersimpan
28. Buka License > Allocation Quota > node `Divisi Logistik`
29. Klik tombol ikon `[Edit]` pada baris `Gudang A`
30. Isi New Allocated Quota `110`
31. Klik `[Save]`
32. Verifikasi Edit sukses dengan toast `Success, group license quota updated.`
33. Buka Fixed Asset > Asset Registration
34. Submit 1 draf aset di Gudang A
35. Verifikasi registrasi berhasil
36. Buka License > Allocation Quota > node `Gudang A`
37. Verifikasi Used by This Group Gudang A `101` dan Remaining `9`

### TC-FA-LIC-393: Remove Allocation grup, registrasi berikutnya memakai Remaining leluhur

38. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT beralokasi 100 (Used 60), Remaining Kantor Pusat `200`, approval OFF, dan draf aset di Divisi IT hingga tersimpan
39. Buka License > Allocation Quota > node `Kantor Pusat`
40. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
41. Klik `[Clear Field]`
42. Klik `[Save]`
43. Tunggu aksi selesai (modal Edit Allocation tertutup)
44. Catat Remaining Kantor Pusat (`240`)
45. Buka Fixed Asset > Asset Registration
46. Submit 1 draf aset di Divisi IT
47. Verifikasi registrasi berhasil memakai Remaining Kantor Pusat
48. Buka License > Allocation Quota > node `Kantor Pusat`
49. Verifikasi Remaining Kantor Pusat `239` (berkurang dari `240` pada langkah 44)
50. Klik node `Divisi IT` di Sidebar
51. Verifikasi Used by This Group Divisi IT `61`
52. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 10, 17, 27, 38, dan 52 (fixture BE pemulih dan penyetel state), langkah 4 (membuka daftar aset untuk mengamati aset), langkah 43 (tunggu aksi selesai), serta navigasi tab dan node Sidebar. Langkah 44 mencatat Remaining Kantor Pusat sebagai baseline langkah 49 (S-12).
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-391, TC-FA-LIC-490, dan TC-FA-LIC-534 (penolakan) lebih dulu, lalu TC-FA-LIC-392 dan TC-FA-LIC-393 yang mengubah alokasi dan menerima registrasi (S-10).
- Alasan di atas sekitar 35 langkah (52 langkah): semua blok satu topik (kapasitas kuota grup menolak atau membuka penerimaan aset) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya navigasi, pembacaan baseline, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-490 Expected b dan c tidak memberi teks penolakan modul transfer dan tidak menyebut toast mana yang dimaksud "toast sendiri"; spec mengasersi sesuai kalimat TC (penolakan memakai copy modul transfer, bukan teks V-FALIC-06, dan halaman License tanpa toast sendiri, dengan License Summary sebagai anchor).
  - TC-FA-LIC-534 langkah 1 meminta "verifikasi aset" tanpa Expected dan tanpa nilai; spec menuliskannya sebagai langkah `Verifikasi` sendiri tanpa nilai konkret (S-03).
  - TC-FA-LIC-534 tidak menyebut cara mengamati kode `QUOTA_EXCEEDED` pada Arrival (tidak ada langkah intercept); spec mengasersi kegagalan Arrival sesuai Expected.
  - TC-FA-LIC-393 langkah 1 tidak memberi Expected; langkah Remove Allocation diakhiri langkah tunggu aksi selesai dan Remaining Kantor Pusat `240` dicatat untuk membuktikan penurunan ke `239`.
