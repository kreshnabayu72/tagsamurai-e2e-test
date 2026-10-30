---
id: TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi
title: "Sesi Scan RFID/NFC/BLE di Staging: Pindai Ulang T-02, Format Salah T-32, Pool User TAG, Remove by Scan, Petunjuk Dialog Remove, Normalisasi BLE, dan Info Kuota Header setelah Commit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-65
  - TC-GS-TAG-69
  - TC-GS-TAG-72
  - TC-GS-TAG-90
  - TC-GS-TAG-93
  - TC-GS-TAG-110
  - TC-GS-TAG-322
coverage:
  web: automated
---

# Sesi Scan RFID/NFC/BLE di Staging: Pindai Ulang T-02, Format Salah T-32, Pool User TAG, Remove by Scan, Petunjuk Dialog Remove, Normalisasi BLE, dan Info Kuota Header setelah Commit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Kemampuan teknis (kelas hardware scan, D-4 dan Q-1; mekanisme tidak didefinisikan di TC, PRD, atau LLD): simulasi reader RFID/NFC/BLE (termasuk Handheld Reader `Zebra RFD40 (SN-2201)` untuk TC-GS-TAG-110) yang menghasilkan pemindaian identifier pada sesi Activate TAG, `Scan TAG` memicu pemindaian, dan `Stop` pada Floating Status Widget mengakhiri pemindaian. Label TC `Manual Only — (b)` tidak menjadi alasan mengeluarkan TC; semua disediakan tim FE.
- Data stok resmi Admin Console Client A (seeding disediakan tim FE/BE): RFID – Object TAG `E2801160600002054D8A1001` (DD-S4) dan `E2801160600002054D8A1003` (DD-S6) Available; RFID – User TAG `E2801160600002054D8A2001` (DD-S7) Available; BLE `AABBCCDDEE12` (DD-S10) Available. Identifier uji format salah: `E2801160600002054D8A` (DD-N10, 20 karakter), `04A224B2C1` (DD-N11, 10 karakter), `AABBCCDD` (DD-N12, 8 karakter). Opsi mandiri (BYO) aktif; Template kosong.
- Kemampuan membaca state BE (disediakan tim FE/BE, tanpa mengarang endpoint): daftar tag registri Client A, dipakai hanya untuk Expected TC-72 (tidak ada unit baru untuk EPC pool User TAG).
- Submit Activation hanya dilakukan pada blok TC-GS-TAG-110 (RFID `E2801160600002054D8A1001`, ditaruh paling akhir); stok resmi dan registri Client A dipulihkan lewat fixture BE sesudah blok itu dan di hook `after`. Letak info kuota header di halaman Activate tidak ditulis di TC; selektor disediakan tim FE.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### Sesi RFID – Object TAG

1. Mulai sesi Activate TAG tipe `RFID – Object TAG`: klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-69: Pindai ulang identifier yang sudah jadi baris staging

2. Pindai `E2801160600002054D8A1001` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
3. Pindai `E2801160600002054D8A1001` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget) sekali lagi
4. Verifikasi toast error `Error, TAG is already on the list.`
5. Verifikasi tidak ada baris baru di staging
6. Verifikasi `Total Scanned: 1`

### TC-GS-TAG-90: Dialog Remove memuat petunjuk Removing by scan

7. Klik `Remove` pada baris `E2801160600002054D8A1001`
8. Verifikasi dialog `Remove TAG` memuat baris `Removing by scan is more accurate. Use the button in the toolbar.` sebelum `Are you sure you want to remove it?`
9. Klik `Cancel` pada dialog

### TC-GS-TAG-93: Remove toolbar bersifat scan-based

10. Pindai `E2801160600002054D8A1003` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
11. Klik `Remove` di toolbar
12. Pindai `E2801160600002054D8A1001` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
13. Verifikasi baris `E2801160600002054D8A1003` tetap
14. Verifikasi tidak ada dialog konfirmasi yang muncul
15. Verifikasi baris `E2801160600002054D8A1001` terhapus

### TC-GS-TAG-72: Sesi RFID – Object TAG tidak mencocokkan EPC pool User TAG

16. Pindai `E2801160600002054D8A2001` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
17. Hover lencana `Error` baris `E2801160600002054D8A2001`
18. Verifikasi baris `E2801160600002054D8A2001` berlencana `Error`
19. Verifikasi tooltip `This TAG belongs to a different TAG pool.`
20. Verifikasi aksi baris `E2801160600002054D8A2001` hanya `Remove`
21. Verifikasi tombol `Submit` tetap aktif (baris `Error` tidak memblokir Submit)
22. Verifikasi tidak ada unit baru untuk EPC `E2801160600002054D8A2001` di registri Client A (dibaca lewat kemampuan BE yang disediakan tim FE/BE)

### TC-GS-TAG-65: Format salah RFID – Object TAG menghasilkan Error T-32

23. Pindai `E2801160600002054D8A` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
24. Hover lencana `Error` baris `E2801160600002054D8A`
25. Verifikasi tooltip `Invalid format. Please scan a valid RFID TAG.`
26. Verifikasi aksi baris `E2801160600002054D8A` hanya `Remove`
27. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi NFC

28. Mulai sesi Activate TAG tipe `NFC`: klik `+ Activate TAG`, pilih `NFC` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-65: Format salah NFC menghasilkan Error T-32

29. Pindai `04A224B2C1` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
30. Hover lencana `Error` baris `04A224B2C1`
31. Verifikasi tooltip `Invalid format. Please scan a valid NFC TAG.`
32. Verifikasi aksi baris `04A224B2C1` hanya `Remove`
33. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi BLE

34. Mulai sesi Activate TAG tipe `BLE`: klik `+ Activate TAG`, pilih `BLE` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-65: Format salah BLE menghasilkan Error T-32

35. Pindai `AABBCCDD` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
36. Hover lencana `Error` baris `AABBCCDD`
37. Verifikasi tooltip `Invalid format. Please scan a valid BLE TAG.`
38. Verifikasi aksi baris `AABBCCDD` hanya `Remove`

### TC-GS-TAG-322: Normalisasi identifier BLE

39. Pindai `aa:bb:cc:dd:ee:12` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
40. Verifikasi baris staging berlencana `Official` untuk identifier BLE `AABBCCDDEE12`
41. Pindai `AABBCCDDEE12` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget) sekali lagi
42. Verifikasi toast error `Error, TAG is already on the list.`
43. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### Sesi RFID – Object TAG (commit)

44. Mulai sesi Activate TAG tipe `RFID – Object TAG`: klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-110: Info kuota header hanya berubah setelah commit

45. Catat info kuota header sebagai `Q0`
46. Pindai `E2801160600002054D8A1001` (klik `Scan TAG`, pindai, lalu klik `Stop` pada Floating Status Widget)
47. Verifikasi info kuota header sama dengan `Q0` (tidak berubah walau baris bertambah)
48. Klik `Submit`, lalu klik `Submit` pada dialog (konfirmasi)
49. Verifikasi info kuota header berkurang satu dari `Q0`
50. Pulihkan stok resmi dan registri Client A ke kondisi awal lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: hardware scan (kelas d, D-4 dan Q-1); pemicu pemindaian adalah kemampuan teknis yang disediakan tim FE, bukan endpoint yang dikarang spec ini.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah (50 langkah): satu kelas harness (simulasi reader pada sesi Activate), empat sesi yang berdiri sendiri (satu per TAG Type karena tipe terkunci selama sesi, ditambah sesi commit TC-110 pada RFID – Object TAG), dan blok TC-65 diulang per TAG Type.
- Pembagian TC: TC-69 (pindai ulang RFID, T-02) ada di spec ini (kelas d, bukan di spec pencocokan GPS 022); TC-68 (Duplicate in File GPS) ada di spec 024; TC-110 (info kuota header setelah commit, reader tersimulasi) ada di spec ini, sedangkan commit GPS manual (TC-98, 99, 101, 169) ada di spec 031.
- Urutan sesi RFID – Object TAG: TC-69, TC-90, TC-93 lebih dulu karena mensyaratkan hitungan staging bersih (TC-69 `Total Scanned: 1`); TC-72 dan TC-65 (RFID) di akhir sesi karena menambah baris `Error` yang memengaruhi `Total Scanned`. TC-90 dan TC-93 memakai baris `E2801160600002054D8A1001` yang sudah ada dari TC-69 sehingga pemindaian `E2801160600002054D8A1001` pada TC-90 langkah 4 dan TC-93 langkah 4 tidak diulang (baris sudah ada; pemindaian ulang akan menghasilkan T-02); TC-93 hanya memindai `E2801160600002054D8A1003` karena `E2801160600002054D8A1001` sudah di staging. Sesi commit TC-110 (langkah 44 sampai 50) ditaruh paling akhir karena Submit mengubah stok dan registri Client A; stok dipulihkan pada langkah 50.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Pindai X` = klik `Scan TAG`, pindai X, lalu `Stop` pada Floating Status Widget sebelum menyentuh kontrol lain (Catatan TC: page-lock sesi scan); `Cancel` pada dialog setelah TC-90 menutup dialog tanpa menghapus; `Catat info kuota header` (langkah 45) dan pemulihan stok (langkah 50); hover lencana `Error` menjalankan pengamatan tooltip yang tidak ada langkahnya di TC-65 dan TC-72; `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini (`Leave` tanpa `Verifikasi` dialog).
- Temuan untuk QA:
  - TC-65, TC-69, TC-72, TC-90, TC-93, TC-110, TC-322 berlabel `Manual Only — (b)` (pemindaian hardware) padahal konvensi E2E mengikat hambatan teknis bukan alasan keluar; cara simulasi reader tidak didefinisikan di TC, PRD, atau LLD (Q-1); spec memasukkannya sebagai kelas d dengan kemampuan "disediakan tim FE".
  - TC-65 Expected d ("Baris Error tidak ikut commit dan hanya bisa di-Remove") tidak punya langkah Submit; spec hanya mengasersi aksi baris hanya `Remove`; komitmen "tidak ikut commit" untuk baris `Error` diasersi di spec 029 (TC-94) dan tidak diulang di sini.
  - TC-72 Expected b ("tidak memblokir `Submit`", "tidak ada unit baru yang dibuat") tanpa langkah Submit; spec mengasersi tombol `Submit` aktif dan registri tanpa unit baru lewat pembaca BE yang disediakan tim FE/BE.
  - TC-69, TC-322 Expected: toast T-02 bersifat sementara sedangkan konvensi `Stop` pada Floating Status Widget terjadi setelah pemindaian; TC tidak menyatakan apakah toast masih tampil saat `Stop`; spec mengasersi toast sebelum langkah berikutnya (butir 5 bagian 8b) dan bergantung pada waktu tampil toast.
  - TC-93 Langkah 4 memindai dua identifier; spec tidak memindai ulang yang sudah di staging (lihat urutan di atas).
  - TC-110: Skenario RFID dengan reader tersimulasi (Handheld Reader `Zebra RFD40 (SN-2201)`, D-4, Q-1); letak info kuota header di halaman Activate tidak ditulis di TC, selektor disediakan tim FE. Langkah TC 4, 6, dan 8 (`Catat`, `Amati`) dipetakan ke langkah spec 45, 47, dan 49.
  - TC-65 Metadata "VAL: 20 karakter" sesuai Data Uji `E2801160600002054D8A` (20 karakter); informasional (Q-13).
