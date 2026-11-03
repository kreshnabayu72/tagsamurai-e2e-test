---
id: TC-AC-LCS-E2E-139-absence-changelog-penolakan-rentang-lifecycle-recycle-approval-limits
title: "Absence Log: Penolakan Server atas Nilai di Atas dan di Bawah Rentang Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits Tidak Menambah Entri Changelog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-622
  - TC-AC-LCS-623
  - TC-AC-LCS-626
  - TC-AC-LCS-627
  - TC-AC-LCS-630
  - TC-AC-LCS-631
  - TC-AC-LCS-634
  - TC-AC-LCS-635
coverage:
  web: automated
---

# Absence Log: Penolakan Server atas Nilai di Atas dan di Bawah Rentang Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits Tidak Menambah Entri Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Dataset Changelog kecil per tab (3 entri: 10, 11, 12 May 26; Modified By `John Doe` dan `Sarah Thompson`) diseed lewat Fixture BE di hook `before` spec ini untuk tab `Client Lifecycle`, `Recycle Bin`, `Approval Settings`, dan `System Limits`; jumlah entri tiap tab dicatat sebagai baseline di hook `before` (S-12). Spec ini tidak menambah entri Changelog.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI memakai sesi API aktor (login API password untuk akun yang sama tanpa mengusir sesi UI); kemampuan membaca jumlah entri Changelog per tab sebagai baseline; Fixture BE untuk menyeed Dataset Changelog kecil per tab.
- Permintaan langsung adalah pemicu kondisi yang diasersi tidak tercatat dan bukan objek uji; status respons dan state data diasersi di spec kelas a (`P-5` butir a).
- Pemulihan: dataset Changelog dikembalikan ke keadaan awal dan ketujuh tab dipulihkan ke nilai default oleh hook `after` suite; permintaan yang ditolak tidak mengubah data.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Nilai Pre-setup dan state Changelog dirujuk lewat `Fixture.lifecycleSettings.<kunci>` dari `fixtures/lifecycle-settings.json`.

## Test Steps

### TC-AC-LCS-622: Save tab Client Lifecycle lewat permintaan langsung dengan Notify Plan Owner Before Event di atas maksimum tidak menambah entri Changelog

1. Klik tab `Client Lifecycle`
2. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Notify Plan Owner Before Event = `1000` memakai sesi API Total Control dan tunggu respons diterima
3. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
4. Verifikasi entri seed Changelog tab `Client Lifecycle` dengan Date `12 May 26` tampil
5. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Client Lifecycle` sama dengan baseline
6. Tutup modal Changelog

### TC-AC-LCS-623: Save tab Client Lifecycle lewat permintaan langsung dengan Notify Plan Owner Before Event di bawah minimum tidak menambah entri Changelog

7. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Notify Plan Owner Before Event = `0` memakai sesi API Total Control dan tunggu respons diterima
8. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
9. Verifikasi entri seed Changelog tab `Client Lifecycle` dengan Date `12 May 26` tampil
10. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Client Lifecycle` sama dengan baseline
11. Tutup modal Changelog

### TC-AC-LCS-626: Save tab Recycle Bin lewat permintaan langsung dengan Permanently Delete Recycle Bin di atas maksimum tidak menambah entri Changelog

12. Klik tab `Recycle Bin`
13. Kirim permintaan Save tab Recycle Bin langsung ke server dengan Permanently Delete Recycle Bin = `1000` memakai sesi API Total Control dan tunggu respons diterima
14. Klik icon Changelog di pojok kanan atas panel tab `Recycle Bin`
15. Verifikasi entri seed Changelog tab `Recycle Bin` dengan Date `12 May 26` tampil
16. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Recycle Bin` sama dengan baseline
17. Tutup modal Changelog

### TC-AC-LCS-627: Save tab Recycle Bin lewat permintaan langsung dengan Permanently Delete Recycle Bin di bawah minimum tidak menambah entri Changelog

18. Kirim permintaan Save tab Recycle Bin langsung ke server dengan Permanently Delete Recycle Bin = `0` memakai sesi API Total Control dan tunggu respons diterima
19. Klik icon Changelog di pojok kanan atas panel tab `Recycle Bin`
20. Verifikasi entri seed Changelog tab `Recycle Bin` dengan Date `12 May 26` tampil
21. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Recycle Bin` sama dengan baseline
22. Tutup modal Changelog

### TC-AC-LCS-630: Save tab Approval Settings lewat permintaan langsung dengan Approval Timeout di atas maksimum tidak menambah entri Changelog

23. Klik tab `Approval Settings`
24. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout = `31` memakai sesi API Total Control dan tunggu respons diterima
25. Klik icon Changelog di pojok kanan atas panel tab `Approval Settings`
26. Verifikasi entri seed Changelog tab `Approval Settings` dengan Date `12 May 26` tampil
27. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Approval Settings` sama dengan baseline
28. Tutup modal Changelog

### TC-AC-LCS-631: Save tab Approval Settings lewat permintaan langsung dengan Approval Timeout di bawah minimum tidak menambah entri Changelog

29. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout = `0` memakai sesi API Total Control dan tunggu respons diterima
30. Klik icon Changelog di pojok kanan atas panel tab `Approval Settings`
31. Verifikasi entri seed Changelog tab `Approval Settings` dengan Date `12 May 26` tampil
32. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Approval Settings` sama dengan baseline
33. Tutup modal Changelog

### TC-AC-LCS-634: Save tab System Limits lewat permintaan langsung dengan Bulk Transaction Row Limit di atas maksimum tidak menambah entri Changelog

34. Klik tab `System Limits`
35. Kirim permintaan Save tab System Limits langsung ke server dengan Bulk Transaction Row Limit = `5001` memakai sesi API Total Control dan tunggu respons diterima
36. Klik icon Changelog di pojok kanan atas panel tab `System Limits`
37. Verifikasi entri seed Changelog tab `System Limits` dengan Date `12 May 26` tampil
38. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `System Limits` sama dengan baseline
39. Tutup modal Changelog

### TC-AC-LCS-635: Save tab System Limits lewat permintaan langsung dengan Bulk Transaction Row Limit di bawah minimum tidak menambah entri Changelog

40. Kirim permintaan Save tab System Limits langsung ke server dengan Bulk Transaction Row Limit = `99` memakai sesi API Total Control dan tunggu respons diterima
41. Klik icon Changelog di pojok kanan atas panel tab `System Limits`
42. Verifikasi entri seed Changelog tab `System Limits` dengan Date `12 May 26` tampil
43. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `System Limits` sama dengan baseline

## Notes

- `P-5` butir a: permintaan langsung ke server hanya memicu kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memakai tab dan baseline sendiri (S-05).
- Pembagian TC lintas spec: butir Expected status `422` dan nilai field tetap diasersi di spec kelas a; TC-AC-LCS-622 dan TC-AC-LCS-623 memuat aksi di spec TC-AC-LCS-E2E-176, TC-AC-LCS-626 dan TC-AC-LCS-627 di spec TC-AC-LCS-E2E-178, TC-AC-LCS-630 dan TC-AC-LCS-631 di spec TC-AC-LCS-E2E-179, serta TC-AC-LCS-634 dan TC-AC-LCS-635 di spec TC-AC-LCS-E2E-180. Spec ini hanya memuat butir "Tidak ada entri Changelog baru" (S-05).
- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC: user berada di tab terkait) dan "Tutup modal Changelog" antar TC; dua TC pada tab yang sama berurutan memakai satu pembukaan tab (S-03, S-09). Anchor positif asersi absence adalah `Verifikasi` entri seed tampil pada surface yang sama (bagian 8b butir 2).
- Temuan untuk QA: Dataset kecil per tab (Pre-setup 9) tidak menyebut Field entri seed; anchor memakai Date `12 May 26` yang tercantum di Pre-setup.
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
- Alasan lebih dari sekitar 35 langkah: delapan blok memakai pola yang sama, semuanya satu kelas absence, dan tiap blok memakai nilai, permintaan, dan baseline sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
