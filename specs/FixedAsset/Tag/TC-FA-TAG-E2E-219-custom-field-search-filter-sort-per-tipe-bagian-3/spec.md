---
id: TC-FA-TAG-E2E-219-custom-field-search-filter-sort-per-tipe-bagian-3
title: "Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 3)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-881
  - TC-FA-TAG-882
  - TC-FA-TAG-883
  - TC-FA-TAG-884
  - TC-FA-TAG-885
coverage:
  web: automated
---

# Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-881: CF Email: AST-0043 = vendor43@qwertysystem.net; AST-0011 = vendor11@qwertysystem.net; kata kunci `vendor43@qwertysystem.net`.
- Data TC-FA-TAG-882: CF Email: AST-0043 = vendor43@qwertysystem.net; AST-0011 = vendor11@qwertysystem.net.
- Data TC-FA-TAG-883: CF Email: AST-0043 = vendor43@qwertysystem.net; AST-0011 = vendor11@qwertysystem.net; aset lain bernilai `—`.
- Data TC-FA-TAG-884: CF URL: AST-0043 = https://vendor.example.com/ast43; AST-0011 = https://vendor.example.com/ast11; kata kunci `https://vendor.example.com/ast43`.
- Data TC-FA-TAG-885: CF URL: AST-0043 = https://vendor.example.com/ast43; AST-0011 = https://vendor.example.com/ast11.
- Nilai Custom Field pada aset acuan AST-0043 dan AST-0011 di-seed idempotent lewat fixture BE di hook `before` dan dihapus di hook `after`; Custom Field yang diuji berstatus Active, 15 aset lain tanpa nilai.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-881: Search kolom Custom Field bertipe Email

1. Ketik Search `vendor43@qwertysystem.net`, tekan Enter
2. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
3. Tampilkan kolom `CF Email` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
4. Ubah page size menjadi 25
5. Verifikasi Popup Detail hanya memuat AST-0043 (nilai kolom CF Email mengandung `vendor43@qwertysystem.net`)
6. Tutup Popup Detail
7. Klik `(←)` pada kotak Search

### TC-FA-TAG-882: Guard: Custom Field bertipe Email tidak punya Filter

8. Klik ikon Filter pada Table Tools halaman
9. Verifikasi Filter Panel memuat field `Brand`
10. Verifikasi Field `CF Email` tidak ada pada Filter Panel
11. Tutup Filter Panel

### TC-FA-TAG-883: Sort tiga tahap Custom Field bertipe Email (A-Z)

12. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
13. Ubah page size menjadi 25
14. Klik header kolom CF Email sekali
15. Verifikasi setelah klik 1 (menaik): AST-0011 tampil sebelum AST-0043 (urutan A-Z), aset bernilai `—` di akhir
16. Klik header kolom CF Email sekali lagi
17. Verifikasi setelah klik 2 (menurun): aset bernilai `—` di awal, lalu AST-0043 sebelum AST-0011
18. Klik header kolom CF Email sekali lagi
19. Verifikasi setelah klik 3: sort netral dan urutan kembali ke bawaan Last Updated terbaru
20. Tutup Popup Detail

### TC-FA-TAG-884: Search kolom Custom Field bertipe URL

21. Ketik Search `https://vendor.example.com/ast43`, tekan Enter
22. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
23. Tampilkan kolom `CF URL` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
24. Ubah page size menjadi 25
25. Verifikasi Popup Detail hanya memuat AST-0043 (nilai kolom CF URL mengandung `https://vendor.example.com/ast43`)
26. Tutup Popup Detail
27. Klik `(←)` pada kotak Search

### TC-FA-TAG-885: Guard: Custom Field bertipe URL tidak punya Filter

28. Klik ikon Filter pada Table Tools halaman
29. Verifikasi Filter Panel memuat field `Brand`
30. Verifikasi Field `CF URL` tidak ada pada Filter Panel
31. Tutup Filter Panel

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 6, 7, 11, 20, 26, 27, 31.
- Popup Detail Excavator 20 Ton / Plant B dibuka pada TC pertama dan tetap terbuka bila TC berikutnya memakai popup yang sama (langkah "Klik Asset Name" TC berikutnya tidak diulang; halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Search ditutup lewat `(←)` dan Filter dibersihkan sesudah tiap TC (langkah penghubung); pada TC sort, kolom Custom Field yang sudah ditampilkan TC pencarian sebelumnya dalam spec yang sama tidak ditampilkan ulang karena langkah itu akan menyembunyikannya.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini belum tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC Search Custom Field menulis Search sebelum kolomnya ditampilkan lewat Setup Column, sedangkan TC Search kolom lain mensyaratkan kolom yang dicari tampil (Search terikat visibilitas kolom); spec mengikuti urutan TC sehingga hasilnya bergantung pada apakah Search memindai Custom Field yang kolomnya belum tampil.
  - Seeding nilai Custom Field pada aset acuan dapat mengubah Last Updated aset itu dan menggeser urutan bawaan Last Updated terbaru; pemulihan lewat fixture BE di hook `after` perlu mengembalikan Last Updated.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
