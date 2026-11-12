---
id: TC-FA-TAG-E2E-208-t-tag-02-filter-per-kolom-bagian-3
title: "Tabel T-TAG-02: Filter per Kolom (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-822
  - TC-FA-TAG-823
  - TC-FA-TAG-824
  - TC-FA-TAG-825
coverage:
  web: automated
---

# Tabel T-TAG-02: Filter per Kolom (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-822: Asset Value (Commercial): AST-0011 = 500; AST-0020 = —; AST-0021 = 300; AST-0043 = 800; AST-0044 = 100.
- Data TC-FA-TAG-823: Asset Value (Fiscal): AST-0011 = 450; AST-0020 = —; AST-0021 = 250; AST-0043 = 700; AST-0044 = 90.
- Data TC-FA-TAG-824: Warranty Expiry: AST-0011 = 01 Mar 27; AST-0020 = —; AST-0021 = 31 Dec 26; AST-0043 = 01 Sep 26; AST-0044 = —.
- Data TC-FA-TAG-825: Last Updated: AST-0011 = 01 Oct 26; AST-0020 = 05 Oct 26; AST-0021 = 10 Oct 26; AST-0043 = 15 Oct 26; AST-0044 = 20 Oct 26.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-822: Filter kolom Asset Value (Commercial) (range Min-Max, "Min" / "Max") pada T-TAG-02

1. Klik ikon Filter pada Table Tools halaman
2. Isi `Min` 300 dan `Max` 800 pada field `Asset Value (Commercial)`
3. Klik `[Apply]`
4. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
5. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
6. Ubah page size menjadi 25
7. Verifikasi Popup Detail hanya memuat: AST-0011, AST-0021, dan AST-0043; AST-0020 (`—`) dan AST-0044 (100) tidak tampil
8. Tutup Popup Detail
9. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-823: Filter kolom Asset Value (Fiscal) (range Min-Max, "Min" / "Max") pada T-TAG-02

10. Klik ikon Filter pada Table Tools halaman
11. Isi `Min` 250 dan `Max` 450 pada field `Asset Value (Fiscal)`
12. Klik `[Apply]`
13. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
14. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
15. Ubah page size menjadi 25
16. Verifikasi Popup Detail hanya memuat: AST-0011 dan AST-0021
17. Tutup Popup Detail
18. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-824: Filter kolom Warranty Expiry (date range picker, "Select date") pada T-TAG-02

19. Klik ikon Filter pada Table Tools halaman
20. Pilih rentang 1 Des 2026 sampai 31 Des 2027 pada field `Warranty Expiry`
21. Klik `[Apply]`
22. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
23. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
24. Ubah page size menjadi 25
25. Verifikasi Popup Detail hanya memuat: AST-0011 dan AST-0021
26. Tutup Popup Detail
27. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-825: Filter kolom Last Updated (date range picker, "Select date") pada T-TAG-02

28. Klik ikon Filter pada Table Tools halaman
29. Pilih rentang 12 Okt 2026 sampai 25 Okt 2026 pada field `Last Updated`
30. Klik `[Apply]`
31. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
32. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
33. Ubah page size menjadi 25
34. Verifikasi Popup Detail hanya memuat: AST-0043 dan AST-0044
35. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 8, 9, 17, 18, 26, 27, 35.
- Filter dipasang di toolbar halaman dan dibersihkan antar TC lewat langkah penghubung; Popup Detail ditutup sebelum Filter dibuka kembali karena toolbar tertutup popup.
- Field Filter kolom curated (Asset Value, Warranty Expiry) tersedia tanpa menampilkan kolomnya, sehingga spec ini tidak memakai Setup Column.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Nilai Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry 15 aset lain (AST-0101 sampai AST-0115) tidak ditetapkan TC; Expected 'hanya memuat' TC-FA-TAG-822 sampai 824 mengandaikan nilai itu di luar rentang filter.
  - TC tidak menyebut kontrol yang membersihkan Filter; langkah penghubung "Bersihkan Filter" dipakai tanpa nama tombol.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
