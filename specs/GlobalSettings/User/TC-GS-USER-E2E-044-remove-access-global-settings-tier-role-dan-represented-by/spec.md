---
id: TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by
title: "Remove Access Global Settings: Dialog Role & Permission untuk Tier dan Holder N Role, Pencabutan Tier, Relasi Represented By Tetap, dan User Basic Tanpa Dialog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-223
  - TC-GS-USER-224
  - TC-GS-USER-225
  - TC-GS-USER-226
  - TC-GS-USER-227
  - TC-GS-USER-1009
coverage:
  web: automated
---

# Remove Access Global Settings: Dialog Role & Permission untuk Tier dan Holder N Role, Pencabutan Tier, Relasi Represented By Tetap, dan User Basic Tanpa Dialog

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca): Yudi Pratomo (No. 3, tier Read Only, pembanding pada tab Read Only di Role & Permission).
- Data Dinamis (di-seed lewat API di hook `before`, dibersihkan di `after`; menggantikan Andi Wijaya No. 10, Doni Pratama No. 11, Dewi Lestari No. 12, Ahmad Fauzi No. 13, dan Non-Login User No. 21 agar data Pre-setup tidak diubah, S-06):
  - `Andi Wijaya {runId}-044` (email `andiwijaya+{runId}-044@qwertysystem.net`, Activated, tier Total Control, Access `Global Settings`).
  - `Doni Pratama {runId}-044` (email `donipratama+{runId}-044@qwertysystem.net`, Activated, tier Read Only, Access `Fixed Asset` dan `Global Settings`).
  - `Ahmad Fauzi {runId}-044` (email `ahmadfauzi+{runId}-044@qwertysystem.net`, Activated, Access `Global Settings`, tiga role individual aktif di Role & Permission dengan nama bersuffix, bukan tier); Non-Login User `Agus Prasetyo {runId}-044` dengan Represented By `Ahmad Fauzi {runId}-044`.
  - `Dewi Lestari {runId}-044` (email `dewilestari+{runId}-044@qwertysystem.net`, Activated, Basic, Access `Fixed Asset` dan `Global Settings`, tanpa borrowed asset dan tanpa approval).
- Kemampuan teknis: seeding tier dan role individual di Role & Permission lewat API (HK1; nama endpoint ditentukan tim FE di tahap script).
- State global: tier dan role individual di Role & Permission berubah oleh aksi spec; dipulihkan lewat cleanup user seed.
- Cleanup (`after`): hapus empat user seed, Non-Login User seed, dan tiga role individual seed.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-1009: Screening dialog Remove Access Global Settings (tier Total Control)

2. Klik icon Search, ketik `Andi Wijaya {runId}-044`, tekan Enter
3. Klik (⋯) baris `Andi Wijaya {runId}-044` → `Edit`
4. Uncheck Access `Global Settings`
5. Klik `[Save]`
6. Verifikasi dialog Title `Remove Access`
7. Verifikasi body dialog memuat bullet `• Andi Wijaya {runId}-044`
8. Verifikasi body dialog memuat `This user currently has Total Control in Role & Permission. Removing Global Settings access will also revoke it.`
9. Verifikasi body dialog diakhiri pertanyaan `Are you sure you want to remove it?`
10. Verifikasi dialog memuat tombol `[Cancel]` dan `[Remove]`
11. Klik `[Cancel]` pada dialog
12. Klik `✕` pada header Popup Edit
13. Verifikasi dialog `Unsaved Changes`
14. Klik `[Leave]`

### TC-GS-USER-225: Holder dengan N role menyebut jumlah role di dialog

15. Ganti isi kotak search dengan `Ahmad Fauzi {runId}-044`, tekan Enter
16. Klik (⋯) baris `Ahmad Fauzi {runId}-044` → `Edit`
17. Uncheck Access `Global Settings`
18. Klik `[Save]`
19. Verifikasi body dialog menyebut `This user currently has 3 roles in Role & Permission. Removing Global Settings access will also revoke it.`
20. Klik `[Cancel]` pada dialog
21. Klik `✕` pada header Popup Edit
22. Verifikasi dialog `Unsaved Changes`
23. Klik `[Leave]`

### TC-GS-USER-223 dan TC-GS-USER-224: User bertier, dialog Role & Permission lalu lanjut mencabut tier

24. Ganti isi kotak search dengan `Doni Pratama {runId}-044`, tekan Enter
25. Klik (⋯) baris `Doni Pratama {runId}-044` → `Edit`
26. Uncheck Access `Global Settings`
27. Klik `[Save]`
28. Verifikasi body dialog memuat bullet `• Doni Pratama {runId}-044`
29. Verifikasi body dialog memuat `This user currently has Read Only in Role & Permission. Removing Global Settings access will also revoke it. Are you sure you want to remove it?`
30. Klik `[Remove]` pada dialog
31. Verifikasi toast sukses: "Success, user has been updated."
32. Buka Global Settings > Role & Permission > Read Only
33. Verifikasi tab Read Only memuat `Yudi Pratomo` (pembanding)
34. Verifikasi `Doni Pratama {runId}-044` tidak lagi tercantum di tab Read Only
35. Buka Global Settings > User > User List (sub-tab Login User)
36. Klik icon Search, ketik `Doni Pratama {runId}-044`, tekan Enter
37. Verifikasi sel Access baris `Doni Pratama {runId}-044` memuat `Fixed Asset` (tidak terpengaruh)

### TC-GS-USER-227: Remove Access Global Settings mempertahankan relasi Represented By

38. Ganti isi kotak search dengan `Ahmad Fauzi {runId}-044`, tekan Enter
39. Klik (⋯) baris `Ahmad Fauzi {runId}-044` → `Edit`
40. Uncheck Access `Global Settings`
41. Klik `[Save]`
42. Klik `[Remove]` pada dialog
43. Tunggu aksi selesai
44. Klik Name `Ahmad Fauzi {runId}-044` di User List
45. Klik Tab Non-Login User
46. Verifikasi `Agus Prasetyo {runId}-044` tetap tercantum di Tab Non-Login User

### TC-GS-USER-226: User Basic tanpa aset atau approval, tanpa dialog

47. Klik menu User di sidebar Global Settings
48. Klik icon Search, ketik `Dewi Lestari {runId}-044`, tekan Enter
49. Klik (⋯) baris `Dewi Lestari {runId}-044` → `Edit`
50. Uncheck Access `Global Settings`
51. Klik `[Save]`
52. Verifikasi toast sukses: "Success, user has been updated."
53. Verifikasi tidak ada dialog

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Semua TC di spec ini satu topik aksi (Remove Access Global Settings) dan tidak berkelas harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (53 langkah) karena enam TC berada di satu topik aksi dan satu layar (Popup Edit dan dialog Remove Access), dengan user seed berbeda per TC sehingga tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-USER-1009 dan TC-GS-USER-225 (hanya melihat dialog lalu `[Cancel]`) mendahului pencabutan sungguhan; TC-GS-USER-223 digabung dengan TC-GS-USER-224 dalam satu pembukaan Popup Edit (dialog lalu `[Remove]`); TC-GS-USER-227 dan TC-GS-USER-226 berada paling akhir karena keduanya mencabut akses sungguhan (bagian 3 prinsip 5). TC-GS-USER-227 memakai Ahmad Fauzi yang tidak dicabut di TC-GS-USER-225 (hanya `[Cancel]`).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (pembukaan), 2, 15, 24, 36, 38, 48 (Search), 11, 20 (menutup dialog), 12 sampai 14 dan 21 sampai 23 (menutup Popup Edit dirty, S-08), 32 dan 35 (navigasi), 43 (menunggu aksi selesai), 44 sampai 45 dan 47 (navigasi).
- Asersi tambahan di luar Expected TC (S-03): langkah 33 adalah pembanding (anchor) untuk absence `Doni Pratama` di tab Read Only; langkah 37 mengamati Expected c TC-GS-USER-224 di User List.
- Temuan untuk QA:
  - TC-GS-USER-224 Post Condition (entri Changelog Role & Permission dengan Modified By = Siti Nurhaliza bukan System; sesi aktif Doni Pratama diakhiri; terdampak Role & Permission) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-GS-USER-225 menyebut "Ahmad Fauzi punya 3 role individual aktif" sedangkan Tabel Data Uji Pre-setup No. 13 hanya menyebut holder Manage user and role; spec men-seed tiga role individual untuk user seed.
  - TC-GS-USER-227 Expected hanya `Agus Prasetyo`; Lina Marlina (Pre-setup No. 21, Inactive) tidak diasersi.
  - TC-GS-USER-223 sampai 227 dan 1009 menyebut user Pre-setup (No. 10, 11, 12, 13, 21); spec memakai user seed bersuffix agar data Pre-setup tidak diubah (S-06).
  - TC-GS-USER-226 Expected a "Tidak ada dialog" tidak punya langkah pembanding di TC; spec mengasersi toast sukses lebih dulu sebagai anchor.
