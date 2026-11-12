---
id: TC-FA-TAG-E2E-016-screening-tab-to-be-returned-header-kolom-dan-format-sel-bagian-1
title: "Screening Tab To Be Returned: Header, Tooltip Toolbar, Kolom Tabel, Urutan Bawaan, dan Format Sel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-76
  - TC-FA-TAG-77
  - TC-FA-TAG-78
  - TC-FA-TAG-79
  - TC-FA-TAG-80
coverage:
  web: automated
---

# Screening Tab To Be Returned: Header, Tooltip Toolbar, Kolom Tabel, Urutan Bawaan, dan Format Sel

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab To Be Returned (hanya dibaca, tidak diubah; dipakai TC-FA-TAG-76 sampai 80; tabel berikut adalah himpunan minimum, jumlah total Tag To Be Returned dalam scope dibaca sebagai N dan tidak diasumsikan tepat 3):

  | TAG Code | Tipe | Last Asset | Reason | Return Group | Current Holder | Since |
  |---|---|---|---|---|---|---|
  | `RF-00071` | RFID | Excavator 20 Ton - 2 | Disposal | Disposal Center | Dedi K. | 01 Sep 2026 |
  | `RF-00088` | RFID | Excavator 20 Ton - 5 | Disposal | Disposal Center | Dedi K. | 20 Sep 2026 |
  | `NF-00092` | NFC | Laptop Pro 14 - 8 | Disposal | HQ Warehouse | Rina T. | 22 Sep 2026 |

- Format tanggal kolom `Since` mengikuti pengaturan General Settings tenant uji; nilai format dibaca dari General Settings dan `[N]` dihitung dari tanggal `Since` terhadap tanggal hari uji.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada kode, urutan, dan tanggal (suite.md).
- Kemampuan teknis (disediakan tim FE/BE): pembacaan jumlah Tag To Be Returned dalam scope (N) lewat kemampuan baca BE di hook `before`, bukan dari badge (bagian 8b butir 10; A-18); spec ini tidak mengubah data sehingga N tidak perlu dibaca ulang.
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-76: Screening header halaman tab To Be Returned: breadcrumb, tab, dan toolbar

1. Klik Tab `To Be Returned`
2. Verifikasi Breadcrumb tampil persis `Fixed Asset > TAG > To Be Returned`
3. Verifikasi segmen terakhir Breadcrumb `To Be Returned` bukan link
4. Verifikasi tidak ada Page Title di atas tab
5. Verifikasi Tab `Paired` dan Tab `To Be Returned` tampil
6. Verifikasi Tab `To Be Returned` aktif dan berbadge jumlah Tag (severity secondary) bernilai N (jumlah Tag To Be Returned dalam scope yang dibaca di hook `before`, sedikitnya 3)
7. Verifikasi toolbar rata kanan berurutan dari kiri: ikon Search, ikon Filter, ikon Download, tombol `Event Log`, lalu tombol scan `Receive TAG` di ujung kanan setelah `Event Log`
8. Verifikasi tombol `Changelog` tidak ada di toolbar tab ini
9. Verifikasi tidak ada tombol Create

### TC-FA-TAG-77: Tooltip ikon toolbar tab To Be Returned (Search, Filter, Download)

10. Arahkan kursor ke ikon Search
11. Verifikasi ikon Search menampilkan tooltip `Search`
12. Arahkan kursor ke ikon Filter
13. Verifikasi ikon Filter menampilkan tooltip `Filter`
14. Arahkan kursor ke ikon Download
15. Verifikasi ikon Download menampilkan tooltip `Download`

### TC-FA-TAG-78: Screening kolom tabel To Be Returned untuk Total Control

16. Periksa header tabel dari kiri ke kanan
17. Verifikasi header kolom berurutan: `TAG Code`, `Last Asset`, `Reason`, `Return Group`, `Current Holder`, `Since`
18. Verifikasi tabel menampilkan satu baris per Tag (sedikitnya 3 baris: `RF-00071`, `RF-00088`, `NF-00092`), tanpa grup baris dan tanpa popup detail
19. Verifikasi kolom checkbox seleksi baris tampil di sisi kiri
20. Verifikasi menu aksi baris tampil di ujung kanan tiap baris
21. Verifikasi tidak ada kolom `Return Status`

### TC-FA-TAG-79: Urutan bawaan tabel To Be Returned: Since terlama di atas

22. Verifikasi baris berurutan dari atas: `RF-00071`, `RF-00088`, `NF-00092` (Since paling lama di atas)

### TC-FA-TAG-80: Format sel tiap kolom tabel To Be Returned

23. Periksa baris pertama (`RF-00071`) pada tiap kolom
24. Verifikasi kolom `TAG Code` menampilkan ikon tipe Tag (label aksesibilitas `RFID`) diikuti teks `RF-00071`
25. Verifikasi kolom `Last Asset` menampilkan teks `Excavator 20 Ton - 2` tanpa tautan
26. Verifikasi kolom `Reason` menampilkan teks `Disposal`
27. Verifikasi kolom `Return Group` menampilkan badge Primary `Disposal Center`
28. Verifikasi kolom `Current Holder` menampilkan `Dedi K.` (format [First Name] [Last Initial])
29. Verifikasi kolom `Since` menampilkan tanggal sesuai format General Settings diikuti `([N] days)`

## Notes

- Langkah 16 dan 23 adalah langkah penghubung (mengamati header dan baris), tanpa asersi (S-03).
- Langkah 8, 9, 18 (klausa "tanpa grup baris dan tanpa popup detail"), dan 21 adalah asersi absence atas elemen UI; anchor positif adalah Verifikasi toolbar tampil (langkah 7) dan header kolom tampil (langkah 17) pada permukaan yang sama (bagian 8b butir 2).
- Langkah 22 mengasersi urutan dari tiga tanggal Since yang berbeda (S-11); TC-FA-TAG-79 mensyaratkan Since `RF-00071` 01 Sep 2026, `RF-00088` 20 Sep 2026, dan `NF-00092` 22 Sep 2026, nilai yang dipakai pula di tabel data di atas.
- Langkah 6 mengasersi Badge terhadap N dan langkah 18 mengasersi sedikitnya tiga baris Pre-setup (relatif, bukan literal `3`; keputusan user 2026-11-04, bagian 8b butir 10).
- TC-FA-TAG-81 sampai 84, 88 sampai 90 ada di spec 017.
- A-15: nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena TC menuntut asersi kode, urutan, dan tanggal; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-80 Expected f ("tanggal sesuai format General Settings diikuti `([N] days)`") tidak menyebut format tanggal tenant uji maupun tanggal acuan untuk menghitung `[N]`; spec menyerahkan nilai format dan perhitungan `[N]` ke tahap script.
  - TC-FA-TAG-76 dan 78 menyebut `Receive TAG` dan menu aksi baris tetapi tidak menyebut isi menu aksi baris; spec hanya mengasersi keberadaannya.
