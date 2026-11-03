---
id: TC-AC-DN-E2E-113-setup-column-geser-reset-dan-persistensi
title: "Setup Column List: Geser Urutan, Reset to Default, dan Persistensi setelah F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-331
  - TC-AC-DN-335
  - TC-AC-DN-341
coverage:
  web: automated
---

# Setup Column List: Geser Urutan, Reset to Default, dan Persistensi setelah F5

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti dan #17 seed 120 baris sebagai isi tabel dan Live Preview. Tidak ada data Dinamis dan tidak ada aksi tulis ke server.
- Tabel "Kolom uji" untuk langkah berulang (langkah 2 sampai 3): `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`.
- Kemampuan teknis: menyeret baris kolom (drag and drop) pada modal Setup Column, muat ulang F5, dan penghapusan preferensi kolom di browser (konfigurasi Setup Column disimpan di cache browser tabel List; kemampuan penghapusan disediakan tim FE, konvensi bagian 4).
- State global: konfigurasi kolom di browser. Hook `before` dan `after` menghapus preferensi kolom di browser. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-331: Geser urutan kolom lalu Save

1. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
2. Seret kolom uji ke posisi paling akhir
3. Verifikasi kolom uji berada di posisi terakhir pada Live Preview
4. Untuk setiap baris tabel "Kolom uji", ulangi langkah 2 sampai 3
5. Seret `Last Modified` ke posisi pertama
6. Verifikasi urutan Live Preview: Last Modified, Device Name, Category, Brand, Model/Type, Measurement
7. Klik `[Save]`
8. Verifikasi header tabel mengikuti urutan Last Modified, Device Name, Category, Brand, Model/Type, Measurement
9. Hapus preferensi kolom di browser, lalu muat ulang halaman dengan F5

### TC-AC-DN-335: Reset to Default mengembalikan konfigurasi kolom ke default

10. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
11. Hapus centang `Category`
12. Seret `Last Modified` ke posisi pertama
13. Pin `Device Name`
14. Klik `[Save]`
15. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
16. Klik `[Reset to Default]`
17. Verifikasi Live Preview menampilkan keenam kolom dengan urutan default Device Name, Category, Brand, Model/Type, Measurement, Last Modified
18. Verifikasi Live Preview tanpa pin
19. Klik `[Save]`
20. Muat ulang halaman dengan F5
21. Verifikasi tabel memakai urutan default dengan keenam kolom tampil
22. Verifikasi tabel tanpa kolom terpin

### TC-AC-DN-341: Konfigurasi kolom hasil Save bertahan setelah F5

23. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
24. Hapus centang `Measurement` dan `Last Modified`
25. Klik `[Save]`
26. Muat ulang halaman dengan F5
27. Verifikasi kolom Device Name tampil
28. Verifikasi kolom Measurement dan Last Modified tetap tersembunyi
29. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
30. Verifikasi checkbox `Measurement` dan `Last Modified` tidak tercentang
31. Klik ikon close `(✕)` pada modal Setup Column
32. Hapus preferensi kolom di browser, lalu muat ulang halaman dengan F5

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis ke server.
- Langkah penghubung (S-03, S-09): langkah 9 dan 32 menghapus preferensi kolom di browser sebelum TC berikutnya dan di akhir spec (bagian 4); langkah 31 menutup modal; langkah 27 menjadi anchor positif (kolom lain tampil) sebelum absence Measurement dan Last Modified sesudah F5 (S-03).
- Ukuran spec (32 langkah nominal, sekitar 40 langkah dengan ekspansi langkah 2 sampai 3 untuk enam kolom; di atas smell 35 langkah, bagian 8b butir 7): satu topik (Setup Column List), satu dataset, satu kelas harness; tiap blok TC mulai dari preferensi kolom yang dihapus sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc; geser urutan, Reset to Default, lalu persistensi.
- Temuan untuk QA:
  - TC-AC-DN-331 Post Condition ("konfigurasi urutan kolom tersimpan di cache browser tabel List") tanpa langkah observasi di TC tidak diasersi; persistensi diasersi lewat F5 pada TC-AC-DN-341.
