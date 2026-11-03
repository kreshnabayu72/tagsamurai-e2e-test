---
id: TC-AC-CS-E2E-098-list-setup-column-anggota-hideable-lain
title: "List Setup Column: Anggota Hideable Lain"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-626
  - TC-AC-CS-627
  - TC-AC-CS-628
coverage:
  web: automated
---

# List Setup Column: Anggota Hideable Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Konfigurasi kolom Setup Column dan overlay Column Visibility yang disimpan spec (List dan Modal Changelog) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE); langkah penghubung "Hapus preferensi kolom di browser" memakai kemampuan yang sama.
- Cache Setup Column browser dikosongkan di hook `before` (kemampuan disediakan tim FE).
- Viewport dipersempit di hook `before` supaya tabel dapat digulir horizontal (TC-AC-CS-628); viewport dipulihkan di hook `after`.
- Tabel "Kolom disembunyikan" (TC-AC-CS-626): `Subscription ID`, `Client`, `Plan`, `Status`, `Start Date`, `End Date` (`Product` dan `Plan Owner` tetap tercentang).
- Tabel "Penempatan kolom" (TC-AC-CS-627), urutan penyeretan: `End Date` ke posisi pertama, `Start Date` ke posisi kedua, `Status` ke posisi ketiga, `Plan` ke posisi keempat, `Product` ke posisi kelima, `Client` ke posisi keenam, `Subscription ID` ke posisi paling akhir.
- Tabel "Kolom di-pin" (TC-AC-CS-628): `Subscription ID`, `Product`, `Plan`, `Status`, `Start Date`, `End Date`, `Plan Owner`.

## Test Steps

### TC-AC-CS-626: Hide dan unhide anggota Hideable lain pada List lalu Save

1. Buka modal Setup Column (`⋯` lalu `[Setup Column]`)
2. Untuk setiap baris tabel "Kolom disembunyikan" (langkah 2 sampai 3): hilangkan centang kolom itu
3. Verifikasi Live Preview menyembunyikan kolom itu
4. Klik `[Save]`
5. Verifikasi tabel hanya menampilkan kolom Product dan Plan Owner (selain kolom Actions)
6. Tekan F5
7. Verifikasi keenam kolom tetap tersembunyi setelah F5
8. Buka modal Setup Column, centang kembali keenam kolom pada tabel "Kolom disembunyikan", lalu klik `[Save]`
9. Verifikasi keenam kolom tampil lagi pada urutan semula

### TC-AC-CS-627: Geser urutan anggota Hideable lain pada List lalu Save

10. Buka modal Setup Column
11. Untuk setiap baris tabel "Penempatan kolom" (langkah 11 sampai 12): seret kolom itu ke posisi yang tertulis pada tabel
12. Verifikasi kolom itu berpindah ke posisi yang dituju tanpa posisi terkunci
13. Verifikasi Live Preview menampilkan urutan End Date, Start Date, Status, Plan, Product, Client, Plan Owner, Subscription ID
14. Klik `[Save]`
15. Verifikasi tabel menampilkan urutan End Date, Start Date, Status, Plan, Product, Client, Plan Owner, Subscription ID
16. Tekan F5
17. Verifikasi urutan bertahan setelah F5

### TC-AC-CS-628: Pin dan unpin anggota Hideable lain pada List lalu Save

18. Buka modal Setup Column lalu klik `[Reset to Default]` dan `[Save]` agar susunan kembali bawaan
19. Untuk setiap baris tabel "Kolom di-pin" (langkah 19 sampai 22): buka modal Setup Column, klik icon Pin pada kolom itu, klik `[Save]`, lalu gulir tabel ke kanan
20. Verifikasi kolom itu tetap di posisinya saat tabel digulir horizontal
21. Buka modal Setup Column, unpin kolom itu, klik `[Save]`, lalu gulir tabel ke kanan
22. Verifikasi kolom itu ikut bergeser saat tabel digulir
23. Buka modal Setup Column, pin kolom `Plan Owner`, klik `[Save]`, lalu tekan F5
24. Gulir tabel ke kanan
25. Verifikasi state Pin kolom `Plan Owner` bertahan setelah F5

## Notes

- Langkah berulang per kolom: langkah 2 sampai 3 (enam iterasi), langkah 11 sampai 12 (tujuh iterasi), dan langkah 19 sampai 22 (tujuh iterasi); parameter tiap iterasi ada di tabel `## Prerequisites`, tanpa langkah bersyarat.
- Spec ini melewati sekitar 35 langkah setelah ekspansi iterasi. Alasannya: seluruh blok satu topik (Setup Column anggota Hideable lain pada List), memakai halaman, dataset, dan harness yang sama, dan berdiri sendiri; tiap blok memulai dari susunan bawaan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Jumlah baris langkah yang ditulis tetap di bawah ambang.
- Langkah penghubung (S-03): langkah `[Reset to Default]` dan `[Save]` sebelum blok TC-AC-CS-628 yang mengembalikan susunan bawaan, langkah membuka modal Setup Column di awal blok, dan gulir tabel ke kanan (langkah 24) setelah F5 agar state Pin `Plan Owner` terlihat.
- Temuan untuk QA:
  - TC-AC-CS-628 butir Langkah Uji ke-2 ("Ulangi langkah 1 satu per satu") berulang untuk tujuh kolom; spec menuliskannya sebagai iterasi tabel "Kolom di-pin".
  - TC-AC-CS-626 Precondition "Cache Setup Column dikosongkan" tidak menyebut cara pengosongan; dikosongkan hook `before` oleh kemampuan tim FE.
