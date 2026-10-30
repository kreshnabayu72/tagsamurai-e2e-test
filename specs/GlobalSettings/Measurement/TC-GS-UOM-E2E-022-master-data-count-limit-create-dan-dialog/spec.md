---
id: TC-GS-UOM-E2E-022-master-data-count-limit-create-dan-dialog
title: "Master Data Count Limit: Create di Batas, Dialog Cannot Add Unit, dan Form Tetap Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UOM-63
  - TC-GS-UOM-64
  - TC-GS-UOM-65
  - TC-GS-UOM-66
coverage:
  web: automated
---

# Master Data Count Limit: Create di Batas, Dialog Cannot Add Unit, dan Form Tetap Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas volume data dan state tenant (prinsip 13e): tenant Client Limit berisi 999 unit.
- Hook suite (login akun default, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`; flag disetel true untuk akun Client Limit oleh hook suite.
- Akun: Total Control Client Limit, Wulan Sari, `totalControl_automated_qaTeam4@qwertysystem.net`, password `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_LIMIT_TC_PASSWORD` dan `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Client Limit (disediakan tim FE): Master Data Count Limit 1.000 dan Selection Limit 100 (nilai minimum, diatur lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits), berisi tepat 999 unit `Lim 001` sampai `Lim 999` (D-28, dibuat lewat Import Type Measurement). Hook `before` memastikan jumlah unit 999 dan limit 1.000.
- Data dinamis milik spec (suffix per run dan nomor spec): `Chain {runId}-022` (Symbol `ch`, D-12) dibuat sukses di TC-GS-UOM-66; `Link {runId}-022` (Symbol `li`) ditolak; `Rod {runId}-022` (Symbol `rd`) ditolak di TC-GS-UOM-65; `Admin Slot {runId}-022` dibuat oleh admin lain lewat sesi API sebagai pemicu ceiling di TC-GS-UOM-65 (akun admin lain tidak ada di Tabel Pre-setup TC: disediakan tim FE, S-13).
- State global bersama: tenant Client Limit juga dipakai spec Master Data Count Limit lain (race slot terakhir) dengan syarat 999 unit saat mulai; suite berjalan serial (`parallel: false`). Spec ini menaikkan jumlah unit menjadi 1.000 di langkah 3, menurunkannya menjadi 999 di langkah 26, dan menaikkannya lagi menjadi 1.000 di langkah 30.
- Cleanup (hook `after`, tidak berasumsi langkah spec berhasil penuh): hapus lewat API `Chain {runId}-022`, `Link {runId}-022`, `Rod {runId}-022`, dan `Admin Slot {runId}-022` bila ada; pulihkan `Lim 999` bila terhapus (dibuat ulang lewat API Measurement atau Import Type Measurement, mekanisme disediakan tim FE) sehingga tenant kembali tepat 999 unit `Lim 001` sampai `Lim 999`.
- Kemampuan teknis: pembacaan jumlah unit Client Limit lewat API; sesi API aktor (lihat `suite.md`, bagian Hook suite) untuk admin lain yang membuat Measurement sebagai pemicu ceiling.

## Test Steps

### TC-GS-UOM-66: Create ke-N tepat di batas berhasil dan ke-N+1 ditolak

1. Klik [+ Unit]
2. Centang checkbox `Stay on this form after submitting`
3. Isi Unit Name `Chain {runId}-022` dan Symbol `ch`, klik [Submit]
4. Verifikasi toast sukses: "Success, unit has been created."
5. Isi Unit Name `Link {runId}-022` dan Symbol `li`, klik [Submit]
6. Verifikasi dialog `Cannot Add Unit` tampil
7. Klik [OK]
8. Klik `[✕]` untuk menutup form yang masih dirty
9. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
10. Klik [Leave]
11. Ketik Search `Link {runId}-022`, tekan Enter
12. Verifikasi empty state `No results found` (Title) untuk Search `Link {runId}-022`, sehingga `Link {runId}-022` tidak tersimpan (tidak ada di tabel)
13. Klik `(←)` pada kotak Search

### TC-GS-UOM-63: Klik [+ Unit] saat jumlah Measurement mencapai ceiling System Limits menampilkan D-06

14. Verifikasi tombol `[+ Unit]` tampil dan enabled
15. Klik [+ Unit]
16. Verifikasi dialog `Cannot Add Unit` dengan body `You've reached the limit of {limit} units. Contact support if you need a higher limit.` dan tombol `[OK]`, dengan `{limit}` terisi nilai Master Data Count Limit aktif (1.000)
17. Verifikasi dialog tidak memuat CTA upgrade
18. Verifikasi form Create tidak terbuka

### TC-GS-UOM-64: OK pada D-06 menutup dialog dan Esc tidak menutupnya

19. Tekan Esc pada dialog `Cannot Add Unit` dari langkah 15
20. Verifikasi dialog `Cannot Add Unit` tetap tampil
21. Klik [OK]
22. Verifikasi dialog tertutup
23. Verifikasi jumlah Measurement Client Limit lewat API tetap 1.000 (tidak ada record dibuat)

### TC-GS-UOM-65: Ceiling tercapai saat Submit menolak Create dan form tetap terbuka

24. Ketik Search `Lim 999`, tekan Enter
25. Klik `⋯` baris `Lim 999` > Delete
26. Klik [Delete] pada dialog
27. Verifikasi toast sukses: "Success, unit has been deleted."
28. Klik `(←)` pada kotak Search
29. Klik [+ Unit]
30. Admin lain membuat 1 Measurement `Admin Slot {runId}-022` lewat sesi API hingga tersimpan, sehingga ceiling 1.000 tercapai
31. Isi Unit Name `Rod {runId}-022` dan Symbol `rd`, centang `Stay on this form after submitting`
32. Klik [Submit]
33. Verifikasi dialog `Cannot Add Unit` tampil
34. Klik [OK]
35. Verifikasi form Create tetap terbuka
36. Verifikasi Unit Name `Rod {runId}-022` dan Symbol `rd` dipertahankan di form
37. Klik `[✕]` untuk menutup form yang masih dirty
38. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
39. Klik [Leave]
40. Ketik Search `Rod {runId}-022`, tekan Enter
41. Verifikasi empty state `No results found` (Title) untuk Search `Rod {runId}-022`, sehingga `Rod {runId}-022` tidak tersimpan (tidak ada di tabel)
42. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: volume data dan state tenant (prinsip 13e).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec adalah 66, 63, 64, 65 (urutan sumber 63 sampai 66): TC-GS-UOM-63, 64, dan 65 bergantung pada TC-GS-UOM-66 (kolom Dependensi), yaitu tabel Client Limit berisi 1.000 unit yang dicapai di TC-GS-UOM-66 (999 unit lalu `Chain {runId}-022`). Rantai ada di dalam satu spec, jadi spec tetap bisa jalan sendiri.
- TC-GS-UOM-64 memakai dialog `Cannot Add Unit` yang masih terbuka dari langkah 15 (TC-GS-UOM-63); langkah Uji TC-GS-UOM-64 "Klik [+ Unit]" tidak diulang karena dialog menghalangi klik berikutnya.
- Nama TC sumber diganti nama bersuffix milik spec (Chain, Link, Rod) sesuai S-12; unit `Lim 999` adalah data fixture tenant Client Limit yang dihapus di TC-GS-UOM-65 sesuai Langkah Uji TC dan dipulihkan di hook `after`.
- Kuota Master Data Count Limit menjadi pemicu state pada spec ini, bukan objek race dua sesi (race ada di spec `TC-GS-UOM-E2E-062-master-data-count-limit-race-slot-terakhir`).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menutup dialog `Cannot Add Unit` dari TC-GS-UOM-66), langkah 8 sampai 10 dan 37 sampai 39 (menutup form dirty lewat `[✕]` lalu [Leave]; langkah 9 dan 38 memverifikasi dialog, S-08), langkah 11, 13, 24, 28, 40, dan 42 (Search lalu menutup Search, supaya `Link` dan `Rod` diperiksa di tabel 10 per halaman dan `Lim 999` ditemukan), serta langkah 25 sampai 27 (aksi Delete `Lim 999` sebagai Langkah Uji 1 TC-GS-UOM-65; toast di langkah 27 menjadi anchor positif).
- Langkah 12, 41 (unit tidak tersimpan) berasal dari Expected Result b TC-GS-UOM-66 dan c TC-GS-UOM-65 dan memakai empty state `No results found` hasil Search sebagai anchor positif bagi asersi absence (bagian 8b butir 2); langkah 23 dari Expected Result b TC-GS-UOM-64 ("tanpa membuat record").
- Spec ini di atas batas 35 langkah (42): seluruhnya satu kelas harness (volume data dan state tenant Client Limit) dengan satu akun; TC-63, 64, 65 bergantung pada kondisi ceiling TC-66 sehingga dipertahankan dalam satu spec agar seeding 999 unit tidak diulang.
- PRD §9.10 menetapkan `{limit}` mengikuti format angka pengguna; asersi memakai nilai 1.000 sesuai format akun Client Limit (disediakan tim FE); TC-GS-UOM-63 menulis `1.000`, Brand menulis `1000` tanpa pemisah.
- Temuan untuk QA:
  - Expected Result b TC-GS-UOM-65 ("checkbox Stay tidak berpengaruh") ambigu: tidak jelas apa yang diamati. Spec hanya mengasersi form tetap terbuka dengan nilai dipertahankan (langkah 35 dan 36); checkbox Stay tidak diasersi terpisah.
  - TC-GS-UOM-66 tidak menyebut cara menutup dialog `Cannot Add Unit` dan form dirty sesudahnya, serta cara memeriksa `Link` tidak tersimpan; spec memakai [OK], `[✕]`, [Leave], dan Search.
  - TC-GS-UOM-65 menulis "Admin lain membuat 1 Measurement" tanpa akun; disediakan tim FE (sesi API).
