---
id: TC-GS-POS-E2E-015-boundary-dan-trim-form-edit
title: Boundary panjang dan trim pada form Edit
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-104
  - TC-GS-POS-105
  - TC-GS-POS-106
coverage:
  web: automated
---

# Boundary panjang dan trim pada form Edit

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.toast.updated` adalah toast sukses Edit, yaitu
  `Success, position has been updated.`
- `Fixture.globalSettingsPosition.captions.form.actions.save` adalah tombol simpan, yaitu `Save`.
- `Fixture.globalSettingsPosition.captions.validation.maxLength` adalah pesan error batas panjang,
  yaitu `Max. 120 characters`. Yang diuji di sini penerimaan pada batas bawah dan atas; penolakan di
  atas batas diuji di spec 014.
- `Fixture.globalSettingsPosition.form.edit.targetName` adalah Position target yang dipakai di
  seluruh subbagian, yaitu `Customer Relations Officer`.
- `Fixture.globalSettingsPosition.form.edit.singleCharName` adalah nama satu karakter untuk batas bawah
  non-empty, yaitu `B`.
- `Fixture.globalSettingsPosition.form.edit.maxLengthAllowed` adalah string tepat 120 karakter valid.
- `Fixture.globalSettingsPosition.form.edit.trimmedName` adalah nama hasil trim yang akan disimpan,
  yaitu `Officer 2`.
- `Fixture.globalSettingsPosition.form.edit.paddedName` adalah nilai yang diketik di field, yaitu dua
  spasi di depan dan dua spasi di belakang nama tersebut.
- Nama hasil trim `Fixture.globalSettingsPosition.form.edit.trimmedName` harus dijamin belum dipakai di
  entitas uji. Kalau sudah ada, subbagian trim gagal karena duplikat dan bukan karena trim.
- Setiap subbagian memulihkan nama target ke nilai semula sebelum memulai, supaya subbagian berikutnya
  tidak bergantung pada hasil subbagian sebelumnya. Nama target dipakai ulang karena hanya satu nama
  itu yang disebut eksplisit di ketiga TC sumber.
- Panjang string batas diukur ulang dari isi field, bukan memakai angka yang ditulis di Prerequisites.
  Kalau fixture memakai string yang panjangnya keliru, test harus gagal di sana dengan pesan yang
  jelas, bukan gagal karena submit ditolak.
- Nilai yang diketik pada subbagian batas bawah dan batas atas tidak boleh sama dengan nama lama
  target, supaya hasilnya benar-benar Edit dan bukan no-op. Kasus no-op diuji di spec 016.

## Test Steps

### Batas bawah: satu karakter diterima

1. Klik ikon Elipsis `(⋯)` pada baris `Fixture.globalSettingsPosition.form.edit.targetName`
2. Klik opsi `Edit`
3. Verifikasi modal Edit terbuka dengan nama lama terisi
4. Hapus seluruh isi field Name, lalu isi dengan
   `Fixture.globalSettingsPosition.form.edit.singleCharName`
5. Verifikasi field Name berisi tepat satu karakter dan tidak kosong
6. Verifikasi tidak ada inline error yang muncul
7. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.save`
8. Verifikasi toast sukses `Fixture.globalSettingsPosition.captions.toast.updated` muncul
9. Verifikasi modal Edit tertutup
10. Verifikasi baris target kini menampilkan nama satu karakter itu
11. Verifikasi nama lama `Fixture.globalSettingsPosition.form.edit.targetName` tidak lagi ada
12. Muat ulang halaman browser
13. Verifikasi nama satu karakter itu tetap ada setelah muat ulang
14. Verifikasi panjang nilai pada baris itu tetap satu karakter

### Kembalikan nama target ke nilai semula

15. Klik ikon Elipsis `(⋯)` pada baris yang kini bernama
    `Fixture.globalSettingsPosition.form.edit.singleCharName`
16. Klik opsi `Edit`
17. Isi field Name kembali dengan `Fixture.globalSettingsPosition.form.edit.targetName`
18. Klik tombol `[Save]`
19. Verifikasi toast sukses Edit muncul
20. Verifikasi baris target kembali menampilkan nama semula
21. Verifikasi nama semula tersedia lagi untuk subbagian berikutnya

### Batas atas: tepat 120 karakter diterima

22. Klik ikon Elipsis `(⋯)` pada baris `Fixture.globalSettingsPosition.form.edit.targetName`
23. Klik opsi `Edit`
24. Verifikasi modal Edit terbuka dengan nama lama terisi
25. Hapus seluruh isi field Name, lalu isi dengan
    `Fixture.globalSettingsPosition.form.edit.maxLengthAllowed`
26. Verifikasi panjang isi field Name tepat 120 karakter sesuai hasil hitung ulang
27. Verifikasi field Name menampilkan seluruh 120 karakter tanpa terpotong
28. Verifikasi tidak ada inline error yang muncul
29. Verifikasi indikator hitung karakter tidak menunjukkan angka di atas 120
30. Klik tombol `[Save]`
31. Verifikasi toast sukses Edit muncul
32. Verifikasi modal Edit tertutup
33. Verifikasi baris target kini menampilkan nama 120 karakter itu
34. Verifikasi kolom Name menampilkan seluruh 120 karakter tanpa terpotong atau diringkas
35. Muat ulang halaman browser
36. Verifikasi baris 120 karakter itu tetap ada setelah muat ulang
37. Verifikasi panjang nilai pada baris itu tetap 120 karakter setelah dibaca ulang dari server

### Kembalikan nama target ke nilai semula

38. Klik ikon Elipsis `(⋯)` pada baris yang kini bernama
    `Fixture.globalSettingsPosition.form.edit.maxLengthAllowed`
39. Klik opsi `Edit`
40. Isi field Name kembali dengan `Fixture.globalSettingsPosition.form.edit.targetName`
41. Klik tombol `[Save]`
42. Verifikasi toast sukses Edit muncul
43. Verifikasi baris target kembali menampilkan nama semula

### Spasi awal dan akhir di-trim

44. Klik ikon Elipsis `(⋯)` pada baris `Fixture.globalSettingsPosition.form.edit.targetName`
45. Klik opsi `Edit`
46. Verifikasi modal Edit terbuka dengan nama lama terisi
47. Hapus seluruh isi field Name, lalu isi dengan
    `Fixture.globalSettingsPosition.form.edit.paddedName`, yaitu nilai dengan spasi di awal dan akhir
48. Verifikasi field Name menampilkan nilai tersebut lengkap dengan spasi di kedua ujungnya
49. Verifikasi panjang isi field Name lebih besar daripada panjang nama hasil trim
50. Verifikasi tidak ada inline error yang muncul pada langkah ini
51. Klik tombol `[Save]`
52. Verifikasi toast sukses Edit muncul
53. Verifikasi modal Edit tertutup
54. Verifikasi baris target kini menampilkan
    `Fixture.globalSettingsPosition.form.edit.trimmedName` tanpa spasi di awal dan akhir
55. Verifikasi tidak ada spasi yang tersisa di kedua ujung nilai yang tersimpan
56. Verifikasi spasi di tengah nama tetap dipertahankan
57. Muat ulang halaman browser
58. Verifikasi nilai yang tersimpan tetap tanpa spasi di kedua ujung setelah dibaca dari server
59. Verifikasi trim terjadi di sisi server dan bukan hanya di tampilan tabel
60. Verifikasi nilai lama `Fixture.globalSettingsPosition.form.edit.targetName` tidak lagi ada, sehingga
    trim bukan sekadar mengganti tampilan nama yang sama

### Nilai yang hanya spasi ditolak saat Edit

61. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.form.edit.trimmedName`
62. Klik opsi `Edit`
63. Verifikasi modal Edit terbuka dengan nilai lama terisi
64. Hapus seluruh isi field Name, lalu isi hanya dengan beberapa spasi
65. Verifikasi tidak ada karakter selain spasi di dalam field Name
66. Klik tombol `[Save]`
67. Verifikasi pesan error `Name must not be empty` muncul, karena setelah di-trim tidak ada sisa
    karakter
68. Verifikasi tidak ada toast sukses yang muncul
69. Verifikasi modal Edit tetap terbuka
70. Verifikasi nilai lama `Fixture.globalSettingsPosition.form.edit.trimmedName` tetap tampil di tabel
71. Verifikasi nilai lama tidak ikut terhapus karena field hanya berisi spasi
72. Muat ulang halaman browser
73. Verifikasi nilai lama tetap ada setelah muat ulang, sehingga field yang gagal disimpan tidak
    merusak data yang sudah ada

## Notes

- Subbagian pemulihan nama target disisipkan dua kali karena nama target disebut eksplisit di ketiga
  TC sumber. Tanpa pemulihan, subbagian kedua dan ketiga akan menguji record yang sudah berubah
  oleh subbagian sebelumnya, dan kegagalan tidak bisa dikaitkan ke aturan yang sedang diuji.
- Batas bawah dan batas atas diuji terpisah karena keduanya bisa salah secara independen. Batas atas
  bisa tertanam atribut `maxlength` yang terlalu kecil, sedangkan batas bawah bisa tertanam validasi
  required yang terlalu agresif.
- Panjang string diukur ulang dari isi field pada langkah 26, bukan memakai angka dari Prerequisites.
  Kalau fixture-nya salah panjang, test harus gagal di sana dengan pesan yang jelas, bukan gagal
  diam-diam karena submit ditolak.
- Trim diuji bukan hanya pada nilai yang tersimpan, tetapi juga pada bentuk nilainya setelah dibaca
  ulang dari server. Trim yang hanya terjadi di sisi klien akan terlihat benar di langkah 54 tapi
  salah di langkah 58.
- Nilai yang hanya spasi ditolak adalah pengaman tambahan yang tidak ada di TC sumber. Ini
  konsekuensi langsung dari aturan trim, yaitu spasi di-trim menjadi string kosong, dan kalau
  validasi required dijalankan sebelum trim, data spasi akan lolos membuat Position tanpa nama.
- Langkah 60 memeriksa nilai lama tidak lagi ada. Tanpa itu, trim yang gagal dan hanya mengosongkan
  kedua ujung bisa lolos karena nama lama dan nama baru tetap tercampur.
- Subbagian spasi ditolak juga memeriksa nilai lama tetap ada setelah muat ulang. Ini memastikan
  percobaan gagal tidak merusak data yang sudah ada, yang merupakan sumber daya dipakai spec lain.
- Tidak ada subbagian duplikat setelah trim di spec ini karena kasus itu sudah diuji di spec 014 untuk
  mode Create dan mode Edit memakai aturan yang sama.
