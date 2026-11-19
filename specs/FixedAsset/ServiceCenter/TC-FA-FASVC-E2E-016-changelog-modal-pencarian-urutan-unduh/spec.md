---
id: TC-FA-FASVC-E2E-016-changelog-modal-pencarian-urutan-unduh
title: "Modal Changelog: Search, Filter, Sort Default, dan Download"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.6#p1", "§4.2.6#p2", "S-FASVC-17", "EB-DL-1@tabel-changelog", "EB-DL-3@tabel-changelog", "§9.5#r3"]
smoke: []
dependsOn: []
trace:
  "§4.2.6#p1": [28, 29, 30, 35, 37, 39, 41, 43, 55, 57, 68, 69, 132]
  "§4.2.6#p2": [117, 119, 126, 128, 130]
  "S-FASVC-17": [45, 50, 57, 62, 128, 130]
  "EB-DL-1@tabel-changelog": [77, 81, 82, 87, 97, 98, 99, 106, 112, 113]
  "EB-DL-3@tabel-changelog": [80, 86]
  "§9.5#r3": [32, 33, 34]
anchor: []
coverage:
  web: automated
---

# Modal Changelog: Search, Filter, Sort Default, dan Download

## Prerequisites
- Aktor: Total Control `Rina Wijaya` (cakupan seluruh Group). Aktor kedua: Asset Admin `Dewi Pratiwi {runId}`, memegang Role Transaksi Maintenance Routine pada Group `Cabang Utara {runId}` (cakupan Group itu saja).
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - DU-016-1: Group `Cabang Utara {runId}`, anak langsung dari root pohon Group.
  - DU-016-2: Group `Cabang Selatan {runId}`, anak langsung dari root pohon Group.
  - DU-016-3: User `Dewi Pratiwi {runId}`, role Asset Admin, Role Transaksi Maintenance Routine pada `Cabang Utara {runId}`, Status `Active`.
  - DU-016-4: Service Center `Bengkel Utara {runId}`, Service type `Routine`, Available to hanya `Cabang Utara {runId}`, City `Malang`, Company email `utara@bengkelutara.example`, Status `Active`, Usage `0`. Edit pertama mengisi Notes `Catatan Utara {runId}` dan Province / State `Jawa Timur`; edit kedua mengganti Name menjadi `Bengkel Utara Baru {runId}`.
  - DU-016-5: Service Center `Bengkel Selatan {runId}`, Service type `Routine`, Available to hanya `Cabang Selatan {runId}`, City `Surabaya`, Company email `selatan@bengkelselatan.example`, Status `Active`, Usage `0`. Edit mengisi Notes `Catatan Selatan {runId}`.
  - DU-016-6: Service Center `Servis Hapus Utara {runId}`, Service type `Routine`, Available to hanya `Cabang Utara {runId}`, City `Kediri`, Company email `hapus@servisutara.example`, Notes `Catatan Hapus {runId}`, Status `Active`, Usage `0`; dihapus oleh langkah spec ini.
  - DU-016-7: Kata kunci Search `Zzz Tidak Ada {runId}`, tidak cocok dengan nilai di kolom mana pun.
  - DU-016-8: Kata kunci Search `T0` dalam format `dd/MM/yy`, dengan `T0` adalah tanggal hari run saat entri Changelog di atas ditulis.
- Kondisi: Entri Changelog ber-`{runId}` spec ini sesudah langkah penyiapan berjumlah lebih dari 10: lima entri dari DU-016-4, satu dari DU-016-5, dan entri `Deleted` per field terisi dari DU-016-6 (Name, Service type, Available to, City, Company email, dan Notes). Client memiliki lisensi addon Maintenance berstatus aktif. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`. Akun `Dewi Pratiwi {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Entri disiapkan, modal Changelog memuat toolbar dan tabel tanpa aksi baris, dengan urutan default Date terbaru
1. Ketik Search `Bengkel Utara {runId}` pada daftar, tekan Enter
2. Klik `⋯` pada baris `Bengkel Utara {runId}`
3. Klik `Edit`
4. Isi Notes `Catatan Utara {runId}`
5. Isi Province / State `Jawa Timur`
6. Klik `[Save]`
7. Klik `⋯` pada baris `Bengkel Utara {runId}`
8. Klik `Edit`
9. Ganti Name menjadi `Bengkel Utara Baru {runId}`
10. Klik `[Save]`
11. Ganti isi kotak search daftar dengan `Bengkel Utara Baru {runId}`, tekan Enter
12. Klik `⋯` pada baris `Bengkel Utara Baru {runId}`
13. Klik `Inactivate`
14. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
15. Klik `⋯` pada baris `Bengkel Utara Baru {runId}`
16. Klik `Activate`
17. Klik `[Activate]` pada dialog `Activate Service Center`
18. Ganti isi kotak search daftar dengan `Bengkel Selatan {runId}`, tekan Enter
19. Klik `⋯` pada baris `Bengkel Selatan {runId}`
20. Klik `Edit`
21. Isi Notes `Catatan Selatan {runId}`
22. Klik `[Save]`
23. Ganti isi kotak search daftar dengan `Servis Hapus Utara {runId}`, tekan Enter
24. Klik `⋯` pada baris `Servis Hapus Utara {runId}`
25. Klik `Delete`
26. Klik `[Delete]` pada dialog `Delete Service Center`
27. Klik ikon `Changelog` pada toolbar daftar
28. Verifikasi judul modal `Changelog: Service Center` tampil
29. Verifikasi toolbar modal memuat ikon `Search`, `Filter`, dan `Download`
30. Verifikasi tabel modal memuat header kolom `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
31. Ketik Search `Bengkel Utara {runId}` pada modal Changelog, tekan Enter
32. Verifikasi baris dengan Action `Updated`, Field `Name`, Old Value `Bengkel Utara {runId}`, dan New Value `Bengkel Utara Baru {runId}` tampil
33. Verifikasi baris dengan Action `Updated`, Field `Notes`, Old Value `—`, dan New Value `Catatan Utara {runId}` tampil
34. Verifikasi baris `Name` berada di atas baris `Notes`, karena entri yang ditulis lebih akhir tampil lebih atas pada urutan default Date terbaru
35. Verifikasi baris `Notes` tidak memiliki aksi baris pada kolom Actions

### Search mencocokkan substring tanpa membedakan huruf besar-kecil dan membuang spasi tepi
36. Ganti isi kotak search modal dengan `Catatan Utara {runId}`, tekan Enter
37. Verifikasi baris dengan Field `Notes` dan New Value `Catatan Utara {runId}` tampil
38. Ganti isi kotak search modal dengan `kel Utara Baru {runId}`, tekan Enter
39. Verifikasi baris dengan Field `Name` dan New Value `Bengkel Utara Baru {runId}` tampil
40. Ganti isi kotak search modal dengan `bengkel utara baru {runId}`, tekan Enter
41. Verifikasi baris dengan Field `Name` dan New Value `Bengkel Utara Baru {runId}` tampil
42. Ganti isi kotak search modal dengan `Bengkel Utara {runId}` yang diapit satu spasi di awal dan satu spasi di akhir, tekan Enter
43. Verifikasi baris dengan Field `Notes` dan New Value `Catatan Utara {runId}` tampil seperti pada Search tanpa spasi tepi

### Search tidak mencakup kolom tanggal dan kolom yang disembunyikan
44. Ganti isi kotak search modal dengan `T0` dalam format `dd/MM/yy`, tekan Enter
45. Verifikasi empty state dengan judul `No results found` tampil
46. Klik header kolom Actions (`⋯`) pada tabel modal
47. Hilangkan centang `New Value` pada panel Column Visibility
48. Tekan Esc untuk menutup panel Column Visibility
49. Ganti isi kotak search modal dengan `Catatan Utara {runId}`, tekan Enter
50. Verifikasi empty state dengan judul `No results found` tampil
51. Klik header kolom Actions (`⋯`) pada tabel modal
52. Centang `New Value` pada panel Column Visibility
53. Tekan Esc untuk menutup panel Column Visibility
54. Tekan Enter pada kotak search modal
55. Verifikasi baris dengan Field `Notes` dan New Value `Catatan Utara {runId}` tampil kembali

### Search dan Filter tanpa hasil menampilkan empty state
56. Ganti isi kotak search modal dengan `Zzz Tidak Ada {runId}`, tekan Enter
57. Verifikasi empty state dengan judul `No results found` dan keterangan `Try adjusting your search or filter.` tampil
58. Ganti isi kotak search modal dengan `Catatan Utara {runId}`, tekan Enter
59. Klik ikon `Filter` pada toolbar modal
60. Pilih `Deleted` pada filter `Action`
61. Klik `[Apply]`
62. Verifikasi empty state dengan judul `No results found` dan keterangan `Try adjusting your search or filter.` tampil
63. Klik `[Clear Field]`
64. Klik `[Apply]`

### Search menyamakan nilai yang menjadi substring nilai lain
65. Pilih `Bengkel Utara Baru {runId}` pada filter `Service Center Name`
66. Klik `[Apply]`
67. Ganti isi kotak search modal dengan `Activated`, tekan Enter
68. Verifikasi baris dengan Action `Activated` dan Field `Status` tampil
69. Verifikasi baris dengan Action `Inactivated` dan Field `Status` tampil karena `Activated` adalah substring dari `Inactivated`
70. Klik ikon `Filter` pada toolbar modal
71. Klik `[Clear Field]`
72. Klik `[Apply]`
73. Tutup modal Changelog lewat icon close

### Download mengikuti Search, Filter, dan kolom yang tampil, dengan nama berkas dari PRD
74. Klik ikon `Changelog` pada toolbar daftar
75. Ketik Search `{runId}` pada modal Changelog, tekan Enter
76. Klik halaman `2` pada paginasi modal
77. Verifikasi baris dengan Action `Updated`, Field `Notes`, dan New Value `Catatan Utara {runId}` tampil di halaman 2
78. Klik ikon `Download` pada toolbar modal
79. Klik `Download as CSV`
80. Verifikasi nama berkas unduhan `Changelog-Service-Center.csv`
81. Verifikasi berkas memuat baris dengan Action `Deleted`, Field `Name`, dan Old Value `Servis Hapus Utara {runId}`, yang tampil di halaman 1
82. Verifikasi berkas memuat baris dengan Action `Updated`, Field `Notes`, dan New Value `Catatan Utara {runId}`, yang tampil di halaman 2
83. Ketik Search `Catatan Utara {runId}` pada modal Changelog, tekan Enter
84. Klik ikon `Download` pada toolbar modal
85. Klik `Download as XLSX`
86. Verifikasi nama berkas unduhan `Changelog-Service-Center.xlsx`
87. Verifikasi berkas memuat tepat satu baris data, yaitu baris dengan Action `Updated`, Field `Notes`, dan New Value `Catatan Utara {runId}`
88. Ganti isi kotak search modal dengan `{runId}`, tekan Enter
89. Klik ikon `Filter` pada toolbar modal
90. Pilih `Updated` pada filter `Action`
91. Klik `[Apply]`
92. Klik header kolom Actions (`⋯`) pada tabel modal
93. Hilangkan centang `Old Value` pada panel Column Visibility
94. Tekan Esc untuk menutup panel Column Visibility
95. Klik ikon `Download` pada toolbar modal
96. Klik `Download as CSV`
97. Verifikasi berkas memuat baris dengan Action `Updated`, Field `Notes`, dan New Value `Catatan Utara {runId}`
98. Verifikasi berkas tidak memuat baris dengan Action `Deleted` dan Old Value `Servis Hapus Utara {runId}`
99. Verifikasi header berkas memuat `New Value` dan tidak memuat `Old Value`
100. Klik ikon `Filter` pada toolbar modal
101. Klik `[Clear Field]`
102. Klik `[Apply]`
103. Klik `(←)` pada kotak Search modal
104. Tutup modal Changelog lewat icon close

### Download tanpa Search dan Filter memuat semua baris, tidak dibatasi halaman
105. Klik ikon `Changelog` pada toolbar daftar
106. Verifikasi paginasi modal memuat halaman `1` dan halaman `2`
107. Catat baris pertama pada halaman 1 sebagai baris halaman 1
108. Klik halaman `2` pada paginasi modal
109. Catat baris pertama pada halaman 2 sebagai baris halaman 2
110. Klik ikon `Download` pada toolbar modal
111. Klik `Download as CSV`
112. Verifikasi berkas memuat baris halaman 1 yang dicatat
113. Verifikasi berkas memuat baris halaman 2 yang dicatat
114. Tutup modal Changelog lewat icon close

### Changelog memuat entri menurut cakupan Group pengguna
115. Klik ikon `Changelog` pada toolbar daftar
116. Ketik Search `Catatan Selatan {runId}` pada modal Changelog, tekan Enter
117. Verifikasi baris dengan Action `Updated`, Field `Notes`, dan New Value `Catatan Selatan {runId}` tampil bagi Total Control
118. Ganti isi kotak search modal dengan `Servis Hapus Utara {runId}`, tekan Enter
119. Verifikasi baris dengan Action `Deleted`, Field `Name`, Old Value `Servis Hapus Utara {runId}`, dan New Value `—` tampil bagi Total Control
120. Tutup modal Changelog lewat icon close
121. Keluar dari akun `Rina Wijaya`
122. Masuk sebagai `Dewi Pratiwi {runId}`
123. Buka Add-ons > Service Center
124. Klik ikon `Changelog` pada toolbar daftar
125. Ketik Search `Catatan Utara {runId}` pada modal Changelog, tekan Enter
126. Verifikasi baris dengan Action `Updated`, Field `Notes`, dan New Value `Catatan Utara {runId}` tampil bagi `Dewi Pratiwi {runId}`
127. Ganti isi kotak search modal dengan `Catatan Selatan {runId}`, tekan Enter
128. Verifikasi empty state dengan judul `No results found` tampil
129. Ganti isi kotak search modal dengan `Servis Hapus Utara {runId}`, tekan Enter
130. Verifikasi empty state dengan judul `No results found` tampil
131. Tutup modal Changelog lewat icon close
132. Verifikasi halaman daftar Service Center tampil kembali dengan tombol `[+ Service Center]`
