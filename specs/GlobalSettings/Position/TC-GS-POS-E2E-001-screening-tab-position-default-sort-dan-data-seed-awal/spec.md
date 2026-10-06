---
id: TC-GS-POS-E2E-001-screening-tab-position-default-sort-dan-data-seed-awal
title: Screening tab Position, default sort, dan data seed awal
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-09
  - TC-GS-POS-15
  - TC-GS-POS-17
coverage:
  web: automated
---

# Screening tab Position, default sort, dan data seed awal

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`, tidak ditulis di spec ini.
- `Fixture.globalSettingsPosition.actors.totalControl` adalah akun penguji baseline untuk seluruh
  alur CRUD dan Table Rules.
- User berada di `Global Settings > User`, di tab `User List`.
- Entitas uji adalah entitas aktif tempat Position disimpan. Position selalu ter-scope ke entitas
  aktif, jadi tabel ini tidak pernah menampilkan data master entitas lain (PRD `position.md` §9.11).
- `Fixture.globalSettingsPosition.positions.seed.financeManager` adalah Position hasil data seed
  awal yang permanen di entitas ini, dan dipakai juga sebagai salah satu fixture "in use" di spec
  020, 023, dan 024. Record ini tidak boleh dihapus selama siklus test.
- `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` adalah Position seed kedua yang
  juga sedang dipakai oleh `Fixture.globalSettingsPosition.seedUsers.hrBusinessPartner`.
- `Fixture.globalSettingsPosition.positions.population` adalah daftar 10 nama Position variasi yang
  menjadi isi tabel tab ini. Urutannya harus berisi nama dengan awalan huruf berbeda supaya
  pengurutan alfabetis bisa dibuktikan, dan nama dengan huruf kapital serta huruf kecil supaya
  pengurutan case-insensitive bisa dibuktikan.
- `Fixture.globalSettingsPosition.data.sortProbe` adalah satu nama Position yang sengaja ditempatkan
  supaya urutannya berbeda bila pengurutan tidak case-insensitive, misalnya `IT manager` berdampingan
  dengan `IT Manager` dan `IT Operations Lead`.
- `Fixture.globalSettingsPosition.captions.tabs` adalah label keempat sub-tab pada halaman User.
- `Fixture.globalSettingsPosition.captions.tableTools` adalah label kelima tombol pada TableTools
  toolbar, sesuai urutan kiri ke kanan yang dipakai PRD `position.md` §4.2.
- `Fixture.globalSettingsPosition.captions.columns.positionList` adalah label kolom data tabel
  T-POS-01, urutannya `Name` lalu `Last Updated`.
- `Fixture.globalSettingsPosition.captions.columns.actionsHeader` adalah label kolom `Actions`.
- `Fixture.globalSettingsPosition.captions.pagination.pageSizes` adalah daftar pilihan page size yang
  diharapkan, yaitu `10`, `25`, `50`, `100`.
- `Fixture.globalSettingsPosition.pagination.defaultPageSize` adalah nilai page size default, yaitu
  `10` (PRD `position.md` §5).
- Navigasi dan toolbar yang dibutuhkan sudah punya selector `aria-label` permanen. Kalau belum ada,
  minta tim FE menambahkannya; jangan pakai xpath atau `nth-child`
  (`docs/e2e-conventions.md` bagian 9).

## Test Steps

### Struktur halaman dan sub-tab

1. Klik tab `Position` pada sub-tab bar halaman User
2. Verifikasi breadcrumb yang tampil adalah `User`
3. Verifikasi sub-tab bar menampilkan keempat sub-tab `User List`, `Position`, `Division`, dan
   `Custom Field`
4. Verifikasi tab `Position` sedang aktif, dan bukan `User List`
5. Verifikasi TabTools Toolbar berada di sisi kanan SectionCard, bukan di sisi kiri
6. Verifikasi urutan tombol pada toolbar dari kiri ke kanan adalah `Search`, `Filter`, `Download`,
   `Changelog`, lalu `[+ Position]`
7. Verifikasi tombol `[+ Position]` berada paling kanan pada toolbar
8. Verifikasi tidak ada tombol lain di luar kelima tombol tersebut pada toolbar
9. Verifikasi Filter Panel dalam keadaan tertutup pada tampilan awal, sesuai §4.2 yang menyebutnya
   `collapsible, hidden by default`
10. Verifikasi tidak ada Bulk Action Bar yang tampil pada kondisi awal, karena belum ada baris
    yang dicentang
11. Verifikasi tidak ada dialog atau popover yang terbuka pada kondisi awal

### Struktur tabel T-POS-01

12. Verifikasi header tabel menampilkan kolom data `Name` lalu `Last Updated`, sesuai urutan
    PRD `position.md` §4.2a
13. Verifikasi kolom `Actions` tampil sebagai kolom paling kanan tabel
14. Verifikasi header kolom `Name` dapat diklik untuk menyortir
15. Verifikasi header kolom `Last Updated` dapat diklik untuk menyortir
16. Verifikasi header kolom `Actions` tidak dapat dipakai untuk menyortir
17. Verifikasi kolom Checkbox seleksi baris tampil di sisi kiri tabel, sebagai kolom tersemat
18. Verifikasi tidak ada kolom `In Use` dan tidak ada kolom `Modified By` pada tabel ini, sesuai
    §4.4 poin 4 yang menyatakan keduanya memang tidak ada pada T-POS-01
19. Verifikasi tidak ada kolom `Total Users` pada tabel ini

### Pagination pada kondisi awal

20. Verifikasi footer tabel menampilkan kontrol pagination beserta navigasi ke halaman sebelumnya dan
    berikutnya
21. Verifikasi page size yang terpilih adalah
    `Fixture.globalSettingsPosition.pagination.defaultPageSize`
22. Verifikasi pilihan page size pada dropdown sesuai
    `Fixture.globalSettingsPosition.captions.pagination.pageSizes`
23. Verifikasi jumlah baris yang tampil di halaman pertama tidak melebihi page size default
24. Verifikasi tampilan tabel berada dalam kondisi Desktop, yaitu lebar viewport di atas 1024px,
    sehingga tabel tampil penuh dan bukan sebagai card list (PRD `position.md` §4.5)

### Default sort Name A-Z

25. Pastikan tidak ada sort atau filter yang sedang aktif, yaitu tombol `[+ Position]` belum pernah
    diklik dan tabel baru dimuat
26. Verifikasi urutan baris pada tabel terurut alfabetis A-Z berdasarkan kolom `Name`
27. Verifikasi pengurutan mengabaikan besar-kecil huruf, sehingga `IT manager` berada bersebelahan
    dengan `IT Manager` dan bukan terpisah di akhir atau awal daftar
28. Verifikasi pengurutan bersifat stabil terhadap nilai huruf besar dan huruf kecil pada awalan
    nama yang sama
29. Verifikasi tidak ada indikator sort aktif pada header kolom `Name`, karena pengurutan ini adalah
    default dan belum dipilih pengguna secara manual
30. Verifikasi header kolom `Last Updated` juga tidak menampilkan indikator sort aktif
31. Verifikasi mengurutkan ulang kolom `Name` secara manual mengembalikan ke urutan yang sama,
    sehingga urutan bawaan konsisten dengan hasil pengurutan manual

### Data seed awal tampil sebagai record biasa

32. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.financeManager` tampil di tabel
    bersama baris Position lainnya
33. Verifikasi baris tersebut tampil sebagai record biasa dan bukan sebagai baris specially marked
    atau baris yang punya badge atau ikon tambahan
34. Verifikasi nama yang tampil persis sama dengan nama yang diketik admin saat membuat entitas
35. Verifikasi tabel tidak menampilkan empty state, baik `No positions yet` maupun `No results found`,
    karena sudah ada data seed
36. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` juga tampil
    sebagai record biasa
37. Verifikasi tidak ada tombol atau aksi khusus pada baris data seed yang tidak ada pada baris
    Position biasa
38. Verifikasi baris data seed dapat memakai seluruh kolom yang sama dengan baris lain, yaitu `Name`
    dan `Last Updated`

## Notes

- Kolom Checkbox dan kolom `Actions` tidak dihitung sebagai kolom data pada §4.2a karena keduanya
  kolom sistem, selalu tersemat, dan tidak bisa di-unpin. Verifikasi pada langkah 17 dan 13
  sengaja memisahkannya dari daftar kolom data pada langkah 12.
- Tidak ada elemen yang punya state Disabled di modul ini. Modul ini murni binary Show/Hidden
  (§4.8), jadi di spec ini tidak ada satu pun langkah yang mengharapkan tombol tampil tapi nonaktif.
- Baris data seed awal adalah target sah untuk Edit, tidak seperti asumsi umum bahwa data seed itu
  terkunci. §9.2 menyatakan seluruh record termasuk data seed awal bisa di-Edit dan di-Delete seperti
  record lain. Yang tidak boleh terjadi di spec ini justru sebaliknya: baris seed harus tampil
  sepenuhnya normal, bukan tersembunyi atau terkunci.
- Nama `Finance Manager` pada tabel harus sama persis dengan yang diketik admin. PRD §11
  menegaskan modul Position tidak mendefinisikan nama seed itu sendiri dan tidak menjamin seed
  selalu ada, jadi spec ini tidak boleh mengarang nama seed literal. Nama diambil dari fixture
  karena berbeda antar entitas.
- Verifikasi emptiness pada langkah 35 memakai dua copy sekaligus. `No positions yet` dan
  `No results found` memang berbeda konteks (§7.1), dan pada kondisi ini keduanya salah.
- Pengurutan default ini perlu dibuktikan case-insensitive, bukan hanya alfabetis. Pasangan data pada
  langkah 27 memakai `IT manager` dan `IT Manager`; tanpa pasangan itu, pengurutan
  berbasis kode ASCII akan lolos dan test tetap hijau.
