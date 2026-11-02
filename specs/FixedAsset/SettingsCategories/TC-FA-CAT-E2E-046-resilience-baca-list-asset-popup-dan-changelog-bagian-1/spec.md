---
id: TC-FA-CAT-E2E-046-resilience-baca-list-asset-popup-dan-changelog-bagian-1
title: "Resilience Baca Bagian 1: Error Load List Kategori, Loading dan Error Tabel Assets Popup Detail, serta Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-13
  - TC-FA-CAT-287
  - TC-FA-CAT-415
coverage:
  web: automated
---

# Resilience Baca Bagian 1: Error Load List Kategori, Loading dan Error Tabel Assets Popup Detail, serta Changelog

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons baca list kategori, data aset Popup Detail, dan Changelog ditahan atau dipaksa 5xx lewat `Spectra.intercept()`, sedangkan data normal dari backend nyata diasersi).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #20 (CatMain): `Electronics` (internal) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12). Data Pre-setup #21 dan #22: aset `Laptop` (12 aset terhitung) dipakai Popup Detail. Data Pre-setup #23: 12 baris riwayat Changelog CatMain dipakai sebagai konten Changelog. Spec tidak membuat atau mengubah data.
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`):
  - TC-FA-CAT-13: respons list kategori dipaksa 5xx.
  - TC-FA-CAT-287: respons data aset Popup Detail ditunda 3 detik, lalu dipaksa 5xx.
  - TC-FA-CAT-415: respons Changelog ditunda 3 detik, lalu dipaksa 5xx.
  Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah. Endpoint yang di-intercept mengikuti halaman; tidak ada endpoint karangan.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-13: Gagal memuat list menampilkan error load

1. Paksa respons list kategori gagal 5xx lewat intercept jaringan
2. Buka Fixed Asset > Settings > Categories lewat menu sidebar
3. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
4. Verifikasi empty state `No subcategory yet` dan `No results found` tidak tampil
5. Verifikasi tidak ada toast yang memuat tombol aksi
6. Lepas intercept respons list kategori
7. Klik `[Try Again]`
8. Verifikasi data kategori tampil normal (sedikitnya satu baris kategori)

### TC-FA-CAT-287: Loading dan error fetch tabel Assets terbatas di area tabel popup

9. Klik node `Electronics` di sidebar
10. Tunda respons data aset 3 detik lewat intercept jaringan
11. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
12. Verifikasi area tabel Assets menampilkan loading component
13. Verifikasi header dan toolbar popup tetap tampil
14. Lepas penundaan respons data aset
15. Klik icon close (✕) pada Popup Detail
16. Paksa respons data aset gagal 5xx lewat intercept jaringan
17. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
18. Verifikasi area tabel Assets menampilkan `Unable to load this data.` dan `[Try Again]`
19. Verifikasi header popup tidak terpengaruh
20. Lepas intercept respons data aset
21. Klik icon close (✕) pada Popup Detail
22. Klik node `All Categories` di sidebar

### TC-FA-CAT-415: Loading dan error fetch Changelog terbatas di area tabel

23. Tunda respons Changelog 3 detik lewat intercept jaringan
24. Klik icon Changelog di Table Tools
25. Verifikasi loading hanya tampil di area tabel Changelog
26. Verifikasi header dan toolbar Changelog tetap tampil
27. Lepas penundaan respons Changelog
28. Tutup modal Changelog
29. Paksa respons Changelog gagal 5xx lewat intercept jaringan
30. Klik icon Changelog di Table Tools
31. Verifikasi area tabel Changelog menampilkan `Unable to load this data.` dan `[Try Again]`
32. Lepas intercept respons Changelog
33. Tutup modal Changelog

## Notes

- Mode: FE+BE (kelas b, fault injection). TC-FA-CAT-645, 646, dan 454 ada di spec 047.
- Langkah penghubung (S-03, S-09): langkah 6, 14, 20, 27, 32 (melepas intercept agar tidak bocor ke blok berikutnya), langkah 9 dan 22 (memilih node `Electronics` untuk menampilkan baris `Laptop`, lalu kembali ke `All Categories`), langkah 15, 21, 28, 33 (menutup popup atau modal).
- Verifikasi langkah 3, 18, 31 memuat teks error dan tombol `[Try Again]` dalam satu Verifikasi karena Expected TC menyebut keduanya sebagai satu butir elemen komposit.
- Temuan untuk QA:
  - TC-FA-CAT-287 dan 415 tidak menyatakan keadaan sesudah loading selesai atau sesudah `[Try Again]` diklik; spec tidak mengasersi keadaan itu (hanya Expected a dan b).
  - TC-FA-CAT-13 Expected b menyebut `[Try Again]` hanya ada pada state error load; spec memverifikasi tidak adanya toast beraksi sesuai TC, tanpa memeriksa tombol di surface lain.
