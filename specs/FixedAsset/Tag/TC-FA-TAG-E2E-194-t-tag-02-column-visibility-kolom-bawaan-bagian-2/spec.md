---
id: TC-FA-TAG-E2E-194-t-tag-02-column-visibility-kolom-bawaan-bagian-2
title: "Tabel T-TAG-02: Column Visibility Kolom Bawaan (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-766
  - TC-FA-TAG-767
  - TC-FA-TAG-768
  - TC-FA-TAG-769
  - TC-FA-TAG-770
coverage:
  web: automated
---

# Tabel T-TAG-02: Column Visibility Kolom Bawaan (Bagian 2)

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

### TC-FA-TAG-766: Menyembunyikan dan menampilkan kembali kolom Brand pada T-TAG-02

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Klik header `⋯` pada tabel T-TAG-02
3. Hilangkan centang Brand
4. Verifikasi kolom Brand tidak tampil, langsung diterapkan tanpa Save
5. Centang kembali Brand
6. Verifikasi kolom Brand tampil kembali
7. Tutup overlay Column Visibility

### TC-FA-TAG-767: Menyembunyikan dan menampilkan kembali kolom Model/Type pada T-TAG-02

8. Klik header `⋯` pada tabel T-TAG-02
9. Hilangkan centang Model/Type
10. Verifikasi kolom Model/Type tidak tampil, langsung diterapkan tanpa Save
11. Centang kembali Model/Type
12. Verifikasi kolom Model/Type tampil kembali
13. Tutup overlay Column Visibility

### TC-FA-TAG-768: Menyembunyikan dan menampilkan kembali kolom Group pada T-TAG-02

14. Klik header `⋯` pada tabel T-TAG-02
15. Hilangkan centang Group
16. Verifikasi kolom Group tidak tampil, langsung diterapkan tanpa Save
17. Centang kembali Group
18. Verifikasi kolom Group tampil kembali
19. Tutup overlay Column Visibility

### TC-FA-TAG-769: Menyembunyikan dan menampilkan kembali kolom Status pada T-TAG-02

20. Klik header `⋯` pada tabel T-TAG-02
21. Hilangkan centang Status
22. Verifikasi kolom Status tidak tampil, langsung diterapkan tanpa Save
23. Centang kembali Status
24. Verifikasi kolom Status tampil kembali
25. Tutup overlay Column Visibility

### TC-FA-TAG-770: Menyembunyikan dan menampilkan kembali kolom Last Updated pada T-TAG-02

26. Klik header `⋯` pada tabel T-TAG-02
27. Hilangkan centang Last Updated
28. Verifikasi kolom Last Updated tidak tampil, langsung diterapkan tanpa Save
29. Centang kembali Last Updated
30. Verifikasi kolom Last Updated tampil kembali
31. Tutup overlay Column Visibility
32. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 7, 13, 19, 25, 31, 32.
- Popup Detail Excavator 20 Ton / Plant B dibuka sekali pada TC pertama dan dibiarkan terbuka antar TC; langkah "Klik Asset Name" TC berikutnya tidak diulang (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Hook `after` spec ini menghapus preferensi kolom; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
