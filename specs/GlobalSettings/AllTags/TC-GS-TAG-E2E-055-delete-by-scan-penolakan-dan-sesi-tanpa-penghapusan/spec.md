---
id: TC-GS-TAG-E2E-055-delete-by-scan-penolakan-dan-sesi-tanpa-penghapusan
title: "Delete by Scan: Penolakan Paired/Reserved T-34, Waiting for Approval T-36, Combined, Tak Dikenal T-08/T-09, dan Sesi Tanpa Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-162
  - TC-GS-TAG-163
  - TC-GS-TAG-173
  - TC-GS-TAG-357
  - TC-GS-TAG-362
coverage:
  web: automated
---

# Delete by Scan: Penolakan Paired/Reserved T-34, Waiting for Approval T-36, Combined, Tak Dikenal T-08/T-09, dan Sesi Tanpa Log

## Prerequisites

- Mode: FE+BE (backend nyata; kelas d, harness scan hardware). Blok yang menghapus data (TC-GS-TAG-173 dan 162, masing-masing satu tag eligible) berada di akhir spec.
- Akun aktor (ganti akun eksplisit hanya pada TC-GS-TAG-357):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun ini sebagai default suite.
  - Principal approver (Mira Anggraini) `principalApprover_automated@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, untuk Admin Console > Approvals > TAG Stock (TC-GS-TAG-357). Kesamaan akun ini dengan env var terdaftar perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; 30 baris). Baris yang dipakai: DD-01 `E2801160600002054D8A0001` (Paired), DD-06 `E2801160600002054D8A0006` (Reserved), DD-03 `04A224B2C15E80` (NFC Waiting for Approval; subject `Activation Collision` pending di Approvals > TAG Stock Tab Active), DD-11 `E2801160600002054D8A0011` (combined), DD-15 `E28011606000020F00000001` dan DD-02 `E2801160600002054D8A0002` (Available, dihapus oleh scan), identifier uji `E2801160600002054D8A3003` (EPC valid belum diaktivasi). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec.
- Kemampuan teknis (disediakan tim FE/BE): simulasi reader RFID dan NFC untuk sesi Delete by Scan (mulai sesi, pindai kode, `Stop`; D-4, Q-1; mekanisme tidak didefinisikan di TC, PRD, atau LLD) dan pemindaian "kode berformat bukan TAG Samurai" (kode acak yang tidak diparse); seed dan reset idempotent Seed Registri A; pembacaan jumlah baris Event Log Tab Activate TAG dan jumlah entri Activity Log (baseline). Langkah dan selektor Admin Console > Approvals tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A lewat fixture BE; sesi dikembalikan ke Total Control Client A.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-163: Kode belum diaktivasi dan kode tidak dikenali

1. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
2. Pindai `E2801160600002054D8A3003` (valid, belum diaktivasi)
3. Verifikasi toast error `Error, TAG not found in registry.`
4. Tutup toast
5. Pindai kode berformat bukan TAG Samurai (kode acak)
6. Verifikasi toast error `Error, can't recognize TAG.`
7. Verifikasi sesi scan tetap aktif
8. Klik `Stop` pada widget
9. Verifikasi registri tidak berubah (jumlah baris tetap `Showing ... of 30`)

### TC-GS-TAG-362: Sesi tanpa penghapusan berhasil tidak menulis log

10. Buka Event Log > Tab Activate TAG, catat jumlah baris, lalu tutup modal
11. Buka Global Settings > Activity Log, catat jumlah entri, lalu kembali ke Global Settings > TAG Tab All
12. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
13. Pindai DD-01 (Paired)
14. Verifikasi toast error `Error, this TAG is currently paired and can't be deleted.`
15. Tutup toast
16. Pindai DD-06 (Reserved)
17. Verifikasi toast error `Error, this TAG is currently reserved and can't be deleted.`
18. Tutup toast
19. Pindai `E2801160600002054D8A3003` (belum diaktivasi)
20. Verifikasi toast error `Error, TAG not found in registry.`
21. Klik `Stop` pada widget
22. Buka Event Log > Tab Activate TAG
23. Verifikasi Event Log tidak memuat baris baru (jumlah baris sama dengan yang dicatat)
24. Tutup modal Event Log, lalu buka Global Settings > Activity Log
25. Verifikasi Activity Log tidak memuat entri `Delete TAG` baru (jumlah entri sama dengan yang dicatat)

### TC-GS-TAG-357: Scan tag Waiting for Approval ditolak

26. Kembali ke Global Settings > TAG Tab All, catat nilai kartu NFC
27. Klik `Delete by Scan` lalu pilih teknologi `NFC` pada overlay
28. Pindai `04A224B2C15E80` (DD-03 Waiting for Approval)
29. Verifikasi toast error `Error, this TAG is waiting for approval and can't be deleted by scan. Delete it from the list instead.`
30. Verifikasi tidak ada dialog
31. Klik `Stop` pada widget
32. Verifikasi DD-03 tetap `Waiting for Approval` di registri
33. Verifikasi kartu NFC tidak berubah dari nilai yang dicatat
34. Ganti akun ke Principal approver, buka Admin Console > Approvals > TAG Stock Tab Active
35. Verifikasi subject `Activation Collision` DD-03 tetap ada di Tab Active
36. Verifikasi subject DD-03 tidak berstatus `Canceled`
37. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All
38. Buka menu baris DD-03, lalu klik `Delete`
39. Verifikasi dialog `Delete TAG` memuat baris peringatan `This will free up license quota and pending approval will be canceled.`
40. Klik `Cancel` pada dialog

### TC-GS-TAG-173: Scan tag combined

41. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
42. Pindai DD-11 (combined)
43. Verifikasi toast error `Error, this TAG is combined and can't be deleted. Separate it first.`
44. Verifikasi tidak ada dialog
45. Verifikasi sesi scan berlanjut tanpa jeda
46. Tutup toast
47. Pindai DD-15
48. Verifikasi toast sukses `Success, E28011606000020F00000001 has been deleted.`
49. Verifikasi tidak ada dialog
50. Klik `Stop` pada widget

### TC-GS-TAG-162: Scan tag Paired atau Reserved

51. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
52. Pindai DD-01 (Paired)
53. Verifikasi toast error `Error, this TAG is currently paired and can't be deleted.`
54. Verifikasi tidak ada dialog
55. Tutup toast
56. Pindai DD-06 (Reserved)
57. Verifikasi toast error `Error, this TAG is currently reserved and can't be deleted.`
58. Verifikasi tidak ada dialog
59. Tutup toast
60. Verifikasi sesi scan berlanjut tanpa jeda
61. Pindai DD-02 (Available)
62. Verifikasi toast sukses `Success, E2801160600002054D8A0002 has been deleted.`
63. Verifikasi tidak ada dialog
64. Klik `Stop` pada widget
65. Verifikasi DD-01 tetap `Paired`
66. Verifikasi DD-06 tetap `Reserved`

## Notes

- Mode: FE+BE. Kelas d (hardware scan). Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (66 langkah nominal). Alasan: lima TC satu topik aksi (penolakan Delete by Scan) dengan satu kelas harness (simulasi reader) dan satu dataset Seed Registri A; tiap blok berdiri sendiri (sesi scan dimulai dan dihentikan per blok) dan dua blok terakhir menghapus tag eligible sehingga berada di akhir.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (162, 163, 173, 357, 362) disusun ulang menjadi 163, 362, 357, 173, 162: blok tanpa penghapusan lebih dulu, blok yang menghapus DD-15 (TC-GS-TAG-173) dan DD-02 (TC-GS-TAG-162) di akhir.
- Pengecualian P-1: asersi bahwa Event Log dan Activity Log tidak memuat entri baru (langkah 23 dan 25; D-1) memakai baseline jumlah entri yang dicatat sebelum sesi scan (langkah 10 dan 11) dan didahului tiga toast error yang diasersi (langkah 14, 17, 20) sebagai anchor pemicu; state berat (sesi scan hardware) dibangun di spec ini.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 4, 15, 18, 46, 55, dan 59 (menutup toast sebelum asersi toast berikutnya, S-09), 10, 11, dan 26 (baseline dan kembali ke Tab All), 24 dan 37 (navigasi), 34 (ganti akun), 22 (membuka Event Log).
- Asersi tambahan di luar Expected TC (S-03): langkah 9 (registri tidak berubah) mengikuti Expected c TC-GS-TAG-163; langkah 33, 35, dan 36 mengikuti Expected b dan c TC-GS-TAG-357.
- Temuan untuk QA:
  - Q-1: seluruh TC di spec ini berlabel `Manual Only — (b)`; kemampuan simulasi reader dicatat di Prerequisites (D-4).
  - Q-4: identifier tetap; hitungan registri 30 baris valid hanya bila Seed Registri A dipulihkan.
  - Q-2: Pre-setup TC memakai `principalApprover_automated`, sedangkan `.env.example` mendaftarkan `totalControlPrincipal_automated_qaTeam1` (GS_PRINCIPAL_TC); kesamaan perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
  - TC-GS-TAG-357 langkah 4 tidak menyebut akun yang membuka Admin Console > Approvals; spec memakai Principal approver. Langkah dan selektor Approvals tidak didefinisikan (Q-9).
  - TC-GS-TAG-163 langkah 3 ("kode berformat bukan TAG Samurai") tidak memberi nilai kode; spec memakai kode acak yang disediakan tim FE (Data Uji TC: "kode acak").
  - Post Condition TC-GS-TAG-357 butir a identik dengan Expected b dan c; butir b ("Tidak ada baris Event Log Delete baru") tidak punya langkah observasi di TC dan tidak diasersi. Post Condition TC-GS-TAG-362 identik dengan Expected b dan c.
