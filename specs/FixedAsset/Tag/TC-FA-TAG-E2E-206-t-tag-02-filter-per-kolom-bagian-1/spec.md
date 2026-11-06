---
id: TC-FA-TAG-E2E-206-t-tag-02-filter-per-kolom-bagian-1
title: "Tabel T-TAG-02: Filter per Kolom (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-814
  - TC-FA-TAG-815
  - TC-FA-TAG-816
  - TC-FA-TAG-817
coverage:
  web: automated
---

# Tabel T-TAG-02: Filter per Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-815: Brand: AST-0011 = Caterpillar; AST-0020 = Komatsu; AST-0021 = Caterpillar; AST-0043 = Hitachi; AST-0044 = Komatsu.
- Data TC-FA-TAG-816: Model/Type: AST-0011 = 320D; AST-0020 = PC200; AST-0021 = 330F; AST-0043 = ZX210; AST-0044 = PC300.
- Data TC-FA-TAG-817: Measurement seluruh aset = pcs.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-814: Kolom Asset ID pada T-TAG-02 tidak Filterable (Asset ID unik)

1. Klik ikon Filter pada Table Tools halaman
2. Verifikasi Filter Panel memuat field `Brand`
3. Verifikasi Filter Panel tidak memuat field `Asset ID`
4. Tutup Filter Panel

### TC-FA-TAG-815: Filter kolom Brand (multi-select searchable, "All brands") pada T-TAG-02

5. Klik ikon Filter pada Table Tools halaman
6. Pilih `Komatsu` pada field `Brand`
7. Klik `[Apply]`
8. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
9. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
10. Ubah page size menjadi 25
11. Verifikasi Popup Detail hanya memuat: AST-0020 dan AST-0044
12. Tutup Popup Detail
13. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-816: Filter kolom Model/Type (multi-select searchable, "All models") pada T-TAG-02

14. Klik ikon Filter pada Table Tools halaman
15. Pilih `PC200` pada field `Model/Type`
16. Klik `[Apply]`
17. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
18. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
19. Ubah page size menjadi 25
20. Verifikasi Popup Detail hanya memuat: AST-0020
21. Tutup Popup Detail
22. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-817: Filter kolom Measurement (multi-select searchable, "All units") pada T-TAG-02

23. Klik ikon Filter pada Table Tools halaman
24. Pilih `pcs` pada field `Measurement`
25. Klik `[Apply]`
26. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
27. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
28. Ubah page size menjadi 25
29. Verifikasi Popup Detail hanya memuat: seluruh 20 aset (satu-satunya opsi `pcs`, nilai sama pada seluruh baris)
30. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 4, 12, 13, 21, 22, 30.
- Filter dipasang di toolbar halaman dan dibersihkan antar TC lewat langkah penghubung; Popup Detail ditutup sebelum Filter dibuka kembali karena toolbar tertutup popup.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-814 tidak menyebut field lain pada Filter Panel; spec memakai field `Brand` (disebut TC-FA-TAG-815) sebagai pembanding positif sebelum asersi absence `Asset ID`.
  - TC tidak menyebut kontrol yang membersihkan Filter; langkah penghubung "Bersihkan Filter" dipakai tanpa nama tombol.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
