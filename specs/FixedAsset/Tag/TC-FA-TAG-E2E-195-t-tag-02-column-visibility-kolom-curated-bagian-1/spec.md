---
id: TC-FA-TAG-E2E-195-t-tag-02-column-visibility-kolom-curated-bagian-1
title: "Tabel T-TAG-02: Column Visibility Kolom Curated (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-771
  - TC-FA-TAG-772
  - TC-FA-TAG-773
  - TC-FA-TAG-774
  - TC-FA-TAG-775
coverage:
  web: automated
---

# Tabel T-TAG-02: Column Visibility Kolom Curated (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 5, 10, 15, 20, 25), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-771: Menampilkan kolom curated Measurement lewat Setup Column

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Klik header `⋯` lalu `Setup Column...`
3. Verifikasi sebelum dicentang kolom Measurement tidak tampil
4. Centang Measurement (default tidak tercentang)
5. Klik `[Save]`
6. Verifikasi setelah Save kolom Measurement tampil di tabel

### TC-FA-TAG-772: Menampilkan kolom curated Category lewat Setup Column

7. Klik header `⋯` lalu `Setup Column...`
8. Verifikasi sebelum dicentang kolom Category tidak tampil
9. Centang Category (default tidak tercentang)
10. Klik `[Save]`
11. Verifikasi setelah Save kolom Category tampil di tabel

### TC-FA-TAG-773: Menampilkan kolom curated Label lewat Setup Column

12. Klik header `⋯` lalu `Setup Column...`
13. Verifikasi sebelum dicentang kolom Label tidak tampil
14. Centang Label (default tidak tercentang)
15. Klik `[Save]`
16. Verifikasi setelah Save kolom Label tampil di tabel

### TC-FA-TAG-774: Menampilkan kolom curated Transactional Policy lewat Setup Column

17. Klik header `⋯` lalu `Setup Column...`
18. Verifikasi sebelum dicentang kolom Transactional Policy tidak tampil
19. Centang Transactional Policy (default tidak tercentang)
20. Klik `[Save]`
21. Verifikasi setelah Save kolom Transactional Policy tampil di tabel

### TC-FA-TAG-775: Menampilkan kolom curated Last Scanned lewat Setup Column

22. Klik header `⋯` lalu `Setup Column...`
23. Verifikasi sebelum dicentang kolom Last Scanned tidak tampil
24. Centang Last Scanned (default tidak tercentang)
25. Klik `[Save]`
26. Verifikasi setelah Save kolom Last Scanned tampil di tabel
27. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 27.
- Popup Detail Excavator 20 Ton / Plant B dibuka sekali pada TC pertama dan dibiarkan terbuka antar TC; kolom curated yang sudah disimpan tetap tampil pada TC berikutnya dan tidak mengganggu asersi "sebelum dicentang" kolom yang berbeda.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 5, 10, 15, 20, 25), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Hook `after` spec ini menghapus preferensi kolom; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-771 sampai 778 menulis "Sebelum dicentang kolom X tidak tampil" sebagai Expected a tanpa langkah amati sendiri; spec menaruh `Verifikasi` itu sesudah dialog Setup Column terbuka dan sebelum kolom dicentang.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
