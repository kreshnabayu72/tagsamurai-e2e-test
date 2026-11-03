---
id: TC-AC-ACHS-E2E-225-setup-column-popup-event-log-guard-reset-dan-tutup
title: "Setup Column Popup Event Log: Guard, Reset, dan Tutup Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-499
  - TC-AC-ACHS-500
  - TC-AC-ACHS-501
  - TC-AC-ACHS-502
coverage:
  web: automated
---

# Setup Column Popup Event Log: Guard, Reset, dan Tutup Popup

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
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column di browser (hook `after` suite).
- State global: konfigurasi Setup Column popup Event Log disimpan spec ini (langkah 21, 50, 59) dan dihapus hook `after`; spec memulihkannya ke susunan default pada langkah 58 dan 59. Suite serial: `parallel: false` (lihat suite.md).
- Susunan default kolom: Date, Activity, Success, Waiting for Approval, Modified By.

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab `Available` aktif
3. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-499: Pin ke-4 disabled setelah 3 kolom di-pin

4. Klik header kolom Actions `(⋯)`
5. Klik `Setup Column...`
6. Klik icon Pin pada Date
7. Klik icon Pin pada Activity
8. Klik icon Pin pada Success
9. Hover icon Pin pada kolom Modified By
10. Verifikasi icon Pin kolom Modified By disabled dan tidak membekukan kolom
11. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
12. Klik icon Pin pada Success (unpin)
13. Verifikasi icon Pin kolom Modified By aktif kembali
14. Klik `[✕]`

### TC-AC-ACHS-500: Reset to Default lalu Save mengembalikan susunan awal

15. Klik header kolom Actions `(⋯)`
16. Klik `Setup Column...`
17. Uncheck Activity
18. Drag Modified By ke posisi paling kiri
19. Klik `[Reset to Default]`
20. Verifikasi Live Preview kembali ke susunan default: kolom Date, Activity, Success, Waiting for Approval, Modified By checked dengan urutan awal
21. Klik `[Save]`
22. Refresh browser (F5)
23. Buka Hardware > Stock, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
24. Pastikan Tab `Available` aktif
25. Klik icon `[Event Log]` di toolbar
26. Verifikasi susunan default tetap setelah Save dan F5: header kolom Date, Activity, Success, Waiting for Approval, Modified By dengan urutan awal

### TC-AC-ACHS-501: Tutup popup via (X) membuang perubahan

27. Klik header kolom Actions `(⋯)`
28. Klik `Setup Column...`
29. Uncheck Activity
30. Klik `[✕]`
31. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (kolom Activity tampil)
32. Verifikasi tidak ada dialog Unsaved Changes
33. Klik header kolom Actions `(⋯)`
34. Klik `Setup Column...`
35. Verifikasi Live Preview menampilkan konfigurasi tersimpan (Activity checked), perubahan sebelumnya dibuang
36. Drag Modified By ke posisi paling kiri
37. Tekan `Esc`
38. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (Date di posisi pertama)
39. Verifikasi tidak ada dialog Unsaved Changes
40. Klik header kolom Actions `(⋯)`
41. Klik `Setup Column...`
42. Verifikasi Live Preview menampilkan urutan tersimpan (Date di posisi pertama), perubahan urutan dibuang
43. Klik `[✕]`

### TC-AC-ACHS-502: Kolom visible terakhir tidak bisa di-uncheck

44. Klik header kolom Actions `(⋯)`
45. Klik `Setup Column...`
46. Uncheck satu per satu kolom Date, Activity, Success, dan Waiting for Approval
47. Hover checkbox kolom Modified By
48. Verifikasi checkbox kolom Modified By disabled dan tidak bisa di-uncheck
49. Verifikasi tooltip `At least one column must remain visible.`
50. Klik `[Save]`
51. Klik header kolom Actions `(⋯)`
52. Hover checkbox kolom Modified By pada panel `Column Visibility`
53. Verifikasi checkbox kolom Modified By pada panel `Column Visibility` disabled
54. Verifikasi tooltip `At least one column must remain visible.` pada panel `Column Visibility`
55. Tutup panel dengan `Esc`
56. Klik header kolom Actions `(⋯)`
57. Klik `Setup Column...`
58. Klik `[Reset to Default]`
59. Klik `[Save]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-499 sampai 502). Tidak ada TC hanya-BE di spec ini.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 14 (menutup popup dengan `[✕]` sehingga pin tidak tersimpan), langkah 23 sampai 25 (membuka kembali popup Event Log setelah F5 lewat jalur navigasi yang sama), langkah 43 (menutup popup), langkah 50 sampai 55 (menyimpan satu kolom visible supaya panel `Column Visibility` dapat diamati, untuk Expected c TC-502), langkah 56 sampai 59 (memulihkan susunan default; bukan penghapusan preferensi, yang dikerjakan hook `after`).
- Langkah 17 dan 18 (TC-500 langkah 5: "uncheck satu kolom dan geser satu kolom") memilih Activity dan Modified By; langkah 36 (TC-501 "mengubah urutan") memilih Modified By.
- Spec ini di atas 35 langkah (59 langkah nominal). Alasan: empat TC berbagi satu popup Setup Column dan satu tabel read-only (Event Log satu SKU); tiap TC berdiri sendiri karena popup ditutup dan susunan kolom dipulihkan di antaranya, dan topik Setup Column satu dataset digabung sesuai prinsip 1.
- Temuan untuk QA:
  - TC-502 Expected c ("Panel cepat `Column Visibility` berperilaku sama") tidak punya langkah di TC; popup yang ditutup tanpa Save membuang perubahan, sehingga spec menyimpan satu kolom lalu mengamati panel (langkah 50 sampai 54).
  - TC-501 Expected b ("perubahan preview dibuang") tidak punya langkah observasi; spec membuka kembali popup untuk mengamati Live Preview (langkah 33 sampai 35 dan 40 sampai 42).
  - TC-499 butir c ("Setelah satu kolom di-unpin, icon Pin kolom lain aktif kembali") tidak menyebut kolom yang di-unpin; spec memakai Success. TC-499 tidak menyebut Save; popup ditutup dengan `[✕]` sehingga pin tidak tersimpan.
  - TC tidak menyebut apakah popup Event Log terbuka kembali setelah F5; spec membuka kembali lewat navigasi dari Hardware > Stock.
