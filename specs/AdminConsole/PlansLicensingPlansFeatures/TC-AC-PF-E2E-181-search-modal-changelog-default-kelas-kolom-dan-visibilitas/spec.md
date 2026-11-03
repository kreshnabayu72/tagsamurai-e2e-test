---
id: TC-AC-PF-E2E-181-search-modal-changelog-default-kelas-kolom-dan-visibilitas
title: Search modal Changelog Default per kelas kolom, tidak mencocokkan Date, dan terikat visibilitas kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-460
  - TC-AC-PF-461
  - TC-AC-PF-462
  - TC-AC-PF-463
coverage:
  web: automated
---

# Search modal Changelog Default per kelas kolom, tidak mencocokkan Date, dan terikat visibilitas kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Kolom Modified By menampilkan `[First Name] [Last Initial]` (nama lengkap Jane Smith, John Doe, Sarah Tan). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: visibilitas kolom modal Changelog Default diubah di blok TC-AC-PF-463 dan dikembalikan ke semua kolom tampil di spec ini; hook `after` menghapus preferensi kolom modal itu di browser (kemampuan disediakan tim FE).

## Test Steps

### Kelas teks: Action, Plan Name, Field, Modified By (TC-AC-PF-460)

1. Klik ikon Changelog pada toolbar tab Default
2. Ketik Search `push`, tekan Enter
3. Verifikasi baris `Push Update`
4. Ganti isi kotak search dengan `sarah`, tekan Enter
5. Verifikasi baris `Push Update` (Modified By `Sarah T`)
6. Ganti isi kotak search dengan `status`, tekan Enter
7. Verifikasi baris `Archive` (Field `Status`)

### Kolom Old Value dan New Value (TC-AC-PF-461)

8. Ganti isi kotak search dengan `active`, tekan Enter
9. Verifikasi baris `Archive Growth Plus (old)` (Old Value `Active`)
10. Ganti isi kotak search dengan `v5`, tekan Enter
11. Verifikasi baris `Push Update`

### Kolom Date tidak dicari (TC-AC-PF-462)

12. Ganti isi kotak search dengan `Aug`, tekan Enter
13. Verifikasi tabel menampilkan "No results found" walau dua entri berbulan Aug
14. Klik `(←)` pada kotak Search

### Search terikat visibilitas kolom (TC-AC-PF-463)

15. Klik header kolom Actions (`⋯`)
16. Hapus centang kolom `Field` pada Overlay Column Visibility
17. Tutup Overlay Column Visibility
18. Ketik Search `status`, tekan Enter
19. Verifikasi hasil "No results found" saat kolom `Field` tersembunyi
20. Klik header kolom Actions (`⋯`)
21. Centang kembali kolom `Field` pada Overlay Column Visibility
22. Tutup Overlay Column Visibility
23. Ganti isi kotak search dengan `status`, tekan Enter
24. Verifikasi baris `Archive Growth Plus (old)` tampil

## Notes

- Langkah penghubung (S-03): langkah 14 menutup input Search dan mereset tabel antar blok; langkah 17 dan 22 menutup overlay Column Visibility.
- Verifikasi langkah 13 dan 19 memakai empty state "No results found" sebagai anchor positif hasil Search (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-PF-463 tidak menyatakan apakah perubahan di Overlay Column Visibility langsung berlaku tanpa Save; spec mengikuti TC-AC-PF-490 yang menyembunyikan kolom lewat overlay yang sama.
  - TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
