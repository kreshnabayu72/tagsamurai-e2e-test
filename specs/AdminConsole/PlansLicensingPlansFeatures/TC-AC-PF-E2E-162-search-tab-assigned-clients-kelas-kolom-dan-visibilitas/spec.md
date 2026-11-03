---
id: TC-AC-PF-E2E-162-search-tab-assigned-clients-kelas-kolom-dan-visibilitas
title: "Search Tab Assigned Clients: kelas kolom dan keterikatan pada visibilitas kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-414
  - TC-AC-PF-415
  - TC-AC-PF-416
  - TC-AC-PF-417
coverage:
  web: automated
---

# Search Tab Assigned Clients: kelas kolom dan keterikatan pada visibilitas kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten; penghapusan preferensi kolom Tab Assigned Clients di browser (disediakan tim FE) di hook `after`. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca data plan; Last Updated dan Changelog plan tidak berubah. Spec menyembunyikan lalu menampilkan kembali kolom `Assigned By` (konfigurasi kolom tersimpan di browser); hook `after` menghapus preferensi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

### Kelas teks pada Client Name dan Assigned By (TC-AC-PF-414)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Verifikasi tabel menampilkan sedikitnya satu baris (footer `Showing 1–9 of 9 entries`).
4. Ketik Search `jaya`, tekan Enter.
5. Verifikasi tabel menampilkan hanya baris `PT Timur Jaya`.
6. Ganti isi kotak search dengan `jane`, tekan Enter.
7. Verifikasi tabel menampilkan lima baris Assigned By `Jane S`: `PT Bumi Sentosa`, `PT Cahaya Mandiri`, `PT Hak Parsial Dua`, `PT Hak Parsial Satu`, `PT Karya Abadi`.

### Kelas badge dan angka pada Subscription Status dan Plan Version (TC-AC-PF-415)

8. Ganti isi kotak search dengan `grace`, tekan Enter.
9. Verifikasi tabel menampilkan baris `PT Cahaya Mandiri`.
10. Ganti isi kotak search dengan `v5`, tekan Enter.
11. Verifikasi tabel menampilkan baris `PT Cahaya Mandiri`, `PT Sejahtera Abadi`, dan `PT Zona Nol`.

### Assigned Date tidak dicocokkan (TC-AC-PF-416)

12. Klik `(←)` pada kotak Search.
13. Verifikasi Assigned Date seluruh sembilan baris berbulan `Jun`.
14. Ketik Search `Jun`, tekan Enter.
15. Verifikasi tabel menampilkan "No results found".

### Pencarian terikat visibilitas kolom (TC-AC-PF-417)

16. Klik `(←)` pada kotak Search.
17. Sembunyikan kolom `Assigned By` lewat Overlay Column Visibility (klik header `Column Visibility (⋯)`, hilangkan centang `Assigned By`, tutup overlay).
18. Ketik Search `john`, tekan Enter.
19. Verifikasi hasil "No results found" saat kolom `Assigned By` tersembunyi.
20. Tampilkan kembali kolom `Assigned By` lewat Overlay Column Visibility (klik header `Column Visibility (⋯)`, centang `Assigned By`, tutup overlay).
21. Ganti isi kotak search dengan `john`, tekan Enter.
22. Verifikasi tabel menampilkan empat baris John Doe: `PT Sejahtera Abadi`, `PT Timur Jaya`, `PT Wahana Nusantara`, `PT Zona Nol`.
23. Klik `(←)` pada kotak Search.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 12, 16, dan 23 (mereset Search); langkah 17 dan 20 (mengubah visibilitas kolom, bagian dari alur TC-AC-PF-417).
- Langkah 3 dan 13 menjadi pembanding positif bagi asersi tabel tersaring (langkah 5, 7, 9, 11, dan 22) dan bagi hasil kosong pada langkah 15 dan 19 (bagian 8b butir 2).
- Rangkaian Search memakai Enter sebagai pemicu; mengganti isi kotak yang sudah berisi ditulis "ganti isi kotak search dengan" (bagian 8b butir 9).
- Temuan untuk QA:
  - TC-AC-PF-417 ("Sembunyikan kolom", "Tampilkan kembali kolom") tidak menyebut cara menyembunyikan kolom; spec memakai Overlay Column Visibility seperti di TC-AC-PF-448.
  - TC-AC-PF-416 Expected menyebut "semua Assigned Date berbulan Jun" sebagai premis tanpa langkah mengamatinya; spec menambah langkah 13 sebagai pembuktian premis itu atas kolom Assigned Date.
