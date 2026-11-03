---
id: TC-AC-ACHS-E2E-204-column-visibility-dan-setup-column-approvals-tab-history
title: "Column Visibility dan Setup Column Approvals > Hardware Stock Tab History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-446
  - TC-AC-ACHS-447
  - TC-AC-ACHS-448
  - TC-AC-ACHS-449
  - TC-AC-ACHS-450
coverage:
  web: automated
---

# Column Visibility dan Setup Column Approvals > Hardware Stock Tab History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column di browser (hook `after` suite; konfigurasi kolom disimpan di `localStorage` menurut TC-448) dan mengatur lebar viewport browser supaya tabel Tab History dapat di-scroll horizontal (langkah 47, 51, 57); viewport dipulihkan di hook `after`.
- State global: konfigurasi Setup Column Tab History disimpan spec ini (langkah 23, 32, 38, 46, 56) dan dihapus hook `after`. Suite serial: `parallel: false` (lihat suite.md).
- Parameter Kolom (langkah 18 sampai 21), urutan default: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At.
- Parameter Drag (langkah 36 sampai 37), urutan iterasi dari kolom paling kanan ke paling kiri: Resolved At, Requested At, Approver, Approval, Requested By, Existing Record, Matched Identifier, Category, Device Name (SKU), Type. Iterasi terakhir menempatkan Type di posisi pertama.

## Test Steps

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`

### TC-AC-ACHS-446: Screening overlay Column Visibility

3. Hover header kolom Actions `(⋯)`
4. Verifikasi tooltip `Column Visibility`
5. Klik header kolom Actions `(⋯)`
6. Verifikasi overlay memuat kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At dengan checkbox berstatus checked dan enabled (Hideable)
7. Verifikasi overlay memuat drag handle
8. Verifikasi item `Setup Column...` di bagian bawah overlay
9. Tutup overlay dengan `Esc`

### TC-AC-ACHS-447: Screening popup Setup Column (3 zona) dan Live Preview

10. Klik header kolom Actions `(⋯)`
11. Klik `Setup Column...`
12. Verifikasi Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol close `[✕]`
13. Verifikasi Body memuat daftar kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At dengan checkbox checked (Hideable), drag handle, dan icon Pin
14. Verifikasi Body memuat Live Preview urutan header
15. Verifikasi Footer: `[Reset to Default]` dan `[Save]` rata kanan
16. Verifikasi Footer tidak memuat `[Cancel]`

### TC-AC-ACHS-448: Setup Column kelas data, uncheck dan check per kolom, Save, persist F5

17. Untuk setiap baris tabel Parameter Kolom (10 kolom), lakukan langkah 18 sampai 21
18. Uncheck kolom tersebut
19. Verifikasi kolom tersebut hilang dari Live Preview
20. Check kolom tersebut kembali
21. Verifikasi kolom tersebut muncul kembali di Live Preview
22. Uncheck `Type`
23. Klik `[Save]`
24. Verifikasi kolom Type tidak tampil di tabel
25. Refresh browser (F5)
26. Klik Tab `History`
27. Verifikasi header kolom Device Name (SKU) tampil
28. Verifikasi kolom Type tetap tidak tampil (tersimpan di `localStorage`)
29. Klik header kolom Actions `(⋯)`
30. Klik `Setup Column...`
31. Check `Type`
32. Klik `[Save]`

### TC-AC-ACHS-449: Setup Column kelas data, drag reorder, Save, persist F5

33. Klik header kolom Actions `(⋯)`
34. Klik `Setup Column...`
35. Untuk setiap baris tabel Parameter Drag (10 kolom), lakukan langkah 36 sampai 37
36. Drag kolom tersebut ke posisi paling kiri
37. Verifikasi Live Preview menampilkan kolom tersebut di posisi pertama
38. Klik `[Save]`
39. Verifikasi tabel menampilkan Type di posisi pertama
40. Refresh browser (F5)
41. Klik Tab `History`
42. Verifikasi urutan kolom tetap, Type di posisi pertama

### TC-AC-ACHS-450: Setup Column kelas data, pin dan unpin, kolom membeku saat scroll horizontal

43. Klik header kolom Actions `(⋯)`
44. Klik `Setup Column...`
45. Klik icon Pin pada Type
46. Klik `[Save]`
47. Scroll tabel horizontal
48. Verifikasi kolom Type membeku di kiri saat scroll horizontal
49. Refresh browser (F5)
50. Klik Tab `History`
51. Scroll tabel horizontal
52. Verifikasi kolom Type tetap membeku di kiri setelah F5
53. Klik header kolom Actions `(⋯)`
54. Klik `Setup Column...`
55. Klik icon Pin pada Type (unpin)
56. Klik `[Save]`
57. Scroll tabel horizontal
58. Verifikasi kolom Type ikut bergeser saat scroll setelah unpin

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-446 sampai 450). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (bukan dari langkah TC): langkah 9 (menutup overlay), langkah 26, 41, 50 (membuka kembali Tab `History` setelah muat ulang karena TC tidak menyebut tab aktif setelah F5), langkah 27 (anchor positif untuk asersi absence kolom Type, bagian 8b butir 2), langkah 29 sampai 32 (memulihkan kolom Type; bukan `[Reset to Default]` karena itu objek TC-452 di spec lain), langkah 47, 51, 57 (scroll horizontal sebelum asersi).
- Langkah berulang: langkah 18 sampai 21 (10 iterasi) dan langkah 36 sampai 37 (10 iterasi).
- Spec ini di atas 35 langkah dengan ekspansi blok ulang (10 iterasi kali 4 langkah ditambah 10 iterasi kali 2 langkah). Alasan: seluruh blok memakai satu popup Setup Column dan satu tabel read-only, tiap blok berdiri sendiri, dan topik Column Visibility dan Setup Column satu dataset digabung sesuai prinsip 1.
- Pasangan TC-AC-ACHS-452 sampai 454 (guard, reset, tutup) ada di spec 205.
- Temuan untuk QA:
  - TC-449 meminta Type di-drag ke posisi paling kiri padahal Type sudah di posisi pertama pada susunan default; spec men-drag setiap kolom ke kiri dengan urutan dari kolom paling kanan sehingga Type berakhir di posisi pertama.
  - TC-450 meminta pin hanya pada Type, yang sudah kolom paling kiri; pembekuan teramati lewat scroll horizontal dan kemampuan mengatur viewport diminta dari tim FE.
  - TC tidak menyebut tab aktif sesudah F5 pada Tab History; spec membuka kembali tab itu secara eksplisit.
  - Penyimpanan di `localStorage` pada TC-448 butir c adalah pernyataan implementasi; spec hanya mengamati kolom tetap tidak tampil setelah F5.
