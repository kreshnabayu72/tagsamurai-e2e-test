---
id: TC-GS-GSET-E2E-042-pencatatan-changelog-dan-activity-log-multi-field-snapshot-dan-tanpa-perubahan
title: "Log multi-field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-109
  - TC-GS-GSET-111
  - TC-GS-GSET-112
coverage:
  web: automated
---

# Log multi-field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Spec tidak membuat data dinamis. Nilai yang disimpan: TC-GS-GSET-109 Date Format `dd MMM yy`, Time Format `hh:mm a`, Session Idle Timeout `2 hours` (tiga field sekaligus); TC-GS-GSET-111 Session Idle Timeout `1 hour` lalu `4 hours`.
- Baseline log (S-12), dicatat sebelum aksi pertama tiap blok: `{nCL0}` (total entri Modal Changelog) dan `{nAL0}` (total entri Activity Log dengan Search `General Settings`, sehingga hanya entri Object `General Settings`) pada langkah 1 dan 2 untuk TC-GS-GSET-109; `{nSI0}` (jumlah hasil Search `Session Idle Timeout` di Modal Changelog) pada langkah 20 untuk TC-GS-GSET-111; `{nCL1}` (total entri Modal Changelog) pada langkah 33 untuk TC-GS-GSET-112.
- Kemampuan teknis: (a) membaca jumlah total entri (total data pada Pagination) Modal Changelog dan Activity Log serta jumlah hasil Search; (b) sesi API Total Control yang memulihkan record Client A ke baseline Pre-setup No 10 lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`; klien HTTP dan penangkapan token disediakan tim FE) pada langkah 19 dan 32, dengan muat ulang halaman sesudahnya; (c) `Spectra.intercept()` pada PUT `/v2/enterprise-management/general-settings` hanya untuk menghitung request tanpa mengubah respons (TC-GS-GSET-112), dilepas segera setelah pengamatan pada langkah 38.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- State global yang diubah: field record General Settings Client A (Date Format, Time Format, Session Idle Timeout), dipulihkan lewat langkah 19 dan 32 serta hook `beforeEach` dan `after` suite. Entri Changelog dan Activity Log bersifat audit trail permanen dan tidak dihapus; pemulihan lewat API menambah entri sehingga baseline blok berikutnya dicatat sesudah pemulihan. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4).

## Test Steps

### TC-GS-GSET-109: Save tiga field sekaligus mencatat tepat tiga baris tanpa duplikat

1. Buka Modal Changelog, catat jumlah total entri sebagai `{nCL0}`, lalu tutup modal
2. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter, catat jumlah total entri sebagai `{nAL0}`, lalu buka Global Settings > General Settings
3. Pilih Date Format `dd MMM yy`, Time Format `hh:mm a`, dan Session Idle Timeout `2 hours`
4. Klik `[Save]`
5. Tunggu aksi selesai (tombol `[Save]` disabled kembali)
6. Buka Modal Changelog
7. Verifikasi jumlah total entri Changelog `{nCL0}` + 3 (tepat 3 baris baru)
8. Verifikasi di antara tiga baris teratas Changelog ada baris Action `Edit`, Field `Date Format`, Old Value `dd/MM/yy`, New Value `dd MMM yy`
9. Verifikasi di antara tiga baris teratas Changelog ada baris Action `Edit`, Field `Time Format`, Old Value `HH:mm`, New Value `hh:mm a`
10. Verifikasi di antara tiga baris teratas Changelog ada baris Action `Edit`, Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `2 hours`
11. Verifikasi tiga baris teratas Changelog tidak memuat baris Field `Currency Code` maupun `Time Zone`
12. Tutup Modal Changelog
13. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter
14. Verifikasi jumlah total entri Activity Log `{nAL0}` + 3 (tepat 3 baris baru)
15. Verifikasi di antara tiga baris teratas Activity Log ada baris Action `Edit`, Name `—`, Field `Date Format`, Old Value `dd/MM/yy`, New Value `dd MMM yy`
16. Verifikasi di antara tiga baris teratas Activity Log ada baris Action `Edit`, Name `—`, Field `Time Format`, Old Value `HH:mm`, New Value `hh:mm a`
17. Verifikasi di antara tiga baris teratas Activity Log ada baris Action `Edit`, Name `—`, Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `2 hours`
18. Buka Global Settings > General Settings
19. Pulihkan record Client A ke baseline Pre-setup No 10 lewat sesi API, lalu muat ulang halaman (F5)

### TC-GS-GSET-111: Snapshot Changelog: entri lama tidak berubah setelah perubahan berikutnya

20. Buka Modal Changelog, ketik Search `Session Idle Timeout`, tekan Enter, catat jumlah hasil sebagai `{nSI0}`, lalu tutup modal
21. Pilih Session Idle Timeout `1 hour`
22. Klik `[Save]`
23. Tunggu aksi selesai (tombol `[Save]` disabled kembali)
24. Pilih Session Idle Timeout `4 hours`
25. Klik `[Save]`
26. Tunggu aksi selesai (tombol `[Save]` disabled kembali)
27. Buka Modal Changelog, ketik Search `Session Idle Timeout`, tekan Enter
28. Verifikasi jumlah hasil Search `{nSI0}` + 2 (satu baris per Save)
29. Verifikasi baris dari Save pertama (baris kedua dari atas) tetap berisi Action `Edit`, Old Value `30 minutes`, New Value `1 hour` (tidak ter-overwrite)
30. Verifikasi baris Save kedua (baris teratas) berisi Action `Edit`, Old Value `1 hour`, New Value `4 hours`
31. Tutup Modal Changelog
32. Pulihkan record Client A ke baseline Pre-setup No 10 lewat sesi API, lalu muat ulang halaman (F5)

### TC-GS-GSET-112: Save tanpa perubahan tidak menghasilkan baris log

33. Buka Modal Changelog, catat jumlah total entri sebagai `{nCL1}`, lalu tutup modal
34. Pasang penghitung request PUT `/v2/enterprise-management/general-settings` (tanpa mengubah respons)
35. Verifikasi tombol `[Save]` disabled
36. Klik tombol `[Save]`
37. Verifikasi tidak ada request PUT yang terkirim (hitungan request 0)
38. Lepas penghitung request PUT
39. Buka Modal Changelog
40. Verifikasi jumlah total entri Changelog sama dengan `{nCL1}`
41. Tutup Modal Changelog

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-109, TC-GS-GSET-111, TC-GS-GSET-112). Mode: FE+BE. Kelas: pencatatan log (presence); asersi jumlah berbaseline, bukan kelas g (prinsip 13 butir g, paragraf akhir).
- Ukuran: 41 langkah nominal. Blok baca-log berpola (langkah 6 sampai 17, 20, dan 27 sampai 31) berjumlah 18 langkah dan tidak dihitung ke batas sekitar 35 langkah (prinsip 13, bagian smell); sisanya 23 langkah. Ketiga blok berdiri sendiri, satu kelas, dan tiap blok memulihkan baseline sendiri.
- Dipisah dari spec 041 karena gabungan langkahnya melewati batas ukuran (41 + 58 = 99 langkah dengan ekspansi; 41 langkah setelah blok baca-log berpola dikecualikan, di atas batas sekitar 35).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 6, 12, 13, 18 sampai 20, 27, 31 sampai 34, 38, 39, dan 41 (membuka, menutup, dan mencari di surface log, serta memulihkan baseline); langkah 5, 23, dan 26 (tunggu Save selesai sebelum membuka surface lain).
- Pemulihan baseline di antara blok (langkah 19 dan 32) memenuhi precondition TC-GS-GSET-111 dan TC-GS-GSET-112 (record baseline Pre-setup No 10). Pemulihan itu aksi tanpa `Verifikasi` dan menambah entri log, sehingga baseline blok berikutnya dicatat sesudahnya (langkah 20 dan 33).
- Asersi TC-GS-GSET-111 memakai hasil Search `Session Idle Timeout` dan selisih terhadap `{nSI0}`, bukan posisi baris absolut; urutan baris teratas ke bawah mengikuti urutan Date terbaru lebih dulu (default Modal Changelog).
- Pada TC-GS-GSET-109 urutan ketiga baris baru tidak diasersi karena TC tidak menyebutnya; `Verifikasi` memeriksa keberadaan tiap baris di antara tiga baris teratas.
- Dependensi TC-GS-GSET-109, 111, dan 112 adalah "-" pada TC; tidak ada langkah dependensi yang dirujuk.
- Temuan untuk QA:
  - TC-GS-GSET-109 Expected a menulis "tepat 3 baris baru" tanpa urutan dan Expected b tanpa kolom Modified By; spec tidak mengasersi keduanya.
  - TC-GS-GSET-112 Expected a ("klik tidak mengirim request") membutuhkan penghitung request; kemampuan itu ditulis di Prerequisites (butir c) dan disediakan tim FE.
