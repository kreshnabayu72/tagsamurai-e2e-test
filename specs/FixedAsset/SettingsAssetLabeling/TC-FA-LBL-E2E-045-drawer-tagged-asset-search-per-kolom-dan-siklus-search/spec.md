---
id: TC-FA-LBL-E2E-045-drawer-tagged-asset-search-per-kolom-dan-siklus-search
title: "Drawer Tagged Asset: Search per kolom dan siklus Search"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/search-cycle
  - FALB:obl/T-ALB-02/search/FLD-07
  - FALB:obl/T-ALB-02/search/FLD-06
  - FALB:obl/T-ALB-02/search/FLD-25
  - FALB:obl/T-ALB-02/search/FLD-21
  - FALB:obl/T-ALB-02/search/FLD-22
coverage:
  web: automated
---

# Drawer Tagged Asset: Search per kolom dan siklus Search

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-045` dengan 12 aset Active bersuffix `{runId}-045`, lebih dari satu halaman; minimal dua Asset Name, dua Brand, dan dua Model/Type; tag RFID, QR, dan NFC), `DU-58` (kata kunci Search tanpa hasil `zzz-{runId}-045`).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset. Hook `before` membuat label dan aset `DU-59`; hook `after` menghapusnya.
- State global: spec ini tidak mengubah konfigurasi kolom atau state global.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset

### FALB:obl/T-ALB-02/search-cycle: Siklus Search Drawer (Enter, kosongkan, tanpa hasil, reset ke halaman 1)

3. Arahkan kursor ke ikon Search di toolbar Drawer
4. Verifikasi tooltip `Search` tampil
5. Klik ikon Search di toolbar Drawer
6. Verifikasi kotak Search melebar, kursor fokus di dalam input, dan placeholder `Search name, asset ID, brand...`
7. Ketik di kotak Search teks lengkap `[Asset Name] - [Increment]` salah satu aset `DU-59` dengan huruf kapital dan kecil dibalik, tanpa menekan Enter
8. Verifikasi ikon `(✕)` tampil di sisi kanan kotak Search dan tabel belum tersaring (halaman pertama masih menampilkan 10 baris)
9. Tekan Enter
10. Verifikasi baris aset pemilik teks itu tampil pada tabel
11. Verifikasi baris aset dengan Name berbeda tidak tampil pada tabel
12. Klik `(✕)` pada kotak Search
13. Verifikasi isi kotak Search kosong, kotak tetap terbuka, dan tabel masih menampilkan hasil Search terakhir
14. Tekan Enter pada kotak Search yang kosong
15. Verifikasi tabel kembali menampilkan seluruh aset `DU-59` (halaman pertama 10 baris)
16. Ketik Search `DU-58`, tekan Enter
17. Verifikasi empty state tabel menampilkan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
18. Klik `(←)` pada kotak Search
19. Verifikasi kotak Search menutup menjadi ikon Search dan tabel menampilkan kembali seluruh aset `DU-59`
20. Pindah ke halaman 2 pada Pagination
21. Ketik Search nilai kolom Brand salah satu aset `DU-59`, tekan Enter
22. Verifikasi Pagination kembali ke halaman 1 dan tabel menampilkan hasil Search

### FALB:obl/T-ALB-02/search/FLD-07: Search menemukan baris lewat kolom Name

23. Ganti isi kotak Search dengan teks lengkap `[Asset Name] - [Increment]` salah satu aset `DU-59`, tekan Enter
24. Verifikasi baris aset pemilik teks itu tampil

### FALB:obl/T-ALB-02/search/FLD-06: Search menemukan baris lewat kolom Asset ID

25. Ganti isi kotak Search dengan nilai Asset ID salah satu aset `DU-59`, tekan Enter
26. Verifikasi baris aset pemilik Asset ID itu tampil

### FALB:obl/T-ALB-02/search/FLD-25: Search menemukan baris lewat kolom TAG

27. Ganti isi kotak Search dengan `RFID`, tekan Enter
28. Verifikasi baris aset yang memiliki tag aktif RFID tampil

### FALB:obl/T-ALB-02/search/FLD-21: Search menemukan baris lewat kolom Brand

29. Ganti isi kotak Search dengan nama Brand salah satu aset `DU-59`, tekan Enter
30. Verifikasi baris aset ber-Brand itu tampil

### FALB:obl/T-ALB-02/search/FLD-22: Search menemukan baris lewat kolom Model/Type

31. Ganti isi kotak Search dengan nama Model/Type salah satu aset `DU-59`, tekan Enter
32. Verifikasi baris aset ber-Model/Type itu tampil
33. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 20 (pindah ke halaman 2 sebagai precondition reset halaman), dan 33 (menutup Search).
- Pembagian klausa lintas spec: Search kolom Group dan Status ditahan (IGAP-0046 dan IGAP-0051); Search kolom curated Measurement, Label, dan Asset Value diasersi di spec 052 dan spec 044.
- Nilai Search tiap kolom diturunkan dari data `DU-59`: teks lengkap `[Asset Name] - [Increment]` (PRD §4.1.1 Tabel 2, kolom Catatan FLD-07), Asset ID, label aksesibilitas ikon tag (`prd-conventions.md` §9.1a), Brand, dan Model/Type. Langkah 7 sekaligus mengasersi pencocokan tidak membedakan huruf besar-kecil (`prd-conventions.md` §9.16).
- Langkah 8 mengasersi tabel belum tersaring sebelum Enter (`prd-conventions.md` §9.1b): jumlah baris halaman pertama sama dengan sebelum mengetik.
