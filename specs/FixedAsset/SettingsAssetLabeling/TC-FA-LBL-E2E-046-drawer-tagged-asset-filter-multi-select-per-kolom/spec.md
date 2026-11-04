---
id: TC-FA-LBL-E2E-046-drawer-tagged-asset-filter-multi-select-per-kolom
title: "Drawer Tagged Asset: Filter Panel dan Filter multi-select per kolom"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:defaults-ordering-spec/default-filter-tabel
  - FALB:obl/T-ALB-02/filter/FLD-07
  - FALB:obl/T-ALB-02/filter/FLD-25
  - FALB:obl/T-ALB-02/filter/FLD-21
  - FALB:obl/T-ALB-02/filter/FLD-22
  - FALB:obl/T-ALB-02/filter-panel
coverage:
  web: automated
---

# Drawer Tagged Asset: Filter Panel dan Filter multi-select per kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-046` dengan 12 aset Active bersuffix `{runId}-046`; minimal dua Asset Name, dua Brand, dua Model/Type, dan tag RFID, QR, NFC).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset. Hook `before` membuat label dan aset `DU-59`; hook `after` menghapusnya.
- State global: spec ini tidak mengubah konfigurasi kolom atau state global; Filter Panel dikosongkan pada langkah 13, 18, 23, 28, dan 34.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset
3. Ubah ukuran halaman Pagination menjadi 25 agar seluruh aset `DU-59` tampil dalam satu halaman

### FALB:defaults-ordering-spec/default-filter-tabel: Tidak ada filter ter-Apply saat Drawer dibuka

4. Klik ikon Filter di toolbar Drawer
5. Verifikasi Filter Panel tampil di bawah toolbar dengan tombol `[Clear Field]` di kiri dan `[Apply]` di kanan, seluruh field menampilkan placeholder tanpa nilai terpilih, dan ikon Filter tanpa badge titik
6. Verifikasi tabel menampilkan seluruh 12 aset `DU-59`

### FALB:obl/T-ALB-02/filter/FLD-07: Filter kolom Name

7. Verifikasi field `Asset Name` berupa multi-select searchable dengan placeholder `All asset names`
8. Buka dropdown field `Asset Name`
9. Verifikasi opsi dropdown adalah nama aset distinct (tanpa Increment) dari data tabel
10. Pilih satu opsi nama aset, klik `[Apply]`
11. Verifikasi seluruh unit aset bernama itu tampil pada tabel
12. Verifikasi baris aset ber-Asset Name lain tidak tampil pada tabel
13. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter/FLD-25: Filter kolom TAG

14. Verifikasi field `TAG` berupa multi-select searchable dengan placeholder `All tags`
15. Pilih opsi `RFID` pada field `TAG`, klik `[Apply]`
16. Verifikasi baris aset yang memiliki tag aktif RFID tampil pada tabel
17. Verifikasi baris aset yang tidak memiliki tag aktif RFID tidak tampil pada tabel
18. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter/FLD-21: Filter kolom Brand

19. Verifikasi field `Brand` berupa multi-select searchable dengan placeholder `All brands`
20. Pilih satu opsi Brand pada field `Brand`, klik `[Apply]`
21. Verifikasi baris aset ber-Brand itu tampil pada tabel
22. Verifikasi baris aset ber-Brand lain tidak tampil pada tabel
23. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter/FLD-22: Filter kolom Model/Type

24. Verifikasi field `Model/Type` berupa multi-select searchable dengan placeholder `All models`
25. Pilih satu opsi Model/Type pada field `Model/Type`, klik `[Apply]`
26. Verifikasi baris aset ber-Model/Type itu tampil pada tabel
27. Verifikasi baris aset ber-Model/Type lain tidak tampil pada tabel
28. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter-panel: Apply, Clear Field, dan kombinasi antar field

29. Pilih opsi Brand pada field `Brand` dan opsi Model/Type pada field `Model/Type` milik aset `DU-59` yang sama, klik `[Apply]`
30. Verifikasi aset pemilik kedua nilai itu tampil dan setiap baris yang tampil ber-Brand dan ber-Model/Type pilihan (AND antar field)
31. Klik `[Clear Field]`
32. Verifikasi field `Brand` dan `Model/Type` kembali menampilkan placeholder `All brands` dan `All models`
33. Klik `[Apply]`
34. Verifikasi tabel kembali menampilkan seluruh 12 aset `DU-59`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 3 (ukuran halaman 25), 4 (membuka Filter Panel), serta 13, 18, 23, dan 28 (mengosongkan Filter Panel sebelum blok berikutnya, S-09).
- Anchor positif (bagian 8b butir 2): langkah 11, 16, 21, dan 26 mendahului absence pada langkah 12, 17, 22, dan 27.
- Pembagian klausa lintas spec: `FALB:defaults-ordering-spec/default-filter-tabel` diasersi di spec ini untuk Tagged Asset List; klausa Labels List ada di spec 033 dan klausa Modal Changelog: Labels di spec 056.
- Filter kolom curated Measurement dan Label diasersi di spec 052; Filter rentang Asset Value, Last Scanned, Warranty Expiry, dan Last Updated di spec 047. Filter kolom Group dan Status ditahan (IGAP-0046 dan IGAP-0051).
- Opsi dropdown diasersi sebagai nilai distinct dari data tabel (`prd-conventions.md` §9.8); langkah 9 mengasersi opsi `Asset Name` tanpa Increment (PRD §4.1.1 Tabel 2, kolom Catatan FLD-07).
