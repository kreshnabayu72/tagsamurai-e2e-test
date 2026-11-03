---
id: TC-AC-ACHS-E2E-165-setup-column-tab-in-use-guard-reset-dan-tutup
title: "Setup Column Tab In Use Guard Reset dan Tutup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-357
  - TC-AC-ACHS-358
  - TC-AC-ACHS-359
  - TC-AC-ACHS-360
coverage:
  web: automated
---

# Setup Column Tab In Use Guard Reset dan Tutup

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): SKU `Fixture.hardwareStock.p18.sku` (Long Range) dengan 7 unit In Use (Pre-setup #18, Tabel F TC; nilai sel tidak diasersi di spec ini); kolom default Tab In Use: Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power.
- State global browser: spec ini menyimpan konfigurasi kolom Tab In Use (`localStorage`). Antar blok TC konfigurasi dipulihkan lewat `[Reset to Default]` lalu `[Save]`; hook `after` suite menghapus preferensi kolom di browser (kemampuan disediakan tim FE). Preferensi kolom seluruh tabel modul berada pada kondisi default saat spec dimulai.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di popup Setup Column; penghapusan preferensi kolom di browser.
- Pilihan spec (bukan nilai TC): TC-358 langkah 4 ("uncheck satu kolom dan geser satu kolom") memakai uncheck `Client` dan geser `Registered By` ke posisi paling kiri; TC-359 langkah 4 memakai uncheck `Client`, langkah 6 mengubah urutan dengan menggeser `Registered By` ke posisi paling kiri; TC-360 menyisakan kolom `Device Name`.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |

## Test Steps

### Pin ke-4 disabled (TC-AC-ACHS-357)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Klik `(⋯)` header kolom Actions, klik `Setup Column...`
4. Pin tiga kolom Device Name, Serial Number, Client
5. Hover icon Pin pada kolom Status
6. Verifikasi icon Pin kolom Status disabled
7. Verifikasi kolom Status tidak membeku di Live Preview
8. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
9. Unpin kolom Client
10. Verifikasi icon Pin kolom Status aktif kembali
11. Klik `[✕]` untuk menutup popup

### Reset to Default lalu Save (TC-AC-ACHS-358)

12. Buka popup Setup Column, uncheck `Client`, geser `Registered By` ke posisi paling kiri
13. Klik `[Reset to Default]`
14. Verifikasi Live Preview kembali ke susunan default: kolom Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power checked dengan urutan awal
15. Klik `[Save]`
16. Muat ulang halaman (F5)
17. Verifikasi susunan default tetap pada tabel Tab In Use

### Tutup popup via (X) atau Esc membuang perubahan (TC-AC-ACHS-359)

18. Buka popup Setup Column, uncheck `Client`
19. Klik `[✕]`
20. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom Client tampil)
21. Verifikasi tidak ada dialog Unsaved Changes
22. Buka popup Setup Column
23. Verifikasi perubahan preview dibuang (Live Preview menampilkan susunan tersimpan: kolom Client tercentang)
24. Geser `Registered By` ke posisi paling kiri
25. Tekan Esc
26. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (urutan default)
27. Verifikasi tidak ada dialog Unsaved Changes

### Kolom visible terakhir tidak bisa di-uncheck (TC-AC-ACHS-360)

28. Buka popup Setup Column
29. Uncheck seluruh kolom satu per satu kecuali `Device Name`
30. Hover checkbox kolom `Device Name`
31. Verifikasi checkbox kolom tersisa disabled, tidak bisa di-uncheck
32. Verifikasi tooltip `At least one column must remain visible.`
33. Klik `[✕]` untuk menutup popup tanpa menyimpan
34. Klik header kolom Actions `(⋯)`
35. Uncheck seluruh kolom satu per satu kecuali `Device Name` pada overlay `Column Visibility`
36. Hover checkbox kolom `Device Name` pada overlay
37. Verifikasi checkbox kolom tersisa pada overlay disabled, tidak bisa di-uncheck
38. Verifikasi tooltip `At least one column must remain visible.` pada overlay
39. Check kembali seluruh kolom pada overlay `Column Visibility`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-357 sampai 360). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (bukan dari langkah TC): langkah 9 dan 10 (unpin dan `Verifikasi` aktif kembali berasal dari Expected c TC-357 yang tidak punya langkah), langkah 11, 33, dan 39 (tutup popup, tutup tanpa menyimpan, dan check kembali kolom untuk memulihkan konfigurasi, S-09). Langkah 33 sampai 38 menjalankan Expected c TC-360 ("Panel cepat Column Visibility berperilaku sama") pada overlay, karena langkah TC tidak menyebut cara menguji panel itu.
- Perubahan konfigurasi tersimpan hanya di langkah 15 (susunan default); TC lain tidak menyimpan, sehingga tidak ada langkah `[Reset to Default]` antar blok selain langkah 13. Hook `after` suite tetap menghapus preferensi kolom.
- Spec melewati sekitar 35 langkah (39 langkah): alasan, semua blok satu surface (Setup Column Tab In Use) dan satu dataset; tiap blok mengembalikan state sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-357 Expected c ("setelah satu kolom di-unpin, icon Pin kolom lain aktif kembali") tidak punya langkah unpin; spec menambah langkah 9 (unpin Client).
  - TC-358 dan TC-359 menyebut "uncheck satu kolom dan geser satu kolom" tanpa menyebut kolom; spec memilih sesuai Prerequisites.
  - TC-360 Expected c tidak menyebut cara menguji panel cepat; spec mengulang perilaku pada overlay `Column Visibility` (langkah 34 sampai 39).
