---
id: TC-GS-POS-E2E-019-delete-position-terakhir
title: Delete pada satu-satunya Position yang tersisa
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-24
coverage:
  web: automated
---

# Delete pada satu-satunya Position yang tersisa

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user and role dengan huruf C, U, dan D.
- Spec ini memakai tenant terpisah yang hanya berisi satu Position. Setup tenant itu disiapkan oleh tim
  FE di environment otomasi dan ditandai lewat
  `Fixture.globalSettingsPosition.actors.totalControl.emptyTenant`, supaya tidak-accident menguji
  tenant utama yang sudah ada datanya.
- `Fixture.globalSettingsPosition.form.delete.solePositionName` adalah nama satu-satunya Position di
  tenant tersebut. Position ini tidak direferensikan user mana pun.
- `Fixture.globalSettingsPosition.captions.emptyTable.title` adalah title empty state tabel, yaitu
  `No positions yet`.
- `Fixture.globalSettingsPosition.captions.emptyTable.description` adalah description empty state,
  yaitu `Get started by creating your first position.`
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title` adalah title Dialog 1, yaitu
  `Delete Position`.
- `Fixture.globalSettingsPosition.captions.toast.deleted` adalah toast sukses Delete, yaitu
  `Success, position has been deleted.`
- `Fixture.globalSettingsPosition.positions.totalCount.emptyTenant` adalah total Position yang
  diharapkan setelah penghapusan, yaitu `0`.
- PRD §10 dan §9.2 tidak menetapkan guard last remaining. Jedanya sengaja tidak mengarang aturan
  tersebut, jadi Delete terhadap satu-satunya record harus diizinkan.
- PRD §7.1 menetapkan dua copywriting empty state yang berbeda. Tabel yang benar-benar kosong memakai
  `No positions yet` dengan description `Get started by creating your first position.`, sedangkan
  hasil pencarian yang tidak cocok memakai `No results found`. Spec ini memeriksa yang pertama, karena
  tabelnya kosong tanpa filter apa pun.
- Empty state ini juga yang membedakan penghapusan terakhir dari sekadar tabel yang terfilter.
  Kalau tabel kosong karena ada filter, jumlah total Position di server tidak benar-benar nol.
- Jumlah entri log pada tiga surface dihitung di awal supaya penghapusan terakhir bisa dibedakan dari
  penghapusan biasa.

## Test Steps

1. Verifikasi tenant aktif adalah tenant yang ditandai
   `Fixture.globalSettingsPosition.actors.totalControl.emptyTenant`
2. Verifikasi jumlah total Position pada footer paginasi bernilai `1`
3. Verifikasi tabel hanya berisi satu baris, yaitu
   `Fixture.globalSettingsPosition.form.delete.solePositionName`
4. Verifikasi tidak ada baris lain, karena ini prasyarat yang membuat skenario ini berarti
5. Verifikasi baris tersebut tidak sedang diseleksi, sehingga tidak ada Bulk Action Bar terbuka
6. Catat jumlah entri log pada tiga surface sebelum Delete
7. Klik ikon Elipsis `(⋯)` pada baris
   `Fixture.globalSettingsPosition.form.delete.solePositionName`
8. Verifikasi opsi `Edit` dan opsi `Delete` tetap tampil pada record terakhir, jadi tidak ada guard
   yang menyembunyikan aksi karena hanya ada satu baris
9. Klik opsi `Delete`
10. Verifikasi Dialog 1 tampil dengan title
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title`
11. Verifikasi dialog tidak menampilkan peringatan tambahan apa pun tentang jumlah data tersisa
12. Verifikasi body dialog memuat bullet
    `Fixture.globalSettingsPosition.form.delete.solePositionName`
13. Verifikasi tombol konfirmasi tetap dalam keadaan aktif, bukan disabled
14. Klik tombol `Delete` pada dialog
15. Verifikasi toast sukses `Fixture.globalSettingsPosition.captions.toast.deleted` muncul
16. Verifikasi dialog tertutup
17. Verifikasi tabel benar-benar kosong tanpa satu pun baris data
18. Verifikasi empty state yang tampil adalah genuinely empty, yaitu title
    `Fixture.globalSettingsPosition.captions.emptyTable.title`
19. Verifikasi description empty state adalah
    `Fixture.globalSettingsPosition.captions.emptyTable.description`
20. Verifikasi empty state tidak memakai title
    `Fixture.globalSettingsPosition.captions.emptyFiltered.title`, karena itu state berbeda untuk
    hasil filter yang tidak cocok
21. Verifikasi tidak ada Bulk Action Bar yang tersisa di layar
22. Verifikasi jumlah total Position pada footer paginasi bernilai
    `Fixture.globalSettingsPosition.positions.totalCount.emptyTenant`
23. Verifikasi jumlah entri log Changelog bertambah satu entri dengan aksi `Delete` dan Old Value
    `Fixture.globalSettingsPosition.form.delete.solePositionName`
24. Verifikasi jumlah entri log Activity Log bertambah satu
25. Verifikasi jumlah entri System Log bertambah satu
26. Verifikasi toolbar tetap berfungsi, khususnya tombol `+ Position` masih tampil dan aktif, karena
    tenant yang kosong masih harus bisa diisi ulang
27. Muat ulang halaman
28. Verifikasi tabel tetap genuinely empty setelah muat ulang, sehingga jumlah nol benar-benar
    persists dan bukan hanya hasil render
29. Verifikasi jumlah total Position tetap
    `Fixture.globalSettingsPosition.positions.totalCount.emptyTenant`
30. Klik tombol `+ Position`
31. Verifikasi modal Create Position terbuka dengan field Name kosong, sehingga tenant kosong memang
    bisa diisi lagi dan tidak terkunci oleh penghapusan terakhir
32. Tutup modal Create Position memakai tombol `[Clear Field]`
33. Verifikasi tidak ada dialog Unsaved Changes yang muncul, karena tidak ada isian yang dimodifikasi
34. Verifikasi tidak ada entri log baru dari pembukaan dan penutupan modal Create

## Notes

- Yang diuji di sini adalah ketiadaan guard last remaining, bukan défa happy path. Kalau produk
  memutuskan menambah guard tersebut, PRD §10 dan §9.2 harus berubah lebih dulu, dan spec ini
  ikut berubah setelahnya.
- Langkah 18 sampai 20 memeriksa genuinely empty dan bukan filtered empty. Dua state itu punya
  copywriting berbeda di PRD §7.1, jadi keberadaannya di UI adalah pembuktian bahwa tabel benar-benar
  tidak punya data.
- Langkah 22 memeriksa total di server, bukan hanya tampilan tabel. Tabel yang terlihat kosong masih
  bisa menyembunyikan data kalau total salah hitung.
- Langkah 27 sampai 29 memuat muat ulang supaya penghapusan terakhir tidak lolos hanya karena state
  klien masih memegang record lama.
- Langkah 30 sampai 33 sengaja diikutkan karena ada risiko nyata bahwa penghapusan terakhir
  meninggalkan tenant dalam keadaan terkunci. Kalau itu terjadi, user tidak punya jalan keluar lagi
  selain menghubungi admin, dan itu bukan perilaku yang diizinkan PRD.
- Tenant terpisah dipakai karena spec ini menghapus seluruh isi tenant. Memakai tenant utama akan
  menghancurkan data yang jadi prasyarat dozens spec lain.
