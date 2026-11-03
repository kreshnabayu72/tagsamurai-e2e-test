---
id: TC-AC-ACC-E2E-237-defense-aksi-asset-control-client-archived-suspended-dan-role-read
title: "Defense: Aksi Asset Control Hidden dan Request Langsung Ditolak Server untuk Client Archived, Suspended, dan Role Read"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-335
  - TC-AC-ACC-336
  - TC-AC-ACC-905
coverage:
  web: automated
---

# Defense: Aksi Asset Control Hidden dan Request Langsung Ditolak Server untuk Client Archived, Suspended, dan Role Read

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-AC-ACC-905). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite. Akun kedua: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (TC-AC-ACC-335). Akun ketiga: Active-Read A-04 `activeReadJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client: Read pada Area Jakarta), password `Spectra.env.AC_CLIENT_ACTIVE_READ_PASSWORD` (TC-AC-ACC-336). Nama env password baru didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script. Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, state tidak berubah karena request ditolak; skrip seed): C-AST-6 "PT Arsip Belum Aktif" (Archived; Station "Stasiun Arsip" Active dengan Tablet "Tablet Arsip 1" Active); C-AST-5 "PT Suspend Belum Aktif" (Suspended; Station "Stasiun Suspend" Active dengan Tablet "Tablet Suspend 1" Active).
- Data Pre-setup (hanya dibaca): C-01 "PT Sejahtera Abadi" dengan Station "Gerbang Gudang B" (Inactive) dan Tablet "Tablet Gudang B 1" (Inactive).
- Kemampuan teknis: klien HTTP yang mengirim request Generate Enrollment QR, Deactivate Station, dan Revoke Tablet langsung ke server dengan token sesi aktor yang sedang login, tanpa melewati browser (disediakan tim FE/BE; endpoint tidak dikarang di spec ini).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-905: Client Archived (Total Control)

1. Klik sub-tab Archived, ketik Search "PT Arsip Belum Aktif", tekan Enter, lalu klik Company Name "PT Arsip Belum Aktif"
2. Klik Tab Asset Control
3. Verifikasi Station Quota dan Station List dapat dibaca (Station "Stasiun Arsip" tampil)
4. Verifikasi tombol [Generate Enrollment QR] Hidden
5. Klik row Station "Stasiun Arsip" untuk expand Tablet List
6. Verifikasi row action Deactivate pada Station "Stasiun Arsip" Hidden
7. Verifikasi row action Revoke pada Tablet "Tablet Arsip 1" Hidden
8. Kirim request Generate Enrollment QR langsung untuk Client "PT Arsip Belum Aktif"
9. Verifikasi respons 403 Forbidden
10. Kirim request Deactivate Station langsung untuk "Stasiun Arsip"
11. Verifikasi respons 403 Forbidden
12. Kirim request Revoke Tablet langsung untuk "Tablet Arsip 1"
13. Verifikasi respons 403 Forbidden
14. Muat ulang Detail (F5), klik Tab Asset Control, lalu klik row Station "Stasiun Arsip" untuk expand Tablet List
15. Verifikasi Status "Stasiun Arsip" tetap `Active`
16. Verifikasi Status "Tablet Arsip 1" tetap `Active`

### Ganti akun

17. Logout, lalu login sebagai Active-Full A-15 (`activeFullJakarta_automated_qaTeam1@qwertysystem.net`)

### TC-AC-ACC-335: Client Suspended (Active-Full)

18. Klik sub-tab Suspended, ketik Search "PT Suspend Belum Aktif", tekan Enter, lalu klik Company Name "PT Suspend Belum Aktif"
19. Klik Tab Asset Control dan catat Station Quota
20. Verifikasi Tab Asset Control tetap tampil: Station Quota dan Station List dapat dibaca
21. Klik row Station "Stasiun Suspend" untuk expand Tablet List
22. Verifikasi tombol [Generate Enrollment QR] Hidden
23. Verifikasi row action Deactivate pada Station "Stasiun Suspend" Hidden
24. Verifikasi row action Revoke pada Tablet "Tablet Suspend 1" Hidden
25. Kirim request Generate Enrollment QR langsung untuk Client "PT Suspend Belum Aktif"
26. Verifikasi respons 403 Forbidden
27. Kirim request Deactivate Station langsung untuk "Stasiun Suspend"
28. Verifikasi respons 403 Forbidden
29. Kirim request Revoke Tablet langsung untuk "Tablet Suspend 1"
30. Verifikasi respons 403 Forbidden
31. Muat ulang Detail (F5), klik Tab Asset Control, lalu klik row Station "Stasiun Suspend" untuk expand Tablet List
32. Verifikasi Status "Stasiun Suspend" tetap `Active`
33. Verifikasi Status "Tablet Suspend 1" tetap `Active`
34. Verifikasi Station Quota sama dengan nilai yang dicatat pada langkah 19

### Ganti akun

35. Logout, lalu login sebagai Active-Read A-04 (`activeReadJakarta_automated_qaTeam1@qwertysystem.net`)

### TC-AC-ACC-336: Tanpa Update Manage active client (Active-Read)

36. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control
37. Klik row Station "Gerbang Gudang B" untuk expand Tablet List
38. Verifikasi tombol [Generate Enrollment QR] Hidden
39. Verifikasi row action Deactivate pada Station "Gerbang Gudang B" Hidden
40. Verifikasi row action Revoke pada Tablet "Tablet Gudang B 1" Hidden
41. Kirim request Generate Enrollment QR langsung untuk Client "PT Sejahtera Abadi"
42. Verifikasi respons 403 Forbidden
43. Kirim request Deactivate Station langsung untuk "Gerbang Gudang B"
44. Verifikasi respons 403 Forbidden
45. Kirim request Revoke Tablet langsung untuk "Tablet Gudang B 1"
46. Verifikasi respons 403 Forbidden
47. Muat ulang Detail (F5), klik Tab Asset Control, lalu klik row Station "Gerbang Gudang B" untuk expand Tablet List
48. Verifikasi Status "Gerbang Gudang B" tetap `Inactive`
49. Verifikasi Status "Tablet Gudang B 1" tetap `Inactive`

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-AC-ACC-905, TC-AC-ACC-335, dan TC-AC-ACC-336 adalah TC kelas a (defense-in-depth) dengan Expected berupa respons API; masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md`. Ketiga TC kini mengasersi respons 403 Forbidden untuk request langsung; langkah request langsung hanya mengasersi respons server dan state data (bagian 8b butir 1); perilaku FE untuk respons yang sama ada di spec jalur aksi (spec 238, 239, 234).
- Langkah penghubung (S-03, R-16): langkah 1, 18, 36 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 5, 14, 21, 31, 37, 47 (expand row agar Tablet List teramati dan muat ulang sesudah request langsung).
- Asersi absence Hidden (langkah 4, 6, 7, 22 sampai 24, 38 sampai 40) memakai anchor positif Station Quota dan Station List yang sudah termuat (butir 2 bagian 8b).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (a) dengan pola identik; ganti akun memakai Step eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras.
- Langkah muat ulang (14, 31, 47) adalah langkah penghubung agar state Station dan Tablet dibaca dari server sesudah request langsung (TC-AC-ACC-905 dan 336 tidak menuliskan muat ulang pada langkah). Status Station dan Tablet tetap serta Station Quota sama dengan baseline (TC-AC-ACC-335) diasersi setelah muat ulang.
