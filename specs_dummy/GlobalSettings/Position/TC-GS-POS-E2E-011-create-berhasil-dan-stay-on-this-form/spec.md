---
id: TC-GS-POS-E2E-011-create-berhasil-dan-stay-on-this-form
title: Create berhasil, populasi data, dan Stay on this form
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-01
  - TC-GS-POS-16
  - TC-GS-POS-45
  - TC-GS-POS-100
coverage:
  web: automated
---

# Create berhasil, populasi data, dan Stay on this form

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.toast.created` adalah toast sukses Create, yaitu
  `Success, position has been created.`
- `Fixture.globalSettingsPosition.captions.modal.create.title` adalah judul modal, yaitu
  `Create Position`.
- `Fixture.globalSettingsPosition.captions.form.checkbox.stayOnForm` adalah label checkbox, yaitu
  `Stay on this form after submitting`.
- `Fixture.globalSettingsPosition.captions.form.actions.submit` adalah tombol submit, yaitu `Submit`.
- `Fixture.globalSettingsPosition.form.create.happyPathName` adalah nama untuk skenario dasar, yaitu
  `IT Manager`.
- `Fixture.globalSettingsPosition.form.create.populationNames` adalah daftar 19 nama valid untuk
  populasi, sesuai urutan yang ditetapkan `TC-GS-POS-16`. Daftarnya diambil dari fixture, bukan
  ditulis di spec, supaya nama yang jadi seed suite ini tidak ditulis ulang di dua tempat.
- Beberapa nama dalam daftar populasi punya peran tambahan bagi spec lain, yaitu
  `Customer Relations Officer` menjadi target validasi Edit di spec 014 sampai 016, dan
  `Data Entry Clerk` menjadi target double-submit serta Edit bersamaan di spec 013 dan spec 017.
  Spec ini tidak mengubahnya, hanya memastikan seluruhnya benar-benar MADE.
- Nama-nama pada daftar populasi harus dijamin belum dipakai di entitas uji. Kalau ada yang bentrok,
  seluruh subbagian populasi gagal karena alasan yang sama sekali tidak terkait dengan checkbox
  Stay on this form.
- `Fixture.globalSettingsPosition.captions.pagination.total` adalah pola jumlah total data yang
  ditampilkan, dipakai untuk memverifikasi pertambahan jumlah data tanpa menghitung baris satu per
  satu.
- Verifikasi persistensi dilakukan dengan memuat ulang halaman, bukan dengan menutup dan membuka kembali
  modal, supaya yang terbukti benar-benar tersimpan di server.

## Test Steps

### Create happy path

1. Klik tombol `[+ Position]` untuk membuka modal Create
2. Verifikasi modal dengan judul `Fixture.globalSettingsPosition.captions.modal.create.title` terbuka
3. Verifikasi field Name kosong dan sudah mendapat fokus keyboard
4. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.happyPathName`
5. Verifikasi field Name menampilkan nilai tersebut tanpa pembatasan tambahan
6. Verifikasi tidak ada inline error yang muncul pada langkah ini
7. Verifikasi checkbox `Fixture.globalSettingsPosition.captions.form.checkbox.stayOnForm` dalam
   keadaan tidak tercentang
8. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.submit`
9. Verifikasi toast sukses `Fixture.globalSettingsPosition.captions.toast.created` muncul
10. Verifikasi modal Create tertutup
11. Verifikasi baris `Fixture.globalSettingsPosition.form.create.happyPathName` masuk ke tabel
12. Verifikasi kolom Name pada baris tersebut menampilkan nilai yang persis sama dengan yang diisi
13. Verifikasi jumlah total data bertambah satu dibanding sebelum submit

### Data persist setelah halaman dimuat ulang

14. Catat jumlah total data Position sebelum memuat ulang
15. Muat ulang halaman browser
16. Verifikasi tab Position terbuka kembali setelah muat ulang
17. Verifikasi baris `Fixture.globalSettingsPosition.form.create.happyPathName` masih ada di tabel
18. Verifikasi jumlah total data sama dengan yang dicatat pada langkah 14
19. Verifikasi tabel kembali ke urutan sort default, bukan ke posisi hasil pencarian
20. Verifikasi baris tersebut muncul di halaman pertama tanpa perlu mencari

### Stay on this form diaktifkan: form di-reset dan tetap terbuka

21. Klik tombol `[+ Position]` untuk membuka modal Create baru
22. Verifikasi field Name kosong
23. Verifikasi checkbox Stay on this form dalam keadaan tidak tercentang
24. Isi field Name dengan nilai valid dari
    `Fixture.globalSettingsPosition.form.create.populationNames` pada elemen pertama
25. Centang checkbox `Fixture.globalSettingsPosition.captions.form.checkbox.stayOnForm`
26. Verifikasi checkbox menampilkan keadaan tercentang
27. Klik tombol `[Submit]`
28. Verifikasi toast sukses muncul
29. Verifikasi modal Create tidak tertutup, justru tetap terbuka
30. Verifikasi field Name dikosongkan kembali ke kondisi kosong
31. Verifikasi checkbox Stay on this form tetap tercentang, supaya submit berikutnya juga bertahan
32. Verifikasi fokus kembali berada di field Name yang kosong, siap untuk nama berikutnya
33. Verifikasi field Name tidak lagi menampilkan inline error dari nilai sebelumnya
34. Verifikasi baris dengan nama yang baru saja disubmit masuk ke tabel di belakang modal
35. Verifikasi jumlah total data bertambah satu

### Populasi 19 nama lewat Stay on this form

36. Pastikan modal Create dari subbagian sebelumnya masih terbuka dengan checkbox Stay on this form
    tercentang
37. Isi field Name dengan elemen kedua dari
    `Fixture.globalSettingsPosition.form.create.populationNames`, lalu klik `[Submit]`
38. Verifikasi toast sukses muncul
39. Verifikasi modal tetap terbuka dan field Name kembali kosong
40. Verifikasi baris dengan nama tersebut sudah ada di tabel
41. Ulangi langkah 37 sampai 40 untuk elemen ketiga sampai kedelapan dari daftar populasi
42. Verifikasi seluruh nama yang sudah disubmit pada langkah 37 sampai 41 ada di tabel
43. Verifikasi jumlah total data bertambah sesuai jumlah nama yang sudah disubmit
44. Isi field Name dengan elemen kesembilan dari daftar populasi
45. Lepas centang checkbox `Fixture.globalSettingsPosition.captions.form.checkbox.stayOnForm`
46. Verifikasi checkbox menampilkan keadaan tidak tercentang
47. Klik tombol `[Submit]`
48. Verifikasi toast sukses muncul
49. Verifikasi modal Create tertutup, karena checkbox sudah tidak tercentang lagi
50. Verifikasi checkbox tidak memengaruhi apa pun selain apakah modal tetap terbuka
51. Verifikasi baris dengan nama pada langkah 44 ada di tabel
52. Verifikasi seluruh 19 nama dari `Fixture.globalSettingsPosition.form.create.populationNames`
    ada di tabel tanpa duplikat
53. Verifikasi jumlah total data bertambah tepat sembilan belas, bukan lebih atau kurang
54. Verifikasi tidak ada nama yang gagal dibuat di tengah proses tanpa terlihat, yaitu tidak ada nama
    yang hilang dari daftar
55. Muat ulang halaman browser
56. Verifikasi seluruh 19 nama tetap ada setelah muat ulang, sehingga benar-benar tersimpan di
    server dan bukan hanya di state tabel
57. Verifikasi jumlah total data tetap sama setelah muat ulang

## Notes

- Skenario Stay on this form dipecah dua subbagian. Subbagian pertama menguji perilaku satu siklus,
  yaitu apa yang terjadi pada field, checkbox, dan fokus setelah submit. Subbagian kedua menguji
  bahwa perilaku itu berulang sampai sembilan belas nama. Menggabungkannya membuat kegagalan pada
  submit yang keempat sulit dipisahkan dari perilaku satu siklus yang salah.
- Langkah 31 memeriksa checkbox tetap tercentang setelah submit. Ini yang membuat populasi berjalan
  tanpa harus mencentang ulang di tiap iterasi, dan kalau checkbox ikut ter-reset, populasi berhenti
  di submit kedua.
- Langkah 34 memeriksa baris baru masuk ke tabel selagi modal masih terbuka. Ini bukti bahwa
  Stay on this form tidak menahan render tabel di belakang modal.
- Langkah 50 memeriksa checkbox tidak memengaruhi apa pun selainKeberadaan modal yang tetap terbuka.
  Ini yang membuktikan `[Submit]` di subbagian kedua tetap bekerja normal setelah checkbox dilepas.
- Langkah 52 memeriksa tidak ada duplikat di daftar. Kalau ada nama yang salah ketik dan tercipta dua
  kali tanpa terlihat, langkah 52 akan menangkapnya, sedangkan sekadar menghitung jumlah baris tidak.
- Langkah 54 memeriksa seluruh nama ada, bukan cuma jumlahnya. Jumlah yang benar bisa terjadi ketika
  satu nama gagal dan nama lain muncul dua kali, jadi kedua pemeriksaan ini tidak saling
  menggantikan.
- Daftar populasi diambil dari fixture karena enam nama di dalamnya juga dipakai sebagai seed oleh
  spec lain. Menyalinnya secara literal ke spec ini berisiko membuat dua sumber kebenaran untuk
  data yang sama.
- `TC-GS-POS-16` menyebut nama pertama `Marketing Lead`, sedangkan `TC-GS-POS-01` memakai
  `IT Manager`. Keduanya tidak dipertentangkan karena ini entitas uji yang sama dan keduanya harus
  bisa hidup berdampingan; daftar populasi diatur agar tidak mengandung `IT Manager`.
- Urutan nama pada daftar populasi tidak diuji sebagai bagian dari scenario ini. Urutan default
  ascending diuji di spec 001, bukan di sini, supaya kegagalan urutan tidak disalahartikan sebagai
  kegagalan Stay on this form.
