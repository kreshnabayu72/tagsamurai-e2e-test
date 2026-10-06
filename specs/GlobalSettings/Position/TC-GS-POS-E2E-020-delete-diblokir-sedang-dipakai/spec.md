---
id: TC-GS-POS-E2E-020-delete-diblokir-sedang-dipakai
title: Delete diblokir karena Position sedang dipakai user
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-96
coverage:
  web: automated
---

# Delete diblokir karena Position sedang dipakai user

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user and role dengan huruf C, U, dan D. Guard in-use bukan soal hak akses,
  jadi Aktor ini harus tetap mendapat blokir.
- `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` adalah Position `HR Business
  Partner` yang sudah direferensikan user bawaan `Rina Wijaya` sejak sebelum siklus test dimulai.
  Relasi itu dibuat permanen oleh tim FE di environment otomasi dan hanya dibaca spec ini.
- `Fixture.globalSettingsPosition.seedUsers.hrBusinessPartner` adalah user pemegang relasi tersebut,
  dipakai untuk memastikan jumlah user yang dilaporkan dialog benar dan bukan angka placeholder.
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title` adalah title Dialog 2, yaitu
  `Cannot Delete Data`.
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.body` adalah body Dialog 2, yaitu
  `These positions are still in use. Remove the references before deleting.`
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok` adalah tombol tunggal Dialog
  2, yaitu `OK`.
- PRD §4.8 menyatakan modul ini murni binary Show atau Hidden tanpa state Disabled. Opsi `Delete` pada
  baris yang sedang dipakai harus tetap tampil dan aktif, karena guard-nya adalah business rule yang
  dievaluasi saat klik, bukan kondisi visibilitas.
- PRD §4.2d Dialog 2 menetapkan satu dialog blokir yang dipakai baris single maupun bulk yang seluruhnya
  terblokir, dengan pembeda hanya jumlah bullet. Dialog itu punya satu tombol `OK`, bukan pasangan
  Cancel dan Delete.
- PRD §6 menetapkan pesan in-use tanpa awalan jumlah user. Yang ada di copy aplikasi adalah
  `These positions are still in use. Remove the references before deleting.`, dan angka jumlah user
  muncul di kontrak API, bukan di teks dialog.
- PRD §9.3 menyatakan guard in-use tetap divalidasi di server secara independen dari UI. Karena itu
  spec ini memeriksa efeknya pada data dan log, bukan hanya pada tampilan dialog.
- Jumlah entri log pada tiga surface dihitung di awal supaya blokir dapat dibedakan dari Delete yang
  hanya gagal di lapisan UI.

## Test Steps

### Opsi Delete tetap tampil dan aktif pada record yang dipakai

1. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` ada di tabel
2. Verifikasi baris tersebut tidak sedang diseleksi lewat checkbox
3. Klik ikon Elipsis `(⋯)` pada baris
   `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
4. Verifikasi opsi `Delete` tetap tampil pada baris ini
5. Verifikasi opsi `Delete` berada dalam keadaan aktif, bukan disabled dan bukan disamarkan
6. Verifikasi tidak ada badge atau ikon pengunci pada baris yang menandakan record sedang dipakai
7. Tutup menu Elipsis
8. Catat jumlah entri log pada tiga surface sebelum attempting Delete
9. Klik ikon Elipsis `(⋯)` pada baris
   `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
10. Klik opsi `Delete`
11. Verifikasi dialog yang tampil adalah Dialog 2 dengan title
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title`, bukan Dialog 1 konfirmasi
12. Verifikasi dialog tidak menampilkan kalimat konfirmasi
    `Are you sure you want to delete it? This action cannot be undone.`, karena dialog konfirmasi
    berarti sistem menganggap data aman dihapus
13. Verifikasi body dialog memuat bullet
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` dengan penanda still in use
14. Verifikasi body dialog memuat kalimat
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.body`
15. Verifikasi dialog hanya punya satu tombol, yaitu
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok`
16. Verifikasi dialog tidak punya tombol `Delete`, karena tidak ada yang boleh dieksekusi
17. Verifikasi dialog tidak punya tombol `Cancel`, karena blokir bukan pilihan yang bisa dibatalkan
18. Verifikasi tidak ada toast yang muncul saat dialog tampil
19. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok`
20. Verifikasi dialog tertutup
21. Verifikasi tidak ada toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` muncul
22. Verifikasi tidak ada toast error maupun toast netral yang muncul setelah dialog ditutup
23. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` tetap ada di
    tabel
24. Verifikasi jumlah total Position tidak berubah
25. Verifikasi jumlah entri log pada tiga surface tidak bertambah, sehingga percobaan yang diblokir
    tidak dicatat sebagai mutasi
26. Muat ulang halaman
27. Verifikasi baris tersebut tetap ada setelah muat ulang

### Jumlah bullet dan isi dialog sesuai data sebenarnya

28. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.multiUserName` ada di tabel
29. Verifikasi Position tersebut direferensikan oleh lebih dari satu user
30. Catat jumlah entri log pada tiga surface sebelum attempting Delete
31. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.positions.seed.multiUserName`
32. Klik opsi `Delete`
33. Verifikasi Dialog 2 tampil dengan title
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title`
34. Verifikasi dialog hanya memuat satu bullet untuk satu nama Position, bukan satu bullet per user
35. Verifikasi bullet memuat `Fixture.globalSettingsPosition.positions.seed.multiUserName`
36. Verifikasi kalimat penutup tetap
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.body` tanpa awalan jumlah user
37. Verifikasi dialog tidak memuat angka jumlah user di badan dialog
38. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok`
39. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.multiUserName` tetap ada
40. Verifikasi jumlah entri log tidak bertambah

### Lepas relasi, Delete succeeds, lalu pulihkan relasi

41. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` masih ada
42. Verifikasi user
    `Fixture.globalSettingsPosition.seedUsers.hrBusinessPartner` masih memegang Position tersebut
43. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
44. Klik opsi `Delete`
45. Verifikasi Dialog 2 tampil, yaitu guard masih aktif karena relasi belum dilepas
46. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok`
47. Verifikasi baris masih ada
48. Verifikasi langkah berikutnya dijalankan lewat fixture FE yang melepas relasi user tersebut, yaitu
    `Fixture.globalSettingsPosition.helpers.releaseSeedUserReference`
49. Verifikasi user tersebut sudah tidak lagi memegang Position
50. Klik ikon Elipsis `(⋯)` pada baris
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
51. Klik opsi `Delete`
52. Verifikasi dialog yang tampil sekarang adalah Dialog 1 konfirmasi, bukan Dialog 2
53. Verifikasi Dialog 1 memuat bullet
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
54. Verifikasi tombol konfirmasi `Delete` pada Dialog 1 aktif
55. Klik tombol `Cancel` pada Dialog 1 supaya spec ini tidak meninggalkan seed dalam keadaan terhapus
56. Verifikasi dialog tertutup
57. Verifikasi baris tetap ada
58. Kembalikan relasi user tersebut melalui
    `Fixture.globalSettingsPosition.helpers.restoreSeedUserReference` supaya prasyarat spec lain yang
    memakai Position ini sebagai target in-use tetap terpenuhi
59. Verifikasi relasi user sudah pulih dan Position kembali berstatus dipakai

## Notes

- Yang diuji di sini adalah dua hal sekaligus. Pertama, guard in-use benar-benar mencegah penghapusan.
  Kedua, guard itu tetap berupa aturan saat klik, bukan kondisi disabled pada opsi `Delete`, karena
  PRD §4.8 melarang state Disabled di modul ini.
- Langkah 12 memeriksa Dialog 1 tidak muncul. Kalau dialog konfirmasi muncul lebih dulu lalu ditolak
  setelahnya, itu berarti guard dijalankan di server tanpa memberi umpan balik yang benar, dan user
  sudah sempat percaya delete akan berjalan.
- Langkah 17 memeriksa tidak ada tombol `Cancel`. Dialog blokir punya aturan Single Dismiss Rule, yaitu
  hanya `OK`. Adanya `Cancel` di sini berarti aturan dismiss tidak dijalankan.
- Langkah 13 sampai 14 dan langkah 36 sampai 37 sengaja mengulang copy yang sama pada dua record dengan
  jumlah user berbeda. Kalau copy-nya ikut bergantung pada jumlah user, dialog single akan berubah bentuk
  tergantung data, dan itu tidak ada di PRD.
- Subbagian kedua dipakai karena bug yang paling sering pada guard in-use adalah dialog yang salah benar
  pada kasus satu user tapi salah kalau ada beberapa user.
- Subbagian ketiga membuktikan guard bersifat dinamis, yaitu mengikuti kondisi aktual data dan bukan
  cache dari state sebelum. Langkah 52 sampai 53 adalah pembuktiannya.
- Langkah 58 sengaja mengembalikan relasi user, karena `HR Business Partner` juga dipakai spec 007 dan
  spec 024 sebagai target in-use. Kalau spec ini meninggalkan relasi user dalam keadaan lepas, dua spec itu
  akan gagal karena alasan yang salah.
- Jumlah user yang dilaporkan tidak diperiksa terhadap angka tertentu. Yang diperiksa adalah bentuk
  dialog, karena PRD tidak menetapkan angka tersebut di copy.
