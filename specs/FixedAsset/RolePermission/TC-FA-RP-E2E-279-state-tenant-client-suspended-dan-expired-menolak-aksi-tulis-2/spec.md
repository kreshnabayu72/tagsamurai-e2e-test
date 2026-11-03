---
id: TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2
title: "State tenant: Client Suspended dan Expired menolak aksi tulis (2/3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-978
  - TC-FA-RP-979
  - TC-FA-RP-980
  - TC-FA-RP-981
  - TC-FA-RP-982
  - TC-FA-RP-983
coverage:
  web: automated
---

# State tenant: Client Suspended dan Expired menolak aksi tulis (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Client Suspended` (Pre-setup #25), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_SUSPENDED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Env var yang dipakai: `FA_SUSPENDED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: #25 (`Client Suspended`), #15 (Ahmad Fauzi, Citra Lestari, Dimas Pranata), #17 (Indra Kusuma tanpa Home Group), #18, #19 (Require Approval Off di semua node), #20 (sub-tab `Transfer` pada `IT Infrastructure` dengan Require Approval On, Approver Pandu Wijaya, aturan OR, Approval Scope `Both`), dan #39 (Detail Role `Manage Open API` terisi dengan Dimas Pranata dan Citra Lestari). Disiapkan lewat seeding di hook `before`.
- Kemampuan teknis: klien HTTP untuk request langsung ke server dan sesi API Total Control pada `Client Suspended` (disediakan tim FE/BE; tanpa endpoint karangan). Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): status tingkat akses, baris peran, nilai Require Approval, dan aturan persetujuan dibaca untuk Expected "tidak ada perubahan data" atau nilai akhir.
- State global: status `Client Suspended` tidak diubah spec ini; entitas tetap Suspended sepanjang spec.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-978: Client Suspended menolak Remove baris peran dengan toast baku

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Klik `[⋯]` baris Dimas Pranata lalu `Remove`
3. Klik `[Remove]`
4. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
5. Verifikasi kontrol `[Remove]` tidak Disabled dan tidak ada tooltip khusus
6. Verifikasi lewat kemampuan baca baris Dimas Pranata tetap ada pada `Manage Open API` (tidak ada perubahan data)
7. Klik `[Cancel]` pada dialog Remove

### TC-FA-RP-979: Client Suspended menolak Bulk Remove dengan toast baku

8. Tunggu toast lama hilang otomatis
9. Centang baris Dimas Pranata dan Citra Lestari
10. Klik `Bulk Action` > `Remove`
11. Klik `[Remove]`
12. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
13. Verifikasi kontrol `[Remove]` tidak Disabled dan tidak ada tooltip khusus
14. Verifikasi lewat kemampuan baca baris Dimas Pranata dan Citra Lestari tetap ada pada `Manage Open API` (tidak ada perubahan data)
15. Klik `[Cancel]` pada dialog Bulk Remove

### TC-FA-RP-980: Client Suspended menolak Toggle Require Approval dengan toast baku

16. Tunggu toast lama hilang otomatis
17. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
18. Aktifkan toggle
19. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
20. Verifikasi toggle tidak Disabled dan tidak ada tooltip khusus
21. Verifikasi lewat kemampuan baca Require Approval `Disposal` pada `IT Infrastructure` tetap Off (tidak ada perubahan data)

### TC-FA-RP-981: Client Suspended menolak Radio aturan persetujuan dengan toast baku

22. Tunggu toast lama hilang otomatis
23. Klik sub-tab `Transfer` pada node `IT Infrastructure`
24. Pilih radio `All approvers (AND)`
25. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
26. Verifikasi radio tidak Disabled dan tidak ada tooltip khusus
27. Verifikasi lewat kemampuan baca aturan persetujuan `Transfer` pada `IT Infrastructure` tetap `Any approver (OR)` (tidak ada perubahan data)

### TC-FA-RP-982: Client Suspended menolak Assign Role Transaksi dengan toast baku

28. Tunggu toast lama hilang otomatis
29. Klik sub-tab `Disposal` pada node `IT Infrastructure`
30. Klik `[+ Assign]` pada section Asset Admin
31. Centang Ahmad Fauzi
32. Klik `[Assign]`
33. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
34. Verifikasi kontrol `[Assign]` tidak Disabled dan tidak ada tooltip khusus
35. Verifikasi lewat kemampuan baca tidak ada penugasan Asset Admin baru untuk Ahmad Fauzi pada `Disposal` di `IT Infrastructure` (tidak ada perubahan data)
36. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-983: Client Suspended menolak permintaan langsung Set Home Group constraint dengan 403 baku

37. Kirim request langsung ke server (bukan lewat UI) dengan sesi API Total Control pada `Client Suspended` untuk menetapkan Home Group constraint `Data Center` pada Indra Kusuma
38. Verifikasi respons status `403` dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
39. Verifikasi lewat kemampuan baca Indra Kusuma tetap tanpa Home Group constraint (tidak ada perubahan data)

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-978 sampai TC-FA-RP-983).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): "Tunggu toast lama hilang otomatis" sebelum tiap toast baku yang sama diasersi lagi (R-12); membuka tab, Detail Role, node, dan sub-tab; menutup popup atau dialog dengan `[Cancel]` (langkah 7, 15, 36) agar state tidak dibawa ke TC berikutnya (S-09).
- K-1: TC-FA-RP-983 mengekspektasi respons API (status `403` dan pesan); spec tetap FE+BE dan hanya mengasersi respons dan state data (bagian 8b butir 1).
- Pembagian TC lintas spec: klausa "tidak ada entri log" pada Expected TC-FA-RP-978 diasersi di spec 293; TC-FA-RP-979 sampai TC-FA-RP-982 di spec 294; TC-FA-RP-983 di spec 292 (semuanya kelas g, absence log, dengan aksi nyata dan baseline sendiri). Spec ini mengasersi klausa lain TC tersebut (S-05).
- Spec melewati sekitar 35 langkah (39 langkah). Semua blok satu kelas harness (state tenant Client Suspended) pada akun dan tenant yang sama; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Akun Total Control pada `Client Suspended` (dan `Client Expired` serta Read Only pada `Client Suspended` bila dipakai) tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - Expected b "Kontrol tidak di-disable dan tidak ada tooltip khusus" tidak menyebut kontrol yang dimaksud; spec memakai kontrol yang diklik pada langkah aksi TC itu.
  - Expected "tidak ada perubahan data" tidak menyebut cara memeriksanya; spec memakai kemampuan baca state lewat fixture BE (bukan langkah observasi UI).
  - TC tidak menyebut apakah popup atau dialog tetap terbuka setelah penolakan; spec mengikuti pola penolakan lain di TC (popup atau dialog tetap terbuka dengan seleksi dipertahankan) dan menutupnya dengan `[Cancel]`.
  - TC-FA-RP-980, 981, dan 982 tidak menyebut kontrol yang dimaksud pada Expected b selain toggle, radio, dan `[Assign]`; spec memakai kontrol itu.
