---
id: TC-FA-TAG-E2E-212-t-tag-02-format-sel-link-badge-hover-dan-pemotongan-bagian-3
title: "Tabel T-TAG-02: Format Sel Category, Measurement, Label, dan Status (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-843
  - TC-FA-TAG-844
  - TC-FA-TAG-845
  - TC-FA-TAG-846
  - TC-FA-TAG-847
  - TC-FA-TAG-848
coverage:
  web: automated
---

# Tabel T-TAG-02: Format Sel Category, Measurement, Label, dan Status (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-844: Measurement Symbol pcs, Unit Name Pieces.
- Data TC-FA-TAG-845: AST-0044 berlabel Audit, Rental, Urgent.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-843: Kolom Category berupa badge Primary dengan hover hierarki lengkap

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Tampilkan kolom `Category` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
3. Arahkan pointer ke badge Category
4. Verifikasi Badge berseverity primary
5. Verifikasi Hover `Heavy Equipment > Earthmoving`

### TC-FA-TAG-844: Kolom Measurement menampilkan Symbol saja tanpa Unit Name

6. Tampilkan kolom `Measurement` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
7. Verifikasi sel menampilkan `pcs`
8. Verifikasi `Pieces` tidak ditampilkan

### TC-FA-TAG-845: Kolom Label menampilkan 1-2 badge berwarna label lalu +N more urut A-Z

9. Ubah page size menjadi 25
10. Tampilkan kolom `Label` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
11. Verifikasi Dua badge `Audit` dan `Rental` (warna hex label) tampil diikuti chip `+1 more`

### TC-FA-TAG-846: Klik +N more pada Label membuka popover Labels dengan seluruh label

12. Klik chip `+1 more` pada AST-0044
13. Verifikasi Popover `Labels` terbuka memuat `Audit`, `Rental`, `Urgent` sebagai badge penuh tanpa truncation
14. Tutup popover Labels

### TC-FA-TAG-847: Kolom Label kosong menampilkan strip

15. Verifikasi Sel menampilkan `—`

### TC-FA-TAG-848: Kolom Status menampilkan beberapa badge berurutan A-Z

16. Verifikasi AST-0020: badge `Assigned` lalu `Tag Reported`
17. Verifikasi AST-0043: badge `Available` lalu `Tag Reported`
18. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 14, 18.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Kolom Category, Measurement, dan Label tetap tampil sesudah ditampilkan TC sebelumnya dalam spec ini (konfigurasi kolom tersimpan).
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini belum tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
