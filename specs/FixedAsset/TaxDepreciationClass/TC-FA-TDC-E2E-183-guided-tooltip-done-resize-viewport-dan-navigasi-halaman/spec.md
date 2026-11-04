---
id: TC-FA-TDC-E2E-183-guided-tooltip-done-resize-viewport-dan-navigasi-halaman
title: "Guided Tooltip: Done, Resize Viewport, dan Navigasi Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-656
  - TC-FA-TDC-657
  - TC-FA-TDC-658
coverage:
  web: automated
---

# Guided Tooltip: Done, Resize Viewport, dan Navigasi Halaman

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite dan seeding mengikuti `suite.md`. Pengecualian flag Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tax-depreciation-class` true; spec ini menghapus flag sesudah hook pada langkah 1, 10, dan 19 sebagai keadaan awal tiap blok TC, dan hook `after` memulihkan flag ke true.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.seedClasses` berisi tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) belum diubah. Data Dinamis: tidak ada.
- Kemampuan teknis: menghapus flag Guided Tooltip akun (disediakan tim FE/BE; nama kunci flag dari TC); mengubah dan memulihkan ukuran viewport browser; navigasi baru ke layar Settings > Accounting > Tax Depreciation Class.
- State global yang diubah: flag Guided Tooltip akun Total Control dan ukuran viewport browser; viewport dipulihkan pada langkah 18 dan flag diselesaikan lewat `[Skip]` pada langkah 27 (keadaan akhir true seperti keadaan awal suite).

## Test Steps

### TC-FA-TDC-656: Step terakhir, Next berubah menjadi Done dan menyimpan flag seen

1. Hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
2. Buka tab `Tax Depreciation Class` (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
3. Klik `[Next]` lima kali sampai Step 6
4. Verifikasi pada Step 6 tombol `[Next]` berubah menjadi `[Done]`
5. Klik `[Done]`
6. Verifikasi walkthrough tertutup
7. Muat ulang halaman (F5)
8. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
9. Verifikasi walkthrough tidak muncul otomatis setelah F5

### TC-FA-TDC-657: Resize viewport di tengah walkthrough menutupnya tanpa menyimpan flag seen

10. Hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
11. Buka tab `Tax Depreciation Class` (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
12. Klik `[Next]` (walkthrough dibiarkan di Step 2)
13. Verifikasi Step 2 of 6 tampil
14. Ubah ukuran viewport browser
15. Verifikasi walkthrough tertutup setelah resize
16. Muat ulang halaman (F5)
17. Verifikasi walkthrough muncul lagi otomatis dari Step 1 of 6
18. Pulihkan ukuran viewport browser

### TC-FA-TDC-658: Navigasi ke halaman lain di tengah walkthrough tidak menyimpan flag seen

19. Hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
20. Buka tab `Tax Depreciation Class` (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
21. Klik `[Next]` (walkthrough dibiarkan di Step 2)
22. Verifikasi Step 2 of 6 tampil
23. Klik tab `Asset Class`
24. Verifikasi walkthrough tertutup saat berpindah tab
25. Klik tab `Tax Depreciation Class`
26. Verifikasi walkthrough muncul lagi otomatis dari Step 1 of 6
27. Klik `[Skip]`

## Notes

- Asersi tambahan di luar Expected TC (S-03): langkah 8 (halaman termuat sebagai anchor absence walkthrough, 8b.2), langkah 13 dan 22 (Step 2 tampil sebelum asersi "tertutup"; transisi walkthrough diamati sebelum state berubah, 8b.5).
- Langkah penghubung (S-03): langkah 1, 2, 10, 11, 19, dan 20 (menghapus flag dan membuka layar awal untuk kunjungan pertama), langkah 12 dan 21 (`[Next]` menuju Step 2 sesuai "biarkan walkthrough di Step 2"), langkah 18 (memulihkan viewport), langkah 27 (menutup walkthrough dengan `[Skip]`).
- Pada langkah 17 flag seen tidak tersimpan sehingga walkthrough muncul lagi dari Step 1; pada langkah 26 hal yang sama berlaku sesudah kembali ke tab.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-656, TC-FA-TDC-657, dan TC-FA-TDC-658 menyebut "Flag seen belum ada" tanpa cara menyetelnya; mekanismenya disediakan tim FE/BE (S-13).
  - TC-FA-TDC-657 tidak menyebut ukuran viewport yang dipakai dan cara memulihkannya; spec memulihkan viewport pada langkah 18.
  - TC-FA-TDC-656 butir c dan TC-FA-TDC-657 butir a mengasersi ketiadaan atau penutupan walkthrough; spec menambah anchor sebelum asersi.
