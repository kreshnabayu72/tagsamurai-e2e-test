---
id: TC-GS-POS-E2E-027-interaksi-search-filter-dan-sort
title: Interaksi Search, Filter Last Updated, dan Sort
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-66
  - TC-GS-POS-67
  - TC-GS-POS-71
  - TC-GS-POS-187
coverage:
  web: automated
---

# Interaksi Search, Filter Last Updated, dan Sort

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user dan role dengan huruf C, U, dan D.
- `Fixture.globalSettingsPosition.data.searchPartialMatch` adalah sebagian teks nama yang cocok dengan
  beberapa Position sekaligus.
- `Fixture.globalSettingsPosition.data.filterRange.recency` adalah rentang Last Updated yang sengaja
  dibuat berbeda dari rentang `Fixture.globalSettingsPosition.data.filterRange.stale`, supaya ada
  Position yang cocok hanya salah satu dari keduanya.
- `Fixture.globalSettingsPosition.data.filterRange.stale` adalah rentang Last Updated lama yang tidak
  beririsan dengan rentang `recency`.
- `Fixture.globalSettingsPosition.captions.filter.panel.label` adalah label field Last Updated di Filter
  Panel, yaitu `Last Updated`.
- `Fixture.globalSettingsPosition.captions.filter.panel.placeholder` adalah placeholder date range
  picker, yaitu `Select date range`.
- `Fixture.globalSettingsPosition.captions.filter.panel.actions.clear` adalah tombol bersihkan filter,
  yaitu `Clear Field`.
- `Fixture.globalSettingsPosition.captions.filter.panel.actions.apply` adalah tombol terapkan filter,
  yaitu `Apply`.
- `Fixture.globalSettingsPosition.captions.sort.ascendingName` dan
  `Fixture.globalSettingsPosition.captions.sort.descendingName` adalah indikator arah pada header kolom
  Name.
- `Fixture.globalSettingsPosition.captions.sort.oldestFirst` dan
  `Fixture.globalSettingsPosition.captions.sort.newestFirst` adalah indikator arah pada header kolom
  Last Updated.
- PRD §5 menetapkan Filter Panel hanya punya satu field, yaitu Last Updated dengan date range picker, dan
  filter baru berlaku saat tombol `Apply` ditekan.
- PRD §9.5 menetapkan default sort kolom Last Updated adalah Newest First, dan nilai kosong selalu
  ditempatkan terakhir baik untuk ascending maupun descending. Karena Position selalu punya Last
  Updated, aturan null-last diuji di spec 029 bersama siklus tiga state.
- Konvensi platform menetapkan tiga hal yang sering tertukar. Search tidak mereset filter, filter tidak
  mereset search, dan ganti kolom sort tidak mereset search maupun filter. Ketiganya diuji di sini.
- Konvensi platform juga menetapkan bahwa menghapus kriteria filter lewat `Clear Field` tidak mereset
  keyword search dan sort yang sedang aktif. Spec 026 menguji arah sebaliknya, yaitu menghapus keyword
  search tidak mereset filter.
- Subbagian dipisah berdasarkan urutan operasi, karena urutan yang berbeda adalah variabel yang diuji
  dan bukan sekadar variasi penulisan.

## Test Steps

### Search dulu, baru filter

1. Verifikasi tabel menampilkan seluruh data tanpa filter dan tanpa search
2. Ketik `Fixture.globalSettingsPosition.data.searchPartialMatch` lalu tekan tombol Enter
3. Verifikasi tabel menampilkan hanya baris yang cocok dengan keyword
4. Buka Filter Panel lewat tombol Filter pada toolbar
5. Verifikasi Filter Panel menampilkan satu field Last Updated dengan label
   `Fixture.globalSettingsPosition.captions.filter.panel.label`
6. Verifikasi date range picker menampilkan placeholder
   `Fixture.globalSettingsPosition.captions.filter.panel.placeholder`
7. Verifikasi tidak ada field lain di Filter Panel, karena tabel ini tidak punya kolom In Use maupun
   Modified By
8. Verifikasi tombol `Clear Field` dan tombol `Apply` tampil
9. Pilih rentang `Fixture.globalSettingsPosition.data.filterRange.stale` pada date range picker
10. Verifikasi tabel belum berubah sebelum tombol `Apply` ditekan, karena filter baru berlaku saat Apply
11. Klik tombol `Fixture.globalSettingsPosition.captions.filter.panel.actions.apply`
12. Verifikasi Filter Panel tertutup setelah Apply
13. Verifikasi tabel menampilkan hasil irisan antara keyword dan rentang filter, yaitu baris yang cocok
    dengan keyword sekaligus Last Updated-nya berada di rentang `stale`
14. Verifikasi keyword pada kotak pencarian tetap terisi dan tidak dikosongkan oleh filter
15. Verifikasi tidak ada baris yang cocok dengan keyword tetapi di luar rentang filter
16. Verifikasi tidak ada baris yang berada di rentang filter tetapi tidak cocok dengan keyword

### Filter dulu, baru search

17. Kosongkan kotak pencarian lalu tekan tombol Enter
18. Verifikasi tabel kembali menampilkan seluruh data
19. Buka Filter Panel
20. Pilih rentang `Fixture.globalSettingsPosition.data.filterRange.recency` lalu tekan tombol `Apply`
21. Verifikasi tabel menampilkan hanya baris dengan Last Updated di rentang `recency`
22. Verifikasi Filter Panel tertutup
23. Ketik `Fixture.globalSettingsPosition.data.searchPartialMatch` lalu tekan tombol Enter
24. Verifikasi tabel menampilkan hasil irisan antara rentang `recency` dan keyword
25. Verifikasi rentang filter tetap aktif, ditunjukkan oleh indikator filter aktif pada toolbar
26. Verifikasi tidak ada baris di luar rentang `recency` yang ditampilkan
27. Verifikasi tidak ada baris yang tidak cocok dengan keyword yang ditampilkan

### Kombinasi Search, Filter, Sort, dan Pagination

28. Verifikasi jumlah hasil pada langkah 27 lebih besar dari
    `Fixture.globalSettingsPosition.pagination.defaultPageSize`, supaya paginasi benar-benar teruji
29. Catat total hasil yang ter-filter
30. Klik header kolom Name untuk mengurutkan menaik
31. Verifikasi urutan baris pada halaman aktif mengikuti abjad menaik
32. Verifikasi indikator arah sort adalah
    `Fixture.globalSettingsPosition.captions.sort.ascendingName`
33. Klik header kolom Name sekali lagi
34. Verifikasi urutan baris mengikuti abjad menurun
35. Verifikasi indikator arah sort adalah
    `Fixture.globalSettingsPosition.captions.sort.descendingName`
36. Pindah ke halaman kedua pada kontrol paginasi
37. Verifikasi halaman kedua juga terurut menurun, bukan kembali ke urutan default
38. Verifikasi keyword search tetap terisi pada halaman kedua
39. Verifikasi rentang filter masih aktif pada halaman kedua
40. Kembali ke halaman pertama
41. Verifikasi urutan pada halaman pertama tetap menurun dan sama seperti sebelum pindah halaman
42. Verifikasi tidak ada data yang berpindah posisi antarp halaman akibat pagination
43. Buka Filter Panel lalu klik tombol
    `Fixture.globalSettingsPosition.captions.filter.panel.actions.clear`
44. Klik tombol `Fixture.globalSettingsPosition.captions.filter.panel.actions.apply`
45. Verifikasi tabel kini menampilkan hasil keyword saja, tanpa pembatasan rentang tanggal
46. Verifikasi keyword search tetap terisi setelah filter dihapus
47. Verifikasi urutan sort yang sedang aktif tetap dipertahankan setelah filter dihapus

### Ganti kolom sort saat search dan filter aktif

48. Verifikasi search dan filter sedang aktif dari subbagian sebelumnya
49. Catat urutan baris pada halaman aktif sebelum ganti kolom sort
50. Klik header kolom Name sampai sort pada kolom Name sedang aktif
51. Klik header kolom Last Updated
52. Verifikasi sort berpindah ke kolom Last Updated, yaitu urutannya bukan lagi mengikuti abjad nama
53. Verifikasi indikator arah sort berpindah ke header kolom Last Updated
54. Verifikasi indikator pada header kolom Name sudah tidak aktif
55. Verifikasi keyword search tetap terisi setelah ganti kolom sort
56. Verifikasi rentang filter masih aktif setelah ganti kolom sort
57. Verifikasi himpunan baris yang tampil sama seperti sebelum ganti kolom sort, jadi hanya urutan yang
    berubah dan bukan isi hasil
58. Verifikasi tidak ada baris yang hilang atau bertambah karena ganti kolom sort
59. Klik header kolom Last Updated lagi untuk menguji arah kedua
60. Verifikasi arah sort pada kolom Last Updated berlawanan dengan langkah 53
61. Verifikasi search dan filter masih aktif setelah klik kedua pada header sort

## Notes

- Yang diuji di spec ini adalah apa yang bertahan dan apa yang hila
ilang saat operasi digabung. Isi data
  dan copywriting filter diuji di spec 028.
- Subbagian pertama dan kedua sengaja dibalik urutannya. Kalau hanya satu urutan diuji, salah satu dari
  dua aturan reset bisa hilang tanpa terdeteksi.
- Langkah 10 memastikan filter baru berlaku setelah `Apply`. Kalau filter langsung berlaku begitu tanggal
  dipilih, test ini akan sering gagal pada langkah yang bukan uji yang dimaksud.
- Langkah 25 memakai indikator filter aktif pada toolbar sebagai bukti filter masih aktif. Isi Filter
  Panel tidak selalu terlihat setelah ditutup, jadi indikator itu satu-satunya bukti yang bisa diamati.
- Langkah 28 memastikan hasil lebih besar dari satu halaman. Kalau hasilnya muat di satu halaman,
  kombinasi paginasi pada langkah 36 tidak benar-benar teruji.
- Langkah 42 memeriksa data tidak berpindah posisi. Urutan yang sama harus berlaku di setiap halaman,
  bukan hanya di halaman yang sedang terlihat.
- Subbagian ketiga juga menguji bahwa menghapus filter tidak mereset search dan sort, karena tiga hal
  itu sering dianggap satu state yang direset bersama.
- Subbagian keempat memindahkan sort antar kolom saat search dan filter aktif. Aturan yang diuji adalah
  sort berpindah, sedangkan search dan filter tetap bertahan dan himpunan baris tidak berubah.
- Langkah 50 memakai fixture arah sort hanya sebagai penanda, bukan sebagai sumber nilai. Arah sort yang
  sebenarnya diamati lewat urutan baris, karena indikator visual bisa saja kosong tanpa mengubah
  urutan yang sebenarnya.
