---
id: TC-FA-TAG-E2E-203-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-2
title: "Tabel T-TAG-02: Search per Kolom (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-801
  - TC-FA-TAG-802
  - TC-FA-TAG-803
  - TC-FA-TAG-804
coverage:
  web: automated
---

# Tabel T-TAG-02: Search per Kolom (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-801: kata kunci `Hitachi`; Brand: AST-0011 = Caterpillar; AST-0020 = Komatsu; AST-0021 = Caterpillar; AST-0043 = Hitachi; AST-0044 = Komatsu.
- Data TC-FA-TAG-802: kata kunci `ZX210`; Model/Type: AST-0011 = 320D; AST-0020 = PC200; AST-0021 = 330F; AST-0043 = ZX210; AST-0044 = PC300.
- Data TC-FA-TAG-803: Label: AST-0020 [Urgent]; AST-0021 [Rental, Urgent]; AST-0044 [Audit, Rental, Urgent]; kata kunci `Urgent`.
- Data TC-FA-TAG-804: kata kunci `tag reported`; Status: AST-0011 = Available; AST-0020 = Assigned, Tag Reported; AST-0021 = In Transfer Process; AST-0043 = Available, Tag Reported; AST-0044 = Available.
- Kolom Brand, Model/Type, dan Status tampil secara bawaan; kolom Label ditampilkan lewat Setup Column sebelum Search TC-FA-TAG-803 (precondition TC: kolom yang dicari ditampilkan).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 14), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-801: Search kolom Brand pada T-TAG-02

1. Ketik Search `Hitachi`, tekan Enter
2. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
3. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
4. Ubah page size menjadi 25
5. Verifikasi Popup Detail hanya memuat: AST-0043
6. Tutup Popup Detail

### TC-FA-TAG-802: Search kolom Model/Type pada T-TAG-02

7. Ganti isi kotak search dengan `ZX210`, tekan Enter
8. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
9. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
10. Ubah page size menjadi 25
11. Verifikasi Popup Detail hanya memuat: AST-0043
12. Tutup Popup Detail

### TC-FA-TAG-803: Search kolom Label (termasuk label di balik +N more) pada T-TAG-02

13. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
14. Tampilkan kolom `Label` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
15. Tutup Popup Detail
16. Ganti isi kotak search dengan `Urgent`, tekan Enter
17. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
18. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
19. Ubah page size menjadi 25
20. Verifikasi Popup Detail hanya memuat: AST-0020, AST-0021, dan AST-0044 (Urgent tersembunyi di balik `+1 more`)
21. Tutup Popup Detail

### TC-FA-TAG-804: Search kolom Status (badge mana pun, tanpa membedakan huruf) pada T-TAG-02

22. Ganti isi kotak search dengan `tag reported`, tekan Enter
23. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
24. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
25. Ubah page size menjadi 25
26. Verifikasi Popup Detail hanya memuat: AST-0020 dan AST-0043
27. Tutup Popup Detail
28. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 6, 12, 13, 14, 15, 21, 27, 28.
- Search dipakai di toolbar halaman; isi kotak diganti pada TC berikutnya dan Search ditutup di akhir spec.
- Langkah penghubung sebelum TC-FA-TAG-803 membuka Popup Detail, menampilkan kolom Label, lalu menutup popup agar Search memenuhi precondition TC.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 14), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
