---
id: TC-GS-POS-E2E-014-screening-dan-validasi-form-edit
title: Screening dan validasi form Edit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-113
  - TC-GS-POS-34
  - TC-GS-POS-101
  - TC-GS-POS-103
  - TC-GS-POS-44
  - TC-GS-POS-108
coverage:
  web: automated
---

# Screening dan validasi form Edit

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.modal.edit.title` adalah judul modal Edit, yaitu
  `Edit Position`.
- `Fixture.globalSettingsPosition.captions.form.label.positionName` adalah label field, yaitu
  `Position Name *`.
- `Fixture.globalSettingsPosition.captions.form.placeholder.positionName` adalah placeholder input.
  Pada mode Edit placeholder ini tidak replaces nilai, karena field terisi nilai lama.
- `Fixture.globalSettingsPosition.captions.form.actions.save` adalah tombol simpan, yaitu `Save`.
- `Fixture.globalSettingsPosition.captions.form.actions.clearField` adalah tombol reset, yaitu
  `Clear Field`.
- `Fixture.globalSettingsPosition.captions.validation.nameEmpty` adalah pesan error Name kosong, yaitu
  `Name must not be empty`.
- `Fixture.globalSettingsPosition.captions.validation.maxLength` adalah pesan error batas panjang,
  yaitu `Max. 120 characters`.
- `Fixture.globalSettingsPosition.captions.validation.invalidChars` adalah pesan error karakter
  terlarang, yaitu `Name contains invalid characters`.
- `Fixture.globalSettingsPosition.captions.validation.duplicate` adalah pesan error duplikat, yaitu
  `Name already exists`.
- `Fixture.globalSettingsPosition.form.edit.targetName` adalah Position target yang dipakai di
  subbagian pembuka dan validasi, yaitu `Customer Relations Officer`.
- `Fixture.globalSettingsPosition.form.edit.targetName` harus dijamin tidak sedang dipakai sebagai
  target oleh spec lain yang berjalan bersamaan, karena suite ini tidak paralel.
- `Fixture.globalSettingsPosition.form.edit.clearFieldTargetName` adalah Position target terpisah untuk
  subbagian Clear Field, yaitu `Interim Coordinator`.
- `Fixture.globalSettingsPosition.form.edit.collisionTargetName` adalah Position lain yang dipakai
  sebagai sumber duplikat, yaitu `Legal Counsel`.
- `Fixture.globalSettingsPosition.form.edit.maxLengthRejected` adalah string 121 karakter untuk uji
  batas panjang.
- Modal Edit tidak punya checkbox `Stay on this form`, karena PRD §4.2c menetapkan checkbox itu hanya
  untuk mode Create. Keberadaannya di mode Edit diuji di subbagian pembuka.
- Perilaku Clear Field pada mode Edit punya aturan sendiri di PRD §4.4 ayat 2, yaitu mengosongkan
  field dan bukan mengembalikan ke nilai database. Subbagian Clear Field menguji itu secara terpisah
  karena bedanya dari mode Create mudah terlewat.
- Validasi Edit memakai aturan yang sama persis dengan Create, karena keduanya memakai satu form
  specification. Yang diuji di sini adalah penerapan aturan itu pada jalur Edit.

## Test Steps

### Struktur modal Edit

1. Klik ikon Elipsis `(⋯)` pada baris `Fixture.globalSettingsPosition.form.edit.targetName`
2. Verifikasi opsi `Edit` tampil pada menu row action
3. Klik opsi `Edit`
4. Verifikasi modal dengan judul `Fixture.globalSettingsPosition.captions.modal.edit.title` terbuka
5. Verifikasi zona Header memuat judul modal dan icon close `[✕]`
6. Verifikasi zona Form Content memuat field Name
7. Verifikasi field Name terisi nilai lama `Fixture.globalSettingsPosition.form.edit.targetName`
8. Verifikasi kursor fokus berada di field Name sejak modal terbuka
9. Verifikasi field Name menampilkan label
   `Fixture.globalSettingsPosition.captions.form.label.positionName`
10. Verifikasi tanda bintang pada label Name tetap menandakan field wajib
11. Verifikasi modal Edit tidak punya checkbox `Stay on this form after submitting`
12. Verifikasi zona Footer Actions berada di sisi kanan dan memuat tombol
    `Fixture.globalSettingsPosition.captions.form.actions.save` serta
    `Fixture.globalSettingsPosition.captions.form.actions.clearField`
13. Verifikasi tombol Save menggantikan tombol Submit yang dipakai di mode Create
14. Verifikasi tidak ada tombol Submit pada mode Edit
15. Verifikasi tidak ada tombol Cancel di footer, sesuai PRD §4.4 ayat 2
16. Verifikasi area di luar modal terhalang overlay gelap

### Name kosong ditolak saat Edit

17. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.clearField` sehingga field Name
    kosong
18. Verifikasi field Name kosong setelah diklik
19. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.save`
20. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.nameEmpty` muncul
21. Verifikasi field Name ditandai invalid
22. Verifikasi modal Edit tetap terbuka
23. Verifikasi tidak ada toast sukses yang muncul
24. Verifikasi nama lama `Fixture.globalSettingsPosition.form.edit.targetName` masih tampil di tabel
    di belakang modal
25. Verifikasi nama lama tidak ikut terhapus karena pengosongan field di langkah 17

### Batas panjang pada Edit

26. Tutup modal Edit tanpa menyimpan perubahan, lalu buka lagi modal Edit untuk baris yang sama
27. Verifikasi nama lama kembali terisi di field Name
28. Ketik lebih dari 120 karakter ke field Name memakai
    `Fixture.globalSettingsPosition.form.edit.maxLengthRejected`
29. Verifikasi input dibatasi pada 120 karakter pertama
30. Verifikasi panjang isi field Name paling banyak 120 karakter
31. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.maxLength` tidak
    muncul, karena batasnya sudah ditangani level input
32. Verifikasi modal Edit tetap terbuka dan tidak terjadi crash

### Emoji diblokir saat Edit

33. Tutup modal Edit tanpa menyimpan, lalu buka lagi modal Edit untuk baris yang sama
34. Verifikasi nama lama kembali terisi di field Name
35. Letakkan kursor di awal isi field Name
36. Ketik satu keystroke emoji
37. Verifikasi karakter emoji tidak masuk ke field Name
38. Verifikasi isi field Name tetap sama seperti sebelum keystroke
39. Verifikasi nama lama yang sudah ada di field tidak ikut terhapus
40. Tempel string yang mengandung emoji ke field Name
41. Verifikasi bagian emoji dari string yang ditempel tidak masuk ke field Name
42. Verifikasi bagian teks dari string yang ditempel tetap masuk
43. Verifikasi nama lama yang sudah ada di field tetap utuh

### Karakter terlarang lain memicu inline error saat Edit

44. Tutup modal Edit tanpa menyimpan, lalu buka lagi modal Edit untuk baris yang sama
45. Ketik karakter terlarang yang bukan emoji ke field Name
46. Verifikasi karakter tersebut masuk ke field Name
47. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.invalidChars` muncul
    langsung saat mengetik
48. Verifikasi field Name ditandai invalid

### Nama duplikat dengan Position lain saat Edit

49. Verifikasi nama `Fixture.globalSettingsPosition.form.edit.collisionTargetName` sudah ada di tabel
50. Klik ikon Elipsis `(⋯)` pada baris `Fixture.globalSettingsPosition.form.edit.targetName`
51. Klik opsi `Edit`
52. Verifikasi modal Edit terbuka dengan nama lama terisi
53. Hapus seluruh isi field Name, lalu ketik
    `Fixture.globalSettingsPosition.form.edit.collisionTargetName` dengan huruf kecilnya berbeda
54. Tunggu jeda deteksi duplikat real-time
55. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.duplicate` muncul
56. Verifikasi pesan error menyebut nama yang sudah dipakai, yaitu
    `Fixture.globalSettingsPosition.form.edit.collisionTargetName`
57. Klik tombol `[Save]`
58. Verifikasi inline error duplikat tetap muncul setelah menekan Save
59. Verifikasi tidak ada toast sukses yang muncul
60. Verifikasi modal Edit tetap terbuka
61. Verifikasi baris target masih menampilkan nama lamanya, bukan nama yang diketik
62. Verifikasi baris `Fixture.globalSettingsPosition.form.edit.collisionTargetName` tidak ikut berubah
63. Verifikasi tidak ada record baru yang dibuat, karena ini mode Edit bukan Create
64. Verifikasi jumlah total data Position tidak bertambah

### Clear Field mengosongkan field, bukan mengembalikan ke nilai lama

65. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.form.edit.clearFieldTargetName`
66. Klik opsi `Edit`
67. Verifikasi modal Edit terbuka
68. Verifikasi field Name terisi nilai lama
    `Fixture.globalSettingsPosition.form.edit.clearFieldTargetName`
69. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.clearField` tanpa mengubah apa pun
    sebelumnya
70. Verifikasi field Name menjadi kosong, bukan kembali ke nilai lama
71. Verifikasi modal Edit tetap terbuka
72. Verifikasi dialog Unsaved Changes tidak muncul, sesuai PRD §4.4 ayat 2
73. Verifikasi tombol Save dan Clear Field masih tersedia
74. Isi field Name dengan nilai baru yang valid
75. Verifikasi field Name menampilkan nilai baru, bukan nilai lama
76. Klik tombol `[Save]`
77. Verifikasi toast sukses Edit muncul
78. Verifikasi baris target kini menampilkan nilai baru
79. Verifikasi nilai lama `Fixture.globalSettingsPosition.form.edit.clearFieldTargetName` tidak lagi ada
80. Muat ulang halaman browser
81. Verifikasi nilai baru tetap ada setelah muat ulang, sehingga Clear Field bukan sekadar tampilan

## Notes

- Subbagian pembuka memeriksa absennya checkbox Stay on this form karena PRD §4.2c membatasinya hanya
  untuk mode Create. Kalau checkbox ikut tampil di mode Edit, pengguna akan mengira ada opsi yang
  tidak ada, dan test ini tidak akan menangkapnya kalau hanya memeriksa field Name.
- Subbagian Name kosong sengaja memakai Clear Field untuk mengosongkan field, bukan menekan Backspace.
  Ini sekaligus membuktikan bahwa Clear Field bekerja pada langkah 17 sebelum validasi kosong diuji, dan
  menghindari dua langkah manual yang bisa kelewat.
- Langkah 25 memeriksa nama lama tidak terhapus. Ini jaring pengaman tambahan; kalau Clear Field
  memicu penghapusan diam-diam, itu akan hilang tanpa indikasi.
- Emoji pada mode Edit diuji dengan meletakkan kursor di awal field, supaya yang terbukti bukan
  sekadar dua karakter tertolak di akhir, tapi juga bahwa penolakan itu tidak merusak isi field
  yang sudah ada.
- Subbagian duplikat Edit memakai collision target yang sudah ada di tabel dan target yang diedit
  adalah record berbeda. Kalau nama yang dipakai justru nama target itu sendiri, hasilnya akan
  berbeda karena itu kasus Edit No-Op, bukan duplikat. Lihat spec 016 untuk kasus no-op.
- Subbagian Clear Field dipecah dari subbagian validasi karena ia menguji kontrak yang berbeda, yaitu
  reset field, bukan penolakan input. Menggabungkannya membuat test lulus kalau Clear Field kebetulan
  mengosongkan field dengan cara yang salah.
- Memastikan modal dengan tombol Save setelah Clear Field di langkah 74 sampai 78 membuktikan bahwa
  Clear Field benar-benar mengubah state form, bukan hanya menghapus tampilan. Kalau hanya tampilan,
  nilai lama akan terkirim dan test akan gagal.
