---
id: TC-GS-POS-E2E-010-validasi-dan-dirty-detection-form-create
title: Validasi form Create, deteksi dirty, dan penutupan form
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-33
  - TC-GS-POS-35
  - TC-GS-POS-37
  - TC-GS-POS-39
  - TC-GS-POS-43
  - TC-GS-POS-107
  - TC-GS-POS-249
coverage:
  web: automated
---

# Validasi form Create, deteksi dirty, dan penutupan form

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.validation.nameEmpty` adalah pesan error untuk Name kosong,
  yaitu `Name must not be empty`.
- `Fixture.globalSettingsPosition.captions.validation.maxLength` adalah pesan error untuk Name lebih
  dari 120 karakter, yaitu `Max. 120 characters`.
- `Fixture.globalSettingsPosition.captions.validation.invalidChars` adalah pesan error untuk karakter
  terlarang, yaitu `Name contains invalid characters`.
- `Fixture.globalSettingsPosition.captions.validation.duplicate` adalah pesan error untuk nama yang
  sudah dipakai, yaitu `Name already exists`.
- `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.title` adalah judul dialog, yaitu
  `Unsaved Changes`.
- `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.body` adalah badan dialog, yaitu
  `You have unsaved changes. Are you sure you want to leave?`
- `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.stay` adalah tombol untuk tetap
  tinggal di form, yaitu `Stay`.
- `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.leave` adalah tombol untuk keluar,
  yaitu `Leave`.
- `Fixture.globalSettingsPosition.captions.form.actions.clearField` adalah label tombol reset, yaitu
  `Clear Field`.
- `Fixture.globalSettingsPosition.form.create.duplicateTarget` adalah nama Position yang sudah ada di
  entitas ini dan dipakai sebagai target uji duplikat, yaitu `IT Manager`.
- `Fixture.globalSettingsPosition.form.create.duplicateTargetVariants` adalah varian huruf besar
  kecil dari nama tersebut yang harus dianggap duplikat, yaitu `it manager` dan `IT MANAGER`.
- `Fixture.globalSettingsPosition.form.create.dirtyName` adalah nama valid untuk menguji form dirty,
  yaitu `Draft`.
- `Fixture.globalSettingsPosition.form.create.maxLengthAllowed` adalah string tepat 120 karakter valid,
  dan `Fixture.globalSettingsPosition.form.create.maxLengthRejected` adalah string 121 karakter.
  Keduanya dibuat oleh fixture, bukan ditulis inline, supaya panjangnya benar-benar terukur.
- `Fixture.globalSettingsPosition.form.create.debounceMs` adalah jeda deteksi duplikat real-time yang
  diambil dari PRD §9.9, yaitu sekitar 500 milidetik. Spec ini tidak mengassert angka ini secara
  ketat, hanya memastikan pesan muncul tanpa perlu blur dan tanpa submit.
- Timing validasi diambil dari PRD §9.9: required dicek setelah Submit, batas panjang dan karakter
  terlarang dicek langsung saat mengetik, dan keunikan dicek real-time dengan debounce plus re-check
  atomik saat Submit.
- Emoji dan karakter terlarang lain dipisahkan jadi dua subbagian karena mekanismenya berbeda. Emoji
  diblokir di level keystroke sehingga tidak pernah masuk ke field, sedangkan karakter terlarang lain
  sampai ke field lalu memicu inline error. Menggabungkannya membuat test tidak bisa membedakan
  blokir yang benar dari pemblokiran yang kebetulan.

## Test Steps

### Name kosong ditolak setelah Submit

1. Klik tombol `[+ Position]` untuk membuka modal Create
2. Biarkan field Name kosong tanpa mengetik apa pun
3. Klik tombol `[Submit]`
4. Verifikasi inline error
   `Fixture.globalSettingsPosition.captions.validation.nameEmpty` muncul di bawah field Name
5. Verifikasi field Name ditandai invalid dengan indikator error yang terlihat
6. Verifikasi modal Create tetap terbuka
7. Verifikasi tidak ada toast sukses yang muncul
8. Verifikasi tidak ada baris baru yang masuk ke tabel
9. Verifikasi jumlah data Position tidak berubah
10. Verifikasi fokus berpindah ke field Name supaya pesan error langsung terbaca
11. Verifikasi field Name tetap terhubung ke pesan error lewat `aria-describedby`

### Batas panjang 120 karakter

12. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.maxLengthAllowed`, yaitu
    string tepat 120 karakter valid
13. Verifikasi tidak ada inline error yang muncul pada langkah ini
14. Verifikasi field Name menampilkan seluruh 120 karakter tanpa terpotong
15. Verifikasi indikator hitung karakter tidak menunjukkan angka yang melebihi 120
16. Verifikasi atribut `maxlength` pada input mencegah input lebih dari 120 karakter

### Input melebihi 120 karakter

17. Kosongkan field Name memakai tombol
    `Fixture.globalSettingsPosition.captions.form.actions.clearField`
18. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.maxLengthRejected`, yaitu string
    121 karakter
19. Verifikasi input dibatasi pada 120 karakter pertama sehingga karakter ke-121 tidak masuk
20. Verifikasi field Name berisi paling banyak 120 karakter
21. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.maxLength` tidak
    muncul pada kondisi ini, karena batasnya sudah ditangani level input
22. Verifikasi setelah modal ditutup dan dibuka ulang, batas 120 karakter tetap berlaku

### Emoji diblokir di level input

23. Buka modal Create baru dengan kondisi field kosong
24. Ketik teks tanpa emoji `Fixture.globalSettingsPosition.form.create.dirtyName` pada field Name
25. Verifikasi teks masuk seluruhnya ke field Name
26. Tekan satu keystroke emoji
27. Verifikasi karakter emoji tidak masuk ke dalam field Name
28. Verifikasi isi field Name tetap sama seperti pada langkah 25
29. Verifikasi nilai yang akan terkirim ke server tidak mengandung karakter emoji
30. Verifikasi posisi kursor tetap berada di dalam field Name, bukan terlempar keluar
31. Verifikasi modal tetap terbuka dan tidak terjadi crash
32. Tempel string yang mengandung emoji ke field Name
33. Verifikasi bagian emoji dari string yang ditempel tidak masuk ke field Name
34. Verifikasi bagian teks dari string yang ditempel tetap masuk
35. Verifikasi field Name tidak mengandung karakter emoji setelah operasi tempel
36. Verifikasi tidak ada karakter lain yang hilang akibat pemotongan emoji, supaya pemotongan tidak
    merusak teks yang tidak boleh terpotong

### Karakter terlarang lain memicu inline error

37. Kosongkan field Name memakai tombol Clear Field
38. Ketik karakter terlarang yang bukan emoji, yaitu yang berada di luar alfanumerik, spasi, dan tanda
    baca standar
39. Verifikasi karakter tersebut masuk ke field Name
40. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.invalidChars` muncul
    langsung saat mengetik
41. Verifikasi field Name ditandai invalid
42. Verifikasi pesan error muncul tanpa perlu menekan Submit

### Nama duplikat terdeteksi real-time tanpa blur

43. Buka modal Create baru dengan kondisi field kosong
44. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.duplicateTargetVariants` yang
    huruf kecilnya berbeda, yaitu `it manager`
45. Verifikasi kursor tetap berada di dalam field Name setelah selesai mengetik
46. Verifikasi fokus belum berpindah keluar dari field Name, sehingga belum terjadi blur
47. Verifikasi tombol `[Submit]` belum diklik
48. Tunggu jeda `Fixture.globalSettingsPosition.form.create.debounceMs` tanpa memindahkan kursor dan
    tanpa memindahkan fokus
49. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.duplicate` muncul
    sendiri tanpa aksi blur maupun submit
50. Verifikasi pesan error menyebut nama yang duplikat dalam bentuk aslinya di server, yaitu
    `Fixture.globalSettingsPosition.form.create.duplicateTarget`
51. Verifikasi field Name ditandai invalid

### Tombol Clear Field mengosongkan field tanpa menutup form

52. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.dirtyName` yang sudah
    dipadding spasi di awal dan akhir
53. Verifikasi field Name menampilkan nilai tersebut lengkap dengan spasi
54. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.clearField`
55. Verifikasi field Name menjadi kosong sepenuhnya, termasuk spasi awal dan akhir
56. Verifikasi modal Create tetap terbuka
57. Verifikasi dialog Unsaved Changes tidak muncul, sesuai PRD §4.4 ayat 2
58. Verifikasi tombol `[Submit]` dan Clear Field masih tersedia
59. Verifikasi fokus berpindah ke field Name yang sekarang kosong
60. Verifikasi nilai `Draft` tidak tersimpan menjadi data Position

### Clear Field juga menghapus status validasi

61. Isi field Name dengan nama duplikat
    `Fixture.globalSettingsPosition.form.create.duplicateTarget` sehingga inline error duplikat muncul
62. Verifikasi inline error duplikat tampil
63. Klik tombol Clear Field
64. Verifikasi field Name kosong
65. Verifikasi inline error duplikat hilang
66. Verifikasi indikator error pada field Name hilang
67. Verifikasi field Name kembali tampil dengan border normal tanpa tanda error

### Menutup form yang tidak dirty tidak memunculkan dialog

68. Buka modal Create dengan field Name kosong
69. Klik icon close `[✕]` pada header modal
70. Verifikasi modal tertutup
71. Verifikasi dialog Unsaved Changes tidak muncul
72. Verifikasi tidak ada perubahan data di tabel

### Menutup form yang dirty memicu dialog Unsaved Changes lewat tiap pemicu

73. Buka modal Create dengan field Name kosong
74. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.dirtyName` sehingga form menjadi
    dirty
75. Verifikasi belum ada dialog Unsaved Changes yang muncul hanya karena mengetik
76. Klik icon close `[✕]` pada header modal
77. Verifikasi dialog dengan judul
    `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.title` muncul
78. Verifikasi badan dialog menampilkan
    `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.body`
79. Verifikasi tombol `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.stay` dan
    `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.leave` keduanya tampil
80. Verifikasi tombol Leave tidak memakai severity danger, sesuai catatan PRD §4.2d
81. Verifikasi modal Create masih terbuka di belakang dialog Unsaved Changes
82. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.leave`
83. Verifikasi modal Create ikut tertutup
84. Verifikasi dialog Unsaved Changes ikut tertutup
85. Verifikasi nilai `Draft` tidak tersimpan menjadi data Position
86. Ulangi langkah 84 sampai 87, kali ini tutup modal memakai tombol `Esc` sebagai pengganti icon
    close
87. Verifikasi dialog Unsaved Changes muncul dari pemicu `Esc`
88. Ulangi langkah 84 sampai 87, kali ini tutup modal dengan klik pada backdrop di luar modal
89. Verifikasi dialog Unsaved Changes muncul dari pemicu klik backdrop
90. Ulangi langkah 84 sampai 87, lalu tutup modal memakai tombol
    `Fixture.globalSettingsPosition.captions.dialog.unsavedChanges.stay`
91. Verifikasi dialog Unsaved Changes tertutup
92. Verifikasi modal Create tetap terbuka
93. Verifikasi field Name masih berisi nilai yang diketik, tidak dikosongkan
94. Verifikasi tidak ada dialog Unsaved Changes yang muncul lagi, karena nilai sudah disimpan di state
    form meskipun belum dikirim ke server
95. Verifikasi data Position di tabel masih belum berubah

### Tombol Clear Field tidak memicu dialog Unsaved Changes
96. Buka modal Create dengan field Name kosong
97. Isi field Name dengan nilai valid sehingga form menjadi dirty
98. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.clearField`
99. Verifikasi dialog Unsaved Changes tidak muncul
100. Verifikasi modal Create tetap terbuka dengan field Name kosong
101. Verifikasi form kembali ke kondisi tidak dirty, sehingga menutup modal berikutnya tidak memunculkan
     dialog
102. Verifikasi tombol Clear Field tidak menutup modal

## Notes

- Timing validasi diambil dari PRD §9.9, bukan dari dugaan. Required dicek setelah Submit, batas
  panjang dan karakter terlarang dicek saat mengetik, keunikan dicek real-time dengan debounce.
  Spec ini menguji ketiga timing itu secara terpisah karena bugs di salah satunya tidak menutupi
  bugs di yang lain.
- Subbagian batas panjang tidak mengharapkan inline error untuk input 121 karakter, karena
  `maxlength` sudah mencegah karakter ke-121 masuk. Dilakukan begitu karena kalau atribut
  `maxlength` hilang, test harus gagal lewat pemeriksaan panjang nilai, bukan lewat pesan error.
- Emoji dan karakter terlarang lain dipisah karena mekanismenya berbeda. Emoji diblokir sebelum
  masuk field sehingga tidak pernah ada di payload, sedangkan karakter terlarang lain masuk dulu
  lalu memicu inline error. Lihat catatan di bawah soal ambiguitas `TC-GS-POS-35`.
- Subbagian duplikat real-time sengaja tidak memindahkan kursor dan tidak memindahkan fokus. Kalau
  salah satu dilakukan, implementasinya yang berbasis blur akan tetap lulus, padahal PRD §9.9
  melarang menunggu kursor keluar field.
- Subbagian re-check atomik memakai varian huruf besar penuh dan langsung menekan Submit tanpa
  menunggu debounce. Ini yang membuktikan ada dua lapis pengecekan, yaitu yang real-time di klien
  dan yang atomik di server.
- Dialog Unsaved Changes diuji lewat tiga pemicu terpisah, yaitu icon close, tombol Esc, dan klik
  backdrop, karena ketiganya punya handler yang berbeda pada library modal dan hanya satu yang
  bisa salah tanpa memengaruhi handler yang lain.
- Langkah 91 memeriksa severity tombol Leave. PRD §4.2d secara khusus melarangnya memakai severity
  danger, dan pemakaiannya yang keliru akan membuat pengguna mengira data hilang permanen padahal
  formnya masih bisa dilanjutkan.
- Langkah 92 memeriksa modal Create masih terbuka di belakang dialog. Kalau modal ikut tertutup,
  pengguna yang menekan Stay akan kehilangan isian yang sudah diketik tanpa pemberitahuan apa pun.
- Subbagian Clear Field sengaja memverifikasi tiga hal sekaligus, yaitu field kosong, modal tetap
  terbuka, dan dialog tidak muncul, karena ketiganya adalah satu kontrak yangPRD §4.4 ayat 2
  tetapkan bersamaan. Mengujinya terpisah membuat kegagalan sulit ditelusuri ke penyebab yang benar.
- Langkah 105 memeriksa dialog tidak muncul lagi setelah menekan Stay. Ini penting karena kondisi
  dirty harus diset ulang saat pengguna eksplisit memilih tetap, kalau tidak dialog akan muncul
  terus untuk data yang sama.
- Catatan ambiguitas sumber: `TC-GS-POS-35` menuliskan nilai harapan `Manager 😀`, yang ambigu antara
  "emoji berhasil diblokir sehingga field berisi `Manager `" dan "emoji masuk lalu error inline
  muncul". Spec ini mengikuti PRD §9.9 yang menyebut emoji diblokir di level keystroke, sehingga
  keduanya tidak dapat terjadi bersamaan. Persis yang ini yang perlu dikonfirmasi pemilik TC kalau
  nanti hasilnya berbeda.
