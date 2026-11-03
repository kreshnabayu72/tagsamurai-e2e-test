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
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk dataset tab Paired di bawah; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup tab Paired (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup acuan | Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupAcuan` |
| Jumlah baris grup | Scope akun Total Control memuat total 25 baris grup | `grup25Baris` |

- State yang diubah: hanya state tampilan tab Paired (Search, Filter, Sort, page size, tab aktif); tidak ada perubahan data bisnis. Filter, Search, dan Sort dipulihkan oleh langkah 12, 13, dan 24; page size dikembalikan ke 10 oleh langkah 13.

## Test Steps

### Refresh F5 mempertahankan state tab Paired (TC-FA-TAG-925)

1. Ketik Search `Ton`, tekan Enter
2. Klik ikon Filter
3. Isi Total Assets Min `10`
4. Klik `[Apply]`
5. Klik header Reported sekali
6. Ubah page size menjadi 25
7. Tekan F5
8. Verifikasi Search `Ton` tetap terisi
9. Verifikasi Filter Total Assets Min 10 tetap ter-Apply
10. Verifikasi sort Reported menaik tetap aktif
11. Verifikasi page size 25 tetap terpilih
12. Klik menu `TAG` di sidebar untuk mereset Search, Filter, dan Sort
13. Ubah page size menjadi 10

### Refresh F5 mempertahankan tab aktif (TC-FA-TAG-926)

14. Klik Tab `To Be Returned`
15. Tekan F5
16. Verifikasi Tab `To Be Returned` tetap aktif setelah refresh
17. Klik Tab `Paired`

### State Search independen per tab (TC-FA-TAG-927)

18. Ketik Search `Forklift`, tekan Enter
19. Klik Tab `To Be Returned`
20. Verifikasi tab To Be Returned tidak membawa Search `Forklift`
21. Klik Tab `Paired`
22. Verifikasi Search `Forklift` terisi kembali
23. Verifikasi hasil Search `Forklift` tampil kembali

### Klik ulang menu TAG mereset state (TC-FA-TAG-928)

24. Klik menu `TAG` di sidebar
25. Verifikasi Search kosong
26. Verifikasi empat baris grup tampil
27. Verifikasi sort bawaan
28. Verifikasi halaman 1

## Notes

- Langkah penghubung (S-03): langkah 12 dan 13 (menutup TC-FA-TAG-925 dengan state default), 17 (kembali ke tab Paired), dan penggunaan state Search `Forklift` dari langkah 18 sebagai Precondition TC-FA-TAG-928 langkah 1 (Search `Forklift` sudah aktif dan diverifikasi pada langkah 22; langkah 24 adalah langkah 2 TC-FA-TAG-928).
- Pembagian TC lintas spec: TC-FA-TAG-929 dan TC-FA-TAG-930 (state pada tab browser baru dan sesudah kembali dari halaman lain) ada di spec 242.
- Temuan untuk QA:
  - TC-FA-TAG-928 Expected "empat baris grup tampil" bertentangan dengan Data Uji TC-FA-TAG-925 ("scope memuat total 25 baris grup", page size bawaan 10): pada page size 10 tabel menampilkan 10 baris, bukan empat. Spec mengikuti teks TC (langkah 26); QA perlu menetapkan angka yang benar.
  - TC-FA-TAG-925 Expected b "Filter Total Assets Min 10 tetap ter-Apply" tidak menyebut indikator yang diamati; spec mengasersi nilai field pada Filter Panel.
  - Post Condition semua TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
