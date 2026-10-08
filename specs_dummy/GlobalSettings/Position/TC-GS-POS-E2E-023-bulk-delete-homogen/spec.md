---
id: TC-GS-POS-E2E-023-bulk-delete-homogen
title: Bulk Delete homogen, pembatalan, dan collapse ke dialog single
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-04
  - TC-GS-POS-29
  - TC-GS-POS-243
coverage:
  web: automated
---

# Bulk Delete homogen, pembatalan, dan collapse ke dialog single

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user and role dengan huruf C, U, dan D. Kolom checkbox dan Bulk Action Bar
  hanya tampil bagi role yang memegang capability Delete.
- `Fixture.globalSettingsPosition.bulkDelete.uniformTargets` adalah dua Position bebas relasi yang
  menjadi target Bulk Delete homogen, yaitu `Junior Analyst` dan `Assistant Coordinator`. Keduanya
  dibuat oleh spec Create, bukan oleh spec ini.
- `Fixture.globalSettingsPosition.bulkDelete.singleSafeTarget` adalah satu Position bebas relasi untuk
  uji collapse ke dialog single.
- `Fixture.globalSettingsPosition.bulkDelete.cancelTargets` adalah dua Position bebas relasi untuk uji
  pembatalan dialog bulk.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.title` adalah title Dialog 4, yaitu
  `Delete Positions`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.bodyItems` adalah daftar bullet nama
  yang akan dihapus, satu bullet per Position terpilih.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.bodyQuestion` adalah kalimat penutup
  Dialog 4, yaitu `Are you sure you want to delete them? This action cannot be undone.`
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.cancel` adalah tombol batal,
  yaitu `Cancel`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.delete` adalah tombol
  konfirmasi, yaitu `Delete`.
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title` adalah title Dialog 1, yaitu
  `Delete Position`.
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.bodyQuestion` adalah kalimat penutup
  Dialog 1, yaitu `Are you sure you want to delete it? This action cannot be undone.`
- `Fixture.globalSettingsPosition.captions.toast.deleted` adalah toast sukses Delete, yaitu
  `Success, position has been deleted.`
- PRD §4.2d menetapkan pemetaan hasil evaluasi bulk ke dialog secara tegas. N lebih dari satu dan
  seluruhnya bebas relasi memakai Dialog 4, sedangkan N sama dengan satu selalu collapse ke Dialog 1
  maupun Dialog 2 dengan title singular dan kalimat `delete it?`. Dialog 3 dan Dialog 4 tidak pernah
  dipakai untuk N sama dengan satu.
- Kalimat penutup `delete them?` dan `delete it?` adalah pembeda paling tajam antara Dialog 4 dan
  Dialog 1. Keduanya dipakai pada area yang sama, yaitu konfirmasi penghapusan, jadi salah pilih
  dialog akan terlihat langsung dari kata ganti tersebut.
- Konvensi platform menetapkan bahwa aksi bulk yang sudah ter-commit membuat Bulk Action Bar langsung
  hilang dan seluruh seleksi di-reset ke nol, termasuk item yang di-skip. Sebaliknya, dialog yang
  dibatalkan tidak mengubah apa pun dan seleksi tidak di-reset.
- Jumlah entri log pada tiga surface dihitung di awal setiap subbagian supaya pembatalan dan Delete
  yang benar-benar jalan bisa dibedakan.

## Test Steps

### Bulk Delete homogen pada dua Position bebas relasi

1. Verifikasi tabel memuat
   `Fixture.globalSettingsPosition.bulkDelete.uniformTargets` pada halaman aktif
2. Verifikasi tidak ada Bulk Action Bar yang tampil pada kondisi awal
3. Catat jumlah total Position pada footer paginasi
4. Catat jumlah entri log pada tiga surface sebelum Delete
5. Centang checkbox pada baris pertama dari
   `Fixture.globalSettingsPosition.bulkDelete.uniformTargets`
6. Verifikasi Bulk Action Bar muncul
7. Centang checkbox pada baris kedua dari
   `Fixture.globalSettingsPosition.bulkDelete.uniformTargets`
8. Verifikasi counter pada bar menunjukkan jumlah dua
9. Klik tombol aksi massa pada bar
10. Verifikasi dialog yang tampil adalah Dialog 4 dengan title
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.title`
11. Verifikasi title memakai bentuk jamak, yaitu `Positions`, bukan `Position`
12. Verifikasi dialog memuat satu bullet untuk
    `Fixture.globalSettingsPosition.bulkDelete.uniformTargets`
13. Verifikasi dialog memuat satu bullet untuk
    `Fixture.globalSettingsPosition.bulkDelete.uniformTargets`
14. Verifikasi tidak ada bagian berlabel `The following are still in use and will be skipped:`, karena
    tidak ada item yang terblokir
15. Verifikasi dialog tidak memuat bagian `The following will be deleted:`, karena itu framing milik
    Dialog 3 untuk kasus campuran
16. Verifikasi body dialog memuat kalimat
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.bodyQuestion`
17. Verifikasi kalimat penutup memakai kata `them`, bukan `it`
18. Verifikasi tombol
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.cancel` dan tombol
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.delete` keduanya tampil
19. Verifikasi daftar nama ditampilkan penuh di dalam container yang bisa digulir, bukan diringkas
    menjadi angka
20. Klik tombol
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.delete`
21. Verifikasi toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` muncul
22. Verifikasi dialog tertutup
23. Verifikasi kedua baris pada
    `Fixture.globalSettingsPosition.bulkDelete.uniformTargets` tidak lagi ada di tabel
24. Verifikasi jumlah total Position pada footer paginasi berkurang dua
25. Verifikasi Bulk Action Bar langsung hilang setelah aksi ter-commit
26. Verifikasi seluruh checkbox baris kembali unchecked, termasuk kalau ada baris lain yang sebelumnya
    tercentang
27. Verifikasi jumlah entri log Changelog bertambah dua entri, satu untuk setiap item yang benar-benar
    terhapus
28. Verifikasi kedua entri log mencatat aksi `Delete` dengan Old Value masing-masing nama target
29. Verifikasi jumlah entri log Activity Log bertambah dua
30. Verifikasi jumlah entri System Log bertambah dua
31. Muat ulang halaman
32. Verifikasi kedua target tetap tidak ada setelah muat ulang

### Membatalkan dialog konfirmasi bulk

33. Verifikasi tabel memuat
   `Fixture.globalSettingsPosition.bulkDelete.cancelTargets` pada halaman aktif
34. Catat jumlah total Position
35. Catat jumlah entri log pada tiga surface sebelum pembatalan
36. Centang kedua baris pada
   `Fixture.globalSettingsPosition.bulkDelete.cancelTargets`
37. Verifikasi counter pada bar menunjukkan jumlah dua
38. Klik tombol aksi massa pada bar
39. Verifikasi dialog konfirmasi bulk tampil
40. Klik tombol
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.cancel`
41. Verifikasi dialog tertutup
42. Verifikasi tidak ada toast apa pun yang muncul
43. Verifikasi kedua baris pada
    `Fixture.globalSettingsPosition.bulkDelete.cancelTargets` tetap ada
44. Verifikasi jumlah total Position tidak berubah
45. Verifikasi jumlah entri log pada tiga surface tidak bertambah
46. Verifikasi Bulk Action Bar masih tampil setelah dialog dibatalkan
47. Verifikasi seleksi pada kedua baris masih tersimpan, karena dialog yang dibatalkan tidak boleh
    mereset seleksi
48. Verifikasi counter pada bar masih menunjukkan jumlah dua
49. Klik tombol aksi massa pada bar lagi
50. Verifikasi dialog konfirmasi yang tampil memuat bullet untuk kedua target
51. Klik tombol
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.delete`
52. Verifikasi toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` muncul
53. Verifikasi kedua target terhapus
54. Verifikasi Bulk Action Bar hilang dan seleksi ter-reset ke nol

### Bulk Action Bar dengan satu item collapse ke dialog single

55. Verifikasi baris `Fixture.globalSettingsPosition.bulkDelete.singleSafeTarget` ada di tabel
56. Catat jumlah entri log pada tiga surface sebelum subbagian ini
57. Centang checkbox pada baris
   `Fixture.globalSettingsPosition.bulkDelete.singleSafeTarget` saja
58. Verifikasi Bulk Action Bar muncul
59. Verifikasi counter pada bar memakai bentuk singular untuk satu baris terpilih
60. Klik tombol aksi massa pada bar
61. Verifikasi dialog yang tampil adalah Dialog 1 dengan title
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title`
62. Verifikasi title memakai bentuk singular, yaitu `Position`, bukan `Positions`
63. Verifikasi dialog memuat tepat satu bullet untuk
    `Fixture.globalSettingsPosition.bulkDelete.singleSafeTarget`
64. Verifikasi dialog tidak memuat bullet tambahan untuk item lain
65. Verifikasi dialog tidak memuat framing `The following will be deleted:`
66. Verifikasi body dialog memuat kalimat
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.bodyQuestion`
67. Verifikasi kalimat penutup memakai kata `it`, bukan `them`
68. Verifikasi dialog yang tampil identik dengan dialog hasil klik opsi `Delete` pada row action,
    sehingga tidak ada varian bulk yang bocor ke jalur ini
69. Verifikasi tombol konfirmasi memakai label `Delete`, bukan `Continue`, karena `Continue` milik
    Dialog 3 untuk kasus campuran
70. Klik tombol konfirmasi pada dialog
71. Verifikasi toast sukses
    `Fixture.globalSettingsPosition.captions.toast.deleted` muncul
72. Verifikasi baris `Fixture.globalSettingsPosition.bulkDelete.singleSafeTarget` tidak lagi ada
73. Verifikasi jumlah entri log bertambah satu, sama dengan jumlah item yang dihapus
74. Verifikasi jumlah entri log Activity Log dan System Log juga bertambah satu

## Notes

- Yang diuji di spec ini adalah Dialog 4 untuk N lebih dari satu dan Dialog 1 untuk N sama dengan satu.
  Dialog 3 dan Dialog 2 untuk jalur bulk diuji di spec 024.
- Langkah 17 dan langkah 67 memeriksa kata `them` versus `it`. Dua kata itu satu-satunya pembeda yang
  terlihat oleh user, dan salah pilih dialog akan lolos seluruh assertion lain kalau hanya judul dan
  jumlah bullet yang diperiksa.
- Langkah 14 dan langkah 15 memeriksa framing yang salah tidak ikut muncul. Dialog 4 boleh menampilkan
  daftar bullet langsung, bukan memakai heading kelompok seperti Dialog 3.
- Langkah 19 memeriksa daftar nama ditampilkan penuh. PRD §4.2d mewajibkan container scrollable dan
  melarang peringkasan menjadi angka, sebanyak apa pun jumlah item terpilih. Kalau jumlah diringkas
  jadi `2 positions`, user tidak tahu apa yang akan hilang.
- Langkah 25 sampai 26 dan langkah 46 sampai 47 memeriksa dua aturan selenium yang berbeda. Aksi yang
  ter-commit mereset seleksi ke nol, sedangkan dialog yang dibATALkan tidak mereset seleksi. Kalau
  keduanya mereset, user harus mengulang seleksi setelah salah membatalkan dialog.
- Subbagian ketiga membandingkan dialog dari Bulk Action Bar dengan dialog dari row action secara
  implisit lewat langkah 68. Keduanya harus identik, karena PRD menetapkan collapse ke dialog single
  dan bukan memakai varian bulk dengan N sama dengan satu.
- Target Delete di subbagian pertama juga dipakai spec 004 sebagai bukti dropdown, dan target di
  subbagian kedua dipakai spec 025. Karena itu semua subbagian memakai set target yang berbeda supaya
  spec-spec itu tidak saling</think> data.
- Pembuktian logging lengkap untuk bulk ada di spec 042 sesuai pola pointer maju pada sumber TC. Yang
  diperiksa di sini hanya jumlah entri per item yang benar-benar terhapus, karena itu bagian yang
  menentukan apakah batch salah menghitung.
