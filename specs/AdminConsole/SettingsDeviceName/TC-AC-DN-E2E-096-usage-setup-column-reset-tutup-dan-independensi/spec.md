---
id: TC-AC-DN-E2E-096-usage-setup-column-reset-tutup-dan-independensi
title: "Usage by Company: Reset to Default, Tutup Modal Membuang Perubahan, dan Independensi dari List"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-636
  - TC-AC-DN-635
  - TC-AC-DN-595
coverage:
  web: automated
---

# Usage by Company: Reset to Default, Tutup Modal Membuang Perubahan, dan Independensi dari List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: konfigurasi Setup Column tabel Usage by Company tersimpan di cache browser per user (Column Visibility, urutan, dan pin). Hook `before` dan `after` spec ini memanggil kemampuan "hapus preferensi kolom Usage di browser" (`suite.md`; disediakan tim FE) sehingga spec mulai dan berakhir dari konfigurasi default. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, hover, tekan Esc, tarik-lepas (drag and drop) kolom di modal Setup Column, dan muat ulang halaman (F5).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik teks nama `Gate Antenna` pada kolom Device Name

### TC-AC-DN-636: Menutup modal Setup Column tabel Usage by Company lewat ikon close atau Esc membuang perubahan

2. Klik trigger Column Visibility pada header kolom Actions tabel Usage, lalu klik `Setup Column...`
3. Hapus centang `Total SKU` dan seret `Total Stock` ke posisi pertama
4. Klik ikon close `(✕)` pada modal Setup Column
5. Verifikasi modal tertutup dan tabel Usage tetap menampilkan keempat kolom dengan urutan default
6. Verifikasi tidak ada dialog konfirmasi pada penutupan lewat ikon close
7. Klik trigger Column Visibility pada header kolom Actions tabel Usage, lalu klik `Setup Column...`
8. Hapus centang `Entity Type`, lalu tekan Esc
9. Verifikasi modal tertutup dan tabel Usage tetap menampilkan keempat kolom dengan urutan default
10. Verifikasi tidak ada dialog konfirmasi pada penutupan lewat Esc

### TC-AC-DN-635: Reset to Default mengembalikan konfigurasi kolom tabel Usage by Company ke default setelah Save

11. Klik trigger Column Visibility pada header kolom Actions tabel Usage, lalu klik `Setup Column...`
12. Hapus centang `Entity Type`, seret `Total Stock` ke posisi pertama, dan pin `Company`
13. Klik `[Save]`
14. Klik trigger Column Visibility pada header kolom Actions tabel Usage, lalu klik `Setup Column...`
15. Klik `[Reset to Default]`
16. Verifikasi Live Preview menampilkan keempat kolom berurutan `Company`, `Entity Type`, `Total SKU`, `Total Stock` tanpa pin
17. Klik `[Save]`
18. Muat ulang halaman dengan F5, lalu klik teks nama `Gate Antenna` pada kolom Device Name
19. Verifikasi tabel Usage memakai urutan default `Company`, `Entity Type`, `Total SKU`, `Total Stock` dengan keempat kolom tampil dan tanpa pin

### TC-AC-DN-595: Konfigurasi Setup Column tabel Usage by Company tidak memengaruhi tabel List

20. Verifikasi toolbar tabel Usage memuat Search dan Filter, kolom Actions menjadi trigger Column Visibility dan Setup Column, dan tombol Download tidak ada
21. Verifikasi pagination tabel Usage memakai default global (10 baris per halaman)
22. Klik trigger Column Visibility pada header kolom Actions tabel Usage lalu hilangkan centang kolom `Total SKU`
23. Verifikasi kolom `Total SKU` tidak tampil pada tabel Usage
24. Klik ikon `[X]` pada dialog Detail
25. Verifikasi tabel List tetap menampilkan enam kolom data: `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`
26. Klik teks nama `Gate Antenna` pada kolom Device Name
27. Klik trigger Column Visibility pada header kolom Actions tabel Usage lalu centang kembali kolom `Total SKU`
28. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: blok yang membuang perubahan (TC-AC-DN-636) di depan karena tidak menyimpan apa pun; blok yang menyimpan lalu mereset (TC-AC-DN-635) sesudahnya dan mengembalikan konfigurasi ke default lewat Reset to Default (objek uji); hook `before` dan `after` menghapus preferensi kolom Usage di browser (kemampuan `suite.md`); blok TC-AC-DN-595 di akhir karena mengubah Column Visibility yang kemudian dipulihkan.
- Langkah penghubung (S-03): membuka kembali modal Setup Column di antara asersi, memuat ulang halaman dengan F5 dan membuka kembali dialog sebagai bagian asersi persistensi, mencentang kembali `Total SKU` agar konfigurasi kembali ke default, dan menutup dialog Detail dengan ikon `[X]`.
- Langkah "Perhatikan toolbar dan footer" pada TC-AC-DN-595 ditulis sebagai Verifikasi pada dialog yang sedang terbuka sebelum kolom disembunyikan, sebab Expected butir a mencakup keduanya.
- Ukuran spec (28 langkah): tidak melewati smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) atau tanpa langkah observasi pada TC spec ini tidak diasersi (S-01).
  - TC-AC-DN-595 menutup dialog dengan ikon `[X]` dan memeriksa List; urutan header List tidak diubah oleh spec.
