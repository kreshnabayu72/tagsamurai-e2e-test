---
id: TC-FA-TAG-E2E-204-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-3
title: "Tabel T-TAG-02: Search per Kolom dan Nilai Sama (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-805
  - TC-FA-TAG-806
  - TC-FA-TAG-807
  - TC-FA-TAG-808
  - TC-FA-TAG-809
coverage:
  web: automated
---

# Tabel T-TAG-02: Search per Kolom dan Nilai Sama (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-805: Asset Value (Commercial) AST-0043 = 800.00; kata kunci `800.00`.
- Data TC-FA-TAG-806: Asset Value (Fiscal) AST-0044 = 90.00; kata kunci `90.00`.
- Data TC-FA-TAG-807: Measurement seluruh aset grup = pcs.
- Data TC-FA-TAG-808: Category seluruh aset grup = Earthmoving.
- Data TC-FA-TAG-809: Group seluruh aset grup = Plant B.
- Kolom Asset Value (Commercial), Asset Value (Fiscal), Measurement, dan Category ditampilkan lewat Setup Column sebelum Search (precondition TC: kolom yang dicari ditampilkan). Nilai sel Asset Value: lihat data TC.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 2), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-805: Search kolom Asset Value (Commercial) pada T-TAG-02

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Tampilkan kolom `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Measurement`, dan `Category` lewat Setup Column (header `⋯`, `Setup Column...`, centang keempat kolom, `[Save]`)
3. Tutup Popup Detail
4. Ketik Search `800.00`, tekan Enter
5. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
6. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
7. Ubah page size menjadi 25
8. Verifikasi Popup Detail hanya memuat: AST-0043 (sel berhak)
9. Tutup Popup Detail

### TC-FA-TAG-806: Search kolom Asset Value (Fiscal) pada T-TAG-02

10. Ganti isi kotak search dengan `90.00`, tekan Enter
11. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
12. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
13. Ubah page size menjadi 25
14. Verifikasi Popup Detail hanya memuat: AST-0044 (sel berhak)
15. Tutup Popup Detail

### TC-FA-TAG-807: Search kolom Measurement pada T-TAG-02 dengan nilai sama di seluruh baris

16. Ganti isi kotak search dengan `pcs`, tekan Enter
17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
18. Ubah page size menjadi 25
19. Verifikasi Popup Detail Excavator 20 Ton / Plant B memuat seluruh 20 aset karena semuanya cocok
20. Tutup Popup Detail

### TC-FA-TAG-808: Search kolom Category pada T-TAG-02 dengan nilai sama di seluruh baris

21. Ganti isi kotak search dengan `Earthmoving`, tekan Enter
22. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
23. Ubah page size menjadi 25
24. Verifikasi Popup Detail Excavator 20 Ton / Plant B memuat seluruh 20 aset karena semuanya cocok
25. Tutup Popup Detail

### TC-FA-TAG-809: Search kolom Group pada T-TAG-02 dengan nilai sama di seluruh baris

26. Ganti isi kotak search dengan `Plant B`, tekan Enter
27. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
28. Ubah page size menjadi 25
29. Verifikasi Popup Detail Excavator 20 Ton / Plant B memuat seluruh 20 aset karena semuanya cocok
30. Tutup Popup Detail
31. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 1, 2, 3, 9, 15, 20, 25, 30, 31.
- Search dipakai di toolbar halaman; isi kotak diganti pada TC berikutnya dan Search ditutup di akhir spec.
- Langkah penghubung di awal menampilkan keempat kolom curated sekaligus untuk memenuhi precondition TC-FA-TAG-805 sampai 808.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 2), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-807 sampai 809 memakai kata kunci yang cocok dengan seluruh baris; Expected menyebut "seluruh 20 aset" sehingga Popup Detail diamati pada page size 25.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
