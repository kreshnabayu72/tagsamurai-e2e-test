---
id: TC-FA-FAAC-E2E-153-changelog-setup-column-ceklis-geser-dan-pin
title: "Modal Changelog: Setup Column Ceklis Kolom, Geser Urutan Kolom, dan Pin serta Unpin Kolom"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-504
  - TC-FA-FAAC-505
  - TC-FA-FAAC-506
sourceRules: ["§4.1.1#r30", "§4.1.1#r31", "§4.1.1#r32", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§5#b10"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r30": [6, 13, 17, 23]
  "§4.1.1#r31": [6, 13, 17, 23]
  "§4.1.1#r32": [6, 13, 17, 23]
  "§4.1.1#r26": [7, 12, 16, 23]
  "§4.1.1#r27": [7, 12, 16, 23]
  "§4.1.1#r28": [7, 12, 16, 23]
  "§4.1.1#r29": [7, 12, 16, 23]
  "§5#b10": [16, 17]
anchor: [31, 37]
coverage:
  web: automated
---

# Modal Changelog: Setup Column Ceklis Kolom, Geser Urutan Kolom, dan Pin serta Unpin Kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri di hook `after`; suite berjalan serial.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `Reset to Default`.
- Kemampuan teknis: lebar jendela browser dapat dipersempit untuk TC-506 (geser horizontal) dan dipulihkan sesudahnya; muat ulang halaman pada TC-504 memakai kemampuan browser yang sama.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAC-504: Ceklis dan unceklis kolom

2. Klik ikon `⋯` pada header kolom Actions modal
3. Klik `Setup Column...`
4. Hilangkan centang `Date`, `Action`, `Class Code`, dan `Field`
5. Klik `Save`
6. Verifikasi kolom Old Value, New Value, dan Modified By masih tampil di tabel modal
7. Verifikasi kolom Date, Action, Class Code, dan Field hilang dari tabel modal
8. Klik ikon `⋯` pada header kolom Actions modal
9. Klik `Setup Column...`
10. Centang `Date`, `Action`, `Class Code`, dan `Field` lalu hilangkan centang `Old Value`, `New Value`, dan `Modified By`
11. Klik `Save`
12. Verifikasi keempat kolom Date, Action, Class Code, dan Field tampil kembali
13. Verifikasi kolom Old Value, New Value, dan Modified By hilang
14. Muat ulang halaman (refresh)
15. Klik icon Changelog
16. Verifikasi kolom Date, Action, Class Code, dan Field tampil setelah muat ulang
17. Verifikasi kolom Old Value, New Value, dan Modified By hilang setelah muat ulang
18. Tampilkan kembali `Old Value`, `New Value`, dan `Modified By` lewat Setup Column lalu klik `Save`

### TC-FA-FAAC-505: Geser urutan kolom

19. Klik ikon `⋯` pada header kolom Actions modal
20. Klik `Setup Column...`
21. Seret `Modified By` ke posisi pertama dan `Date` ke posisi terakhir
22. Klik `Save`
23. Verifikasi tabel modal menampilkan urutan Modified By, Action, Class Code, Field, Old Value, New Value, Date
24. Kembalikan urutan awal kolom lewat Setup Column lalu klik `Save`

### TC-FA-FAAC-506: Pin dan Unpin kolom

25. Klik ikon `⋯` pada header kolom Actions modal
26. Klik `Setup Column...`
27. Klik icon Pin pada `Date`
28. Klik `Save`
29. Persempit lebar jendela browser
30. Geser tabel modal secara horizontal
31. Verifikasi kolom Date membeku saat tabel digeser
32. Klik ikon `⋯` pada header kolom Actions modal
33. Klik `Setup Column...`
34. Klik Unpin pada `Date`
35. Klik `Save`
36. Geser tabel modal secara horizontal
37. Verifikasi kolom Date ikut bergeser setelah Unpin
38. Pulihkan lebar jendela browser

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. Pemulihan antar blok: kolom dan urutan dikembalikan lewat Setup Column (langkah penghubung) supaya TC berikutnya mulai dari ketujuh kolom pada urutan awal; hook `after` menghapus preferensi kolom di browser sebagai cadangan.
5. TC-506 menggeser tabel pada lebar layar sempit; asersi 'membeku' dan 'ikut bergeser' diamati sesudah geser horizontal (S-14).
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 18, 24, 29, 38.
7. Alasan melebihi sekitar 35 langkah (38 langkah): semua blok membaca tab atau modal yang sama dengan data Pre-setup yang sama, tidak mengubah data, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
8. Anchor absence (8b butir 2): `Verifikasi` kolom Old Value, New Value, dan Modified By tampil (langkah 6) mendahului `Verifikasi` kolom Date, Action, Class Code, dan Field hilang (langkah 7); `Verifikasi` kolom tampil (langkah 16) mendahului `Verifikasi` kolom hilang (langkah 17) setelah muat ulang, satu klausa per `Verifikasi`.
