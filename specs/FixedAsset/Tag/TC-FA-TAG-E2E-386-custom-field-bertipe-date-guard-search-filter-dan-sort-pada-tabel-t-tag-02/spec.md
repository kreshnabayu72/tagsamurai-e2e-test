---
id: TC-FA-TAG-E2E-386-custom-field-bertipe-date-guard-search-filter-dan-sort-pada-tabel-t-tag-02
title: "Custom Field Bertipe Date pada Tabel T-TAG-02: Guard Search, Filter, dan Sort"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-905
  - TC-FA-TAG-906
  - TC-FA-TAG-907
coverage:
  web: automated
---

# Custom Field Bertipe Date pada Tabel T-TAG-02: Guard Search, Filter, dan Sort

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-905: CF Date: AST-0043 = 15 Okt 2026; AST-0011 = 01 Okt 2026.
- Data TC-FA-TAG-906: CF Date: AST-0043 = 15 Okt 2026; AST-0011 = 01 Okt 2026.
- Data TC-FA-TAG-907: CF Date: AST-0043 = 15 Okt 2026; AST-0011 = 01 Okt 2026; aset lain bernilai `—`.
- Nilai Custom Field pada aset acuan AST-0043 dan AST-0011 di-seed idempotent lewat fixture BE di hook `before` dan dihapus di hook `after`; Custom Field yang diuji berstatus Active, 15 aset lain tanpa nilai.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Nilai literal Pre-setup (nama aset, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR). Nilai Custom Field pada AST-0043 dan AST-0011 di-seed dan dihapus lewat fixture backend di hook `before` dan `after`, dan [Save] Setup Column (langkah 2) hanya menyimpan preferensi kolom di browser yang dihapus di hook `after`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-905: Guard: Custom Field bertipe Date tidak dapat dicari

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Tampilkan kolom `CF Date` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
3. Catat teks sel kolom `CF Date` baris AST-0043 persis seperti tampil
4. Tutup Popup Detail
5. Ketik Search nilai kolom `CF Date` AST-0043 persis seperti tampil (teks yang dicatat pada langkah 3), tekan Enter
6. Verifikasi `No results found`: Custom Field bertipe Date tidak punya Search
7. Klik `(←)` pada kotak Search

### TC-FA-TAG-906: Filter Custom Field bertipe Date (date range picker)

8. Klik ikon Filter pada Table Tools halaman
9. Pilih rentang 12 Okt 2026 sampai 25 Okt 2026 pada field `CF Date`
10. Klik `[Apply]`
11. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
12. Ubah page size menjadi 25
13. Verifikasi Popup Detail hanya memuat AST-0043
14. Verifikasi Aset tanpa nilai tersaring keluar
15. Tutup Popup Detail
16. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-907: Sort tiga tahap Custom Field bertipe Date (tanggal (Oldest First lalu Newest First))

17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
18. Ubah page size menjadi 25
19. Klik header kolom CF Date sekali
20. Verifikasi setelah klik 1 (menaik): AST-0011 tampil sebelum AST-0043 (urutan tanggal (Oldest First lalu Newest First)), aset bernilai `—` di akhir
21. Klik header kolom CF Date sekali lagi
22. Verifikasi setelah klik 2 (menurun): aset bernilai `—` di awal, lalu AST-0043 sebelum AST-0011
23. Klik header kolom CF Date sekali lagi
24. Verifikasi setelah klik 3: sort netral dan urutan kembali ke bawaan Last Updated terbaru
25. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 1, 2, 3, 4, 7, 15, 16, 25.
- Pembagian TC lintas spec: TC-FA-TAG-902 sampai 904 ada di spec `TC-FA-TAG-E2E-224-custom-field-search-filter-sort-per-tipe-bagian-8`; TC-FA-TAG-908 sampai 911 ada di spec `TC-FA-TAG-E2E-225-custom-field-search-filter-sort-per-tipe-bagian-9`.
- Langkah 1 sampai 4 (penghubung) membuka Popup Detail, menampilkan kolom `CF Date`, dan mencatat teks sel AST-0043 agar Search pada langkah 5 memakai teks persis seperti tampil dan hasil `No results found` bukan akibat kolom tersembunyi atau salah format.
- Langkah 15 dan 16 (penghubung) menutup Popup Detail dan membersihkan Filter sebelum TC-FA-TAG-907, supaya Sort tidak berjalan di atas hasil filter TC-FA-TAG-906.
- Kolom `CF Date` ditampilkan pada langkah 2 dan tidak ditampilkan ulang pada TC-FA-TAG-907 karena langkah itu akan menyembunyikannya; Search ditutup lewat `(←)` sesudah TC-FA-TAG-905.
- A-15: nilai literal Pre-setup (nama aset, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR). Nilai Custom Field pada AST-0043 dan AST-0011 di-seed dan dihapus lewat fixture backend di hook `before` dan `after`, dan [Save] Setup Column (langkah 2) hanya menyimpan preferensi kolom di browser yang dihapus di hook `after`.
- Temuan untuk QA:
  - Seeding nilai Custom Field pada aset acuan dapat mengubah Last Updated aset itu dan menggeser urutan bawaan Last Updated terbaru; pemulihan lewat fixture BE di hook `after` perlu mengembalikan Last Updated.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
