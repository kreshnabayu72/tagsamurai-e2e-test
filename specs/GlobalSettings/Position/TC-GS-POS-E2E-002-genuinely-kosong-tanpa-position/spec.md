---
id: TC-GS-POS-E2E-002-genuinely-kosong-tanpa-position
title: Empty state genuinely kosong pada entitas tanpa Position
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-18
coverage:
  web: automated
---

# Empty state genuinely kosong pada entitas tanpa Position

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- `Fixture.globalSettingsPosition.actors.totalControl` adalah akun penguji baseline.
- Spec ini memakai entitas uji kedua yang berbeda dari entitas pada spec 001 dan spec 003.
  `Fixture.globalSettingsPosition.actors.totalControl.emptyTenant` adalah akun Total Control pada
  entitas tersebut.
- Entitas kedua dibuat lewat Admin Console dengan field Position dikosongkan ketika membuat Default
  User. PRD §11 menegaskan modul Position tidak membuat record-nya sendiri saat entitas dibuat,
  sehingga tanpa field Position terisi, tabel Position entitas itu benar-benar tidak punya baris.
- `Fixture.globalSettingsPosition.positions.totalCount.emptyTenant` harus bernilai `0` untuk entitas
  kedua dan diverifikasi lewat seed sebelum spec berjalan. Kalau nilainya bukan nol, spec ini tidak
  sah karena bukan lagi genuinely kosong.
- `Fixture.globalSettingsPosition.captions.emptyTable.title` adalah judul empty state genuinely
  kosong, yaitu `No positions yet`.
- `Fixture.globalSettingsPosition.captions.emptyTable.description` adalah deskripsi empty state
  genuinely kosong, yaitu `Get started by creating your first position.`
- `Fixture.globalSettingsPosition.captions.emptyFiltered.title` adalah judul empty state hasil
  filter, yaitu `No results found`. Dipakai di sini sebagai pembeda agar spec ini tidak lolos kalau
  yang tampil adalah empty state yang salah.
- `Fixture.globalSettingsPosition.captions.emptyFiltered.description` adalah deskripsi empty state
  hasil filter, yaitu `Try adjusting your search or filter.`
- Entitas kedua tidak boleh menjalankan spec 046 lebih dulu, karena spec itu menjalankan Create
  berulang kali sampai `master_data_count_limit` tercapai dan akan menghilangkan kondisi genuinely
  kosong ini.

## Test Steps

### Membuka tab Position pada entitas kedua

1. Pastikan sedang berada di entitas kedua, bukan entitas pada spec 001
2. Buka `Global Settings > User`
3. Klik tab `Position`
4. Verifikasi tabel selesai memuat data tanpa berhenti pada kondisi error
5. Verifikasi tidak ada pesan `Unable to load this data.` dan tidak ada tombol `[Try Again]`,
   sehingga kegagalan baca data tidak salah dibaca sebagai tabel kosong
6. Verifikasi tidak ada skeleton loader yang masih tampil setelah data selesai dimuat

### Empty state genuinely kosong

7. Verifikasi empty state tampil di dalam area tabel
8. Verifikasi empty state memuat ilustrasi berukuran sekitar 100x100
9. Verifikasi judul yang tampil adalah `Fixture.globalSettingsPosition.captions.emptyTable.title`
10. Verifikasi deskripsi yang tampil adalah
    `Fixture.globalSettingsPosition.captions.emptyTable.description`
11. Verifikasi judul yang tampil bukan `Fixture.globalSettingsPosition.captions.emptyFiltered.title`
12. Verifikasi deskripsi yang tampil bukan
    `Fixture.globalSettingsPosition.captions.emptyFiltered.description`
13. Verifikasi empty state yang tampil berbeda dari empty state hasil pencarian pada spec 003, dan
    perbedaannya bukan hanya pada teks tetapi juga pada konteksnya

### Toolbar dan kontrol tetap utuh saat tabel kosong

14. Verifikasi tombol `[+ Position]` tetap tampil di toolbar dan dapat diklik
15. Verifikasi tombol `Search` tetap tampil di toolbar
16. Verifikasi tombol `Filter` tetap tampil di toolbar dan dapat diklik
17. Verifikasi tombol `Download` tetap tampil di toolbar
18. Verifikasi tombol `Changelog` tetap tampil di toolbar
19. Verifikasi tidak ada tombol aksi apa pun di dalam area empty state, misalnya tombol `Create
    Position` atau `Add Position` di bawah deskripsi
20. Verifikasi tidak ada tombol `Cancel` maupun `Clear` di dalam empty state
21. Verifikasi area empty state tidak memuat input pencarian pengganti

### Membuka modal Create dari kondisi kosong

22. Klik tombol `[+ Position]`
23. Verifikasi modal Create Position terbuka dengan judul `Create Position`
24. Verifikasi field `Position Name` dengan placeholder `Enter position name` tampil dan kosong
25. Verifikasi checkbox `Stay on this form after submitting` tampil dan tidak tercentang
26. Verifikasi tombol `[Clear Field]` dan `[Submit]` tampil di footer modal
27. Verifikasi modal Create tidak punya tombol `[Cancel]`, sesuai `prd-conventions.md` §24.1
28. Verifikasi kursor fokus berada di field `Position Name` saat modal terbuka, sesuai §4.5
29. Tutup modal Create lewat ikon `[✕]` tanpa mengisi apa pun
30. Verifikasi tidak ada dialog `Unsaved Changes` yang muncul, karena form tidak pernah dirty
31. Verifikasi kembali ke tab Position dan empty state `No positions yet` masih tampil
32. Verifikasi jumlah baris Position pada entitas kedua masih bernilai nol

## Notes

- Spec ini dipisah dari spec 001 dan spec 003 karena kondisi datanya berbeda secara fundamental.
  Spec 001 memakai entitas yang punya data seed, spec 003 memakai entitas yang punya data tapi tidak
  ada yang cocok dengan kata kunci. Spec ini memakai entitas yang benar-benar tidak punya data
  Position sama sekali. Menggabungkannya akan memaksa satu spec berjalan di dua entitas berbeda dan
  membuat kondisi kosongnya tidak terbukti.
- Entitas kedua ini bukan data sementara sekali pakai. Ia harus dipertahankan sepanjang siklus
  test karena dipakai ulang oleh spec 046 untuk menguji penambahan Position sampai menyentuh
  ceiling. Karena itu langkah 32 sengaja memverifikasi jumlah baris masih nol sebagai bukti tidak
  ada mutasi sampingan.
- Perbedaan empty state genuinely kosong dan empty state hasil filter adalah hal yang diuji di sini,
  bukan sekadar dokumen. Kalau keduanya sama, user tidak bisa membedakan apakah katalog Position
  masih kosong atau memang filter-nya yang tidak cocok.
- Verifikasi tidak adanya tombol di dalam empty state sengaja dilakukan dengan memeriksa beberapa
  nama tombol sekaligus, karena PRD §7 hanya menyebut ilustrasi, judul, dan deskripsi tanpa
  menyatakan eksplisit bahwa area itu tidak punya tombol.
- Jumlah baris pada entitas kedua sengaja diverifikasi ulang di langkah 32 supaya kebocoran data
  dari spec lain ke entitas ini langsung terlihat.
