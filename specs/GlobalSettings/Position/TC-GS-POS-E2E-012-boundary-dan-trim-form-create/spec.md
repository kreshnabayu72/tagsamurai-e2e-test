---
id: TC-GS-POS-E2E-012-boundary-dan-trim-form-create
title: Boundary panjang dan trim pada form Create
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-40
  - TC-GS-POS-41
  - TC-GS-POS-42
coverage:
  web: automated
---

# Boundary panjang dan trim pada form Create

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.toast.created` adalah toast sukses Create, yaitu
  `Success, position has been created.`
- `Fixture.globalSettingsPosition.captions.form.actions.submit` adalah tombol submit, yaitu `Submit`.
- `Fixture.globalSettingsPosition.captions.validation.maxLength` adalah pesan error batas panjang,
  yaitu `Max. 120 characters`. Yang diuji di spec ini adalah penerimaan pada batas bawah dan atas,
  sedangkan penolakan di atas batas diuji di spec 010.
- `Fixture.globalSettingsPosition.form.create.maxLengthAllowed` adalah string tepat 120 karakter yang
  seluruhnya valid. Yang invalid dalam PRD §9.9 hanya karakter di luar alfanumerik, spasi, dan tanda
  baca standar, termasuk emoji.
- `Fixture.globalSettingsPosition.form.create.singleCharName` adalah nama satu karakter untuk batas
  bawah non-empty, yaitu `A`.
- `Fixture.globalSettingsPosition.form.create.trimmedName` adalah nama hasil trim yang akan disimpan,
  yaitu `IT Manager 2`.
- `Fixture.globalSettingsPosition.form.create.paddedName` adalah nilai yang diketik di field,
  yaitu dua spasi di depan dan di belakang nama tersebut.
- Nama hasil trim `Fixture.globalSettingsPosition.form.create.trimmedName` harus dijamin belum dipakai
  di entitas uji, karena kalau sudah ada seluruh subbagian trim gagal karena duplikat, bukan karena
  trim.
- `Fixture.globalSettingsPosition.form.create.trimCollisionTarget` adalah nama yang sudah ada dan akan
  dipakai untuk menguji bahwa pengecekan duplikat juga melihat nilai hasil trim.
- Panjang string batas diukur ulang di spec dari isi field, bukan memakai angka yang ditulis di
  Prerequisites. Ini supaya test gagal kalau fixture memakai string yang panjangnya keliru, bukan
  kalau implementasinya salah.
- Ketiga subbagian dipecah terpisah karena masing-masing punya kondisi awal sendiri. Menggabungkan
  ketiganya membuat kegagalan trim menutupi kegagalan boundary, atau sebaliknya.

## Test Steps

### Batas bawah: satu karakter diterima

1. Klik tombol `[+ Position]` untuk membuka modal Create
2. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.singleCharName`
3. Verifikasi field Name berisi tepat satu karakter dan tidak kosong
4. Verifikasi tidak ada inline error yang muncul
5. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.submit`
6. Verifikasi toast sukses `Fixture.globalSettingsPosition.captions.toast.created` muncul
7. Verifikasi baris dengan nama satu karakter itu masuk ke tabel
8. Verifikasi kolom Name pada baris tersebut menampilkan tepat satu karakter, tidak lebih
9. Muat ulang halaman browser
10. Verifikasi baris satu karakter itu tetap ada setelah muat ulang

### Batas atas: tepat 120 karakter diterima

11. Klik tombol `[+ Position]` untuk membuka modal Create baru
12. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.maxLengthAllowed`
13. Verifikasi panjang isi field Name tepat 120 karakter sesuai hasil hitung ulang
14. Verifikasi field Name menampilkan seluruh 120 karakter tanpa terpotong
15. Verifikasi tidak ada inline error yang muncul
16. Verifikasi indikator hitung karakter tidak menunjukkan angka di atas 120
17. Klik tombol `[Submit]`
18. Verifikasi toast sukses muncul
19. Verifikasi baris dengan nama 120 karakter itu masuk ke tabel
20. Verifikasi kolom Name pada baris tersebut menampilkan seluruh 120 karakter tanpa terpotong atau
    diringkas
21. Muat ulang halaman browser
22. Verifikasi baris 120 karakter itu tetap ada setelah muat ulang
23. Verifikasi panjang nilai pada baris itu tetap 120 karakter setelah dibaca ulang dari server

### Spasi awal dan akhir di-trim

24. Klik tombol `[+ Position]` untuk membuka modal Create baru
25. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.paddedName`, yaitu nilai yang
    punya spasi di awal dan di akhir
26. Verifikasi field Name menampilkan nilai tersebut lengkap dengan spasi di kedua ujungnya
27. Verifikasi panjang isi field Name lebih besar daripada panjang nama hasil trim
28. Verifikasi tidak ada inline error yang muncul pada langkah ini
29. Klik tombol `[Submit]`
30. Verifikasi toast sukses muncul
31. Verifikasi baris baru masuk ke tabel
32. Verifikasi kolom Name pada baris tersebut menampilkan
    `Fixture.globalSettingsPosition.form.create.trimmedName` tanpa spasi di awal dan akhir
33. Verifikasi tidak ada spasi yang tersisa di kedua ujung nama yang tersimpan
34. Verifikasi spasi di tengah nama tetap dipertahankan, sehingga trim tidak menghapus seluruh spasi
35. Muat ulang halaman browser
36. Verifikasi nilai yang tersimpan tetap tanpa spasi di kedua ujung setelah dibaca dari server
37. Verifikasi trim terjadi di sisi server dan bukan hanya di tampilan tabel

### Trim membuat nama bertabrakan dengan nama yang sudah ada

38. Pastikan nama `Fixture.globalSettingsPosition.form.create.trimCollisionTarget` sudah ada di
    entitas uji
39. Klik tombol `[+ Position]` untuk membuka modal Create baru
40. Isi field Name dengan nilai yang punya spasi di awal dan akhir dari nama tersebut, memakai
    `Fixture.globalSettingsPosition.form.create.paddedName`
41. Tunggu jeda deteksi duplikat real-time
42. Verifikasi inline error duplikat muncul, sehingga pengecekan keunikan juga melihat nilai hasil
    trim
43. Verifikasi nama yang duplikat itu sendiri ada di tabel dan tidak ikut berubah
44. Verifikasi tidak ada baris baru yang dibuat
45. Verifikasi jumlah data Position tidak bertambah

### Nilai yang hanya spasi ditolak

46. Klik tombol `[+ Position]` untuk membuka modal Create baru
47. Isi field Name hanya dengan beberapa spasi tanpa karakter lain
48. Verifikasi tidak ada karakter selain spasi di dalam field Name
49. Klik tombol `[Submit]`
50. Verifikasi pesan error `Name must not be empty` muncul, karena setelah di-trim tidak ada sisa
    karakter
51. Verifikasi tidak ada toast sukses yang muncul
52. Verifikasi tidak ada baris yang masuk ke tabel
53. Verifikasi jumlah data Position tidak bertambah

## Notes

- Batas bawah dan batas atas diuji terpisah karena keduanya bisa salah secara terpisah.
  Batas atas bisa tertanam atribut `maxlength` yang terlalu kecil, sedangkan batas bawah bisa tertanam
  validasi required yang terlalu agresif.
- Panjang string diukur ulang dari isi field pada langkah 13 dan 23, bukan memakai angka dari
  Prerequisites. Kalau fixture-nya salah panjang, test harus gagal di sana dengan pesan yang jelas,
  bukan gagal diam-diam karena submit ditolak.
- Trim diuji bukan hanya pada nilai yang disimpan, tetapi juga pada interaksinya dengan pengecekan
  duplikat. Kalau trim hanya terjadi saat tampilan, nama yang berbeda spasi akan lolos membuat record
  duplikat yang berbeda casing dan spasi, dan itu tidak terlihat di tabel.
- Langkah 34 memeriksa spasi di tengah tetap ada. Trim yang salah bisa menghapus seluruh spasi dari
  nama, dan itu akan terlihat pada nama seperti `Warehouse Supervisor` yang kata katanya memang
  dipisahkan spasi.
- Subbagian nilai yang hanya spasi sengaja ditambahkan karena kasus ini tidak ada di TC sumber.
  Ini konsekuensi langsung dari aturan trim, yaitu spasi di-trim menjadi string kosong, dan kalau
  validasi required dijalankan sebelum trim, data spasi akan lolos membuat Position tanpa nama.
  Ditambahkan sebagai pengaman, bukan sebagai pengganti TC.
- Nama yang diuji diambil dari fixture supaya spec ini tidak menduplikasi string yang juga dipakai
  spec lain. Kalau nama hasil trim di sini sama dengan seed spec lain, subbagian trim akan gagal
  karena duplikat yang tidak ada hubungannya dengan trim.
- Persistensi setiap subbagian diperiksa dengan muat ulang halaman. Ini menjaga agar test tidak
  lulus karena state tabel di klien saja.
