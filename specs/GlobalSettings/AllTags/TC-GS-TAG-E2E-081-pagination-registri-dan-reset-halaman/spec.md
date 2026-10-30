---
id: TC-GS-TAG-E2E-081-pagination-registri-dan-reset-halaman
title: "Pagination Registri: Default, Pilihan Rows per Page, Reset ke Halaman 1 oleh Search/Filter, dan Sort Mempertahankan Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-245
  - TC-GS-TAG-246
coverage:
  web: automated
---

# Pagination Registri: Default, Pilihan Rows per Page, Reset ke Halaman 1 oleh Search/Filter, dan Sort Mempertahankan Halaman

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; hitungan (30 baris, 16 baris `Generic`, tiga halaman pada 10 baris per halaman) valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): Rows per page dikembalikan ke 10, Search, Filter, dan Sort dikosongkan.
- Kemampuan teknis: membaca teks pagination `Showing ... of N TAGs`, nilai `Rows per page`, nomor halaman aktif, dan mengetik pada input nomor halaman (selektor disediakan tim FE).

## Test Steps

### TC-GS-TAG-245: Pagination default dan pilihan rows per page

1. Verifikasi pagination default `Showing 1 - 10 of 30 TAGs`
2. Verifikasi `Rows per page: 10`
3. Pindah ke halaman 2
4. Buka pilihan Rows per page
5. Verifikasi opsi `10`, `25`, `50`, dan `100`
6. Verifikasi tidak ada opsi `All`
7. Tutup pilihan Rows per page
8. Buka pilihan Rows per page, lalu pilih `25`
9. Verifikasi tabel kembali ke halaman 1
10. Verifikasi pagination `Showing 1 - 25 of 30 TAGs`
11. Buka pilihan Rows per page, lalu pilih `100`
12. Buka pilihan Rows per page, lalu pilih `10`

### TC-GS-TAG-246: Search dan Apply Filter mereset halaman ke 1; input halaman tidak valid diabaikan

13. Pindah ke halaman 3
14. Ketik Search `Generic`, tekan Enter
15. Verifikasi tabel berada di halaman 1 (pagination `Showing 1 - 10 of 16 TAGs`)
16. Pindah ke halaman 2
17. Ketik `99` pada input nomor halaman, tekan Enter
18. Verifikasi nomor halaman 99 diabaikan dan tabel tetap di halaman 2
19. Klik header `Code` sekali
20. Verifikasi tabel tetap di halaman 2 (sort mempertahankan nomor halaman)
21. Buka Filter, pilih satu opsi `Status` (`Available`), klik `[Apply]`
22. Verifikasi tabel berada di halaman 1 (pagination `Showing 1 - 10 of 16 TAGs`)
23. Hapus chip filter `Status` lewat `✕` pada chip
24. Klik header `Code` dua kali lagi (kembali netral)
25. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (245, 246). Spec tidak mengubah data dan tidak menghapus apa pun.
- Panjang spec: 25 langkah, di bawah ambang sekitar 35 langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menutup pilihan Rows per page), langkah 12 (memulihkan Rows per page 10), langkah 23 (menghapus chip filter), langkah 24 dan 25 (mengembalikan sort ke netral dan mengosongkan Search).
- Langkah 11 (memilih `100`) adalah langkah 5 TC-GS-TAG-245 yang tidak punya Expected sendiri; spec tidak menambah asersi untuk langkah itu.
- Hitungan 30 baris, 16 baris `Generic` (DD-15 sampai DD-30 dan merek Generic), dan tiga halaman pada 10 baris per halaman diturunkan dari Seed Registri A; Expected TC-GS-TAG-246 hanya menyebut "halaman 1" dan "halaman 2".
- Opsi `Available` pada field `Status` (langkah 21) adalah pilihan spec karena TC-GS-TAG-246 menyebut "satu opsi" tanpa nilai; dengan Search `Generic` aktif, seluruh 16 baris (DD-15 sampai DD-30) berstatus `Available` sehingga hasil Filter masih dua halaman dan reset ke halaman 1 teramati.
- Pemisahan dari spec topik registri lain (Search, Filter, Sort, Pagination, Setup Column): ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Temuan untuk QA:
  - TC-GS-TAG-245 langkah 5 (memilih 100) tidak punya Expected.
  - TC-GS-TAG-246 butir b ("Nomor halaman 99 diabaikan") tidak menyebut apakah input dikosongkan atau dikembalikan ke nilai halaman aktif; spec hanya mengasersi tabel tetap di halaman 2.
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
