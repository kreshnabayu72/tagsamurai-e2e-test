---
id: TC-FA-TAG-E2E-225-custom-field-search-filter-sort-per-tipe-bagian-9
title: "Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 9)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-908
  - TC-FA-TAG-909
  - TC-FA-TAG-910
  - TC-FA-TAG-911
coverage:
  web: automated
---

# Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 9)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B (20 aset) memuat lima aset acuan: AST-0011 (Excavator 20 Ton - 11), AST-0020 (- 20), AST-0021 (- 21), AST-0043 (- 43), AST-0044 (- 44); urutan Last Updated terbaru ke terlama: AST-0044, AST-0043, AST-0021, AST-0020, AST-0011; 15 aset lain memakai Asset ID AST-0101 sampai AST-0115 (Brand Volvo, Model EC210, tanpa Label, Last Scanned kosong, Last Updated sebelum 30 Sep 26); Asset Name Excavator 20 Ton di Plant A memakai increment 201 sampai 220.
- Data TC-FA-TAG-908: CF DateTime: AST-0043 = 15 Okt 2026 10:00; AST-0011 = 01 Okt 2026 09:00.
- Data TC-FA-TAG-909: CF DateTime: AST-0043 = 15 Okt 2026 10:00; AST-0011 = 01 Okt 2026 09:00.
- Data TC-FA-TAG-910: CF DateTime: AST-0043 = 15 Okt 2026 10:00; AST-0011 = 01 Okt 2026 09:00; aset lain bernilai `—`.
- Data TC-FA-TAG-911: CF Formula: AST-0043 = 1946; AST-0011 = 176.
- Nilai Custom Field pada aset acuan AST-0043 dan AST-0011 di-seed idempotent lewat fixture BE di hook `before` dan dihapus di hook `after`; Custom Field yang diuji berstatus Active, 15 aset lain tanpa nilai.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent data Pre-setup di atas lewat fixture backend di hook `before` dan `after`; penghapusan preferensi kolom tabel T-TAG-02 di browser (cache browser tempat konfigurasi Setup Column disimpan) dipakai di hook `after` dan sebagai langkah penghubung bila tertulis.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dan kembalikan data Pre-setup yang diubah seeding spec ini ke keadaan awal. Spec ini tidak mengubah state global selain preferensi kolom di browser.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 2, 27).

## Test Steps

### TC-FA-TAG-908: Guard: Custom Field bertipe DateTime tidak dapat dicari

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Tampilkan kolom `CF DateTime` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
3. Catat teks sel kolom `CF DateTime` baris AST-0043 persis seperti tampil
4. Tutup Popup Detail
5. Ketik Search nilai kolom `CF DateTime` AST-0043 persis seperti tampil (teks yang dicatat pada langkah 3), tekan Enter
6. Verifikasi `No results found`: Custom Field bertipe DateTime tidak punya Search
7. Klik `(←)` pada kotak Search

### TC-FA-TAG-909: Filter Custom Field bertipe DateTime (date range picker)

8. Klik ikon Filter pada Table Tools halaman
9. Pilih rentang 12 Okt 2026 sampai 25 Okt 2026 pada field `CF DateTime`
10. Klik `[Apply]`
11. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
12. Ubah page size menjadi 25
13. Verifikasi Popup Detail hanya memuat AST-0043
14. Verifikasi Aset tanpa nilai tersaring keluar
15. Tutup Popup Detail
16. Bersihkan Filter: buka Filter Panel, hapus pilihan yang dipasang, klik `[Apply]`

### TC-FA-TAG-910: Sort tiga tahap Custom Field bertipe DateTime (tanggal (Oldest First lalu Newest First))

17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
18. Ubah page size menjadi 25
19. Klik header kolom CF DateTime sekali
20. Verifikasi setelah klik 1 (menaik): AST-0011 tampil sebelum AST-0043 (urutan tanggal (Oldest First lalu Newest First)), aset bernilai `—` di akhir
21. Klik header kolom CF DateTime sekali lagi
22. Verifikasi setelah klik 2 (menurun): aset bernilai `—` di awal, lalu AST-0043 sebelum AST-0011
23. Klik header kolom CF DateTime sekali lagi
24. Verifikasi setelah klik 3: sort netral dan urutan kembali ke bawaan Last Updated terbaru
25. Tutup Popup Detail

### TC-FA-TAG-911: Guard: Custom Field bertipe Formula tidak dapat dicari

26. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
27. Tampilkan kolom `CF Formula` lewat Setup Column (header `⋯`, `Setup Column...`, centang kolom, `[Save]`)
28. Catat teks sel kolom `CF Formula` baris AST-0043 persis seperti tampil
29. Tutup Popup Detail
30. Ketik Search nilai kolom `CF Formula` AST-0043 persis seperti tampil (teks yang dicatat pada langkah 28), tekan Enter
31. Verifikasi `No results found`: Custom Field bertipe Formula tidak punya Search
32. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): 1, 2, 3, 4, 7, 15, 16, 25, 26, 27, 28, 29, 32.
- Langkah 1 sampai 4 dan 26 sampai 29 (penghubung) menampilkan kolom `CF DateTime` dan `CF Formula` serta mencatat teks sel AST-0043 sebelum Search; langkah TC-FA-TAG-910 'Tampilkan kolom `CF DateTime`' tidak diulang karena kolom sudah ditampilkan pada langkah 2.
- Popup Detail Excavator 20 Ton / Plant B dibuka ulang pada tiap TC yang memakainya (langkah 1, 11, 17, dan 26 'Klik Asset Name') dan ditutup pada langkah 4, 15, 25, dan 29; tidak ada Popup Detail yang dibiarkan terbuka antar TC.
- Search ditutup lewat `(←)` (langkah 7 dan 32) dan Filter dibersihkan (langkah 16) sesudah TC yang memakainya (langkah penghubung); pada TC sort, kolom Custom Field yang sudah ditampilkan TC pencarian sebelumnya dalam spec yang sama tidak ditampilkan ulang karena langkah itu akan menyembunyikannya.
- Pembagian TC lintas spec: TC-FA-TAG-902 sampai 904 ada di spec `TC-FA-TAG-E2E-224-custom-field-search-filter-sort-per-tipe-bagian-8`; TC-FA-TAG-905 sampai 907 ada di spec `TC-FA-TAG-E2E-386-custom-field-bertipe-date-guard-search-filter-dan-sort-pada-tabel-t-tag-02`.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 2, 27).
- Temuan untuk QA:
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column dan hook `after` spec ini menghapus preferensi kolom di browser; nomor spec ini tercantum pada daftar pemulihan kolom di `suite.md`.
  - TC Search Custom Field menulis Search sebelum kolomnya ditampilkan lewat Setup Column, sedangkan TC Search kolom lain mensyaratkan kolom yang dicari tampil (Search terikat visibilitas kolom); spec mengikuti urutan TC sehingga hasilnya bergantung pada apakah Search memindai Custom Field yang kolomnya belum tampil.
  - Seeding nilai Custom Field pada aset acuan dapat mengubah Last Updated aset itu dan menggeser urutan bawaan Last Updated terbaru; pemulihan lewat fixture BE di hook `after` perlu mengembalikan Last Updated.
  - Post Condition TC ("Tidak ada perubahan data bisnis (aksi hanya membaca)" dan "Konfigurasi kolom tersimpan di cache browser ...") tidak punya langkah observasi di TC; tidak diasersi.
