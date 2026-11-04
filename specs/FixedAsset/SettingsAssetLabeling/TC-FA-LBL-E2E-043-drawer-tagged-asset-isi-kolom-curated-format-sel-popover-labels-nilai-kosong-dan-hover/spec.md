---
id: TC-FA-LBL-E2E-043-drawer-tagged-asset-isi-kolom-curated-format-sel-popover-labels-nilai-kosong-dan-hover
title: "Drawer Tagged Asset: isi kolom curated (format sel, popover Labels, nilai kosong, dan hover)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:component-states/label-chip-badge
  - FALB:obl/T-ALB-02/cell-format
  - FALB:obl/T-ALB-02/link/FLD-24
  - FALB:obl/T-ALB-02/empty-value/FLD-28
  - FALB:obl/T-ALB-02/empty-value/FLD-29
  - FALB:obl/T-ALB-02/empty-value/FLD-30
  - FALB:obl/T-ALB-02/hover/FLD-30
coverage:
  web: automated
---

# Drawer Tagged Asset: isi kolom curated (format sel, popover Labels, nilai kosong, dan hover)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-043` dengan 12 aset Active bersuffix `{runId}-043`; satu aset yang hanya menempel pada label itu juga menempel pada label kedua `LongTrunc043-xxxxxTailEnd-043Z` sepanjang 30 karakter, di luar aset `DU-61`), `DU-60` (atribut curated pada aset `DU-59`: Measurement, Last Scanned, Asset Value, Warranty Expiry dengan nilai ada dan belum ada), `DU-61` (sebagian aset `DU-59` menempel pada lebih dari 2 label sehingga sel Label menampilkan `+N more`).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label, aset, dan atribut aset; penghapusan preferensi kolom tersimpan di browser untuk tabel Tagged Asset List di hook `after`. Hook `before` membuat data `DU-59`, `DU-60`, dan `DU-61`; hook `after` menghapusnya.
- State global: konfigurasi kolom tabel Tagged Asset List tersimpan di browser (bukan di server). Spec menampilkan enam kolom curated pada langkah 3 sampai 5 dan memulihkannya pada langkah 23 sampai 25; hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset
3. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
4. Centang kolom Measurement, Label, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry
5. Klik `[Save]`
6. Ubah ukuran halaman Pagination menjadi 25 agar seluruh aset `DU-59` tampil dalam satu halaman

### FALB:obl/T-ALB-02/cell-format: Format sel kolom curated tabel Tagged Asset List

7. Verifikasi sel Measurement menampilkan Symbol saja (mis. `kg`) tanpa Unit Name
8. Verifikasi sel Label berupa badge berwarna hex label, memuat satu sampai dua badge terurut A–Z diikuti `+N more` bila label aset lebih dari dua
9. Verifikasi sel Last Scanned aset yang pernah dipindai berformat tanggal dan jam sesuai Date Format dan Time Format di Global Settings > General Settings
10. Verifikasi sel Asset Value (Commercial) dan Asset Value (Fiscal) aset bernilai berformat currency 2 desimal dan rata kanan
11. Verifikasi sel Warranty Expiry aset yang garansinya terisi berformat tanggal sesuai Date Format di Global Settings > General Settings

### FALB:obl/T-ALB-02/link/FLD-24: Klik kolom Label membuka popover Labels

12. Klik `+N more` pada sel Label baris aset yang menempel pada lebih dari 2 label (`DU-61`)
13. Verifikasi popover `Labels` tampil dan memuat seluruh label aset sebagai badge penuh tanpa truncation, termasuk label `DU-59`
14. Tekan Esc untuk menutup popover `Labels`

### FALB:component-states/label-chip-badge: Chip Label kolom Label mengikuti truncation badge kontekstual

15. Verifikasi sel Label baris aset yang menempel pada label kedua `DU-59` `LongTrunc043-xxxxxTailEnd-043Z` (30 karakter, lebih dari 25) menampilkan chip `LongTrunc043..TailEnd-043Z` (12 huruf pertama, `..`, 12 huruf terakhir), bukan nama penuh

### FALB:obl/T-ALB-02/empty-value/FLD-28: Nilai kosong kolom Last Scanned

16. Verifikasi sel Last Scanned aset yang belum pernah dipindai menampilkan `—`

### FALB:obl/T-ALB-02/empty-value/FLD-29: Nilai kosong kolom Asset Value bagi pemegang hak

17. Verifikasi sel Asset Value (Commercial) dan Asset Value (Fiscal) aset yang belum memiliki nilai menampilkan `—`

### FALB:obl/T-ALB-02/empty-value/FLD-30: Nilai kosong kolom Warranty Expiry bagi pemegang hak

18. Verifikasi sel Warranty Expiry aset yang garansinya belum diisi menampilkan `—`

### FALB:obl/T-ALB-02/hover/FLD-30: Hover kolom Warranty Expiry

19. Arahkan kursor ke sel Warranty Expiry yang tanggal garansinya sudah lewat
20. Verifikasi tooltip menampilkan `Warranty expired`
21. Arahkan kursor ke sel Warranty Expiry yang tanggal garansinya segera habis
22. Verifikasi tooltip menampilkan `Warranty expires soon`
23. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
24. Hapus centang kolom Measurement, Label, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry
25. Klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 3 sampai 5 (menampilkan kolom curated sebagai precondition), 6 (ukuran halaman 25), 14 (menutup popover), serta 23 sampai 25 (pemulihan Setup Column tanpa `Verifikasi`; 8b.14, R-24).
- Pembagian klausa lintas spec: klausa `FALB:component-states/label-chip-badge` dibagi dua: chip Label pada Labels List dan Live Preview (tampil penuh tanpa truncation) diasersi di spec 030; chip Label pada kolom Label Tabel 2 `FLD-24` di Drawer (truncation `prd-conventions.md` §9.14) diasersi di spec ini pada langkah 15. `FALB:obl/T-ALB-02/cell-format` diasersi di spec 041 untuk kolom default dan di spec ini untuk kolom curated. `FALB:obl/T-ALB-02/empty-value/FLD-29`, `FALB:obl/T-ALB-02/empty-value/FLD-30`, dan `FALB:obl/T-ALB-02/hover/FLD-30` diasersi di spec ini untuk pemegang hak (nilai `—`, tooltip tanggal garansi) dan di spec 044 untuk sel `No access`.
- Temuan PRD: `FALB:obl/T-ALB-02/empty-value/FLD-24` (nilai kosong kolom Label `Tampil —`) tidak dapat dihasilkan oleh data: Tagged Asset List hanya memuat aset yang memakai label yang dibuka, dan kolom Label memuat seluruh label aset termasuk label Drawer itu (PRD §4.1.1 Tabel 2, kolom Catatan FLD-24). Sel Label tidak pernah kosong sehingga klausa `Tampil —` tidak teramati; aturan itu tidak dikutip spec dan ditahan di halaman coverage (baru: nilai kosong kolom Label tidak dapat terjadi di Tagged Asset List).
- Klausa tooltip `No access` kolom Asset Value (`Requires View asset value access in this group.`) tidak punya ID aturan di indeks, sehingga tidak diasersi.
