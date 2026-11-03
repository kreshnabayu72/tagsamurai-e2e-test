---
id: TC-AC-ACHS-E2E-185-setup-column-approvals-tab-active-guard-reset-tutup-dan-cache-independen
title: "Setup Column Approvals Tab Active Guard Reset Tutup dan Cache Independen"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-401
  - TC-AC-ACHS-402
  - TC-AC-ACHS-403
  - TC-AC-ACHS-404
  - TC-AC-ACHS-602
coverage:
  web: automated
---

# Setup Column Approvals Tab Active Guard Reset Tutup dan Cache Independen

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Spec ini mengamati kolom dan konfigurasi kolom tabel, tanpa merujuk nilai sel.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40) untuk membuka Stock Detail Tab Available dan Tab In Use (TC-602) | `Fixture.hardwareStock.p16.a[4].sku` |
- State global browser: spec ini menyimpan konfigurasi kolom Approvals Tab Active (Setup Column, `localStorage`). Antar blok TC konfigurasi dipulihkan lewat `[Reset to Default]` lalu `[Save]`; hook `after` suite menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE). Preferensi kolom seluruh tabel modul (Stock List, Tab Available, Tab In Use, Approvals Tab Active, Approvals Tab History, Popup Event Log) berada pada kondisi default (cache browser bersih) saat spec dimulai (precondition c TC-602), dijamin hook `after` suite pada spec sebelumnya.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di popup Setup Column; penghapusan preferensi kolom di browser.
- Data tambahan TC-602 (hanya dibaca): SKU Handheld Reader Long Range dengan unit Available dan In Use (`Fixture.hardwareStock.p16.a[4].sku`, Tabel A TC) pada Stock List (Pre-setup #16 sampai #20) untuk membuka Stock Detail Tab Available dan Tab In Use; Approvals Tab History dari Pre-setup #22 (Tabel D TC).
- Kolom default tiap tabel pada TC-602:

| Tabel | Kolom default |
|---|---|
| Approvals Tab Active | Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At |
| Approvals Tab History | Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At |
| Stock List | Photo, Device Name, SKU, Type, Range Type, Brand, Model/Type, Total Registered, Available, In Use, Last Updated |
| Stock Detail Tab Available | Device Name, Serial Number, Status, Registered At, Registered By, Min Power, Max Power, Current Power |
| Stock Detail Tab In Use | Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power |

- Pilihan spec (bukan nilai TC): TC-402 dan TC-403 langkah 3 ("uncheck satu kolom dan geser satu kolom") memakai uncheck `Category` dan geser `Requested By` ke posisi paling kiri; TC-404 menyisakan kolom `Type`.

## Test Steps

### Pin ke-4 disabled (TC-AC-ACHS-401)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Klik `(⋯)` header kolom Actions, klik `Setup Column...`
4. Pin tiga kolom Type, Device Name (SKU), Category
5. Hover icon Pin pada kolom Matched Identifier
6. Verifikasi icon Pin kolom Matched Identifier disabled
7. Verifikasi kolom Matched Identifier tidak membeku di Live Preview
8. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
9. Unpin kolom Category
10. Verifikasi icon Pin kolom Matched Identifier aktif kembali
11. Klik `[✕]` untuk menutup popup

### Reset to Default lalu Save (TC-AC-ACHS-402)

12. Buka popup Setup Column, uncheck `Category`, geser `Requested By` ke posisi paling kiri
13. Klik `[Reset to Default]`
14. Verifikasi Live Preview kembali ke susunan default: kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Requested At checked dengan urutan awal
15. Klik `[Save]`
16. Muat ulang halaman (F5)
17. Verifikasi susunan default tetap pada tabel Approvals Tab Active

### Tutup popup via (X) atau Esc membuang perubahan (TC-AC-ACHS-403)

18. Buka popup Setup Column, uncheck `Category`
19. Klik `[✕]`
20. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom Category tampil)
21. Verifikasi tidak ada dialog Unsaved Changes
22. Buka popup Setup Column
23. Verifikasi perubahan preview dibuang (Live Preview menampilkan susunan tersimpan: kolom Category tercentang)
24. Geser `Requested By` ke posisi paling kiri
25. Tekan Esc
26. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (urutan default)
27. Verifikasi tidak ada dialog Unsaved Changes

### Kolom visible terakhir tidak bisa di-uncheck (TC-AC-ACHS-404)

28. Buka popup Setup Column
29. Uncheck seluruh kolom satu per satu kecuali `Type`
30. Hover checkbox kolom `Type`
31. Verifikasi checkbox kolom tersisa disabled, tidak bisa di-uncheck
32. Verifikasi tooltip `At least one column must remain visible.`
33. Klik `[✕]` untuk menutup popup tanpa menyimpan
34. Klik header kolom Actions `(⋯)`
35. Uncheck seluruh kolom satu per satu kecuali `Type` pada overlay `Column Visibility`
36. Hover checkbox kolom `Type` pada overlay
37. Verifikasi checkbox kolom tersisa pada overlay disabled, tidak bisa di-uncheck
38. Verifikasi tooltip `At least one column must remain visible.` pada overlay
39. Check kembali seluruh kolom pada overlay `Column Visibility`

### Cache Setup Column independen per tabel, arah B (TC-AC-ACHS-602)

40. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
41. Uncheck `Category`, klik `[Save]`
42. Verifikasi Approvals Tab Active tidak menampilkan kolom Category setelah Save
43. Klik Tab `History`
44. Verifikasi kolom Approvals Tab History tidak berubah: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At tetap tampil
45. Buka Hardware > Stock
46. Verifikasi kolom Stock List tidak berubah: Photo, Device Name, SKU, Type, Range Type, Brand, Model/Type, Total Registered, Available, In Use, Last Updated tetap tampil
47. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
48. Verifikasi kolom Tab Available tidak berubah: Device Name, Serial Number, Status, Registered At, Registered By, Min Power, Max Power, Current Power tetap tampil
49. Klik Tab `In Use`
50. Verifikasi kolom Tab In Use tidak berubah: Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power tetap tampil
51. Kembali ke Approvals > Hardware Stock Tab `Active`
52. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
53. Klik `[Reset to Default]`, klik `[Save]`
54. Verifikasi Approvals Tab Active kembali menampilkan kolom Category

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-401 sampai 404 dan 602). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Langkah penghubung (bukan dari langkah TC): langkah 2 (klik Tab `Active`); langkah 9 dan 10 (unpin dan `Verifikasi` aktif kembali berasal dari Expected c TC-401 yang tidak punya langkah unpin); langkah 11, 33, dan 39 (tutup popup, tutup tanpa menyimpan, check kembali kolom untuk memulihkan konfigurasi, S-09). Langkah 33 sampai 38 menjalankan Expected c TC-404 ("Panel cepat Column Visibility berperilaku sama") pada overlay, karena langkah TC tidak menyebut cara menguji panel itu. Langkah 51 menggabungkan "Kembali ke Approvals Tab Active" sesuai langkah 8 TC-602.
- Perubahan konfigurasi tersimpan di langkah 15 (susunan default) dan langkah 41 (TC-602), dan dipulihkan di langkah 53; hook `after` suite tetap menghapus preferensi kolom.
- TC-602 sebagai TC terakhir spec ini: ia membutuhkan cache bersih sebelum langkah 41 (precondition c TC-602), yang dipenuhi karena blok TC-401 sampai 404 mengembalikan konfigurasi tersimpan ke default (langkah 13 sampai 15) dan tidak menyimpan perubahan lain.
- Spec melewati sekitar 35 langkah (54 langkah): alasan, semua blok berkaitan dengan Setup Column Approvals Tab Active, satu dataset read-only (TC-602 menyentuh tabel lain hanya untuk membaca kolomnya); tiap blok mengembalikan state sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-401 Expected c ("setelah satu kolom di-unpin, icon Pin kolom lain aktif kembali") tidak punya langkah unpin; spec menambah langkah 9.
  - TC-402 dan TC-403 menyebut "uncheck satu kolom dan geser satu kolom" tanpa menyebut kolom; spec memilih sesuai Prerequisites.
  - TC-404 Expected c tidak menyebut cara menguji panel cepat; spec mengulang perilaku pada overlay `Column Visibility` (langkah 34 sampai 39).
  - TC-602 langkah 5 sampai 7 hanya menyebut "amati kolom" tanpa asersi bernomor selain Expected b; spec mengasersi per tabel sesuai daftar kolom Expected b.
