---
id: TC-GS-TAG-E2E-054-delete-by-scan-page-lock-dan-penghapusan-sukses
title: "Delete by Scan: Penghapusan Langsung T-35, Page-Lock/Widget, Scan Ulang T-08, Sesi Beruntun, dan Pencatatan Sesi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-161
  - TC-GS-TAG-164
  - TC-GS-TAG-165
  - TC-GS-TAG-181
  - TC-GS-TAG-359
coverage:
  web: automated
---

# Delete by Scan: Penghapusan Langsung T-35, Page-Lock/Widget, Scan Ulang T-08, Sesi Beruntun, dan Pencatatan Sesi

## Prerequisites

- Mode: FE+BE (backend nyata; kelas d, harness scan hardware). Spec ini menghapus data registri; seluruh aksi spec adalah Delete by Scan atas baris berbeda atau dipulihkan lewat fixture BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun ini sebagai default suite. Spec ini tidak mengganti akun.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30). Baris yang dipakai: DD-01 `E2801160600002054D8A0001` (Paired), DD-02 `E2801160600002054D8A0002` (Available), DD-15 `E28011606000020F00000001`, DD-16 `E28011606000020F00000002`, DD-17 `E28011606000020F00000003` (Available, filler). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan pada langkah 18, 31, dan 44.
- Kemampuan teknis (disediakan tim FE/BE): simulasi reader RFID untuk sesi Delete by Scan (mulai sesi, pindai kode, `Stop`) dan Handheld Reader terdaftar `Zebra RFD40 (SN-2201)` untuk TC-GS-TAG-164 (D-4, Q-1; mekanisme tidak didefinisikan di TC, PRD, atau LLD); seed dan reset idempotent Seed Registri A; pembacaan jumlah baris Event Log Tab Activate TAG dan jumlah entri Activity Log (baseline).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-161: Scan tag eligible langsung terhapus

1. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
2. Pindai DD-02 `E2801160600002054D8A0002`
3. Verifikasi tidak ada dialog konfirmasi apa pun
4. Verifikasi toast sukses `Success, E2801160600002054D8A0002 has been deleted.`
5. Klik `Stop` pada widget
6. Verifikasi DD-02 hilang dari registri

### TC-GS-TAG-181: Page-lock dan Floating Status Widget

7. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
8. Verifikasi halaman blur
9. Verifikasi halaman non-interaktif
10. Verifikasi widget tampil dengan counter
11. Verifikasi widget memuat kontrol `Stop`
12. Pindai DD-15
13. Verifikasi hasil pindai berupa toast
14. Verifikasi tidak ada dialog
15. Klik `Stop` pada widget
16. Verifikasi halaman interaktif
17. Verifikasi sesi Delete by Scan berakhir

### TC-GS-TAG-359: Scan ulang kode yang sudah terhapus

18. Pulihkan Seed Registri A lewat fixture BE (DD-15 Available), lalu muat ulang halaman
19. Buka Event Log > Tab Activate TAG, catat jumlah baris, lalu tutup modal
20. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
21. Pindai DD-15
22. Verifikasi toast sukses `Success, E28011606000020F00000001 has been deleted.`
23. Tutup toast
24. Pindai DD-15 sekali lagi
25. Verifikasi toast error `Error, TAG not found in registry.`
26. Verifikasi tidak ada dialog
27. Verifikasi sesi scan berlanjut
28. Klik `Stop` pada widget
29. Buka Event Log > Tab Activate TAG
30. Verifikasi satu baris baru Delete dengan Success `1` (jumlah baris bertambah satu dari nilai yang dicatat)

### TC-GS-TAG-165: Scan beruntun

31. Tutup modal Event Log, pulihkan Seed Registri A lewat fixture BE, lalu muat ulang halaman
32. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
33. Pindai DD-15
34. Verifikasi toast sukses `Success, E28011606000020F00000001 has been deleted.`
35. Pindai DD-16
36. Verifikasi toast sukses `Success, E28011606000020F00000002 has been deleted.`
37. Pindai DD-17
38. Verifikasi toast sukses `Success, E28011606000020F00000003 has been deleted.`
39. Verifikasi hanya satu toast yang tampil (toast baru menggantikan toast sebelumnya, satu slot)
40. Verifikasi tidak ada dialog yang terbuka
41. Verifikasi tidak ada pemindaian yang ditahan
42. Klik `Stop` pada widget
43. Verifikasi DD-15, DD-16, dan DD-17 hilang dari registri

### TC-GS-TAG-164: Satu baris Event Log dan satu entri Activity Log per sesi

44. Pulihkan Seed Registri A lewat fixture BE, lalu muat ulang halaman
45. Buka Event Log > Tab Activate TAG, catat jumlah baris, lalu tutup modal
46. Buka Global Settings > Activity Log, catat jumlah entri, lalu kembali ke Global Settings > TAG Tab All
47. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
48. Pindai DD-15
49. Pindai DD-01 (Paired)
50. Pindai DD-16
51. Klik `Stop` pada widget (tutup pemindai)
52. Buka Event Log > Tab Activate TAG
53. Verifikasi satu baris baru Activity `Delete` (jumlah baris bertambah satu dari nilai yang dicatat)
54. Verifikasi baris itu bernilai Success `2` dan Failed `0`
55. Verifikasi Hardware pada baris itu berisi nama Handheld Reader `Zebra RFD40 (SN-2201)`
56. Tutup modal Event Log, lalu buka Global Settings > Activity Log
57. Verifikasi satu entri baru `Delete TAG` (jumlah entri bertambah satu dari nilai yang dicatat)
58. Verifikasi entri itu memiliki Name `2 TAGs`, Field `Status`, Old `—`, dan New `Deleted (Delete by Scan)`

## Notes

- Mode: FE+BE. Kelas d (hardware scan). Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (58 langkah nominal). Alasan: lima TC satu topik aksi (Delete by Scan sukses) dengan satu kelas harness (simulasi reader), satu akun, dan satu dataset Seed Registri A; tiap blok berdiri sendiri karena data dipulihkan lewat fixture BE di awal blok yang memakai DD-15 sampai DD-17 (langkah 18, 31, dan 44) dan baseline dicatat per blok.
- Pemisahan: TC-GS-TAG-160 (tooltip) dan TC-GS-TAG-358 (verifikasi lintas FAMS dengan ganti akun) ada di spec 099; spec ini satu akun tanpa ganti akun sehingga kegagalan di FAMS tidak menutupi blok Delete by Scan.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (161, 164, 165, 181, 359) disusun ulang menjadi 161, 181, 359, 165, 164. TC-GS-TAG-181 memindai DD-15 sebelum blok yang memulihkannya; 359, 165, dan 164 memakai DD-15 secara berulang dan memulihkannya di langkah 18, 31, dan 44.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 19, 45, dan 46 (mencatat baseline), 23 (menutup toast sebelum asersi toast berikutnya, S-09), 29 dan 52 (membuka Event Log > Tab Activate TAG sebelum asersi barisnya), 56 (navigasi), 18, 31, dan 44 (memulihkan data lewat fixture BE).
- Asersi tambahan di luar Expected TC (S-03): langkah 8 dan 9 serta 10 dan 11 memecah klausa Expected a TC-GS-TAG-181 (blur dan non-interaktif; counter dan `Stop`), dan langkah 13 dan 14 memecah "hasil pindai berupa toast tanpa dialog".
- Rujukan lintas spec: TC-GS-TAG-162, 163, 173, 357, dan 362 (penolakan Delete by Scan) ada di spec 055; TC-GS-TAG-360 dan 361 (kegagalan server dan race) ada di spec 056; TC-GS-TAG-160 dan 358 ada di spec 099.
- Temuan untuk QA:
  - Q-1: TC-GS-TAG-161, 164, 165, 181, dan 359 berlabel `Manual Only — (b)` (scan hardware); kemampuan simulasi reader dicatat di Prerequisites (D-4).
  - Q-4: identifier tetap; Seed Registri A dipulihkan lewat fixture BE sebelum spec dan pada langkah 18, 31, dan 44.
  - TC-GS-TAG-165 Expected b menulis toast untuk "DD-15, DD-16, DD-17" dengan kode `E28011606000020F00000001` sampai `...03` (sama dengan Seed Registri A); tidak ada ketidakkonsistenan.
  - Post Condition TC-GS-TAG-161 butir b (Event Log dan Activity Log), butir c (kuota RFID – User TAG), Post Condition TC-GS-TAG-165 butir b, dan Post Condition TC-GS-TAG-359 (kuota berkurang 1 saja) tidak punya langkah observasi di TC dan tidak diasersi.
  - Post Condition TC-GS-TAG-164: butir a (DD-15 dan DD-16 tidak ada di registri) dan butir b bagian Tab Usage Event Type `Delete TAG` tidak punya langkah observasi di TC (langkah TC hanya membuka Event Log dan Activity Log) dan tidak diasersi. Baris Event Log dengan Hardware reader dan entri Activity Log diasersi karena menjadi Expected a dan b.
