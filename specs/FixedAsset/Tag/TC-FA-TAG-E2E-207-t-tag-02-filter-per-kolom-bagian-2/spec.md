---
id: TC-FA-TAG-E2E-207-t-tag-02-filter-per-kolom-bagian-2
title: "Tabel T-TAG-02: Filter per Kolom (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-818
  - TC-FA-TAG-819
  - TC-FA-TAG-820
  - TC-FA-TAG-821
coverage:
  web: automated
---

# Tabel T-TAG-02: Filter per Kolom (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-818: Label: AST-0043 [Audit]; AST-0044 [Audit, Rental, Urgent].
- Data TC-FA-TAG-819: Status: AST-0020 [Assigned, Tag Reported]; AST-0043 [Available, Tag Reported].
- Data TC-FA-TAG-820: Opsi: Borrow, Self Service Borrow, Assign, Transfer.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-818: Filter kolom Label (multi-select searchable, "All labels", opsi berbadge warna label) pada T-TAG-02

1. Klik ikon Filter pada Table Tools halaman
2. Pilih `Audit` pada field `Label`
3. Klik `[Apply]`
4. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
5. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
6. Ubah page size menjadi 25
7. Verifikasi Popup Detail hanya memuat: AST-0043 dan AST-0044 (salah satu label sama dengan opsi, OR)
8. Tutup Popup Detail
9. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-819: Filter kolom Status (multi-select searchable, "All statuses") pada T-TAG-02

10. Klik ikon Filter pada Table Tools halaman
11. Pilih `Tag Reported` pada field `Status`
12. Klik `[Apply]`
13. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
14. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
15. Ubah page size menjadi 25
16. Verifikasi Popup Detail hanya memuat: AST-0020 dan AST-0043 (salah satu badge sama, OR)
17. Tutup Popup Detail
18. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-820: Filter kolom Transactional Policy (multi-select, "All transactions", empat opsi tetap) pada T-TAG-02

19. Klik ikon Filter pada Table Tools halaman
20. Pilih `Transfer` pada field `Transactional Policy`
21. Klik `[Apply]`
22. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
23. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
24. Ubah page size menjadi 25
25. Verifikasi Popup Detail hanya memuat: seluruh 20 aset (policy Transfer On dimiliki Asset Name)
26. Tutup Popup Detail
27. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-821: Filter kolom Last Scanned (date range picker, "Select date") pada T-TAG-02

28. Klik ikon Filter pada Table Tools halaman
29. Pilih rentang 15 Okt 2026 sampai 30 Okt 2026 pada field `Last Scanned`
30. Klik `[Apply]`
31. Verifikasi Tabel grup hanya memuat grup yang memuat baris cocok (Excavator 20 Ton / Plant B)
32. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
33. Ubah page size menjadi 25
34. Verifikasi Popup Detail hanya memuat: AST-0011 dan AST-0021; aset dengan Last Scanned `—` (AST-0020, AST-0044) tidak tampil
35. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 8, 9, 17, 18, 26, 27, 35.
- Filter dipasang di toolbar halaman dan dibersihkan antar TC lewat langkah penghubung; Popup Detail ditutup sebelum Filter dibuka kembali karena toolbar tertutup popup.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - TC tidak menyebut kontrol yang membersihkan Filter; langkah penghubung "Bersihkan Filter" dipakai tanpa nama tombol.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
