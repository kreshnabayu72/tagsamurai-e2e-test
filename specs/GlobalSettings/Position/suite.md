---
name: Global Settings Position
id: suite-global-settings-position
description: Test cases derived from tc-position.md for Global Settings > User > Position
executionOrder: 1.2
parallel: false
---

# Suite: Global Settings Position

Suite ini mencakup tab `Position` di `Global Settings > User`: katalog jabatan yang hanya menyimpan
satu atribut (`Name`), beserta tabel utama T-POS-01, modal Changelog T-POS-02, seluruh operasi CRUD
(Create/Edit/Delete/Bulk Delete) dengan guard `POS-LOGIC-02`, aturan tabel (search, filter, sort,
pagination, download, Setup Column), Role Matrix capability, pencatatan tiga surface logging, sinkron
lintas modul ke form User, dan edge case plan gating serta konkurensi.

Position bukan menu sidebar terpisah. Ia adalah sub-tab di dalam halaman `User`, dan seluruh spec
dalam suite ini dijalankan dengan sudah berada di `Global Settings > User > Position`.

`parallel: false` karena lima hal:

- Data seed Position dipakai bersama oleh banyak spec. `HR Business Partner` dan `Finance Manager`
  adalah fixture "in use" permanen bagi spec 018, 019, 020, 023, dan 024; `IT Manager` adalah target
  duplikat bagi spec 010 dan 013; `Customer Relations Officer` adalah target validasi Edit bagi spec
  014, 015, dan 016. Satu spec yang menghapus atau mengganti nama salah satu record itu membuat
  precondition spec lain hilang.
- Spec 046 menjalankan Create berulang kali sampai `master_data_count_limit` entitas tercapai. Kondisi
  itu bersifat global per entitas, bukan per spec, sehingga selama spec 046 berjalan spec Create lain
  ikut tertahan oleh Dialog 6 "Limit Reached".
- Spec 042 memverifikasi baris log di tiga surface sekaligus, dan setiap mutasi Position yang
  dilakukan spec mana pun menulis baris log baru ke surface yang sama. Pencocokan baris jadi tidak
  bisa diandalkan kalau ada spec lain yang bermutasi bersamaan.
- Preferensi Setup Column disimpan per pengguna di local storage browser dengan kunci
  `table_columns_gs_position` (PRD `position.md` §4.2e). Spec 034 dan spec 040 mengubah preferensi
  ini, sehingga spec yang lain membaca kolom bisa melihat susunan kolom yang berbeda.
- Runner belum terbukti mengikuti nomor folder, sehingga spec yang mengubah data bersama tidak bisa
  diandalkan berjalan berurutan.

Setiap spec menjalankan seed data sendiri lewat hook, jadi tidak saling menumpang hasil. Spec 046,
spec 047, dan spec 048 adalah spec yang paling sensitif urutan dan sebaiknya dijalankan sendirian.

## Mode eksekusi

- **Spec FE+BE** — dijalankan terhadap backend nyata dengan data seeding. Ini mayoritas suite.
- **Spec `Mode: mock`** — hanya tiga spec: `TC-GS-POS-E2E-004` (Guided Tooltip, tampilan murni),
  `TC-GS-POS-E2E-049` (kegagalan server di seluruh endpoint), dan `TC-GS-POS-E2E-050` (fallback
  karakter terlarang saat DOM dimanipulasi di luar jalur UI). Kebutuhan mock ditulis di
  `## Prerequisites`.

## TC yang tidak diotomasi

Lima TC hanya tingkat backend dan tidak masuk spec mana pun. Rincian alasannya ada di
`docs/coverage/GlobalSettingsPosition.md`: `TC-GS-POS-63`, `TC-GS-POS-84`, `TC-GS-POS-87`,
`TC-GS-POS-88`, dan `TC-GS-POS-91`. Konsekuensinya, seluruh TC pada section 9 "Security &
Defense-in-Depth" (`87`, `88`) tidak punya spec karena tidak terjangkau UI.
