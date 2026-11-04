---
id: TC-FA-LBL-E2E-044-drawer-tagged-asset-sel-no-access-bagi-pemegang-view-tagged-assets-di-luar-group
title: "Drawer Tagged Asset: sel No access (Asset Value, Warranty Expiry) bagi pemegang View Tagged Assets di luar group"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/empty-value/FLD-29
  - FALB:obl/T-ALB-02/empty-value/FLD-30
  - FALB:obl/T-ALB-02/hover/FLD-30
  - FALB:obl/T-ALB-02/sort/FLD-29
  - FALB:obl/T-ALB-02/sort/FLD-30
  - FALB:obl/T-ALB-02/search/FLD-29
coverage:
  web: automated
---

# Drawer Tagged Asset: sel No access (Asset Value, Warranty Expiry) bagi pemegang View Tagged Assets di luar group

## Prerequisites

- Mode: FE+BE
- Akun aktor: Read Only di group kedua `DU-47` (env `FA_G2RO_EMAIL`, `FA_G2RO_PASSWORD`) pada Group `DU-46`; akun ini memegang View Tagged Assets (PRD §2.1: Read Only dapat melihat Tagged Assets), tanpa akses View asset value dan Manage purchase pada Group pertama. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji: `DU-46` (group kedua beserta departemen dan divisi sendiri), `DU-59` (satu label `Tagged-{runId}-044` dengan 12 aset Active bersuffix `{runId}-044`, tersebar di Group pertama dan Group `DU-46`), `DU-60` (atribut curated pada aset `DU-59`: Asset Value Commercial dan Fiscal serta Warranty Expiry dengan nilai ada dan belum ada).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label, aset, dan atribut aset; hak `DU-47` atas nilai aset dan Manage purchase pada Group `DU-46` dan ketiadaan hak itu pada Group pertama; penghapusan preferensi kolom tersimpan di browser untuk tabel Tagged Asset List di hook `after`. Hook `before` membuat data `DU-59` dan `DU-60`; hook `after` menghapusnya.
- State global: konfigurasi kolom tabel Tagged Asset List akun `DU-47` tersimpan di browser (bukan di server). Spec menampilkan tiga kolom curated pada langkah 4 sampai 6 dan memulihkannya pada langkah 25 sampai 27; hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset
3. Ubah ukuran halaman Pagination menjadi 25 agar seluruh aset `DU-59` tampil dalam satu halaman
4. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
5. Centang kolom Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry
6. Klik `[Save]`

### FALB:obl/T-ALB-02/empty-value/FLD-29: Sel Asset Value di luar hak menampilkan No access

7. Verifikasi sel Asset Value (Commercial) dan Asset Value (Fiscal) pada baris aset Group pertama menampilkan `No access`

### FALB:obl/T-ALB-02/empty-value/FLD-30: Sel Warranty Expiry di luar hak menampilkan No access

8. Verifikasi sel Warranty Expiry pada baris aset Group pertama menampilkan `No access`

### FALB:obl/T-ALB-02/hover/FLD-30: Hover sel Warranty Expiry bertanda No access

9. Arahkan kursor ke sel Warranty Expiry yang menampilkan `No access`
10. Verifikasi tooltip menampilkan `Requires Manage purchase access in this group.`

### FALB:obl/T-ALB-02/sort/FLD-29: Sort kolom Asset Value menempatkan No access paling akhir

11. Verifikasi sedikitnya satu baris aset Group `DU-46` menampilkan nilai pada Asset Value (Commercial) selain `No access`
12. Klik header kolom Asset Value (Commercial)
13. Verifikasi seluruh sel `No access` berada setelah seluruh sel yang menampilkan nilai atau `—` pada Asset Value (Commercial) (ascending)
14. Klik header kolom Asset Value (Commercial) lagi
15. Verifikasi seluruh sel `No access` tetap berada paling akhir pada Asset Value (Commercial) (descending)

### FALB:obl/T-ALB-02/sort/FLD-30: Sort kolom Warranty Expiry menempatkan No access paling akhir

16. Klik header kolom Warranty Expiry
17. Verifikasi seluruh sel `No access` berada setelah seluruh sel yang menampilkan tanggal atau `—` pada Warranty Expiry (Oldest First)
18. Klik header kolom Warranty Expiry lagi
19. Verifikasi seluruh sel `No access` tetap berada paling akhir pada Warranty Expiry (Newest First)

### FALB:obl/T-ALB-02/search/FLD-29: Search nilai Asset Value tidak mencocokkan sel No access

20. Ketik Search nilai Asset Value (Commercial) yang tampil pada sel baris aset Group `DU-46`, tekan Enter
21. Verifikasi baris aset Group `DU-46` pemilik nilai itu tampil
22. Verifikasi baris aset Group pertama (sel `No access`) tidak tampil
23. Klik `(←)` pada kotak Search
24. Verifikasi seluruh aset `DU-59` tampil kembali
25. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
26. Hapus centang kolom Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry
27. Klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 3 (ukuran halaman 25 agar urutan seluruh baris teramati pada satu halaman; 8b.15), 4 sampai 6 (menampilkan kolom curated sebagai precondition), 23 (menutup Search), serta 25 sampai 27 (pemulihan Setup Column tanpa `Verifikasi`; 8b.14, R-24). Langkah 24 adalah pembanding yang membuktikan tabel pulih penuh setelah Search ditutup (S-03).
- Anchor positif (bagian 8b butir 2): langkah 11 membuktikan ada baris berhak pada surface yang sama sebelum asersi urutan pada langkah 13, 15, 17, dan 19; langkah 21 mendahului absence pada langkah 22.
- Pembagian klausa lintas spec: `FALB:obl/T-ALB-02/empty-value/FLD-29`, `FALB:obl/T-ALB-02/empty-value/FLD-30`, dan `FALB:obl/T-ALB-02/hover/FLD-30` diasersi di spec ini untuk sel `No access` dan di spec 043 untuk pemegang hak. `FALB:obl/T-ALB-02/sort/FLD-29` dan `FALB:obl/T-ALB-02/sort/FLD-30` diasersi di spec ini untuk penempatan `No access` paling akhir dan di spec 049 untuk urutan numerik dan tanggal. `FALB:obl/T-ALB-02/search/FLD-29` diasersi di spec ini untuk sel `No access` yang tidak cocok dan di spec 052 untuk nilai pada sel pemegang hak.
- Tooltip `No access` kolom Asset Value (`Requires View asset value access in this group.`) tidak punya ID aturan di indeks, sehingga tidak diasersi.
- Gerbang akses sel dimiliki `asset/` (`AST-LOGIC-10`); spec ini hanya mengasersi klausa sel yang dinyatakan PRD modul ini.
