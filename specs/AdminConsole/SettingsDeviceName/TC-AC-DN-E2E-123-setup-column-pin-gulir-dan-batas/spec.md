---
id: TC-AC-DN-E2E-123-setup-column-pin-gulir-dan-batas
title: "Setup Column List: Kolom Terpin saat Gulir, Persistensi F5, dan Pin Ke-4 Diblok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-333
  - TC-AC-DN-334
coverage:
  web: automated
---

# Setup Column List: Kolom Terpin saat Gulir, Persistensi F5, dan Pin Ke-4 Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti dan #17 seed 120 baris sebagai isi tabel. Tidak ada data Dinamis dan tidak ada aksi tulis ke server.
- Kemampuan teknis: mengubah lebar viewport sampai tabel dapat digulir horizontal dan memulihkannya; muat ulang F5; penghapusan preferensi kolom di browser (konfigurasi Setup Column disimpan di cache browser tabel List; kemampuan penghapusan disediakan tim FE, konvensi bagian 4).
- State global: konfigurasi pin di browser; hook `before` dan `after` menghapus preferensi kolom di browser. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-333: Kolom terpin tetap di tempat saat digulir dan bertahan setelah F5

1. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
2. Pin `Device Name` dan `Category`
3. Klik `[Save]`
4. Perkecil lebar viewport sampai tabel dapat digulir horizontal
5. Gulir tabel ke kanan
6. Verifikasi kolom `Device Name` dan `Category` membeku di sisi kiri dan tidak ikut bergeser saat tabel digulir
7. Verifikasi kolom lain bergeser di belakang kolom terpin
8. Muat ulang halaman dengan F5
9. Verifikasi `Device Name` dan `Category` tetap terpin
10. Pulihkan lebar viewport ke ukuran awal
11. Hapus preferensi kolom di browser, lalu muat ulang halaman dengan F5

### TC-AC-DN-334: Pin ke-4 diblok setelah tiga kolom terpin

12. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
13. Pin `Device Name`, `Category`, dan `Brand`
14. Arahkan kursor ke ikon Pin `Measurement`
15. Verifikasi ikon Pin `Model/Type`, `Measurement`, dan `Last Modified` tetap tampil namun disabled
16. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
17. Klik ikon Pin `Measurement`
18. Verifikasi klik pada ikon disabled tidak membekukan kolom Measurement
19. Klik ikon close `(✕)` pada modal Setup Column

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis ke server.
- Langkah penghubung (S-03, S-09): langkah 10 memulihkan viewport; langkah 11 menghapus preferensi pin di browser sebelum TC-AC-DN-334; langkah 19 menutup modal tanpa menyimpan.
- TC-AC-DN-332 (pin dan unpin tiap kolom) ada di spec 114.
- Urutan: mengikuti sourceTc.
- Temuan untuk QA:
  - TC-AC-DN-333 Post Condition ("konfigurasi pin tersimpan di cache browser") tanpa langkah observasi tidak diasersi; persistensi diasersi lewat F5 (langkah 9).
