---
id: TC-AC-LCS-E2E-137-absence-changelog-penolakan-read-only
title: "Absence Log: Penolakan Server Read Only pada Save Setiap Tab Tidak Menambah Entri Changelog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-586
  - TC-AC-LCS-588
  - TC-AC-LCS-590
  - TC-AC-LCS-592
  - TC-AC-LCS-594
  - TC-AC-LCS-596
  - TC-AC-LCS-598
coverage:
  web: automated
---

# Absence Log: Penolakan Server Read Only pada Save Setiap Tab Tidak Menambah Entri Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Pratama`, Principal), password dari `Spectra.env.AC_RO_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Dataset Changelog kecil per tab (3 entri: 10, 11, 12 May 26; Modified By `John Doe` dan `Sarah Thompson`) diseed lewat Fixture BE di hook `before` spec ini untuk ketujuh tab; jumlah entri tiap tab dicatat sebagai baseline di hook `before` (S-12). Spec ini tidak menambah entri Changelog.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI memakai sesi API aktor (login API password untuk akun yang sama tanpa mengusir sesi UI); kemampuan membaca jumlah entri Changelog per tab sebagai baseline; Fixture BE untuk menyeed Dataset Changelog kecil per tab.
- Permintaan langsung adalah pemicu kondisi yang diasersi tidak tercatat dan bukan objek uji; status respons dan state data diasersi di spec kelas a (`P-5` butir a).
- Pemulihan: dataset Changelog dikembalikan ke keadaan awal dan ketujuh tab dipulihkan ke nilai default oleh hook `after` suite; permintaan yang ditolak tidak mengubah data.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-586: Save tab Trial Settings lewat permintaan langsung oleh Read Only tidak menambah entri Changelog

1. Klik tab `Trial Settings`
2. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `31` memakai sesi API Read Only dan tunggu respons diterima
3. Klik icon Changelog di pojok kanan atas panel tab `Trial Settings`
4. Verifikasi entri seed Changelog tab `Trial Settings` dengan Date `12 May 26` tampil
5. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Trial Settings` sama dengan baseline
6. Tutup modal Changelog

### TC-AC-LCS-588: Save tab Free Plan Settings lewat permintaan langsung oleh Read Only tidak menambah entri Changelog

7. Klik tab `Free Plan Settings`
8. Kirim permintaan Save tab Free Plan Settings langsung ke server dengan Free Plan Duration = `366` memakai sesi API Read Only dan tunggu respons diterima
9. Klik icon Changelog di pojok kanan atas panel tab `Free Plan Settings`
10. Verifikasi entri seed Changelog tab `Free Plan Settings` dengan Date `12 May 26` tampil
11. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Free Plan Settings` sama dengan baseline
12. Tutup modal Changelog

### TC-AC-LCS-590: Save tab License Timing lewat permintaan langsung oleh Read Only tidak menambah entri Changelog

13. Klik tab `License Timing`
14. Kirim permintaan Save tab License Timing langsung ke server dengan Managed Transition Time = `25` memakai sesi API Read Only dan tunggu respons diterima
15. Klik icon Changelog di pojok kanan atas panel tab `License Timing`
16. Verifikasi entri seed Changelog tab `License Timing` dengan Date `12 May 26` tampil
17. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `License Timing` sama dengan baseline
18. Tutup modal Changelog

### TC-AC-LCS-592: Save tab Client Lifecycle lewat permintaan langsung oleh Read Only tidak menambah entri Changelog

19. Klik tab `Client Lifecycle`
20. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Notify Plan Owner Before Event = `46` memakai sesi API Read Only dan tunggu respons diterima
21. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
22. Verifikasi entri seed Changelog tab `Client Lifecycle` dengan Date `12 May 26` tampil
23. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Client Lifecycle` sama dengan baseline
24. Tutup modal Changelog

### TC-AC-LCS-594: Save tab Recycle Bin lewat permintaan langsung oleh Read Only tidak menambah entri Changelog

25. Klik tab `Recycle Bin`
26. Kirim permintaan Save tab Recycle Bin langsung ke server dengan Permanently Delete Recycle Bin = `31` memakai sesi API Read Only dan tunggu respons diterima
27. Klik icon Changelog di pojok kanan atas panel tab `Recycle Bin`
28. Verifikasi entri seed Changelog tab `Recycle Bin` dengan Date `12 May 26` tampil
29. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Recycle Bin` sama dengan baseline
30. Tutup modal Changelog

### TC-AC-LCS-596: Save tab Approval Settings lewat permintaan langsung oleh Read Only tidak menambah entri Changelog

31. Klik tab `Approval Settings`
32. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout = `4` memakai sesi API Read Only dan tunggu respons diterima
33. Klik icon Changelog di pojok kanan atas panel tab `Approval Settings`
34. Verifikasi entri seed Changelog tab `Approval Settings` dengan Date `12 May 26` tampil
35. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Approval Settings` sama dengan baseline
36. Tutup modal Changelog

### TC-AC-LCS-598: Save tab System Limits lewat permintaan langsung oleh Read Only tidak menambah entri Changelog

37. Klik tab `System Limits`
38. Kirim permintaan Save tab System Limits langsung ke server dengan Bulk Transaction Row Limit = `1001` memakai sesi API Read Only dan tunggu respons diterima
39. Klik icon Changelog di pojok kanan atas panel tab `System Limits`
40. Verifikasi entri seed Changelog tab `System Limits` dengan Date `12 May 26` tampil
41. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `System Limits` sama dengan baseline

## Notes

- `P-5` butir a: permintaan langsung ke server memakai sesi Read Only hanya memicu kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memakai tab dan baseline sendiri (S-05).
- Pembagian TC lintas spec: butir Expected status `403` dan nilai field tetap diasersi di spec kelas a; TC 586, 588, dan 590 ada di spec 168, TC 592, 594, dan 596 di spec 169, dan TC 598 di spec 170. Spec ini hanya memuat butir "Tidak ada entri Changelog baru" (S-05).
- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC: user berada di tab terkait) dan "Tutup modal Changelog" antar TC (S-03, S-09). Anchor positif asersi absence adalah `Verifikasi` entri seed tampil pada surface yang sama (bagian 8b butir 2).
- Alasan lebih dari sekitar 35 langkah: tujuh blok memakai pola yang sama, semuanya satu kelas absence, dan tiap blok memakai tab, permintaan, dan baseline sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: Dataset kecil per tab (Pre-setup 9) tidak menyebut Field entri seed; anchor memakai Date `12 May 26` yang tercantum di Pre-setup.
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
