---
id: TC-GS-POS-E2E-018-delete-single-berhasil-dan-batal
title: Delete single berhasil, pembatalan, dan kesetaraan row action
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-03
  - TC-GS-POS-21
  - TC-GS-POS-23
coverage:
  web: automated
---

# Delete single berhasil, pembatalan, dan kesetaraan row action

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user and role dengan huruf C, U, dan D.
- `Fixture.globalSettingsPosition.form.delete.targetName` adalah Position bebas relasi yang menjadi
  target Delete single, yaitu `Temporary Staff`. Position ini dibuat oleh spec Create, bukan oleh
  spec ini, supaya spec ini tidak menguji mutasi yang belum ada saat test mulai.
- `Fixture.globalSettingsPosition.positions.seed.financeManager` adalah Position seed
  `Finance Manager`. Sesuai PRD §9.2, seluruh record termasuk data seed awal bisa di-Edit dan di-Delete
  seperti record lain, tanpa flag khusus.
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title` adalah title Dialog 1, yaitu
  `Delete Position`.
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.body` adalah body Dialog 1, yaitu
  `Are you sure you want to delete it? This action cannot be undone.`
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.cancel` adalah tombol batal,
  yaitu `Cancel`.
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete` adalah tombol konfirmasi,
  yaitu `Delete`.
- `Fixture.globalSettingsPosition.captions.toast.deleted` adalah toast sukses Delete, yaitu
  `Success, position has been deleted.`
- `Fixture.globalSettingsPosition.captions.rowActions.edit` dan
  `Fixture.globalSettingsPosition.captions.rowActions.delete` adalah dua opsi di dalam ikon Elipsis.
- PRD §4.2d Dialog 1 menetapkan satu dialog konfirmasi untuk Delete single dengan bullet nama
  Position dan kalimat singular `delete it?`. Kalimat jamak `delete them?` hanya dipakai Dialog 4
  untuk bulk homogen, jadi kemunculannya di spec ini berarti dialog yang salah.
- PRD §7.2 ayat 3 menetapkan bahwa error 404 menutup modal otomatis, me-refresh tabel, dan memunculkan
  toast netral. Jalur itu tidak boleh muncul pada Delete yang sukses, dan dipakai sebagai pembeda
  antara data yang benar-benar terhapus dan data yang hanya hilang dari tampilan.
- Jumlah entri log pada tiga surface dihitung ulang di awal setiap subbagian supaya tidak ada mutasi
  dari subbagian sebelumnya yang ikut terhitung.
- Subbagian dipisah karena subbagian pertama benar-benar menghapus target, sedangkan dua subbagian
  berikutnya tidak boleh mengubah data apa pun.

## Test Steps

### Delete single pada Position bebas relasi

1. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.targetName` ada di tabel
2. Verifikasi baris tersebut tidak sedang diseleksi lewat checkbox, sehingga tidak ada Bulk Action
   Bar yang terbuka
3. Catat jumlah total Position pada footer paginasi
4. Catat jumlah entri log pada tiga surface sebelum Delete
5. Klik ikon Elipsis `(⋯)` pada baris
   `Fixture.globalSettingsPosition.form.delete.targetName`
6. Verifikasi menu Elipsis memuat opsi `Edit` dan opsi `Delete`
7. Klik opsi `Fixture.globalSettingsPosition.captions.rowActions.delete`
8. Verifikasi Dialog 1 tampil dengan title
   `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title`
9. Verifikasi body dialog memuat bullet berisi
   `Fixture.globalSettingsPosition.form.delete.targetName`
10. Verifikasi body dialog memuat kalimat
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.body`
11. Verifikasi dialog tidak memuat kalimat `delete them?`, karena itu kalimat Dialog 4
12. Verifikasi tombol `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.cancel` dan
    tombol `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete` keduanya
    tampil
13. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete`
14. Verifikasi toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` muncul
15. Verifikasi dialog konfirmasi tertutup
16. Verifikasi toast netral `This position is no longer available.` tidak muncul, karena record
    benar-benar terhapus dan bukan hilang karena error
17. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.targetName` tidak lagi ada di tabel
18. Verifikasi jumlah total Position pada footer paginasi berkurang satu
19. Verifikasi posisi baris berikutnya naik ke tempat baris target berada, bukan menyisakan baris kosong
20. Verifikasi jumlah entri log Changelog bertambah satu entri dengan aksi `Delete`
21. Verifikasi entri log tersebut mencatat field `Name` dengan Old Value
    `Fixture.globalSettingsPosition.form.delete.targetName` dan New Value berupa tanda pisah
22. Verifikasi jumlah entri log Activity Log bertambah satu, sinkron dengan Changelog
23. Verifikasi jumlah entri System Log bertambah satu pada Detail User aktor, sinkron dengan Changelog
24. Muat ulang halaman
25. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.targetName` tetap tidak ada setelah
    muat ulang, sehingga penghapusan benar-benar persists

### Membatalkan dialog konfirmasi Delete

26. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.cancelTargetName` ada di tabel
27. Catat jumlah entri log pada tiga surface sebelum pembatalan
28. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.form.delete.cancelTargetName`
29. Klik opsi `Fixture.globalSettingsPosition.captions.rowActions.delete`
30. Verifikasi Dialog 1 tampil untuk baris tersebut
31. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.cancel`
32. Verifikasi dialog tertutup
33. Verifikasi tidak ada toast apa pun yang muncul, baik sukses maupun error
34. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.cancelTargetName` tetap ada
35. Verifikasi isinya tidak berubah
36. Verifikasi jumlah total Position tidak berubah
37. Verifikasi jumlah entri log pada tiga surface tidak bertambah, sehingga pembatalan tidak
    dicatat sebagai mutasi
38. Buka kembali dialog konfirmasi untuk baris yang sama
39. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete`
40. Verifikasi toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` muncul
41. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.cancelTargetName` hilang dari tabel
42. Verifikasi jumlah entri log bertambah satu, membuktikan pembatalan sebelumnya memang tidak
    mengirim request apa pun

### Row action seed identik dengan row biasa

43. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.financeManager` ada di tabel
44. Verifikasi baris seed tersebut dan satu baris biasa tampil pada tabel yang sama tanpa perlakuan
    visual yang berbeda
45. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.positions.seed.financeManager`
46. Verifikasi menu Elipsis memuat opsi `Edit` dan opsi `Delete`, sama seperti baris biasa
47. Verifikasi opsi `Edit` dan opsi `Delete` tidak tampil dalam keadaan disabled, ter-disable, atau
    disamarkan
48. Verifikasi tidak ada tooltip permission yang muncul saat menu dibuka pada baris seed
49. Tutup menu Elipsis tanpa memilih apa pun
50. Klik ikon Elipsis `(⋯)` pada baris biasa
51. Verifikasi himpunan opsi pada menu Elipsis baris biasa identik dengan baris seed, yaitu
    `Edit` dan `Delete` tanpa opsi tambahan
52. Verifikasi urutan opsi pada kedua menu juga identik
53. Tutup menu Elipsis
54. Buka Dialog konfirmasi untuk baris
    `Fixture.globalSettingsPosition.positions.seed.financeManager`
55. Verifikasi dialog yang tampil adalah Dialog 1, bukan Dialog blokir, karena
    `Fixture.globalSettingsPosition.positions.seed.financeManager` pada prinsipnya boleh dihapus
56. Verifikasi dialog menampilkan bullet nama seed tersebut
57. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.cancel`
58. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.financeManager` tetap ada, supaya
    spec ini tidak bergantung pada urutan eksekusi terhadap spec lain yang memakai seed yang sama

## Notes

- Subbagian pertama memakai `Fixture.globalSettingsPosition.form.delete.targetName`, sedangkan
  subbagian kedua memakai `Fixture.globalSettingsPosition.form.delete.cancelTargetName`. Keduanya
  sengaja dipisah supaya pembatalan tidak bergantung pada record yang sudah dihapus oleh subbagian
  sebelumnya.
- Langkah 11 memeriksa kalimat jamak secara eksplisit karena Dialog 1 dan Dialog 4 punya kalimat yang
  hanya dibedakan oleh `it` dan `them`. Kalau kalimat yang muncul `them`, berarti dialog yang dipakai
  adalah Dialog 4 dan itu bug di sisi dialog, bukan beda yang bisa diabaikan.
- Langkah 20 sampai 23 memeriksa tiga surface sekaligus. Changelog yang benar saja tidak cukup,
  karena logging tiga surface adalah satu kontrak dan bisa gagal separuh.
- Langkah 24 dan 25 sengaja memuat muat ulang. Delete yang hanya hilang dari tampilan tapi masih ada
  di server akan lolos seluruh langkah sebelumnya kecuali langkah ini.
- Subbagian ketiga menguji kesetaraan akses, bukan kemampuan menghapus seed. Dialog konfirmasi
  sengaja dibatalkan pada langkah 57 supaya seed `Finance Manager` tidak hilang di spec ini, karena
  seed itu juga dipakai spec 007 dan spec 024 sebagai target in-use.
- Verifikasi `disabled` pada langkah 47 penting karena PRD §4.8 menyatakan modul ini murni binary
  Show atau Hidden. Opsi yang tampil tapi disabled melanggar aturan itu, dan kondisi itu tidak bisa
  ditangkap hanya dari isi menu.
