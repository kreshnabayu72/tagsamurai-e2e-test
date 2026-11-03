---
id: TC-AC-ACHS-E2E-125-setup-column-stock-list-guard-reset-tutup-dan-cache-independen
title: "Setup Column Stock List: Batas Pin, Reset to Default, Tutup Popup, Kolom Terakhir, dan Cache Independen antar Tabel"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-242
  - TC-AC-ACHS-243
  - TC-AC-ACHS-244
  - TC-AC-ACHS-245
  - TC-AC-ACHS-601
coverage:
  web: automated
---

# Setup Column Stock List: Batas Pin, Reset to Default, Tutup Popup, Kolom Terakhir, dan Cache Independen antar Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List dan halaman Approvals Hardware Stock; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): #16 Katalog SKU 30 baris Stock List (Tabel A: 8 SKU nama dan 22 SKU `Fixture.hardwareStock.p16.a[9].sku` sampai `Fixture.hardwareStock.p16.a[30].sku`) dan #15 General Settings (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | SKU baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
  | SKU baris padding 22 (Tabel A baris 30) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
  | Device Name unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
- Data Pre-setup tambahan (read-only, TC-AC-ACHS-601): SKU `Fixture.hardwareStock.p16.a[4].sku` dengan Tab Available (unit `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`) dan Tab In Use (7 unit, #18), Approvals Hardware Stock Tab Active (12 Subject, #21) dan Tab History (12 Subject, #22), serta Popup Event Log SKU `Fixture.hardwareStock.p16.a[4].sku` (12 sesi, #20). Preferensi kolom seluruh tabel modul dalam keadaan default (preferensi di browser dihapus di hook `before` spec ini; kemampuan disediakan tim FE).
- Data uji TC-AC-ACHS-245 (kolom yang di-uncheck satu per satu pada popup dan pada overlay; kolom tersisa `Last Updated`, pilihan spec):

  | No | Kolom |
  |---|---|
  | 1 | `Photo` |
  | 2 | `Device Name` |
  | 3 | `SKU` |
  | 4 | `Type` |
  | 5 | `Range Type` |
  | 6 | `Brand` |
  | 7 | `Model/Type` |
  | 8 | `Total Registered` |
  | 9 | `Available` |
  | 10 | `In Use` |

- Daftar kolom tabel lain (TC-AC-ACHS-601): Tab Available `Device Name | Serial Number | Status | Registered At | Registered By | Min Power | Max Power | Current Power`; Tab In Use `Device Name | Serial Number | Client | Status | Registered At | Registered By | Activated At | Min Power | Max Power | Current Power`; Approvals Tab Active `Type | Device Name (SKU) | Category | Matched Identifier | Existing Record | Requested By | Requested At`; Approvals Tab History `Type | Device Name (SKU) | Category | Matched Identifier | Existing Record | Requested By | Approval | Approver | Requested At | Resolved At`; Popup Event Log `Date | Activity | Success | Waiting for Approval | Modified By`.
- Pilihan spec: TC-AC-ACHS-243 meng-uncheck `Brand` dan menggeser `Last Updated` ke posisi pertama; TC-AC-ACHS-244 meng-uncheck `Type` (TC menulis "satu kolom") dan mengubah urutan dengan menggeser `Last Updated` ke posisi pertama.
- Kemampuan teknis (disediakan tim FE): hover checkbox dan icon Pin untuk membaca tooltip; drag and drop baris kolom di popup Setup Column; menghapus preferensi kolom di browser (hook `before` dan `after`).
- State global yang diubah: preferensi kolom di browser; dipulihkan lewat `[Reset to Default]` dan `[Save]` pada akhir TC-AC-ACHS-243 dan 601, dan hook suite `after` menghapus preferensi kolom (didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-242: Pin ke-4 disabled setelah 3 kolom di-pin

1. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
2. Klik icon Pin pada `Device Name`, `SKU`, dan `Type`
3. Arahkan kursor ke icon Pin kolom `Brand`
4. Verifikasi icon Pin kolom `Brand` disabled dan tidak membekukan kolom
5. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
6. Klik icon Pin pada `Type` (unpin)
7. Verifikasi icon Pin kolom `Brand` aktif kembali
8. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-AC-ACHS-243: Reset to Default lalu Save mengembalikan susunan awal

9. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
10. Hilangkan centang `Brand` dan drag `Last Updated` ke posisi pertama pada popup
11. Klik `[Reset to Default]`
12. Verifikasi Live Preview kembali ke susunan default: `Photo`, `Device Name`, `SKU`, `Type`, `Range Type`, `Brand`, `Model/Type`, `Total Registered`, `Available`, `In Use`, `Last Updated` semuanya checked dengan urutan awal
13. Klik `[Save]`
14. Muat ulang halaman (F5)
15. Verifikasi susunan default tetap pada tabel: kolom `Photo`, `Device Name`, `SKU`, `Type`, `Range Type`, `Brand`, `Model/Type`, `Total Registered`, `Available`, `In Use`, `Last Updated` dengan urutan awal

### TC-AC-ACHS-244: Tutup popup via (X) atau Esc membuang perubahan

16. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
17. Hilangkan centang `Type`, klik `[✕]`
18. Verifikasi kolom `Type` tetap tampil pada tabel (konfigurasi tersimpan terakhir)
19. Verifikasi tidak ada dialog Unsaved Changes
20. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
21. Verifikasi checkbox `Type` pada popup tercentang (perubahan preview dibuang)
22. Drag `Last Updated` ke posisi pertama pada popup, tekan Esc
23. Verifikasi urutan kolom tabel tidak berubah (`Photo` tetap pertama)
24. Verifikasi tidak ada dialog Unsaved Changes

### TC-AC-ACHS-245: Kolom visible terakhir tidak bisa di-uncheck

25. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
26. Untuk setiap baris tabel Data uji TC-AC-ACHS-245 (langkah 26): hilangkan centang kolom di popup
27. Arahkan kursor ke checkbox kolom tersisa `Last Updated`
28. Verifikasi checkbox `Last Updated` disabled dan tidak bisa di-uncheck
29. Verifikasi tooltip `At least one column must remain visible.`
30. Klik `[✕]` untuk menutup popup tanpa menyimpan
31. Klik header kolom Actions `(⋯)`
32. Untuk setiap baris tabel Data uji TC-AC-ACHS-245 (langkah 32): hilangkan centang kolom di overlay Column Visibility
33. Arahkan kursor ke checkbox kolom tersisa `Last Updated` pada overlay
34. Verifikasi checkbox `Last Updated` pada overlay disabled dan tidak bisa di-uncheck
35. Verifikasi tooltip `At least one column must remain visible.` pada overlay
36. Untuk setiap baris tabel Data uji TC-AC-ACHS-245 (langkah 36): ceklis kembali kolom di overlay Column Visibility
37. Tutup overlay Column Visibility

### TC-AC-ACHS-601: Cache Setup Column independen per tabel (arah A)

38. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
39. Hilangkan centang `Brand`, klik `[Save]`
40. Verifikasi Stock List tidak menampilkan kolom `Brand`
41. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`, pastikan Tab Available aktif
42. Verifikasi kolom Tab Available `Device Name`, `Serial Number`, `Status`, `Registered At`, `Registered By`, `Min Power`, `Max Power`, `Current Power` tampil
43. Klik Tab In Use
44. Verifikasi kolom Tab In Use `Device Name`, `Serial Number`, `Client`, `Status`, `Registered At`, `Registered By`, `Activated At`, `Min Power`, `Max Power`, `Current Power` tampil
45. Buka Approvals > Hardware Stock
46. Verifikasi kolom Approvals Tab Active `Type`, `Device Name (SKU)`, `Category`, `Matched Identifier`, `Existing Record`, `Requested By`, `Requested At` tampil
47. Klik Tab History
48. Verifikasi kolom Approvals Tab History `Type`, `Device Name (SKU)`, `Category`, `Matched Identifier`, `Existing Record`, `Requested By`, `Approval`, `Approver`, `Requested At`, `Resolved At` tampil
49. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`, klik icon `[Event Log]`
50. Verifikasi kolom Popup Event Log `Date`, `Activity`, `Success`, `Waiting for Approval`, `Modified By` tampil
51. Tutup Popup Event Log, buka Hardware > Stock
52. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`
53. Verifikasi Stock List kembali menampilkan kolom `Brand`


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Urutan TC: 242, 243, 244, 245, lalu TC-AC-ACHS-601 paling akhir karena berpindah ke Stock Detail, Approvals, dan Popup Event Log. Setelah `[Reset to Default]` dan `[Save]` pada TC-AC-ACHS-243 preferensi berupa susunan default yang tersimpan, setara dengan cache bersih untuk TC-AC-ACHS-601.
- Langkah 26, 32, dan 36 berulang untuk setiap baris tabel Data uji (sepuluh iterasi masing-masing; bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan popup (`[✕]`), pemulihan kolom di overlay (langkah 36), pemulihan lewat `[Reset to Default]` lalu `[Save]` (aksi sisi klien, tanpa "Tunggu aksi selesai"), serta navigasi antar-halaman pada TC-AC-ACHS-601. Langkah "Verifikasi kolom `Device Name` ... tampil" pada daftar kolom tabel lain adalah asersi isi daftar kolom (bukan absence).
- Spec memiliki 53 langkah nominal dan 80 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Setup Column Stock List pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC-AC-ACHS-243 dan TC-AC-ACHS-244 menulis "satu kolom" dan "mengubah urutan" tanpa nama kolom; spec memilih kolom (Prerequisites). TC-AC-ACHS-245 tidak menyebut kolom yang tersisa; spec menyisakan `Last Updated`.
  - TC-AC-ACHS-245 Expected c ("Panel cepat Column Visibility berperilaku sama") tidak menyebut apakah perubahan overlay langsung berlaku; spec memulihkan dengan ceklis ulang di overlay (langkah 36) dan menutup overlay.
  - TC-AC-ACHS-601 menyebut icon `[Event Log]` pada Stock Detail tanpa teks tooltip (NC-07 dalam TC); spec memakai nama icon seperti TC.
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
