---
id: TC-FA-RP-E2E-137-tab-total-control-search-3
title: "Tab Total Control: Search (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-474
  - TC-FA-RP-475
  - TC-FA-RP-476
  - TC-FA-RP-477
  - TC-FA-RP-478
coverage:
  web: automated
---

# Tab Total Control: Search (3/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; kolom Last Updated memuat teks tanggal sesuai Date Format General Settings #34) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Tab yang dibuka TC 478: Total Control, Read Only, Group Manager, dan System (Pre-setup #38 untuk isi Tab Group Manager dan #39 untuk Tab System tersedia pada tenant yang sama; isi tidak diasersi).
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### Search tidak mencocokkan kolom tanggal (TC 474)

1. Catat teks sel Last Updated baris Siti Rahayu dari layar.
2. Klik ikon Search.
3. Ketik Search teks tanggal yang dicatat pada langkah 1, tekan Enter.
4. Verifikasi tabel menampilkan empty state `No results found` karena kolom tanggal tidak dapat dicari.
5. Klik `✕` pada Search, tekan Enter.
6. Klik ikon Filter.
7. Verifikasi Filter Panel memuat field `Last Updated` bertipe date range picker (penyaringan kolom tanggal hanya melalui Filter Panel).
8. Klik ikon Filter untuk menutup panel.

### Search terikat visibilitas kolom (TC 475 dan TC 476)

9. Sembunyikan kolom Position lewat Setup Column, lalu klik `[Save]`.
10. Ketik Search `custod`, tekan Enter.
11. Verifikasi keyword `custod` tidak mencocokkan baris berdasarkan kolom Position yang disembunyikan; tabel menampilkan empty state `No results found` karena tidak ada kolom lain yang memuat `custod` (Pre-setup #36).
12. Ganti isi kotak search dengan `rina`, tekan Enter.
13. Verifikasi kolom lain yang tampil tetap dapat dicari: hanya baris Rina Wulandari yang tampil.
14. Klik `✕` pada Search, tekan Enter.
15. Tampilkan kembali kolom Position lewat Setup Column, lalu klik `[Save]`.
16. Sembunyikan kolom Position lewat Setup Column, lalu klik `[Save]`.
17. Tampilkan kembali kolom Position lewat Setup Column, lalu klik `[Save]`.
18. Ketik Search `custod`, tekan Enter.
19. Verifikasi pencarian kembali mencocokkan baris Ahmad Fauzi.
20. Klik `✕` pada Search, tekan Enter.

### Search membuang spasi awal dan akhir (TC 477)

21. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
22. Ketik Search `  rina  ` (spasi di awal dan akhir), tekan Enter.
23. Verifikasi tabel tersaring seperti query `rina`: hanya baris Rina Wulandari.
24. Verifikasi isi input tidak berubah (spasi awal dan akhir tetap terlihat di input).
25. Klik `(←)` pada kotak Search.

### Placeholder Search per tab (TC 478)

26. Klik ikon Search di Tab Total Control.
27. Verifikasi placeholder input Search berbunyi `Search name, position, division...`
28. Klik `(←)` pada kotak Search, lalu klik Tab `Read Only`.
29. Klik ikon Search.
30. Verifikasi placeholder input Search berbunyi `Search name, position, division...`
31. Klik `(←)` pada kotak Search, lalu klik Tab `Group Manager`.
32. Klik ikon Search.
33. Verifikasi placeholder input Search berbunyi `Search name, group, position...`
34. Klik `(←)` pada kotak Search, lalu klik Tab `System`.
35. Klik ikon Search.
36. Verifikasi placeholder input Search berbunyi `Search role name...`
37. Klik `(←)` pada kotak Search, lalu klik Tab `Total Control`.

## Notes

- Alasan di atas 35 langkah: seluruh blok berkelas fungsional sama (Search pada tab dan dataset Pre-setup #36 yang sama), tiap blok berdiri sendiri dengan pemulihan state di antaranya, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1, 2, 5, 6, 8, 14, 15, 16, 17, 20, 25, 26, 28, 29, 31, 32, 34, 35, dan 37. Langkah 5, 14, 20, dan 25 mengosongkan atau menutup Search (8b butir 9); langkah 15 memulihkan kolom Position (S-09); langkah 28, 31, 34, dan 37 menutup kotak Search sebelum pindah tab supaya status kotak deterministik.
- Langkah 21 adalah pembanding positif untuk asersi universal langkah 23 (8b butir 2). Langkah 4 dan 11 memakai empty state `No results found` sebagai anchor positif absence hasil Search.
- Copy bertanda `copy usulan, PRD 12 #1` (placeholder Search) di-assert literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - TC 475 Expected b ("kolom lain yang tampil tetap dapat dicari") tidak punya keyword atau langkah di TC; spec memakai keyword `rina` (kolom Name) pada langkah 12 dan 13.
  - TC 474 Expected b ("penyaringan kolom tanggal hanya melalui Filter Panel") bukan keadaan yang teramati langsung; spec mengasersi keberadaan field `Last Updated` di Filter Panel (langkah 6 dan 7) sebagai langkah observasi.
  - TC 478 tidak menyebut keadaan kotak Search sesudah pindah tab; spec menutup kotak dengan `(←)` sebelum pindah tab.
