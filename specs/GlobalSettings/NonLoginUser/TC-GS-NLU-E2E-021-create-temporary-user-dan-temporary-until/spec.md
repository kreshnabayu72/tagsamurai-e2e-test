---
id: TC-GS-NLU-E2E-021-create-temporary-user-dan-temporary-until
title: "Create: Temporary User dan Temporary Until"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-78
  - TC-GS-NLU-79
  - TC-GS-NLU-80
  - TC-GS-NLU-90
coverage:
  web: automated
---

# Create: Temporary User dan Temporary Until

## Prerequisites

- Mode: FE+BE (backend nyata; validasi server atas Temporary Until dan record dibaca dari backend nyata; TC-GS-NLU-90 menyuntikkan nilai ke state date picker di browser).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By).
- Data Dinamis, nilai field wajib lain milik spec (TC tidak menyebut nilainya): First Name `Temp`, Last Name `Uji` (TC-GS-NLU-79 dan TC-GS-NLU-90, tidak tersimpan) atau `Uji {runId}-021` (TC-GS-NLU-80, tersimpan), Division `Logistics`, Represented By `Ahmad Fauzi`. Email TC-GS-NLU-79 dan TC-GS-NLU-90 `tempuji1+{runId}-021@qwertysystem.net` (tidak tersimpan); Email TC-GS-NLU-80 `tempuji2+{runId}-021@qwertysystem.net` (tersimpan). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-021` lewat API (mekanisme disediakan tim FE/BE).
- Kemampuan teknis: menyuntikkan nilai tanggal hari ini langsung ke state date picker `Temporary Until` (melewati penonaktifan tanggal di UI) untuk TC-GS-NLU-90; membaca jumlah total baris tabel (baseline B0). Mekanisme penyuntikan tidak disebut TC, PRD, atau LLD (disediakan tim FE).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

1. Catat jumlah total baris tabel Non-Login User sebagai baseline B0

### TC-GS-NLU-78: Checkbox Set as Temporary User menampilkan dan menyembunyikan Temporary Until

2. Klik `[+ Non-Login User]`
3. Centang `Set as Temporary User`
4. Verifikasi date picker `Temporary Until` tampil dengan placeholder `Select date`
5. Pilih Temporary Until besok
6. Hapus centang `Set as Temporary User`
7. Verifikasi field `Temporary Until` hilang
8. Centang kembali `Set as Temporary User`
9. Verifikasi date picker `Temporary Until` tampil kosong dengan placeholder `Select date` (nilainya dikosongkan)

### TC-GS-NLU-79: Temporary User tercentang tanpa Temporary Until ditolak

10. Biarkan Temporary Until kosong; lengkapi field wajib lain: First Name `Temp`, Last Name `Uji`, Email `tempuji1+{runId}-021@qwertysystem.net`, pilih Division `Logistics` dan Represented By `Ahmad Fauzi`
11. Klik `[Submit]`
12. Verifikasi pesan inline di bawah Temporary Until: `Temporary until must not be empty`
13. Verifikasi Popup Create tetap terbuka

### TC-GS-NLU-90: Server menolak Temporary Until hari ini yang lolos date picker

14. Suntikkan nilai tanggal hari ini langsung ke state date picker Temporary Until
15. Klik `[Submit]`
16. Verifikasi pesan inline di bawah Temporary Until: `Please select a future date.`
17. Verifikasi Popup Create tetap terbuka

### Penutup dan asersi record tidak tersimpan

18. Klik `✕`
19. Verifikasi dialog `Unsaved Changes` tampil
20. Klik `[Leave]`
21. Verifikasi jumlah total baris tabel sama dengan baseline B0

### TC-GS-NLU-80: Date picker Temporary Until menonaktifkan hari ini dan tanggal lampau serta menerima besok

22. Klik `[+ Non-Login User]`
23. Centang `Set as Temporary User` dan buka date picker `Temporary Until`
24. Verifikasi tanggal kemarin dan hari ini disabled (tidak dapat dipilih)
25. Pilih tanggal besok
26. Lengkapi field wajib lain: First Name `Temp`, Last Name `Uji {runId}-021`, Email `tempuji2+{runId}-021@qwertysystem.net`, pilih Division `Logistics` dan Represented By `Ahmad Fauzi`
27. Klik `[Submit]`
28. Verifikasi tanggal besok tersimpan sukses
29. Ketik Search `Temp Uji {runId}-021`, tekan Enter
30. Buka Detail record `Temp Uji {runId}-021`
31. Verifikasi Detail menampilkan `Temporary until` tanggal besok

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC mengubah nomor TC: dua validasi ditolak (TC-GS-NLU-79, 90) mendahului aksi sukses (TC-GS-NLU-80) sehingga klausa "tidak ada record dibuat/diubah" pada TC-GS-NLU-79 dan TC-GS-NLU-90 dapat diasersi terhadap B0 di langkah 21 sebelum record TC-GS-NLU-80 tersimpan (S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline B0), langkah 5, 6, dan 8 (memilih tanggal dulu agar klausa "nilainya dikosongkan" TC-GS-NLU-78 Expected b teramati), langkah 18 sampai 20 (menutup form dirty secara deterministik; S-08), langkah 29 (Search untuk menemukan baris target; R-16), langkah 30 (membuka Detail).
- P-5 (b): TC-GS-NLU-90 (kelas b, penyuntikan nilai tanggal ke state date picker) adalah satu TC objek uji ringan tanpa harness eksternal dan tanpa state berat sendiri; ia berada di spec fungsional Create ini karena permukaannya sama (Popup Create, Temporary Until).
- Pada langkah 10 popup masih berisi centang `Set as Temporary User` dari langkah 8; langkah 14 melanjutkan form yang sama dengan error inline berbeda sehingga tidak butuh `[Clear Field]`.
- Temuan untuk QA:
  - TC-GS-NLU-78 langkah 3 hanya mengamati field baru dan langkah 4 menghapus centang; nilai Temporary Until tidak pernah diisi sebelum dihapus centangnya, sehingga "nilainya dikosongkan" tidak teramati. Spec menambah langkah penghubung 5 dan 8 agar klausa itu bisa diasersi.
  - TC-GS-NLU-90 menyebut "Injeksi nilai tanggal hari ini langsung ke state date picker" tanpa cara; spec menuliskannya sebagai kemampuan teknis disediakan tim FE.
  - TC-GS-NLU-80 Expected b menyebut `Temporary until [tanggal besok]` pada Detail; format tanggal bergantung General Settings (Pre-setup No. 16: `dd/MM/yy`) dan tidak ditulis di TC; spec mengasersi tanggal besok dalam format Detail yang berlaku.
  - TC-GS-NLU-79, 80, dan 90 tidak menyebut nilai field wajib lain; spec memakai nilai pilihannya sendiri (lihat Prerequisites).
  - TC-GS-NLU-80 tidak menyebut cara menemukan baris; spec mencari lewat Name bersuffix di langkah 29 (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
