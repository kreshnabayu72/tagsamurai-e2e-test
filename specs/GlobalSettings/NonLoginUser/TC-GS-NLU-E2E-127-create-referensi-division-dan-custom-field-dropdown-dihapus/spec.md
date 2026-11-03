---
id: TC-GS-NLU-E2E-127-create-referensi-division-dan-custom-field-dropdown-dihapus
title: "Create: referensi Division dan Custom Field dropdown dihapus sebelum Submit"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-85
  - TC-GS-NLU-86
coverage:
  web: automated
---

# Create: referensi Division dan Custom Field dropdown dihapus sebelum Submit

## Prerequisites

- Mode: FE+BE (backend nyata; penghapusan referensi dilakukan di backend nyata lewat sesi API aktor, bukan konteks UI kedua).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`); pelaku penghapusan memakai sesi API aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By). TC-GS-NLU-85 menulis target hapus dari master data tanpa nama; spec memakai Division milik spec supaya Pre-setup tidak berubah (S-06).
- Data Dinamis, di-seed lewat API di hook `before` (mekanisme disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD):
  - Division `Divisi Hapus {runId}-127` (target hapus TC-GS-NLU-85).
  - Custom Field uji `Blood Type Uji` (Dropdown A/B/O/AB, Active, tidak Required; Tabel Data Uji Pre-setup No. 13), dibuat dan diaktifkan di hook `before`, dihapus atau dinonaktifkan di hook `after`. Opsi `AB` dihapus oleh langkah spec.
  - Nilai field wajib lain milik spec: First Name `Rujuk`; Last Name `Divisi` atau `Opsi`; Email `rujukdivisi+{runId}-127@qwertysystem.net` dan `rujukopsi+{runId}-127@qwertysystem.net`; Division `Logistics` dan Represented By `Ahmad Fauzi` pada TC-GS-NLU-86; Position tidak diisi.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-127`, Division milik spec, dan Custom Field uji lewat API.
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: Custom Field uji `Blood Type Uji` (opsi `AB` dihapus), dipulihkan atau dibuang di hook `after`. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-85: Division yang dihapus sebelum submit ditolak server

1. Klik `[+ Non-Login User]`
2. Isi First Name `Rujuk`, Last Name `Divisi`, Email `rujukdivisi+{runId}-127@qwertysystem.net`, dan pilih Division `Divisi Hapus {runId}-127`
3. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
4. Hapus Division `Divisi Hapus {runId}-127` dari master data lewat sesi API aktor hingga perubahan tersimpan
5. Klik `[Submit]`
6. Verifikasi server menolak dengan pesan inline di bawah dropdown Division: `This division no longer exists. Please select another.`
7. Verifikasi pilihan Division auto-clear
8. Klik dropdown Division
9. Verifikasi opsi di-fetch ulang: daftar memuat `Logistics` dan tidak memuat `Divisi Hapus {runId}-127`
10. Verifikasi field lain tetap terisi
11. Verifikasi Popup Create tetap terbuka

### TC-GS-NLU-86: Custom Field dropdown yang dihapus sebelum submit ditolak server

12. Klik `[Clear Field]`
13. Isi First Name `Rujuk`, Last Name `Opsi`, Email `rujukopsi+{runId}-127@qwertysystem.net`, dan pilih Division `Logistics`
14. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
15. Pilih Blood Type Uji `AB`
16. Hapus opsi `AB` dari Custom Field Blood Type Uji lewat sesi API aktor hingga perubahan tersimpan
17. Klik `[Submit]`
18. Verifikasi server menolak dengan pesan inline di bawah Blood Type Uji: `This blood type uji no longer exists. Please select another.`
19. Verifikasi pilihan Blood Type Uji auto-clear
20. Verifikasi field lain tetap terisi
21. Verifikasi Popup Create tetap terbuka
22. Klik `✕`
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-NLU-81, 82, dan 84 ada di spec 022.
- Pelaku penghapusan memakai sesi API aktor (kemampuan dari `suite.md`), bukan konteks UI kedua; butir `P-2` tidak dipakai.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 (membuka dropdown untuk mengamati opsi), langkah 12 (`[Clear Field]` mengosongkan isian TC-GS-NLU-85), langkah 22 sampai 24 (menutup form dirty secara deterministik; S-08).
- Temuan untuk QA:
  - TC-GS-NLU-85 menyebut "Division yang akan dihapus" tanpa nama; spec memakai `Divisi Hapus {runId}-127`. TC-GS-NLU-86 memakai `Blood Type Uji` dari Pre-setup No. 13 yang dibuat Active hanya selama TC berjalan.
  - TC-GS-NLU-85 Expected b "opsi di-fetch ulang" tidak punya cara pengamatan; spec mengasersi isi daftar dropdown (langkah 9).
  - Post Condition kedua TC berupa `-` sehingga tidak diasersi.
