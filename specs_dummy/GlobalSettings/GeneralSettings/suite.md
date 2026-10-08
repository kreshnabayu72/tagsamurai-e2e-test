---
name: Global Settings General Settings
id: suite-global-settings-general-settings
description: E2E test cases derived from tc-general-settings.md for Global Settings > General Settings
executionOrder: 1.3
parallel: false
---

# Suite: Global Settings General Settings

Suite ini mencakup halaman `Global Settings > General Settings`: form single-record ter-auto-create yang
hanya menyimpan atribut `Currency`, `Time Zone`, `Session Idle Timeout`, `Date Format`, dan `Time Format`,
beserta semua perilaku yang melingkupinya — state form dan seed default, Role Matrix capability, dialog
Change Currency dan dialog Unsaved Changes, modal Changelog yang menyimpan riwayat mutasi per field, sinkron
realtime via SSE feed, penataan ulang preferensi kolom tabel Changelog, serta edge case data existing,
idle timeout, plan gating, dan konkurensi.

General Settings adalah sub-tab/no sisi sidebar sendiri di bawah `Global Settings`, dan seluruh spec dalam
suite ini dijalankan dengan sudah berada di `Global Settings > General Settings`.

`parallel: false` karena lima hal:

- Halaman menampilkan satu record global yang identik untuk semua pengguna. Spec 012 dan 013 mengganti
  sekaligus mengembalikan nilai Currency, spec 039, 040 dan 041 memverifikasi perilaku sesi idle timeout,
  dan spec 011/015/login melaku memverifikasi state form yang sama. Dua spec yang bermutasi bersamaan
  membuat precondition spec lain hilang.
- Modal Changelog menyimpan seluruh riwayat mutasi global. Spec 035 memverifikasi baris log di tiga
  surface sekaligus, dan setiap mutasi General Settings yang dilakukan spec mana pun menulis baris log baru
  ke modal yang sama. Pencocokan baris jadi tidak bisa diandalkan kalau ada spec lain yang bermutasi
  bersamaan.
- Preferensi Setup Column tersimpan per pengguna di local storage browser dengan kunci
  `table_columns_gs_general_settings`. Spec 029 s.d. 032 mengubah preferensi ini, sehingga spec lain yang
  membaca kolom Changelog bisa melihat susunan kolom yang berbeda.
- SSE push realtime (spec 037) melakukan auto-refresh tabel Changelog dan state server per tenant. Ketika
  satu spec berada di tengah verifikasi, push dari spec lain mengubah data yang sedang diperiksa.
- Spec 046 memverifikasi conflict 409 saat dua admin mengedit bersamaan. Kondisi itu sengaja menggantung
  satu mutasi sepanjang spec berjalan, sehingga tidak bisa dijalankan bersamaan dengan spec lain yang juga
  membuka dialog.

Setiap spec menjalankan seed data sendiri lewat hook, jadi tidak saling menumpang hasil. Spec paling
sensitif urutan adalah 011, 012, 035, 037, dan 046 dan sebaiknya dijalankan sendirian.

## Mode eksekusi

- **Spec FE+BE** — dijalankan terhadap backend nyata dengan data seeding. Ini mayoritas suite.
- **Spec `Mode: mock`** — hanya empat spec: `TC-GS-GSET-E2E-002` (kegagalan GET form), `TC-GS-GSET-E2E-007`
  (Guided Tooltip, tampilan murni), `TC-GS-GSET-E2E-014` (kegagalan dan timeout pada PUT save), dan
  `TC-GS-GSET-E2E-034` (kegagalan server pada download). Kebutuhan mock ditulis di `## Prerequisites`.

## TC yang tidak diotomasi

Tujuh belas TC hanya tingkat backend dan tidak masuk spec mana pun. Rincian alasannya ada di
`docs/coverage/GlobalSettingsGeneralSettings.md`: seluruh TC section 6 "API Contract" (`110`, `112`,
`114`, `115`, `116`, `118`, `119`, `120`, `121`, `122`, `124`, `126`) yang memvalidasi bentuk payload dan
respons langsung tanpa permukaan UI, `133` (isolasi tenant via SSE, tanpa permukaan UI), dan seluruh TC
section 8 "Security & Defense-in-Depth" (`141`, `142`, `143`, `144`) yang memverifikasi bypass via API
client dan tidak terjangkau UI.