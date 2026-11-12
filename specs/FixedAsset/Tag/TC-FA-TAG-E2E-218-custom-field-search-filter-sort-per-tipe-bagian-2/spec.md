---
id: TC-FA-TAG-E2E-218-custom-field-search-filter-sort-per-tipe-bagian-2
title: "Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-877
  - TC-FA-TAG-878
  - TC-FA-TAG-879
  - TC-FA-TAG-880
coverage:
  web: automated
---

# Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-877: CF Text Area: AST-0043 = Needs hydraulic seal check; AST-0011 = Check later; aset lain bernilai `—`.
- Data TC-FA-TAG-878: CF Phone: AST-0043 = +62 21 5550 0143; AST-0011 = +62 21 5550 0011; kata kunci `+62 21 5550 0143`.
- Data TC-FA-TAG-879: CF Phone: AST-0043 = +62 21 5550 0143; AST-0011 = +62 21 5550 0011.
- Data TC-FA-TAG-880: CF Phone: AST-0043 = +62 21 5550 0143; AST-0011 = +62 21 5550 0011; aset lain bernilai `—`.
- Nilai Custom Field pada aset acuan AST-0043 dan AST-0011 di-seed idempotent lewat fixture BE di hook `before` dan dihapus di hook `after`; Custom Field yang diuji berstatus Active, 15 aset lain tanpa nilai.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 2, 13).

## Test Steps

### TC-FA-TAG-877: Sort tiga tahap Custom Field bertipe Text Area (A-Z)

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Tampilkan kolom `CF Text Area` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
3. Ubah page size menjadi 25
4. Klik header kolom CF Text Area sekali
5. Verifikasi setelah klik 1 (menaik): AST-0011 tampil sebelum AST-0043 (urutan A-Z), aset bernilai `—` di akhir
6. Klik header kolom CF Text Area sekali lagi
7. Verifikasi setelah klik 2 (menurun): aset bernilai `—` di awal, lalu AST-0043 sebelum AST-0011
8. Klik header kolom CF Text Area sekali lagi
9. Verifikasi setelah klik 3: sort netral dan urutan kembali ke bawaan Last Updated terbaru
10. Tutup Popup Detail

### TC-FA-TAG-878: Search kolom Custom Field bertipe Phone

11. Ketik Search `+62 21 5550 0143`, tekan Enter
12. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
13. Tampilkan kolom `CF Phone` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
14. Ubah page size menjadi 25
15. Verifikasi Popup Detail hanya memuat AST-0043 (nilai kolom CF Phone mengandung `+62 21 5550 0143`)
16. Tutup Popup Detail
17. Klik `(←)` pada kotak Search

### TC-FA-TAG-879: Guard: Custom Field bertipe Phone tidak punya Filter

18. Klik ikon Filter pada Table Tools halaman
19. Verifikasi Filter Panel memuat field `Brand`
20. Verifikasi Field `CF Phone` tidak ada pada Filter Panel
21. Tutup Filter Panel

### TC-FA-TAG-880: Sort tiga tahap Custom Field bertipe Phone (A-Z)

22. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
23. Ubah page size menjadi 25
24. Klik header kolom CF Phone sekali
25. Verifikasi setelah klik 1 (menaik): AST-0011 tampil sebelum AST-0043 (urutan A-Z), aset bernilai `—` di akhir
26. Klik header kolom CF Phone sekali lagi
27. Verifikasi setelah klik 2 (menurun): aset bernilai `—` di awal, lalu AST-0043 sebelum AST-0011
28. Klik header kolom CF Phone sekali lagi
29. Verifikasi setelah klik 3: sort netral dan urutan kembali ke bawaan Last Updated terbaru
30. Tutup Popup Detail

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 10, 16, 17, 21, 30.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Search ditutup lewat `(←)` dan Filter dibersihkan sesudah tiap TC (langkah penghubung); pada TC sort, kolom Custom Field yang sudah ditampilkan TC pencarian sebelumnya dalam spec yang sama tidak ditampilkan ulang karena langkah itu akan menyembunyikannya.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 2, 13).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC Search Custom Field menulis Search sebelum kolomnya ditampilkan lewat Setup Column, sedangkan TC Search kolom lain mensyaratkan kolom yang dicari tampil (Search terikat visibilitas kolom); spec mengikuti urutan TC sehingga hasilnya bergantung pada apakah Search memindai Custom Field yang kolomnya belum tampil.
  - Seeding nilai Custom Field pada aset acuan dapat mengubah Last Updated aset itu dan menggeser urutan bawaan Last Updated terbaru; pemulihan lewat fixture BE di hook `after` perlu mengembalikan Last Updated.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
