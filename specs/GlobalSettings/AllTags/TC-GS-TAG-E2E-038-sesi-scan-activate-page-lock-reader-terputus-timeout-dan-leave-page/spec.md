---
id: TC-GS-TAG-E2E-038-sesi-scan-activate-page-lock-reader-terputus-timeout-dan-leave-page
title: "Sesi Scan Activate: Reader Belum Tersambung, Page-Lock dan Floating Status Widget, Reader Terputus, Timeout T-29, dan Modal Leave-Page"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-115
  - TC-GS-TAG-116
  - TC-GS-TAG-178
  - TC-GS-TAG-179
  - TC-GS-TAG-182
coverage:
  web: automated
---

# Sesi Scan Activate: Reader Belum Tersambung, Page-Lock dan Floating Status Widget, Reader Terputus, Timeout T-29, dan Modal Leave-Page

## Prerequisites

- Mode: FE+BE (backend nyata; reader dan koneksi Bluetooth tersimulasi).
- Akun aktor: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Tidak ada ganti akun.
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, S-12): stok resmi Admin Console Client A: RFID Object TAG `E2801160600002054D8A1001` (DD-S4) dan `E2801160600002054D8A1003` (DD-S6) Available, `E2801160600002054D8A1002` (DD-S5) Damaged/Missing; GPS DD-S1 s.d. DD-S3 (bagian precondition TC, tidak dipakai langkah).
- Tabel "Teknologi sesi" untuk TC-GS-TAG-178 (pilihan overlay `Select TAG Type` dan pesan saat reader belum tersambung):

  | Teknologi | Pilihan overlay | Pesan |
  |---|---|---|
  | RFID | `RFID – Object TAG` | "Reader not connected. Check Bluetooth connection." |
  | NFC | `NFC` | "Reader not connected. Check Bluetooth connection." |
  | BLE | `BLE` | "Scanner not connected. Check Bluetooth connection." |

- Kemampuan teknis (disediakan tim FE, kelas d harness hardware, D-4, Q-1): simulasi Handheld Reader `Zebra RFD40 (SN-2201)` (tersambung, tidak tersambung, pemutusan koneksi Bluetooth di tengah sesi, timeout pembacaan tanpa tag, pemindaian EPC); `Pindai X` berarti pemicu scan lalu X dipindai oleh reader tersimulasi, dan sesi tetap aktif kecuali langkah menyebut klik [Stop]; pengamatan blur halaman dan Floating Status Widget; penanganan dialog `beforeunload` (S-08); pindah ke tab browser lain lalu kembali; tombol Back browser; seed/reset stok dan registri Client A; label dan placeholder input entri manual serta tombol `Scan TAG` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): sambungkan kembali reader tersimulasi, buang staging yang tersisa, pulihkan stok dan registri Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-178: Memulai sesi scan tanpa reader tersambung

1. Putuskan reader tersimulasi (tidak ada Handheld Reader yang tersambung)
2. Untuk setiap baris tabel "Teknologi sesi" (langkah 2 sampai 7): klik `+ Activate TAG`, pilih pilihan overlay `Select TAG Type` pada baris itu, lalu klik [Continue] pada popup `Ready to Activate a TAG`
3. Klik [Scan TAG]
4. Verifikasi pesan pada baris tabel muncul (RFID dan NFC: "Reader not connected. Check Bluetooth connection."; BLE: "Scanner not connected. Check Bluetooth connection.")
5. Verifikasi sesi tidak dimulai (tetap Idle)
6. Verifikasi tombol `Reconnect` tampil inline
7. Klik item sidebar `TAG` (staging kosong, tanpa dialog)

### TC-GS-TAG-179: Sesi Scan TAG, halaman terkunci dan Floating Status Widget

8. Sambungkan Handheld Reader tersimulasi
9. Klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
10. Klik [Scan TAG]
11. Coba klik [Submit] dan row action pada halaman
12. Verifikasi seluruh halaman blur ringan
13. Verifikasi halaman tidak dapat diklik (tombol [Submit] dan row action tidak merespons)
14. Verifikasi Floating Status Widget muncul di kanan bawah
15. Verifikasi widget memuat status sesi
16. Verifikasi widget memuat counter langsung
17. Verifikasi widget memuat satu-satunya kontrol [Stop]
18. Pindai `E2801160600002054D8A1001` (sesi tetap aktif)
19. Verifikasi counter widget bertambah
20. Klik [Stop] pada widget
21. Verifikasi blur dan widget hilang
22. Verifikasi halaman interaktif kembali
23. Verifikasi baris `E2801160600002054D8A1001` ada di staging

### TC-GS-TAG-116: Timeout pembacaan hardware (melanjutkan sesi RFID dengan satu baris staging)

24. Klik [Scan TAG]
25. Picu pembacaan hingga timeout tanpa tag (reader tersimulasi)
26. Verifikasi toast error: "Error, scan timed out. Please try again."
27. Verifikasi baris staging tidak berubah (tetap satu baris `E2801160600002054D8A1001`)
28. Verifikasi tidak ada retry otomatis (sesi tetap Idle sampai [Scan TAG] diklik)
29. Verifikasi kontrol [Scan TAG] aktif untuk memindai ulang
30. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging)

### TC-GS-TAG-182: Meninggalkan halaman saat sesi scan aktif

31. Sambungkan Handheld Reader tersimulasi, lalu klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, dan klik [Continue] pada popup `Ready to Activate a TAG`
32. Klik [Scan TAG] dan pindai `E2801160600002054D8A1001` (sesi tetap aktif)
33. Klik tombol Back browser
34. Verifikasi modal `RFID Scan Stopped` tampil
35. Verifikasi body modal "The scan process was interrupted because you left this window."
36. Verifikasi tombol [Leave Page] dan [Continue Scan] tampil pada modal
37. Klik [Continue Scan]
38. Verifikasi modal tertutup dan halaman Activate TAG tampil kembali
39. Pindah ke tab browser lain lalu kembali ke tab ini
40. Verifikasi modal `RFID Scan Stopped` yang sama muncul saat tab aktif lagi
41. Klik [Continue Scan]
42. Muat ulang halaman (F5)
43. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul tanpa teks kustom aplikasi
44. Setujui konfirmasi bawaan browser (muat ulang halaman)

### TC-GS-TAG-115: Reader terputus di tengah sesi

45. Buka Global Settings > TAG > Tab All, pulihkan stok dan registri Client A lewat fixture BE, lalu klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, dan klik [Continue] pada popup `Ready to Activate a TAG`
46. Klik [Scan TAG] dan pindai `E2801160600002054D8A1001` (sesi tetap aktif)
47. Putuskan koneksi Bluetooth reader (reader tersimulasi)
48. Verifikasi sesi pemindaian berhenti otomatis tanpa error state
49. Verifikasi baris `E2801160600002054D8A1001` dipertahankan di staging
50. Verifikasi tidak ada toast error
51. Verifikasi tidak ada tombol `Reconnect` terpisah
52. Verifikasi Sync Panel terbuka otomatis untuk menyambung ulang
53. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
54. Verifikasi Submit berjalan dengan baris yang ada (baris `E2801160600002054D8A1001` keluar dari staging)

## Notes

- Mode: FE+BE. Kelas d (harness hardware tersimulasi; D-4 dan Q-1: label `Manual Only — (b)` di TC tidak menjadi alasan mengeluarkan TC).
- Spec melewati sekitar 35 langkah (54 langkah nominal; 66 langkah dengan ekspansi langkah 2 sampai 7 untuk tiga teknologi, yaitu 18 langkah ekspansi dari 6 langkah nominal). Alasan: seluruh blok satu kelas harness (reader tersimulasi) dan berdiri sendiri; staging dibuang dan stok dipulihkan antar blok (langkah 7, 30, 44 sampai 45) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pengulangan per teknologi memakai tabel Prerequisites (butir 7 bagian 8b); `Verifikasi` tetap satu per klausa.
- Urutan: TC-GS-TAG-178 (reader tidak tersambung) lebih dulu; TC-GS-TAG-116 melanjutkan sesi TC-GS-TAG-179 yang meninggalkan satu baris staging (precondition TC-GS-TAG-116); blok yang menyubmit (TC-GS-TAG-115) paling akhir.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 7, 8, 24, 30, 31, 44, 45 (menyiapkan reader, pindah ke registri, membuang staging, pemulihan, memulai ulang sesi); langkah 41 menutup modal sebelum F5 (TC tidak menyebut aksi ini); langkah 44 menyetujui konfirmasi bawaan browser (TC tidak menyebut pilihan).
- Pembagian TC lintas spec: TC-GS-TAG-180 (page-lock Audit) berada di spec 041; TC-GS-TAG-181 (Delete by Scan) berada di spec Delete by Scan (054); TC-GS-TAG-93 (Remove toolbar scan-based) berada di spec lain.
- Temuan untuk QA:
  - Q-1: simulasi reader (tersambung, putus, timeout, pemindaian) tidak didefinisikan di TC, PRD, maupun LLD; ditulis "disediakan tim FE" tanpa endpoint karangan.
  - Konvensi TC "Pindai X" (Catatan TC baris 109) mengakhiri dengan `Stop`, sedangkan TC-GS-TAG-115, 179 (sebelum langkah Stop), dan 182 membutuhkan sesi tetap aktif. Spec menulis "sesi tetap aktif" pada langkah 18, 32, 46.
  - TC-GS-TAG-179 langkah 5: "Coba klik tombol Submit dan row action" dilakukan sebelum pemindaian sehingga staging masih kosong dan row action belum ada; spec memakai urutan TC.
  - TC-GS-TAG-182: Langkah Uji tidak menyebut aksi menutup modal sebelum F5 (langkah 41) maupun pilihan pada konfirmasi bawaan; Expected d menyebut "teks tidak dikustom" yang tidak dapat dibaca; spec mengasersi kemunculan konfirmasi tanpa dialog aplikasi.
  - TC-GS-TAG-115 Expected d ("Submit tetap dapat dijalankan dengan baris yang ada") tidak menyebut hasil konkret; spec mengasersi baris keluar dari staging (langkah 54).
  - TC-GS-TAG-116 Expected b ("dapat langsung memindai ulang tanpa retry otomatis") dibaca sebagai tiga klausa (langkah 27 sampai 29).
  - Post Condition semua TC bernilai `-`.
