---
id: TC-AC-ACHS-E2E-289-sort-approvals-tab-active-dan-urutan-fifo
title: "Sort Approvals Tab Active dan Urutan FIFO"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-390
  - TC-AC-ACHS-391
  - TC-AC-ACHS-392
  - TC-AC-ACHS-393
  - TC-AC-ACHS-394
  - TC-AC-ACHS-395
  - TC-AC-ACHS-416
coverage:
  web: automated
---

# Sort Approvals Tab Active dan Urutan FIFO

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Jam server digeser (langkah 35 sampai 38): sesi UI dan sesi API aktor tetap valid selama jam digeser; kemampuan dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Baris dirujuk lewat nomor baris Tabel C: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel C. Urutan default FIFO (Requested At terlama di atas) sama dengan urutan Tabel C (#1 teratas, #12 terbawah). Nilai sel tidak ditulis di spec ini; penulis script membaca nilainya dari Tabel C TC lewat kunci fixture pada tabel berikut (R-06; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada):

| Parameter (atribut baris #n) | Pre-setup | Peran dan sifat baris | Kunci fixture (n = 1 sampai 12) |
|---|---|---|---|
| Type | #21 (Tabel C) | Activation Collision pada #1, #4, #5, #9, #11, #12; Register Duplicate pada #2, #3, #6, #7, #8, #10 | `Fixture.hardwareStock.p21.c[n].type` |
| Device Name (SKU) | #21 (Tabel C) | Device Name diikuti kode SKU dalam kurung; #9 adalah Subject BYO tanpa SKU (Device Name (SKU) tanpa kode SKU, Category `—`) | `Fixture.hardwareStock.p21.c[n].deviceNameSku` |
| Category | #21 (Tabel C) | Long Range pada #1 dan #10; Short Range pada #2, #3, #5, #6, #7, #8, #11; Smart Fixed Reader pada #4; BLE Gateway pada #12; `—` pada #9 | `Fixture.hardwareStock.p21.c[n].category` |
| Matched Identifier | #21 (Tabel C) | Serial Number atau MAC address unik tiap baris; #3, #9, #12 berformat MAC | `Fixture.hardwareStock.p21.c[n].matchedIdentifier` |
| Existing Record | #21 (Tabel C) | memuat kata `Registrant` pada #2, #3, #6, #7, #8, #10; memuat `Active (Client: ...)` pada baris lain | `Fixture.hardwareStock.p21.c[n].existingRecord` |
| Requested By | #21 (Tabel C) | Client, Distributor, atau Principal (Pre-setup #23) dengan label peran dalam kurung; Distributor pada #3, #6, #8, #10 | `Fixture.hardwareStock.p21.c[n].requestedBy` |
| Requested At | #21 (Tabel C) | naik menurut n (FIFO), bulan Jun 2026 pada seluruh baris | `Fixture.hardwareStock.p21.c[n].requestedAt` |
| K1 | - | keyword Search turunan: nama Client pada Existing Record baris #1 dan #11 serta Requested By baris #5; cocok dengan tepat tiga baris Tabel C (#1, #5, #11) | `Fixture.hardwareStock.derived.clientThreeRows` |
| akun totalControlPrincipal | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email` |

- Keyword Search `Fixture.hardwareStock.derived.clientThreeRows` (parameter `K1` pada tabel di atas) = nama Client yang muncul pada Existing Record #1 dan #11 serta Requested By #5 (turunan: nama Client pada `Fixture.hardwareStock.p21.c[1].existingRecord` (bagian setelah `Client: `), sama dengan `Fixture.hardwareStock.p23.client[1].name`); Search `Fixture.hardwareStock.derived.clientThreeRows` cocok pada kolom Existing Record dan Requested By dan menghasilkan tepat tiga baris: #1, #5, #11 (urutan FIFO). Semua baris itu bertipe Activation Collision.
- Parameter sort per kolom (dipakai langkah 4 sampai 12; "teratas" = tiga baris pertama tabel, diidentifikasi lewat Matched Identifier):

| Kolom | Klik 1 (Ascending) teratas | Klik 2 (Descending) teratas |
|---|---|---|
| Type | #1, #4, #5 | #2, #3, #6 |
| Device Name (SKU) | #12, #4, #9 | #6, #7, #11 |
| Category | #12, #1, #10 | #9, #4, #2 |
| Matched Identifier | #4, #9, #12 | #7, #11, #10 |
| Existing Record | #5, #12, #4 | #7, #6, #8 |
| Requested By | #12, #1, #11 | #9, #10, #5 |
| Requested At | #1, #2, #3 | #12, #11, #10 |

- Urutan default (klik 3, netral, dan sebelum sort apa pun): FIFO, Requested At terlama di atas; teratas #1, #2, #3, #4, #5.
- TC-416 (state tulis, dijalankan terakhir dalam spec ini): membuat satu Subject Register Duplicate baru lewat Add Stock Sync pada sesi lain. Kebutuhan:
  - Pelaku kedua: sesi lain yang melakukan Add Stock Sync dengan simulator reader USB (Pre-setup #25 TC, driver Handheld Reader mock) pada SKU Handheld Reader dan Serial Number yang cocok dengan unit yang sudah ada sehingga menghasilkan Subject Register Duplicate. Akun, SKU, dan Serial Number tidak tertulis di TC (disediakan tim FE/BE; lihat Temuan untuk QA).
  - Jeda 5 menit antara `[Sync]` dan `[Submit]` dipenuhi dengan mengatur jam server (jam server saja yang diatur, TTL dihitung di server): `[Sync]` pada waktu server T_sync, jam server diset absolut ke T_sync + 5 menit, `[Submit]`, lalu jam server dipulihkan sebelum langkah berikutnya (R-10, bagian 6 konvensi). Nilai 5 menit adalah pilihan spec (data uji, bukan aturan PRD).
  - Waktu server sesudah `[Submit]` (T_submit) dicatat; kolom Requested At dibandingkan dengan T_submit dengan toleransi satu menit (S-12).
  - Pemulihan state (hook `after` spec ini): Subject baru dibersihkan lewat fixture BE yang disediakan tim FE/BE sehingga Tab Active kembali 12 Subject; jam server dipulihkan; hook `after` tetap jalan walau spec gagal di tengah. Suite serial.

## Test Steps

### Siklus 3-state per kolom (TC-AC-ACHS-390, 391, 392)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Untuk setiap baris tabel "Parameter sort per kolom" (langkah 4 sampai 12): lakukan langkah berikut
4. Klik header kolom (klik 1)
5. Verifikasi indikator Ascending (`↑`) aktif pada kolom
6. Verifikasi urutan teratas sesuai kolom "Klik 1" tabel parameter
7. Klik header kolom lagi (klik 2)
8. Verifikasi indikator Descending (`↓`) aktif pada kolom
9. Verifikasi urutan teratas sesuai kolom "Klik 2" tabel parameter
10. Klik header kolom lagi (klik 3)
11. Verifikasi indikator sort kolom netral
12. Verifikasi urutan kembali ke urutan default (teratas #1, #2, #3)

### Sort default FIFO (TC-AC-ACHS-393)

13. Verifikasi urutan default tanpa menyentuh header sort: teratas #1, #2, #3, #4, #5
14. Klik header Type tiga kali sampai netral
15. Verifikasi urutan sama dengan default: teratas #1, #2, #3, #4, #5

### Guard kolom non-sortable (TC-AC-ACHS-394)

16. Verifikasi kolom Type memiliki ikon sort (anchor header tabel termuat)
17. Verifikasi kolom Actions tidak punya ikon sort
18. Klik header kolom Actions `(⋯)`
19. Verifikasi overlay `Column Visibility` terbuka
20. Verifikasi urutan baris tidak berubah (teratas #1, #2, #3)
21. Tutup overlay `Column Visibility`

### Sort tidak mereset Search (TC-AC-ACHS-395)

22. Ketik Search `Fixture.hardwareStock.derived.clientThreeRows`, tekan Enter
23. Klik header Type (Ascending)
24. Klik header Requested At (Ascending)
25. Verifikasi keyword `Fixture.hardwareStock.derived.clientThreeRows` tetap terisi
26. Verifikasi tabel hanya berisi hasil search: 3 baris #1, #5, #11 (himpunan baris, urutan tidak diasersi)
27. Verifikasi indikator Type kembali netral
28. Verifikasi indikator Requested At Ascending
29. Klik header Requested At dua kali sampai netral
30. Klik icon `(←)` pada kotak Search

### Urutan FIFO dan Requested At memakai waktu server saat Submit (TC-AC-ACHS-416)

31. Muat ulang halaman (F5)
32. Verifikasi Tab `Active` tampil dengan 12 baris
33. Verifikasi Subject dengan Requested At terlama berada di atas (FIFO): teratas #1, #2, #3
34. Di sesi lain (pelaku kedua), jalankan Add Stock Sync dan klik `[Sync]`; catat waktu server T_sync
35. Atur jam server absolut ke T_sync + 5 menit
36. Di sesi lain klik `[Submit]` hingga Subject Register Duplicate baru tersimpan
37. Catat waktu server T_submit sesudah `[Submit]`
38. Pulihkan jam server
39. Tunggu aksi selesai, lalu muat ulang Tab `Active` (F5)
40. Verifikasi Tab `Active` tampil dengan 13 baris
41. Klik `Next` ke halaman 2
42. Verifikasi Subject Register Duplicate baru berada di baris paling bawah halaman 2
43. Verifikasi Requested At Subject baru sama dengan T_submit (toleransi satu menit)
44. Verifikasi Requested At Subject baru berbeda dari T_sync (selisih sekitar 5 menit)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-390 sampai 395 dan 416). Tidak ada TC hanya-BE di spec ini.
- Konfirmasi keyword Search terhadap nilai penuh Pre-setup (#8): keyword Search `Fixture.hardwareStock.derived.clientThreeRows` adalah nilai penuh nama Client dari Existing Record baris 1 dan 11 serta Requested By baris 5 (Tabel C, Pre-setup #21; sama dengan `Fixture.hardwareStock.p23.client[1].name`). Dicocokkan dengan Tabel C: baris lain tidak memuat nama itu pada kolom Existing Record maupun Requested By, sehingga tepat tiga baris (#1, #5, #11), sesuai asersi langkah 26. Tidak ada perbedaan.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Urutan dalam spec: TC-416 menulis state (Subject baru) sehingga ditaruh paling akhir (prinsip 3 butir 5 dan Prerequisites); blok TC-390 sampai 395 hanya membaca. Hook `after` membersihkan Subject baru lewat fixture BE.
- Langkah penghubung (bukan dari langkah TC): langkah 2 (klik Tab `Active`); langkah 14 (klik header Type tiga kali, bagian TC-393 langkah 4), langkah 21 (tutup overlay), 29 (kembalikan sort Requested At ke netral), 30 (klik `(←)` mereset Search); langkah 16 (anchor positif untuk absence ikon sort pada langkah 17, bagian 8b butir 2); langkah 31, 32, 39, 40 (muat ulang untuk membaca Tab Active, "muat ulang Tab Active" pada langkah 3 TC-416); langkah 37 dan 38 (mencatat T_submit dan memulihkan jam, R-10 dan S-12); langkah 41 (Next ke halaman 2 karena 13 baris di halaman berukuran 10).
- Idiom ulang "Untuk setiap baris tabel" pada langkah 3 sampai 12 (7 iterasi, ekspansi sekitar 63 langkah); parameter di Prerequisites; `Verifikasi` per klausa (indikator dan urutan dipecah).
- Pemicu pelaku kedua dengan simulator USB adalah pemicu state (bukan objek asersi); simulator USB (kelas d) sebagai pemicu bukan kasus P-2 persis (P-2 menyebut request langsung, fixture BE, dan konteks browser kedua); dicatat di Temuan untuk QA sebagai usulan pengecualian.
- Spec melewati sekitar 35 langkah (44 langkah nominal, sekitar 100 dengan ekspansi): alasan, semua blok satu surface (Approvals Tab Active) dan satu dataset; blok baca mengembalikan Search dan sort ke netral; satu-satunya blok tulis (TC-416) di akhir dan dibersihkan hook `after`; topik satu dataset tetap satu spec (prinsip 1).
- Temuan untuk QA:
  - TC-416 langkah 3 tidak menyebut akun pelaku kedua, SKU, Serial Number, dan Existing Record yang menghasilkan Subject Register Duplicate; spec menulis "disediakan tim FE/BE". Pilihan 5 menit adalah data uji (PRD? tidak ada flag eksplisit di baris TC; lihat disposisi di laporan akhir).
  - TC-416 Expected b "berada di baris paling bawah": dengan 13 baris dan 10 baris per halaman, baris itu berada di halaman 2; spec menambah langkah Next.
  - TC-395 Expected b menulis urutan yang tidak tunggal setelah dua kali ganti sort; spec mengasersi himpunan baris.
