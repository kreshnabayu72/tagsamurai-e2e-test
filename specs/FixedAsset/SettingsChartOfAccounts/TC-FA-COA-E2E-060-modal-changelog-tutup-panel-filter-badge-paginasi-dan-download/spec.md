---
id: TC-FA-COA-E2E-060-modal-changelog-tutup-panel-filter-badge-paginasi-dan-download
title: "Modal Changelog: Tutup Panel Filter, Badge, Paginasi, dan Download"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-216
  - TC-FA-COA-217
  - TC-FA-COA-219
  - TC-FA-COA-335
  - TC-FA-COA-336
coverage:
  web: automated
---

# Modal Changelog: Tutup Panel Filter, Badge, Paginasi, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Riwayat Changelog P41 (asumsi pre-setup, bukan data PRD): empat baris Example Data Modal Changelog (PRD §4.1.1; tanggal contoh 20 sampai 23 Oct 2026; kode 5-6001, 6-2001, 1-1002, 5-6000; Modified By Rina P) ditambah satu baris Create, satu baris Delete, satu baris Activate, dan satu entri oleh user B. Riwayat lebih dari 10 baris. Changelog adalah audit trail permanen yang tumbuh; jumlah baris tidak diasersi sebagai angka absolut.
- Kemampuan teknis: membaca isi berkas CSV yang terunduh (nama berkas, kolom, jumlah baris) dan membaca jumlah baris riwayat Changelog lewat BE; disediakan tim FE/BE.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-335: Paginasi modal Changelog

1. Klik ikon Changelog di toolbar
2. Verifikasi ukuran halaman default 10
3. Buka pilihan ukuran halaman
4. Verifikasi pilihan ukuran halaman 10, 25, 50, dan 100
5. Pilih ukuran halaman 25
6. Verifikasi modal kembali ke halaman 1 dengan maksimal 25 baris
7. Pindah ke halaman 2
8. Verifikasi halaman 2 memuat lanjutan riwayat tanpa mengubah data
9. Pilih kembali ukuran halaman 10

### TC-FA-COA-336: Download Changelog

10. Klik ikon Download di modal, lalu pilih `Download as CSV`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas bernama `Changelog-Chart-of-Accounts` terunduh
13. Verifikasi berkas memuat kolom Changelog yang sedang visible
14. Verifikasi baris berkas sesuai Search dan Filter modal (tanpa Search dan Filter: seluruh baris riwayat)

### TC-FA-COA-216: Tutup panel dengan klik di luar panel

15. Klik ikon Filter di modal Changelog
16. Pilih Action = Edit, lalu klik Apply
17. Pilih Modified By user B tanpa klik Apply
18. Klik di area luar Filter Panel (di dalam modal Changelog)
19. Klik ikon Filter untuk membuka kembali Filter Panel
20. Verifikasi panel menampilkan Action = Edit (ter-Apply terakhir)
21. Verifikasi field Modified By kosong
22. Verifikasi tabel Changelog tetap menampilkan hasil filter Action = Edit (baris Edit tampil)

### TC-FA-COA-217: Tutup panel dengan klik ulang ikon Filter

23. Pilih Modified By user B tanpa klik Apply
24. Klik ikon Filter untuk menutup panel
25. Klik ikon Filter untuk membuka kembali Filter Panel
26. Verifikasi panel menampilkan Action = Edit (ter-Apply terakhir)
27. Verifikasi field Modified By kosong
28. Verifikasi tabel Changelog tetap menampilkan hasil filter Action = Edit (baris Edit tampil)

### TC-FA-COA-219: Badge titik indikator filter aktif

29. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter dengan panel terbuka
30. Klik ikon Filter untuk menutup panel
31. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter dengan panel tertutup
32. Klik ikon Filter untuk membuka panel
33. Klik Clear Field pada Action, lalu klik Apply
34. Verifikasi badge titik pada ikon Filter hilang
35. Klik ikon Filter untuk menutup panel
36. Tutup modal dengan ikon ✕

## Notes

- Urutan TC-335 dan TC-336 (tanpa Filter) dijalankan lebih dulu, lalu TC-216, TC-217, dan TC-219 yang memakai Filter Action = Edit yang sama secara berurutan.
- TC-217 langkah 1 sampai 2 (Filter Action = Edit ter-Apply) dipenuhi oleh keadaan akhir TC-216 pada langkah 16; TC-219 langkah 1 sampai 2 dipenuhi oleh keadaan akhir TC-217 (Action = Edit ter-Apply, panel terbuka pada langkah 25).
- Asersi absence toast pada langkah 11 diletakkan segera setelah pemicu sebelum asersi berkas; berkas terunduh (langkah 12) menjadi bukti positif bahwa respons sudah diproses (8b.11).
- P-10: TC-336 mengasersi UI (toast) dan isi berkas (nama berkas, kolom, baris) pada alur unduh yang sama; klausa isi berkas diletakkan setelah klausa UI dan `Verifikasi` isi berkas satu per klausa.
- Spec ini sedikit melewati 35 langkah karena satu kelas dan satu dataset read-only (riwayat Modal Changelog): TC-216, TC-217, dan TC-219 sengaja berurutan karena memakai keadaan Filter Action = Edit yang sama, sedangkan TC-335 dan TC-336 berdiri sendiri tanpa Filter.
- Langkah penghubung (S-03): langkah 9 (memulihkan ukuran halaman), langkah 35 dan 36 (menutup panel dan modal).
- Temuan untuk QA:
  - TC-335 langkah 4 meminta pindah ke halaman 2 setelah memilih ukuran 25, tetapi riwayat "lebih dari 10 baris" (P41) belum tentu lebih dari 25 baris; halaman 2 pada ukuran 25 hanya ada bila audit trail melebihi 25 baris.
  - TC-336 butir b ("baris sesuai Search dan Filter modal") tidak menyebut Search atau Filter yang aktif; spec mengasersi seluruh baris riwayat tanpa Search dan Filter.
  - TC-216 dan TC-217 tidak menyebut apakah panel tetap terbuka setelah Apply; spec mengikuti urutan langkah TC.
  - P41 adalah asumsi pre-setup, bukan data PRD.
