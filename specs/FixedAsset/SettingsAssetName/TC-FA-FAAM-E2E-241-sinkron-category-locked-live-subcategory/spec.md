---
id: TC-FA-FAAM-E2E-241-sinkron-category-locked-live-subcategory
title: "Sinkron Lintas Modul: Subcategory Menambah dan Menghapus Kunci Category Locked Asset Name Secara Live"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-597
coverage:
  web: automated
---

# Sinkron Lintas Modul: Subcategory Menambah dan Menghapus Kunci Category Locked Asset Name Secara Live

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control pada client `AutoLockedLive` (Tabel Data Uji Pre-setup No. 12b); email dan kredensial disediakan tim FE (Email akun ini tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_LOCKLIVE_TC_PASSWORD` (nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_LOCKLIVE_TC_PASSWORD`.
- Data Pre-setup (Pre-setup No. 12b, client `AutoLockedLive`, nama literal karena client dan Category dipakai satu TC ini saja): Asset Name `Locked Live Item` (Total Asset 0) ber-Category leaf `Live Lock Leaf`. Spec tidak men-seed data lain; hook `before` memastikan `Live Lock Leaf` tanpa subcategory (idempotent) dan hook `after` menghapus subcategory yang dibuat spec ini bila masih ada.
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; membaca jumlah baris hasil Search Changelog sebelum aksi (baseline).
- State global yang diubah: struktur Category `Live Lock Leaf` pada client `AutoLockedLive` (dipulihkan di langkah 13 dan di hook `after`). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-597: login sebagai Total Control pada client `AutoLockedLive` dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

1. Ketik Search `Locked Live Item`, tekan Enter
2. Klik icon Changelog
3. Ketik Search `Locked Live Item`, tekan Enter
4. Catat jumlah baris Changelog `Locked Live Item` sebagai baseline L
5. Tutup Modal Changelog
6. Di Settings > Categories tambahkan subcategory pada `Live Lock Leaf`
7. Buka tab Asset Name
8. Ketik Search `Locked Live Item`, tekan Enter
9. Verifikasi baris `Locked Live Item` menampilkan badge `Needs Update`
10. Klik icon Changelog
11. Ketik Search `Locked Live Item`, tekan Enter
12. Verifikasi jumlah baris Changelog `Locked Live Item` sama dengan baseline L pada langkah 4 (tanpa baris log)
13. Tutup Modal Changelog
14. Hapus subcategory tadi di Settings > Categories
15. Buka tab Asset Name
16. Ketik Search `Locked Live Item`, tekan Enter
17. Verifikasi baris `Locked Live Item` tampil tanpa badge `Needs Update`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 8, 16 (Search untuk menemukan baris target), langkah 2, 3, 5, 10, 11, 13 (membuka, mencari, dan menutup Modal Changelog), langkah 4 (mencatat baseline), dan langkah 7 serta 15 (pindah tab).
- Langkah 12 menggantikan asersi absence "tanpa baris log" dengan asersi jumlah terhadap baseline; asersi absence murni hanya di spec kelas g (S-05). Anchor positif absence badge pada langkah 17: baris `Locked Live Item` tampil.
- Spec ini memakai client `AutoLockedLive` yang terpisah dari client utama; tidak ada ganti akun di tengah spec.
- Temuan untuk QA: Pre-setup No. 12b tidak memuat email akun Total Control untuk client `AutoLockedLive`; TC-FA-FAAM-597 butir a ("tanpa baris log") tidak menyebut surface log yang diperiksa, spec memakai Modal Changelog.
