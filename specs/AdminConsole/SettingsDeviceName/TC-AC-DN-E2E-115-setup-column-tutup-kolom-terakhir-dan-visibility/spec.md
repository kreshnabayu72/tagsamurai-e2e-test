---
id: TC-AC-DN-E2E-115-setup-column-tutup-kolom-terakhir-dan-visibility
title: "Setup Column List: Tutup Modal Membuang Perubahan, Kolom Terakhir, Column Visibility, dan Independensi Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-336
  - TC-AC-DN-337
  - TC-AC-DN-338
  - TC-AC-DN-339
  - TC-AC-DN-340
  - TC-AC-DN-342
coverage:
  web: automated
---

# Setup Column List: Tutup Modal Membuang Perubahan, Kolom Terakhir, Column Visibility, dan Independensi Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti dan #17 seed 120 baris sebagai isi tabel; #19 riwayat Changelog Uji (11 entri) dan #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta) untuk modal Changelog. Tidak ada data Dinamis dan tidak ada aksi tulis ke server.
- Kemampuan teknis: menyeret kolom (drag and drop), tombol Esc, muat ulang F5, dan penghapusan preferensi kolom di browser (konfigurasi kolom disimpan di cache browser tabel List; kemampuan penghapusan disediakan tim FE, konvensi bagian 4).
- State global: konfigurasi kolom di browser. Hook `before` dan `after` menghapus preferensi kolom di browser. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-336: Menutup modal Setup Column lewat ikon close membuang perubahan

1. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
2. Hapus centang `Brand`
3. Seret `Measurement` ke posisi pertama
4. Klik ikon close `(✕)`
5. Verifikasi modal menutup
6. Verifikasi tidak ada dialog konfirmasi
7. Verifikasi tabel kembali memakai konfigurasi tersimpan terakhir (enam kolom urutan default)

### TC-AC-DN-337: Menutup modal Setup Column lewat Esc membuang perubahan

8. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
9. Hapus centang `Brand`
10. Seret `Measurement` ke posisi pertama
11. Tekan Esc
12. Verifikasi modal menutup
13. Verifikasi tidak ada dialog konfirmasi
14. Verifikasi tabel kembali memakai konfigurasi tersimpan terakhir (enam kolom urutan default)

### TC-AC-DN-338: Kolom visible terakhir tidak dapat di-uncheck di modal Setup Column

15. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
16. Hapus centang `Category`, `Brand`, `Model/Type`, `Measurement`, dan `Last Modified`
17. Arahkan kursor ke checkbox `Device Name`
18. Verifikasi checkbox `Device Name` tampil namun disabled
19. Verifikasi tooltip `At least one column must remain visible.` tampil
20. Klik checkbox `Device Name`
21. Verifikasi klik pada checkbox disabled tidak menyembunyikan kolom Device Name
22. Klik ikon close `(✕)`

### TC-AC-DN-339: Kolom visible terakhir tidak dapat di-uncheck di Overlay Column Visibility

23. Klik header `⋯`
24. Hapus centang `Category`, `Brand`, `Model/Type`, `Measurement`, dan `Last Modified` satu per satu
25. Arahkan kursor ke checkbox `Device Name`
26. Verifikasi checkbox `Device Name` tampil namun disabled
27. Verifikasi tooltip `At least one column must remain visible.` tampil
28. Centang kembali `Category`, `Brand`, `Model/Type`, `Measurement`, dan `Last Modified`

### TC-AC-DN-340: Perubahan di Overlay Column Visibility berlaku langsung

29. Hapus centang `Category` pada overlay yang masih terbuka
30. Verifikasi kolom Category hilang dari tabel seketika tanpa tombol Save
31. Seret `Last Modified` ke posisi pertama di dalam overlay
32. Verifikasi kolom Last Modified berpindah ke posisi pertama seketika
33. Muat ulang halaman dengan F5
34. Verifikasi kolom Device Name, Brand, Model/Type, Measurement, dan Last Modified tetap tampil setelah F5
35. Verifikasi Category tetap tersembunyi setelah F5
36. Verifikasi Last Modified tetap di posisi pertama setelah F5
37. Hapus preferensi kolom di browser, lalu muat ulang halaman dengan F5

### TC-AC-DN-342: Konfigurasi kolom List tidak memengaruhi kolom modal Changelog

38. Klik header `⋯`, hapus centang `Measurement`
39. Klik ikon Changelog di toolbar
40. Verifikasi modal `Changelog: Device Name` tetap menampilkan ketujuh kolomnya: `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By`
41. Klik ikon close `(✕)` pada modal Changelog
42. Hapus preferensi kolom di browser, lalu muat ulang halaman dengan F5

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis ke server.
- Langkah penghubung (S-03, S-09): langkah 22 menutup modal yang berisi perubahan tak tersimpan; langkah 28 memulihkan kolom sebelum TC-AC-DN-340; langkah 37 dan 42 menghapus preferensi kolom di browser. langkah 34 (kolom lain tampil setelah F5) adalah anchor positif sebelum asersi Category tersembunyi pada langkah 35 (S-03). TC-AC-DN-340 memakai overlay yang masih terbuka dari langkah 23 (satu pembukaan dipakai bersama), sehingga langkah klik header `⋯` tidak diulang.
- Ukuran spec (42 langkah, di atas smell 35 langkah): modal Setup Column dan overlay Column Visibility yang sama dipakai berulang oleh enam TC tanpa submit ke server; pembukaan ulang hanya bila precondition TC berbeda, dan tiap blok memulai dari konfigurasi kolom yang dipulihkan sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc; TC-AC-DN-342 yang membuka modal Changelog di akhir.
- Temuan untuk QA:
  - TC-AC-DN-338 dan TC-AC-DN-339 tidak menyebut pemulihan kolom yang di-uncheck sesudah TC; spec menutup modal tanpa Save (langkah 22) dan mencentang ulang kolom di overlay (langkah 28).
