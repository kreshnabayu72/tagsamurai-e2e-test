---
id: TC-FA-TAG-E2E-196-t-tag-02-column-visibility-kolom-curated-bagian-2
title: "Tabel T-TAG-02: Column Visibility Kolom Curated dan Kolom Visible Terakhir (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-776
  - TC-FA-TAG-777
  - TC-FA-TAG-778
  - TC-FA-TAG-779
coverage:
  web: automated
---

# Tabel T-TAG-02: Column Visibility Kolom Curated dan Kolom Visible Terakhir (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-776: Menampilkan kolom curated Asset Value (Commercial) lewat Setup Column

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Klik header `⋯` lalu `Setup Column...`
3. Verifikasi sebelum dicentang kolom Asset Value (Commercial) tidak tampil
4. Centang Asset Value (Commercial) (default tidak tercentang)
5. Klik `[Save]`
6. Verifikasi setelah Save kolom Asset Value (Commercial) tampil di tabel

### TC-FA-TAG-777: Menampilkan kolom curated Asset Value (Fiscal) lewat Setup Column

7. Klik header `⋯` lalu `Setup Column...`
8. Verifikasi sebelum dicentang kolom Asset Value (Fiscal) tidak tampil
9. Centang Asset Value (Fiscal) (default tidak tercentang)
10. Klik `[Save]`
11. Verifikasi setelah Save kolom Asset Value (Fiscal) tampil di tabel

### TC-FA-TAG-778: Menampilkan kolom curated Warranty Expiry lewat Setup Column

12. Klik header `⋯` lalu `Setup Column...`
13. Verifikasi sebelum dicentang kolom Warranty Expiry tidak tampil
14. Centang Warranty Expiry (default tidak tercentang)
15. Klik `[Save]`
16. Verifikasi setelah Save kolom Warranty Expiry tampil di tabel

### TC-FA-TAG-779: Kolom visible terakhir pada T-TAG-02 tidak dapat di-uncheck

17. Klik header `⋯`
18. Hilangkan centang Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry yang disimpan TC sebelumnya
19. Hilangkan centang tujuh kolom default sehingga tersisa satu
20. Arahkan pointer ke checkbox kolom tersisa
21. Verifikasi Checkbox kolom tersisa disabled
22. Verifikasi Tooltip `At least one column must remain visible.` tampil
23. Tutup overlay Column Visibility
24. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 18, 23, 24.
- Popup Detail Excavator 20 Ton / Plant B dibuka sekali pada TC pertama dan dibiarkan terbuka antar TC.
- Urutan TC-FA-TAG-779 sesudah TC kolom curated dipertahankan; kolom curated yang disimpan TC sebelumnya dihilangkan dulu agar tepat satu kolom tersisa (langkah penghubung).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Hook `after` spec ini menghapus preferensi kolom; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-779 menyebut "tujuh kolom default" sedangkan kolom default ada delapan (Name, Asset ID, TAG Code, Brand, Model/Type, Group, Status, Last Updated); spec mengikuti TC (tersisa satu kolom).
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
