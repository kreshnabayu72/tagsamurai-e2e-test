---
id: TC-GS-POS-E2E-006-actor-non-total-control-mengubah-data
title: Actor non-Total-Control menyelesaikan aksi mutasi sampai sukses
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-122
  - TC-GS-POS-123
coverage:
  web: automated
---

# Actor non-Total-Control menyelesaikan aksi mutasi sampai sukses

## Prerequisites

- Spec ini adalah pasangan wajib dari spec 005. Spec 005 hanya membuktikan kontrolnya tampil,
  sedangkan spec ini membuktikan aksi capability itu benar-benar berhasil sampai ada toast sukses
  dan data berubah. Menjalankan spec 005 tanpa spec ini meninggalkan celah yang disebut di
  TC-GS-POS-57, 58, dan 59.
- Login dilakukan sebagai akun bercapability khusus, bukan akun Total Control. Tanpa akun seperti
  ini, test tidak menguji apa pun, jadi keberadaan keempat akun pada tabel di bawah adalah syarat
  jalannya spec, bukan sesuatu yang diasumsikan sudah ada.
- `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD` hanya dipakai untuk menyiapkan data
  awal lewat Total Control. Semua mutasi yang diuji dilakukan oleh akun bercapability, bukan oleh
  akun admin.
- `Fixture.globalSettingsPosition.captions.toast` adalah pemformatan toast sukses yang dipakai modul,
  yaitu `Success, position has been created.`, `Success, position has been updated.`, dan
  `Success, position has been deleted.`
- `Fixture.globalSettingsPosition.captions.modal.create` dan `.edit` adalah judul modal Create dan
  Edit Position.
- `Fixture.globalSettingsPosition.seed.referenceUser.position` adalah user yang dipakai sebagai
  titik referensi di spec 007, dan di spec ini hanya dipastikan tidak ikut terpengaruh.

Role yang diuji:

| Role | Akun | Capability yang dimiliki | Aksi yang diuji |
|---|---|---|---|
| Create-Only | `Fixture.globalSettingsPosition.actors.createOnly` | Create | Create Position |
| Update-Only | `Fixture.globalSettingsPosition.actors.updateOnly` | Update | Edit Position |
| Delete-Only | `Fixture.globalSettingsPosition.actors.deleteOnly` | Delete | Delete Position |
| Capability Read-Only | `Fixture.globalSettingsPosition.actors.capabilityReadOnly` | Read | Tidak ada aksi mutasi |

## Test Steps

### Create-Only genuinely dapat membuat Position

1. Siapkan data awal dengan login sebagai Total Control dan buat Position
   `Fixture.globalSettingsPosition.seed.referenceUser.position` sebagai penanda bahwa data awal ada
2. Keluar dari akun Total Control
3. Login sebagai Role Create-Only
4. Verifikasi tab `Position` terbuka dan data awal terbaca
5. Klik tombol `[+ Position]`
6. Verifikasi modal Create Position terbuka
7. Isi field `Name` dengan nilai baru
   `Fixture.globalSettingsPosition.createOnly.newName`
8. Verifikasi nilai field `Name` terbaca sesuai yang diisi
9. Klik tombol `[Submit]`
10. Verifikasi toast sukses `Success, position has been created.` muncul
11. Verifikasi modal Create Position tertutup
12. Verifikasi baris dengan nilai `Fixture.globalSettingsPosition.createOnly.newName` muncul di
    tabel
13. Verifikasi baris tersebut dibaca dari server dengan memuat ulang halaman, sehingga ini bukan
    sekadar state lokal di tabel
14. Verifikasi Position yang dibuat pada langkah 1 tidak berubah

### Update-Only genuinely dapat mengubah Position

15. Siapkan Position dengan nama
    `Fixture.globalSettingsPosition.updateOnly.originalName` lewat akun Total Control
16. Keluar dari akun Total Control
17. Login sebagai Role Update-Only
18. Verifikasi baris `Fixture.globalSettingsPosition.updateOnly.originalName` terlihat di tabel
19. Klik ikon Elipsis `(⋯)` pada baris tersebut
20. Verifikasi opsi `Edit` tampil pada menu row action
21. Klik opsi `Edit`
22. Verifikasi modal Edit Position terbuka
23. Verifikasi field `Name` terisi nilai lama
    `Fixture.globalSettingsPosition.updateOnly.originalName`
24. Ubah field `Name` menjadi `Fixture.globalSettingsPosition.updateOnly.newName`
25. Klik tombol `[Save]`
26. Verifikasi toast sukses `Success, position has been updated.` muncul
27. Verifikasi modal Edit Position tertutup
28. Verifikasi baris menampilkan nama baru
    `Fixture.globalSettingsPosition.updateOnly.newName`
29. Verifikasi baris dengan nama lama
    `Fixture.globalSettingsPosition.updateOnly.originalName` tidak lagi ada
30. Verifikasi perubahan tetap ada setelah memuat ulang halaman
31. Verifikasi tidak ada Position lain yang ikut berubah namanya

### Update-Only tidak bisa Mutasi di luar capability-nya

32. Pastikan masih login sebagai Role Update-Only
33. Verifikasi tombol `[+ Position]` tidak tampil
34. Verifikasi tidak ada kolom Checkbox seleksi, sehingga Bulk Delete tidak bisa dijangkau
35. Verifikasi opsi `Delete` tidak ada pada menu row action

### Delete-Only genuinely dapat menghapus Position

36. Siapkan Position `Fixture.globalSettingsPosition.deleteOnly.targetName` lewat akun Total
    Control, dan pastikan Position itu tidak direferensikan user mana pun
37. Keluar dari akun Total Control
38. Login sebagai Role Delete-Only
39. Verifikasi baris `Fixture.globalSettingsPosition.deleteOnly.targetName` terlihat di tabel
40. Klik ikon Elipsis `(⋯)` pada baris tersebut
41. Verifikasi opsi `Edit` tidak tampil pada menu row action
42. Verifikasi opsi `Delete` tampil pada menu row action
43. Klik opsi `Delete`
44. Verifikasi popup konfirmasi Delete muncul
45. Verifikasi popup konfirmasi memuat nama Position yang akan dihapus, sehingga tidak ambigu
46. Klik tombol `[Delete]` pada popup konfirmasi
47. Verifikasi toast sukses `Success, position has been deleted.` muncul
48. Verifikasi popup konfirmasi tertutup
49. Verifikasi baris `Fixture.globalSettingsPosition.deleteOnly.targetName` tidak lagi ada di tabel
50. Verifikasi penghapusan tetap berlaku setelah memuat ulang halaman
51. Verifikasi Position lain tetap utuh setelah penghapusan

### Capability Read-Only tidak dapat Mutasi sama sekali

52. Keluar dari akun Role Delete-Only
53. Login sebagai Role Capability Read-Only
54. Verifikasi tombol `[+ Position]` tidak tampil
55. Verifikasi tidak ada kolom Checkbox seleksi
56. Verifikasi tidak ada ikon Elipsis `(⋯)` pada baris mana pun
57. Verifikasi seluruh data tetap dapat dibaca tanpa ada satu pun jalur mutasi yang bisa dijangkau
    dari UI

## Notes

- Spec ini sengaja memuat langkah "muat ulang halaman" setelah tiap mutasi. Tanpa itu, baris baru atau
  perubahan nama masih mungkin hanya berasal dari state lokal tabel, dan test akan lulus meskipun
  server tidak pernah menyimpan perubahan.
- Delete-Only memakai menu row action, bukan checkbox, karena langkah ini harus membuktikan capability
  Delete bekerja lewat jalur yang berbeda dari bulk delete di spec 007.
- Subbagian Update-Only diberi langkah negatif tersendiri karena TC-GS-POS-123 hanya membuktikan
  capability Update bekerja, dan tidak membuktikan capability lain tersembunyi. Spec 005 sudah
  memeriksa visibilitas, tetapi pemeriksaan itu hanya pada tampilan awal. Di sini pemeriksaan
  dilakukan pada akun yang sama yang baru saja melakukan mutasi, sehingga juga menutup kemungkinan
  kontrol muncul setelah aksi.
- Syarat bahwa Position target Delete tidak direferensikan user ditegaskan di Prerequisite, bukan
  hanya di langkah. Kalau ternyata direferensikan, server menolak penghapusan dan toast sukses tidak
  pernah muncul, sehingga kegagalan test tidak dapat dibedakan antara bug permission dan referensi data.
- Akun Total Control hanya dipakai menyiapkan dan membaca ulang data, tidak pernah melakukan mutasi
  yang diuji. Kalau admin yang performing mutasinya, spec ini akan lulus tanpa pernah menguji
  capability-nya sama sekali.
