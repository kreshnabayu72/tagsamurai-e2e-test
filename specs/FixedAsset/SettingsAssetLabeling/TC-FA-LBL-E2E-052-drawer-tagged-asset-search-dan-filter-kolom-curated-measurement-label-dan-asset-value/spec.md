---
id: TC-FA-LBL-E2E-052-drawer-tagged-asset-search-dan-filter-kolom-curated-measurement-label-dan-asset-value
title: "Drawer Tagged Asset: Search dan Filter kolom curated (Measurement, Label, Asset Value)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/search/FLD-26
  - FALB:obl/T-ALB-02/search/FLD-24
  - FALB:obl/T-ALB-02/search/FLD-29
  - FALB:obl/T-ALB-02/filter/FLD-26
  - FALB:obl/T-ALB-02/filter/FLD-24
coverage:
  web: automated
---

# Drawer Tagged Asset: Search dan Filter kolom curated (Measurement, Label, Asset Value)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-052` dengan 12 aset Active bersuffix `{runId}-052`), `DU-60` (atribut curated pada aset `DU-59`: Measurement dengan sedikitnya dua Symbol berbeda dan Asset Value Commercial dengan nilai ada), `DU-61` (sebagian aset `DU-59` menempel pada lebih dari 2 label bersuffix sehingga sel Label menampilkan `+N more`).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label, aset, dan atribut aset; penghapusan preferensi kolom tersimpan di browser untuk tabel Tagged Asset List di hook `after`. Hook `before` membuat data `DU-59`, `DU-60`, dan `DU-61`; hook `after` menghapusnya.
- State global: konfigurasi kolom tabel Tagged Asset List tersimpan di browser (bukan di server). Spec menampilkan kolom Measurement, Label, dan Asset Value (Commercial) pada langkah 4 sampai 6 dan memulihkannya pada langkah 16 sampai 18; hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset
3. Ubah ukuran halaman Pagination menjadi 25 agar seluruh aset `DU-59` tampil dalam satu halaman
4. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
5. Centang kolom Measurement, Label, dan Asset Value (Commercial)
6. Klik `[Save]`

### FALB:obl/T-ALB-02/search/FLD-26: Search menemukan baris lewat kolom Measurement

7. Ketik Search Symbol Measurement salah satu aset `DU-60`, tekan Enter
8. Verifikasi baris aset ber-Symbol Measurement itu tampil
9. Verifikasi baris aset ber-Symbol Measurement berbeda tidak tampil

### FALB:obl/T-ALB-02/search/FLD-24: Search menemukan baris lewat nama label, termasuk label di balik `+N more`

10. Ganti isi kotak Search dengan nama label tambahan `DU-61` yang tersembunyi di balik `+N more`, tekan Enter
11. Verifikasi baris aset yang memiliki label tambahan itu tampil

### FALB:obl/T-ALB-02/search/FLD-29: Search menemukan baris lewat nilai Asset Value yang tampil

12. Ganti isi kotak Search dengan nilai Asset Value (Commercial) yang tampil pada sel salah satu aset `DU-60`, tekan Enter
13. Verifikasi baris aset pemilik nilai itu tampil
14. Klik `(←)` pada kotak Search
15. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
16. Hapus centang kolom Measurement, Label, dan Asset Value (Commercial)
17. Klik `[Save]`
18. Klik ikon Filter di toolbar Drawer

### FALB:obl/T-ALB-02/filter/FLD-26: Filter kolom Measurement

19. Verifikasi field `Measurement` berupa multi-select searchable dengan placeholder `All units`
20. Pilih satu opsi Symbol pada field `Measurement`, klik `[Apply]`
21. Verifikasi baris aset ber-Symbol Measurement itu tampil
22. Verifikasi baris aset ber-Symbol Measurement lain tidak tampil
23. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter/FLD-24: Filter kolom Label

24. Verifikasi field `Label` berupa multi-select searchable dengan placeholder `All labels`
25. Pilih satu opsi label tambahan `DU-61` pada field `Label`, klik `[Apply]`
26. Verifikasi baris aset yang memiliki label itu tampil
27. Verifikasi baris aset yang tidak memiliki label itu tidak tampil
28. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 3 (ukuran halaman 25), 4 sampai 6 (menampilkan kolom curated sebagai precondition Search, yang terikat visibilitas kolom), 14 (menutup Search), 15 sampai 17 (pemulihan Setup Column tanpa `Verifikasi`; 8b.14, R-24), 18 (membuka Filter Panel), serta 23 dan 28 (mengosongkan Filter Panel, S-09). Filter diasersi sesudah kolom disembunyikan kembali karena Filter independen dari visibilitas kolom (`prd-conventions.md` §9.3, §9.8).
- Anchor positif (bagian 8b butir 2): langkah 8 mendahului absence pada langkah 9; langkah 21 mendahului absence pada langkah 22; langkah 26 mendahului absence pada langkah 27.
- Pembagian klausa lintas spec: `FALB:obl/T-ALB-02/search/FLD-29` diasersi di spec ini untuk nilai pada sel pemegang hak dan di spec 044 untuk sel `No access` yang tidak cocok.
- Langkah 10 mengasersi Search mencocokkan nama label mana pun pada aset, termasuk label di balik `+N more` (PRD §4.1.1 Tabel 2, kolom Catatan FLD-24). Langkah 25 mengasersi opsi Filter Label berupa label distinct dari data tabel.
- Sort kolom Measurement, Label, dan Asset Value diasersi di spec 049; kolom curated tidak tampil sampai dicentang di spec 051.
