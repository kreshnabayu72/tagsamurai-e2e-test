---
id: TC-FA-RP-E2E-219-modal-changelog-search-dan-filter-2
title: "Modal Changelog: Search dan Filter (2/6)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-711
  - TC-FA-RP-712
  - TC-FA-RP-713
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter (2/6)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Entri seed #42 ditambahkan fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen (S-12): spec tidak mengasumsikan total entri tetap; entri seed dikenali lewat kombinasi Action, User Name, Old Value, dan New Value, dan total pada info pagination dibandingkan dengan baseline yang dicatat di langkah spec. Spec ini tidak mengubah data.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan di langkah 23 sampai 25; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Keyword Search (TC 711):

| Kolom | Keyword | Hasil yang tampil |
|---|---|---|
| Action | `auto` | hanya entri Auto-Revert Fitri Handayani |
| User Name | `ahmad` | hanya entri Assign Ahmad Fauzi |
| Field | `access` | seluruh entri Tab Total Control (semua Field `Access Level`, termasuk keenam entri seed #42); jumlah hasil sama dengan baseline langkah 2 |
| Old Value | `read only` | hanya entri Assign Maya Anggraeni |
| New Value | `total control` | entri Assign Rina Wulandari, Assign Ahmad Fauzi, Assign Budi Santoso, dan Assign Maya Anggraeni |
| Modified By | `prasetyo` | hanya entri Assign Budi Santoso |

## Test Steps

### Search per kelas teks (TC 711)

1. Klik ikon Changelog pada toolbar.
2. Catat total entri pada info pagination sebagai baseline.
3. Klik ikon Search.
4. Untuk setiap baris pada tabel Keyword Search, lakukan langkah 5 sampai 7.
5. Ketik Search keyword, tekan Enter.
6. Verifikasi baris yang tampil sesuai kolom Hasil yang tampil pada tabel (untuk baris Field, jumlah hasil pada info pagination sama dengan baseline langkah 2).
7. Kosongkan isi kotak search, tekan Enter.

### Search tidak mencocokkan kolom tanggal (TC 712)

8. Catat teks tanggal sel Date entri Assign Ahmad Fauzi (sesuai General Settings).
9. Ketik Search teks tanggal yang dicatat pada langkah 8, tekan Enter.
10. Verifikasi tabel menampilkan empty state `No results found`.
11. Klik ikon Filter.
12. Verifikasi panel Filter memuat field `Date` (date range picker).
13. Klik ikon Filter untuk menutup panel.
14. Kosongkan isi kotak search, tekan Enter.

### Search terikat visibilitas kolom (TC 713)

15. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
16. Hapus centang kolom `Modified By`.
17. Klik `[Save]`.
18. Ketik Search `prasetyo`, tekan Enter.
19. Verifikasi empty state `No results found`: keyword `prasetyo` tidak mencocokkan baris berdasarkan kolom `Modified By` yang disembunyikan.
20. Ganti isi kotak search dengan `ahmad`, tekan Enter.
21. Verifikasi entri Assign Ahmad Fauzi tampil: kolom lain yang tampil tetap dapat dicari.
22. Kosongkan isi kotak search, tekan Enter.
23. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
24. Centang kembali kolom `Modified By`.
25. Klik `[Save]`.

## Notes

- Alasan di atas 35 langkah: langkah 5 sampai 7 adalah blok berulang dengan parameter pada tabel Prerequisites (enam iterasi); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena Search dikosongkan di akhir iterasi. Langkah yang diulang: 5 sampai 7. `Verifikasi` tetap satu per klausa Expected (S-01).
- Langkah penghubung (S-03): langkah 2 (mencatat total entri sebagai baseline TC 711 langkah 3), 3 (membuka input Search), 4 (kepala perulangan), 7, 8 (mencatat teks Date sebagai nilai keyword TC 712), 13, 14, 22, serta 23 sampai 25 (memulihkan kolom `Modified By`).
- Langkah 11 dan 12 mewujudkan Expected TC 712 butir b ("penyaringan kolom tanggal hanya melalui Filter Panel") dengan asersi bahwa panel Filter memiliki field `Date`; langkah 20 dan 21 mewujudkan Expected TC 713 butir b memakai keyword `ahmad` dari TC 711 (alasan: TC tidak memberi langkah untuk butir itu).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 713 butir b ("kolom lain yang tampil tetap dapat dicari") tidak punya langkah pada TC; spec menambah langkah 20 dan 21.
  - TC 712 butir b menyatakan hal yang tidak teramati langsung; spec mengasersi keberadaan field `Date` di Filter Panel.
