---
id: TC-GS-TAG-E2E-090-atribusi-hardware-handheld-reader-dan-tab-usage
title: "Atribusi Hardware Handheld Reader: Kolom Hardware Event Log dan Tab Usage untuk Activate, Audit, dan Delete by Scan, serta Tanpa Reader"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-270
  - TC-GS-TAG-271
  - TC-GS-TAG-272
  - TC-GS-TAG-273
coverage:
  web: automated
---

# Atribusi Hardware Handheld Reader: Kolom Hardware Event Log dan Tab Usage untuk Activate, Audit, dan Delete by Scan, serta Tanpa Reader

## Prerequisites

- Mode: FE+BE.
- Akun aktor utama: Total Control Client A Sari Dewi (`Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite).
- Akun kedua (langkah 38 sampai 40, TC-271): Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`; kredensial `Spectra.env.GS_TC_AUDIT_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` untuk kedua akun mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Hook `after` suite memulihkan Seed Registri A, stok resmi, dan Seed Client Audit secara idempotent (pernyataan hook di `suite.md`).
- Data Pre-setup (dipulihkan ke kondisi awal oleh hook `before` lewat fixture BE; mekanisme disediakan tim FE/BE, lihat Temuan untuk QA):
  - Client A: stok resmi GPS `356938035643001` (DD-S1, Available) dan RFID Object `E2801160600002054D8A1001` (DD-S4) dan `E2801160600002054D8A1003` (DD-S6) Available; Seed Registri A dengan DD-15 `E28011606000020F00000001`, DD-16 `E28011606000020F00000002`, DD-17 `E28011606000020F00000003`, DD-18 `E28011606000020F00000004` (RFID Object, Official, Available, Tab Not Paired).
  - Client Audit: Seed Client Audit AU1 `E2801160600002054D8A5001`, AU2 `...5002`, AU3 `...5003`, AU4 `...5004` (Tabel Data Uji Dinamis DD-31 sampai DD-34).
  - Handheld Reader `Zebra RFD40 (SN-2201)` (modul Hardware > Handheld Reader): reader yang diamati Tab Usage-nya. Akun yang menyambungkan reader dan keberadaan reader lain di client uji tidak didefinisikan di TC (disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): simulasi Handheld Reader tersambung via USB dan terdeteksi di Sync Panel, pemutusannya (untuk TC-273), serta pemindaian tag RFID (pindai kode, `Stop` pada Floating Status Widget sebelum menyentuh kontrol halaman lain; page-lock sesi scan, NC-43; label TC `Manual Only — (b)` bukan alasan mengeluarkan TC, keputusan D-4, Q-1); entri manual GPS (input lalu klik `Add`; label dan placeholder menunggu desain, NC-11); pembaca nilai footer pagination.
- Baseline log: Event Log dan Tab Usage reader menumpuk antar spec (tidak dibersihkan), sehingga semua asersi entri baru memakai selisih total terhadap baseline yang dicatat sebelum aksi (S-12). Tiap blok mencatat baseline sendiri (TC-273 `N0`/`U0`, TC-270 `N1`/`U1`, TC-272 `N2`/`U2`, TC-271 `M0`/`U3`).
- State global yang diubah: koneksi reader (disambung atau diputus oleh simulasi); dipulihkan di hook `after` ke kondisi awal. Selain itu hanya data (stok, registri, dan log).

## Test Steps

### TC-GS-TAG-273: Tanpa reader terdeteksi tidak ada entri Tab Usage

1. Putus semua Handheld Reader dari Client A (simulasi reader terputus; tidak ada reader terdeteksi di Sync Panel)
2. Buka Hardware > Handheld Reader > Detail `Zebra RFD40 (SN-2201)` > Tab Usage, catat total entri `U0`
3. Buka Global Settings > TAG, Tab All, klik tombol `Event Log`, catat total `N0` pada footer Tab Activate TAG, lalu tutup modal lewat `✕`
4. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik `Continue` pada popup `Ready to Activate a TAG`
5. Tambahkan lewat entri manual `356938035643001`
6. Klik `Submit` lalu konfirmasi
7. Tunggu aksi selesai
8. Buka Event Log, Tab Activate TAG
9. Verifikasi total log menjadi `N0 + 1`
10. Verifikasi baris pertama (Date terbaru): TAG Type `GPS`, Activity `Activate`, Hardware `—`
11. Tutup modal lewat `✕`, buka Hardware > Handheld Reader > Detail `Zebra RFD40 (SN-2201)` > Tab Usage
12. Verifikasi total entri sama dengan `U0` (tidak ada entri baru pada Tab Usage reader)
13. Catat baseline sebelum aksi: total entri Tab Usage `U1` pada footer, buka Global Settings > TAG, Tab All, klik tombol `Event Log`, catat total `N1` pada footer Tab Activate TAG, lalu tutup modal lewat `✕`

### TC-GS-TAG-270: Sesi Activate dengan Handheld Reader tercatat di kolom Hardware dan Tab Usage

14. Sambungkan Handheld Reader `Zebra RFD40 (SN-2201)` via USB sehingga terdeteksi di Sync Panel
15. Buka Global Settings > TAG, Tab All, klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, lalu klik `Continue`
16. Pindai `E2801160600002054D8A1001` dan `E2801160600002054D8A1003`, lalu klik `Stop` pada Floating Status Widget
17. Klik `Submit` lalu konfirmasi, kemudian Tunggu aksi selesai
18. Buka Event Log, Tab Activate TAG
19. Verifikasi total log menjadi `N1 + 1`
20. Verifikasi baris pertama (Date terbaru): Hardware `Zebra RFD40 (SN-2201)`
21. Tutup modal lewat `✕`, buka Hardware > Handheld Reader > Detail `Zebra RFD40 (SN-2201)` > Tab Usage
22. Verifikasi total entri menjadi `U1 + 1`
23. Verifikasi entri teratas: Event Type `Activate TAG`, Product `Global Settings`, Transaction ID `—`, PIC `Sari D`
24. Verifikasi rujukan sesi tidak ditampilkan pada entri teratas

### TC-GS-TAG-272: Delete by Scan dengan reader tercatat sebagai Delete TAG, Delete menu baris dan bulk tidak mencatat device

25. Catat baseline sebelum aksi: total `N2` pada footer Event Log Tab Activate TAG dan total `U2` entri Tab Usage `Zebra RFD40 (SN-2201)`
26. Buka Global Settings > TAG, Tab All, jalankan Delete by Scan: pilih teknologi `RFID`, pindai DD-15 (`E28011606000020F00000001`) hingga langsung terhapus, lalu klik `Stop` pada Floating Status Widget
27. Ketik Search `E28011606000020F00000002`, tekan Enter, buka menu baris DD-16, klik `Delete`, lalu konfirmasi dengan klik `Delete` pada dialog
28. Klik `(←)` pada kotak Search, klik Tab Not Paired, ketik Search `E28011606000020F00000003`, tekan Enter, lalu centang baris DD-17
29. Ganti isi kotak search dengan `E28011606000020F00000004`, tekan Enter, centang baris DD-18, pilih `Bulk Action` > `Delete`, lalu klik `Delete` pada dialog
30. Tunggu aksi selesai, lalu buka Event Log, Tab Activate TAG
31. Verifikasi total log menjadi `N2 + 3`
32. Verifikasi di antara tiga baris baru, satu baris Activity `Delete` dengan Success `1` dan Hardware `Zebra RFD40 (SN-2201)` (Delete by Scan)
33. Verifikasi di antara tiga baris baru, satu baris Activity `Delete` dengan Success `1` dan Hardware `—` (Delete menu baris)
34. Verifikasi di antara tiga baris baru, satu baris Activity `Delete` dengan Success `2` dan Hardware `—` (Bulk Delete)
35. Tutup modal lewat `✕`, buka Hardware > Handheld Reader > Detail `Zebra RFD40 (SN-2201)` > Tab Usage
36. Verifikasi total entri menjadi `U2 + 1`
37. Verifikasi entri teratas: Event Type `Delete TAG`

### TC-GS-TAG-271: Sesi Audit dengan Handheld Reader tercatat sebagai Audit TAG

38. Klik avatar akun, pilih `Logout`
39. Login sebagai Total Control Client Audit Joko Santoso (`Spectra.env.GS_TC_AUDIT_PASSWORD`)
40. Sambungkan Handheld Reader `Zebra RFD40 (SN-2201)` via USB sehingga terdeteksi di Sync Panel, buka Hardware > Handheld Reader > Detail `Zebra RFD40 (SN-2201)` > Tab Usage, catat total entri `U3`
41. Buka Global Settings > TAG, klik tombol `Event Log`, klik tab `Audit TAG`, catat total `M0` pada footer, lalu tutup modal lewat `✕`
42. Klik Tab Not Paired, klik `Audit TAG`, pilih `RFID` pada overlay `Select TAG Type`
43. Pindai AU1 sampai AU4 (`E2801160600002054D8A5001` sampai `E2801160600002054D8A5004`), lalu klik `Stop` pada Floating Status Widget
44. Klik `Submit`, kemudian Tunggu aksi selesai
45. Buka Event Log, klik tab `Audit TAG`
46. Verifikasi total log menjadi `M0 + 1`
47. Verifikasi baris pertama (Date terbaru): Hardware `Zebra RFD40 (SN-2201)`
48. Tutup modal lewat `✕`, buka Hardware > Handheld Reader > Detail `Zebra RFD40 (SN-2201)` > Tab Usage
49. Verifikasi total entri menjadi `U3 + 1`
50. Verifikasi entri teratas: Event Type `Audit TAG`, Product `Global Settings`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Kelas d (hardware: simulasi reader).
- Urutan TC dalam spec: 273, 270, 272, 271 (bukan urutan sumber). TC-273 mendahului karena butuh kondisi tanpa reader sebelum reader disambungkan (langkah 14); TC-272 (Delete, destruktif) di akhir blok Client A (prinsip 5 bagian 3); TC-271 memakai Client Audit sehingga di akhir setelah ganti akun eksplisit (langkah 38 sampai 40). Perubahan urutan dicatat sesuai S-05.
- Klausa absence TC-273 (tidak ada entri baru pada Tab Usage reader, langkah 12) ditulis di spec asal dengan baseline `U0` sesuai keputusan D-1; anchor positif adalah baris Event Log baru `N0 + 1` pada langkah 9 sampai 10. P-1 (state berat): asersi bergantung pada sesi Activate yang baru dibangun langkah 4 sampai 7.
- Alasan spec di atas sekitar 35 langkah (50 langkah): empat TC berkelas sama (atribusi hardware reader pada Event Log dan Tab Usage) dan memakai reader dan surface log yang sama; TC-271 berdiri di bagian setelah ganti akun yang tetap bermakna bila bagian sebelumnya gagal (bagian 3 prinsip 13, poin ganti akun eksplisit). Tidak ada langkah berulang dengan ekspansi.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 2 sampai 3, 13, 25, 40, 41 (baseline sebelum aksi pemicu, S-12), langkah 1 dan 14 (memutus dan menyambungkan reader; precondition TC-273 dan TC-270), langkah 7, 17, 30, 44 (Tunggu aksi selesai), langkah 11, 21, 35, 48 (pindah surface), langkah 26 sampai 29 (Search, pemilihan baris, dan Tab Not Paired untuk Bulk Delete), langkah 38 sampai 39 (ganti akun), langkah 40 (menyambungkan reader pada Client Audit).
- Langkah 32 sampai 34 mengidentifikasi tiga baris baru lewat kombinasi Success dan Hardware karena Date berketelitian menit tidak membedakan urutan tiga sesi dalam satu menit.
- Temuan untuk QA:
  - TC-270 sampai TC-272 berlabel `Manual Only — (b)`; cara simulasi reader (sambung USB, terdeteksi di Sync Panel, pindai, putus) tidak didefinisikan di TC, PRD, atau LLD (Q-1); disediakan tim FE tanpa endpoint karangan.
  - TC-273 Expected ("tidak ada entri baru pada Tab Usage reader manapun") tidak menyebut daftar reader di client uji; spec mengamati reader `Zebra RFD40 (SN-2201)` saja (Pre-setup tidak mendaftar reader lain).
  - Langkah navigasi Hardware > Handheld Reader > Detail > Tab Usage melibatkan modul Hardware yang selektornya tidak didefinisikan; disediakan tim FE (Q-9). Akun yang dipakai membaca Tab Usage tidak disebut TC; spec memakai akun Total Control yang sedang login.
  - TC-271 menyebut reader terdeteksi pada Client Audit tetapi reader `Zebra RFD40 (SN-2201)` pada Event Log seed berada di Client A; kepemilikan reader per client tidak didefinisikan di TC.
  - TC-270 Expected b tidak menyebut format PIC di Tab Usage; spec memakai `Sari D` (format `[First Name] [Last Initial]`).
  - Seeding dan reset antar spec tidak didefinisikan di TC (Q-4).
