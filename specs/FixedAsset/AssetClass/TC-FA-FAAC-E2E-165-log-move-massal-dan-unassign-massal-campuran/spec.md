---
id: TC-FA-FAAC-E2E-165-log-move-massal-dan-unassign-massal-campuran
title: "Log Move Massal dan Unassign Massal Campuran pada Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-549
  - TC-FA-FAAC-550
coverage:
  web: automated
---

# Log Move Massal dan Unassign Massal Campuran pada Changelog

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Light Vehicles` (`LT-VEH`) memiliki Asset Name `Cargo Net` dan `Strap Set` (masing-masing 0 aset aktif), `Cable Reel` (0 aset aktif), dan `Pickup Van` (3 aset aktif); Asset Class Active `Machinery` (`MACHINERY`).
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Cargo Net dan Strap Set kembali ke LT-VEH dari MACHINERY; Cable Reel kembali ter-assign ke LT-VEH.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-549: Move massal dua Asset Name menulis dua entri L-08 per Asset Name

1. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
2. Ketik Search `LT-VEH`, tekan Enter
3. Klik link Class Code `LT-VEH` di tabel
4. Klik tab `Asset Names`
5. Centang `Cargo Net` dan `Strap Set`, lalu pilih `Bulk Action` > `Move to another asset class`
6. Pilih `Destination Asset Class` = `MACHINERY – Machinery`, lalu klik `[Move]`
7. Tunggu aksi selesai
8. Klik kembali ke tabel Asset Class
9. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
10. Verifikasi jumlah entri Changelog bertambah tepat 4 dari Nc
11. Verifikasi entri Edit Field `Asset Names` Class Code `LT-VEH`: Old Value `Cargo Net`, New Value `—`
12. Verifikasi entri Edit Field `Asset Names` Class Code `MACHINERY`: Old Value `—`, New Value `Cargo Net`
13. Verifikasi entri Edit Field `Asset Names` Class Code `LT-VEH`: Old Value `Strap Set`, New Value `—`
14. Verifikasi entri Edit Field `Asset Names` Class Code `MACHINERY`: Old Value `—`, New Value `Strap Set`
15. Tutup modal Changelog

### TC-FA-FAAC-550: Unassign massal campuran hanya menulis entri L-07 untuk yang berhasil dilepas

16. Buka Fixed Asset > Settings > Accounting > tab Asset Class
17. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
18. Ketik Search `LT-VEH`, tekan Enter
19. Klik link Class Code `LT-VEH` di tabel
20. Klik tab `Asset Names`
21. Centang `Cable Reel` (0 aset aktif) dan `Pickup Van` (3 aset aktif), lalu pilih `Bulk Action` > `Unassign`
22. Klik `[Continue]`
23. Tunggu aksi selesai
24. Klik kembali ke tabel Asset Class
25. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
26. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc (hanya satu entri, untuk Asset Name yang berhasil dilepas)
27. Verifikasi baris teratas Changelog: Field `Asset Names`, Old Value `Cable Reel`, New Value `—`
28. Tutup modal Changelog

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan awal tiap blok TC (baseline log), langkah 2 dan 18 (Search kode `LT-VEH` untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), dan langkah kembali ke layar awal. Langkah "Tunggu aksi selesai" (7, 23) sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log (8b butir 8).
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: Expected b TC-550 "Tidak ada entri untuk Pickup Van (dilewati)" diasersi sebagai selisih tepat satu entri yang barisnya milik Cable Reel; ini asersi jumlah, bukan kelas g. TC-550 tidak menyebut pesan dialog saat Pickup Van dilewati; hanya `[Continue]` yang ditulis.
