---
id: TC-AC-ACHS-E2E-184-column-visibility-dan-setup-column-approvals-tab-active
title: "Column Visibility dan Setup Column Approvals Tab Active"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-396
  - TC-AC-ACHS-397
  - TC-AC-ACHS-398
  - TC-AC-ACHS-399
  - TC-AC-ACHS-400
coverage:
  web: automated
---

# Column Visibility dan Setup Column Approvals Tab Active

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Spec ini mengamati kolom dan konfigurasi kolom tabel, tanpa merujuk nilai sel.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
- State global browser: spec ini menyimpan konfigurasi kolom Approvals Tab Active (Setup Column, disimpan di `localStorage`). Antar blok TC konfigurasi dipulihkan lewat `[Reset to Default]` lalu `[Save]`; hook `after` suite menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE). Preferensi kolom seluruh tabel modul berada pada kondisi default saat spec dimulai.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di popup Setup Column; scroll horizontal tabel; penghapusan preferensi kolom di browser.
- Kolom default Tab Active (7): Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At.
- Anggota yang diulang (TC-398, 399, 400): Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At.

## Test Steps

### Screening overlay Column Visibility (TC-AC-ACHS-396)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Hover header kolom Actions `(⋯)`
4. Verifikasi tooltip `Column Visibility`
5. Klik header kolom Actions `(⋯)`
6. Verifikasi overlay memuat kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At dengan checkbox berstatus checked dan enabled (Hideable)
7. Verifikasi tiap kolom pada overlay punya drag handle
8. Verifikasi item `Setup Column...` di bagian bawah overlay

### Screening popup Setup Column (TC-AC-ACHS-397)

9. Klik `Setup Column...`
10. Verifikasi header popup: Title `Setup Column` dan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi tombol close `[✕]` di header popup
12. Verifikasi body memuat daftar kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At dengan checkbox checked (Hideable)
13. Verifikasi tiap kolom punya drag handle
14. Verifikasi tiap kolom punya icon Pin
15. Verifikasi Live Preview urutan header
16. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan
17. Verifikasi tidak ada `[Cancel]` di footer
18. Klik `[✕]` untuk menutup popup

### Uncheck dan check, Save, persist F5 (TC-AC-ACHS-398)

19. Buka popup Setup Column
20. Untuk setiap anggota (langkah 21 sampai 24): lakukan langkah berikut
21. Uncheck anggota
22. Verifikasi anggota hilang dari Live Preview
23. Check kembali anggota
24. Verifikasi anggota muncul kembali di Live Preview
25. Uncheck Type, klik `[Save]`
26. Verifikasi kolom Type tidak tampil di tabel
27. Muat ulang halaman (F5)
28. Verifikasi Approvals Hardware Stock Tab `Active` tampil dengan kolom Requested At
29. Verifikasi kolom Type tetap tidak tampil (tersimpan di localStorage)
30. Pulihkan konfigurasi: buka popup Setup Column, klik `[Reset to Default]`, klik `[Save]`

### Drag reorder, Save, persist F5 (TC-AC-ACHS-399)

31. Untuk setiap anggota (langkah 32 sampai 38): lakukan langkah berikut
32. Buka popup Setup Column
33. Drag kolom anggota ke posisi paling kiri
34. Verifikasi Live Preview menampilkan anggota di posisi pertama
35. Klik `[Save]`
36. Verifikasi tabel menampilkan anggota di posisi pertama
37. Muat ulang halaman (F5)
38. Verifikasi urutan tetap, anggota di posisi pertama
39. Pulihkan konfigurasi: buka popup Setup Column, klik `[Reset to Default]`, klik `[Save]`

### Pin dan unpin (TC-AC-ACHS-400)

40. Untuk setiap anggota (langkah 41 sampai 50): lakukan langkah berikut
41. Buka popup Setup Column
42. Klik icon Pin pada anggota
43. Klik `[Save]`
44. Scroll tabel horizontal
45. Verifikasi anggota membeku di kiri saat scroll horizontal
46. Muat ulang halaman (F5)
47. Verifikasi anggota tetap membeku di kiri setelah F5
48. Buka popup Setup Column, klik Pin pada anggota yang sama (unpin), klik `[Save]`
49. Scroll tabel horizontal
50. Verifikasi anggota ikut bergeser saat scroll

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-396 sampai 400). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Langkah penghubung (bukan dari langkah TC): langkah 2 (klik Tab `Active`), langkah 18 (tutup popup), langkah 30 dan 39 (pulihkan konfigurasi kolom, S-09). Langkah 28 memuat `Verifikasi` Tab Active termuat sebagai anchor positif untuk asersi absence kolom Type sesudah F5 (bagian 8b butir 2, R-21). Langkah 48 sampai 50 memulihkan pin setiap iterasi sehingga iterasi berikutnya mulai dari konfigurasi tanpa pin.
- Idiom ulang "Untuk setiap anggota": isi iterasi langkah 21 sampai 24, 32 sampai 38, 41 sampai 50; tiap iterasi punya `Verifikasi` per klausa; parameter anggota di Prerequisites.
- Spec melewati sekitar 35 langkah dengan ekspansi (7 anggota dikali blok drag dan pin): alasan, semua blok satu surface (Setup Column Approvals Tab Active) dan satu dataset read-only; tiap blok memulihkan konfigurasi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; topik satu dataset tetap satu spec (prinsip 1).
- Temuan untuk QA:
  - TC-399 menyebut "Drag kolom Type ke posisi paling kiri (anggota lain diulang dengan posisi berbeda)"; Type sudah di posisi pertama pada urutan default, sehingga asersi "posisi pertama" untuk anggota itu tidak membuktikan reorder. Spec mengulang tiap anggota ke posisi paling kiri sesuai TC.
  - TC-400 Expected a memuat "tetap setelah F5" padahal langkah TC tidak memuat F5; spec menambah langkah F5 (langkah 46) dari Expected.
  - TC-398 sampai 400 tidak menyebut tab yang tampil sesudah F5; spec mengasumsikan halaman Approvals Hardware Stock Tab Active tetap tampil (diverifikasi lewat kolom Requested At di langkah 28).
