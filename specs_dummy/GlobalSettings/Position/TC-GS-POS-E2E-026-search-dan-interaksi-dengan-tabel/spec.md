---
id: TC-GS-POS-E2E-026-search-dan-interaksi-dengan-tabel
title: Search by Name, empty state, tooltip, dan interaksi dengan seleksi serta mutasi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-64
  - TC-GS-POS-215
  - TC-GS-POS-216
  - TC-GS-POS-217
  - TC-GS-POS-186
  - TC-GS-POS-188
  - TC-GS-POS-189
  - TC-GS-POS-190
  - TC-GS-POS-191
coverage:
  web: automated
---

# Search by Name, empty state, tooltip, dan interaksi dengan seleksi serta mutasi

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user and role dengan huruf C, U, dan D.
- `Fixture.globalSettingsPosition.data.searchPartialMatch` adalah sebagian teks nama yang cocok dengan
  beberapa Position sekaligus, dipakai untuk menguji pencocokan sebagian dan case-insensitive.
- `Fixture.globalSettingsPosition.data.searchNoMatch` adalah keyword yang dijamin tidak cocok dengan
  nama Position mana pun, dipakai untuk menguji empty state hasil pencarian.
- `Fixture.globalSettingsPosition.data.searchCaseVariants` adalah sepasang nama yang berbeda hanya dari
  huruf besar-kecil, dipakai untuk membuktikan pencarian tidak case-sensitive.
- `Fixture.globalSettingsPosition.data.searchLongName` adalah Position dengan nama panjang yang pasti
  terpotong di kolom Name, dipakai untuk menguji tooltip hasil pemotongan teks.
- `Fixture.globalSettingsPosition.captions.search.placeholder` adalah placeholder kotak pencarian, yaitu
  `Search position name...`
- `Fixture.globalSettingsPosition.captions.emptyFiltered.title` adalah title empty state hasil pencarian
  atau filter, yaitu `No results found`.
- `Fixture.globalSettingsPosition.captions.emptyFiltered.description` adalah description empty state
  tersebut, yaitu `Try adjusting your search or filter.`
- `Fixture.globalSettingsPosition.captions.tableTools` adalah himpunan tombol pada toolbar tabel.
- PRD §5 menetapkan pencarian hanya menyaring berdasarkan kolom Name, bersifat case-insensitive, dan
  dipicu dengan menekan Enter tanpa debounce. Tidak ada pencarian real-time saat mengetik.
- PRD §4.2a menetapkan hanya kolom Name yang searchable. Kolom Last Updated tidak punya kolom search,
  sehingga mengetik di kotak pencarian tidak boleh ikut menyaring berdasarkan tanggal.
- PRD §7.1 menetapkan dua empty state yang berbeda. Tabel yang benar-benar kosong memakai
  `No positions yet`, sedangkan hasil pencarian atau filter yang tidak cocok memakai `No results found`
  dengan description `Try adjusting your search or filter.`
- PRD §9.5 menetapkan default sort Name menaik tanpa filter, search, atau paginasi aktif.
- Konvensi platform menetapkan bahwa checkbox yang sudah tercentang bertahan ketika keyword search
  dikosongkan, dan bahwa data yang tidak lagi cocok dengan search atau filter hilang dari tabel tanpa
  hilang dari server.
- Subbagian dipisah supaya kegagalan satu jenis search tidak menutup jenis search yang lain. Subbagian
  yang membandingkan genuinely empty dengan filtered empty harus berjalan tanpa data yang terpengaruh
  oleh subbagian sebelumnya.

## Test Steps

### Search hanya memicu saat Enter dan hanya menyaring kolom Name

1. Verifikasi kotak pencarian tampil di toolbar tabel dengan placeholder
   `Fixture.globalSettingsPosition.captions.search.placeholder`
2. Verifikasi tabel menampilkan seluruh data tanpa filter
3. Catat jumlah total Position pada footer paginasi
4. Klik kotak pencarian
5. Verifikasi kursor terfokus otomatis di dalam kotak pencarian setelah diklik
6. Verifikasi tidak ada tooltip yang muncul hanya karena kotak pencarian difokuskan
7. Ketik `Fixture.globalSettingsPosition.data.searchPartialMatch` tanpa menekan Enter
8. Verifikasi tabel belum berubah dan total belum berubah, karena pencarian tidak berjalan saat mengetik
9. Tekan tombol Enter
10. Verifikasi tabel sekarang hanya menampilkan Position yang namanya memuat teks tersebut
11. Verifikasi semua baris yang tampil memang cocok dengan keyword
12. Verifikasi total pada footer paginasi berkurang sesuai jumlah hasil
13. Verifikasi tidak ada baris yang tidak cocok ditampilkan
14. Ketik `Fixture.globalSettingsPosition.data.searchNoMatch` pada kotak pencarian yang sama
15. Tekan tombol Enter
16. Verifikasi tabel menjadi kosong dan empty state yang muncul adalah filtered empty, yaitu title
    `Fixture.globalSettingsPosition.captions.emptyFiltered.title`
17. Verifikasi description empty state adalah
    `Fixture.globalSettingsPosition.captions.emptyFiltered.description`
18. Verifikasi empty state tersebut bukan genuinely empty, karena judulnya berbeda dari `No positions yet`
19. Verifikasi toolbar tetap tampil dan kotak pencarian masih terisi, supaya user punya jalan keluar
20. Kosongkan kotak pencarian lalu tekan tombol Enter
21. Verifikasi seluruh data kembali tampil dan total kembali seperti pada langkah 3
22. Verifikasi urutan kembali ke default Name menaik setelah keyword dikosongkan

### Pencarian bersifat case-insensitive dan tidak menyentuh kolom lain

23. Catat nama-nama pada `Fixture.globalSettingsPosition.data.searchCaseVariants` pada tabel tanpa filter
24. Ketik salah satu nama itu ke dalam kotak pencarian dengan huruf besar semua
25. Tekan tombol Enter
26. Verifikasi tabel tetap menampilkan kedua nama yang berbeda hanya dari huruf besar-kecil
27. Verifikasi tidak ada baris yang hilang karena perbedaan kapital
28. Ketik nama yang sama dengan huruf kecil semua
29. Tekan tombol Enter
30. Verifikasi hasil pada langkah 28 sama dengan hasil pada langkah 26
31. Verifikasi kolom Last Updated tidak pernah ikut menyaring hasil, jadi mengetik potongan tanggal
    tidak mengubah hasil
32. Verifikasi tidak ada input pencarian tambahan di toolbar untuk kolom Last Updated
33. Verifikasi himpunan tombol toolbar tetap sama seperti pada langkah 1

### Tooltip pada teks terpotong dan penanda primary identifier

34. Verifikasi baris `Fixture.globalSettingsPosition.data.searchLongName` ada di tabel
35. Verifikasi teks pada kolom Name untuk baris itu terpotong dengan ellipsis, karena tidak muat di
    lebar kolom
36. Arahkan kursor ke teks yang terpotong itu
37. Verifikasi tooltip muncul memuat nama lengkap `Fixture.globalSettingsPosition.data.searchLongName`
38. Verifikasi tooltip memuat teks penuh, bukan versi terpotong yang sama dengan yang tampil di sel
39. Pindahkan kursor menjauhi baris tersebut
40. Verifikasi tooltip hilang
41. Verifikasi nama pada kolom Name memakai warna primary identifier, yaitu styling yang menandai kolom
    utama tabel
42. Verifikasi kolom Last Updated tidak memakai styling primary identifier yang sama

### Seleksi bertahan saat keyword search dikosongkan

43. Verifikasi tabel menampilkan beberapa baris tanpa filter
44. Catat jumlah entri log pada tiga surface sebelum subbagian ini
45. Centang checkbox pada dua baris yang namanya cocok dengan
    `Fixture.globalSettingsPosition.data.searchPartialMatch`
46. Verifikasi counter pada Bulk Action Bar menunjukkan jumlah dua
47. Ketik `Fixture.globalSettingsPosition.data.searchPartialMatch` pada kotak pencarian lalu tekan Enter
48. Verifikasi tabel menyaring sesuai keyword
49. Verifikasi baris yang tercentang masih terlihat karena tetap cocok dengan keyword
50. Verifikasi checkbox pada kedua baris itu tetap tercentang
51. Verifikasi counter pada bar tidak berubah
52. Kosongkan kotak pencarian lalu tekan tombol Enter
53. Verifikasi seluruh data kembali tampil
54. Verifikasi checkbox pada kedua baris yang sama tetap tercentang setelah keyword dikosongkan
55. Verifikasi baris yang tercentang tetap tercatat pada state seleksi meski sempat tidak terlihat
56. Verifikasi tidak ada toast sukses yang muncul, karena tidak ada aksi yang dieksekusi di subbagian ini

### Mutasi Create dan Edit saat search aktif

57. Verifikasi search yang aktif hanya menampilkan sebagian data
58. Catat jumlah entri log pada tiga surface sebelum subbagian ini
59. Klik tombol `+ Position`
60. Verifikasi modal Create Position terbuka
61. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.outsideFilterName`
62. Klik tombol submit pada modal
63. Verifikasi toast sukses `Fixture.globalSettingsPosition.captions.toast.created` muncul
64. Verifikasi tabel tetap menampilkan hasil search yang sama seperti sebelum Create
65. Verifikasi Position
    `Fixture.globalSettingsPosition.form.create.outsideFilterName` tidak muncul di tabel, karena
    namanya tidak cocok dengan keyword search
66. Verifikasi jumlah entri log bertambah satu untuk Create, sehingga mutasi tetap tercatat walau tidak
    terlihat
67. Kosongkan kotak pencarian lalu tekan tombol Enter
68. Verifikasi Position
    `Fixture.globalSettingsPosition.form.create.outsideFilterName` muncul di tabel
69. Verifikasi baris itu berada di posisi urut sesuai default sort Name menaik
70. Ketik lagi `Fixture.globalSettingsPosition.data.searchPartialMatch` lalu tekan tombol Enter
71. Verifikasi baris
        `Fixture.globalSettingsPosition.form.create.outsideFilterName` tidak lagi terlihat karena tidak
        cocok
72. Verifikasi baris yang cocok tetap terlihat
73. Verifikasi `Fixture.globalSettingsPosition.form.edit.targetName` sedang terlihat karena cocok dengan
    keyword
74. Klik ikon Elipsis `(⋯)` pada baris `Fixture.globalSettingsPosition.form.edit.targetName`
75. Klik opsi `Edit`
76. Verifikasi modal Edit terbuka dengan nilai lama
77. Ganti field Name dengan `Fixture.globalSettingsPosition.form.edit.targetNewName` yang tidak lagi cocok
    dengan keyword
78. Klik tombol `Save`
79. Verifikasi toast sukses `Fixture.globalSettingsPosition.captions.toast.updated` muncul
80. Verifikasi baris `Fixture.globalSettingsPosition.form.edit.targetName` hilang dari tabel karena nama
    barunya tidak cocok dengan keyword search aktif
81. Verifikasi baris tidak hilang karena error, melainkan karena tidak cocok dengan filter tampilan
82. Kosongkan kotak pencarian lalu tekan tombol Enter
83. Verifikasi Position yang sudah diubah muncul dengan nama baru
84. Verifikasi nama lama tidak lagi muncul di tabel

## Notes

- Yang diuji di spec ini adalah perilaku search dan akibatnya terhadap seleksi serta mutasi. Kombinasi
  search dengan filter dan sort diuji di spec 027.
- Langkah 8 memastikan pencarian tidak berjalan saat mengetik. Perilaku ini yang membedakan modul ini dari
  tabel lain di platform yang memakai pencarian langsung, jadi kalau berubah, spec ini harus ikut berubah.
- Langkah 31 sampai 33 memeriksa kolom Last Updated tidak punya pencarian. Kolom itu punya filter tanggal,
  bukan pencarian teks, dan membiarkan keduanya aktif akan menyamarkan perbedaan itu.
- Langkah 16 sampai 18 memeriksa filtered empty secara terpisah dari genuinely empty. Keduanya punya
  judul dan description berbeda di PRD §7.1, dan memakai judul yang salah akan mengarahkan user untuk
  membuat Position baru saat sebenarnya hanya keyword search yang salah.
- Langkah 22 memeriksa urutan kembali ke default. Kalau urutannya tetap kosong atau tidak kembali ke
  default, tabel akan tampil dengan urutan yang tidak terduga.
- Tooltip pada langkah 37 adalah satu-satunya cara user membaca nama lengkap Position yang terpotong.
  Tanpa itu, Position dengan nama panjang praktis tidak bisa dibedakan.
- Subbagian keempat sengaja memakai dua baris yang tetap cocok dengan keyword, supaya terlihat apakah
  centang hilang karena filter atau karena state. Kalau barisnya tidak terlihat, checkbox yang tercentang
  tidak bisa diamati langsung.
- Subbagian kelima sengaja memakai nama yang tidak cocok dengan search, supaya efeknya terlihat sebagai
  baris yang hilang, bukan sebagai kegagalan. Kalau data barunya ikut tampil, berarti search tidak
  benar-benar menyaring dan user akan salah mengira Create gagal.
- Langkah 80 sampai 81 memeriksa baris hilang karena tidak cocok, bukan karena error. Dua keadaan itu
  terlihat sama dari sisi user kalau tidak diperiksa eksplisit.
