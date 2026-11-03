---
id: TC-AC-SG-E2E-008-semantik-pilih-node-descendant-all-groups-exclusive-toggle-off-dan-reset-pagination
title: "Semantik Pilih Node: Descendant Rekursif, All Groups, Exclusive, Toggle Off, dan Reset Pagination"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-28
  - TC-AC-SG-29
  - TC-AC-SG-30
  - TC-AC-SG-31
  - TC-AC-SG-35
coverage:
  web: automated
---

# Semantik Pilih Node: Descendant Rekursif, All Groups, Exclusive, Toggle Off, dan Reset Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); `Region A` dengan descendant `Branch 1`, `Branch 2`, `Floor 1`, `Room 301` dan `Region B` dengan descendant `Branch 3`, `Branch 4`; Total User dan Total Member per node (#17, #19): `Region A` 5 dan 4, `Region B` 2 dan 1, agregat All Groups 10 dan 12.
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-008`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-28: Klik node sidebar menampilkan seluruh descendant secara rekursif pada tabel

1. Klik node `Region A` di Sidebar Group Tree
2. Verifikasi tabel menampilkan tepat 4 baris descendant: `Branch 1`, `Branch 2`, `Floor 1`, `Room 301` (rekursif hingga level 4, bukan hanya anak langsung)
3. Verifikasi Group Context Header menampilkan "Region A" | "Total User: 5" | "Total Member: 4" (angka node itu sendiri)
4. Cari baris `Region A` pada tabel
5. Verifikasi node `Region A` sendiri tidak muncul sebagai baris tabel
6. Klik node `Region A` sekali lagi untuk melepas pilihan

### TC-AC-SG-30: Memilih node lain memindahkan pilihan secara exclusive

7. Klik node `Region A`
8. Klik node `Region B`
9. Verifikasi hanya node `Region B` yang ber-highlight
10. Verifikasi node `Region A` di Sidebar Group Tree tidak ber-highlight
11. Verifikasi tabel menampilkan descendant `Region B` (`Branch 3`, `Branch 4`)
12. Verifikasi Group Context Header menampilkan "Region B" | "Total User: 2" | "Total Member: 1"
13. Klik node `Region B` sekali lagi untuk melepas pilihan

### TC-AC-SG-31: Klik ulang node terpilih menjadi toggle off dan kembali ke All Groups

14. Klik node `Region A`
15. Klik node `Region A` sekali lagi
16. Verifikasi pilihan node `Region A` dilepas
17. Verifikasi root "All Groups" aktif kembali
18. Verifikasi tabel menampilkan seluruh 14 group
19. Verifikasi Group Context Header kembali ke agregat "All Groups" | "Total User: 10" | "Total Member: 12"

### TC-AC-SG-29: Node All Groups menampilkan seluruh tree flat dengan pagination

20. Klik node `Region A`
21. Klik root "All Groups (14)"
22. Verifikasi tabel menampilkan seluruh 14 group sebagai daftar flat tanpa filter dengan 10 baris pada halaman 1
23. Pindah ke halaman 2 pada Pagination
24. Verifikasi halaman 2 menampilkan 4 baris
25. Verifikasi Group Context Header kembali "All Groups" | "Total User: 10" | "Total Member: 12"

### TC-AC-SG-35: Mengganti node mereset pagination ke halaman 1

26. Kembali ke halaman 1 pada Pagination
27. Pindah ke halaman 2 pada Pagination (node `All Groups`)
28. Klik node `Region A`
29. Verifikasi tabel kembali ke halaman 1
30. Verifikasi tabel menampilkan 4 baris descendant `Region A`
31. Klik node `Region A` sekali lagi untuk melepas pilihan

## Notes

- Urutan TC di spec: TC-AC-SG-28, 30, 31, 29, lalu 35 supaya pilihan node tiap blok berawal dari `All Groups` dan dipulihkan di akhir blok (S-09); TC-AC-SG-29 dan TC-AC-SG-35 berurutan karena sama-sama memakai Pagination All Groups.
- Langkah penghubung (S-03, S-09): langkah 4 mengamati tanpa asersi sendiri; langkah 6, 13, dan 31 melepas pilihan node; langkah 26 mengembalikan Pagination ke halaman 1 sebelum TC-AC-SG-35.
- Temuan untuk QA:
  - TC-AC-SG-30 langkah 2 (klik `Region A` sebelum `Region B`) tidak punya Expected padanan; exclusive diasersi lewat `Verifikasi` hanya `Region B` yang ber-highlight (langkah 9) dan node `Region A` tidak ber-highlight (langkah 10, pembanding untuk "hanya").
