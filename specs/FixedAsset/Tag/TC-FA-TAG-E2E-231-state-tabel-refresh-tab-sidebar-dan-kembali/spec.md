---
id: TC-FA-TAG-E2E-231-state-tabel-refresh-tab-sidebar-dan-kembali
title: "State Tabel Paired: Refresh F5, Pindah Tab, dan Klik Ulang Menu TAG di Sidebar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-925
  - TC-FA-TAG-926
  - TC-FA-TAG-927
  - TC-FA-TAG-928
coverage:
  web: automated
---

# State Tabel Paired: Refresh F5, Pindah Tab, dan Klik Ulang Menu TAG di Sidebar

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk dataset tab Paired di bawah, termasuk penggantian dataset umum empat grup dengan dataset khusus 25 grup pada langkah 16 dan pemulihannya pada langkah 30 (hook `after` sebagai cadangan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup tab Paired (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup acuan | Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupAcuan` |
| Jumlah baris grup | Dataset khusus TC-FA-TAG-925 (precondition d): scope akun Total Control memuat total 25 baris grup (empat grup acuan ditambah 21 grup lain), dimuat pada langkah 16; TC-FA-TAG-926 sampai TC-FA-TAG-928 memakai dataset umum empat grup `grupAcuan` | `grup25Baris` |

- State yang diubah: state tampilan tab Paired (Search, Filter, Sort, page size, tab aktif) dan dataset tab Paired (diganti ke 25 grup pada langkah 16, dipulihkan ke dataset umum empat grup pada langkah 30); tidak ada perubahan data bisnis lain. Search, Filter, dan Sort dipulihkan oleh langkah 11 dan 28; page size dikembalikan ke 10 oleh langkah 29.

## Test Steps

### Refresh F5 mempertahankan tab aktif (TC-FA-TAG-926)

1. Klik Tab `To Be Returned`
2. Tekan F5
3. Verifikasi Tab `To Be Returned` tetap aktif setelah refresh
4. Klik Tab `Paired`

### State Search independen per tab (TC-FA-TAG-927)

5. Ketik Search `Forklift`, tekan Enter
6. Klik Tab `To Be Returned`
7. Verifikasi tab To Be Returned tidak membawa Search `Forklift`
8. Klik Tab `Paired`
9. Verifikasi Search `Forklift` terisi kembali
10. Verifikasi hasil Search `Forklift` tampil kembali

### Klik ulang menu TAG mereset state (TC-FA-TAG-928)

11. Klik menu `TAG` di sidebar
12. Verifikasi Search kosong
13. Verifikasi empat baris grup tampil
14. Verifikasi sort bawaan
15. Verifikasi halaman 1

### Refresh F5 mempertahankan state tab Paired (TC-FA-TAG-925)

16. Atur dataset tab Paired menjadi 25 baris grup (kunci `grup25Baris`) lewat fixture backend hingga tersimpan, lalu muat ulang halaman (F5)
17. Ketik Search `Ton`, tekan Enter
18. Klik ikon Filter
19. Isi Total Assets Min `10`
20. Klik `[Apply]`
21. Klik header Reported sekali
22. Ubah page size menjadi 25
23. Tekan F5
24. Verifikasi Search `Ton` tetap terisi
25. Verifikasi Filter Total Assets Min 10 tetap ter-Apply
26. Verifikasi sort Reported menaik tetap aktif
27. Verifikasi page size 25 tetap terpilih
28. Klik menu `TAG` di sidebar untuk mereset Search, Filter, dan Sort
29. Ubah page size menjadi 10
30. Pulihkan dataset tab Paired ke dataset umum empat grup lewat fixture backend

## Notes

- Langkah penghubung (S-03): langkah 4 (kembali ke tab Paired), 16 (memuat dataset 25 grup), 28 dan 29 (menutup TC-FA-TAG-925 dengan state default), 30 (memulihkan dataset umum empat grup), dan penggunaan state Search `Forklift` dari langkah 5 sebagai Precondition TC-FA-TAG-928 langkah 1 (Search `Forklift` sudah aktif dan diverifikasi pada langkah 9; langkah 11 adalah langkah 2 TC-FA-TAG-928).
- Urutan TC di dalam spec: TC-FA-TAG-926, 927, 928, lalu 925, karena TC-FA-TAG-925 memakai dataset khusus 25 grup (beda dari dataset umum empat grup yang dipakai TC-FA-TAG-926 sampai 928) sehingga dataset diganti satu kali di akhir (S-10).
- Pembagian TC lintas spec: TC-FA-TAG-929 (state pada tab browser baru, kelas c) ada di spec 387 dan TC-FA-TAG-930 (state sesudah kembali dari halaman lain) ada di spec 242.
- Temuan untuk QA:
  - TC-FA-TAG-925 Expected b "Filter Total Assets Min 10 tetap ter-Apply" tidak menyebut indikator yang diamati; spec mengasersi nilai field pada Filter Panel.
  - Post Condition semua TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
