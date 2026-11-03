---
id: TC-AC-SG-E2E-110-delete-group-fallback-seleksi-ke-all-groups-setelah-node-header-atau-ancestor-terhapus
title: "Delete Group: Fallback Seleksi ke All Groups Setelah Node Header atau Ancestor Terhapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-144
  - TC-AC-SG-145
coverage:
  web: automated
---

# Delete Group: Fallback Seleksi ke All Groups Setelah Node Header atau Ancestor Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Hapus Utama (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`), nama literal karena TC memakai node bernama: `Hapus Warn B` (tanpa entitas, Group Role pada `Nina Amelia`) dengan anak `Hapus Warn B1` (Group Manager `Lia Marlina`) dan `Hapus Warn B2`.
- Spec ini menghapus subtree Pre-setup `Hapus Warn B` pada kedua TC (node bernama dan penugasan Pre-setup tidak dapat dimiliki spec, S-06 pengecualian 2026-10-30). Pemulihan lewat Fixture BE di hook `before` dan `after` serta di langkah 14 (antar blok TC). Efek: Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) entitas bertambah oleh penghapusan dan pemulihan dan tidak diasersi.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-144: Delete node yang sedang menjadi header mengembalikan seleksi ke All Groups

1. Klik node `Hapus Warn B` di sidebar
2. Ketik Search `B1`, tekan Enter
3. Urutkan kolom Total User secara descending
4. Klik ikon `⋯` pada node `Hapus Warn B` di sidebar, lalu pilih "Delete"
5. Klik `[Delete]` pada dialog
6. Verifikasi toast sukses: "Success, group has been deleted."
7. Verifikasi seleksi otomatis kembali ke "All Groups"
8. Verifikasi Group Context Header menampilkan tampilan default seluruh tree
9. Verifikasi tabel menampilkan tampilan default seluruh tree
10. Verifikasi Search kosong
11. Verifikasi Filter tidak aktif
12. Verifikasi Sort kembali ke Group A-Z
13. Verifikasi tabel berada di halaman 1
14. Lewat Fixture BE, pulihkan subtree `Hapus Warn B` beserta penugasan Group Role `Nina Amelia` dan Group Manager `Lia Marlina` hingga tersimpan
15. Muat ulang halaman (F5)

### TC-AC-SG-145: Delete ancestor dari node header juga mengembalikan seleksi ke All Groups

16. Klik node `Hapus Warn B1` di sidebar
17. Klik ikon `⋯` pada node `Hapus Warn B` di sidebar, lalu pilih "Delete"
18. Klik `[Delete]` pada dialog
19. Verifikasi seleksi kembali ke "All Groups" karena `Hapus Warn B1` ikut terhapus lewat cascade
20. Verifikasi Group Context Header dan tabel menampilkan default
21. Verifikasi Search kembali ke default (kosong)
22. Verifikasi Filter kembali ke default (tidak aktif)
23. Verifikasi Sort kembali ke default (Group A-Z)
24. Verifikasi tabel berada di halaman default (halaman 1)

## Notes

- Langkah penghubung (S-03): langkah 14 dan 15 (pemulihan baseline dan muat ulang antar blok, S-09).
- Default Sidebar Group Tree: seluruh tree ter-expand (PRD §4.2b), sehingga spec ini tidak memuat langkah expand node. Anak `Hapus Warn B1` langsung terlihat di sidebar sehingga langkah 16 (klik `Hapus Warn B1`) tidak didahului expand, sesuai TC-AC-SG-145.
- Asersi Search, Filter, Sort, dan halaman pada langkah 10 sampai 13 dan 21 sampai 24 dipecah satu `Verifikasi` per klausa (S-01).
- TC-AC-SG-133 (konfirmasi Delete) dan TC-AC-SG-146 berada di spec 041.
- Temuan untuk QA:
  - TC-AC-SG-145 tidak menyebut toast sukses pada Expected; spec tidak mengasersinya.
  - TC-AC-SG-145 tidak mengubah Search, Filter, Sort, atau halaman sebelum Delete, sehingga asersi "kembali ke default" pada TC itu diasersi terhadap keadaan yang sudah default.
  - TC-AC-SG-145 langkah 2 mengklik `Hapus Warn B1` di sidebar tanpa menyebut expand node induk; PRD menetapkan seluruh tree ter-expand secara default, sehingga spec tidak menambah langkah expand.
