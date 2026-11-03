---
id: TC-FA-RP-E2E-153-tab-total-control-kombinasi-search-filter-sort-pagination
title: "Tab Total Control: kombinasi Search, Filter, Sort, Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-527
  - TC-FA-RP-528
  - TC-FA-RP-529
  - TC-FA-RP-530
  - TC-FA-RP-531
coverage:
  web: automated
---

# Tab Total Control: kombinasi Search, Filter, Sort, Pagination

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Pre-setup #37 disebut pada Precondition TC sumber tetapi tidak dipakai langkah spec ini.
- Search, Filter, Sort, dan ukuran halaman adalah state sisi klien; spec mengembalikannya ke default di akhir (langkah 28).

## Test Steps

### Kombinasi penuh (TC-FA-RP-527)

1. Klik Tab `Total Control`
2. Ketik Search `Fina`, tekan Enter
3. Klik ikon Filter, pilih opsi `Finance` pada field Division, klik `[Apply]`
4. Klik header kolom Name dua kali (Name descending)
5. Ganti ukuran halaman menjadi 25
6. Verifikasi tabel menampilkan Rudi Hartono lalu Fitri Handayani (irisan Search `Fina` dan Filter Division `Finance`, Sort Name descending)
7. Verifikasi ukuran halaman 25

### Kosongkan Search saat Filter dan Sort aktif (TC-FA-RP-529)

8. Kosongkan isi kotak search, tekan Enter
9. Verifikasi tabel menampilkan Rudi Hartono lalu Fitri Handayani
10. Verifikasi kriteria Filter Division `Finance` dan Sort Name descending tetap aktif menyaring tabel

### Lepas Filter saat Search dan Sort aktif (TC-FA-RP-528)

11. Ketik Search `Fina`, tekan Enter
12. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`
13. Verifikasi tabel menampilkan Siti Rahmawati, Rudi Hartono, lalu Fitri Handayani
14. Verifikasi keyword Search `Fina` dan Sort Name descending tetap aktif menyaring tabel

### Ganti kolom Sort saat Search dan Filter aktif (TC-FA-RP-530)

15. Klik ikon Filter, pilih opsi `Finance` pada field Division, klik `[Apply]`
16. Klik header kolom Position sekali (Position ascending)
17. Verifikasi sort berpindah ke kolom Position ascending: Fitri Handayani (Finance Officer) lalu Rudi Hartono (Finance Supervisor)
18. Verifikasi Search `Fina` dan Filter Division `Finance` tidak direset

### Pemulihan dari empty state Search dan Filter (TC-FA-RP-531)

19. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`
20. Klik `(←)` pada kotak Search
21. Klik header kolom Position dua kali (kembali ke default sort)
22. Ganti ukuran halaman menjadi 10
23. Klik ikon Filter, pilih opsi `HR` pada field Division, klik `[Apply]`
24. Ketik Search `Fina`, tekan Enter
25. Verifikasi empty state `No results found` tampil dengan kombinasi Filter Division `HR` dan Search `Fina`
26. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`
27. Verifikasi tabel pulih menampilkan Fitri Handayani, Rudi Hartono, dan Siti Rahmawati
28. Klik `(←)` pada kotak Search

## Notes

- Urutan TC dalam spec: 527, 529, 528, 530, 531 (bukan urutan nomor). Alasan: state Search, Filter, dan Sort dibangun berurutan sehingga tiap TC memakai state TC sebelumnya tanpa membangun ulang dari nol (S-09, S-10); tiap TC tetap memiliki langkah pembangun state yang disebut di Langkah Uji TC-nya.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik Tab `Total Control` (langkah 1); langkah pemulihan state pada langkah 19 sampai 22 dan 28; langkah 11 dan 15 membangun ulang Search dan Filter untuk TC berikutnya.
- Search `Fina` mengikuti Search yang hanya menyaring saat Enter (bagian 8b butir 9); langkah 8 dan langkah 20 mengosongkan Search, langkah 20 menutup kotak Search.
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - Precondition TC-FA-RP-527 sampai TC-FA-RP-531 menyebut Pre-setup #37 (Tab Read Only) yang tidak dipakai langkah maupun Expected; spec tidak memakainya.
  - TC tidak menyebut apakah Filter Panel menutup sesudah `[Apply]`; spec mengasumsikan panel menutup dan dibuka ulang lewat ikon Filter sebelum `[Clear Field]`.
  - Expected TC-FA-RP-528 dan TC-FA-RP-529 ("tetap aktif menyaring tabel") tidak menyebut indikator yang diamati; spec mengamati indikator sort kolom Name dan nilai Filter pada panel.
