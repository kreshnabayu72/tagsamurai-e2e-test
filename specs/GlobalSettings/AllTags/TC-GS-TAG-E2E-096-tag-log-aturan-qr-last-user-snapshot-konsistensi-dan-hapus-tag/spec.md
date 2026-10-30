---
id: TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag
title: "TAG Log: Log QR, Delete dan Scan Tidak Masuk Log, Log Ikut Terhapus, Snapshot Nama Entitas, Last User, Konsistensi Status, dan Log To be Returned Hanya RFID dan NFC"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-287
  - TC-GS-TAG-288
  - TC-GS-TAG-289
  - TC-GS-TAG-290
  - TC-GS-TAG-291
  - TC-GS-TAG-292
  - TC-GS-TAG-377
coverage:
  web: automated
---

# TAG Log: Log QR, Delete dan Scan Tidak Masuk Log, Log Ikut Terhapus, Snapshot Nama Entitas, Last User, Konsistensi Status, dan Log To be Returned Hanya RFID dan NFC

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Client Log Wulan Sari `totalControl_automated_qaLog@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_LOG_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Login sekali di hook `before` spec ini.
- Akun kedua (langkah 22 sampai 23): Total Control Client A Sari Dewi (`Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`). Hook `after` mengembalikan sesi ke akun ini (akun default suite).
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Admin FAMS memicu langkah 35, 42, dan 46.
- Pelaku pemicu FAMS (TC-292 dan TC-377; pelaku kedua yang hanya memicu perubahan state, sesi API): Admin FAMS Hendra Gunawan `famsAdmin_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.FA_ADMIN_PASSWORD` (terdaftar di `.env.example`). Langkah FAMS dijalankan lewat sesi API ("hingga ... tersimpan"); endpoint dan langkah Register Asset, pair, disposal, dan Receive TAG di FAMS tidak didefinisikan di TC dan disediakan tim FE (Q-9, S-13). Akun pelaku Supply Asset, Return Group, dan penggantian nama aset di luar Pre-setup TC (Q-15).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` untuk kedua akun mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All. Pengaturan Setup Column kolom `Last User` (langkah 9 sampai 10) adalah state browser dan disembunyikan kembali pada langkah 21; hook `after` memulihkannya sebagai cadangan dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; kolom `Last User` kembali Hidden).
- Hook `after` suite memulihkan Seed Registri A dan fixture TAG Log secara idempotent (pernyataan hook di `suite.md`).
- Data Pre-setup (dipulihkan ke kondisi awal oleh hook `before` dan pada langkah 24 lewat fixture BE; mekanisme disediakan tim FE/BE, lihat Temuan untuk QA):
  - Client Log (fixture TAG Log): DD-55 `TAG-QR-LOG-055` (QR, Paired, entri pertama dan satu-satunya `Paired` ke Asset); DD-43 `E2801160600002054D8C0043` (RFID Object, Paired ke Asset `Forklift 01`, `AST-0043`; aset kemudian di-rename setelah pair); DD-42 `E2801160600002054D8C0042` (`Reserved` oleh Siti Amalia, `Released` oleh approver); DD-41 `04A224B2C15F41` (hanya `Waiting for Approval` dan `Approved`); DD-50 `E2801160600002054D8C0050` (`Received` oleh Rina Wulandari, user FAMS penerima).
  - Client A (Seed Registri A): DD-02 `E2801160600002054D8A0002` (RFID User TAG, Self-Purchased, Available; satu entri TAG Log `Activated` 09/09/26 09:15 oleh Siti Amalia); DD-15 `E28011606000020F00000001` (RFID, Available, tanpa entri TAG Log); DD-07 (RFID, To be Returned); DD-13 `04A224B2C15E83` (NFC, Self-Purchased, Available; disetel `Paired` ke aset FAMS lewat fixture BE dengan relasi combined dengan DD-11 dilepas pada langkah 41); DD-04 `AABBCCDDEE80` (BLE), DD-09 `356938035643501` (GPS), DD-05 `TAG-QR-00512` (QR, Paired).
- Kemampuan teknis (disediakan tim FE): simulasi pemindai RFID untuk Search by Scan dan aktivasi ulang (klik pemicu scan, pindai kode, `Stop` pada Floating Status Widget sebelum menyentuh kontrol halaman lain; page-lock sesi scan, NC-43; label TC `Manual Only — (b)` bukan alasan mengeluarkan TC, keputusan D-4, Q-1); sesi API admin FAMS sebagai pemicu; pembaca nilai kolom registri.
- Opsi mandiri (BYO) aktif untuk Client A (diperlukan agar DD-02 dapat diaktivasi ulang sebagai Self-Purchased pada langkah 65).
- Nilai Template Self-Purchased untuk aktivasi ulang DD-02 (langkah 65) disediakan tim FE sebagai fixture, karena `E2801160600002054D8A0002` bukan stok resmi dan TC tidak menyebut Template (lihat Temuan untuk QA).
- State global yang diubah: data (Seed Registri A, registri Client A, TAG Log) dan Setup Column kolom `Last User`; tidak ada state tenant.

## Test Steps

### TC-GS-TAG-287: Log QR dimulai dari Pair dan tidak punya event Activated, Waiting for Approval, Approved, atau Audit

1. Klik Tab Paired, ketik Search `TAG-QR-LOG-055`, tekan Enter, buka menu baris DD-55, klik `TAG Log`
2. Verifikasi entri pertama (paling lama) pada TAG Log DD-55 adalah `TAG Paired by`
3. Verifikasi tidak ada entri `Activated`, `Waiting for Approval`, `Approved`, maupun `Audit` pada TAG Log DD-55
4. Tutup popup lewat `[✕]`

### TC-GS-TAG-290: Nama entitas pada Paired dan Unpaired adalah snapshot saat kejadian

5. Klik Tab All, ketik Search `E2801160600002054D8C0043`, tekan Enter, buka menu baris DD-43, klik `TAG Log`
6. Verifikasi entri `Paired` DD-43 menampilkan nama aset dan kode saat kejadian (`Forklift 01`, `AST-0043`), bukan nama aset terbaru setelah di-rename
7. Verifikasi entri `Paired` DD-43 tidak memuat tautan ke modul lain
8. Tutup popup lewat `[✕]`

### TC-GS-TAG-291: Last User dihitung dari entri aksi terbaru, event administratif tidak dihitung

9. Klik `(←)` pada kotak Search, buka Setup Column lewat ikon (⋯) di header kolom Actions dan item `Setup Column...`
10. Centang kolom `Last User`, klik `Save`
11. Ketik Search `E2801160600002054D8C0042`, tekan Enter
12. Verifikasi Last User baris DD-42 `Siti A` (entri `Released` tidak dihitung)
13. Ganti isi kotak search dengan `04A224B2C15F41`, tekan Enter
14. Verifikasi Last User baris DD-41 `—` (entri `Waiting for Approval` dan `Approved` tidak dihitung)
15. Ganti isi kotak search dengan `E2801160600002054D8C0050`, tekan Enter
16. Verifikasi Last User baris DD-50 `Rina W` (entri `Received` oleh user FAMS penerima dihitung sebagai aksi)
17. Buka menu baris DD-50, klik `TAG Log`, lalu tutup popup lewat `[✕]`
18. Ganti isi kotak search dengan `04A224B2C15F41`, tekan Enter, buka menu baris DD-41, klik `TAG Log`, lalu tutup popup lewat `[✕]`
19. Ganti isi kotak search dengan `E2801160600002054D8C0042`, tekan Enter, buka menu baris DD-42, klik `TAG Log`, lalu tutup popup lewat `[✕]`
20. Klik `(←)` pada kotak Search
21. Buka Setup Column lewat ikon (⋯) di header kolom Actions dan item `Setup Column...`, hapus centang kolom `Last User`, lalu klik `Save`

### Ganti akun ke Client A

22. Klik avatar akun, pilih `Logout`
23. Login sebagai Total Control Client A Sari Dewi (`Spectra.env.GS_TC_PASSWORD`)
24. Pulihkan Seed Registri A dan fixture TAG Log Client A lewat fixture BE ke kondisi awal

### TC-GS-TAG-288: Delete dan pemindaian biasa tidak masuk TAG Log, entri tidak dapat diubah atau dihapus dari UI

25. Buka Global Settings > TAG, Tab All, ketik Search `E2801160600002054D8A0002`, tekan Enter, buka menu baris DD-02, klik `TAG Log`
26. Verifikasi TAG Log DD-02 memuat entri `TAG Activated by Siti A`
27. Catat jumlah entri `L0` pada TAG Log DD-02
28. Tutup popup lewat `[✕]`, klik `Search by Scan`, pilih teknologi `RFID` pada overlay, pindai `E2801160600002054D8A0002`, lalu klik `Stop` pada Floating Status Widget
29. Buka menu baris DD-02, klik `TAG Log`
30. Verifikasi jumlah entri TAG Log DD-02 sama dengan `L0` (tidak ada entri baru untuk Search by Scan)
31. Verifikasi tidak ada kontrol edit atau hapus pada entri TAG Log DD-02
32. Tutup popup lewat `[✕]`

### TC-GS-TAG-292: Status tag dan TAG Log tidak berselisih setelah perubahan lintas modul

33. Ganti isi kotak search dengan `E28011606000020F00000001`, tekan Enter, buka menu baris DD-15, klik `TAG Log`
34. Tutup popup lewat `[✕]`
35. Pemicu (sesi API Admin FAMS): di FAMS pindai tag DD-15 dan pair ke aset hingga tersimpan
36. Tunggu aksi selesai
37. Verifikasi Status baris DD-15 di registri `Paired`
38. Buka menu baris DD-15, klik `TAG Log`
39. Verifikasi TAG Log DD-15 memuat entri `TAG Paired by` pelaku pair

### TC-GS-TAG-377: Entri TAG Log To be Returned dan Received hanya ada pada tag RFID dan NFC

40. Tutup popup lewat `[✕]`, klik `(←)` pada kotak Search
41. Siapkan lewat fixture BE: DD-13 (`04A224B2C15E83`) `Paired` ke aset FAMS dan relasi combined dengan DD-11 dilepas
42. Pemicu (sesi API Admin FAMS): di FAMS selesaikan disposal aset bertag NFC DD-13 hingga tersimpan
43. Tunggu aksi selesai, lalu tanpa muat ulang pasang filter `Status` = `To be Returned` di Tab All
44. Verifikasi hasil filter memuat tepat dua baris: DD-07 (RFID) dan DD-13 (NFC) berstatus `To be Returned`
45. Verifikasi tidak ada baris BLE, GPS, maupun QR berstatus `To be Returned`
46. Pemicu (sesi API Admin FAMS): di FAMS terima tag DD-13 lewat `Receive TAG` (pemindaian) hingga tersimpan
47. Tunggu aksi selesai, lalu hapus chip filter `Status`, ketik Search `04A224B2C15E83`, tekan Enter
48. Buka menu baris DD-13, klik `TAG Log`
49. Verifikasi TAG Log DD-13 memuat entri `TAG Marked To be Returned by` pelaku disposal
50. Verifikasi TAG Log DD-13 memuat entri `TAG Received by` pelaku user FAMS yang menerima dengan `Previous Status: To be Returned → Available`
51. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `AABBCCDDEE80`, tekan Enter, buka menu baris DD-04, klik `TAG Log`
52. Verifikasi popup `TAG Log` DD-04 (BLE) tampil
53. Verifikasi TAG Log DD-04 tidak memuat entri `TAG Marked To be Returned by ...` maupun `TAG Received by ...`
54. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `356938035643501`, tekan Enter, buka menu baris DD-09, klik `TAG Log`
55. Verifikasi popup `TAG Log` DD-09 (GPS) tampil
56. Verifikasi TAG Log DD-09 tidak memuat entri `TAG Marked To be Returned by ...` maupun `TAG Received by ...`
57. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `TAG-QR-00512`, tekan Enter, buka menu baris DD-05, klik `TAG Log`
58. Verifikasi popup `TAG Log` DD-05 (QR) tampil
59. Verifikasi TAG Log DD-05 tidak memuat entri `TAG Marked To be Returned by ...` maupun `TAG Received by ...`
60. Tutup popup lewat `[✕]`

### TC-GS-TAG-289: TAG Log ikut terhapus bersama tag, aktivasi ulang kode yang sama tidak memunculkan riwayat lama

61. Ganti isi kotak search dengan `E2801160600002054D8A0002`, tekan Enter, buka menu baris DD-02, klik `Delete`, lalu konfirmasi dengan klik `Delete` pada dialog
62. Tunggu aksi selesai
63. Klik `+ Activate TAG`, pilih `RFID – User TAG` pada overlay `Select TAG Type`, lalu klik `Continue` pada popup `Ready to Activate a TAG`
64. Pindai `E2801160600002054D8A0002`, lalu klik `Stop` pada Floating Status Widget
65. Isi Template Self-Purchased dengan nilai fixture yang disediakan tim FE, klik `Submit` lalu konfirmasi
66. Tunggu aksi selesai, lalu buka Global Settings > TAG, Tab All, ketik Search `E2801160600002054D8A0002`, tekan Enter
67. Buka menu baris DD-02 (tag baru), klik `TAG Log`
68. Verifikasi TAG Log tag baru memuat entri `TAG Activated by Sari D`
69. Verifikasi TAG Log tag baru hanya memuat satu entri (entri lama `TAG Activated by Siti A` tidak muncul kembali)
70. Tutup popup lewat `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 287, 290, 291 (Client Log), lalu ganti akun, 288, 292, 377, 289 (Client A). Blok Client Log dahulu karena akun hook `before` spec ini; TC-289 (menghapus DD-02) di akhir spec (prinsip 5 bagian 3) sesudah semua kasus Client A yang membutuhkan DD-02 (TC-288) selesai. Perubahan urutan dicatat sesuai S-05.
- Alasan spec di atas sekitar 35 langkah (70 langkah): ketujuh TC berbagi satu permukaan (popup TAG Log) dan dikelompokkan menurut akun (Client Log lalu Client A); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras (bagian 3, pemisah akun dengan Step ganti akun eksplisit, langkah 22 sampai 24), dan tiap blok berdiri sendiri pada data berbeda sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Harness lain sebatas pemicu: sesi API Admin FAMS (langkah 35, 42, 46) hanya memicu perubahan state dan hasilnya diasersi di UI registri dan TAG Log; pemindaian pada langkah 28 dan 64 adalah pemicu (Search by Scan dan aktivasi ulang), bukan objek uji. Langkah 12 sampai 20, 44 sampai 45, dan 49 sampai 58 mengulang pola buka TAG Log lalu amati; tidak ada langkah bersyarat.
- Klausa absence TC-288 ("tidak ada entri baru untuk Search by Scan") ditulis di spec asal dengan baseline `L0` sesuai keputusan D-1 (kelas g ringan). P-1 (state berat): asersi bergantung pada pemindaian yang baru dilakukan langkah 28; anchor positif adalah entri `TAG Activated by Siti A` (langkah 26).
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1, 5, 11, 13, 15, 18, 19, 25, 33, 47 sampai 48, 51, 54, 57, 61, 66 sampai 67 (Search agar baris target tampil dan membuka TAG Log), langkah 9 sampai 10 dan 20 (Setup Column `Last User` dan penutupan Search; precondition TC-291 "kolom Last User ditampilkan"), langkah 22 sampai 24 (ganti akun dan reset fixture), langkah 36, 43, 47, 62, 66 (Tunggu aksi selesai), langkah 4, 8, 17 sampai 19, 28, 32, 34, 40, 51, 54, 57, 60, 70 (menutup popup), langkah 35, 42, 46 (pemicu FAMS), langkah 40 dan 47 (membersihkan filter dan Search), langkah 21 (menyembunyikan kembali kolom `Last User`; pemulihan state), langkah 41 (precondition TC-377: DD-13 `Paired` dan relasi combined dengan DD-11 dilepas lewat fixture BE; dipakai sebagai precondition, hasilnya teramati pada langkah 44).
- Langkah 17 sampai 19 membuka TAG Log DD-50, DD-41, dan DD-42 mengikuti langkah 2 TC-291; Expected TC-291 hanya menyebut sel Last User sehingga tidak ada asersi pada isi popup (isi entri diasersi di spec 093 dan 094).
- Langkah 33 membuka TAG Log DD-15 yang kosong (`No history yet`) sebagai baseline sebelum pemicu pair; keadaan kosong bukan Expected TC-292, sehingga tidak diasersi, dan langkah 34 menutup popup.
- Langkah 3, 7, 31, 45, 53, 56, 59, 69 (absence atau klausa universal) memakai entri atau baris lain pada surface yang sama sebagai anchor positif (langkah 2, 6, 26, 44, 52, 55, 58, 68).
- Temuan untuk QA:
  - TC-288 precondition "Last Scanned DD-02 dicatat" tidak punya Expected padanan; spec tidak mengasersi Last Scanned (Post Condition tanpa observasi).
  - TC-288 langkah 1 ("Search by Scan DD-02") tidak menyebut pilihan teknologi pada overlay; spec memilih `RFID` karena DD-02 bertipe RFID User TAG.
  - TC-289 langkah 2 ("Aktivasi ulang kode lewat Activate TAG") tidak menyebut TAG Type overlay, pemindaian, dan Template Self-Purchased untuk kode yang bukan stok resmi; spec memakai `RFID – User TAG` (Type DD-02 `User TAG`), pemindaian tersimulasi, dan Template fixture disediakan tim FE.
  - TC-289 tidak menyebut isi entri lama DD-02; spec mengacu ke fixture Tabel Data Uji Dinamis (`Activated` 09/09/26 09:15 oleh Siti Amalia).
  - TC-290 precondition "aset terkait tag DD-43 diubah namanya setelah pair" tidak menyebut nama baru dan akun yang mengubah; spec mengasersi nama saat kejadian (`Forklift 01`) dari fixture (Q-15).
  - TC-291 langkah 2 membuka TAG Log tanpa Expected; kolom `Last User` bersifat curated default Hidden menurut catatan Setup Column dan precondition TC menyatakan "ditampilkan" tanpa langkah; spec menambah langkah Setup Column sebagai penghubung.
  - TC-292 Expected ("bersamaan") tidak punya batas waktu atau cara mengamati urutan; spec mengasersi Status `Paired` dan entri `TAG Paired by` setelah pemicu tersimpan. Penyelesaian pair di FAMS (selektor, aset, akun) disediakan tim FE (Q-9, Q-15).
  - TC-377 Post Condition "Tag DD-13 berstatus Available di Tab Not Paired" tidak punya langkah observasi dan tidak diasersi (S-01); status Available teramati tidak langsung lewat entri `Previous Status: To be Returned → Available`.
  - TC-377 langkah 1 dan 3 (disposal dan Receive TAG di FAMS) tidak menyebut pelaku API atau UI; spec memakai sesi API Admin FAMS sebagai pemicu dan mengasersi hasil di registri dan TAG Log.
  - TC-377 precondition menyatakan DD-13 disetel Paired lewat fixture BE sedangkan DD-13 pada Seed Registri A berstatus Available; spec membaca precondition TC-377 sebagai penyetelan fixture BE pada langkah 41.
  - Seeding dan reset Seed Registri A, Client Log, dan Client A antar spec tidak didefinisikan di TC (Q-4).
