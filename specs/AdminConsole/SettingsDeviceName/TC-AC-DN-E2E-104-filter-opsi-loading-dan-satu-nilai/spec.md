---
id: TC-AC-DN-E2E-104-filter-opsi-loading-dan-satu-nilai
title: "Filter Panel List: Loading Opsi, Pencarian Opsi, dan Filter Satu Nilai (Brand, Model/Type, Measurement)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-293
  - TC-AC-DN-295
  - TC-AC-DN-296
  - TC-AC-DN-297
  - TC-AC-DN-298
coverage:
  web: automated
---

# Filter Panel List: Loading Opsi, Pencarian Opsi, dan Filter Satu Nilai (Brand, Model/Type, Measurement)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #15 Brand `Brand A` sampai `Brand D` dan `International Scanner Solutions`; #16 Device Name inti beserta SKU-nya (`Gate Antenna`, `NFC Tag`, `RFID Reader` ber-Brand A; `RFID Reader` ber-Model R1/R2/R3; `Tag Reel` ber-Measurement `Meter`); #17 seed 120 baris. Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons permintaan opsi filter selama 3 detik di atas backend nyata (TC-AC-DN-293); intercept dilepas segera setelah loading diamati.
- State global: tidak ada yang diubah. Filter yang di-Apply dilepas lewat `[Clear Field]` lalu `[Apply]` di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-293: Indikator pemuatan opsi dropdown filter

1. Siapkan penundaan respons permintaan opsi filter selama 3 detik (intercept jaringan)
2. Klik ikon Filter lalu klik field `Brand`
3. Verifikasi dropdown menampilkan skeleton atau spinner selama opsi dimuat, bukan dropdown kosong tanpa indikator
4. Lepas penundaan respons dan tunggu respons diterima
5. Verifikasi opsi `Brand A`, `Brand B`, `Brand C`, `Brand D`, dan `International Scanner Solutions` tampil
6. Tutup dropdown `Brand`

### TC-AC-DN-295: Pencarian di dalam dropdown filter

7. Klik field `Brand`, ketik `brand` di kotak pencarian dropdown
8. Verifikasi opsi `Brand A`, `Brand B`, `Brand C`, `Brand D` tampil
9. Verifikasi opsi `International Scanner Solutions` tidak tampil
10. Ganti isi kotak pencarian dropdown dengan `zzzxyz`
11. Verifikasi daftar `Brand` tanpa opsi
12. Tutup dropdown `Brand`, klik field `Model/Type`, ketik `model r` di kotak pencarian dropdown
13. Verifikasi opsi `Model R1`, `Model R2`, `Model R3` tampil
14. Ganti isi kotak pencarian dropdown dengan `zzzxyz`
15. Verifikasi daftar `Model/Type` tanpa opsi
16. Tutup dropdown `Model/Type`, klik field `Measurement`, ketik `ME` di kotak pencarian dropdown
17. Verifikasi opsi `Meter` tampil (huruf besar-kecil tidak dibedakan)
18. Ganti isi kotak pencarian dropdown dengan `zzzxyz`
19. Verifikasi daftar `Measurement` tanpa opsi
20. Tutup dropdown `Measurement`

### TC-AC-DN-296: Filter Brand dengan satu opsi

21. Klik field `Brand`, centang `Brand A`
22. Klik `[Apply]`
23. Verifikasi tabel menampilkan 3 baris: Gate Antenna, NFC Tag, RFID Reader
24. Verifikasi ikon Filter menampilkan indikator filter aktif
25. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-297: Filter Model/Type dengan satu opsi

26. Klik ikon Filter, klik field `Model/Type`, centang `Model R3`
27. Klik `[Apply]`
28. Verifikasi tabel menampilkan 1 baris: RFID Reader
29. Verifikasi `Model R3` berada di balik chip `+1 more` pada sel Model/Type RFID Reader
30. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-298: Filter Measurement dengan satu opsi

31. Klik ikon Filter, klik field `Measurement`, centang `Meter`
32. Klik `[Apply]`
33. Verifikasi tabel menampilkan 1 baris: Tag Reel
34. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- TC-AC-DN-293 menahan respons opsi filter hanya untuk mengamati state UI (loading) di atas backend nyata; bukan kegagalan yang dipaksakan (prinsip 13b), sehingga tetap di spec fungsional.
- Langkah penghubung (S-03, S-09): langkah 6, 12, 16, dan 20 menutup dropdown; langkah 25, 30, dan 34 melepas filter yang di-Apply sebelum blok berikutnya; langkah 25, 26, 30, 31, dan 34 membuka kembali Filter Panel karena panel menutup setelah `[Apply]` (mengikuti pola TC lain; lihat Temuan untuk QA).
- Urutan: mengikuti sourceTc; loading opsi di awal, lalu pencarian opsi, lalu filter satu nilai per field.
- Temuan untuk QA:
  - TC-AC-DN-293 tidak menyebut endpoint permintaan opsi filter; spec menunda permintaan opsi lewat intercept tanpa menyebut endpoint (S-13) dan kemampuan intercept disediakan tim FE.
  - Perilaku Filter Panel setelah `[Apply]` (menutup atau tetap terbuka) tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-296 hingga TC-AC-DN-298: langkah TC menyebut chip tampil di dalam field sebagai hasil centang, tetapi Expected tidak memuatnya; spec tidak menambahkan asersi chip.
