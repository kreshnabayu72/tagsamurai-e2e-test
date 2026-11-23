---
id: TC-FA-TDC-E2E-284-edit-versi-baru-declining-balance-rate-end-of-life-treatment-dan-useful-life-lewat-d-09
title: "Edit: Perubahan Declining Balance Rate, End-of-Life Treatment, atau Useful Life Membentuk Versi Baru Lewat Dialog D-09 dan Rate Tersimpan Tidak Dihitung Ulang"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-946
  - TC-FA-TDC-947
  - TC-FA-TDC-949
sourceRules: ["FATDC-LOGIC-04b.3", "FATDC-LOGIC-04b.5", "FATDC-LOGIC-04b.6", "F-FATDC-02.k5", "E-FATDC-15", "FATDC-LOGIC-03f.2", "FATDC-LOGIC-03f.5", "N-19"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04b.3": [3, 4, 10, 11, 14, 15]
  "FATDC-LOGIC-04b.5": [6, 7, 14, 15, 22, 23, 30, 31]
  "FATDC-LOGIC-04b.6": [20, 26, 27, 30, 31]
  "F-FATDC-02.k5": [5, 6, 10, 21, 22, 26]
  "E-FATDC-15": [6, 10, 22, 26]
  "FATDC-LOGIC-03f.2": [37, 38, 39, 43]
  "FATDC-LOGIC-03f.5": [37, 38, 39, 43]
  "N-19": [37, 38, 39, 43]
coverage:
  web: automated
---

# Edit: Perubahan Declining Balance Rate, End-of-Life Treatment, atau Useful Life Membentuk Versi Baru Lewat Dialog D-09 dan Rate Tersimpan Tidak Dihitung Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; awalan `DBE-` tidak dipakai TC lain; kemampuan seeding disediakan tim FE/BE). Setiap class: Non-building, Useful Life 8, Straight Line dan Declining Balance (Declining Balance Rate 25, End-of-Life Treatment `Charge in final period`), hanya satu versi (Current tanpa Effective From), Active, Used By 0, tanpa versi Scheduled.

| Class Code | Dipakai TC |
|---|---|
| `DBE-08` | TC-FA-TDC-946 |
| `DBE-09` | TC-FA-TDC-947 |
| `DBE-11` | TC-FA-TDC-949 |

- Tabel memuat tujuh class seed bawaan dan tiga class milik spec (10 baris dalam satu halaman); baris target dibuka lewat Search Class Code (8b.13, R-23).
- Tahun pajak 2026 belum tertutup (Exported through belum mencapai Des 2026) sehingga Effective From "Jan 2026" ditawarkan; TC tidak menyebutnya (lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-946: Edit: mengubah hanya Declining Balance Rate membentuk versi baru lewat D-09

1. Ketik Search `DBE-08`, tekan Enter
2. Klik link Class Code `DBE-08` pada tabel
3. Ganti Declining Balance Rate menjadi `30`
4. Verifikasi helper "Equivalent to 2.4× the straight-line rate"
5. Klik `[Save]`
6. Verifikasi dialog D-09 berjudul "Save Changes" muncul (bukan simpan langsung)
7. Verifikasi label field Effective From berpenanda wajib (`Effective From *`)
8. Pilih Effective From "Jan 2026"
9. Klik `[Apply]`
10. Verifikasi toast sukses "Success, tax depreciation class has been updated."
11. Verifikasi baris `DBE-08`: Straight Line Rate "12.5%", Declining Balance Rate "30%", Effective From "Jan 2026"
12. Klik link Class Code `DBE-08` pada tabel
13. Klik tautan View versions
14. Verifikasi modal Versions: baris "Jan 2026" berstatus "Current" dengan Declining Balance Rate "30%"
15. Verifikasi modal Versions: baris "—" berstatus "Past" dengan Declining Balance Rate "25%"
16. Tutup modal Versions
17. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-947: Edit: mengubah hanya End-of-Life Treatment membentuk versi baru lewat D-09

18. Ganti isi kotak search dengan `DBE-09`, tekan Enter
19. Klik link Class Code `DBE-09` pada tabel
20. Ganti End-of-Life Treatment menjadi `Switch to straight-line`
21. Klik `[Save]`
22. Verifikasi dialog D-09 berjudul "Save Changes" muncul (bukan simpan langsung)
23. Verifikasi label field Effective From berpenanda wajib (`Effective From *`)
24. Pilih Effective From "Jan 2026"
25. Klik `[Apply]`
26. Verifikasi toast sukses "Success, tax depreciation class has been updated."
27. Verifikasi baris `DBE-09` tidak berubah: Straight Line Rate "12.5%", Declining Balance Rate "25%", Effective From "Jan 2026"
28. Klik link Class Code `DBE-09` pada tabel
29. Klik tautan View versions
30. Verifikasi modal Versions: baris "Jan 2026" berstatus "Current" dengan End-of-Life Treatment "Switch to straight-line"
31. Verifikasi modal Versions: baris "—" berstatus "Past" dengan End-of-Life Treatment "Charge in final period"
32. Tutup modal Versions
33. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-949: Edit: mengubah Useful Life tidak menghitung ulang Declining Balance Rate yang tersimpan

34. Ganti isi kotak search dengan `DBE-11`, tekan Enter
35. Klik link Class Code `DBE-11` pada tabel
36. Ganti Useful Life menjadi `10`
37. Verifikasi Straight Line Rate (%) "10"
38. Verifikasi Declining Balance Rate (%) tetap "25"
39. Verifikasi helper "Equivalent to 2.5× the straight-line rate"
40. Klik `[Save]` hingga dialog D-09 muncul
41. Pilih Effective From "Jan 2026"
42. Klik `[Apply]`
43. Verifikasi baris `DBE-11`: Useful Life (years) "10", Straight Line Rate "10%", Declining Balance Rate "25%", Effective From "Jan 2026"
44. Klik `(←)` pada kotak Search

## Notes

- Alasan melewati sekitar 35 langkah (44 langkah): ketiga TC satu topik Edit yang membentuk versi baru lewat D-09 dengan alur identik dan berdiri sendiri (tiap TC memakai class sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna).
- Langkah penghubung (S-03): langkah 1, 18, dan 34 (Search Class Code untuk menemukan baris target; R-16); langkah 16, 17, 32, dan 33 (menutup modal Versions dan Drawer Edit tanpa perubahan, tanpa dialog `Unsaved Changes`); langkah 40 (membuka dialog D-09; TC-FA-TDC-949 tidak punya Expected untuk dialog itu sehingga tanpa `Verifikasi`); langkah 44 (mengosongkan Search; frasa baku `(←)` pada kotak Search, S-09).
- Pencatatan log L-03 (Post Condition TC-FA-TDC-946 dan TC-FA-TDC-947: "entri log L-03 untuk Declining Balance Rate dan Effective From" dan "untuk End-of-Life Treatment dan Effective From") tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01) dan dicatat di Temuan untuk QA. Asersi pencatatan log L-03 ada di spec 286 (TC-FA-TDC-953 dan TC-FA-TDC-954).
- Asumsi: sesudah `[Apply]` yang sukses dialog D-09 dan Drawer Edit tertutup sehingga langkah 12 dan 28 membuka Drawer Edit lagi (TC-FA-TDC-946 dan TC-FA-TDC-947 langkah 6 menulis "Buka Drawer Edit ... lalu klik tautan View versions"); perlu konfirmasi FE.
- Temuan untuk QA:
  - TC-FA-TDC-946, 947, dan 949 memilih Effective From "Jan 2026" pada tanggal sistem uji 15 Okt 2026 tanpa menyebut Exported through; spec mengasumsikan tahun pajak 2026 belum tertutup (V-21).
  - TC-FA-TDC-946 dan TC-FA-TDC-947 Post Condition menyebut entri log L-03 "detail di section 5" tanpa langkah observasi; log L-03 untuk perubahan ini diasersi TC-FA-TDC-953 dan TC-FA-TDC-954 (spec 286), bukan di spec ini.
  - TC-FA-TDC-949 langkah 3 menyebut "dialog D-09 muncul" tanpa Expected; spec menulis langkah 40 tanpa `Verifikasi`. Expected a menyebut helper "Equivalent to 2.5× the straight-line rate" pada Useful Life 10 dengan Declining Balance Rate 25.
  - TC-FA-TDC-949 Post Condition "Versi Current menyimpan Useful Life 10 dan Declining Balance Rate 25" sudah teramati lewat langkah 43 (baris tabel).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
