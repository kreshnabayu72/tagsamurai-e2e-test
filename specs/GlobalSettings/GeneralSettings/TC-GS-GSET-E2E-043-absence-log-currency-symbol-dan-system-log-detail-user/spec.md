---
id: TC-GS-GSET-E2E-043-absence-log-currency-symbol-dan-system-log-detail-user
title: "Absence log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-110
  - TC-GS-GSET-113
coverage:
  web: automated
---

# Absence log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Spec tidak membuat data dinamis. Aksi nyata tiap TC: TC-GS-GSET-110 menyimpan Currency Code `USD`; TC-GS-GSET-113 menyimpan Session Idle Timeout `1 hour`. Tiap TC punya baseline sendiri.
- Baseline log (S-12): `{nCL0}` (total entri Modal Changelog) dan `{nAL0}` (total entri Activity Log dengan Search `General Settings`) dicatat pada langkah 1 dan 2, sebelum Save TC-GS-GSET-110. TC-GS-GSET-113 mencari kata kunci `General Settings` pada tab System Log (tanpa angka absolut) setelah Save toast sukses.
- Kemampuan teknis: (a) membaca jumlah total entri (total data pada Pagination) Modal Changelog dan Activity Log; (b) membaca tab System Log pada Global Settings > User > Detail Budi Santoso; (c) sesi API Total Control yang memulihkan record Client A ke baseline Pre-setup No 10 lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`; klien HTTP dan penangkapan token disediakan tim FE) pada langkah 25, dengan muat ulang halaman sesudahnya.
- State global yang diubah: Currency Code (TC-GS-GSET-110) dan Session Idle Timeout (TC-GS-GSET-113) record General Settings Client A, dipulihkan lewat langkah 25 serta hook `beforeEach` dan `after` suite. Entri log bersifat audit trail permanen dan tidak dihapus. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4).

## Test Steps

### TC-GS-GSET-110: Mengubah Currency Code tidak mencatat baris Currency Symbol

1. Buka Modal Changelog, catat jumlah total entri sebagai `{nCL0}`, lalu tutup modal
2. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter, catat jumlah total entri sebagai `{nAL0}`, lalu buka Global Settings > General Settings
3. Pilih Currency Code `USD`
4. Klik `[Save]`, lalu klik `[Change Currency]` pada dialog Change Currency
5. Tunggu aksi selesai (tombol `[Save]` disabled kembali)
6. Buka Modal Changelog
7. Verifikasi jumlah total entri Changelog `{nCL0}` + 1 (tepat 1 baris baru)
8. Verifikasi baris teratas Changelog berisi Field `Currency Code`
9. Ketik Search `Currency Symbol`, tekan Enter
10. Verifikasi empty state `No results found` (tidak ada baris Field `Currency Symbol` di Modal Changelog)
11. Ganti isi kotak search dengan `Decimal Places`, tekan Enter
12. Verifikasi empty state `No results found` (tidak ada baris Field `Decimal Places` di Modal Changelog)
13. Klik `(←)` pada kotak Search
14. Buka panel Filter, lalu buka dropdown Field
15. Verifikasi dropdown Field memuat opsi `Currency Code`
16. Verifikasi opsi dropdown Field tidak memuat `Currency Symbol` maupun `Decimal Places`
17. Tutup panel Filter, lalu tutup Modal Changelog
18. Buka Global Settings > Activity Log, ketik Search `General Settings`, tekan Enter
19. Verifikasi jumlah total entri Activity Log `{nAL0}` + 1 (tepat 1 baris baru)
20. Verifikasi baris teratas Activity Log berisi Field `Currency Code`
21. Ganti isi kotak search dengan `Currency Symbol`, tekan Enter
22. Verifikasi empty state `No results found` (tidak ada baris Field `Currency Symbol` di Activity Log)
23. Ganti isi kotak search dengan `Decimal Places`, tekan Enter
24. Verifikasi empty state `No results found` (tidak ada baris Field `Decimal Places` di Activity Log)
25. Pulihkan record Client A ke baseline Pre-setup No 10 lewat sesi API, lalu buka Global Settings > General Settings

### TC-GS-GSET-113: Save General Settings tidak menulis System Log pada Detail User

26. Pilih Session Idle Timeout `1 hour`
27. Klik `[Save]`
28. Verifikasi toast sukses `Success, general settings has been saved.`
29. Buka Global Settings > User > Detail Budi Santoso > tab System Log
30. Verifikasi tab System Log memuat entri login terakhir user Budi Santoso
31. Ketik Search `General Settings`, tekan Enter
32. Verifikasi empty state `No results found` (tab System Log tidak memuat entri perubahan General Settings)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-110 dan TC-GS-GSET-113). Mode: FE+BE. Kelas: absence log (prinsip 13 butir g); tiap TC punya aksi nyata dan baseline sendiri (S-05).
- Anchor positif absence (bagian 8b butir 2): langkah 7 dan 8 (entri Currency Code hadir di Modal Changelog), langkah 15 (opsi pembanding `Currency Code` di dropdown Field), langkah 19 dan 20 (entri Currency Code hadir di Activity Log), dan empty state `No results found` pada Search sebagai anchor absence hasil Search. Pada TC-GS-GSET-113 anchor adalah toast sukses Save (langkah 28, ditambahkan sebagai anchor pemicu; bukan Expected TC) dan entri login terakhir (langkah 30, sesuai Expected TC).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 6, 9, 11, 13, 14, 17, 18, 21, 23, 25, 29, dan 31 (membuka, menutup, dan mencari di surface log, serta memulihkan baseline); langkah 5 (tunggu Save selesai sebelum membuka surface lain). Search `General Settings` pada Activity Log membatasi hitungan ke entri Object `General Settings` (hanya kolom Date yang dikecualikan dari Search, NC-16).
- Urutan TC mengikuti TC. Pemulihan baseline pada langkah 25 memenuhi precondition TC-GS-GSET-113 (record baseline Pre-setup No 10).
- Spec ini adalah spec absence untuk TC-GS-GSET-110 dan TC-GS-GSET-113; TC-GS-GSET-110 juga memuat `Verifikasi` presence baris Currency Code (langkah 7, 8, 19, 20) sebagai anchor. TC-GS-GSET-104 (presence Currency Code) ada di spec 041.
- Temuan untuk QA:
  - TC-GS-GSET-113 Expected hanya menyebut "entri login terakhir tetap tampil" sebagai anchor tanpa kolom atau nilai Action; spec mengasersi keberadaan entri login terakhir tanpa kolom. Cara mengenali entri perubahan General Settings pada System Log tidak ditulis TC; spec memakai Search `General Settings`.
  - TC-GS-GSET-110 Expected b ("Opsi filter Field tidak memuat `Currency Symbol` maupun `Decimal Places`") mengandalkan opsi filter yang diisi dari data tabel (NC-18); setelah Save Currency, opsi `Currency Code` hadir sebagai pembanding.
