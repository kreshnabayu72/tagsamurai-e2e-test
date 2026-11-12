---
id: TC-FA-TAG-E2E-198-t-tag-02-sort-tiga-tahap-per-kolom-bagian-2
title: "Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-784
  - TC-FA-TAG-785
  - TC-FA-TAG-786
coverage:
  web: automated
---

# Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-784: Model/Type: AST-0011 = 320D; AST-0020 = PC200; AST-0021 = 330F; AST-0043 = ZX210; AST-0044 = PC300.
- Data TC-FA-TAG-785: Label: AST-0011 [1 label, pertama Rental]; AST-0020 [1 label, pertama Urgent]; AST-0021 [2 label, pertama Rental]; AST-0043 [1 label, pertama Audit]; AST-0044 [3 label, pertama Audit].
- Data TC-FA-TAG-786: Status: AST-0011 = Available; AST-0020 = Assigned; AST-0021 = In Transfer Process; AST-0043 = Available; AST-0044 = Available.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 9), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-784: Sort tiga tahap kolom Model/Type pada T-TAG-02

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Ubah page size menjadi 25
3. Klik header kolom Model/Type sekali
4. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0011, AST-0021, AST-0020, AST-0044, AST-0043; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
5. Klik header kolom Model/Type sekali lagi
6. Verifikasi setelah klik 2 (menurun): AST-0043, AST-0044, AST-0020, AST-0021, AST-0011
7. Klik header kolom Model/Type sekali lagi
8. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-785: Sort tiga tahap kolom Label pada T-TAG-02

9. Tampilkan kolom `Label` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
10. Klik header kolom Label sekali
11. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0043, AST-0011, AST-0020, AST-0021, AST-0044; ascending = jumlah label terkecil, tiebreaker label pertama A-Z
12. Klik header kolom Label sekali lagi
13. Verifikasi setelah klik 2 (menurun): AST-0044, AST-0021, AST-0020, AST-0011, AST-0043
14. Klik header kolom Label sekali lagi
15. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru

### TC-FA-TAG-786: Sort tiga tahap kolom Status pada T-TAG-02

16. Klik header kolom Status sekali
17. Verifikasi setelah klik 1 (menaik): urutan relatif lima aset acuan: AST-0020, AST-0044, AST-0043, AST-0011, AST-0021; nilai sama diurutkan menurut default sort (Last Updated terbaru di atas); nilai kosong `—` di akhir saat menaik dan di awal saat menurun
18. Klik header kolom Status sekali lagi
19. Verifikasi setelah klik 2 (menurun): AST-0021, AST-0044, AST-0043, AST-0011, AST-0020
20. Klik header kolom Status sekali lagi
21. Verifikasi setelah klik 3: indikator sort netral dan urutan kembali ke bawaan Last Updated terbaru
22. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 22.
- Popup Detail dibuka sekali dan page size 25 diatur sekali pada TC pertama; klik ketiga tiap TC mengembalikan sort ke netral.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 9), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column (TC-FA-TAG-785) dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
