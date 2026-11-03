---
id: TC-FA-TAG-E2E-199-t-tag-02-sort-tiga-tahap-per-kolom-bagian-3
title: "Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-787
  - TC-FA-TAG-788
  - TC-FA-TAG-789
coverage:
  web: automated
---

# Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-787: Last Scanned: AST-0011 = 20 Oct 26; AST-0020 = —; AST-0021 = 25 Oct 26; AST-0043 = 10 Oct 26; AST-0044 = —.
- Data TC-FA-TAG-788: Asset Value (Commercial): AST-0011 = 500; AST-0020 = —; AST-0021 = 300; AST-0043 = 800; AST-0044 = 100.
- Data TC-FA-TAG-789: Asset Value (Fiscal): AST-0011 = 450; AST-0020 = —; AST-0021 = 250; AST-0043 = 700; AST-0044 = 90.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-787: Sort tiga tahap kolom Last Scanned pada T-TAG-02

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Tampilkan kolom `Last Scanned` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
4. Klik header kolom Last Scanned sekali
5. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0043, AST-0011, AST-0021, AST-0044, AST-0020; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
6. Klik header kolom Last Scanned sekali lagi
7. Verifikasi setelah klik 2 (menurun): AST-0044, AST-0020, AST-0021, AST-0011, AST-0043
8. Klik header kolom Last Scanned sekali lagi
9. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-788: Sort tiga tahap kolom Asset Value (Commercial) pada T-TAG-02

10. Tampilkan kolom `Asset Value (Commercial)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
11. Klik header kolom Asset Value (Commercial) sekali
12. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0044, AST-0021, AST-0011, AST-0043, AST-0020; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
13. Klik header kolom Asset Value (Commercial) sekali lagi
14. Verifikasi setelah klik 2 (menurun): AST-0020, AST-0043, AST-0011, AST-0021, AST-0044
15. Klik header kolom Asset Value (Commercial) sekali lagi
16. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-789: Sort tiga tahap kolom Asset Value (Fiscal) pada T-TAG-02

17. Tampilkan kolom `Asset Value (Fiscal)` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
18. Klik header kolom Asset Value (Fiscal) sekali
19. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0044, AST-0021, AST-0011, AST-0043, AST-0020; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
20. Klik header kolom Asset Value (Fiscal) sekali lagi
21. Verifikasi setelah klik 2 (menurun): AST-0020, AST-0043, AST-0011, AST-0021, AST-0044
22. Klik header kolom Asset Value (Fiscal) sekali lagi
23. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru
24. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 24.
- Popup Detail dibuka sekali dan page size 25 diatur sekali pada TC pertama; klik ketiga tiap TC mengembalikan sort ke netral.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini belum tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
