---
id: TC-AC-DN-E2E-177-jalur-b-handheld-reader-usb
title: "Pemilih Device Name Aktivasi Jalur B Handheld Reader oleh Client (Simulator USB)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-656
  - TC-AC-DN-658
coverage:
  web: automated
---

# Pemilih Device Name Aktivasi Jalur B Handheld Reader oleh Client (Simulator USB)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun konteks kedua: Total Control pada entitas Client `Client Jaringan` `totalControlClient_automated_{namaCompany}@qwertysystem.net` (Pre-setup #11 dan #29; email lewat `Fixture.settings-device-name.akunClient`), password `Spectra.env.AC_DN_CLIENT_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Konteks Client dibuka dan login di langkah spec (bukan hook), dan ditutup di akhir tiap blok TC.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #11, Measurement `Unit`, node Category `UHF Handheld`. Nama dinamis dibentuk `<nama dasar> {runId}-177` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Hardware` > `Handheld Reader` > `UHF Handheld`); #16 `RFID Reader` dan `Legacy Scanner` (UHF Handheld) sebagai opsi pembanding dalam konteks, `Gate Antenna` (Antenna) dan `Cable Tester` (Accessory) di luar konteks; #29 Client Jalur B siap aktivasi (toggle `Allow Self-Purchased Device Activation` aktif, kuota lisensi Short Range Handheld Reader, Serial Number reader tidak terdaftar di stok Principal).
- Data Dinamis (milik spec; dihapus fixture BE di hook `after`): `Pemindai Gerbang {runId}-177` (dibuat langkah UI pada TC-AC-DN-656) dan `Pemindai Uji Hapus {runId}-177` (dibuat langkah UI, dihapus langkah UI pada TC-AC-DN-658), keduanya Measurement `Unit`, Category `UHF Handheld`.
- Kemampuan teknis (disediakan tim FE/BE): simulator driver USB yang membaca Serial Number reader yang tidak terdaftar di stok Principal untuk langkah `[Sync]`; dua konteks browser (Principal dan Client).
- State global: tidak ada yang diubah. Perangkat simulator USB dipakai bergantian; suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_CLIENT_PASSWORD`.

## Test Steps

### TC-AC-DN-656: Device Name baru muncul pada pemilih Device Name Jalur B

1. Sebagai Principal, klik `+ Device Name`
2. Ketik "Pemindai Gerbang {runId}-177" pada field Device Name
3. Klik field Measurement lalu pilih `Unit`
4. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih leaf `UHF Handheld`
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, device name has been created."
7. Buka konteks browser Client, login sebagai Client (`Spectra.env.AC_DN_CLIENT_PASSWORD`)
8. Buka halaman `Global Settings > Hardware > Handheld Reader`
9. Klik `[+ Activate Reader]`, pilih Range Type `Short Range`
10. Klik `[Sync]` dengan reader yang Serial Number-nya tidak terdaftar di stok Principal (simulator USB)
11. Verifikasi popup aktivasi menampilkan field `Device Name*` (placeholder "Search and select device name..."), `SKU` (placeholder "Search and select SKU (optional)..."), `Brand`, dan `Model/Type`
12. Klik field `Device Name`
13. Verifikasi daftar opsi `Device Name` memuat "Pemindai Gerbang {runId}-177", "RFID Reader", dan "Legacy Scanner"
14. Verifikasi daftar opsi `Device Name` tidak memuat "Gate Antenna" maupun "Cable Tester"
15. Ketik "Pemindai" pada field `Device Name`
16. Verifikasi opsi dipersempit dan memuat "Pemindai Gerbang {runId}-177"
17. Tutup popup aktivasi tanpa Submit
18. Tutup konteks browser Client

### TC-AC-DN-658: Delete Device Name menghapus opsinya dari pemilih Jalur B

19. Sebagai Principal, klik `+ Device Name`
20. Ketik "Pemindai Uji Hapus {runId}-177" pada field Device Name
21. Klik field Measurement lalu pilih `Unit`
22. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih leaf `UHF Handheld`
23. Klik `[Submit]`
24. Verifikasi toast sukses "Success, device name has been created."
25. Buka konteks browser Client, login sebagai Client (`Spectra.env.AC_DN_CLIENT_PASSWORD`)
26. Buka halaman `Global Settings > Hardware > Handheld Reader`, klik `[+ Activate Reader]`, pilih Range Type `Short Range`
27. Klik `[Sync]` dengan reader yang Serial Number-nya tidak terdaftar di stok Principal (simulator USB)
28. Klik field `Device Name`
29. Verifikasi daftar opsi `Device Name` memuat "Pemindai Uji Hapus {runId}-177"
30. Sebagai Principal, ketik Search `Pemindai Uji Hapus {runId}-177`, tekan Enter
31. Buka menu aksi pada baris `Pemindai Uji Hapus {runId}-177`, klik `Delete`
32. Verifikasi dialog konfirmasi berjudul "Delete Device Name" memuat bullet "Pemindai Uji Hapus {runId}-177"
33. Klik `[Delete]` pada dialog
34. Verifikasi toast sukses "Success, device name has been deleted."
35. Sebagai Client, tutup lalu buka kembali daftar opsi `Device Name` pada popup aktivasi
36. Verifikasi daftar opsi `Device Name` memuat "RFID Reader"
37. Verifikasi daftar opsi `Device Name` tidak memuat "Pemindai Uji Hapus {runId}-177"
38. Tutup popup aktivasi tanpa Submit
39. Tutup konteks browser Client

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- P-7: TC-AC-DN-656 dan TC-AC-DN-658 membutuhkan simulator reader USB (kelas d: `[Sync]` pada aktivasi Jalur B) bersama konteks lain kelas c: TC-AC-DN-656 memakai konteks Principal dan konteks Client; TC-AC-DN-658 memakai konteks Client yang tetap terbuka dengan popup aktivasi saat konteks Principal menghapus Device Name (langkah 30 sampai 34). Keduanya satu spec; TC lain yang tidak membutuhkan USB berada di spec lain.
- Langkah penghubung (S-03, R-16): langkah 30 (Search) menemukan baris record milik spec; langkah 17, 18, 38, 39 menutup popup dan konteks Client (S-09); langkah 35 menutup lalu membuka kembali daftar opsi sesuai langkah TC.
- Urutan: mengikuti sourceTc; Delete (TC-AC-DN-658) di akhir. Anchor absence langkah 14 adalah langkah 13 dan anchor langkah 37 adalah langkah 36 (8b butir 2). Nama pembanding di luar konteks bukan substring nama uji (R-13).
- Konteks Client dibuka per blok (langkah 7 dan 25) karena TC-AC-DN-656 selesai tanpa Submit dan TC-AC-DN-658 membutuhkan sesi bersih.
- Ukuran spec (39 langkah, di atas smell 35 langkah, kode R2): dua blok berdiri sendiri dengan satu kelas harness (simulator USB dengan konteks Principal dan Client); tiap blok membuka konteks Client dan aktivasi `[Sync]` sendiri serta memakai Device Name sendiri, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-656 dan TC-AC-DN-658.
  - TC-AC-DN-656 dan TC-AC-DN-658: TC tidak menyebut apakah popup aktivasi yang berisi ketikan pencarian menampilkan dialog `Unsaved Changes` saat ditutup; langkah 17 dan 38 menutup popup tanpa asersi dialog.
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-177` (S-12).
