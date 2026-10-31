---
id: TC-GS-GSET-E2E-013-mobile-dialog-unsaved-changes-dan-change-currency
title: "Mobile dialog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-148
  - TC-GS-GSET-149
coverage:
  mobile: automated
---

# Mobile dialog

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android uji bersama, sehingga suite berjalan serial (`parallel: false`, S-09).
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di aplikasi Android di hook `before`; halaman Global Settings > General Settings dibuka di hook `beforeEach`.
- Guided Tooltip: spec ini mengecualikan hook suite untuk flag `guided_tooltip_seen_gs-general-settings` (spec mobile tidak memakai hook web suite). Hook `before` spec mencatat nilai awal flag akun aktor lalu menyetelnya true lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC, PRD, atau LLD); hook `after` memulihkan nilai awal.
- Data Pre-setup No 10 (record Client A): Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`. Data uji: Session Idle Timeout `1 hour` (TC-GS-GSET-148, tidak disimpan) dan Currency Code `USD` (TC-GS-GSET-149; `[Change Currency]` menyimpan `USD`).
- State global yang diubah: record Client A (Currency Code `USD` tersimpan di langkah 21) dan entri Changelog bertambah (audit trail permanen). Hook `after` memulihkan record ke baseline (Currency Code `IDR`) lewat PUT API di `global-settings/general-settings/API/openapi.yaml` walau spec gagal di tengah; suite berjalan serial.
- Kemampuan teknis: gesture ketuk, pembukaan bottom sheet, tombol Back perangkat Android, dan pembacaan preferensi/record tersimpan setelah membuka kembali halaman.

## Test Steps

### TC-GS-GSET-148: Dialog Unsaved Changes lewat tombol Back

1. Ketuk Select "Session Idle Timeout" lalu pilih `1 hour` pada bottom sheet
2. Ketuk tombol Back
3. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Cancel]` dan `[Leave]`
4. Ketuk `[Cancel]`
5. Verifikasi dialog tertutup
6. Verifikasi tetap berada di General Settings dengan Session Idle Timeout `1 hour`
7. Ketuk tombol Back lagi
8. Ketuk `[Leave]`
9. Verifikasi keluar dari halaman General Settings tanpa menyimpan
10. Buka kembali Global Settings > General Settings
11. Verifikasi Select "Session Idle Timeout" bernilai `30 minutes`

### TC-GS-GSET-149: Dialog Change Currency

12. Ketuk Select "Currency Code" lalu pilih `USD`
13. Ketuk `[Save]`
14. Verifikasi dialog Title "Change Currency"
15. Verifikasi Body dialog "Amounts already entered elsewhere in the app (e.g. Purchase Price) will not be converted — they'll simply be displayed under the new currency symbol. For example, an amount saved as 7,000 will still show as 7,000 — just with the new symbol. No conversion is applied. Are you sure you want to change the currency?"
16. Verifikasi dialog memiliki tombol `[Cancel]` dan `[Change Currency]`
17. Ketuk `[Cancel]`
18. Verifikasi dialog tertutup
19. Verifikasi form tetap unsaved dengan Currency Code `USD`
20. Ketuk `[Save]` lagi
21. Ketuk `[Change Currency]`
22. Verifikasi toast sukses "Success, general settings has been saved."

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Spec mobile Android (`coverage.mobile: automated`, tanpa `web`), mengikuti spec mobile suite Division. 22 langkah.
- Urutan TC sama dengan sumber (148 lalu 149). TC-GS-GSET-149 dijalankan terakhir karena menyimpan `USD`; TC-GS-GSET-148 tidak menyimpan perubahan sehingga record tetap baseline.
- Pecahan Expected: TC-GS-GSET-148 a menjadi langkah 3, b menjadi langkah 5 dan 6, c menjadi langkah 9, d menjadi langkah 11; TC-GS-GSET-149 a menjadi langkah 14 sampai 16, b menjadi langkah 18 dan 19, c menjadi langkah 22.
- Judul, isi, dan tombol dialog Change Currency dipecah satu `Verifikasi` per klausa (langkah 14 sampai 16) karena TC menyebut Title, Body, dan tombol sebagai klausa terpisah; dialog Unsaved Changes (langkah 3) satu `Verifikasi` karena teks dan kedua tombolnya disebut utuh dalam satu butir.
- Langkah 20 (`[Save]` lagi) membuka dialog Change Currency kedua, yang langsung dikonfirmasi di langkah 21; dialog kedua tidak diasersi ulang karena TC tidak memintanya.
- Tidak ada langkah penghubung; langkah 10 adalah langkah 6 TC-GS-GSET-148.
- Temuan untuk QA:
  - TC-GS-GSET-148 Expected c ("keluar dari halaman tanpa menyimpan") tidak menyebut halaman tujuan setelah `[Leave]`; spec mengasersi bahwa halaman General Settings tidak lagi tampil.
  - TC-GS-GSET-149 Post Condition tidak diasersi (tidak ada langkah observasi); record tersimpan `USD` dipulihkan oleh hook `after`.
