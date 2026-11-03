---
id: TC-FA-TAG-E2E-049-download-tab-paired-pilihan-nama-berkas-search-filter-kolom-bagian-1
title: "Download Tab Paired: Pilihan CSV dan XLSX, Nama Berkas, serta Pengaruh Search, Filter, Kolom, dan Jumlah Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-219
  - TC-FA-TAG-220
  - TC-FA-TAG-221
  - TC-FA-TAG-224
  - TC-FA-TAG-225
  - TC-FA-TAG-226
  - TC-FA-TAG-227
coverage:
  web: automated
---

# Download Tab Paired: Pilihan CSV dan XLSX, Nama Berkas, serta Pengaruh Search, Filter, Kolom, dan Jumlah Baris

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Scope Download memuat 75 aset (20 + 20 + 25 + 10).
- Data khusus: AST-0043 (Excavator 20 Ton - 43, Tag QR-00231) berbrand Hitachi; Search `QR-00231` hanya cocok dengan baris AST-0043; Filter Brand `Hitachi` hanya cocok dengan aset berbrand Hitachi.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV dan XLSX (nama berkas, header kolom, jumlah baris, nama sheet) pada hook atau langkah; seed idempotent aset dan Brand lewat fixture backend (lihat `suite.md`).
- Pemulihan di hook `after`: kembalikan data Pre-setup tab Paired ke keadaan awal bila seeding mengubahnya. Konfigurasi kolom Popup Detail yang diubah pada langkah 25 dipulihkan pada langkah 30 (preferensi kolom spec ini tidak termasuk daftar pemulihan di `suite.md`).
- State global: tidak ada. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-219 dan TC-FA-TAG-220: pilihan Download dan Download CSV

1. Klik ikon Download pada Table Tools
2. Verifikasi overlay menampilkan pilihan `Download as CSV` dan `Download as XLSX`
3. Klik `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi file `Paired-TAGs.csv` terunduh
6. Verifikasi file berisi satu baris per aset (bukan per grup) sesuai kolom T-TAG-02 yang tampil

### TC-FA-TAG-221: Download XLSX

7. Klik ikon Download pada Table Tools
8. Klik `Download as XLSX`
9. Verifikasi tidak ada toast sukses
10. Verifikasi file `Paired-TAGs.xlsx` terunduh
11. Verifikasi file memuat satu sheet bernama `Sheet1`

### TC-FA-TAG-224: Download mengikuti Search

12. Ketik Search `QR-00231`, tekan Enter
13. Klik ikon Download pada Table Tools
14. Klik `Download as CSV`
15. Verifikasi file memuat sedikitnya satu baris
16. Verifikasi file hanya memuat baris AST-0043
17. Klik `(←)` pada kotak Search

### TC-FA-TAG-225: Download mengikuti Filter

18. Klik ikon Filter pada Table Tools
19. Pilih Brand `Hitachi`, lalu klik `[Apply]`
20. Klik ikon Download pada Table Tools
21. Klik `Download as CSV`
22. Verifikasi file memuat sedikitnya satu baris
23. Verifikasi file hanya memuat aset berbrand Hitachi
24. Hapus Filter Brand

### TC-FA-TAG-226: Download hanya memuat kolom yang tampil

25. Buka Popup Detail grup Excavator 20 Ton / Plant B, sembunyikan kolom Brand lewat Column Visibility, lalu tutup popup
26. Klik ikon Download pada Table Tools
27. Klik `Download as CSV`
28. Verifikasi file tidak memuat kolom Brand
29. Verifikasi kolom yang tampil ikut terunduh
30. Buka Popup Detail grup Excavator 20 Ton / Plant B, tampilkan kembali kolom Brand lewat Column Visibility, lalu tutup popup

### TC-FA-TAG-227: Download mencakup seluruh baris yang cocok

31. Atur page size 10
32. Klik ikon Download pada Table Tools
33. Klik `Download as CSV`
34. Verifikasi file memuat 75 baris data

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): 17 (mengosongkan Search lewat `(←)`), 24 (menghapus Filter), 30 (memulihkan kolom Brand). Langkah 25 menggabungkan langkah 1 dan 2 TC-FA-TAG-226 (buka Popup Detail, sembunyikan kolom Brand, tutup popup). Pilihan overlay Download yang masih terbuka dari TC-FA-TAG-219 dipakai TC-FA-TAG-220: langkah 1 memenuhi langkah klik ikon Download milik TC-FA-TAG-220 (S-04).
- Absence toast (langkah 4 dan 9) diletakkan sesudah pemicu klik pilihan format dan sebelum Verifikasi berkas terunduh; pemicu menjadi anchor yang buktinya menyusul pada langkah 5 dan 10 (bagian 8b butir 11).
- Asersi tambahan di luar Expected TC (S-03): langkah 15 dan 22 (file memuat sedikitnya satu baris sebagai pembanding asersi universal "hanya memuat", bagian 8b butir 2).
- Langkah 16 dan 23 membaca isi berkas hanya sebagai jumlah baris dan identitas baris (fungsional); isi sel, BOM, dan tipe sel (kelas f) tidak diasersi di spec ini.
- Langkah 31: TC-FA-TAG-227 menulis "Atur page size 10" yang sama dengan nilai default Pagination; langkah tetap ditulis sesuai TC.
- Temuan untuk QA:
  - TC-FA-TAG-226 tidak menyebut grup mana yang dibuka untuk menyembunyikan kolom Brand dan tidak menyebut pemulihan kolom di akhir TC; Post Condition-nya ("konfigurasi kolom tersimpan di cache browser") tidak punya langkah observasi sehingga tidak diasersi. Spec memilih grup Excavator 20 Ton / Plant B dan memulihkan kolom pada langkah 30. `suite.md` tidak mendaftarkan spec 049 pada pemulihan preferensi kolom.
  - TC-FA-TAG-225 menyebut hanya AST-0043 berbrand Hitachi tanpa menyebut brand aset lain; jumlah baris hasil Filter tidak ditentukan sehingga hanya asersi "hanya aset berbrand Hitachi".
  - TC-FA-TAG-224 mengharapkan "baris AST-0043" tanpa menyebut kolom yang dipakai mengenali baris di berkas; spec memakai ID aset.
  - TC-FA-TAG-220 mengharapkan toast sukses tidak ada tanpa anchor lain selain pemicu; anchor-nya berkas terunduh (langkah 5).
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; Lampiran A belum memuat butir untuk modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
