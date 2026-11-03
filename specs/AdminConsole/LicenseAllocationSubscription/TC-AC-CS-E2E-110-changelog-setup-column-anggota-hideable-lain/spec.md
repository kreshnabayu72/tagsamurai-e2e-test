---
id: TC-AC-CS-E2E-110-changelog-setup-column-anggota-hideable-lain
title: "Changelog: Setup Column Anggota Hideable Lain"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-629
  - TC-AC-CS-630
  - TC-AC-CS-631
coverage:
  web: automated
---

# Changelog: Setup Column Anggota Hideable Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- Changelog, Activity Log, dan System Log adalah audit trail permanen: spec ini tidak menulis entri dan tidak mengasersi total entri sebagai angka absolut (S-12).
- Konfigurasi kolom Setup Column dan overlay Column Visibility yang disimpan spec (List dan Modal Changelog) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE); langkah penghubung "Hapus preferensi kolom di browser" memakai kemampuan yang sama.
- Cache Setup Column browser dikosongkan di hook `before` (kemampuan disediakan tim FE). Viewport dipersempit di hook `before` supaya tabel Changelog dapat digulir horizontal (TC-AC-CS-631); viewport dipulihkan di hook `after`.
- Tabel "Kolom disembunyikan" (TC-AC-CS-629): `Date`, `Action`, `Client — Product`, `Field`, `Modified By` (`Old Value` dan `New Value` tetap tercentang).
- Tabel "Penempatan kolom" (TC-AC-CS-630), urutan penyeretan: `New Value` ke posisi pertama, `Old Value` ke posisi kedua, `Field` ke posisi ketiga, `Client — Product` ke posisi keempat, `Action` ke posisi kelima, `Date` ke posisi keenam.
- Tabel "Kolom di-pin" (TC-AC-CS-631): `Action`, `Client — Product`, `Field`, `Old Value`, `New Value`, `Modified By`.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-AC-CS-629: Hide dan unhide anggota Hideable lain pada Changelog lalu Save

2. Buka modal Setup Column
3. Untuk setiap baris tabel "Kolom disembunyikan" (langkah 3 sampai 4): hilangkan centang kolom itu
4. Verifikasi tabel Changelog menyembunyikan kolom itu
5. Klik `[Save]`
6. Tunggu aksi selesai (modal Changelog Setup Column tertutup)
7. Tekan F5 lalu buka lagi modal Changelog
8. Verifikasi tabel hanya menampilkan Old Value dan New Value setelah F5
9. Buka modal Setup Column, centang kembali kelima kolom pada tabel "Kolom disembunyikan", lalu klik `[Save]`
10. Verifikasi kelima kolom tampil lagi pada urutan semula

### TC-AC-CS-630: Geser urutan anggota Hideable lain pada Changelog lalu Save

11. Buka modal Setup Column
12. Untuk setiap baris tabel "Penempatan kolom" (langkah 12 sampai 13): seret kolom itu ke posisi yang tertulis pada tabel
13. Verifikasi kolom itu berpindah ke posisi yang dituju tanpa posisi terkunci
14. Klik `[Save]`
15. Verifikasi tabel Changelog menampilkan urutan New Value, Old Value, Field, Client — Product, Action, Date, Modified By
16. Tekan F5 lalu buka lagi modal Changelog
17. Verifikasi urutan bertahan setelah F5

### TC-AC-CS-631: Pin dan unpin anggota Hideable lain pada Changelog lalu Save

18. Buka modal Setup Column lalu klik `[Reset to Default]` dan `[Save]` agar susunan kembali bawaan
19. Untuk setiap baris tabel "Kolom di-pin" (langkah 19 sampai 22): buka modal Setup Column, klik icon Pin pada kolom itu, klik `[Save]`, lalu gulir tabel ke kanan
20. Verifikasi kolom itu tetap di posisinya saat tabel digulir horizontal
21. Buka modal Setup Column, unpin kolom itu, klik `[Save]`, lalu gulir tabel ke kanan
22. Verifikasi kolom itu ikut bergeser saat tabel digulir

## Notes

- Langkah berulang per kolom: langkah 3 sampai 4 (lima iterasi), langkah 12 sampai 13 (enam iterasi), dan langkah 19 sampai 22 (enam iterasi); parameter tiap iterasi ada di tabel `## Prerequisites`, tanpa langkah bersyarat.
- Spec ini melewati sekitar 35 langkah setelah ekspansi iterasi. Alasannya: seluruh blok satu topik (Setup Column anggota Hideable lain pada Modal Changelog), memakai modal, seed #84, dan harness yang sama, dan berdiri sendiri; tiap blok memulai dari susunan bawaan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah baris langkah yang ditulis tetap di bawah ambang.
- Langkah penghubung (S-03): langkah `[Reset to Default]` dan `[Save]` sebelum blok TC-AC-CS-631 yang mengembalikan susunan bawaan, dan langkah membuka modal Setup Column di awal blok.
- Langkah penghubung (S-03, bagian 8b butir 8): langkah `Tunggu aksi selesai` (langkah 6) menunggu modal Changelog Setup Column tertutup sesudah `[Save]` sebelum langkah berikutnya mengubah permukaan.
- Temuan untuk QA:
  - TC-AC-CS-629 Expected a menyebut kolom tersembunyi "satu per satu saat centang dilepas"; spec menuliskannya sebagai iterasi tabel "Kolom disembunyikan".
  - TC-AC-CS-630 Expected a dan b menyebut urutan akhir dan posisi tiap kolom; Langkah Uji tidak menyebut kolom Modified By yang ikut bergeser ke posisi ketujuh.
  - TC-AC-CS-631 butir Langkah Uji ke-3 ("Ulangi langkah 2 satu per satu") berulang untuk enam kolom; spec menuliskannya sebagai iterasi tabel "Kolom di-pin".
