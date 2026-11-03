---
id: TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari
title: "Search Client List Terikat Visibilitas Kolom: Nilai Kolom Hidden Tidak Ditemukan, Ditemukan Setelah Kolom Ditampilkan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-365
  - TC-AC-ACC-366
  - TC-AC-ACC-367
  - TC-AC-ACC-368
  - TC-AC-ACC-369
  - TC-AC-ACC-370
  - TC-AC-ACC-371
  - TC-AC-ACC-930
coverage:
  web: automated
---

# Search Client List Terikat Visibilitas Kolom: Nilai Kolom Hidden Tidak Ditemukan, Ditemukan Setelah Kolom Ditampilkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-LST-1 `PT Sortir Alfa` (juga C-LST-2 `PT Sortir Beta` dan C-LST-3 `PT Sortir Gamma`) tersedia dan hanya dibaca. Kolom Company Email, PIC Email, PIC Phone, Industry, Country, State, dan City berada pada kondisi Hidden default untuk akun A-01 saat spec mulai (preferensi per pengguna).
- Tabel parameter kolom Curated (dipakai langkah 1 sampai 8): Company Email `kontak@sortiralfa.qwertysystem.net`; PIC Email `hendra@sortiralfa.qwertysystem.net`; PIC Phone `081300000030`; Industry `Healthcare`; Country `Malaysia`; State `Selangor`; City `Shah Alam`. Nilai kolom `PT Sortir Alfa` sama dengan kata kunci.
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Kemampuan teknis: menghapus preferensi Setup Column di browser (disediakan tim FE). Tidak butuh intercept, klien HTTP, atau jam server.

## Test Steps

### Kolom Curated Hidden tidak dicari (TC-AC-ACC-365 sampai TC-AC-ACC-371)

1. Untuk setiap baris tabel parameter kolom Curated: ketik Search kata kunci kolom itu, tekan Enter
2. Verifikasi empty state `No results found` tampil (anchor bahwa hasil Search sudah diproses)
3. Verifikasi baris `PT Sortir Alfa` tidak tampil karena kolom Hidden tidak dapat dicari
4. Klik header kolom Actions `(⋯)` lalu centang kolom itu
5. Ganti isi kotak search dengan kata kunci yang sama, tekan Enter
6. Verifikasi kolom itu tampil di tabel
7. Verifikasi baris `PT Sortir Alfa` tampil dengan nilai kolom sama dengan kata kunci
8. Klik header kolom Actions `(⋯)` lalu hapus centang kolom itu (pulihkan preferensi Setup Column A-01), lalu klik `(←)` pada kotak Search

### Kolom Hideable PIC Name disembunyikan lalu ditampilkan (TC-AC-ACC-930)

9. Klik header kolom Actions `(⋯)` lalu hapus centang PIC Name
10. Verifikasi kolom PIC Name hilang dari tabel
11. Ketik Search `Hendra Gunawan`, tekan Enter
12. Verifikasi empty state `No results found` tampil (anchor bahwa hasil Search sudah diproses)
13. Verifikasi baris `PT Sortir Alfa` tidak tampil karena kolom PIC Name Hidden tidak dapat dicari
14. Verifikasi baris `PT Sortir Beta` dan `PT Sortir Gamma` tidak tampil
15. Klik header kolom Actions `(⋯)` lalu centang PIC Name
16. Ganti isi kotak search dengan `Hendra Gunawan`, tekan Enter (Search diulang setelah kolom ditampilkan)
17. Verifikasi kolom PIC Name tampil kembali
18. Verifikasi baris `PT Sortir Alfa` tampil dengan PIC Name `Hendra Gunawan`
19. Klik `(←)` pada kotak Search

## Notes

- Langkah 1 sampai 8 diulang per baris tabel parameter (7 iterasi); `Verifikasi` tiap klausa Expected ditulis sekali per iterasi. Spec melewati sekitar 35 langkah setelah ekspansi; alasan: seluruh blok satu kelas harness dan dataset (Search List dengan Setup Column) dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Langkah penghubung (S-03): `(←)` pada kotak Search, centang/hapus centang kolom untuk pemulihan preferensi (Post Condition TC-AC-ACC-365 sampai TC-AC-ACC-371 dan TC-AC-ACC-930 menyebut pemulihan), dan `Verifikasi` empty state `No results found` sebagai anchor positif absence baris (bagian 8b butir 2) yang tidak tertulis di Expected TC.
- Temuan untuk QA
  - TC-AC-ACC-930: Post Condition `Kolom PIC Name dicentang kembali pada Langkah 4` dan Langkah TC tidak mengosongkan kotak Search sebelum Search kedua; spec memakai `ganti isi kotak search dengan`.
