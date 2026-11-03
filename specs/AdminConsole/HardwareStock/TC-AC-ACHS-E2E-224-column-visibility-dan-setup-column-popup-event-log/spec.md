---
id: TC-AC-ACHS-E2E-224-column-visibility-dan-setup-column-popup-event-log
title: "Column Visibility dan Setup Column Popup Event Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-494
  - TC-AC-ACHS-495
  - TC-AC-ACHS-496
  - TC-AC-ACHS-497
  - TC-AC-ACHS-498
coverage:
  web: automated
---

# Column Visibility dan Setup Column Popup Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki tepat 12 sesi Event Log; baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40); pemilik Event Log Pre-setup #20 | `Fixture.hardwareStock.p16.a[4].sku` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column di browser (hook `after` suite; konfigurasi kolom disimpan di `localStorage` menurut TC-496) dan mengatur lebar viewport browser supaya tabel popup Event Log dapat di-scroll horizontal (langkah 52, 58, 64); viewport dipulihkan di hook `after`.
- State global: konfigurasi Setup Column popup Event Log disimpan spec ini (langkah 24, 35, 41, 51, 63) dan dihapus hook `after`. Suite serial: `parallel: false` (lihat suite.md).
- Parameter Kolom (langkah 19 sampai 22), urutan default: Date, Activity, Success, Waiting for Approval, Modified By.
- Parameter Drag (langkah 39 sampai 40), urutan iterasi dari kolom paling kanan ke paling kiri: Modified By, Waiting for Approval, Success, Activity, Date. Iterasi terakhir menempatkan Date di posisi pertama.

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab `Available` aktif
3. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-494: Screening overlay Column Visibility

4. Hover header kolom Actions `(⋯)`
5. Verifikasi tooltip `Column Visibility`
6. Klik header kolom Actions `(⋯)`
7. Verifikasi overlay memuat kolom Date, Activity, Success, Waiting for Approval, Modified By dengan checkbox berstatus checked dan enabled (Hideable)
8. Verifikasi overlay memuat drag handle
9. Verifikasi item `Setup Column...` di bagian bawah overlay
10. Tutup overlay dengan `Esc`

### TC-AC-ACHS-495: Screening popup Setup Column (3 zona) dan Live Preview

11. Klik header kolom Actions `(⋯)`
12. Klik `Setup Column...`
13. Verifikasi Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol close `[✕]`
14. Verifikasi Body memuat daftar kolom Date, Activity, Success, Waiting for Approval, Modified By dengan checkbox checked (Hideable), drag handle, dan icon Pin
15. Verifikasi Body memuat Live Preview urutan header
16. Verifikasi Footer: `[Reset to Default]` dan `[Save]` rata kanan
17. Verifikasi Footer tidak memuat `[Cancel]`

### TC-AC-ACHS-496: Setup Column kelas data, uncheck dan check per kolom, Save, persist F5

18. Untuk setiap baris tabel Parameter Kolom (5 kolom), lakukan langkah 19 sampai 22
19. Uncheck kolom tersebut
20. Verifikasi kolom tersebut hilang dari Live Preview
21. Check kolom tersebut kembali
22. Verifikasi kolom tersebut muncul kembali di Live Preview
23. Uncheck `Date`
24. Klik `[Save]`
25. Verifikasi kolom Date tidak tampil di tabel
26. Refresh browser (F5)
27. Buka Hardware > Stock, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
28. Pastikan Tab `Available` aktif
29. Klik icon `[Event Log]` di toolbar
30. Verifikasi header kolom Activity tampil
31. Verifikasi kolom Date tetap tidak tampil (tersimpan di `localStorage`)
32. Klik header kolom Actions `(⋯)`
33. Klik `Setup Column...`
34. Check `Date`
35. Klik `[Save]`

### TC-AC-ACHS-497: Setup Column kelas data, drag reorder, Save, persist F5

36. Klik header kolom Actions `(⋯)`
37. Klik `Setup Column...`
38. Untuk setiap baris tabel Parameter Drag (5 kolom), lakukan langkah 39 sampai 40
39. Drag kolom tersebut ke posisi paling kiri
40. Verifikasi Live Preview menampilkan kolom tersebut di posisi pertama
41. Klik `[Save]`
42. Verifikasi tabel menampilkan Date di posisi pertama
43. Refresh browser (F5)
44. Buka Hardware > Stock, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
45. Pastikan Tab `Available` aktif
46. Klik icon `[Event Log]` di toolbar
47. Verifikasi urutan kolom tetap, Date di posisi pertama

### TC-AC-ACHS-498: Setup Column kelas data, pin dan unpin, kolom membeku saat scroll horizontal

48. Klik header kolom Actions `(⋯)`
49. Klik `Setup Column...`
50. Klik icon Pin pada Date
51. Klik `[Save]`
52. Scroll tabel horizontal
53. Verifikasi kolom Date membeku di kiri saat scroll horizontal
54. Refresh browser (F5)
55. Buka Hardware > Stock, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
56. Pastikan Tab `Available` aktif
57. Klik icon `[Event Log]` di toolbar
58. Scroll tabel horizontal
59. Verifikasi kolom Date tetap membeku di kiri setelah F5
60. Klik header kolom Actions `(⋯)`
61. Klik `Setup Column...`
62. Klik icon Pin pada Date (unpin)
63. Klik `[Save]`
64. Scroll tabel horizontal
65. Verifikasi kolom Date ikut bergeser saat scroll setelah unpin

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-494 sampai 498). Tidak ada TC hanya-BE di spec ini.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 10 (menutup overlay), langkah 27 sampai 29, 44 sampai 46, dan 55 sampai 57 (membuka kembali popup Event Log setelah F5 lewat jalur navigasi yang sama), langkah 30 (anchor positif untuk asersi absence kolom Date, bagian 8b butir 2), langkah 32 sampai 35 (memulihkan kolom Date; bukan `[Reset to Default]` karena itu objek TC-500 di spec lain), langkah 52, 58, 64 (scroll horizontal sebelum asersi).
- Langkah berulang: langkah 19 sampai 22 (5 iterasi) dan langkah 39 sampai 40 (5 iterasi).
- Spec ini di atas 35 langkah (65 langkah nominal). Alasan: seluruh blok memakai satu popup Setup Column dan satu tabel read-only, tiap blok berdiri sendiri, dan topik Column Visibility dan Setup Column satu dataset digabung sesuai prinsip 1.
- Pasangan TC-AC-ACHS-499 sampai 502 (guard, reset, tutup) ada di spec 225.
- Temuan untuk QA:
  - TC-497 meminta Date di-drag ke posisi paling kiri padahal Date sudah di posisi pertama pada susunan default; spec men-drag setiap kolom ke kiri dengan urutan dari kolom paling kanan sehingga Date berakhir di posisi pertama.
  - TC-498 meminta pin hanya pada Date, yang sudah kolom paling kiri; pembekuan teramati lewat scroll horizontal dan kemampuan mengatur viewport diminta dari tim FE.
  - TC tidak menyebut apakah popup Event Log terbuka kembali setelah F5; spec membuka kembali lewat navigasi dari Hardware > Stock.
  - Penyimpanan di `localStorage` pada TC-496 butir c adalah pernyataan implementasi; spec hanya mengamati kolom tetap tidak tampil setelah F5.
