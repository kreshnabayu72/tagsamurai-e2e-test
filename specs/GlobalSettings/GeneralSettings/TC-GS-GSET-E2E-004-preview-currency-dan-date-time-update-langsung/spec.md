---
id: TC-GS-GSET-E2E-004-preview-currency-dan-date-time-update-langsung
title: "Preview live"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-30
  - TC-GS-GSET-31
  - TC-GS-GSET-32
coverage:
  web: automated
---

# Preview live

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): login akun aktor, flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen, record Client A dipulihkan ke baseline, dan halaman Global Settings > General Settings dibuka di `beforeEach`.
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`.
- Data Pre-setup No 10 (record Client A): Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`. Referensi Preview No 11: Jumat 17 Maret 2023 14:30, nominal `5.000,00`. Currency Code `USD`, `EUR`, `IDR` (No 12; label dan simbol `USD`/`EUR` ditentukan programmer, NC-10): `[simbol opsi X]` adalah simbol pada label opsi X yang dibaca dari dropdown saat memilih (langkah 1 dan 5), bukan literal. Time Zone Lain (No 13) dipetakan ke `UTC` (label `(UTC+00:00) UTC, Reykjavik, Accra`, PRD §4.3a); label dibaca dari dropdown saat memilih (langkah 10).
- Spec tidak menekan `[Save]`; semua pilihan hanya di form, dan langkah 23 mengembalikan Date Format `dd/MM/yy` dan Time Format `HH:mm` ke nilai tersimpan sehingga tidak ada perubahan belum disimpan saat spec berikutnya membuka halaman. Tidak ada state global yang diubah.

## Test Steps

### TC-GS-GSET-30: Preview Currency ter-update langsung

1. Pilih Currency Code `USD` dan catat simbol pada label opsinya sebagai `[simbol opsi USD]`
2. Verifikasi Preview text Currency "[simbol opsi USD] 5.000,00"
3. Verifikasi angka Preview memakai pemisah ribuan titik, pemisah desimal koma, dan 2 digit desimal
4. Pilih Currency Code `EUR`
5. Verifikasi Preview text Currency "[simbol opsi EUR] 5.000,00" (simbol dicatat dari label opsi `EUR`)
6. Verifikasi angka Preview memakai pemisah ribuan titik, pemisah desimal koma, dan 2 digit desimal
7. Pilih Currency Code `IDR`
8. Verifikasi Preview text Currency "Rp 5.000,00"
9. Verifikasi angka Preview memakai pemisah ribuan titik, pemisah desimal koma, dan 2 digit desimal

### TC-GS-GSET-32: Time Zone tidak mengubah Preview Date & Time

10. Pilih Time Zone `UTC` (Time Zone Lain) dan catat label opsinya
11. Verifikasi Preview Date & Time tetap "17/03/23 14:30"
12. Verifikasi Button "Save" enabled

### TC-GS-GSET-31: Preview Date & Time mengikuti kombinasi Date Format dan Time Format

13. Pilih Time Zone `Asia/Jakarta` kembali
14. Verifikasi Preview Date & Time awal (`dd/MM/yy` + `HH:mm`) "17/03/23 14:30"
15. Pilih Date Format `M/d/yy`
16. Verifikasi Preview Date & Time "3/17/23 14:30"
17. Pilih Date Format `dd MMM yy`
18. Verifikasi Preview Date & Time "17 Mar 23 14:30"
19. Pilih Date Format `DDD, MMM dd, yy`
20. Verifikasi Preview Date & Time "Fri, Mar 17, 23 14:30"
21. Pilih Date Format `DDD, MMM dd, yyyy` dan Time Format `hh:mm a`
22. Verifikasi Preview Date & Time "Fri, Mar 17, 2023 02:30 PM"
23. Pilih kembali Date Format `dd/MM/yy` dan Time Format `HH:mm`

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. 23 langkah.
- Urutan TC di dalam spec: TC-GS-GSET-30, TC-GS-GSET-32, TC-GS-GSET-31. TC-GS-GSET-32 dijalankan sebelum TC-GS-GSET-31 supaya Date Format dan Time Format masih bernilai baseline (`dd/MM/yy`, `HH:mm`) ketika Preview "17/03/23 14:30" diasersi, dan supaya "Save enabled" (langkah 12) hanya berasal dari perubahan Time Zone (setelah langkah 7 Currency Code kembali ke nilai tersimpan `IDR`, form identik dengan record dan Save disabled, NC-12). Langkah 13 mengembalikan Time Zone ke nilai tersimpan sebagai langkah penghubung (tanpa `Verifikasi`, S-09).
- Pecahan Expected TC-GS-GSET-30: a menjadi langkah 2, b menjadi langkah 5, c menjadi langkah 8, d menjadi langkah 3, 6, dan 9 (satu `Verifikasi` per pilihan Currency).
- Langkah 23 adalah langkah penghubung (tanpa `Verifikasi`) yang mengembalikan form ke nilai tersimpan supaya form tidak dirty di akhir spec (S-09).
- TC-GS-GSET-31 langkah 1 (Amati Preview awal) diasersi di langkah 14 setelah Time Zone dikembalikan ke `Asia/Jakarta`.
- Temuan untuk QA:
  - "Time Zone Lain" di TC-GS-GSET-32 tidak punya nilai pasti karena daftar opsi Time Zone ditentukan programmer (NC-09); spec memakai `UTC` sebagai satu-satunya opsi selain `Asia/Jakarta` yang labelnya dikunci PRD §4.3a.
  - Label dan simbol opsi `USD` dan `EUR` tidak dikunci di PRD (NC-10); spec membaca simbol dari label opsi saat memilih dan memakainya pada langkah 2 dan 5.
