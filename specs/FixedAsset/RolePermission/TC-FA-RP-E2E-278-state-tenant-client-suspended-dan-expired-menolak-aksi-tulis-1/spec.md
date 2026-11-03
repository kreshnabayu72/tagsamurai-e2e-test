---
id: TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1
title: "State tenant: Client Suspended dan Expired menolak aksi tulis (1/3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-969
  - TC-FA-RP-973
  - TC-FA-RP-974
  - TC-FA-RP-975
  - TC-FA-RP-976
  - TC-FA-RP-977
coverage:
  web: automated
---

# State tenant: Client Suspended dan Expired menolak aksi tulis (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1: Read Only pada `Client Suspended` (Pre-setup #25), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_SUSPENDED_RO_PASSWORD` (nama env belum terdaftar di `suite.md`; lihat Temuan untuk QA). Login di hook `before` spec ini (dipakai TC-FA-RP-969 lewat sesi API); halaman dibuka hook `beforeEach` suite.
- Akun aktor 2: Total Control pada `Client Suspended` (Pre-setup #25), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_SUSPENDED_TC_PASSWORD`. Dipakai sesudah ganti akun (langkah 5 sebagai halaman awal). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Env var yang dipakai: `FA_SUSPENDED_RO_PASSWORD`, `FA_SUSPENDED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: #25 (`Client Suspended`), #15 (Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata), #18, #19, #36 (baris Budi Santoso di Tab Total Control, TC-FA-RP-974), dan #39 (Detail Role `Manage accounting` dan `Manage Open API` terisi; baris Citra Lestari dengan Create tercentang). Ahmad Fauzi tidak memegang `Manage Open API` pada TC-FA-RP-976 (Precondition #15) dan tidak memegang penugasan Group Manager pada TC-FA-RP-975; kondisi itu dibuat lewat seeding di hook `before`.
- Kemampuan teknis: klien HTTP untuk request langsung ke server dan sesi API Read Only pada `Client Suspended` (disediakan tim FE/BE; tanpa endpoint karangan). Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): status tingkat akses, baris peran, nilai Require Approval, dan aturan persetujuan dibaca untuk Expected "tidak ada perubahan data" atau nilai akhir.
- State global: status `Client Suspended` tidak diubah spec ini; entitas tetap Suspended sepanjang spec.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-969: Urutan penolakan server, Suspended mendahului penolakan permission biasa

1. Kirim request langsung ke server (bukan lewat UI) dengan sesi API Read Only pada `Client Suspended` untuk mengubah Create baris Ahmad Fauzi pada `Manage accounting`
2. Verifikasi respons status `403` dengan pesan `Changes can't be saved while this workspace is suspended or expired.`
3. Verifikasi pesan permission biasa `You don't have permission to do this.` tidak dipakai
4. Ganti akun: logout, lalu login sebagai Total Control pada `Client Suspended` dengan `Spectra.env.FA_SUSPENDED_TC_PASSWORD`
5. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`

### TC-FA-RP-973: Client Suspended menolak Assign Total Control dengan toast baku

6. Klik `[+ Assign]` di Tab Total Control
7. Centang Dimas Pranata
8. Klik `[Assign]`
9. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
10. Verifikasi kontrol `[Assign]` tidak Disabled dan tidak ada tooltip khusus
11. Verifikasi lewat kemampuan baca Dimas Pranata tidak berstatus Total Control (tidak ada perubahan data)
12. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-974: Client Suspended menolak Remove Total Control dengan toast baku

13. Tunggu toast lama hilang otomatis
14. Klik `[⋯]` baris Budi Santoso lalu `Remove`
15. Klik `[Remove]`
16. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
17. Verifikasi kontrol `[Remove]` tidak Disabled dan tidak ada tooltip khusus
18. Verifikasi lewat kemampuan baca Budi Santoso tetap berstatus Total Control (tidak ada perubahan data)
19. Klik `[Cancel]` pada dialog Remove

### TC-FA-RP-975: Client Suspended menolak Assign Group Manager dengan toast baku

20. Tunggu toast lama hilang otomatis
21. Klik Tab `Group Manager`
22. Klik `[+ Assign]` di Tab Group Manager
23. Pilih group `Data Center`, centang Ahmad Fauzi
24. Klik `[Assign]`
25. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
26. Verifikasi kontrol `[Assign]` tidak Disabled dan tidak ada tooltip khusus
27. Verifikasi lewat kemampuan baca tidak ada penugasan Group Manager Ahmad Fauzi di `Data Center` (tidak ada perubahan data)
28. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-976: Client Suspended menolak Assign User ke Role dengan toast baku

29. Tunggu toast lama hilang otomatis
30. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
31. Klik `[+ Assign]`
32. Centang Ahmad Fauzi
33. Klik `[Assign]`
34. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
35. Verifikasi kontrol `[Assign]` tidak Disabled dan tidak ada tooltip khusus
36. Verifikasi lewat kemampuan baca tidak ada baris baru Ahmad Fauzi pada Detail Role `Manage Open API` (tidak ada perubahan data)
37. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-977: Client Suspended menolak Edit CRUD dengan toast baku

38. Tunggu toast lama hilang otomatis
39. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
40. Hapus centang Create pada baris Citra Lestari
41. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
42. Verifikasi cell Create baris Citra Lestari tidak Disabled dan tidak ada tooltip khusus
43. Verifikasi lewat kemampuan baca Create baris Citra Lestari tetap aktif (tidak ada perubahan data)

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-969, 973, 974, 975, 976, 977).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): ganti akun dan membuka halaman (langkah 4 dan 5); "Tunggu toast lama hilang otomatis" sebelum tiap toast baku yang sama diasersi lagi (R-12); membuka tab dan Detail Role; memilih group dan mencentang kandidat; menutup popup atau dialog dengan `[Cancel]` (langkah 12, 19, 28, 37) agar state tidak dibawa ke TC berikutnya (S-09).
- Urutan TC: TC-FA-RP-969 dijalankan lebih dulu karena akun Read Only login di hook `before` dan satu kali ganti akun menuju Total Control (S-07).
- K-1: TC-FA-RP-969 mengekspektasi respons API (status `403` dan pesan); spec tetap FE+BE dan hanya mengasersi respons (bagian 8b butir 1).
- Pembagian TC lintas spec: klausa "tidak ada entri log" pada Expected c TC-FA-RP-973 sampai TC-FA-RP-977 diasersi di spec 293 (kelas g, absence log) dengan aksi nyata dan baseline sendiri; spec ini mengasersi klausa lain TC tersebut (S-05). TC-FA-RP-969 tidak memuat klausa log.
- Spec melewati sekitar 35 langkah (43 langkah). Semua blok satu kelas harness (state tenant Client Suspended) pada akun dan tenant yang sama; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Memecahnya hanya mengulang hook dan ganti akun.
- Temuan untuk QA:
  - Akun Total Control pada `Client Suspended` (dan `Client Expired` serta Read Only pada `Client Suspended` bila dipakai) tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - TC-FA-RP-969 menyebut "Login sbg Role: Read Only" pada `Client Suspended` tanpa akun atau env password; spec memakai nama env `FA_SUSPENDED_RO_PASSWORD` yang belum terdaftar di `suite.md` dan perlu didaftarkan tim FE.
  - Expected b "Kontrol tidak di-disable dan tidak ada tooltip khusus" tidak menyebut kontrol yang dimaksud; spec memakai kontrol yang diklik pada langkah aksi TC itu.
  - Expected "tidak ada perubahan data" tidak menyebut cara memeriksanya; spec memakai kemampuan baca state lewat fixture BE (bukan langkah observasi UI).
  - TC tidak menyebut apakah popup atau dialog tetap terbuka setelah penolakan; spec mengikuti pola penolakan lain di TC (popup atau dialog tetap terbuka dengan seleksi dipertahankan) dan menutupnya dengan `[Cancel]`.
  - TC-FA-RP-976 memakai Ahmad Fauzi sebagai kandidat Assign ke `Manage Open API` dengan Precondition Pre-setup #15, sedangkan Pre-setup #39 sudah memuat Ahmad Fauzi pada role itu; spec membuat Ahmad Fauzi tanpa penugasan `Manage Open API` lewat seeding. TC-FA-RP-977 tidak menyebut keadaan cell Create di UI sesudah penolakan; spec hanya mengasersi state data.
