---
id: TC-GS-NLU-E2E-022-create-referensi-represented-by-dan-position-dihapus-atau-di-rename
title: "Create: referensi Represented By dan Position dihapus atau di-rename sebelum Submit"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-81
  - TC-GS-NLU-82
  - TC-GS-NLU-84
coverage:
  web: automated
---

# Create: referensi Represented By dan Position dihapus atau di-rename sebelum Submit

## Prerequisites

- Mode: FE+BE (backend nyata; penghapusan dan rename referensi dilakukan di backend nyata lewat sesi API aktor, bukan konteks UI kedua).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`); pelaku penghapusan dan rename memakai sesi API aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Position `Driver`, Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By). TC menulis target hapus dan rename dari Pre-setup (`Wawan Setiadi`, `Driver`, `Logistics`, `Ahmad Fauzi`); spec memakai padanan milik spec supaya data Pre-setup tidak berubah (S-06).
- Data Dinamis, di-seed lewat API di hook `before` (mekanisme seeding dan penghapusan disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD):
  - Login User Active `Wakil Hapus {runId}-022` (target hapus TC-GS-NLU-81).
  - Login User Active `Wakil Rename {runId}-022`, Position `Posisi Rename {runId}-022`, Division `Divisi Rename {runId}-022` (target rename TC-GS-NLU-82; nama setelah rename `Wakil Rename Baru {runId}-022`, `Posisi Rename Baru {runId}-022`, `Divisi Rename Baru {runId}-022`).
  - Position `Posisi Hapus {runId}-022` (target hapus TC-GS-NLU-84).
  - Nilai field wajib lain milik spec: First Name `Rujuk`; Last Name `Hapus`, `Rename {runId}-022`, atau `Posisi`; Email `rujukhapus+{runId}-022@qwertysystem.net`, `rujukrename+{runId}-022@qwertysystem.net`, `rujukposisi+{runId}-022@qwertysystem.net`; Division `Logistics` kecuali disebut lain; Represented By `Ahmad Fauzi` pada TC-GS-NLU-84.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-022`, Login User, Position, dan Division milik spec lewat API.
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada pada data Pre-setup. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-81: Represented By yang dihapus sebelum submit ditolak server

1. Klik `[+ Non-Login User]`
2. Isi First Name `Rujuk`, Last Name `Hapus`, Email `rujukhapus+{runId}-022@qwertysystem.net`, dan pilih Division `Logistics`
3. Klik `[+ Select User]`, klik baris `Wakil Hapus {runId}-022` pada popup Select User, klik `[Select]`
4. Hapus Login User `Wakil Hapus {runId}-022` lewat sesi API aktor hingga perubahan tersimpan
5. Klik `[Submit]`
6. Verifikasi server menolak dengan pesan inline di bawah Represented By: `This user no longer exists. Please select another.`
7. Verifikasi Represented By kembali ke `[+ Select User]` (badge hilang)
8. Verifikasi field lain yang valid tetap terisi
9. Verifikasi Popup Create tetap terbuka

### TC-GS-NLU-82: Rename Position, Division, atau Represented By sebelum submit bukan error

10. Klik `[Clear Field]`
11. Isi First Name `Rujuk`, Last Name `Rename {runId}-022`, Email `rujukrename+{runId}-022@qwertysystem.net`, pilih Position `Posisi Rename {runId}-022` dan Division `Divisi Rename {runId}-022`
12. Klik `[+ Select User]`, klik baris `Wakil Rename {runId}-022` pada popup Select User, klik `[Select]`
13. Rename Position, Division, dan Login User ketiganya lewat sesi API aktor hingga perubahan tersimpan
14. Klik `[Submit]`
15. Verifikasi Submit sukses tanpa error dan tanpa auto-clear: Popup Create tertutup
16. Ketik Search `Rujuk Rename {runId}-022`, tekan Enter
17. Buka Detail record `Rujuk Rename {runId}-022`
18. Verifikasi Detail menampilkan nama terbaru Position `Posisi Rename Baru {runId}-022`
19. Verifikasi Detail menampilkan nama terbaru Division `Divisi Rename Baru {runId}-022`
20. Verifikasi Detail menampilkan nama terbaru Represented By `Wakil Rename Baru {runId}-022`
21. Kembali ke User List sub-tab Non-Login User

### TC-GS-NLU-84: Position yang dihapus sebelum submit ditolak server

22. Klik `[+ Non-Login User]`
23. Isi First Name `Rujuk`, Last Name `Posisi`, Email `rujukposisi+{runId}-022@qwertysystem.net`, pilih Position `Posisi Hapus {runId}-022` dan Division `Logistics`
24. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
25. Hapus Position `Posisi Hapus {runId}-022` dari master data lewat sesi API aktor hingga perubahan tersimpan
26. Klik `[Submit]`
27. Verifikasi server menolak dengan pesan inline di bawah dropdown Position: `This position no longer exists. Please select another.`
28. Verifikasi pilihan Position auto-clear
29. Klik dropdown Position
30. Verifikasi opsi di-fetch ulang: daftar memuat `Driver` dan tidak memuat `Posisi Hapus {runId}-022`
31. Verifikasi field lain tetap terisi
32. Verifikasi Popup Create tetap terbuka
33. Klik `✕`
34. Verifikasi dialog `Unsaved Changes` tampil
35. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-NLU-85 dan TC-GS-NLU-86 (Division dan Custom Field dihapus) ada di spec 127.
- Pelaku penghapusan dan rename memakai sesi API aktor (kemampuan dari `suite.md`), bukan konteks UI kedua; butir `P-2` tidak dipakai.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 (`[Clear Field]` mengosongkan isian TC-GS-NLU-81), langkah 16 (Search untuk menemukan baris target; R-16), langkah 17 (membuka Detail), langkah 21 (kembali ke daftar), langkah 29 (membuka dropdown untuk mengamati opsi), langkah 33 sampai 35 (menutup form dirty secara deterministik; S-08).
- TC-GS-NLU-81 memberi pilihan "dinonaktifkan atau dihapus"; spec memilih dihapus agar sesuai teks pesan `no longer exists`.
- Langkah 15 memetakan klausa Expected a TC-GS-NLU-82 ("tanpa error dan tanpa auto-clear") lewat popup yang tertutup sukses; error inline atau auto-clear tidak dapat diamati sesudah popup tertutup.
- Temuan untuk QA:
  - TC-GS-NLU-81, 82, dan 84 memakai data Pre-setup (`Wawan Setiadi`, `Driver`, `Logistics`, `Ahmad Fauzi`) sebagai target hapus atau rename; hal ini bertentangan dengan data Pre-setup yang hanya dibaca. Spec memakai padanan milik spec.
  - TC-GS-NLU-84 menyebut "Position yang akan dihapus" tanpa nama; spec memakai `Posisi Hapus {runId}-022`.
  - TC-GS-NLU-84 Expected b "opsi di-fetch ulang" tidak punya cara pengamatan; spec mengasersi isi daftar dropdown (langkah 30).
  - TC-GS-NLU-82 tidak menyebut cara menemukan baris; spec mencari lewat Name bersuffix di langkah 16 (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
