---
id: TC-FA-TAG-E2E-193-t-tag-02-column-visibility-kolom-bawaan-bagian-1
title: "Tabel T-TAG-02: Column Visibility Kolom Bawaan (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-760
  - TC-FA-TAG-761
  - TC-FA-TAG-762
  - TC-FA-TAG-763
  - TC-FA-TAG-764
  - TC-FA-TAG-765
coverage:
  web: automated
---

# Tabel T-TAG-02: Column Visibility Kolom Bawaan (Bagian 1)

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

### TC-FA-TAG-760: Screening overlay Column Visibility pada tabel T-TAG-02

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Klik header kolom terakhir `⋯` pada tabel T-TAG-02
3. Verifikasi Overlay memuat kolom default tercentang: Name, Asset ID, TAG Code, Brand, Model/Type, Group, Status, Last Updated
4. Verifikasi Kolom curated tidak tercentang: Measurement, Category, Label, Transactional Policy, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), Warranty Expiry, dan satu kolom per Custom Field Active
5. Verifikasi Item `Setup Column...` tampil di bagian bawah
6. Tutup overlay Column Visibility

### TC-FA-TAG-761: Urutan kolom T-TAG-02: TAG Code tepat setelah Asset ID

7. Verifikasi urutan kolom: `Name | Asset ID | TAG Code | Brand | Model/Type | Group | Status | Last Updated`
8. Verifikasi tidak ada kolom TAG terpisah selain TAG Code

### TC-FA-TAG-762: Urutan bawaan T-TAG-02 Last Updated terbaru di atas

9. Ubah page size menjadi 25
10. Verifikasi Urutan relatif lima aset acuan: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011
11. Verifikasi Tidak ada indikator sort aktif pada kolom lain

### TC-FA-TAG-763: Menyembunyikan dan menampilkan kembali kolom Name pada T-TAG-02

12. Klik header `⋯` pada tabel T-TAG-02
13. Hilangkan centang Name
14. Verifikasi kolom Name tidak tampil, langsung diterapkan tanpa Save
15. Centang kembali Name
16. Verifikasi kolom Name tampil kembali
17. Tutup overlay Column Visibility

### TC-FA-TAG-764: Menyembunyikan dan menampilkan kembali kolom Asset ID pada T-TAG-02

18. Klik header `⋯` pada tabel T-TAG-02
19. Hilangkan centang Asset ID
20. Verifikasi kolom Asset ID tidak tampil, langsung diterapkan tanpa Save
21. Centang kembali Asset ID
22. Verifikasi kolom Asset ID tampil kembali
23. Tutup overlay Column Visibility

### TC-FA-TAG-765: Menyembunyikan dan menampilkan kembali kolom TAG Code pada T-TAG-02

24. Klik header `⋯` pada tabel T-TAG-02
25. Hilangkan centang TAG Code
26. Verifikasi kolom TAG Code tidak tampil, langsung diterapkan tanpa Save
27. Centang kembali TAG Code
28. Verifikasi kolom TAG Code tampil kembali
29. Tutup overlay Column Visibility
30. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 6, 17, 23, 29, 30.
- Popup Detail Excavator 20 Ton / Plant B dibuka sekali pada TC pertama dan dibiarkan terbuka antar TC; langkah "Klik Asset Name" TC berikutnya tidak diulang (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Pemicu observasi "Amati urutan header kolom" (TC-FA-TAG-761) dan "Amati ..." TC lain ditulis sebagai `Verifikasi` langsung.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Hook `after` spec ini menghapus preferensi kolom; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
