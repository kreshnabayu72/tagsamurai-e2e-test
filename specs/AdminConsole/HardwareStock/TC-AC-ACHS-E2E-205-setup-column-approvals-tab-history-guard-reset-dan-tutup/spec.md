---
id: TC-AC-ACHS-E2E-205-setup-column-approvals-tab-history-guard-reset-dan-tutup
title: "Setup Column Approvals > Hardware Stock Tab History: Guard, Reset, dan Tutup Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-451
  - TC-AC-ACHS-452
  - TC-AC-ACHS-453
  - TC-AC-ACHS-454
coverage:
  web: automated
---

# Setup Column Approvals > Hardware Stock Tab History: Guard, Reset, dan Tutup Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column di browser (hook `after` suite).
- State global: konfigurasi Setup Column Tab History disimpan spec ini (langkah 20, 47, 56) dan dihapus hook `after`; spec memulihkannya ke susunan default pada langkah 55 dan 56. Suite serial: `parallel: false` (lihat suite.md).
- Susunan default kolom: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At.

## Test Steps

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`

### TC-AC-ACHS-451: Pin ke-4 disabled setelah 3 kolom di-pin

3. Klik header kolom Actions `(⋯)`
4. Klik `Setup Column...`
5. Klik icon Pin pada Type
6. Klik icon Pin pada Device Name (SKU)
7. Klik icon Pin pada Category
8. Hover icon Pin pada kolom Matched Identifier
9. Verifikasi icon Pin kolom Matched Identifier disabled dan tidak membekukan kolom
10. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
11. Klik icon Pin pada Category (unpin)
12. Verifikasi icon Pin kolom Matched Identifier aktif kembali
13. Klik `[✕]`

### TC-AC-ACHS-452: Reset to Default lalu Save mengembalikan susunan awal

14. Klik header kolom Actions `(⋯)`
15. Klik `Setup Column...`
16. Uncheck Category
17. Drag Resolved At ke posisi paling kiri
18. Klik `[Reset to Default]`
19. Verifikasi Live Preview kembali ke susunan default: kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At checked dengan urutan awal
20. Klik `[Save]`
21. Refresh browser (F5)
22. Klik Tab `History`
23. Verifikasi susunan default tetap setelah Save dan F5: header kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At dengan urutan awal

### TC-AC-ACHS-453: Tutup popup via (X) membuang perubahan

24. Klik header kolom Actions `(⋯)`
25. Klik `Setup Column...`
26. Uncheck Category
27. Klik `[✕]`
28. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom Category tampil)
29. Verifikasi tidak ada dialog Unsaved Changes
30. Klik header kolom Actions `(⋯)`
31. Klik `Setup Column...`
32. Verifikasi Live Preview menampilkan konfigurasi tersimpan (Category checked), perubahan sebelumnya dibuang
33. Drag Resolved At ke posisi paling kiri
34. Tekan `Esc`
35. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (Type di posisi pertama)
36. Verifikasi tidak ada dialog Unsaved Changes
37. Klik header kolom Actions `(⋯)`
38. Klik `Setup Column...`
39. Verifikasi Live Preview menampilkan urutan tersimpan (Type di posisi pertama), perubahan urutan dibuang
40. Klik `[✕]`

### TC-AC-ACHS-454: Kolom visible terakhir tidak bisa di-uncheck

41. Klik header kolom Actions `(⋯)`
42. Klik `Setup Column...`
43. Uncheck satu per satu kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, dan Requested At
44. Hover checkbox kolom Resolved At
45. Verifikasi checkbox kolom Resolved At disabled dan tidak bisa di-uncheck
46. Verifikasi tooltip `At least one column must remain visible.`
47. Klik `[Save]`
48. Klik header kolom Actions `(⋯)`
49. Hover checkbox kolom Resolved At pada panel `Column Visibility`
50. Verifikasi checkbox kolom Resolved At pada panel `Column Visibility` disabled
51. Verifikasi tooltip `At least one column must remain visible.` pada panel `Column Visibility`
52. Tutup panel dengan `Esc`
53. Klik header kolom Actions `(⋯)`
54. Klik `Setup Column...`
55. Klik `[Reset to Default]`
56. Klik `[Save]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-451 sampai 454). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (bukan dari langkah TC): langkah 13 (menutup popup dengan `[✕]` sehingga pin tidak tersimpan), langkah 22 (membuka kembali Tab `History` setelah F5), langkah 40 (menutup popup), langkah 47 sampai 52 (menyimpan satu kolom visible supaya panel `Column Visibility` dapat diamati, untuk Expected c TC-454), langkah 53 sampai 56 (memulihkan susunan default; bukan penghapusan preferensi, yang dikerjakan hook `after`).
- Langkah 16 dan 17 (TC-452 langkah 3: "uncheck satu kolom dan geser satu kolom") memilih Category dan Resolved At; langkah 33 (TC-453 "mengubah urutan") memilih Resolved At.
- Spec ini di atas 35 langkah (56 langkah nominal). Alasan: empat TC berbagi satu popup Setup Column dan satu tabel read-only (Tab History); tiap TC berdiri sendiri karena popup ditutup dan susunan kolom dipulihkan di antaranya, dan topik Setup Column satu dataset digabung sesuai prinsip 1.
- Temuan untuk QA:
  - TC-454 Expected c ("Panel cepat `Column Visibility` berperilaku sama") tidak punya langkah di TC; popup yang ditutup tanpa Save membuang perubahan, sehingga spec menyimpan satu kolom lalu mengamati panel (langkah 47 sampai 51).
  - TC-453 Expected b ("perubahan preview dibuang") tidak punya langkah observasi; spec membuka kembali popup untuk mengamati Live Preview (langkah 30 sampai 32 dan 37 sampai 39).
  - TC-451 butir c ("Setelah satu kolom di-unpin, icon Pin kolom lain aktif kembali") tidak menyebut kolom yang di-unpin; spec memakai Category.
  - TC-451 tidak menyebut Save; popup ditutup dengan `[✕]` sehingga pin tidak tersimpan.
