---
id: TC-AC-DN-E2E-097-usage-pagination-reset-state-dan-klik-baris
title: "Usage by Company: Pagination, Klik Baris, dan Dialog Dibuka Kembali Mereset State"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-617
  - TC-AC-DN-592
  - TC-AC-DN-652
coverage:
  web: automated
---

# Usage by Company: Pagination, Klik Baris, dan Dialog Dibuka Kembali Mereset State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, hover, tekan Esc, tarik-lepas (drag and drop) kolom di modal Setup Column, dan muat ulang halaman (F5).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DN-617: Kontrol pagination tabel Usage by Company: default 10, opsi page size, dan navigasi pada lima baris

1. Klik teks nama `Gate Antenna` pada kolom Device Name
2. Verifikasi footer tabel Usage memuat selector jumlah data per halaman bernilai 10, navigasi halaman, dan input nomor halaman
3. Klik selector jumlah data per halaman di footer tabel Usage
4. Verifikasi Overlay Page Size memuat opsi `10 | 25 | 50 | 100` dan tidak ada opsi "All"
5. Verifikasi indikator halaman menunjukkan halaman 1 dan tombol halaman berikutnya serta sebelumnya tidak aktif
6. Pilih `25`
7. Verifikasi kelima baris `Company A` sampai `Company E` tetap tampil pada halaman 1
8. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-592: Klik baris tabel Usage by Company di luar kontrol tidak membuka apa pun

9. Klik teks nama `Gate Antenna` pada kolom Device Name
10. Klik sel Company pada baris `Company A`
11. Verifikasi tidak ada perubahan: dialog Device Name Detail tetap tampil tanpa dialog atau popup tambahan dan tidak ada navigasi halaman
12. Klik sel Total SKU pada baris `Company A`
13. Verifikasi tidak ada perubahan: dialog Device Name Detail tetap tampil tanpa dialog atau popup tambahan dan tidak ada navigasi halaman
14. Verifikasi kolom Company dan Total SKU tidak berupa tautan
15. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-652: Dialog Detail ditutup lalu dibuka kembali mengembalikan Search, Filter, Sort, dan Pagination tabel Usage by Company ke default

16. Klik teks nama `Gate Antenna` pada kolom Device Name
17. Verifikasi tabel Usage memuat lima baris `Company A` sampai `Company E`
18. Klik ikon Filter pada toolbar tabel Usage, isi field `Total SKU` Min `2` dan Max `3`, lalu klik `[Apply]`
19. Verifikasi baris `Company A` dan `Company B` tampil
20. Klik ikon Search pada toolbar tabel Usage, ketik `company a`, tekan Enter
21. Verifikasi baris `Company A` tampil
22. Klik header kolom `Total Stock` satu kali
23. Verifikasi sort ascending aktif pada kolom `Total Stock`
24. Ubah page size menjadi 25 lewat Overlay Page Size footer tabel Usage
25. Verifikasi tabel dimuat ulang dengan page size 25
26. Klik ikon `[X]` pada dialog Detail
27. Klik teks nama `Gate Antenna` pada kolom Device Name
28. Verifikasi Search: kolom pencarian kembali ke ikon Search dan tidak ada kata kunci aktif
29. Verifikasi Filter: ikon Filter tanpa badge titik
30. Klik ikon Filter pada toolbar tabel Usage
31. Verifikasi field `Total SKU` dan `Total Stock` menampilkan placeholder `Min` dan `Max` tanpa nilai
32. Verifikasi Sort: tidak ada indikator sort pada header kolom mana pun dan urutan kembali ke default Company A-Z
33. Verifikasi Pagination: Overlay Page Size menunjukkan 10 dan indikator halaman aktif menunjukkan halaman 1
34. Verifikasi tabel Usage menampilkan lima baris: `Company A`, `Company B`, `Company C`, `Company D`, `Company E`
35. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: pagination (TC-AC-DN-617) lalu klik sel (TC-AC-DN-592), dan TC-AC-DN-652 di akhir karena membuka kembali dialog untuk menilai reset state. Dialog ditutup dengan ikon `[X]` di antara blok sehingga tiap blok dimulai dari state default (S-09, S-03).
- Asersi Search pada blok TC-AC-DN-652 ("kolom pencarian kembali ke ikon Search") dan Overlay Page Size diperiksa sesudah dialog dibuka kembali; panel Filter dibuka hanya untuk melihat placeholder.
- Ukuran spec (35 langkah): tidak melewati smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) atau tanpa langkah observasi pada TC spec ini tidak diasersi (S-01).
  - TC-AC-DN-617 membahas "lima baris"; Pre-setup #18 mencantumkan `Company F` sampai `Company I` untuk `Gate Antenna` yang dikhususkan bagi TC lain, dan spec mengasumsikan baris itu tidak ada.
