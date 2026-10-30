---
id: TC-GS-TAG-E2E-030-submit-activation-diblokir-needs-info-staging-kosong-dan-hanya-error
title: "Submit Activation Diblokir: Baris Needs Info T-05, Staging Kosong T-18, Hanya Baris Error, dan Submit Setelah Dikosongkan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-95
  - TC-GS-TAG-96
  - TC-GS-TAG-97
  - TC-GS-TAG-331
coverage:
  web: automated
---

# Submit Activation Diblokir: Baris Needs Info T-05, Staging Kosong T-18, Hanya Baris Error, dan Submit Setelah Dikosongkan

## Prerequisites

- Mode: FE+BE (backend nyata; tidak ada intercept).
- Akun aktor:
  - Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` (TC-GS-TAG-95, 96, 331).
  - Total Control Client NoByo Eka Pratama `totalControl_automated_qaNoByo@qwertysystem.net`, `Spectra.env.GS_TC_NOBYO_PASSWORD` (TC-GS-TAG-97): login lewat langkah ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec, S-12): stok resmi Admin Console Client A: GPS `356938035643001` (DD-S1) dan `356938035643003` (DD-S3) Available, `356938035643002` (DD-S2) Damaged/Missing, Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`; RFID DD-S4 s.d. DD-S6 (tidak dipakai langkah, bagian precondition TC). Opsi mandiri Client A aktif. Client NoByo: opsi mandiri nonaktif; stok resmi GPS DD-S1 (`356938035643001`); `356938035643101` (DD-N1) tidak ada di stok maupun registri.
- Data uji: IMEI `356938035643001` (Official), `356938035643101` (DD-N1; Needs Info di Client A karena Template kosong, Error di Client NoByo). Identifier tetap tidak diberi sufiks `{runId}` (S-12, suite serial).
- Kemampuan teknis (disediakan tim FE/BE): seed/reset stok resmi dan registri Client A dan Client NoByo; baca jumlah entri Event Log Tab Activate TAG dan Activity Log (baseline); pemantau jumlah request commit Activate pada jaringan (hanya menghitung, tidak mengubah respons; endpoint dari `openapi.yaml` dilengkapi tahap script, S-13); label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): buang staging yang tersisa, pulihkan registri dan stok ke kondisi awal, kembalikan sesi ke akun default suite.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### Baseline log (Client A)

1. Buka Event Log > Tab Activate TAG, catat jumlah entri sebagai baseline `E1`, lalu tutup Event Log
2. Buka Activity Log, catat jumlah entri sebagai baseline `A1`, lalu buka Global Settings > TAG > Tab All

### TC-GS-TAG-96: Submit saat staging kosong adalah no-op T-18

3. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
4. Klik [Submit]
5. Verifikasi toast error: "Error, please scan or add at least one TAG before submitting."
6. Verifikasi dialog `Submit Activation` tidak tampil
7. Verifikasi hitungan request commit Activate sejak sesi dibuka = 0

### TC-GS-TAG-331: Submit setelah staging dikosongkan kembali

8. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
9. Hapus baris `356938035643001` lewat `Remove` dan konfirmasi
10. Klik [Submit]
11. Verifikasi toast error: "Error, please scan or add at least one TAG before submitting."
12. Verifikasi hitungan request commit Activate sejak sesi dibuka = 0

### Absence log untuk TC-GS-TAG-96 dan TC-GS-TAG-331

13. Klik item sidebar `TAG` (staging kosong, tanpa dialog), lalu buka Event Log > Tab Activate TAG
14. Verifikasi jumlah entri Event Log Tab Activate TAG sama dengan baseline `E1` (tidak ada entri baru)
15. Buka Activity Log
16. Verifikasi jumlah entri Activity Log sama dengan baseline `A1` (tidak ada entri baru)

### TC-GS-TAG-95: Submit dengan baris Needs Info diblokir T-05

17. Buka Global Settings > TAG > Tab All, klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
18. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001` (Official) dan `356938035643101` (Needs Info)
19. Verifikasi tombol [Submit] enabled sebelum diklik
20. Klik [Submit]
21. Verifikasi toast error: "Error, please resolve or remove all incomplete rows before submitting."
22. Verifikasi tabel staging tidak berubah (dua baris: `356938035643001` dan `356938035643101`)
23. Verifikasi dialog `Submit Activation` tidak tampil

### TC-GS-TAG-97: Staging hanya berisi baris Error adalah no-op (Client NoByo)

24. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging Client A)
25. Ganti akun: logout, lalu login sebagai Total Control Client NoByo dengan `Spectra.env.GS_TC_NOBYO_PASSWORD`
26. Buka Event Log > Tab Activate TAG, catat jumlah entri sebagai baseline `E2`, lalu tutup Event Log
27. Buka Activity Log, catat jumlah entri sebagai baseline `A2`, lalu buka Global Settings > TAG > Tab All
28. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
29. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643101` (tidak di stok)
30. Klik [Submit]
31. Verifikasi toast error: "Error, please scan or add at least one TAG before submitting."
32. Verifikasi baris `356938035643101` berstatus Error tetap ada di staging
33. Verifikasi hitungan request commit Activate sejak sesi dibuka = 0
34. Klik item sidebar `TAG`, klik [Leave] pada dialog Unsaved Changes, lalu buka Event Log > Tab Activate TAG
35. Verifikasi jumlah entri Event Log Tab Activate TAG sama dengan baseline `E2`
36. Buka Activity Log
37. Verifikasi jumlah entri Activity Log sama dengan baseline `A2`

## Notes

- Mode: FE+BE. Kelas: g untuk klausa absence log (keputusan D-1: klausa "tanpa entri log" ditulis di spec asal dengan baseline jumlah entri sebelum aksi, tanpa spec absence terpisah). P-1 (S-05): klausa absence TC-GS-TAG-96, 97, dan 331 berada di spec asal; baseline `E1`, `A1`, `E2`, `A2` dicatat sebelum aksi pemicu pertama (S-12) dan toast penolakan pada langkah 5, 11, 31 menjadi anchor positif yang terhubung ke pemicu. Subjudul `###` memetakan langkah ke id TC.
- Spec melewati sekitar 35 langkah (37 langkah). Alasan: seluruh blok satu kelas (Submit yang ditolak atau no-op, tanpa commit), memakai dataset stok yang sama dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-GS-TAG-96 dan TC-GS-TAG-331 berbagi satu sesi dan satu pasangan baseline log (pembacaan log sekali di langkah 13 sampai 16 untuk keduanya), mengurangi pembukaan Event Log dan Activity Log berulang.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 2, 13, 15, 17, 24, 25 (ganti akun), 26, 27, 34, 36 (membuka dan menutup surface log, membuang staging, ganti akun), 8, 9, 29 (bagian aksi yang disebut TC sebagai langkah).
- Pembagian TC lintas spec: TC-GS-TAG-94 (baris Error dapat dihapus dan tidak memblokir Submit) berada di spec lain.
- Temuan untuk QA:
  - TC-GS-TAG-331 langkah 5: jalur `Remove` (row action atau Bulk Action > `Remove`) dan label tombol konfirmasi dialog tidak ditulis; spec memakai frasa TC "lewat `Remove` dan konfirmasi" dan selektor disediakan tim FE.
  - TC-GS-TAG-96 dan 331: "tanpa request commit" tidak punya cara observasi di TC; spec memakai pemantau jumlah request commit (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
  - TC-GS-TAG-96/97/331: surface log yang dimaksud ("Event Log maupun Activity Log") dibaca sebagai Event Log > Tab Activate TAG dan Activity Log; jalur membuka Activity Log tidak ditulis di TC.
  - TC-GS-TAG-97 memakai Client NoByo (bukan Client A); spec mengikuti TC dengan ganti akun eksplisit.
  - Post Condition semua TC bernilai `-`.
