---
id: TC-AC-DN-E2E-093-usage-search-dan-filter-kombinasi
title: "Usage by Company: Kombinasi AND Filter dan Search Nama Company/Entity Type/Total"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-631
  - TC-AC-DN-264
  - TC-AC-DN-593
coverage:
  web: automated
---

# Usage by Company: Kombinasi AND Filter dan Search Nama Company/Entity Type/Total

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, ketik, hover, dan membaca urutan baris serta isi sel tabel Usage by Company.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik teks nama `Gate Antenna` pada kolom Device Name

### TC-AC-DN-631: Kombinasi AND Entity Type, Total SKU, dan Total Stock pada Filter tabel Usage by Company

2. Klik ikon Filter pada toolbar tabel Usage
3. Klik field `Entity Type`, centang `Client`, lalu isi `Total Stock` Min `6`
4. Verifikasi satu chip dan satu nilai tampil pada Filter Panel
5. Klik `[Apply]`
6. Verifikasi tabel menampilkan 2 baris: `Company C` (`Client`, Total SKU 0, Total Stock 6) dan `Company E` (`Client`, Total SKU 0, Total Stock 12)
7. Verifikasi `Company B` (`Distributor` dan `Client`, Total Stock 2) tidak tampil karena Total Stock di bawah 6 (irisan AND antar-field), dan `Company A` serta `Company D` tidak tampil
8. Verifikasi ikon Filter menampilkan badge titik tanpa angka selama filter ter-Apply
9. Klik ikon Filter pada toolbar tabel Usage
10. Klik `[Clear Field]`, lalu klik `[Apply]`
11. Verifikasi tabel menampilkan lima baris `Company A` sampai `Company E`
12. Verifikasi badge titik pada ikon Filter hilang

### TC-AC-DN-264: Search nama Company pada Usage by Company

13. Klik ikon Search pada toolbar tabel Usage
14. Verifikasi field Search menampilkan placeholder `Search by company name`
15. Ketik `company d`, tekan Enter
16. Verifikasi hanya baris `Company D` yang tampil
17. Verifikasi pencocokan tidak membedakan huruf besar dan kecil

### TC-AC-DN-593: Search tabel Usage by Company mencocokkan kolom Entity Type, Total SKU, dan Total Stock

18. Hapus teks pada input Search
19. Verifikasi input pencarian pada toolbar dialog Detail memuat placeholder "Search by company name"
20. Ketik `Distributor`, tekan Enter
21. Verifikasi tampil `Company B` dan `Company D` saja
22. Hapus teks pada input Search, ketik `3`, tekan Enter
23. Verifikasi tampil `Company A` saja
24. Hapus teks pada input Search, ketik `12`, tekan Enter
25. Verifikasi tampil `Company E` saja
26. Klik ikon `(✕)` pada input Search, lalu tekan Enter pada input kosong
27. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: filter kombinasi (TC-AC-DN-631) di depan dan dilepas sebelum Search; TC-AC-DN-593 memakai Search yang masih terbuka dari TC-AC-DN-264, sehingga langkah "Klik ikon Search" TC-AC-DN-593 digantikan menghapus teks pada input yang sudah terbuka.
- Langkah penghubung (S-03): `[Clear Field]` lalu `[Apply]` untuk melepas filter, membuka kembali Filter Panel setelah `[Apply]`, menghapus teks Search di antara kata kunci, dan klik `(✕)` lalu Enter pada input kosong untuk mereset tabel sebelum dialog ditutup. Siklus `(✕)` dan Enter pada input kosong diasersi di spec Search siklus Clear dan empty state.
- Input Search dikosongkan (langkah 18) sebelum asersi placeholder TC-AC-DN-593 butir a (langkah 19), karena placeholder hanya teramati pada input kosong; asersi ini juga tumpang tindih dengan TC-AC-DN-264 (langkah 14).
- Ukuran spec: di bawah smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - TC-AC-DN-631 menyebut "Apply" dan "Clear Field" tanpa bracket; spec memakai `[Apply]` dan `[Clear Field]` sesuai TC-AC-DN-630.
