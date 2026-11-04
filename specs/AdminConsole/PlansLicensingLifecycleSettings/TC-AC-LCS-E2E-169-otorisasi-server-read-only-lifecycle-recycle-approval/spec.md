---
id: TC-AC-LCS-E2E-169-otorisasi-server-read-only-lifecycle-recycle-approval
title: "Otorisasi Server: Read Only Save dan Reset Tab Client Lifecycle, Recycle Bin, dan Approval Settings Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-592
  - TC-AC-LCS-593
  - TC-AC-LCS-594
  - TC-AC-LCS-595
  - TC-AC-LCS-596
  - TC-AC-LCS-597
coverage:
  web: automated
---

# Otorisasi Server: Read Only Save dan Reset Tab Client Lifecycle, Recycle Bin, dan Approval Settings Ditolak

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Pratama`), password dari `Spectra.env.AC_RO_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; permintaan langsung memakai login API password akun yang sama (sesi API aktor, disediakan tim BE/FE); hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7); nilai non-default per tab untuk TC Reset diatur lewat Fixture BE sebagai precondition TC (Data Dinamis 2).
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-592: Save tab Client Lifecycle lewat permintaan langsung oleh Read Only ditolak server

1. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Notify Plan Owner Before Event = `46` memakai sesi Read Only
2. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
3. Muat ulang halaman Lifecycle Settings dan buka tab Client Lifecycle
4. Verifikasi Notify Plan Owner Before Event tetap `45`

### TC-AC-LCS-593: Reset to Default tab Client Lifecycle lewat permintaan langsung oleh Read Only ditolak server

5. Atur lewat Fixture BE: ketujuh tab pada nilai default kecuali tab Client Lifecycle tersimpan dengan nilai non-default: Notify Plan Owner Before Event: 60, First Reminder Before Event: 45, Second Reminder Before Event: 14, Final Reminder Before Event: 3, Grace Period Duration: 20, Archive Period Duration: 25, Purge Warning Email: 12, Purge Urgent Warning Email: 4, Post-Purge Retention: 1000
6. Kirim permintaan Reset tab Client Lifecycle langsung ke server memakai sesi Read Only
7. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
8. Muat ulang halaman dan buka tab Client Lifecycle
9. Verifikasi nilai tab tidak kembali ke default (tetap Notify Plan Owner Before Event: 60, First Reminder Before Event: 45, Second Reminder Before Event: 14, Final Reminder Before Event: 3, Grace Period Duration: 20, Archive Period Duration: 25, Purge Warning Email: 12, Purge Urgent Warning Email: 4, Post-Purge Retention: 1000)

### TC-AC-LCS-594: Save tab Recycle Bin lewat permintaan langsung oleh Read Only ditolak server

10. Pulihkan ketujuh tab ke nilai default lewat Fixture BE
11. Kirim permintaan Save tab Recycle Bin langsung ke server dengan Permanently Delete Recycle Bin = `31` memakai sesi Read Only
12. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
13. Muat ulang halaman Lifecycle Settings dan buka tab Recycle Bin
14. Verifikasi Permanently Delete Recycle Bin tetap `30`

### TC-AC-LCS-595: Reset to Default tab Recycle Bin lewat permintaan langsung oleh Read Only ditolak server

15. Atur lewat Fixture BE: ketujuh tab pada nilai default kecuali tab Recycle Bin tersimpan dengan nilai non-default: Permanently Delete Recycle Bin: 45
16. Kirim permintaan Reset tab Recycle Bin langsung ke server memakai sesi Read Only
17. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
18. Muat ulang halaman dan buka tab Recycle Bin
19. Verifikasi nilai tab tidak kembali ke default (tetap Permanently Delete Recycle Bin: 45)

### TC-AC-LCS-596: Save tab Approval Settings lewat permintaan langsung oleh Read Only ditolak server

20. Pulihkan ketujuh tab ke nilai default lewat Fixture BE
21. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout = `4` memakai sesi Read Only
22. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
23. Muat ulang halaman Lifecycle Settings dan buka tab Approval Settings
24. Verifikasi Approval Timeout tetap `3`

### TC-AC-LCS-597: Reset to Default tab Approval Settings lewat permintaan langsung oleh Read Only ditolak server

25. Atur lewat Fixture BE: ketujuh tab pada nilai default kecuali tab Approval Settings tersimpan dengan nilai non-default: Approval Timeout: 7
26. Kirim permintaan Reset tab Approval Settings langsung ke server memakai sesi Read Only
27. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
28. Muat ulang halaman dan buka tab Approval Settings
29. Verifikasi nilai tab tidak kembali ke default (tetap Approval Timeout: 7)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`.
- Expected c "Tidak ada entri Changelog baru" TC-AC-LCS-592, TC-AC-LCS-594, TC-AC-LCS-596 diasersi di spec absence `TC-AC-LCS-E2E-137` (kelas g) dengan permintaan tersebut sebagai pemicu, user dan baseline sendiri (S-05, `P-5` butir a); id TC tetap di `sourceTc` spec ini dan spec ini hanya mengasersi status respons dan state data (bagian 8b butir 1).
- Pemisahan dari 168 dan 170: satu spec per kelompok tab (Client Lifecycle, Recycle Bin, Approval Settings) agar alur otorisasi Read Only tiap kelompok berdiri sendiri.
- Temuan untuk QA:
  - TC 592 sampai 597 mensyaratkan sesi Read Only untuk permintaan langsung; spec memakai login API password akun Read Only (sesi API aktor).
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 5, 10, 15, 20, 25.
