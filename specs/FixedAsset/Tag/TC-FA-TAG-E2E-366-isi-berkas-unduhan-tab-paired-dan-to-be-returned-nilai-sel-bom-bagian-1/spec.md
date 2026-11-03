---
id: TC-FA-TAG-E2E-366-isi-berkas-unduhan-tab-paired-dan-to-be-returned-nilai-sel-bom-bagian-1
title: "Isi Berkas Unduhan: BOM, Nilai Sel, dan Scope Baris CSV Tab Paired, To Be Returned, dan Event Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-222
  - TC-FA-TAG-231
  - TC-FA-TAG-223
  - TC-FA-TAG-232
  - TC-FA-TAG-233
  - TC-FA-TAG-1311
  - TC-FA-TAG-1312
coverage:
  web: automated
---

# Isi Berkas Unduhan: BOM, Nilai Sel, dan Scope Baris CSV Tab Paired, To Be Returned, dan Event Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
  - Manage asset & TAG (Read + Update) (Update: Plant A) `manageAssetTagReadUpdateUpdatePlantA_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC, kode MU_PA), password `Spectra.env.FA_TAG_MU_PA_PASSWORD`. Dipakai pada langkah ganti akun (langkah 22 dan 23).
  - Manage asset & TAG (Read) dengan assign group Disposal Center `manageAssetTagReadDenganAssignGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC, kode MR_ADC), password `Spectra.env.FA_TAG_MR_ADC_PASSWORD`. Dipakai pada langkah ganti akun (langkah 27 dan 28).
  - Nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk ketiga akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV (byte awal, pemisah, isi sel, jumlah baris, nama berkas); penanganan unduhan file di browser; seed idempotent aset, Tag, dan entri Event Log lewat fixture backend; penghapusan preferensi kolom Setup Column di browser pada hook `after` (hook `after` spec ini menjalankannya karena Setup Column disimpan pada langkah 17).
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011. Group Head Office > Plant B; AST-0020 berstatus Assigned dan Tag Reported; AST-0021 tanpa Brand; AST-0044 berlabel Audit, Rental, Urgent dengan TAG Code `QR-00232, RF-00132`.
- Data Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.). Event Log berisi entri RF-00071 (Disposal Center) dan NF-00093 (HQ Warehouse).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom Setup Column di browser, kembalikan data seed ke keadaan awal, lalu kembalikan sesi ke akun default suite. Spec ini hanya membaca data (aksi hanya membaca).
- State global: preferensi kolom Setup Column pada browser (dipulihkan seperti di atas). Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-222 dan TC-FA-TAG-231: pemisah, BOM, dan format sel

1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi file CSV memakai pemisah koma
4. Verifikasi file CSV berencoding UTF-8 dengan BOM
5. Verifikasi sel Group memuat hierarki penuh `Head Office > Plant B`
6. Verifikasi sel Brand memuat nama penuh tanpa hierarki
7. Verifikasi sel Status AST-0020 `Assigned, Tag Reported`
8. Verifikasi sel yang kosong di tabel (`—`) ditulis `-`

### TC-FA-TAG-223: TAG Code aset multi-Tag

9. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
10. Tutup Popup Detail
11. Klik ikon Download
12. Klik `Download as CSV`
13. Verifikasi baris AST-0044 memuat TAG Code `QR-00232, RF-00132` pada satu sel
14. Verifikasi jumlah baris data sama dengan jumlah aset dalam scope (satu baris per aset)

### TC-FA-TAG-232: label aset

15. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
16. Klik header `⋯` lalu `Setup Column...`
17. Centang kolom Label lalu klik `[Save]`
18. Tutup Popup Detail
19. Klik ikon Download
20. Klik `Download as CSV`
21. Verifikasi sel Label baris AST-0044 `Audit, Rental, Urgent` (semua label tampil penuh, tanpa `+N more`)

### Ganti akun

22. Logout dari akun Total Control
23. Login sebagai Manage asset & TAG (Read + Update) (Update: Plant A) (MU_PA)

### TC-FA-TAG-233: scope user

24. Klik ikon Download
25. Klik `Download as CSV`
26. Verifikasi file memuat sedikitnya satu baris aset dan hanya memuat aset Plant A dan descendant

### Ganti akun

27. Logout dari akun MU_PA
28. Login sebagai Manage asset & TAG (Read) dengan assign group Disposal Center (MR_ADC)

### TC-FA-TAG-1311 dan TC-FA-TAG-1312: scope tab To Be Returned dan Event Log

29. Buka Fixed Asset > TAG > To Be Returned
30. Klik ikon Download lalu "Download as CSV"
31. Verifikasi file "To-Be-Returned-TAGs" memuat RF-00071 dan RF-00088
32. Verifikasi file "To-Be-Returned-TAGs" tidak memuat NF-00092
33. Klik "Event Log"
34. Klik ikon Download lalu "Download as CSV"
35. Verifikasi file "Event-Log-To-Be-Returned" hanya memuat entri RF-00071

## Notes

- Spec isi berkas (kelas f, binary buffer). Nama berkas, header, dan jumlah baris adalah asersi fungsional; nilai sel, BOM, dan scope baris dibaca lewat pembaca berkas.
- TC-FA-TAG-222 dan TC-FA-TAG-231 memakai satu unduhan (langkah 1 dan 2) karena langkah Download identik dan data tidak berubah di antaranya.
- Langkah penghubung (tanpa awalan `Verifikasi`): 9 dan 10 (membuka dan menutup popup yang disebut TC), 15 sampai 18 (menampilkan kolom Label lewat Setup Column), 22, 23, 27, 28 (ganti akun), 29 dan 33 (navigasi).
- Anchor positif absence dan asersi universal (bagian 8b butir 2): langkah 26 memuat pembanding "sedikitnya satu baris aset" sebelum klaim "hanya aset Plant A dan descendant"; langkah 31 (RF-00071 dan RF-00088 ada) mendahului langkah 32.
- Temuan untuk QA:
  - TC-FA-TAG-232 menyebut "setelah kolom Label ditampilkan" tanpa langkah menampilkannya; spec menambah langkah 15 sampai 18 lewat Setup Column.
  - Hook suite pada `suite.md` yang menghapus preferensi kolom Setup Column tidak mencantumkan spec ini; spec memulihkannya sendiri di hook `after`.
  - TC-FA-TAG-1311 dan TC-FA-TAG-1312 tidak menyebut cara membaca berkas selain "File ... hanya memuat"; spec memakai pembaca berkas CSV.
  - TC-FA-TAG-222 dan TC-FA-TAG-233 tidak menyebut Post Condition selain "aksi hanya membaca"; tidak diasersi.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
