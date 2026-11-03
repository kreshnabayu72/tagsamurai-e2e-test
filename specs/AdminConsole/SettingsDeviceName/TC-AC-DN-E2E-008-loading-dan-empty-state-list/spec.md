---
id: TC-AC-DN-E2E-008-loading-dan-empty-state-list
title: "Loading State dan Empty State Search/Filter/Sidebar pada List"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-24
  - TC-AC-DN-26
  - TC-AC-DN-27
  - TC-AC-DN-28
coverage:
  web: automated
---

# Loading State dan Empty State Search/Filter/Sidebar pada List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Master Brand (#15: `Brand A`), Master Measurement (#13: `Meter`), dan Device Name inti (#16: `Door Antenna`, `Gate Antenna`, `Cable Tester`, `Barcode Station`); baca-saja. Tidak ada data Dinamis.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons list Device Name selama 3 detik di atas backend nyata (TC-AC-DN-24); intercept dilepas segera setelah loading diamati.
- State global: tidak ada yang diubah; Search, Filter, dan pilihan Sidebar yang dipakai spec dibersihkan di akhir tiap TC.

## Test Steps

### TC-AC-DN-24: Loading state tampil saat data List sedang dimuat

1. Siapkan penundaan respons list Device Name selama 3 detik (intercept jaringan)
2. Muat ulang halaman `Settings > Device > Device Name`
3. Verifikasi loading component tampil pada area tabel
4. Verifikasi selama penundaan baris data, empty state, dan error load tidak tampil
5. Lepas penundaan respons dan tunggu respons diterima
6. Verifikasi loading hilang
7. Verifikasi baris Device Name tampil

### TC-AC-DN-26: Search tanpa hasil dengan Sidebar Category = All menampilkan empty state S-04

8. Ketik Search `zzzxyzq`, tekan Enter
9. Verifikasi empty state dengan illustration, Title "No results found" dan Description "Try adjusting your search or filter."
10. Verifikasi kolom pencarian tetap berisi "zzzxyzq"
11. Verifikasi tabel tidak menampilkan baris
12. Verifikasi empty state ini tanpa teks "No device names yet"
13. Verifikasi empty state ini bukan error load
14. Klik `(←)` pada kotak Search

### TC-AC-DN-27: Filter Panel tanpa hasil dengan Sidebar Category = All menampilkan empty state S-04

15. Klik ikon Filter
16. Pilih Brand `Brand A` pada field `Brand` (placeholder "All brands")
17. Pilih Measurement `Meter` pada field `Measurement` (placeholder "All measurements")
18. Klik `[Apply]`
19. Verifikasi empty state dengan illustration, Title "No results found" dan Description "Try adjusting your search or filter."
20. Verifikasi tabel tidak menampilkan baris karena tidak ada Device Name ber-Brand `Brand A` sekaligus ber-Measurement `Meter`
21. Verifikasi ikon Filter menampilkan badge titik (filter aktif)
22. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-28: Search digabung Sidebar Category aktif tanpa hasil menampilkan empty state S-03 yang sama dengan S-04

23. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
24. Pilih node `Antenna` pada Category Sidebar
25. Ketik Search `Cable`, tekan Enter
26. Verifikasi empty state dengan illustration, Title "No results found" dan Description "Try adjusting your search or filter."; copy identik dengan empty state Search atau Filter Panel tanpa hasil pada Sidebar Category = All (`S-04`)
27. Verifikasi tabel tidak menampilkan baris karena Device Name berkategori Antenna (Door Antenna, Gate Antenna) tidak memuat "Cable"
28. Verifikasi empty state bukan error load
29. Verifikasi empty state tidak menampilkan teks "No device names yet"
30. Verifikasi kolom pencarian tetap berisi "Cable"
31. Verifikasi node `Antenna` tetap terpilih di Category Sidebar
32. Klik `(←)` pada kotak Search
33. Hapus pilihan node `Antenna` pada Category Sidebar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Tidak ada aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- TC-AC-DN-24 menahan respons list hanya untuk mengamati state UI (loading) di atas backend nyata; bukan kegagalan yang dipaksakan (prinsip 13b), sehingga tetap di spec fungsional. Halaman dimuat ulang pada langkah 2 karena halaman sudah dibuka hook `beforeEach` suite sebelum intercept dipasang.
- Langkah penghubung (S-03, S-09, R-16): langkah 14 dan 32 mengosongkan Search; langkah 22 mengosongkan Filter Panel; langkah 33 melepas pilihan Sidebar; langkah 23 membuka cabang pohon Sidebar yang dibutuhkan TC-AC-DN-28.
- Urutan: loading (TC-AC-DN-24) di awal, lalu empty state Search, Filter Panel, dan kombinasi Sidebar + Search di akhir.
- Temuan untuk QA:
  - TC-AC-DN-28 langkah 2 menyebut List difilter menjadi dua baris (Door Antenna, Gate Antenna) sebagai hasil memilih `Antenna`, tetapi Expected tidak memuatnya; spec tidak menambahkan asersi dua baris.
