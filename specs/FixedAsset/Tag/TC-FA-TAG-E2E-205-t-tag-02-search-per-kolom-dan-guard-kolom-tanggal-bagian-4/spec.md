---
id: TC-FA-TAG-E2E-205-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-4
title: "Tabel T-TAG-02: Search Transactional Policy dan Guard Kolom Tanggal (Bagian 4)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-810
  - TC-FA-TAG-811
  - TC-FA-TAG-812
  - TC-FA-TAG-813
coverage:
  web: automated
---

# Tabel T-TAG-02: Search Transactional Policy dan Guard Kolom Tanggal (Bagian 4)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-810: Transactional Policy (nama transaksi pada ikon) seluruh aset grup = Transfer.
- Data TC-FA-TAG-811: kata kunci = teks tanggal dari sel kolom Last Scanned.
- Data TC-FA-TAG-812: kata kunci = teks tanggal dari sel kolom Warranty Expiry.
- Data TC-FA-TAG-813: kata kunci = teks tanggal dari sel kolom Last Updated.
- Kolom Transactional Policy, Last Scanned, dan Warranty Expiry ditampilkan lewat Setup Column sebelum Search; kolom Last Updated tampil secara bawaan. Nilai tanggal tampil sesuai format General Settings (precondition TC).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-810: Search kolom Transactional Policy (nama transaksi pada ikon) pada T-TAG-02 dengan nilai sama di seluruh baris

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Tampilkan kolom `Transactional Policy`, `Last Scanned`, dan `Warranty Expiry` lewat Setup Column (header `⋯`, `Setup Column...`, centang ketiga kolom, `[Save]`)
3. Catat teks tanggal persis seperti tampil pada sel kolom Last Scanned, Warranty Expiry, dan Last Updated salah satu baris
4. Tutup Popup Detail
5. Ketik Search `Transfer`, tekan Enter
6. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
7. Ubah page size menjadi 25
8. Verifikasi Popup Detail Excavator 20 Ton / Plant B memuat seluruh 20 aset karena semuanya cocok
9. Tutup Popup Detail

### TC-FA-TAG-811: Guard: Search tidak mencocokkan kolom tanggal Last Scanned

10. Ganti isi kotak search dengan teks tanggal persis seperti tampil pada sel kolom Last Scanned yang dicatat, tekan Enter
11. Verifikasi `No results found`: kolom tanggal dikecualikan dari cakupan Search

### TC-FA-TAG-812: Guard: Search tidak mencocokkan kolom tanggal Warranty Expiry

12. Ganti isi kotak search dengan teks tanggal persis seperti tampil pada sel kolom Warranty Expiry yang dicatat, tekan Enter
13. Verifikasi `No results found`: kolom tanggal dikecualikan dari cakupan Search

### TC-FA-TAG-813: Guard: Search tidak mencocokkan kolom tanggal Last Updated

14. Ganti isi kotak search dengan teks tanggal persis seperti tampil pada sel kolom Last Updated yang dicatat, tekan Enter
15. Verifikasi `No results found`: kolom tanggal dikecualikan dari cakupan Search
16. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 1, 2, 3, 4, 9, 16.
- Search dipakai di toolbar halaman; isi kotak diganti pada TC berikutnya dan Search ditutup di akhir spec.
- Langkah penghubung di awal menampilkan kolom dan mencatat teks tanggal dari sel agar kata kunci TC-FA-TAG-811 sampai 813 persis seperti tampil.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini belum tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC-FA-TAG-811 sampai 813 tidak menyebut baris mana yang dipakai untuk mengambil teks tanggal; spec mencatat teks dari salah satu baris Popup Detail Excavator 20 Ton / Plant B.
  - Empty state `No results found` pada TC-FA-TAG-811 sampai 813 diasersi pada tabel grup; TC tidak menyebut lokasi empty state itu.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
