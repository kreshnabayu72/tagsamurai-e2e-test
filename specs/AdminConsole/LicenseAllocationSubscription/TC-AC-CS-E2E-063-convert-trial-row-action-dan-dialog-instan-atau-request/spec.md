---
id: TC-AC-CS-E2E-063-convert-trial-row-action-dan-dialog-instan-atau-request
title: "Convert Trial: Row Action dan Dialog Instan atau Request"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-239
  - TC-AC-CS-240
  - TC-AC-CS-241
coverage:
  web: automated
---

# Convert Trial: Row Action dan Dialog Instan atau Request

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Distributor PT Maju Bersama, Eko Saputra (Pre-setup #9), `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_DIST_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Read Only Distributor PT Maju Bersama, Wulan Sari (Pre-setup #10), `readOnlyDistSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_RO_DIST_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Group Manager scope Group Jawa Distributor PT Maju Bersama, Dewi Anggraini (Pre-setup #5), `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_GM_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup: trial Active `Klinik Harapan Bunda` SAMS Growth (Start `10/08/26`, End `08/09/26`, Plan Owner CV Karya Mandiri) tanpa term paid SAMS (#71); trial Expired `Klinik Harapan Bunda` FAMS Starter (End `30/07/26`) tanpa term paid FAMS (#72); trial Waiting `SUBS-20260819-00004` Client PT Bintang Timur (#59); trial Rejected `Klinik Gigi Ceria` FAMS Growth (#80); trial Canceled `Optik Cahaya` FAMS Professional (#81); trial Active FAMS Growth milik Partner CV Karya Mandiri untuk Client `Bengkel Cahaya Motor` (binaan langsung CV Karya Mandiri, di luar scope WRITE Distributor) (#44, #74); Toggle Require Approval for Allocation ON untuk TC-AC-CS-241 (#23); harga SAMS Professional $7,000.00 per tahun (#27); Group Manager `Dewi Anggraini` (#5) bypass.
- Akun Read Only Distributor `Wulan Sari` Pre-setup #10 tidak tertulis di Pre-setup TC; email `readOnlyDistSub_automated_{namaCompany}@qwertysystem.net` dari TC-AC-CS-239 dan kredensial lewat `Spectra.env.AC_SUB_RO_DIST_PASSWORD` (nama baru, disediakan tim FE dan didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Data Dinamis: tidak ada data bersuffix; dialog Convert Trial tidak dikonfirmasi sehingga data tidak berubah.

## Test Steps

### TC-AC-CS-239: Row action Convert hanya untuk trial Active atau Expired dalam scope WRITE dengan capability Create

1. Ketik Search `Klinik Harapan Bunda`, tekan Enter, lalu buka menu row action baris trial Active SAMS Growth
2. Verifikasi menu memuat Convert
3. Tutup menu lalu buka menu row action baris trial Expired FAMS Starter
4. Verifikasi menu memuat Convert
5. Tutup menu, ganti isi kotak search dengan `PT Bintang Timur`, tekan Enter, lalu buka menu row action baris trial Waiting for Approval
6. Verifikasi menu memuat item Detail
7. Verifikasi menu tidak memuat Convert
8. Tutup menu, ganti isi kotak search dengan `Bengkel Cahaya Motor`, tekan Enter, lalu buka menu row action baris trial Active milik Partner
9. Verifikasi menu memuat item Detail
10. Verifikasi menu tidak memuat Convert karena di luar scope WRITE
11. Tutup menu, klik tab `History`, ganti isi kotak search dengan `Klinik Gigi Ceria`, tekan Enter, lalu buka menu row action baris trial Rejected
12. Verifikasi menu memuat item Detail
13. Verifikasi menu tidak memuat Convert
14. Tutup menu, ganti isi kotak search dengan `Optik Cahaya`, tekan Enter, lalu buka menu row action baris trial Canceled
15. Verifikasi menu memuat item Detail
16. Verifikasi menu tidak memuat Convert
17. Tutup menu. Ganti akun: Logout lalu login sebagai Read Only Distributor (`Wulan Sari`)
18. Buka menu Allocation > Client Subscription
19. Klik tab `Current`, ketik Search `Klinik Harapan Bunda`, tekan Enter, lalu buka menu row action baris trial Active
20. Verifikasi menu memuat item Detail
21. Verifikasi menu tidak memuat Convert

### TC-AC-CS-240: Dialog Convert Trial untuk jalur instan menampilkan notice dan Estimated Cost

22. Tutup menu. Ganti akun: Logout lalu login sebagai Group Manager (`Dewi Anggraini`)
23. Buka menu Allocation > Client Subscription
24. Ketik Search `Klinik Harapan Bunda`, tekan Enter
25. Klik ikon `⋯` pada baris trial Active SAMS Growth lalu pilih `Convert`
26. Pilih Plan `Professional`, isi Duration `1` lalu klik `[Submit]`
27. Verifikasi Header: Title "Convert Trial"
28. Verifikasi Body: bullet "• Klinik Harapan Bunda — SAMS"
29. Verifikasi Body: notice "This client has an active trial (Growth). Continuing will convert the trial to a paid subscription. The trial ends as soon as you confirm and any remaining trial days are forfeited; the paid term starts on its start date."
30. Verifikasi Body: baris Feature pricing charge "Estimated Cost: $7,000.00 (1 year(s) × $7,000.00/year)"
31. Verifikasi Body: penutup "Are you sure you want to convert it?"
32. Verifikasi Footer: tombol `[Go Back]` dan `[Convert]`
33. Klik `[Go Back]`, klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`

### TC-AC-CS-241: Dialog Convert Trial untuk requester biasa dengan toggle ON memakai notice pengajuan

34. Ganti akun: Logout lalu login sebagai Create-Only Distributor (`Fajar Nugroho`)
35. Buka menu Allocation > Client Subscription
36. Ketik Search `Klinik Harapan Bunda`, tekan Enter
37. Klik ikon `⋯` pada baris trial Active SAMS Growth lalu pilih `Convert`
38. Pilih Plan `Professional`, isi Duration `1` lalu klik `[Submit]`
39. Verifikasi notice "This client has an active trial (Growth). Continuing will submit a request to convert the trial to a paid subscription. The trial stays active until an approver decides; if approved, any remaining trial days are forfeited."
40. Verifikasi Title "Convert Trial", bullet "• Klinik Harapan Bunda — SAMS", baris Estimated Cost, penutup "Are you sure you want to convert it?", dan tombol `[Go Back]` serta `[Convert]`
41. Klik `[Go Back]`, klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`

## Notes

- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); menu row action ditutup sebelum menu berikutnya; `Go Back`, `✕`, dialog `Unsaved Changes`, dan `[Leave]` menutup form dirty (S-08, S-09); ganti akun eksplisit (S-07), diikuti `Buka menu Allocation > Client Subscription` sebelum Search (S-14); Search pada kotak terisi ditulis "ganti isi kotak search dengan" (8b.9).
- Anchor absence (bagian 8b butir 2): ketiadaan Convert pada tiap menu didahului Verifikasi item Detail tampil pada menu yang sama.
- Alasan melewati sekitar 35 langkah: semua blok satu topik (permukaan Convert Trial) tanpa kelas harness lain; langkah absence per menu berulang menurut data (bagian 8b butir 7).
- Temuan untuk QA: (1) TC-AC-CS-239 butir "trial Active milik Partner di luar scope WRITE" memakai Pre-setup #44 dan #74 tetapi tidak menyebut ID baris; spec mencarinya lewat nama Client. (2) Akun Read Only `Wulan Sari` (Pre-setup #10) tidak tertulis di Pre-setup TC dan password env `AC_SUB_RO_DIST_PASSWORD` belum didaftarkan di `suite.md`; penyelaras suite perlu menambahkannya. (3) TC-AC-CS-241 mengacu "Toggle ON" tanpa nilai Estimated Cost; spec mengasersi baris ada.
