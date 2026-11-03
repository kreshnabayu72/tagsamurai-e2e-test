---
id: TC-AC-LCS-E2E-182-save-no-op-recycle-approval-limits
title: "Save Identik No-Op Lewat Permintaan Langsung: Tab Recycle Bin, Approval Settings, dan System Limits"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-648
  - TC-AC-LCS-649
  - TC-AC-LCS-650
coverage:
  web: automated
---

# Save Identik No-Op Lewat Permintaan Langsung: Tab Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Permintaan langsung memakai login API password akun yang sama (sesi API aktor, disediakan tim BE/FE).
- Data Pre-setup dan Dinamis yang dipakai: nilai tersimpan non-default per tab dan Changelog satu entri per tab diatur lewat Fixture BE sebagai precondition TC (nama user `Andi Wijaya`); Changelog bersifat permanen sehingga asersi memakai baseline jumlah entri sebelum aksi (S-12) dan dataset dikembalikan lewat Fixture BE di hook `after` suite.
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu. Fixture BE juga membaca antrean job (Countdown Reset Job, Recalculate Job, recalculation timer).
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-648: Save tab Recycle Bin lewat permintaan langsung dengan seluruh nilai sama dengan tersimpan berhasil sebagai no-op

1. Atur lewat Fixture BE: tab Recycle Bin tersimpan dengan nilai Permanently Delete Recycle Bin: 45; Changelog tab Recycle Bin berisi tepat 1 entri; catat baseline jumlah entri Changelog dan antrean job
2. Kirim permintaan Save tab Recycle Bin langsung ke server dengan seluruh nilai sama dengan nilai tersimpan
3. Verifikasi permintaan diterima sebagai sukses tanpa perubahan data
4. Muat ulang halaman, buka tab Recycle Bin lalu klik icon Changelog
5. Verifikasi nilai field sama dengan sebelumnya (Permanently Delete Recycle Bin: 45)
6. Verifikasi Changelog tetap `1–1 of 1` (tidak ada entri baru; selisih terhadap baseline 0)
7. Periksa fixture BE untuk antrean job
8. Verifikasi tidak mengantrekan Countdown Reset Job

### TC-AC-LCS-649: Save tab Approval Settings lewat permintaan langsung dengan seluruh nilai sama dengan tersimpan berhasil sebagai no-op

9. Atur lewat Fixture BE: tab Approval Settings tersimpan dengan nilai Approval Timeout: 7; Changelog tab Approval Settings berisi tepat 1 entri; catat baseline jumlah entri Changelog dan antrean job
10. Kirim permintaan Save tab Approval Settings langsung ke server dengan seluruh nilai sama dengan nilai tersimpan
11. Verifikasi permintaan diterima sebagai sukses tanpa perubahan data
12. Muat ulang halaman, buka tab Approval Settings lalu klik icon Changelog
13. Verifikasi nilai field sama dengan sebelumnya (Approval Timeout: 7)
14. Verifikasi Changelog tetap `1–1 of 1` (tidak ada entri baru; selisih terhadap baseline 0)
15. Periksa fixture BE untuk antrean job
16. Verifikasi tidak memicu Recalculate Job

### TC-AC-LCS-650: Save tab System Limits lewat permintaan langsung dengan seluruh nilai sama dengan tersimpan berhasil sebagai no-op

17. Atur lewat Fixture BE: tab System Limits tersimpan dengan nilai Bulk Transaction Row Limit: 2000, Selection Limit: 1500, Register Asset Bulk Limit: 2500, Hierarchy Depth Limit: 60, Master Data Count Limit: 20000, Max Visible Columns: 25; Changelog tab System Limits berisi tepat 1 entri; catat baseline jumlah entri Changelog dan antrean job
18. Kirim permintaan Save tab System Limits langsung ke server dengan seluruh nilai sama dengan nilai tersimpan
19. Verifikasi permintaan diterima sebagai sukses tanpa perubahan data
20. Muat ulang halaman, buka tab System Limits lalu klik icon Changelog
21. Verifikasi nilai field sama dengan sebelumnya (Bulk Transaction Row Limit: 2000, Selection Limit: 1500, Register Asset Bulk Limit: 2500, Hierarchy Depth Limit: 60, Master Data Count Limit: 20000, Max Visible Columns: 25)
22. Verifikasi Changelog tetap `1–1 of 1` (tidak ada entri baru; selisih terhadap baseline 0)
23. Periksa fixture BE untuk antrean job
24. Verifikasi tidak memicu job apa pun

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`.
- Asersi jumlah Changelog `1–1 of 1` bukan kelas g: asersi jumlah dengan baseline (bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC 644 sampai 650 mengasersi `1–1 of 1` sebagai angka absolut dengan precondition "berisi tepat 1 entri"; S-12 melarang total entri absolut pada audit trail permanen, sehingga spec mengasersi label `1–1 of 1` bersama selisih terhadap baseline 0 dengan dataset diatur Fixture BE.
  - TC 644 sampai 650 langkah 2 mengurutkan muat ulang, buka tab, dan klik icon Changelog dalam satu langkah; spec mengasersi nilai field sesudah modal Changelog terbuka karena field tetap ada pada halaman di belakang modal.
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1, 9, 17.
