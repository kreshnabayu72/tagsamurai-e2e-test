---
id: TC-FA-NOTIF-E2E-114-reset-lewat-show-all-dan-kombinasi-empat-kontrol
title: "Reset Kontrol lewat Show All dan Kombinasi Tab, Search, Filter, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-226
  - TC-FA-NOTIF-228
coverage:
  web: automated
---

# Reset Kontrol lewat Show All dan Kombinasi Tab, Search, Filter, dan Sort

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; env var didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi; N-05 `Your Total Control access was removed` Unread bertipe `access_total_control_removed`) milik akun aktor; Pre-setup #18 memuat sedikitnya dua item Unread bertipe `access_total_control_removed` dengan timestamp berbeda (prasyarat TC-FA-NOTIF-228), dipulihkan fixture BE pemulih di hook `before` dan `after`. Spec hanya membaca data. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-226: Masuk kembali lewat [Show All] mereset Tab dan kontrol ke default

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Klik Tab `Unread`
3. Ketik Search `access`, tekan Enter
4. Klik Bell icon, lalu klik `[Show All]`
5. Verifikasi Tab `All` aktif
6. Verifikasi kotak Search kosong (tanpa Search)
7. Verifikasi Sort `Newest` aktif
8. Verifikasi indikator titik pada icon Filter tidak tampil (tanpa Filter)

### TC-FA-NOTIF-228: Kombinasi empat kontrol Tab, Search, Filter, dan Sort bersamaan

9. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
10. Klik Tab `Unread`, ketik Search `access`, tekan Enter
11. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
12. Klik toggle Sort dari `Newest` ke `Oldest`
13. Scroll sampai akhir list hingga seluruh item termuat
14. Verifikasi list memuat sedikitnya dua item, termasuk N-05
15. Verifikasi sedikitnya dua item pada list memiliki timestamp berbeda
16. Verifikasi setiap item yang tampil berstatus Unread (tidak ada item Read)
17. Verifikasi setiap item yang tampil bertipe `access_total_control_removed`
18. Verifikasi setiap item yang tampil memuat `access`
19. Verifikasi item terurut Oldest
20. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat TC-226 dan TC-228; TC lain pada topik Search, Filter, dan Sort ada di spec 046 sampai 053 dan 115.
- Langkah penghubung (S-03): langkah 1 (precondition TC), 9 dan 20 (masuk kembali lewat `[Show All]`), 13 (memuat seluruh item agar asersi universal mencakup semua item).
- Asersi tambahan di luar Expected TC (S-03): langkah 14 dan 15 memeriksa item pembanding (sedikitnya dua item dengan timestamp berbeda, sesuai Expected TC-228) sebelum asersi universal langkah 16 sampai 19 (8b butir 2) dan sebelum asersi urutan Oldest; langkah 8 (tanpa Filter) mengasersi kondisi kontrol default yang disebut Expected TC-226 ("tanpa Filter").
- Temuan untuk QA:
  - TC-226 langkah 2 menyebut "terapkan Search `access`" pada Tab `Unread`; spec menerapkan Search sesudah Tab `Unread` dan tidak menerapkan Sort maupun Filter sebelum `[Show All]`, sehingga reset Sort dan Filter ke default hanya teramati sebagai keadaan default.
  - TC-228 butir "terurut Oldest" tidak menyebut cara membaca urutan; spec mengasersi urutan berdasarkan waktu pembuatan menaik.
