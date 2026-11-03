---
id: TC-GS-NLU-E2E-119-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis
title: "State tenant: Client Suspended dan Expired menolak aksi tulis, Auto-Deactivate di Suspended"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-438
  - TC-GS-NLU-439
  - TC-GS-NLU-497
coverage:
  web: automated
---

# State tenant: Client Suspended dan Expired menolak aksi tulis, Auto-Deactivate di Suspended

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; state Client (Suspended, Expired) disiapkan sebagai Pre-setup No. 15 dan tidak diubah spec ini. Tidak ada respons yang di-mock atau di-intercept.
- Role yang diuji (Total Control pada Client uji; password hanya lewat `Spectra.env`):

| TC | Client | State | Akun | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-438, 497 | PT Sinar Abadi | Suspended | Total Control Client PT Sinar Abadi; email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD` |
| TC-GS-NLU-439 | PT Sinar Lama | Expired | Total Control Client PT Sinar Lama; email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.GS_CLIENTEXP_TC_PASSWORD` |

- Environment variable: `GS_CLIENTSUSP_TC_PASSWORD`, `GS_CLIENTEXP_TC_PASSWORD`.
- Login akun aktor pertama (Total Control PT Sinar Abadi) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec di Client uji (dibuat fixture BE yang melewati guard Suspended dan Expired, dibersihkan hook `after`; mekanisme disediakan tim FE/BE; Division `Operations`, Email `<nama>+{runId}-119@qwertysystem.net`, Active):
  - PT Sinar Abadi: `Suspend Edit {runId}-119`, `Suspend Hapus {runId}-119`, `Suspend Status {runId}-119`, `Suspend Convert {runId}-119`, dan `Auto Suspend Satu {runId}-119` (Temporary Until kemarin, TC-GS-NLU-497).
  - PT Sinar Lama: `Expired Convert {runId}-119`.
  - Payload Create yang ditolak (TC-GS-NLU-438): First Name `Ditolak`, Last Name `Buat {runId}-119`, Division `Logistics`, Email `ditolakbuat+{runId}-119@qwertysystem.net`, Represented By `Ahmad Fauzi`.
- Kemampuan teknis: pengamatan status respons permintaan tulis (`403 Forbidden`), fixture jadwal untuk menjalankan job Auto-Deactivate (00.00 zona waktu client), dan polling worker commit (muat ulang halaman tiap 5 detik, batas 2 menit).
- Baseline log TC-GS-NLU-497: jumlah entri Activity Log dengan Action `Auto-Deactivate` dan aktor `System` dicatat sebelum job; kemampuan membaca jumlah entri disediakan tim FE/BE.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-119` yang tersisa tanpa mengasumsikan seeding berhasil penuh. State Client tidak diubah spec ini.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-438: Aksi tulis pada entitas Suspended ditolak server dengan toast baku

1. Verifikasi data Non-Login User terbaca: sedikitnya satu baris tampil di tabel
2. Buka Global Settings > Activity Log lewat sidebar dan catat jumlah entri aktor `System` dengan Action `Auto-Deactivate` sebagai baseline
3. Buka sub-tab Non-Login User lewat sidebar
4. Klik `[+ Non-Login User]`
5. Isi First Name `Ditolak`, Last Name `Buat {runId}-119`, Division `Logistics`, Email `ditolakbuat+{runId}-119@qwertysystem.net`
6. Pilih Represented By `Ahmad Fauzi` lewat popup Select User
7. Klik `[Submit]`
8. Verifikasi server menolak dengan `403 Forbidden`
9. Verifikasi Toast error `Changes can't be saved while this workspace is suspended or expired.`
10. Tutup popup Create dengan `✕`
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`
13. Ketik Search `Suspend Edit {runId}-119`, tekan Enter, klik `⋯` baris `Suspend Edit {runId}-119` > `Edit`
14. Ubah First Name menjadi `Diubah`, lalu klik `[Save]`
15. Verifikasi server menolak dengan `403 Forbidden`
16. Verifikasi Toast error `Changes can't be saved while this workspace is suspended or expired.`
17. Tutup Popup Edit dengan `✕`
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`
20. Ketik Search `Suspend Hapus {runId}-119`, tekan Enter, klik `⋯` baris `Suspend Hapus {runId}-119` > `Delete`
21. Klik `[Delete]` pada dialog konfirmasi
22. Verifikasi server menolak dengan `403 Forbidden`
23. Verifikasi Toast error `Changes can't be saved while this workspace is suspended or expired.`
24. Ketik Search `Suspend Status {runId}-119`, tekan Enter, klik switch Active baris `Suspend Status {runId}-119` (ON)
25. Klik `[Deactivate]` pada dialog konfirmasi
26. Verifikasi server menolak dengan `403 Forbidden`
27. Verifikasi Toast error `Changes can't be saved while this workspace is suspended or expired.`
28. Ketik Search `Suspend Convert {runId}-119`, tekan Enter, klik `⋯` baris `Suspend Convert {runId}-119` > `Convert to Login User`
29. Klik `[Convert]` pada dialog konfirmasi
30. Verifikasi server menolak dengan `403 Forbidden`
31. Verifikasi Toast error `Changes can't be saved while this workspace is suspended or expired.`
32. Verifikasi halaman tetap di sub-tab Non-Login User, tanpa redirect, setelah kelima aksi tulis
33. Verifikasi kontrol UI mengikuti capability Total Control, bukan state entitas: `[+ Non-Login User]` tampil dan aktif

### TC-GS-NLU-497: Auto-Deactivate tetap berjalan pada entitas Suspended

34. Ketik Search `Auto Suspend Satu {runId}-119`, tekan Enter
35. Jalankan job Auto-Deactivate lewat fixture jadwal, lalu muat ulang halaman tiap 5 detik sampai switch Active baris `Auto Suspend Satu {runId}-119` OFF (batas tunggu 2 menit)
36. Verifikasi switch Active baris `Auto Suspend Satu {runId}-119` OFF
37. Klik Name baris `Auto Suspend Satu {runId}-119` untuk membuka Detail, lalu klik tab `Changelog`
38. Verifikasi Tab Changelog Detail: entri `Auto-Deactivate` Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `System`
39. Buka Global Settings > Activity Log lewat sidebar
40. Verifikasi Activity Log: jumlah entri aktor `System` dengan Action `Auto-Deactivate` bertambah satu dibanding baseline dan entri baru memuat object Non-Login User

### TC-GS-NLU-439: Aksi tulis pada entitas Expired ditolak dengan toast yang sama

41. Ganti akun: logout dari Total Control PT Sinar Abadi, lalu login sebagai Total Control PT Sinar Lama (`Spectra.env.GS_CLIENTEXP_TC_PASSWORD`)
42. Buka Global Settings > User > User List > sub-tab Non-Login User lewat sidebar, ketik Search `Expired Convert {runId}-119`, tekan Enter, klik `⋯` baris tersebut > `Convert to Login User`
43. Klik `[Convert]` pada dialog konfirmasi
44. Verifikasi Toast error `Changes can't be saved while this workspace is suspended or expired.`
45. Verifikasi baris `Expired Convert {runId}-119` tetap ada sebagai Non-Login User (record tidak berubah)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 4, 13, 20, 24, 28, 34, 42 (membuka popup atau menu dan Search record yang dicari), langkah 10, 17 (menutup form dirty: `✕`, `Verifikasi` dialog `Unsaved Changes`, `[Leave]`, S-08), langkah 41 (ganti akun eksplisit, S-07).
- Urutan TC dalam spec: TC-GS-NLU-438, 497, 439. TC-GS-NLU-497 memakai akun PT Sinar Abadi yang sama dengan TC-GS-NLU-438, sehingga dijalankan sebelum ganti akun ke PT Sinar Lama (TC-GS-NLU-439).
- Job Auto-Deactivate pada TC-GS-NLU-497 hanya pemicu kondisi yang diasersi (bagian 3 prinsip 13, P-2 untuk proses sistem yang memicu kondisi); polling memakai idiom baku muat ulang tiap 5 detik dengan batas 2 menit (bagian 6).
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 45 langkah, 6 di antaranya blok baca-log berpola. Semua blok kelas h (state tenant) dan berdiri sendiri: tiap aksi tulis ditolak memakai record milik spec sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-NLU-438 dan 439 menyebut aktor Total Control entitas Suspended dan Expired tanpa email akun; email tidak tertulis di Pre-setup TC. Env `GS_CLIENTSUSP_TC_PASSWORD` dan `GS_CLIENTEXP_TC_PASSWORD` sudah terdaftar untuk "Client uji Suspended/Expired" (Auth > MFA) dan dipakai ulang bila akunnya sama dengan PT Sinar Abadi dan PT Sinar Lama; konfirmasi tim FE.
  - TC-GS-NLU-497 berlabel Automation "Manual Only" (job terjadwal sisi server tidak dapat dipicu dari klien), tetapi Precondition TC menyebut job dijalankan lewat fixture jadwal; spec memakai fixture itu (disediakan tim FE/BE).
  - TC-GS-NLU-438 Expected b menyebut `403 Forbidden` dan Expected c "kontrol UI mengikuti capability"; spec mengamati status respons dan keberadaan `[+ Non-Login User]` saja karena TC tidak menyebut kontrol lain.
  - Seeding record di Client Suspended dan Expired ditolak guard tulis; pembuatan lewat fixture BE yang melewati guard disediakan tim FE/BE.
