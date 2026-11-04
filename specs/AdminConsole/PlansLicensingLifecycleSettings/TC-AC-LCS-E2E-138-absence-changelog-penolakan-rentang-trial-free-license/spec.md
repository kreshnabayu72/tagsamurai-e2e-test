---
id: TC-AC-LCS-E2E-138-absence-changelog-penolakan-rentang-trial-free-license
title: "Absence Log: Penolakan Server atas Nilai di Atas dan di Bawah Rentang Tab Trial, Free Plan, dan License Timing Tidak Menambah Entri Changelog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-610
  - TC-AC-LCS-611
  - TC-AC-LCS-614
  - TC-AC-LCS-615
  - TC-AC-LCS-618
  - TC-AC-LCS-619
coverage:
  web: automated
---

# Absence Log: Penolakan Server atas Nilai di Atas dan di Bawah Rentang Tab Trial, Free Plan, dan License Timing Tidak Menambah Entri Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Dataset Changelog kecil per tab (3 entri: 10, 11, 12 May 26; Modified By `John Doe` dan `Sarah Thompson`) diseed lewat Fixture BE di hook `before` spec ini untuk tab `Trial Settings`, `Free Plan Settings`, dan `License Timing`; jumlah entri tiap tab dicatat sebagai baseline di hook `before` (S-12). Spec ini tidak menambah entri Changelog.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI memakai sesi API aktor (login API password untuk akun yang sama tanpa mengusir sesi UI); kemampuan membaca jumlah entri Changelog per tab sebagai baseline; Fixture BE untuk menyeed Dataset Changelog kecil per tab.
- Permintaan langsung adalah pemicu kondisi yang diasersi tidak tercatat dan bukan objek uji; status respons dan state data diasersi di spec kelas a (`P-5` butir a).
- Pemulihan: dataset Changelog dikembalikan ke keadaan awal dan ketujuh tab dipulihkan ke nilai default oleh hook `after` suite; permintaan yang ditolak tidak mengubah data.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Nilai Pre-setup dan state Changelog dirujuk lewat `Fixture.lifecycleSettings.<kunci>` dari `fixtures/lifecycle-settings.json`.

## Test Steps

### TC-AC-LCS-610: Save tab Trial Settings lewat permintaan langsung dengan Max Trial Duration di atas maksimum tidak menambah entri Changelog

1. Klik tab `Trial Settings`
2. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `366` memakai sesi API Total Control dan tunggu respons diterima
3. Klik icon Changelog di pojok kanan atas panel tab `Trial Settings`
4. Verifikasi entri seed Changelog tab `Trial Settings` dengan Date `12 May 26` tampil
5. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Trial Settings` sama dengan baseline
6. Tutup modal Changelog

### TC-AC-LCS-611: Save tab Trial Settings lewat permintaan langsung dengan Max Trial Duration di bawah minimum tidak menambah entri Changelog

7. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `0` memakai sesi API Total Control dan tunggu respons diterima
8. Klik icon Changelog di pojok kanan atas panel tab `Trial Settings`
9. Verifikasi entri seed Changelog tab `Trial Settings` dengan Date `12 May 26` tampil
10. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Trial Settings` sama dengan baseline
11. Tutup modal Changelog

### TC-AC-LCS-614: Save tab Free Plan Settings lewat permintaan langsung dengan Free Plan Duration di atas maksimum tidak menambah entri Changelog

12. Klik tab `Free Plan Settings`
13. Kirim permintaan Save tab Free Plan Settings langsung ke server dengan Free Plan Duration = `10000` memakai sesi API Total Control dan tunggu respons diterima
14. Klik icon Changelog di pojok kanan atas panel tab `Free Plan Settings`
15. Verifikasi entri seed Changelog tab `Free Plan Settings` dengan Date `12 May 26` tampil
16. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Free Plan Settings` sama dengan baseline
17. Tutup modal Changelog

### TC-AC-LCS-615: Save tab Free Plan Settings lewat permintaan langsung dengan Free Plan Duration di bawah minimum tidak menambah entri Changelog

18. Kirim permintaan Save tab Free Plan Settings langsung ke server dengan Free Plan Duration = `0` memakai sesi API Total Control dan tunggu respons diterima
19. Klik icon Changelog di pojok kanan atas panel tab `Free Plan Settings`
20. Verifikasi entri seed Changelog tab `Free Plan Settings` dengan Date `12 May 26` tampil
21. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `Free Plan Settings` sama dengan baseline
22. Tutup modal Changelog

### TC-AC-LCS-618: Save tab License Timing lewat permintaan langsung dengan Managed Transition Time di atas maksimum tidak menambah entri Changelog

23. Klik tab `License Timing`
24. Kirim permintaan Save tab License Timing langsung ke server dengan Managed Transition Time = `1000` memakai sesi API Total Control dan tunggu respons diterima
25. Klik icon Changelog di pojok kanan atas panel tab `License Timing`
26. Verifikasi entri seed Changelog tab `License Timing` dengan Date `12 May 26` tampil
27. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `License Timing` sama dengan baseline
28. Tutup modal Changelog

### TC-AC-LCS-619: Save tab License Timing lewat permintaan langsung dengan Managed Transition Time di bawah minimum tidak menambah entri Changelog

29. Kirim permintaan Save tab License Timing langsung ke server dengan Managed Transition Time = `0` memakai sesi API Total Control dan tunggu respons diterima
30. Klik icon Changelog di pojok kanan atas panel tab `License Timing`
31. Verifikasi entri seed Changelog tab `License Timing` dengan Date `12 May 26` tampil
32. Verifikasi tidak ada entri Changelog baru: jumlah entri Changelog tab `License Timing` sama dengan baseline

## Notes

- `P-5` butir a: permintaan langsung ke server hanya memicu kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memakai tab dan baseline sendiri (S-05).
- Pembagian TC lintas spec: butir Expected status `422` dan nilai field tetap diasersi di spec kelas a; TC-AC-LCS-610 dan TC-AC-LCS-611 memuat aksi di spec TC-AC-LCS-E2E-173, TC-AC-LCS-614 dan TC-AC-LCS-615 di spec TC-AC-LCS-E2E-174, serta TC-AC-LCS-618 dan TC-AC-LCS-619 di spec TC-AC-LCS-E2E-175. Spec ini hanya memuat butir "Tidak ada entri Changelog baru" (S-05).
- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC: user berada di tab terkait) dan "Tutup modal Changelog" antar TC; dua TC pada tab yang sama berurutan memakai satu pembukaan tab (S-03, S-09). Anchor positif asersi absence adalah `Verifikasi` entri seed tampil pada surface yang sama (bagian 8b butir 2).
- Temuan untuk QA: Dataset kecil per tab (Pre-setup 9) tidak menyebut Field entri seed; anchor memakai Date `12 May 26` yang tercantum di Pre-setup.
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
