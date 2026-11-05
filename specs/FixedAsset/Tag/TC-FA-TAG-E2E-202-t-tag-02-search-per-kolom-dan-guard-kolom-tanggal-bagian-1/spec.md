---
id: TC-FA-TAG-E2E-202-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-1
title: "Tabel T-TAG-02: Search per Kolom (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-797
  - TC-FA-TAG-798
  - TC-FA-TAG-799
  - TC-FA-TAG-800
coverage:
  web: automated
---

# Tabel T-TAG-02: Search per Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-797: kata kunci `Ton - 4`.
- Data TC-FA-TAG-798: kata kunci `AST-0043`.
- Data TC-FA-TAG-799: kata kunci `QR-00231`; TAG Code: AST-0011 = RF-00101; AST-0020 = RF-00130; AST-0021 = RF-00140; AST-0043 = QR-00231; AST-0044 = QR-00232 (Tag pertama).
- Data TC-FA-TAG-800: kata kunci `RF-00132`; TAG Code: AST-0044 memiliki Tag kedua `RF-00132` (selain `QR-00232`); empat aset acuan lain tidak memiliki `RF-00132`.
- Kolom yang dicari (Name, Asset ID, TAG Code) tampil secara bawaan di tabel T-TAG-02, sehingga memenuhi precondition TC bahwa Search terikat visibilitas kolom.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-797: Search kolom Name pada T-TAG-02

1. Ketik Search `Ton - 4`, tekan Enter
2. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
3. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
4. Ubah page size menjadi 25
5. Verifikasi Popup Detail hanya memuat: AST-0043 dan AST-0044 (teks lengkap `[Asset Name] - [Increment]`)
6. Tutup Popup Detail

### TC-FA-TAG-798: Search kolom Asset ID pada T-TAG-02

7. Ganti isi kotak search dengan `AST-0043`, tekan Enter
8. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
9. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
10. Ubah page size menjadi 25
11. Verifikasi Popup Detail hanya memuat: AST-0043
12. Tutup Popup Detail

### TC-FA-TAG-799: Search kolom TAG Code (Tag pertama) pada T-TAG-02

13. Ganti isi kotak search dengan `QR-00231`, tekan Enter
14. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
15. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
16. Ubah page size menjadi 25
17. Verifikasi Popup Detail hanya memuat: AST-0043
18. Tutup Popup Detail

### TC-FA-TAG-800: Search kolom TAG Code (Tag lain pada aset multi-Tag) pada T-TAG-02

19. Ganti isi kotak search dengan `RF-00132`, tekan Enter
20. Verifikasi Tabel grup hanya memuat Excavator 20 Ton / Plant B (atau grup lain yang memuat baris cocok)
21. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
22. Ubah page size menjadi 25
23. Verifikasi Popup Detail hanya memuat: AST-0044 (TAG Code mana pun pada aset dicocokkan)
24. Tutup Popup Detail
25. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 6, 12, 18, 24, 25.
- Search dipakai di toolbar halaman; hasil Search sebelumnya diganti isi kotaknya pada TC berikutnya dan Search ditutup di akhir spec (langkah penghubung).
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Asersi "hanya memuat" pada Popup Detail memakai baris acuan hasil Search itu sendiri sebagai pembanding (baris yang disebut Expected dijamin tampil oleh Search).
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
