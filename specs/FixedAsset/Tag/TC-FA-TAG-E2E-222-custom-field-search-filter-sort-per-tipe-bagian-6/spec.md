---
id: TC-FA-TAG-E2E-222-custom-field-search-filter-sort-per-tipe-bagian-6
title: "Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 6)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-894
  - TC-FA-TAG-895
  - TC-FA-TAG-896
  - TC-FA-TAG-897
coverage:
  web: automated
---

# Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 6)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-894: CF Multi-Dropdown: AST-0043 = Option Gamma, Option Delta; AST-0011 = Option Alpha.
- Data TC-FA-TAG-895: CF Multi-Dropdown: AST-0043 = Option Gamma, Option Delta; AST-0011 = Option Alpha; aset lain bernilai `—`.
- Data TC-FA-TAG-896: CF Numeric: AST-0043 = 1234; AST-0011 = 56; kata kunci `1234`.
- Data TC-FA-TAG-897: CF Numeric: AST-0043 = 1234; AST-0011 = 56.
- Nilai Custom Field pada aset acuan AST-0043 dan AST-0011 di-seed idempotent lewat fixture BE di hook `before` dan dihapus di hook `after`; Custom Field yang diuji berstatus Active, 15 aset lain tanpa nilai.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-894: Filter Custom Field bertipe Multi-Dropdown (multi-select searchable, OR)

1. Klik ikon Filter pada Table Tools halaman
2. Pilih `Option Gamma` pada field `CF Multi-Dropdown`
3. Klik `[Apply]`
4. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
5. Ubah page size menjadi 25
6. Verifikasi Popup Detail hanya memuat aset yang nilainya cocok dengan `Option Gamma`: AST-0043
7. Tutup Popup Detail
8. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-895: Sort tiga tahap Custom Field bertipe Multi-Dropdown (A-Z)

9. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
10. Tampilkan kolom `CF Multi-Dropdown` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
11. Ubah page size menjadi 25
12. Klik header kolom CF Multi-Dropdown sekali
13. Verifikasi setelah klik 1 (menaik): AST-0011 tampil sebelum AST-0043 (urutan A-Z), aset bernilai `—` di akhir
14. Klik header kolom CF Multi-Dropdown sekali lagi
15. Verifikasi setelah klik 2 (menurun): aset bernilai `—` di awal, lalu AST-0043 sebelum AST-0011
16. Klik header kolom CF Multi-Dropdown sekali lagi
17. Verifikasi setelah klik 3: sort netral dan urutan kembali ke bawaan Last Updated terbaru
18. Tutup Popup Detail

### TC-FA-TAG-896: Search kolom Custom Field bertipe Numeric

19. Ketik Search `1234`, tekan Enter
20. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
21. Tampilkan kolom `CF Numeric` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
22. Ubah page size menjadi 25
23. Verifikasi Popup Detail hanya memuat AST-0043 (nilai kolom CF Numeric mengandung `1234`)
24. Tutup Popup Detail
25. Klik `(←)` pada kotak Search

### TC-FA-TAG-897: Filter Custom Field bertipe Numeric (range Min-Max)

26. Klik ikon Filter pada Table Tools halaman
27. Isi `Min` 1000 dan `Max` 2000 pada field `CF Numeric`
28. Klik `[Apply]`
29. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
30. Ubah page size menjadi 25
31. Verifikasi Popup Detail hanya memuat AST-0043 (nilai di dalam rentang)
32. Verifikasi Aset tanpa nilai tersaring keluar
33. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 7, 8, 18, 24, 25, 33.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Search ditutup lewat `(←)` dan Filter dibersihkan sesudah tiap TC (langkah penghubung); pada TC sort, kolom Custom Field yang sudah ditampilkan TC pencarian sebelumnya dalam spec yang sama tidak ditampilkan ulang karena langkah itu akan menyembunyikannya.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini belum tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC Search Custom Field menulis Search sebelum kolomnya ditampilkan lewat Setup Column, sedangkan TC Search kolom lain mensyaratkan kolom yang dicari tampil (Search terikat visibilitas kolom); spec mengikuti urutan TC sehingga hasilnya bergantung pada apakah Search memindai Custom Field yang kolomnya belum tampil.
  - Seeding nilai Custom Field pada aset acuan dapat mengubah Last Updated aset itu dan menggeser urutan bawaan Last Updated terbaru; pemulihan lewat fixture BE di hook `after` perlu mengembalikan Last Updated.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
