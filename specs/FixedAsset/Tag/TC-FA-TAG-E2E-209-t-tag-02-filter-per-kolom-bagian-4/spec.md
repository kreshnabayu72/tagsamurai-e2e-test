---
id: TC-FA-TAG-E2E-209-t-tag-02-filter-per-kolom-bagian-4
title: "Tabel T-TAG-02: Filter TAG Type, Category, Opsi Kosong, dan Field Kolom Curated (Bagian 4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-826
  - TC-FA-TAG-827
  - TC-FA-TAG-828
  - TC-FA-TAG-829
coverage:
  web: automated
---

# Tabel T-TAG-02: Filter TAG Type, Category, Opsi Kosong, dan Field Kolom Curated (Bagian 4)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-827: Category hierarki Heavy Equipment > Earthmoving.
- Kolom Label dan Warranty Expiry tidak ditampilkan (keadaan bawaan, belum dicentang di Setup Column) selama spec ini.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-826: Filter kolom TAG Code (label TAG Type) QR menyaring baris detail berdasarkan tipe Tag aset pada T-TAG-02

1. Klik ikon Filter
2. Verifikasi Filter Panel hanya memuat satu field `TAG Type`; tipe pada Asset Name tidak menjadi field filter terpisah
3. Pilih TAG Type `QR` pada field `TAG Type`
4. Klik `[Apply]`
5. Verifikasi tabel grup hanya memuat grup yang memuat baris detail dengan Tag bertipe QR: Excavator 20 Ton / Plant B dan Laptop Pro 14 / HQ tampil, Excavator 20 Ton / Plant A tidak tampil
6. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
7. Verifikasi Popup Detail Excavator 20 Ton / Plant B memuat AST-0044 dengan `QR-00232` dan setiap baris yang tampil memiliki minimal satu Tag bertipe QR
8. Tutup Popup Detail
9. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-827: Filter kolom Category (Tree Picker multi-select, "All categories")

10. Klik ikon Filter
11. Klik tombol field `Category` ("All categories")
12. Verifikasi Modal Tree Picker memuat tree Category penuh client dengan checkbox cascade parent ke turunan dan footer `[Cancel]` `[Select]`
13. Centang node `Heavy Equipment` (parent dari Earthmoving)
14. Klik `[Select]`
15. Verifikasi Nilai terpilih tampil sebagai chip
16. Klik `[Apply]`
17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
18. Ubah page size menjadi 25
19. Verifikasi Aset cocok bila Category-nya node terpilih atau turunannya: seluruh 20 aset Excavator 20 Ton tampil
20. Tutup Popup Detail
21. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-828: Filter tidak menyediakan opsi nilai kosong dan baris kosong tersaring keluar

22. Klik ikon Filter
23. Buka dropdown `Label`
24. Verifikasi opsi `Audit`, `Rental`, dan `Urgent` tampil pada dropdown `Label`
25. Verifikasi Tidak ada opsi untuk nilai kosong
26. Pilih opsi `Audit` pada field `Label`
27. Klik `[Apply]`
28. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
29. Ubah page size menjadi 25
30. Verifikasi Popup Detail memuat AST-0043 (berlabel Audit)
31. Verifikasi memilih opsi apa pun menyaring keluar aset tanpa Label: AST-0101 (tanpa Label) tidak tampil
32. Tutup Popup Detail
33. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-829: Field Filter kolom curated tetap ada walau kolom disembunyikan

34. Klik ikon Filter
35. Verifikasi Field `Label` dan `Warranty Expiry` tetap ada pada Filter Panel

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 8, 9, 17, 18, 20, 21, 32, 33.
- Langkah 24 (Verifikasi opsi `Audit`, `Rental`, dan `Urgent` tampil pada dropdown `Label`) adalah anchor positif untuk asersi absence pada langkah 25 (bagian 8b butir 2); asersi ini tidak ada di Expected TC-FA-TAG-828 dan dicatat sebagai asersi tambahan (S-03).
- Filter dipasang di toolbar halaman dan dibersihkan antar TC lewat langkah penghubung.
- Langkah penghubung TC-FA-TAG-827 membuka Popup Detail dan mengatur page size 25 agar Expected "seluruh 20 aset Excavator 20 Ton tampil" dapat diamati.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-827 tidak menyebut tabel mana (tabel grup atau Popup Detail) yang menampilkan "seluruh 20 aset"; spec mengamatinya di Popup Detail.
  - TC-FA-TAG-828 Expected b (memilih opsi menyaring keluar aset tanpa Label) tidak punya langkah di Langkah Uji; spec menambah pemilihan opsi `Audit`, `[Apply]`, dan pembukaan Popup Detail sebagai langkah aksi pendukung, dengan AST-0043 (berlabel Audit) sebagai pembanding positif.
  - TC tidak menyebut kontrol yang membersihkan Filter; langkah penghubung "Bersihkan Filter" dipakai tanpa nama tombol.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
