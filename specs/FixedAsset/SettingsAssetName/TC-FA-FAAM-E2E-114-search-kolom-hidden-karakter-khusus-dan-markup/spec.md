---
id: TC-FA-FAAM-E2E-114-search-kolom-hidden-karakter-khusus-dan-markup
title: "Search: Kolom Hidden, Keyword Khusus Literal, dan Nilai Sel Markup sebagai Teks"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-351
  - TC-FA-FAAM-358
  - TC-FA-FAAM-359
coverage:
  web: automated
---

# Search: Kolom Hidden, Keyword Khusus Literal, dan Nilai Sel Markup sebagai Teks

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10) dan Asset Name `<img src=x>` (Pre-setup #15d, hanya dibaca).
- Kemampuan teknis: hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (Code di-hide lalu dimunculkan kembali lewat Column Visibility, tersimpan di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-358: Keyword khusus dicocokkan sebagai teks literal
1. Ketik Search `<b>x</b>`, tekan Enter
2. Verifikasi tabel menampilkan `No results found`
3. Verifikasi input Search berisi teks literal `<b>x</b>` tanpa markup terinterpretasi
4. Ganti isi kotak search dengan `%`, tekan Enter
5. Verifikasi tidak ada kecocokan: tabel menampilkan `No results found`
### TC-FA-FAAM-359: Nilai sel berisi markup dirender sebagai teks
6. Ganti isi kotak search dengan `img`, tekan Enter
7. Verifikasi baris tampil dengan teks `<img src=x>` apa adanya
8. Verifikasi sel Asset Name baris `<img src=x>` tidak memuat gambar
### TC-FA-FAAM-351: Kolom yang di-hide tidak dicari dan kembali dicari saat di-unhide
9. Klik `(←)` pada kotak Search
10. Verifikasi baris `Dell Latitude` tampil di tabel
11. Klik header kolom Actions (⋯) untuk membuka Column Visibility
12. Uncheck kolom `Code`
13. Tutup Column Visibility
14. Ketik Search `dlat`, tekan Enter
15. Verifikasi keyword `dlat` tidak menemukan baris: tabel menampilkan `No results found`
16. Ganti isi kotak search dengan `LATITUDE`, tekan Enter
17. Verifikasi kolom lain yang tampil tetap dapat dicari: baris `Dell Latitude` tampil
18. Klik header kolom Actions (⋯) untuk membuka Column Visibility
19. Check kolom `Code`
20. Tutup Column Visibility
21. Ganti isi kotak search dengan `dlat`, tekan Enter
22. Verifikasi keyword `dlat` menemukan baris `Dell Latitude`
23. Klik `(←)` pada kotak Search
24. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, lalu tekan F5

## Notes

- Urutan di spec: TC-FA-FAAM-358 dan TC-FA-FAAM-359 (Search murni) lebih dulu, TC-FA-FAAM-351 terakhir karena mengubah konfigurasi kolom (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): klik `(←)` pada kotak Search, membuka dan menutup Column Visibility, klik `(←)` terakhir, dan pemulihan konfigurasi kolom.
- Keyword `LATITUDE` pada TC-FA-FAAM-351 dipilih spec untuk mengamati Expected b ("kolom lain tetap dapat dicari"); TC tidak menyebut keyword untuk klausa itu.
- Temuan untuk QA: TC-FA-FAAM-351 tidak menyebut hasil keyword `dlat` saat Code di-hide selain "tidak menemukan baris"; spec memakai empty state `No results found` sebagai anchor absence (bagian 8b butir 2).
