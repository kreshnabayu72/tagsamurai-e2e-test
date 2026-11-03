---
id: TC-FA-RP-E2E-159-tab-group-manager-search-2
title: "Tab Group Manager: Search (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-542
  - TC-FA-RP-543
  - TC-FA-RP-544
  - TC-FA-RP-1064
coverage:
  web: automated
---

# Tab Group Manager: Search (2/3)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris), #18 (pohon group), #11 (email Lina Marlina `groupManagerHq_automated_{namaCompany}@qwertysystem.net`, dipakai sebagai data, bukan login), dan #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Tabel Search kolom curated (TC-FA-RP-1064):

| Kolom | Keyword | Baris yang tampil |
|---|---|---|
| Email | `groupmanagerhq` | hanya Lina Marlina |
| Activation Status | `pending activation` | hanya Dimas Pranata |
| Temporary User | `yes` | kedua baris Kevin Susanto |
| TAG | `tag-2001` | hanya Dimas Pranata |
| Cost Center | `cc-200` | hanya Cahyo Aji |
| Badge No | `bn-77` | hanya Fajar Nugroho |

- State yang diubah: konfigurasi kolom Setup Column Tab Group Manager (kolom Group disembunyikan lalu ditampilkan kembali; kolom curated ditampilkan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Kolom tanggal tidak dapat dicari (TC-FA-RP-542)

1. Klik Tab `Group Manager`
2. Catat teks sel Last Updated baris Lina Marlina
3. Ketik Search teks tanggal yang dicatat, tekan Enter
4. Verifikasi empty state `No results found` (kolom tanggal tidak dapat dicari)
5. Klik ikon Filter
6. Verifikasi Filter Panel memuat field `Last Updated` (date range picker, `Select date`) sebagai jalur penyaringan kolom tanggal
7. Tutup Filter Panel
8. Kosongkan isi kotak search, tekan Enter

### Kolom Group disembunyikan tidak dapat dicari (TC-FA-RP-543)

9. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
10. Hapus centang kolom `Group`, lalu klik `[Save]`
11. Ketik Search `rack`, tekan Enter
12. Verifikasi empty state `No results found` (keyword `rack` tidak mencocokkan baris berdasarkan kolom Group yang disembunyikan)
13. Ganti isi kotak search dengan `fajar`, tekan Enter
14. Verifikasi kolom lain yang tampil tetap dapat dicari: hanya baris Fajar Nugroho yang tampil
15. Kosongkan isi kotak search, tekan Enter

### Kolom Group ditampilkan kembali dapat dicari (TC-FA-RP-544)

16. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
17. Centang kembali kolom `Group`, lalu klik `[Save]`
18. Ketik Search `rack`, tekan Enter
19. Verifikasi pencarian kembali mencocokkan baris Dimas Pranata
20. Kosongkan isi kotak search, tekan Enter

### Search kolom curated (TC-FA-RP-1064)

21. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
22. Centang kolom `Email`, `Activation Status`, `Temporary User`, `TAG`, `Cost Center`, dan `Badge No`, lalu klik `[Save]`
23. Untuk setiap baris pada Tabel Search kolom curated, lakukan langkah 24 sampai 26
24. Ketik Search `<Keyword>`, tekan Enter
25. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel
26. Kosongkan isi kotak search, tekan Enter

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 24 sampai 26 adalah blok berulang dengan parameter pada Tabel Search kolom curated (enam iterasi); nominal 26 langkah, ekspansi 41. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #38), dan tiap iterasi berdiri sendiri karena Search dikosongkan di akhir iterasi. Langkah yang diulang: 24 sampai 26.
- Urutan TC: 542, 543, 544, 1064; TC-FA-RP-544 bergantung pada TC-FA-RP-543 sehingga kolom Group yang sudah disembunyikan pada langkah 10 ditampilkan kembali pada langkah 17 (TC-FA-RP-544 langkah "sembunyikan lalu tampilkan" dilebur karena kolom sudah tersembunyi).
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); mencatat teks sel (langkah 2); menutup Filter Panel (langkah 7); membuka Setup Column dan menyimpan (langkah 9, 10, 16, 17, 21, 22); mengosongkan Search (langkah 8, 15, 20, 26); mengganti isi Search (langkah 13).
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC tidak menyebut cara menutup Filter Panel tanpa `[Apply]`; spec menulis "Tutup Filter Panel" sebagai langkah penghubung.
  - TC-FA-RP-543 Expected a bersyarat ("empty state bila tidak ada kolom lain yang cocok"); spec mengasumsikan tidak ada kolom lain yang memuat `rack` pada Pre-setup #38 sehingga empty state tampil.
  - TC-FA-RP-543 Expected b ("kolom lain yang tampil tetap dapat dicari") tidak menyebut keyword; spec memakai `fajar` pada kolom Name (pilihan spec).
  - TC-FA-RP-1064 Precondition menyebut Pre-setup #11 sebagai data (email Lina Marlina `groupManagerHq_automated_...`); Expected hanya menyebut baris Lina Marlina untuk keyword `groupmanagerhq`.
