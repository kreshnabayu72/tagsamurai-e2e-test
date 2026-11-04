---
id: TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi
title: "Timestamp Relatif Item Notifikasi di Dropdown Panel dan Notification Center"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-34
  - TC-FA-NOTIF-35
  - TC-FA-NOTIF-36
  - TC-FA-NOTIF-37
  - TC-FA-NOTIF-38
  - TC-FA-NOTIF-39
  - TC-FA-NOTIF-40
coverage:
  web: automated
---

# Timestamp Relatif Item Notifikasi di Dropdown Panel dan Notification Center

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Dropdown Panel, dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: satu notifikasi uji per TC pada seed Pre-setup #18 akun aktor, berumur tertentu terhadap jam fixture (18/06/26, zona Asia/Jakarta), ditukar fixture BE penukar varian seed (seed waktu) lewat langkah penghubung:

| TC | Umur notifikasi uji | Timestamp yang diasersi |
|---|---|---|
| TC-34 | 30 detik | `Just now` |
| TC-35 | 60 detik | `1m` |
| TC-36 | 59 menit | `59m` |
| TC-37 | 60 menit | `1h` |
| TC-38 | 23 jam | `23h` |
| TC-39 | 24 jam | `1d` |
| TC-40 | 6 hari | `6d` |

- Jam: batas eksak umur (60 detik, 60 menit, 24 jam) mensyaratkan jam server dan jam browser dibekukan pada waktu fixture selama tiap blok TC, dengan umur seed dihitung terhadap jam beku itu. Kemampuan menjalankan dan membekukan jam disediakan tim FE/BE (dinyatakan di `suite.md`); jam dipulihkan di hook `after`. Sesi UI dan sesi API aktor tetap valid selama jam dibekukan. Suite berjalan serial (`parallel: false`).
- Fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih dan penukar seed notifikasi, serta kemampuan jam server dan jam fixture.

## Test Steps

### TC-FA-NOTIF-34: Timestamp relatif berumur kurang dari 1 menit

1. Seed notifikasi uji berumur 30 detik lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
2. Klik Bell icon
3. Verifikasi timestamp item uji pada Dropdown Panel `Just now`
4. Klik `[Show All]` untuk membuka Notification Center
5. Verifikasi timestamp item yang sama pada Notification Center `Just now`

### TC-FA-NOTIF-35: Timestamp relatif berumur tepat 1 menit

6. Seed notifikasi uji berumur 60 detik lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
7. Klik Bell icon
8. Verifikasi timestamp item uji pada Dropdown Panel `1m`
9. Klik `[Show All]` untuk membuka Notification Center
10. Verifikasi timestamp item yang sama pada Notification Center `1m`

### TC-FA-NOTIF-36: Timestamp relatif berumur 59 menit

11. Seed notifikasi uji berumur 59 menit lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
12. Klik Bell icon
13. Verifikasi timestamp item uji pada Dropdown Panel `59m`
14. Klik `[Show All]` untuk membuka Notification Center
15. Verifikasi timestamp item yang sama pada Notification Center `59m`

### TC-FA-NOTIF-37: Timestamp relatif berumur tepat 60 menit

16. Seed notifikasi uji berumur 60 menit lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
17. Klik Bell icon
18. Verifikasi timestamp item uji pada Dropdown Panel `1h`
19. Klik `[Show All]` untuk membuka Notification Center
20. Verifikasi timestamp item yang sama pada Notification Center `1h`

### TC-FA-NOTIF-38: Timestamp relatif berumur 23 jam

21. Seed notifikasi uji berumur 23 jam lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
22. Klik Bell icon
23. Verifikasi timestamp item uji pada Dropdown Panel `23h`
24. Klik `[Show All]` untuk membuka Notification Center
25. Verifikasi timestamp item yang sama pada Notification Center `23h`

### TC-FA-NOTIF-39: Timestamp relatif berumur tepat 24 jam

26. Seed notifikasi uji berumur 24 jam lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
27. Klik Bell icon
28. Verifikasi timestamp item uji pada Dropdown Panel `1d`
29. Klik `[Show All]` untuk membuka Notification Center
30. Verifikasi timestamp item yang sama pada Notification Center `1d`

### TC-FA-NOTIF-40: Timestamp relatif berumur 6 hari

31. Seed notifikasi uji berumur 6 hari lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
32. Klik Bell icon
33. Verifikasi timestamp item uji pada Dropdown Panel `6d`
34. Klik `[Show All]` untuk membuka Notification Center
35. Verifikasi timestamp item yang sama pada Notification Center `6d`
36. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 11, 16, 21, 26, 31 (seed umur per TC, bekukan jam, muat ulang halaman; langkah "Klik Bell icon" berikutnya membuka Dropdown Panel kembali), langkah 4, 9, 14, 19, 24, 29, 34 (buka Notification Center dari Dropdown Panel; TC menulis "Buka Notification Center"), langkah 36 (pulihkan jam server dan jam browser ke waktu nyata setelah blok terakhir yang membekukan jam; jam beku tidak terbawa ke spec berikutnya, S-03 dan R-08).
- Ketujuh blok berurutan memuat langkah yang sama dengan parameter berbeda di tabel `## Prerequisites` (8b butir 7); jumlah langkah 36 (melewati ambang sekitar 35 langkah) berasal dari ekspansi tujuh blok lima langkah ditambah satu langkah pemulihan jam, semua blok satu kelas (fungsional format timestamp), dan tiap blok berdiri sendiri karena seed dan jam dikembalikan di awal blok.
- Tiap TC mengasersi dua surface (Dropdown Panel dan Notification Center) sehingga memiliki dua `Verifikasi`.
- Temuan untuk QA:
  - TC-34 sampai TC-40 menulis "seed waktu" tanpa menyebut mekanisme seeding umur atau pembekuan jam; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
