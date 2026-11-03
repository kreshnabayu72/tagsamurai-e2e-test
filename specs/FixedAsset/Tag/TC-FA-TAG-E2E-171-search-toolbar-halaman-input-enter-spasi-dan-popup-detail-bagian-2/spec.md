---
id: TC-FA-TAG-E2E-171-search-toolbar-halaman-input-enter-spasi-dan-popup-detail-bagian-2
title: "Search Toolbar Halaman: Karakter Khusus, Reset, Halaman 1, dan Popup Detail (Bagian 2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-686
  - TC-FA-TAG-687
  - TC-FA-TAG-688
  - TC-FA-TAG-689
  - TC-FA-TAG-690
  - TC-FA-TAG-691
coverage:
  web: automated
---

# Search Toolbar Halaman: Karakter Khusus, Reset, Halaman 1, dan Popup Detail (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Grup tambahan milik spec untuk TC-FA-TAG-689 (delapan grup di luar dataset sehingga tabel grup lebih dari 10 baris), dibuat dan dihapus lewat fixture backend. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Grup tambahan TC-FA-TAG-689 | Delapan grup tambahan milik spec, nama tidak memuat `Excavator`, `Forklift`, atau `Laptop`, bersuffix `{runId}-171-<n>`; dibuat sebelum TC-FA-TAG-689 dan dihapus sebelum TC-FA-TAG-690 | `grupTambahan171` |
| Aset acuan grup 'Excavator 20 Ton' / Plant B | 20 aset, memuat AST-0011, AST-0020, AST-0021, AST-0043, AST-0044 | `asetAcuanPlantB` |

- State yang diubah dan pemulihannya: grup tambahan dibuat sebelum TC-FA-TAG-689 dan dihapus sesudahnya; hook `after` menghapusnya bila masih ada.

## Test Steps

### TC-FA-TAG-686

1. Ketik Search `<script>alert(1)</script>`, tekan Enter
2. Verifikasi `No results found` tampil
3. Verifikasi tidak ada eksekusi script atau galat
4. Ganti isi kotak Search dengan `%`, tekan Enter
5. Verifikasi `%` diperlakukan sebagai teks biasa
6. Verifikasi `%` tidak mencocokkan semua baris (keempat baris grup tidak tampil bersamaan)

### TC-FA-TAG-687

7. Ganti isi kotak Search dengan `Forklift`, tekan Enter
8. Kosongkan isi kotak Search, tekan Enter
9. Verifikasi empat baris grup tampil

### TC-FA-TAG-688

10. Ganti isi kotak Search dengan `Forklift`, tekan Enter
11. Klik ikon close pada input Search
12. Verifikasi input Search tertutup
13. Verifikasi empat baris grup tampil

### TC-FA-TAG-689

14. Buat delapan grup tambahan lewat fixture backend hingga tersimpan, lalu muat ulang halaman
15. Verifikasi paginasi tabel grup memuat lebih dari satu halaman
16. Pindah ke halaman 2 tabel grup
17. Verifikasi tabel grup menampilkan halaman 2
18. Ketik Search `Excavator`, tekan Enter
19. Verifikasi tabel grup menampilkan halaman 1 dari hasil pencarian

### TC-FA-TAG-690

20. Hapus delapan grup tambahan lewat fixture backend hingga tersimpan, lalu muat ulang halaman
21. Ketik Search `AST-0043`, tekan Enter
22. Verifikasi tabel grup hanya memuat baris Excavator 20 Ton / Plant B
23. Klik Asset Name 'Excavator 20 Ton' pada baris Plant B
24. Verifikasi Popup Detail hanya memuat baris AST-0043
25. Verifikasi Popup Detail tidak memiliki toolbar Search atau Filter sendiri

### TC-FA-TAG-691

26. Tutup Popup Detail, lalu klik `(←)` pada kotak Search
27. Klik Asset Name 'Excavator 20 Ton' pada baris Plant B
28. Verifikasi tidak ada ikon Search maupun Filter di dalam Popup Detail
29. Verifikasi ikon Search dan Filter tampil pada toolbar halaman (penyaringan hanya lewat toolbar halaman)
30. Tutup Popup Detail

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-686, TC-FA-TAG-687, TC-FA-TAG-688, TC-FA-TAG-689, TC-FA-TAG-690, TC-FA-TAG-691). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Search toolbar halaman ada di spec 170 (TC-FA-TAG-680 s.d. 685) dan spec 171 (TC-FA-TAG-686 s.d. 691).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 14, 20, 26, 30 (seeding dan penghapusan grup tambahan, menutup Popup Detail, dan mereset input Search).
- Temuan untuk QA:
  - TC-FA-TAG-689 mensyaratkan lebih dari 10 baris grup, sedangkan TC-FA-TAG-686 s.d. 688 dan TC-FA-TAG-690 menegaskan empat baris grup; spec menambah grup hanya untuk TC-FA-TAG-689 dan menghapusnya sebelum TC-FA-TAG-690. Jumlah grup tambahan (delapan) dan cara pembuatannya tidak disebut TC.
  - TC-FA-TAG-689 tidak menyebut kata kunci yang menghasilkan lebih dari satu halaman; spec memakai `Excavator` sesuai langkah TC sehingga halaman 1 hasil pencarian berisi dua baris.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
