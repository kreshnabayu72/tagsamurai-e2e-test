---
id: TC-GS-TAG-E2E-035-resilience-commit-activate-gagal-server-dan-klik-ganda
title: "Resilience Commit Activate: Gagal Server T-25 dengan Retry Tidak Ganda dan Klik Ganda Submit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-108
  - TC-GS-TAG-109
coverage:
  web: automated
---

# Resilience Commit Activate: Gagal Server T-25 dengan Retry Tidak Ganda dan Klik Ganda Submit

## Prerequisites

- Mode: FE+BE (backend nyata dengan intercept parsial pada request commit Activate; asersi memakai state backend nyata, bagian 6 konvensi).
- Akun aktor: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Tidak ada ganti akun.
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, S-12): stok resmi Admin Console Client A: GPS `356938035643001` (DD-S1) dan `356938035643003` (DD-S3) Available, `356938035643002` (DD-S2) Damaged/Missing, Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`; registri Client A tidak memuat `356938035643001` pada awal tiap blok.
- Kemampuan teknis (disediakan tim FE/BE): intercept jaringan di atas backend nyata untuk request commit Activate: respons 5xx (TC-GS-TAG-108) dan penahanan respons sementara agar state loading tombol dialog teramati (TC-GS-TAG-109); endpoint commit Activate dari `openapi.yaml` dilengkapi tahap script (S-13); intercept dilepas segera setelah pemicu selesai (S-09); baca jumlah entri Event Log Tab Activate TAG (baseline); seed/reset stok resmi dan registri Client A; label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): lepas intercept yang tersisa, pulihkan stok resmi dan registri Client A, buang staging yang tersisa.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-108: Commit gagal server, staging dipertahankan, Submit dapat diulang

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
3. Aktifkan intercept: request commit Activate dijawab 5xx
4. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
5. Verifikasi toast error persisten: "Error, failed to activate TAG."
6. Verifikasi staging tetap berisi baris `356938035643001`
7. Verifikasi halaman Activate TAG tetap terbuka
8. Lepas intercept
9. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi) lagi
10. Verifikasi toast sukses: "Success, TAG has been activated."
11. Klik item sidebar `TAG`, klik Tab All, ketik Search `356938035643001`, tekan Enter
12. Verifikasi registri memuat tepat satu baris `356938035643001` (tidak ganda)
13. Pulihkan stok resmi dan registri Client A ke kondisi awal lewat fixture BE

### TC-GS-TAG-109: Klik ganda Submit memproses satu request dan satu entri Event Log

14. Buka Event Log > Tab Activate TAG, catat jumlah entri sebagai baseline `E109`, lalu tutup Event Log
15. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
16. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
17. Aktifkan penahanan respons pada request commit Activate (agar state loading teramati)
18. Klik [Submit]
19. Klik dua kali cepat [Submit] pada dialog `Submit Activation`
20. Verifikasi tombol [Submit] pada dialog disabled dengan loading setelah klik pertama
21. Lepas penahanan respons
22. Klik item sidebar `TAG`, klik Tab All, ketik Search `356938035643001`, tekan Enter
23. Verifikasi registri memuat tepat satu tag `356938035643001` aktif
24. Buka Event Log > Tab Activate TAG
25. Verifikasi jumlah entri Event Log `Activate` bertambah tepat satu dari baseline `E109`

## Notes

- Mode: FE+BE dengan intercept parsial (kelas b, bagian 6). TC-GS-TAG-109 (klik ganda, objek uji ringan tanpa harness eksternal) berada di spec ini karena memakai penahanan respons yang sama dengan kelas b.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 8, 11, 13, 14, 15, 17, 21, 22, 24 (membuka sesi, pasang dan lepas intercept, pindah ke registri dan Search untuk menemukan baris target, pemulihan, membuka dan menutup Event Log). Langkah 17 menahan respons hanya untuk mengamati state loading (bukan kegagalan yang dipaksakan) dan dilepas pada langkah 21 sesuai butir 5 bagian 8b.
- Baseline `E109` dicatat sebelum aksi pemicu pertama yang diasersi (S-12). Registri pada langkah 12 dan 23 dibaca setelah `Search` karena baris target tidak dijamin tampil pada halaman aktif.
- Pembagian TC lintas spec: TC-GS-TAG-176 (seluruh baris Failed, toast T-25) berada di spec 033.
- Temuan untuk QA:
  - TC-GS-TAG-109 langkah 6: state loading tombol hanya teramati bila respons ditahan; TC tidak menyebut mekanismenya (penahanan respons disediakan tim FE).
  - TC-GS-TAG-109 Expected b memuat "satu tag aktif dan tepat satu baris Event Log `Activate` baru"; spec mengasersi keduanya sebagai dua klausa (langkah 23 dan 25).
  - Post Condition TC-GS-TAG-108 (satu tag `356938035643001` aktif setelah retry) diasersi lewat Expected b (langkah 12); Post Condition TC-GS-TAG-109 sama dengan Expected b.
