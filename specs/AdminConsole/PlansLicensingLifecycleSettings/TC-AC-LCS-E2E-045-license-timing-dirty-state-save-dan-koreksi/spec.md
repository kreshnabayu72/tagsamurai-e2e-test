---
id: TC-AC-LCS-E2E-045-license-timing-dirty-state-save-dan-koreksi
title: "Tab License Timing: Dirty State, Save Seluruh Field, dan Koreksi Nilai Salah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-159
  - TC-AC-LCS-160
  - TC-AC-LCS-168
coverage:
  web: automated
---

# Tab License Timing: Dirty State, Save Seluruh Field, dan Koreksi Nilai Salah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: License Timing (Managed Transition Time `24`, Managed Action Retry Delay `2`, Addon Reactivation Delay `2`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab License Timing adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

1. Klik tab License Timing

### TC-AC-LCS-159: Save mengikuti dirty state dan Reset to Default selalu enabled

2. Verifikasi `[Save]` disabled pada kondisi awal
3. Verifikasi `[Reset to Default]` enabled pada kondisi awal
4. Ubah Managed Transition Time dari `24` menjadi `25`
5. Verifikasi `[Save]` enabled
6. Verifikasi `[Reset to Default]` enabled
7. Kembalikan Managed Transition Time menjadi `24`
8. Verifikasi `[Save]` disabled kembali
9. Verifikasi `[Reset to Default]` tetap enabled

### TC-AC-LCS-168: memperbaiki nilai yang salah menghapus pesan error dan meng-enable Save

10. Isi Managed Transition Time dengan `0`
11. Klik area kosong di luar field (blur)
12. Verifikasi pesan error rentang tampil pada Managed Transition Time
13. Verifikasi `[Save]` disabled
14. Isi Managed Transition Time dengan `25`
15. Klik area kosong di luar field (blur)
16. Verifikasi pesan error hilang
17. Verifikasi `[Save]` enabled

### TC-AC-LCS-160: Save tab License Timing dengan seluruh field diubah ke nilai valid

18. Ubah Managed Transition Time menjadi `48`
19. Ubah Managed Action Retry Delay menjadi `5`
20. Ubah Addon Reactivation Delay menjadi `7`
21. Klik `[Save]`
22. Verifikasi toast sukses "Success, license timing settings have been saved."
23. Verifikasi tab refresh: field memuat nilai tersimpan Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7`
24. Verifikasi `[Save]` disabled
25. Muat ulang halaman dengan F5 lalu klik tab License Timing
26. Verifikasi setelah F5: Managed Transition Time bernilai `48`
27. Verifikasi setelah F5: Managed Action Retry Delay bernilai `5`
28. Verifikasi setelah F5: Addon Reactivation Delay bernilai `7`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 159, 168, 160 (validasi yang diblokir dan perbaikannya sebelum Save sukses, S-10).
- Langkah penghubung (S-03): langkah 1 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Pembagian TC lintas spec: TC-AC-LCS-161 (Save nilai minimum License Timing) ada di spec 187 (`TC-AC-LCS-E2E-187-license-timing-save-nilai-minimum`), bukan di spec ini.
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-160 (entri Changelog `Edit` per field) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - TC-AC-LCS-168 menyebut "pesan error rentang" tanpa teks pesan; spec mengasersi keberadaan pesan tanpa mengutip teksnya (S-02).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
