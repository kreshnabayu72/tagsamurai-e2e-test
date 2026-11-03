---
id: TC-AC-DN-E2E-176-sinkron-general-settings-dan-capability
title: "General Settings (Date Format) dan Capability Delete yang Dicabut"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-534
  - TC-AC-DN-535
  - TC-AC-DN-536
  - TC-AC-DN-538
coverage:
  web: automated
---

# General Settings (Date Format) dan Capability Delete yang Dicabut

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun pada langkah 19 dan 27): Full CRUD non-Total Control `manageDeviceCUD_automated_{namaCompany}@qwertysystem.net` (Pre-setup #7, role custom Create + Update + Delete + Read; email lewat `Fixture.settings-device-name.akunFullCrud`), password `Spectra.env.AC_DN_CRUD_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #7, nama role Full CRUD non-Total Control.
- Data Pre-setup (dibaca saja kecuali dinyatakan): #16 Device Name `Cable Tester` (Last Modified 10/09/26 12:25); #19 riwayat Changelog (entri Create `Cable Tester` 01/09/26 08:30 dan Create `NFC Tag` 02/09/26 09:10); #20 General Settings entitas uji (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta); #7 role custom. Record Device Name tidak diubah.
- State global (S-06, pengecualian 2026-10-30): Date Format General Settings diubah ke `dd MMM yy` pada langkah 1 dan capability Delete role Full CRUD non-Total Control dicabut pada langkah 17; fixture backend yang disediakan tim FE/BE memulihkan Date Format `dd/MM/yy` (langkah 16) dan capability Delete (langkah 28) serta menjalankan pemulihan yang sama di hook `before` dan `after`. Efeknya (Last Modified dan audit trail General Settings dan Role & Permission) dicatat di sini. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_CRUD_PASSWORD`.

## Test Steps

### TC-AC-DN-534 sampai TC-AC-DN-536: Date Format General Settings

1. Buka halaman `General Settings`
2. Ubah Date Format menjadi `dd MMM yy`
3. Klik `[Save]`
4. Tunggu aksi selesai (konfigurasi tersimpan)

### TC-AC-DN-534: Format kolom Last Modified pada List

5. Buka halaman `Settings > Device > Device Name`, ketik Search `Cable Tester`, tekan Enter
6. Verifikasi kolom Last Modified baris "Cable Tester" menampilkan tanggal "10 Sep 26" dan jam "12:25"

### TC-AC-DN-535: Format kolom Date pada modal Changelog

7. Klik ikon Changelog
8. Klik header kolom Date sekali
9. Verifikasi kolom Date baris pertama menampilkan tanggal "01 Sep 26" dan jam "08:30"
10. Verifikasi kolom Date baris kedua menampilkan tanggal "02 Sep 26" dan jam "09:10"
11. Klik icon `(✕)` pada modal

### TC-AC-DN-536: Format tanggal pada input Filter Last Modified

12. Klik ikon Filter
13. Klik field Last Modified, pilih rentang tanggal 05 September 2026 sampai 10 September 2026
14. Verifikasi input Last Modified menampilkan tanggal awal "05 Sep 26" dan tanggal akhir "10 Sep 26"
15. Tutup Filter Panel
16. Pulihkan Date Format `dd/MM/yy` lewat fixture BE

### TC-AC-DN-538: Capability Delete dicabut

17. Buka halaman `Settings > Role & Permission`, ubah capability Manage device master data role Full CRUD non-Total Control: hapus centang Delete, klik `[Save]`
18. Tunggu aksi selesai (perubahan tersimpan)
19. Ganti akun: logout, lalu login sebagai Full CRUD non-Total Control (`Spectra.env.AC_DN_CRUD_PASSWORD`)
20. Muat ulang halaman `Settings > Device > Device Name`
21. Buka menu aksi pada baris "Cable Tester"
22. Verifikasi overlay row action memuat `Detail` dan `Edit`
23. Verifikasi overlay row action tidak memuat `Delete`
24. Verifikasi kolom checkbox seleksi baris tidak tampil
25. Verifikasi tombol `+ Device Name` tetap tampil
26. Tutup overlay row action
27. Ganti akun: logout, lalu login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
28. Pulihkan capability Delete role Full CRUD non-Total Control lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 sampai 4 dipakai bersama oleh TC-AC-DN-534, TC-AC-DN-535, dan TC-AC-DN-536 karena langkah pertama ketiganya identik dan state yang diubah sama; langkah 5 (Search) menemukan baris Pre-setup #16 yang hanya dibaca; langkah 11, 15, 26 menutup modal, panel, atau overlay; langkah 16 dan 28 memulihkan state global (S-06); langkah 18 menunggu penyimpanan yang hasilnya tidak diasersi (8b butir 8).
- Ganti akun eksplisit pada langkah 19 dan 27 (S-07); TC sumber menyebut "sesi kedua", tetapi ganti akun pada satu konteks memadai karena tidak ada asersi lintas sesi.
- Asersi tanggal dan jam (S-12): nilai berasal dari data seed Pre-setup #19 dan Last Modified Pre-setup #16 yang tidak diubah spec lain; baris Changelog dibaca dengan sort Oldest First sehingga entri seed berada di atas entri baru (S-14).
- Urutan: mengikuti sourceTc; pemulihan Date Format sebelum TC-AC-DN-538 supaya state global tidak terbawa.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-534, TC-AC-DN-535, TC-AC-DN-536 (Date Format tersimpan), TC-AC-DN-538 (capability tersimpan tidak aktif).
  - TC-AC-DN-538: nama role dan kode Pre-setup #7 menyebut email akun tanpa nama role; nama role diambil dari fixture yang disediakan tim FE.
