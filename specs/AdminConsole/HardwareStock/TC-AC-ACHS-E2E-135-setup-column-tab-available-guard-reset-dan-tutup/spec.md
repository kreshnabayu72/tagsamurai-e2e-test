---
id: TC-AC-ACHS-E2E-135-setup-column-tab-available-guard-reset-dan-tutup
title: "Setup Column Stock Detail Tab Available: Batas Pin, Reset to Default, Tutup Popup, dan Kolom Terakhir"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-301
  - TC-AC-ACHS-302
  - TC-AC-ACHS-303
  - TC-AC-ACHS-304
coverage:
  web: automated
---

# Setup Column Stock Detail Tab Available: Batas Pin, Reset to Default, Tutup Popup, dan Kolom Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): SKU `Fixture.hardwareStock.p16.a[4].sku` (Long Range) dengan 18 unit Available dan 1 unit Waiting for Approval (#17, Tabel E: `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`; Tab Available 19 baris) dan General Settings #15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | Device Name unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
- Setup Column: preferensi kolom disimpan di browser; hook suite `after` menghapusnya (bukan `[Reset to Default]`; kemampuan disediakan tim FE, lihat `suite.md`).
- Data uji TC-AC-ACHS-304 (kolom yang di-uncheck satu per satu pada popup dan pada overlay; kolom tersisa `Current Power`, pilihan spec):

  | No | Kolom |
  |---|---|
  | 1 | `Device Name` |
  | 2 | `Serial Number` |
  | 3 | `Status` |
  | 4 | `Registered At` |
  | 5 | `Registered By` |
  | 6 | `Min Power` |
  | 7 | `Max Power` |

- Pilihan spec: TC-AC-ACHS-302 meng-uncheck `Status` dan menggeser `Current Power` ke posisi pertama; TC-AC-ACHS-303 meng-uncheck `Status` dan menggeser `Current Power` ke posisi pertama (TC menulis "satu kolom" dan "mengubah urutan" tanpa nama kolom).
- Kemampuan teknis (disediakan tim FE): hover checkbox dan icon Pin untuk membaca tooltip; drag and drop baris kolom di popup Setup Column; menghapus preferensi kolom di browser.
- State global yang diubah: preferensi kolom Tab Available di browser; dipulihkan lewat `[Reset to Default]` dan `[Save]` pada akhir TC-AC-ACHS-302 dan hook suite `after` menghapusnya (didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab Available aktif

### TC-AC-ACHS-301: Pin ke-4 disabled setelah 3 kolom di-pin

3. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
4. Klik icon Pin pada `Device Name`, `Serial Number`, dan `Status`
5. Arahkan kursor ke icon Pin kolom `Registered By`
6. Verifikasi icon Pin kolom `Registered By` disabled dan tidak membekukan kolom
7. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
8. Klik icon Pin pada `Status` (unpin)
9. Verifikasi icon Pin kolom `Registered By` aktif kembali
10. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-AC-ACHS-302: Reset to Default lalu Save mengembalikan susunan awal

11. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
12. Hilangkan centang `Status` dan drag `Current Power` ke posisi pertama pada popup
13. Klik `[Reset to Default]`
14. Verifikasi Live Preview kembali ke susunan default: `Device Name`, `Serial Number`, `Status`, `Registered At`, `Registered By`, `Min Power`, `Max Power`, `Current Power` semuanya checked dengan urutan awal
15. Klik `[Save]`
16. Muat ulang halaman (F5)
17. Verifikasi susunan default tetap pada tabel: kolom `Device Name`, `Serial Number`, `Status`, `Registered At`, `Registered By`, `Min Power`, `Max Power`, `Current Power` dengan urutan awal

### TC-AC-ACHS-303: Tutup popup via (X) atau Esc membuang perubahan

18. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
19. Hilangkan centang `Status`, klik `[✕]`
20. Verifikasi kolom `Status` tetap tampil pada tabel (konfigurasi tersimpan terakhir)
21. Verifikasi tidak ada dialog Unsaved Changes
22. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
23. Verifikasi checkbox `Status` pada popup tercentang (perubahan preview dibuang)
24. Drag `Current Power` ke posisi pertama pada popup, tekan Esc
25. Verifikasi urutan kolom tabel tidak berubah (`Device Name` tetap pertama)
26. Verifikasi tidak ada dialog Unsaved Changes

### TC-AC-ACHS-304: Kolom visible terakhir tidak bisa di-uncheck

27. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
28. Untuk setiap baris tabel Data uji TC-AC-ACHS-304 (langkah 28): hilangkan centang kolom di popup
29. Arahkan kursor ke checkbox kolom tersisa `Current Power`
30. Verifikasi checkbox `Current Power` disabled dan tidak bisa di-uncheck
31. Verifikasi tooltip `At least one column must remain visible.`
32. Klik `[✕]` untuk menutup popup tanpa menyimpan
33. Klik header kolom Actions `(⋯)`
34. Untuk setiap baris tabel Data uji TC-AC-ACHS-304 (langkah 34): hilangkan centang kolom di overlay Column Visibility
35. Arahkan kursor ke checkbox kolom tersisa `Current Power` pada overlay
36. Verifikasi checkbox `Current Power` pada overlay disabled dan tidak bisa di-uncheck
37. Verifikasi tooltip `At least one column must remain visible.` pada overlay
38. Untuk setiap baris tabel Data uji TC-AC-ACHS-304 (langkah 38): ceklis kembali kolom di overlay Column Visibility
39. Tutup overlay Column Visibility


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Urutan TC: 301, 302, 303, lalu 304. Setelah `[Reset to Default]` dan `[Save]` pada TC-AC-ACHS-302 preferensi berupa susunan default yang tersimpan.
- Langkah 28, 34, dan 38 berulang untuk setiap baris tabel Data uji (tujuh iterasi masing-masing; bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pastikan Tab Available aktif", penutupan popup (`[✕]`), pemulihan kolom di overlay (langkah 38), dan pemulihan lewat `[Reset to Default]` lalu `[Save]` (aksi sisi klien, tanpa "Tunggu aksi selesai").
- Spec memiliki 39 langkah nominal dan 57 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Setup Column Tab Available pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-302 dan TC-AC-ACHS-303 menulis "satu kolom" dan "mengubah urutan" tanpa nama kolom; spec memilih kolom (Prerequisites). TC-AC-ACHS-304 tidak menyebut kolom yang tersisa; spec menyisakan `Current Power`.
  - TC-AC-ACHS-304 Expected c ("Panel cepat Column Visibility berperilaku sama") tidak menyebut apakah perubahan overlay langsung berlaku; spec memulihkan dengan ceklis ulang di overlay (langkah 38) dan menutup overlay.
