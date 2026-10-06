---
id: TC-GS-POS-E2E-017-edit-bersamaan-dan-double-submit
title: Edit bersamaan oleh dua aktor dan double-submit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-77
  - TC-GS-POS-78
coverage:
  web: automated
---

# Edit bersamaan oleh dua aktor dan double-submit

## Prerequisites

- Spec ini butuh dua sesi browser yang hidup bersamaan. Keduanya disiapkan tim FE di environment
  otomasi, dan keduanya login sebagai Role Total Control memakai kredensial yang sama dari
  `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD`.
- Dua sesi dinotasikan sebagai `adminA` dan `adminB` supaya langkah bisa menyebut aktor dengan jelas.
  `adminB` yang selalu menang adalah pilihan yang disengaja, bukan asumsi soal siapa yang lebih cepat.
- `Fixture.globalSettingsPosition.form.edit.concurrencyTargetName` adalah Position target untuk uji
  Edit bersamaan, yaitu `Data Entry Clerk`.
- `Fixture.globalSettingsPosition.form.edit.adminANewName` adalah nama baru yang diketik `adminA`,
  yaitu `Data Entry Executive`.
- `Fixture.globalSettingsPosition.form.edit.adminBNewName` adalah nama baru yang diketik `adminB`,
  yaitu `Data Entry Officer`.
- `Fixture.globalSettingsPosition.form.edit.doubleSubmitName` adalah nama hasil akhir setelah
  double-klik Save, dipakai subbagian kedua.
- `Fixture.globalSettingsPosition.captions.toast.updated` adalah toast sukses Edit, yaitu
  `Success, position has been updated.`
- `Fixture.globalSettingsPosition.captions.validation.duplicate` adalah pesan error duplikat, yaitu
  `Name already exists`.
- PRD §9.6 menetapkan Edit Position bersifat idempotent dan tidak menetapkan aturan optimistic
  locking maupun versi record. Karena itu spec ini tidak mengarang pesan konflik seperti
  `Record has been modified by another user`. Yang diuji adalah akibat yang benar-benar
  ditetapkan PRD, yaitu nilai akhir yang tersimpan.
- Aturan-Edit no-op berlaku di sini juga. `adminA` mengirim request dengan nilai basi, dan kalau
  server ternyata mendeteksi tidak ada perubahan relatif nilai saat itu, hasilnya boleh jadi toast
  netral dan bukan toast sukses. Keduanya diizinkan dan keduanya diperiksa.
- Urutan eksekusi `adminB` lebih dulu dijamin oleh spec, bukan hopes-and-pray pada kecepatan klik.
  `adminB` menyelesaikan simulasinya sampai toast sukses terlihat sebelum `adminA` menekan Save.
- Jumlah entri log dihitung pada akhir setiap subbagian untuk memastikan tidak ada mutasi yang
  tertulis di log tanpa benar-benar mengubah data, atau sebaliknya.
- Dua subbagian dipecah karena dua-duanya memakai record target yang sama dan saling bisa
  memengaruhi bila tidak dipisahkan.

## Test Steps

### Dua aktor mengubah record yang sama, adminB menang

1. Verifikasi baris `Fixture.globalSettingsPosition.form.edit.concurrencyTargetName` ada di tabel
2. Catat nilai awal baris tersebut
3. Catat jumlah entri log pada tiga surface sebelum Edit bersamaan
4. Di sesi `adminA`, buka baris tersebut lewat ikon Elipsis lalu opsi `Edit`
5. Di sesi `adminB`, buka baris yang sama lewat ikon Elipsis lalu opsi `Edit`
6. Verifikasi kedua sesi menampilkan modal Edit dengan nilai lama yang sama di field Name
7. Verifikasi kedua form Edit terbuka secara independen, yaitu menutup yang satu tidak menutup yang
   lain
8. Di sesi `adminB`, ganti field Name dengan
   `Fixture.globalSettingsPosition.form.edit.adminBNewName`
9. Di sesi `adminB`, klik tombol `[Save]`
10. Verifikasi toast sukses Edit muncul di sesi `adminB`
11. Verifikasi modal Edit tertutup di sesi `adminB`
12. Verifikasi baris target kini menampilkan
    `Fixture.globalSettingsPosition.form.edit.adminBNewName`
13. Di sesi `adminA`, pastikan field Name masih berisi nilai lama, karena `adminA` belum menyentuh
    field apa pun
14. Di sesi `adminA`, ganti field Name dengan
    `Fixture.globalSettingsPosition.form.edit.adminANewName`
15. Di sesi `adminA`, klik tombol `[Save]`
16. Verifikasi hasil di sesi `adminA` termasuk salah satu dari dua bentuk yang diizinkan, yaitu toast
    sukses Edit atau toast netral `No changes to save.`
17. Verifikasi tidak ada toast error yang muncul di sesi `adminA`, khususnya tidak ada
    `Name already exists` dan tidak ada pesan konflik versi yang tidak ada di PRD
18. Verifikasi modal Edit tertutup di sesi `adminA` dalam kedua kemungkinan hasil
19. Verifikasi nilai akhir yang tersimpan di server adalah
    `Fixture.globalSettingsPosition.form.edit.adminANewName`, sehingga request terakhir menang
20. Verifikasi nilai `Fixture.globalSettingsPosition.form.edit.adminBNewName` tidak lagi ada
21. Muat ulang halaman pada kedua sesi
22. Verifikasi kedua sesi menampilkan nilai akhir yang sama, yaitu
    `Fixture.globalSettingsPosition.form.edit.adminANewName`
23. Verifikasi jumlah baris dengan nama yang berasal dari kedua aktor tetap satu, tidak ada record
    baru yang tercipta dari Edit
24. Verifikasi jumlah total data tidak bertambah
25. Verifikasi jumlah entri log Changelog bertambah sesuai jumlah mutasi yang benar-benar mengubah
    nilai, yaitu satu entri untuk `adminB` danpaling banyak satu entri tambahan untuk `adminA` bila hasilnya
    toast sukses
26. Verifikasi entri log untuk `adminA` mencatat Old Value nama hasil `adminB` dan New Value nama hasil
    `adminA`, bukan nama lama sebagai Old Value
27. Verifikasi tidak ada entri log dengan Old Value dan New Value yang sama
28. Verifikasi jumlah entri log Activity Log sinkron dengan Changelog
29. Verifikasi tidak ada entri System Log baru, sesuai aturan katalog yang tidak melekat pada user

### Double-klik Save tidak menimpa nilai dua kali

30. Verifikasi baris `Fixture.globalSettingsPosition.form.edit.concurrencyTargetName` ada di tabel
31. Catat jumlah entri log pada tiga surface sebelum double-submit
32. Klik ikon Elipsis `(⋯)` pada baris tersebut
33. Klik opsi `Edit`
34. Verifikasi modal Edit terbuka dengan nilai lama terisi
35. Hapus seluruh isi field Name, lalu isi dengan
    `Fixture.globalSettingsPosition.form.edit.doubleSubmitName`
36. Klik tombol `[Save]` dua kali dengan cepat tanpa jeda berarti
37. Verifikasi hanya satu request update yang terkirim ke server
38. Verifikasi tidak ada toast error yang muncul akibat request kedua
39. Verifikasi toast sukses Edit muncul paling banyak satu kali
40. Verifikasi modal Edit tertutup
41. Verifikasi baris target kini menampilkan
    `Fixture.globalSettingsPosition.form.edit.doubleSubmitName`
42. Verifikasi jumlah entri log Changelog bertambah paling banyak satu
43. Verifikasi tidak ada dua entri log dengan New Value yang sama dari satu aksi
44. Muat ulang halaman browser
45. Verifikasi nilai yang tersimpan tetap
    `Fixture.globalSettingsPosition.form.edit.doubleSubmitName`
46. Verifikasi jumlah entri log tidak bertambah setelah muat ulang

### Dua editor membuka form yang sama dan satu menutup tanpa menyimpan

47. Verifikasi baris `Fixture.globalSettingsPosition.form.edit.concurrencyTargetName` ada di tabel
48. Di sesi `adminA`, buka modal Edit untuk baris tersebut
49. Di sesi `adminB`, buka modal Edit untuk baris yang sama
50. Di sesi `adminB`, ubah field Name menjadi nilai valid baru lalu klik `[Save]`
51. Verifikasi toast sukses Edit muncul di sesi `adminB`
52. Di sesi `adminA`, tutup modal Edit memakai tombol `Esc`
53. Verifikasi dialog Unsaved Changes muncul di sesi `adminA`, karena field Name di sana sudah
    dimodifikasi
54. Klik tombol `[Leave]`
55. Verifikasi modal Edit tertutup di sesi `adminA`
56. Verifikasi data yang tersimpan tetap hasil `adminB`, sehingga meninggalkan form tidak menimpa nilai
57. Verifikasi tidak ada toast sukses yang muncul di sesi `adminA`
58. Verifikasi jumlah entri log tidak bertambah dari tindakan di sesi `adminA`
59. Muat ulang halaman
60. Verifikasi nilai akhir tetap hasil `adminB`

## Notes

- PRD §9.6 tidak menetapkan optimistic locking untuk Edit Position. Test ini sengaja tidak
  mengarang pesan konflik yang tidak ada di PRD, dan hanya memeriksa akibat yang benar-benar
  ditetapkan, yaitu request terakhir menang.
- Langkah 16 memperbolehkan dua hasil yang berbeda. Tanpa itu, test akan gagal pada implementasi yang
  benar secara tidak sengaja, dan yang benar secara tidak sengaja akan dianggap satu-satunya jawaban
  yang benar.
- Langkah 17 memeriksa tidak ada pesan konflik yang tidak ada di PRD. Ini yang membedakan
  last-write-wins yang disengaja dari proteksi versi yang lupa direview.
- Langkah 26 memeriksa Old Value entri log `adminA` adalah nilai hasil `adminB`. Kalau Old Value-nya
  masih nama lama, berarti log ditulis dari state form klien, bukan dari nilai yang benar-benar
  ada di server, dan log itu tidak bisa dipakai untuk audit.
- Jumlah entri log diperiksa longgar pada langkah 25, yaitu satu atau dua tergantung apakah Edit
  `adminA` Counts sebagai perubahan nyata. Mengakuinya longgar disengaja karena itu mengikuti aturan
  no-op, bukan karena tidak tahu.
- Urutan `adminB` lebih dulu dijamin eksplisit pada langkah 9 sampai 12. Ini menghindari hasil yang
  bergantung pada kecepatan klik, yang akan membuat test tidak bisa diulang.
- Subbagian pertama memakai dua sesi browser sungguhan, bukan satu sesi dengan dua tab. Dua tab dari
  profil yang sama berbagi local storage dan bisa menyembunyikan masalah yang benar-benar terjadi
  pada dua orang yang berbeda.
- Subbagian ketiga ditambahkan karena menutup form dengan `[Leave]` adalah jalur yang bisa menimpa
  nilai tanpa mengirim request, dan jalur itu tidak diuji oleh dua subbagian pertama.
- Kedua nilai nama untuk kedua aktor diambil dari fixture karena keduanya juga dipakai sebagai target
  validasi di spec lain. Menyalinnya secara literal berisiko membuat dua sumber kebenaran untuk data
  yang sama.
