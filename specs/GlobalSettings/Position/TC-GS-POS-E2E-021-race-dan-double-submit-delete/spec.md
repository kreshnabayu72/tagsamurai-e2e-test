---
id: TC-GS-POS-E2E-021-race-dan-double-submit-delete
title: Race Delete dan guard double-submit pada dialog konfirmasi
priority: High
caseType: Edge Case
status: draft
sourceTc:
  - TC-GS-POS-79
  - TC-GS-POS-80
  - TC-GS-POS-82
coverage:
  web: automated
---

# Race Delete dan guard double-submit pada dialog konfirmasi

## Prerequisites

- Spec ini butuh dua sesi browser yang hidup bersamaan. Keduanya disiapkan tim FE di environment
  otomasi, dan keduanya login sebagai Role Total Control memakai kredensial yang sama dari
  `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD`.
- Dua sesi dinotasikan sebagai `adminA` dan `adminB` supaya langkah bisa menyebut aktor dengan jelas.
- `Fixture.globalSettingsPosition.form.delete.concurrentTargetName` adalah Position target untuk
  seluruh subbagian di spec ini.
- `Fixture.globalSettingsPosition.helpers.assignPositionToSeedUser` adalah fixture FE yang meng-assign
  Position target ke user bawaan, dipakai untuk memicu race in-use.
- `Fixture.globalSettingsPosition.helpers.releaseSeedUserReference` adalah kebalikan dari fixture
  tersebut, dipakai untuk mengembalikan Prasyarat setelah race selesai.
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete` adalah tombol konfirmasi
  Dialog 1, yaitu `Delete`.
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title` adalah title Dialog 2, yaitu
  `Cannot Delete Data`.
- `Fixture.globalSettingsPosition.captions.toast.recordUnavailable` adalah toast netral untuk record yang
  sudah tidak ada, yaitu `This position is no longer available.`
- PRD §9.2 menetapkan dua fase cek untuk Delete. Cek awal menentukan dialog mana yang muncul dan boleh
  tidak atomik, sedangkan cek ulang atomik dijalankan bersama proses hapus di server per item. Kalau
  kondisi item berubah di antara cek awal dan Confirm, hasil final harus ikut kondisi terbaru.
- PRD §7.2 ayat 3 menetapkan bahwa error 404 menutup modal otomatis, me-refresh tabel, dan memunculkan
  toast netral. Spec ini mengikuti aturan itu. `TC-GS-POS-79` menuliskan conflict popup untuk kasus
  yang sama, dan perbedaan itu dicatat sebagai temuan di dokumen coverage, bukan diselesaikan dengan
  mengarang dialog tambahan di spec ini.
- PRD §9.4 ayat `Must NOT` melarang memproses submit kedua dari klik ganda. Karena itu double-submit di
  sini harus menghasilkan tepat satu eksekusi, bukan dua request yang salah satunya gagal.
- Jumlah entri log pada tiga surface dihitung di awal setiap subbagian supaya percobaan yang gagal
  tidak tertukar dengan mutasi yang berhasil.

## Test Steps

### Record dihapus aktor lain sebelum Confirm ditekan

1. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.concurrentTargetName` ada di tabel
2. Catat jumlah entri log pada tiga surface sebelum subbagian ini
3. Di sesi `adminB`, buka dialog konfirmasi Delete untuk baris tersebut
4. Di sesi `adminB`, klik tombol
   `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete`
5. Verifikasi toast sukses
   `Fixture.globalSettingsPosition.captions.toast.deleted` muncul di sesi `adminB`
6. Verifikasi baris tersebut tidak lagi ada di tabel pada sesi `adminB`
7. Di sesi `adminA`, yang masih memegang baris tersebut dari state lama, tekan tombol
   `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete`
8. Verifikasi modal pada sesi `adminA` tertutup otomatis
9. Verifikasi tabel pada sesi `adminA` ter-refresh dan baris tersebut hilang
10. Verifikasi toast netral `Fixture.globalSettingsPosition.captions.toast.recordUnavailable` muncul di
    sesi `adminA`
11. Verifikasi toast yang muncul di sesi `adminA` bukan toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted`
12. Verifikasi tidak ada dialog konfirmasi yang tampil di sesi `adminA`
13. Verifikasi jumlah entri log bertambah satu saja untuk seluruh subbagian ini, yaitu entri milik
    `adminB`, karena percobaan `adminA` tidak boleh menambah entri
14. Verifikasi jumlah total Position pada sesi `adminA` sama dengan jumlah pada sesi `adminB`
15. Muat ulang halaman pada kedua sesi
16. Verifikasi kedua sesi unanimously menampilkan state yang sama, yaitu baris tersebut tidak ada

### Status berubah tepat antara cek awal dan Confirm

17. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.concurrentTargetName` ada di tabel
18. Verifikasi Position tersebut belum direferensikan user mana pun
19. Catat jumlah entri log pada tiga surface sebelum subbagian ini
20. Di sesi `adminA`, buka dialog konfirmasi Delete untuk baris tersebut
21. Verifikasi dialog yang tampil adalah Dialog 1 konfirmasi, bukan Dialog 2 blokir, karena pada saat
    cek awal Position memang belum dipakai
22. Verifikasi jumlah entri log belum bertambah hanya dengan membuka dialog
23. Di sesi `adminB`, jalankan
    `Fixture.globalSettingsPosition.helpers.assignPositionToSeedUser` untuk Position tersebut
24. Verifikasi Position tersebut kini direferensikan user bawaan
25. Verifikasi dialog pada sesi `adminA` masih terbuka dan tidak berubah sendiri
26. Di sesi `adminA`, klik tombol
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete`
27. Verifikasi dialog yang tampil setelah itu adalah Dialog 2 dengan title
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title`
28. Verifikasi Dialog 2 memuat bullet
    `Fixture.globalSettingsPosition.form.delete.concurrentTargetName`
29. Verifikasi Dialog 2 tidak memakai Dialog 1, karena itu berarti server memakai kondisi basi dari
    cek awal
30. Verifikasi baris
    `Fixture.globalSettingsPosition.form.delete.concurrentTargetName` tetap ada di tabel
31. Verifikasi jumlah entri log pada tiga surface tidak bertambah
32. Verifikasi tidak ada toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` yang muncul
33. Klik tombol `OK` pada Dialog 2
34. Verifikasi dialog tertutup
35. Jalankan `Fixture.globalSettingsPosition.helpers.releaseSeedUserReference` supaya prasyarat subbagian
    berikutnya tetap terpenuhi
36. Verifikasi Position tersebut kembali tidak direferensikan

### Double-klik Delete hanya mengeksekusi satu kali

37. Verifikasi baris `Fixture.globalSettingsPosition.form.delete.concurrentTargetName` ada di tabel
38. Verifikasi Position tersebut tidak direferensikan user mana pun
39. Catat jumlah total Position sebelum subbagian ini
40. Catat jumlah entri log pada tiga surface sebelum subbagian ini
41. Klik ikon Elipsis `(⋯)` pada baris tersebut lalu opsi `Delete`
42. Verifikasi Dialog 1 tampil
43. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete` dua kali
    dengan cepat tanpa jeda berarti
44. Verifikasi tombol konfirmasi berubah menjadi keadaan disabled atau loading setelah klik pertama
45. Verifikasi hanya satu request delete yang terkirim ke server
46. Verifikasi tidak ada error yang muncul akibat request kedua
47. Verifikasi toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` muncul paling banyak satu kali
48. Verifikasi dialog tertutup
49. Verifikasi baris tersebut tidak lagi ada di tabel
50. Verifikasi jumlah total Position berkurang tepat satu
51. Verifikasi jumlah entri log Changelog bertambah tepat satu entri dengan aksi `Delete`
52. Verifikasi jumlah entri log Activity Log bertambah tepat satu
53. Verifikasi jumlah entri System Log bertambah tepat satu
54. Verifikasi tidak ada entri log kedua dengan Old Value
    `Fixture.globalSettingsPosition.form.delete.concurrentTargetName`
55. Muat ulang halaman
56. Verifikasi baris tersebut tetap tidak ada
57. Verifikasi jumlah entri log tidak bertambah setelah muat ulang

## Notes

- PRD §7.2 ayat 3 dan `TC-GS-POS-79` tidak mendeskripsikan hal yang sama dengan cara yang sama.
  PRD menetapkan modal tertutup otomatis, refresh tabel, dan toast netral untuk 404, sedangkan
  TC menyebut conflict popup. Spec ini mengikuti PRD karena PRD adalah sumber aturan perilaku, dan
  perbedaannya dicatat di dokumen coverage.
- Subbagian pertama memakai toast netral, bukan dialog, karena record-nya benar-benar sudah tidak ada.
  Kalau yang dimaksud adalah konflik versi, itu kasus 409 dan memang memakai dialog
  kontekstual. PRD membedakan keduanya, dan spec ini tidak mencampurkannya.
- Subbagian kedua menguji re-cek atomik, yaitu bagian yang paling mudah hilang kalau hanya ada cek awal.
  Kalau implementasi hanya mengecek sekali saat dialog dibuka, subbagian ini akan loloskan penghapusan
  yang seharusnya ditolak dan data yang sedang dipakai user akan hilang.
- Langkah 22 memastikan membuka dialog tidak punya efek samping. Kalau entri log bertambah hanya karena
  dialog dibuka, itu berarti pencatatan terjadi di tempat yang salah.
- Subbagian ketiga memeriksa tiga hal sekaligus. Guard double-submit bisa terlihat benar di UI karena
  tombolnya disabled, tapi tetap mengirim dua request kalau penagan-nya hanya kosmetik. Langkah 50 dan
  51 sampai 54 adalah pembuktiannya di sisi data.
- Jumlah entri log diperiksa di tiga surface pada subbagian ketiga karena logging per item adalah satu
  transaksi, dan kegagalan di salah satu surface akan terlihat sebagai selisih jumlah.
  tidak bisa diuji
  diuji dengan satu sesi karena tidak ada dua konteks yang benar-benar melihat state berbeda.
- `adminB` selalu menyelesaikan aksinya lebih dulu secara eksplisit, bukan mengandalkan kecepatan klik,
  supaya hasil test tidak bergantung pada timing mesin.
