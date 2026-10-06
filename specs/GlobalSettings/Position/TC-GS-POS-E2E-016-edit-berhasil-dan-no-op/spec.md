---
id: TC-GS-POS-E2E-016-edit-berhasil-dan-no-op
title: Edit berhasil dan submit no-op
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-02
  - TC-GS-POS-22
  - TC-GS-POS-25
  - TC-GS-POS-114
coverage:
  web: automated
---

# Edit berhasil dan submit no-op

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.toast.updated` adalah toast sukses Edit, yaitu
  `Success, position has been updated.`
- `Fixture.globalSettingsPosition.captions.toast.noChange` adalah toast netral untuk submit tanpa
  perubahan, yaitu `No changes to save.` Nilainya berbeda dari toast sukses dan dari toast error,
  dan PRD §9.6 mewajibkan yang netral.
- `Fixture.globalSettingsPosition.captions.validation.duplicate` adalah pesan error duplikat, yaitu
  `Name already exists`.
- `Fixture.globalSettingsPosition.captions.form.actions.save` adalah tombol simpan, yaitu `Save`.
- `Fixture.globalSettingsPosition.captions.form.actions.clearField` adalah tombol reset, yaitu
  `Clear Field`.
- `Fixture.globalSettingsPosition.captions.changelog.actions.create` dan `.edit` adalah nilai kolom
  Action pada entri log, yaitu `Create` dan `Edit`. Dipakai untuk menghitung entri log baru.
- `Fixture.globalSettingsPosition.form.edit.targetName` adalah Position target untuk happy path, yaitu
  `IT Support Specialist`.
- `Fixture.globalSettingsPosition.form.edit.targetNewName` adalah nilai barunya, yaitu
  `IT Operations Lead`.
- `Fixture.globalSettingsPosition.form.edit.hoverTargetName` adalah Position target untuk uji tombol,
  yaitu `Customer Relations Officer`.
- `Fixture.globalSettingsPosition.form.edit.defaultSeedName` adalah Position seed bawaan yang
  ditandai `is_default`, yaitu `Finance Manager`. Posisi ini punya user pemakai, jadi yang diuji di
  sini adalah hak edit-nya, bukan hak hapus yang memang diblokir.
- `Fixture.globalSettingsPosition.form.edit.defaultSeedNewName` adalah nilai baru untuk seed tersebut.
- Jumlah entri log pada tiga surface dihitung sebelum dan sesudah setiap mutasi, karena PRD §9.6 dan
  `foundation/functions/changelog-entry.md` §8.5 menetapkan aturan berbeda untuk Edit yang mengubah
  nilai dan Edit no-op.
- Position adalah katalog yang tidak melekat pada satu user, sehingga per
  `foundation/functions/changelog-entry.md` §8.1 ayat 1 tidak ada entri System Log yang ditulis.
  Verifikasi ini dipakai sebagai pembanding untuk memastikan penghitungan log tidak salah baca
  ketiadaan entri di System Log sebagai kegagalan.
- Target happy path `IT Support Specialist` disinkronkan ke dropdown Position pada form User. Yang
  diuji di sini hanya bukti sinkronisasinya secara singkat, pembuktian lengkap ada di spec 047.
- Subbagian dipecah menurut jenis mutasi, yaitu yang mengubah nilai, yang tidak mengubah apa pun,
  yang menguji seed, dan yang menguji tombol. Menggabungkan no-op dengan happy path akan membuat
  penghitungan entri log saling meniadakan.

## Test Steps

### Edit happy path mengubah nama

1. Verifikasi baris `Fixture.globalSettingsPosition.form.edit.targetName` ada di tabel
2. Catat jumlah entri log pada tiga surface sebelum Edit
3. Klik ikon Elipsis `(⋯)` pada baris tersebut
4. Klik opsi `Edit`
5. Verifikasi modal Edit terbuka dengan field Name terisi
   `Fixture.globalSettingsPosition.form.edit.targetName`
6. Hapus seluruh isi field Name, lalu isi dengan
   `Fixture.globalSettingsPosition.form.edit.targetNewName`
7. Verifikasi field Name menampilkan nilai baru
8. Verifikasi tidak ada inline error yang muncul
9. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.save`
10. Verifikasi toast sukses `Fixture.globalSettingsPosition.captions.toast.updated` muncul
11. Verifikasi modal Edit tertutup
12. Verifikasi baris target kini menampilkan
    `Fixture.globalSettingsPosition.form.edit.targetNewName`
13. Verifikasi baris dengan nama lama `Fixture.globalSettingsPosition.form.edit.targetName` tidak lagi
    ada
14. Verifikasi jumlah total data tidak bertambah, karena ini Edit bukan Create
15. Muat ulang halaman browser
16. Verifikasi nama baru tetap ada setelah muat ulang
17. Verifikasi jumlah entri log bertambah tepat satu pada surface Changelog
18. Verifikasi entri log baru mencatat Action Edit dengan Old Value nama lama dan New Value nama baru
19. Verifikasi jumlah entri log Activity Log bertambah tepat satu dan isinya sinkron dengan Changelog
20. Verifikasi tidak ada entri System Log baru, sesuai aturan katalog yang tidak melekat pada user
21. Verifikasi nilai baru tersedia di dropdown Position pada form User

### Submit no-op tidak menghasilkan entri log

22. Catat jumlah entri log pada tiga surface sebelum submit tanpa perubahan
23. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.form.edit.targetNewName`
24. Klik opsi `Edit`
25. Verifikasi field Name terisi `Fixture.globalSettingsPosition.form.edit.targetNewName`
26. Klik tombol `[Save]` tanpa mengubah field Name sama sekali
27. Verifikasi toast netral `Fixture.globalSettingsPosition.captions.toast.noChange` muncul
28. Verifikasi toast sukses Edit tidak muncul pada langkah ini
29. Verifikasi toast error tidak muncul pada langkah ini
30. Verifikasi modal Edit tetap terbuka, sehingga pengguna bisa membatalkan tanpa kehilangan isi
31. Verifikasi field Name masih berisi nilai yang sama
32. Verifikasi jumlah entri log pada Changelog tidak bertambah sama sekali
33. Verifikasi jumlah entri log Activity Log tidak bertambah sama sekali
34. Verifikasi jumlah entri log System Log tetap nol, seperti sebelum submit
35. Verifikasi tidak ada entri log dengan Old Value dan New Value yang sama
36. Verifikasi tidak ada error duplikat muncul terhadap record yang sedang diedit
37. Verifikasi baris di tabel tidak berubah
38. Verifikasi jumlah total data tidak berubah
39. Muat ulang halaman browser
40. Verifikasi jumlah entri log tetap sama setelah muat ulang

### Submit no-op dengan nilai yang identik setelah trim

41. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.form.edit.targetNewName`
42. Klik opsi `Edit`
43. Tambahkan spasi di awal dan akhir pada field Name sehingga isinya identik setelah di-trim
44. Klik tombol `[Save]`
45. Verifikasi toast netral `No changes to save.` muncul
46. Verifikasi toast sukses Edit tidak muncul
47. Verifikasi jumlah entri log tidak bertambah, sehingga perbandingan nilai dilakukan pada nilai
    yang sudah di-trim dan bukan pada input mentah
48. Verifikasi tidak ada error duplikat muncul

### Edit pada Position seed bawaan diizinkan

49. Verifikasi baris `Fixture.globalSettingsPosition.form.edit.defaultSeedName` ada di tabel
50. Verifikasi baris tersebut adalah record seed bawaan, bukan record yang dibuat spec ini
51. Catat jumlah entri log pada tiga surface sebelum Edit
52. Klik ikon Elipsis `(⋯)` pada baris seed tersebut
53. Verifikasi opsi `Edit` tampil pada menu row action
54. Verifikasi opsi `Edit` tidak dalam keadaan nonaktif
55. Klik opsi `Edit`
56. Verifikasi modal Edit terbuka dengan field Name terisi
    `Fixture.globalSettingsPosition.form.edit.defaultSeedName`
57. Hapus seluruh isi field Name, lalu isi dengan
    `Fixture.globalSettingsPosition.form.edit.defaultSeedNewName`
58. Klik tombol `[Save]`
59. Verifikasi toast sukses Edit muncul
60. Verifikasi modal Edit tertutup
61. Verifikasi baris seed kini menampilkan
    `Fixture.globalSettingsPosition.form.edit.defaultSeedNewName`
62. Verifikasi tidak ada dialog pemblokiran yang muncul, karena guard di PRD §9.5 hanya berlaku untuk
    Delete Position yang masih dipakai, bukan untuk Edit
63. Verifikasi status seed pada baris itu tidak berubah menjadi terkunci
64. Verifikasi jumlah entri log Changelog bertambah tepat satu
65. Verifikasi user yang memakai Position itu masih memakai Position yang sama, hanya namanya yang
    berubah
66. Kembalikan nama seed ke
    `Fixture.globalSettingsPosition.form.edit.defaultSeedNewName` menuju
    `Fixture.globalSettingsPosition.form.edit.defaultSeedName` supaya spec lain yang bergantung pada
    nama seed tetap punya targetnya
67. Verifikasi toast sukses Edit muncul saat mengembalikan nama
68. Verifikasi baris seed kembali menampilkan
    `Fixture.globalSettingsPosition.form.edit.defaultSeedName`

### Feedback tombol Save dan Clear Field

69. Catat jumlah entri log pada tiga surface sebelum seluruh subbagian tombol
70. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.form.edit.hoverTargetName`
71. Klik opsi `Edit`
72. Verifikasi modal Edit terbuka
73. Arahkan kursor ke tombol `Fixture.globalSettingsPosition.captions.form.actions.save`
74. Verifikasi tombol Save menampilkan state hover
75. Arahkan kursor ke tombol `Fixture.globalSettingsPosition.captions.form.actions.clearField`
76. Verifikasi tombol Clear Field menampilkan state hover
77. Verifikasi state hover kedua tombol berbeda dari warna latar saat pointer dilepas
78. Verifikasi tombol Save tampil dengan variant filled
79. Verifikasi tombol Clear Field tampil dengan variant text, bukan filled
80. Verifikasi tombol Clear Field tidak sama visual dengan tombol Save
81. Ubah field Name menjadi nilai baru yang valid
82. Klik tombol `[Save]`
83. Verifikasi toast sukses Edit muncul
84. Verifikasi baris target menampilkan nilai baru
85. Verifikasi jumlah entri log bertambah tepat satu, sehingga tidak ada entri log tambahan dari
   yang lain yang tidak terkait mutasi
86. Verifikasi tidak ada entri log yang tercatat saat hanya hover tombol

## Notes

- Toast no-op `No changes to save.` sengaja dibedakan dari toast sukses pada langkah 27 sampai 29.
  PRD §9.6 dan `foundation/functions/changelog-entry.md` §8.5 menyebutnya toast netral, dan kalau
  implementasinya memakai toast sukses, test hanya akan lolos kalau yang diperiksa adalah teksnya.
- Penghitungan entri log dipecah per subbagian dengan penghitungan ulang di awal tiap subbagian.
  Kalau penghitungan dilakukan sekali di awal spec saja, no-op pada subbagian kedua akan terlihat
  sebagai tidak ada perubahan dan lulus karena alasan yang salah.
- Langkah 20 dan 34 memeriksa tidak adanya entri System Log. Ini bukan pemeriksaan negatif, melainkan
  pembanding. `foundation/functions/changelog-entry.md` §8.1 ayat 1 menyatakan Position tidak menulis
  System Log, jadi kalau nanti muncul entri di sana, itu temuan baru dan bukan bagian dari test ini.
- Subbagian no-op dengan spasi tambahan membuktikan perbandingan dilakukan pada nilai hasil trim.
  Tanpa spasi itu, implementasi yang membandingkan input mentah apa adanya akan salah menganggap ada
  perubahan dan tetap menulis entri log.
- Subbagian seed diakhiri dengan mengembalikan nama seed pada langkah 66 sampai 68. Ini wajib karena
  `Finance Manager` juga dipakai spec 018, 019, 020, 023, dan 024 sebagai fixture in-use, dan nama
  yang sudah diganti akan membuat spec-spec itu tidak menemukan targetnya.
- Langkah 54 memeriksa opsi Edit tidak nonaktif. PRD §9.5 hanya melarang Delete pada data yang masih
  dipakai, jadi di mode Edit tidak boleh ada state nonaktif sama sekali.
- Uji tombol dipisah dari mutasi utama, dan jumlah entri log diukurnya diambil ulang di awal
  subbagian. Ini mencegah hover yang salah ikut tercampur dengan entri log dari subbagian
  sebelumnya.
- Sinkronisasi ke dropdown form User diuji hanya sebatas bukti sinkronisasinya secara singkat pada
  langkah 21. Pembuktian penuh dengan kasus lengkap ada di spec 047, supaya kegagalan di sini
  tidak disalahartikan sebagai kegagalan sinkronisasi.
