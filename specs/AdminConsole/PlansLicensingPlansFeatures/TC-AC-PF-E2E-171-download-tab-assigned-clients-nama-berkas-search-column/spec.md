---
id: TC-AC-PF-E2E-171-download-tab-assigned-clients-nama-berkas-search-column
title: "Download Tab Assigned Clients: nama berkas, mengikuti Search dan Column Visibility, dan hasil kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-444
  - TC-AC-PF-447
  - TC-AC-PF-448
  - TC-AC-PF-449
coverage:
  web: automated
---

# Download Tab Assigned Clients: nama berkas, mengikuti Search dan Column Visibility, dan hasil kosong

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten, penangkapan berkas unduhan browser, dan pembacaan isi berkas CSV; penghapusan preferensi kolom Tab Assigned Clients di browser (disediakan tim FE). Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec menyembunyikan lalu menampilkan kembali kolom `Assigned By` (konfigurasi kolom tersimpan di browser); hook `after` menghapus preferensi kolom. Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Overlay Download dan nama berkas (TC-AC-PF-444)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Hover ikon Download.
4. Verifikasi tooltip `Download` tampil.
5. Klik ikon Download.
6. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`.
7. Pilih `Download as CSV`.
8. Verifikasi tidak ada toast sukses.
9. Verifikasi berkas CSV terunduh bernama `Assigned-Clients-Growth.csv`.
10. Klik ikon Download → `Download as XLSX`.
11. Verifikasi tidak ada toast sukses.
12. Verifikasi berkas XLSX terunduh bernama `Assigned-Clients-Growth.xlsx`.

### Download mengikuti Search (TC-AC-PF-447)

13. Ketik Search `abadi`, tekan Enter.
14. Klik ikon Download → `Download as CSV`.
15. Buka berkas CSV.
16. Verifikasi berkas memuat tepat dua baris data, yaitu `PT Karya Abadi` dan `PT Sejahtera Abadi`.

### Download mengikuti Column Visibility (TC-AC-PF-448)

17. Klik `(←)` pada kotak Search.
18. Sembunyikan kolom `Assigned By` lewat Overlay Column Visibility (klik header `Column Visibility (⋯)`, hilangkan centang `Assigned By`, tutup overlay).
19. Klik ikon Download → `Download as CSV`.
20. Verifikasi tidak ada toast atau dialog peringatan.
21. Buka berkas CSV.
22. Verifikasi header berkas tidak memuat kolom `Assigned By`.
23. Verifikasi kolom lain yang tampil (`Client Name`, `Subscription Status`, `Plan Version`, `Assigned Date`) ikut diekspor.
24. Tampilkan kembali kolom `Assigned By` lewat Overlay Column Visibility (klik header `Column Visibility (⋯)`, centang `Assigned By`, tutup overlay).

### Download hasil kosong (TC-AC-PF-449)

25. Ketik Search `zzzzz`, tekan Enter (hasil kosong).
26. Verifikasi tombol Download tetap aktif.
27. Klik ikon Download → `Download as CSV`.
28. Verifikasi tidak ada toast sukses.
29. Buka berkas CSV.
30. Verifikasi berkas hanya berisi baris header kolom yang tampil.
31. Verifikasi berkas tidak memuat baris data.
32. Klik `(←)` pada kotak Search.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 17 dan 32 (mereset Search), 18 dan 24 (mengubah visibilitas kolom sesuai alur TC-AC-PF-448).
- Asersi absence toast (langkah 8, 11, 20, 28) diletakkan segera setelah pemicu unduhan dan sebelum asersi berkas (bagian 8b butir 11); pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 9 dan 12) atau pembacaan berkas (langkah 15, 21, 29).
- Nama berkas, header, dan jumlah baris adalah asersi fungsional (bagian 3 prinsip 13 butir f); nilai sel dan encoding berkas diasersi di spec 172.
- Temuan untuk QA:
  - TC-AC-PF-447 Expected ("Berkas hanya memuat `PT Karya Abadi` dan `PT Sejahtera Abadi`") mengasersi nilai sel Client Name pada berkas, yang termasuk kelas f (isi berkas); TC ini ada di spec fungsional ini dan perlu dikonfirmasi apakah dipindah ke spec isi berkas.
  - TC-AC-PF-448 tidak menyebut cara menyembunyikan kolom; spec memakai Overlay Column Visibility sesuai nama langkahnya.
  - TC-AC-PF-444 Expected b menyebut berkas XLSX "terunduh bernama `Assigned-Clients-Growth.xlsx`" tanpa langkah membuka berkas; spec hanya mengasersi nama berkas.
